# Getting started with Spacetime's APIs

## Spacetime’s two endpoints

Spacetime exposes two primary endpoints through which one can programmatically
interact with the SDN Controller:

1. The Northbound Interface (NBI), located at
   `nbi.spacetime-$INSTANCE_NAME.aalyria.com:443`, and

2. The Control to Data-Plane Interface (CDPI), located at
   `cdpi.spacetime-$INSTANCE_NAME.aalyria.com:443`.

Each serves a distinct purpose. The NBI endpoint provides methods for defining
the network to be orchestrated. Meanwhile, the CDPI endpoint provides methods
through which network devices can receive commands from the SDN controller and
report status back in turn.

## gRPC and Protocol Buffers

Calls to the endpoints can be made using the [gRPC](https://grpc.io/) RPC
framework in combination with
[Protocol Buffers](https://developers.google.com/protocol-buffers/docs/overview)
to serialize requests and responses. In practice, this means that software
applications that interact with the SDN Controller will call out to these
endpoints using client libraries generated by the gRPC framework in your
[language of choice](https://grpc.io/docs/languages/) from our
[interface descriptions](https://github.com/aalyria/api).

> ℹ️ For more info detailing the the creation and usage of these client
> libraries, see the
> [gRPC Basics Tutorial](https://grpc.io/docs/languages/java/basics/).

However, to get started exploring the APIs without first building an entire
application, we can use [`grpcurl`](https://github.com/fullstorydev/grpcurl), a
tool that lets you interact with gRPC servers from the command-line.

## Getting started with `grpcurl`

1. To begin, install `grpcurl`. Installation instructions are available
   [here](https://github.com/fullstorydev/grpcurl#installation).

2. Next, acquire an ID Token from the Google OAuth Token endpoint by following
   the directions laid out
   [here](how-to-authenticate.md).

3. Verify access to the Spacetime APIs. Run:

   ```sh
   grpcurl -H "authorization: Bearer $ID_TOKEN" \
           nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
           list \
           minkowski.nbi.proto.NetOps
   ```

   Which, if successful, should return a list of the methods available on the
   Spacetime NBI’s NetOps service:

   ```console
   minkowski.nbi.proto.NetOps.CesiumVisualization
   minkowski.nbi.proto.NetOps.CreateEntity
   minkowski.nbi.proto.NetOps.DeleteEntity
   minkowski.nbi.proto.NetOps.GenerateHistoricalCzml
   minkowski.nbi.proto.NetOps.ListEntities
   minkowski.nbi.proto.NetOps.ListEntitiesOverTime
   minkowski.nbi.proto.NetOps.ListWeather
   minkowski.nbi.proto.NetOps.UpdateEntity
   ```

4. Finally, we can actually issue a request. Let’s request a list of all of the
   network nodes present in the instance:

   ```sh
   grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
           nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
           minkowski.nbi.proto.NetOps.ListEntities <<EOM
   {"type": "NETWORK_NODE"}
   EOM
   ```

   The `-d @` flag here tells `grpcurl` to read the JSON-formatted request body
   from standard input. Given that this is an invocation of the
   [`minkowski.nbi.proto.NetOps.ListEntities`](https://github.com/aalyria/api/blob/66067e6ca91180b1f7781eb13a32d23e65409473/api/nbi/nbi.proto#L127)
   gRPC method, the request body provided to standard input is a
   [`ListEntitiesRequest`](https://github.com/aalyria/api/blob/66067e6ca91180b1f7781eb13a32d23e65409473/api/nbi/nbi.proto#L198)
   message.

   The results returned will of course depend on the state of the Spacetime
   instance. It is normal for the results to be empty if no network nodes have
   yet been created in the instance.

## "Entities" and the NBI

Interactions with the NBI happen primarily through the manipulation of
"entities", which are persistent mutable resources. Each entity has a "type"
that dictates the nature of the data it holds. For example, we queried for
`NETWORK_NODE`-type entities above. Entity types include `ANTENNA_PATTERN`
entities, `PLATFORM_DEFINITION` entities, `ROUTE_PROVISION` entities, among
others. The complete list of types can be found in our NBI interface
description
[here](https://github.com/aalyria/api/blob/66067e6ca91180b1f7781eb13a32d23e65409473/api/nbi/nbi.proto#L39).

By manipulating these entities we can do things such as configure the SDN
Controller with the properties of the networks it is orchestrating, or request
that traffic be routed across that network.

### Entity commit timestamps and optimistic concurrency control

Each version of an entity is automatically assigned a "commit timestamp".
Spacetime assigns a commit timestamp to each entity upon creating it, and that
commit timestamp is automatically changed to a new, unique value each time the
entity is updated.

Commit timestamps play an important role in Spacetime’s
[optimistic concurrency control](https://en.wikipedia.org/wiki/Optimistic_concurrency_control).
When updating or deleting an entity one must provide the commit timestamp of
the version of the entity being modified. If Spacetime finds that the provided
commit timestamp does not match the commit timestamp of the entity being
modified, it will reject the change. Such an occurrence indicates that another
user has modified the entity concurrently, and the rejection is intended to
prevent accidental overwriting of the other user’s changes.

### In action

To see this in action, let’s create, update, and then delete a `NETWORK_NODE`
entity.

1. Create a new `NETWORK_NODE` entity using the
   `minkowski.nbi.proto.NetOps.CreateEntity` gRPC method

   > ℹ️ The network node created here is functionally useless. It does not have
   > any network interfaces attached. However it will do for now as a means to
   > explore the entity lifecycle.

   ```sh
   grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
           nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
          minkowski.nbi.proto.NetOps.CreateEntity <<EOM
   {
     "type": "NETWORK_NODE",
     "entity": {
       "networkNode": {
         "name": "my-node"
       }
     }
   }
   EOM
   ```

   Spacetime will respond with the created entity. It should look something like:

   ```json
   {
     "group": {
       "type": "NETWORK_NODE",
       "appId": "Minkowski NetOps"
     },
     "id": "7bccb866-a7b6-45b0-9839-7831432e2387",
     "commitTimestamp": "1666726189348545",
     "networkNode": {
       "name": "my-node"
     }
   }
   ```

   Note that Spacetime has assigned the entity an ID and a commit timestamp.

2. Now, let's modify the network node entity by invoking the
   `minkowski.nbi.proto.NetOps.UpdateEntity` gRPC method. We'll attach a
   network interface to the network node entity. Recall that, for concurrency
   control, we must provide the commit timestamp of the entity version we are
   overwriting. This yields an invocation that looks like:

   ```sh
   grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
           nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
           minkowski.nbi.proto.NetOps.UpdateEntity <<EOM
   {
     "type": "NETWORK_NODE",
     "id": "7bccb866-a7b6-45b0-9839-7831432e2387",
     "entity": {
       "commitTimestamp": 1666726189348545,
       "networkNode": {
         "name": "my-node",
         "nodeInterface": [
           {
             "interfaceId": "eth0",
             "wired": {

             }
          }
         ]
       }
     }
   }
   EOM
   ```

   Spacetime should then respond with the updated entity, something like:

   ```json
   {
     "group": {
       "type": "NETWORK_NODE",
       "appId": "Minkowski NetOps"
     },
     "id": "7bccb866-a7b6-45b0-9839-7831432e2387",
     "commitTimestamp": "1666754275124662",
     "networkNode": {
       "name": "my-node",
       "nodeInterface": [
         {
           "interfaceId": "eth0",
           "wired": {
             "maxDataRateBps": 1e9
           }
         }
       ]
     }
   }
   ```

   Note that Spacetime has changed the entity's commit timestamp to reflect the
   new revision of the entity.

3. Finally, we can delete the network node entity by invoking the
   `minkowski.nbi.proto.NetOps.DeleteEntity` gRPC method. Once more, we must
   include the commit timestamp of the entity we are modifying:

   ```sh
   grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
           nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
           minkowski.nbi.proto.NetOps.DeleteEntity <<EOM
   {
     "type": "NETWORK_NODE",
     "id": "7bccb866-a7b6-45b0-9839-7831432e2387",
     "commitTimestamp": "1666754275124662"
   }
   EOM
   ```

## Defining a network

> 🚧 TODO include a screenshot of the complete network.

The entity types essential for defining a network are:

- `PLATFORM_DEFINITION` entities, which define instances of physical
  objects ("platforms") in the network (satellites, ships, or aircraft, for
  instance). The entities specify attributes of the platforms, including their
  motion, and any wireless transceivers mounted on the platforms.
  [🔗&nbsp;https://github.com/aalyria/api/blob/main/api/common/platform.proto]

- `ANTENNA_PATTERN` entities, which define any three-dimensional antenna
  [radiation patterns](https://en.wikipedia.org/wiki/Radiation_pattern) needed
  to describe the radiation or receiving properties of any antennas in the
  network.
  [🔗&nbsp;https://github.com/aalyria/api/blob/main/api/nbi/antenna_pattern.proto]

- `BAND_PROFILE` entities, which define the wireless frequency bands with which
  the network's transceivers are compatible.
  [🔗&nbsp;https://github.com/aalyria/api/blob/main/api/common/channel.proto]

- `NETWORK_NODE` entities, which define the logical network devices in the
  network and their attributes, including IP addresses and subnets.
  [🔗&nbsp;https://github.com/aalyria/api/blob/main/api/nbi/network_element.proto]

- `INTERFACE_LINK_REPORT` entities, which define the static links in the
  network. Most typically these are used to define a terrestrial network
  topology.
  [🔗&nbsp;https://github.com/aalyria/api/blob/main/api/nbi/network_link.proto]

We can employ the `CreateEntity`, `UpdateEntity`, and `DeleteEntity` operations
on entities of these types to define networks in Spacetime. As an example,
let's define a simple network composed of a satellite, a user terminal, a
gateway, and a
[point of presence (PoP)](https://en.wikipedia.org/wiki/Point_of_presence).

The user terminal and gateway will each have a single transmitter and receiver.
The satellite will have two: one for the user link and one for the gateway
link.

### Defining a band profile

First we'll create a `BAND_PROFILE` representing a wireless band made up of
250 MHz-wide channels. This will define the wireless medium to be used by the
wireless links in our network. In the same entity we must also define a "rate
table" specifying how the capacity of a link in this band depends on the
[SNIR](https://en.wikipedia.org/wiki/Signal-to-interference-plus-noise_ratio)
at a receiver.

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "BAND_PROFILE",
  "entity": {
    "bandProfile": {
      "channelWidthHz": 250000000,
      "rateTable": {
        "step": [
          {
            "minCarrierToNoisePlusInterferenceDb": -100,
            "txDataRateBps": 1e8
          },
          {
            "minCarrierToNoisePlusInterferenceDb": -90,
            "txDataRateBps": 2e8
          },
          {
            "minCarrierToNoisePlusInterferenceDb": -80,
            "txDataRateBps": 3e8
          }
        ]
      }
    }
  }
}
EOM
```

Hold on to the entity's ID as `BAND_PROFILE_ID`; we'll need it later.

### Defining antenna patterns

Next, we can use antenna patterns to define how radiation is emitted or
received from the antennas in the network. For now, we'll assume that all
antennas in our network are identical, so a single antenna pattern is sufficient:

> ℹ️ In the interest of simplicity, we'll assume our antennas are all
> [parabolic](https://en.wikipedia.org/wiki/Parabolic_antenna), though
> Spacetime supports arbitrary
> [user-defined radiation patterns](https://github.com/aalyria/api/blob/66067e6ca91180b1f7781eb13a32d23e65409473/api/nbi/antenna_pattern.proto#L19).

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "ANTENNA_PATTERN",
  "entity": {
    "antennaPattern": {
      "parabolicPattern": {
        "diameterM": 1,
        "efficiencyPercent":0.9,
        "backlobeGainDb":-60
      }
    }
  }
}
EOM
```

Save this entity's ID, we'll refer to it in the future as `ANTENNA_PATTERN_ID`.

### Defining the user terminal

We can now begin defining the network assets themselves. The user terminal,
gateway, and satellite will each be defined by a combination of two entities:
(1) `PLATFORM_DEFINITION` entity defining the physical characteristics of the
asset and (2) a `NETWORK_NODE` entity defining the logical network attributes
of the asset.

To define the user terminal, we first create its `PLATFORM_DEFINITION`
entity:

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "PLATFORM_DEFINITION",
  "entity": {
    "platform": {
      "name": "user-terminal",
      "coordinates": {
        "geodeticWgs84": {
          "longitudeDeg": -121.7,
          "latitudeDeg": 37.7
        }
      },
      "transceiverModel": [
        {
          "id": "transceiver-model",
          "transmitter": {
            "name": "tx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "channel": {
                  "11000000000": {
                    "maxPowerWatts": 100
                  }
                }
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "receiver": {
            "name": "rx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "centerFrequencyHz": [
                  "12000000000",
                ]
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "antenna": {
            "name": "antenna",
            "antennaPatternId": "$ANTENNA_PATTERN_ID",
            "targeting": {

            }
          }
        }
      ]
    }
  }
}
EOM
```

This entity is verbose, but it is fairly simple. In short, it
specifies that:

- The user terminal is placed on the ground in Livermore, California.
- The user terminal has a single transceiver, operating in the band we defined
  earlier (note the `$BAND_PROFILE_ID` reference).
- The transmitter is capable of operating at 11 Ghz, while the receiver
  operates at 12 GHz.
- The transmit and receive signal chains each contain a low-noise amplifier.
- The attached antenna exihibits the radiation properties of a 1 meter
  parabolic dish as defined earlier (note the `$ANTENNA_PATTERN_ID` reference).
- The attached antenna is steerable.

Save this entity's ID as `USER_TERMINAL_PLATFORM_ID`.

Now we define the user terminal's `NETWORK_NODE` to represent its logical
network representation.

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "NETWORK_NODE",
  "entity": {
    "networkNode": {
      "name": "user-terminal",
      "nodeInterface": [
        {
          "interfaceId": "wireless",
          "wireless": {
            "transceiverModelId": {
              "platformId": "$USER_TERMINAL_PLATFORM_ID",
              "transceiverModelId": "transceiver-model"
            }
          }
        }
      ],
      "subnet": [
        "fd00:0:0:2a:0:0:0:0/64"
      ]
    },
  }
}
EOM
```

This entity declares a network node with a single interface, and ties the
interface to the user terminal's transceiver. This means that the interface's
connectivity is determined by the connectivity of the transceiver.

Save this entity's ID as `USER_TERMINAL_NETWORK_NODE`.

And with that, our user terminal is complete. We'll follow a similar process
for the remaining assets.

### Defining the gateway

The gateway is much like the user terminal except that:

- Its location is different.
- In addition to its wireless interface, it also has a WAN-facing wired
  interface attached.

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "PLATFORM_DEFINITION",
  "entity": {
    "platform": {
      "name": "gateway",
      "coordinates": {
        "geodeticWgs84": {
          "longitudeDeg": -122.1,
          "latitudeDeg": 37.4
        }
      },
      "transceiverModel": [
        {
          "id": "transceiver-model",
          "transmitter": {
            "name": "tx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "channel": {
                  "13000000000": {
                    "maxPowerWatts": 100
                  }
                }
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "receiver": {
            "name": "rx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "centerFrequencyHz": [
                  "14000000000",
                ]
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "antenna": {
            "name": "antenna",
            "antennaPatternId": "$ANTENNA_PATTERN_ID",
            "targeting": {

            }
          }
        }
      ]
    }
  }
}
EOM
```

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "NETWORK_NODE",
  "entity": {
    "networkNode": {
      "name": "gateway",
      "nodeInterface": [
        {
          "interfaceId": "wireless",
          "wireless": {
            "transceiverModelId": {
            "platformId": "$GATEWAY_PLATFORM_ID",
              "transceiverModelId": "transceiver-model"
            }
          }
        },
        {
          "interfaceId": "wan",
          "wired": {

          }
        }
      ]
    },
  }
}
EOM
```

### Defining the satellite

The configuration required to define a satellite is not dramatically different
from that required to define a user terminal or gateway. Among them the
satellite is unique however in that:

- It has two transceivers: one for the user link and one for the gateway link.
- It is in orbit.

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "PLATFORM_DEFINITION",
  "entity": {
    "platform": {
      "name": "sat",
      "coordinates": {
        "tle": {
          "line1": "1 25544U 98067A   22300.17251634  .00011552  00000-0  21405-3 0  9995",
          "line2": "2 25544  51.6439  42.7225 0005918   8.7497  61.6745 15.49455110365659"
        }
      },
      "transceiverModel": [
        {
          "id": "user-link-transceiver-model",
          "transmitter": {
            "name": "tx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "channel": {
                  "12000000000": {
                    "maxPowerWatts": 100
                  }
                }
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "receiver": {
            "name": "rx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "centerFrequencyHz": [
                  "11000000000",
                ]
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "antenna": {
            "name": "antenna",
            "antennaPatternId": "$ANTENNA_PATTERN_ID",
            "targeting": {

            }
          }
        },
        {
          "id": "gateway-link-transceiver-model",
          "transmitter": {
            "name": "tx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "channel": {
                  "14000000000": {
                    "maxPowerWatts": 100
                  }
                }
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "receiver": {
            "name": "rx",
            "channelSet": {
              "$BAND_PROFILE_ID": {
                "centerFrequencyHz": [
                  "13000000000",
                ]
              }
            },
            "signalProcessingStep": [
              {
                "amplifier": {
                  "constantGain": {
                    "gainDb": 10,
                    "noiseFactor": 1,
                    "referenceTemperatureK": 290
                  }
                }
              }
            ]
          },
          "antenna": {
            "name": "antenna",
            "antennaPatternId": "$ANTENNA_PATTERN_ID",
            "targeting": {

            }
          }
        }
      ]
    }
  }
}
EOM
```

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "NETWORK_NODE",
  "entity": {
    "networkNode": {
      "name": "sat",
      "nodeInterface": [
        {
          "interfaceId": "user-link",
          "wireless": {
            "transceiverModelId": {
              "platformId": "$SATELLITE_PLATFORM_ID",
              "transceiverModelId": "user-link-transceiver-model"
            }
          }
        },
        {
          "interfaceId": "gateway-link",
          "wireless": {
            "transceiverModelId": {
              "platformId": "$SATELLITE_PLATFORM_ID",
              "transceiverModelId": "gateway-link-transceiver-model"
            }
          }
        }
      ]
    },
  }
}
EOM
```

### Defining the terrestrial network

Finally, let's define the terrestrial network. The network is to be made up of
a point of presence (PoP) connected to the gateway by a terrestrial link. It is
worth noting that while the user terminal, gateway, and satellite were all
defined using a combination of a `PLATFORM_DEFINITION` entities and
`NETWORK_NODE` entities, the PoP can be defined without a `PLATFORM_DEFINITON`
at all. This is because the PoP has no wireless interfaces, so connectivity to
the PoP is not impacted by the physical attributes one might specify in a
`PLATFORM_DEFINITION`.

We begin with the PoP's `NETWORK_NODE`:

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "NETWORK_NODE",
  "entity": {
    "networkNode": {
      "name": "pop",
      "nodeInterface": [
        {
          "interfaceId": "wan",
          "wired": {

          }
        }
      ]
    },
  }
}
EOM
```

And then we can add the terrestrial links. One from the PoP to the gateway:

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "INTERFACE_LINK_REPORT",
  "entity": {
    "interfaceLinkReport": {
      "links": [
        {
          "accessIntervals": [
            {
              "accessibility": "ACCESS_EXISTS",
              "sampledMetrics": [
                {
                  "dataRateBps": 1e+11
                }
              ]
            }
          ],
          "dst": {
            "nodeId": "$GATEWAY_NETWORK_NODE_ID",
            "interfaceId": "wan"
          }
        }
      ],
      "src": {
        "nodeId": "$POP_NETWORK_NODE_ID",
        "interfaceId": "wan"
      }
    }
  }
}
EOM
```

and then another in the opposite direction:

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "INTERFACE_LINK_REPORT",
  "entity": {
    "interfaceLinkReport": {
      "links": [
        {
          "accessIntervals": [
            {
              "accessibility": "ACCESS_EXISTS",
              "sampledMetrics": [
                {
                  "dataRateBps": 1e+11
                }
              ]
            }
          ],
          "dst": {
            "nodeId": "$POP_NETWORK_NODE_ID",
            "interfaceId": "wan"
          }
        }
      ],
      "src": {
        "nodeId": "$GATEWAY_NETWORK_NODE_ID",
        "interfaceId": "wan"
      }
    }
  }
}
EOM
```

and with that, we've completed our definition of a minimal network.

## Requesting a service

Spacetime orchestrates a network with the objective of satisfying or fulfilling
services requested of the network. So, to see Spacetime's orchestration in
action, we must issue a service request. This can be accomplished by creating a
`ROUTE_PROVISION` entity. Let's request service between the user terminal and
the PoP:

```sh
grpcurl -d @ -H "authorization: Bearer $ID_TOKEN" \
        nbi.spacetime-$INSTANCE_NAME.aalyria.com:443 \
      minkowski.nbi.proto.NetOps.CreateEntity <<EOM
{
  "type": "ROUTE_PROVISION",
  "entity": {
    "routeProvision": {
      "srcElementIds": [
        "$USER_TERMINAL_NETWORK_NODE_ID"
      ],
      "dstElementIds": [
        "$POP_NETWORK_NODE_ID"
      ],
      "requirements": [
        {
          "bandwidthBpsRequested": 1e+06
        }
      ],
    },
  }
}
EOM
```

## The CDPI

> 🚧 TODO