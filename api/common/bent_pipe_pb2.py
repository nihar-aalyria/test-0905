# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/common/bent_pipe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import platform_antenna_pb2 as api_dot_common_dot_platform__antenna__pb2
from api.common import wireless_pb2 as api_dot_common_dot_wireless__pb2
from api.common import wireless_receiver_pb2 as api_dot_common_dot_wireless__receiver__pb2
from api.common import wireless_transmitter_pb2 as api_dot_common_dot_wireless__transmitter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/common/bent_pipe.proto\x12\x1c\x61\x61lyria.spacetime.api.common\x1a!api/common/platform_antenna.proto\x1a\x19\x61pi/common/wireless.proto\x1a\"api/common/wireless_receiver.proto\x1a%api/common/wireless_transmitter.proto\"\xc3\x0e\n\x0f\x42\x65ntPipePayload\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x64\n\x08\x61ntennas\x18\x02 \x03(\x0b\x32H.aalyria.spacetime.api.common.BentPipePayload.AntennaAndSignalProcessorsR\x08\x61ntennas\x12_\n\rfixed_payload\x18\x03 \x01(\x0b\x32:.aalyria.spacetime.api.common.BentPipePayload.FixedPayloadR\x0c\x66ixedPayload\x12\x65\n\x0f\x64igital_payload\x18\x04 \x01(\x0b\x32<.aalyria.spacetime.api.common.BentPipePayload.DigitalPayloadR\x0e\x64igitalPayload\x12;\n\x1amax_processed_bandwidth_hz\x18\x05 \x01(\rR\x17maxProcessedBandwidthHz\x12!\n\x0cmax_channels\x18\x06 \x01(\rR\x0bmaxChannels\x1a\x86\x04\n\x1a\x41ntennaAndSignalProcessors\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12I\n\x07\x61ntenna\x18\x02 \x01(\x0b\x32/.aalyria.spacetime.api.common.AntennaDefinitionR\x07\x61ntenna\x12s\n\x1atransmit_signal_processors\x18\x03 \x03(\x0b\x32\x35.aalyria.spacetime.api.common.TransmitSignalProcessorR\x18transmitSignalProcessors\x12p\n\x19receive_signal_processors\x18\x04 \x03(\x0b\x32\x34.aalyria.spacetime.api.common.ReceiveSignalProcessorR\x17receiveSignalProcessors\x12p\n\tdirection\x18\x05 \x01(\x0e\x32R.aalyria.spacetime.api.common.BentPipePayload.AntennaAndSignalProcessors.DirectionR\tdirection\"4\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x05\n\x01\x41\x10\x01\x12\x05\n\x01\x42\x10\x02\x1a\xab\x04\n\x0c\x46ixedPayload\x12^\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x42.aalyria.spacetime.api.common.BentPipePayload.FixedPayload.ChannelR\x08\x63hannels\x12\x86\x01\n\x16\x63hannel_configurations\x18\x03 \x03(\x0b\x32O.aalyria.spacetime.api.common.BentPipePayload.FixedPayload.ChannelConfigurationR\x15\x63hannelConfigurations\x1a\x9f\x01\n\x07\x43hannel\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12<\n\x06signal\x18\x02 \x01(\x0b\x32$.aalyria.spacetime.api.common.SignalR\x06signal\x12\x46\n antenna_and_signal_processors_id\x18\x03 \x01(\tR\x1c\x61ntennaAndSignalProcessorsId\x1a\x8f\x01\n\x14\x43hannelConfiguration\x12(\n\x10input_channel_id\x18\x01 \x01(\tR\x0einputChannelId\x12*\n\x11output_channel_id\x18\x02 \x01(\tR\x0foutputChannelId\x12!\n\x0c\x62\x61ndwidth_hz\x18\x03 \x01(\x01R\x0b\x62\x61ndwidthHz\x1a\xda\x02\n\x0e\x44igitalPayload\x12\x33\n\x16min_input_frequency_hz\x18\x01 \x01(\x04R\x13minInputFrequencyHz\x12\x33\n\x16max_input_frequency_hz\x18\x02 \x01(\x04R\x13maxInputFrequencyHz\x12\x35\n\x17min_output_frequency_hz\x18\x03 \x01(\x04R\x14minOutputFrequencyHz\x12\x35\n\x17max_output_frequency_hz\x18\x04 \x01(\x04R\x14maxOutputFrequencyHz\x12\x37\n\x18min_channel_bandwidth_hz\x18\x05 \x01(\x04R\x15minChannelBandwidthHz\x12\x37\n\x18max_channel_bandwidth_hz\x18\x06 \x01(\x04R\x15maxChannelBandwidthHzBD\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.common.bent_pipe_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common'
  _globals['_BENTPIPEPAYLOAD']._serialized_start=198
  _globals['_BENTPIPEPAYLOAD']._serialized_end=2057
  _globals['_BENTPIPEPAYLOAD_ANTENNAANDSIGNALPROCESSORS']._serialized_start=632
  _globals['_BENTPIPEPAYLOAD_ANTENNAANDSIGNALPROCESSORS']._serialized_end=1150
  _globals['_BENTPIPEPAYLOAD_ANTENNAANDSIGNALPROCESSORS_DIRECTION']._serialized_start=1098
  _globals['_BENTPIPEPAYLOAD_ANTENNAANDSIGNALPROCESSORS_DIRECTION']._serialized_end=1150
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD']._serialized_start=1153
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD']._serialized_end=1708
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD_CHANNEL']._serialized_start=1403
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD_CHANNEL']._serialized_end=1562
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD_CHANNELCONFIGURATION']._serialized_start=1565
  _globals['_BENTPIPEPAYLOAD_FIXEDPAYLOAD_CHANNELCONFIGURATION']._serialized_end=1708
  _globals['_BENTPIPEPAYLOAD_DIGITALPAYLOAD']._serialized_start=1711
  _globals['_BENTPIPEPAYLOAD_DIGITALPAYLOAD']._serialized_end=2057
# @@protoc_insertion_point(module_scope)
