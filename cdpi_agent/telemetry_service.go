// Copyright 2023 Aalyria Technologies, Inc., and its affiliates.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package agent

import (
	"context"

	afpb "aalyria.com/spacetime/api/cdpi/v1alpha"
	"aalyria.com/spacetime/cdpi_agent/internal/channels"
	"aalyria.com/spacetime/cdpi_agent/internal/loggable"
	"aalyria.com/spacetime/cdpi_agent/internal/task"
	"aalyria.com/spacetime/cdpi_agent/telemetry"

	"github.com/rs/zerolog"
	"golang.org/x/sync/errgroup"
)

type telemetryService struct {
	nc              *nodeController
	telemetryClient afpb.NetworkTelemetryStreamingClient
	tb              telemetry.Backend
}

func (nc *nodeController) newTelemetryService(tc afpb.NetworkTelemetryStreamingClient, tb telemetry.Backend) task.Task {
	return (&telemetryService{nc: nc, telemetryClient: tc, tb: tb}).run
}

func (ts *telemetryService) run(ctx context.Context) error {
	g, ctx := errgroup.WithContext(ctx)

	ti, err := ts.telemetryClient.TelemetryInterface(ctx)
	if err != nil {
		return err
	}

	// sendCh contains the messages queued to send over the gRPC stream
	sendCh := make(chan *afpb.TelemetryUpdate)
	// recvCh contains the messages received over the gRPC stream
	recvCh := make(chan *afpb.TelemetryRequest)
	// triggerCh contains empty messages that trigger sending a TelemetryUpdate
	// via the sendCh.
	triggerCh := make(chan struct{})

	g.Go(channels.NewSource(sendCh).ForwardTo(ti.Send).
		WithStartingStoppingLogs("sendLoop", zerolog.TraceLevel).
		WithLogField("task", "send").
		WithCtx(ctx))

	g.Go(channels.NewSink(recvCh).FillFrom(ti.Recv).
		WithStartingStoppingLogs("recvLoop", zerolog.TraceLevel).
		WithLogField("task", "recv").
		WithCtx(ctx))

	g.Go(ts.statLoop(triggerCh, sendCh).
		WithStartingStoppingLogs("statLoop", zerolog.TraceLevel).
		WithLogField("task", "stat").
		WithCtx(ctx))

	g.Go(ts.mainLoop(triggerCh, recvCh).
		WithStartingStoppingLogs("mainLoop", zerolog.TraceLevel).
		WithLogField("task", "main").
		WithCtx(ctx))

	triggerCh <- struct{}{}

	err = g.Wait()
	zerolog.Ctx(ctx).Trace().Err(err).Msg("service finished")
	return err
}

// statLoop reads values from `triggerCh`, generates telemetry updates, then
// forwards them to the `sendCh`.
func (ts *telemetryService) statLoop(triggerCh <-chan struct{}, sendCh chan<- *afpb.TelemetryUpdate) task.Task {
	mapFn := func(ctx context.Context, _ struct{}) (*afpb.TelemetryUpdate, error) {
		zerolog.Ctx(ctx).Trace().Msg("got trigger")
		report, err := ts.tb(ctx)
		if err != nil {
			return nil, err
		}
		zerolog.Ctx(ctx).Trace().
			Object("report", loggable.Proto(report)).
			Msg("generated stats report")

		return &afpb.TelemetryUpdate{Type: &afpb.TelemetryUpdate_Statistics{Statistics: report}}, nil
	}

	return channels.MapBetween(triggerCh, sendCh, mapFn)
}

// mainLoop processes incoming telemetry requests and manages triggering stats
// generation for both periodic and one-off requests.
func (ts *telemetryService) mainLoop(triggerCh chan<- struct{}, recvCh <-chan *afpb.TelemetryRequest) task.Task {
	return func(ctx context.Context) error {
		log := zerolog.Ctx(ctx)
		ticker := newReusableTicker(ts.nc.clock)

		for {
			select {
			case <-ctx.Done():
				return context.Cause(ctx)

			case <-ticker.Chan():
				log.Trace().Msg("triggering periodic report generation")
				triggerCh <- struct{}{}

			case req := <-recvCh:
				if req.GetNodeId() != ts.nc.id {
					log.Warn().
						Str("requestedID", req.GetNodeId()).
						Object("req", loggable.Proto(req)).
						Msg("got mismatched node ID in telemetry request")
					continue
				}

				switch req.Type.(type) {
				case *afpb.TelemetryRequest_QueryStatistics:
					log.Trace().Msg("triggering one-off report generation")
					triggerCh <- struct{}{}

				case *afpb.TelemetryRequest_StatisticsPublishRateHz:
					newHz := req.GetStatisticsPublishRateHz()
					log.Trace().Float64("hz", newHz).Msg("updating publish rate")

					if newHz > 0 {
						dur := hzToDuration(newHz)
						ticker.Start(dur)
					} else {
						ticker.Stop()
					}

				default:
					log.Warn().
						Object("req", loggable.Proto(req)).
						Msg("unknown telemetry request type received")
				}
			}
		}
	}
}