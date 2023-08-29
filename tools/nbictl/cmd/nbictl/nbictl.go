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

package main

import (
	"context"
	"errors"
	"flag"
	"fmt"
	"os"

	nbictl "aalyria.com/spacetime/github/tools/nbictl"
)

var subCmds = map[string]func(context.Context, []string) error{
	"list":          nbictl.List,
	"create":        nbictl.Create,
	"update":        nbictl.Update,
	"delete":        nbictl.Delete,
	"generate-keys": nbictl.GenerateKeys,
	"set-context":   nbictl.SetContext,
}

var errUsage = fmt.Errorf("expected one of %s", getSubcommandNames())

const (
	linkToAuthGuide = "https://docs.spacetime.aalyria.com/authentication"
	clientName      = "nbictl"
)

func getSubcommandNames() []string {
	var cmdList []string
	for cmd := range subCmds {
		cmdList = append(cmdList, cmd)
	}
	return cmdList
}

func run(args []string) error {
	if len(args) == 0 {
		return fmt.Errorf("no command specified: %w", errUsage)
	}
	cmd, args := args[0], args[1:]
	ctx := context.Background()

	cmdToPerform, ok := subCmds[cmd]
	if !ok {
		return fmt.Errorf("invalid command %q: %w", cmd, errUsage)
	}
	return cmdToPerform(ctx, args)
}

func main() {
	fs := flag.NewFlagSet(clientName, flag.ContinueOnError)
	fs.Usage = func() {
		w := fs.Output()
		fmt.Fprintf(w, "Usage of %s:\n", clientName)
		fmt.Fprintln(w, "")
		fmt.Fprintf(w, "  %s -h | --help\n", clientName)
		for subcmd := range subCmds {
			fmt.Fprintf(w, "  %s %s [-h | --help] [options...]\n", clientName, subcmd)
		}
		fs.PrintDefaults()
	}

	err := fs.Parse(os.Args[1:])
	if err == nil {
		err = run(fs.Args())
	}

	if err != nil && errors.Is(err, flag.ErrHelp) {
		os.Exit(0)
	} else if err != nil && errors.Is(err, errUsage) {
		fmt.Fprintf(os.Stderr, "usage error: %v\n\n", err)
		fs.Usage()
		os.Exit(1)
	} else if err != nil {
		fmt.Fprintf(os.Stderr, "fatal error: %v\n", err)
		os.Exit(2)
	}
}
