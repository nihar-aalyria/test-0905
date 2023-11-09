# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/common/control_beam.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import coordinates_pb2 as api_dot_common_dot_coordinates__pb2
from api.common import network_pb2 as api_dot_common_dot_network__pb2
from api.common import platform_pb2 as api_dot_common_dot_platform__pb2
from api.common import time_pb2 as api_dot_common_dot_time__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/common/control_beam.proto\x12\x1c\x61\x61lyria.spacetime.api.common\x1a\x1c\x61pi/common/coordinates.proto\x1a\x18\x61pi/common/network.proto\x1a\x19\x61pi/common/platform.proto\x1a\x15\x61pi/common/time.proto\x1a\x1egoogle/protobuf/duration.proto\"\xe2\x06\n\nBeamUpdate\x12 \n\x0c\x62\x65\x61m_task_id\x18\x03 \x01(\tR\nbeamTaskId\x12P\n\toperation\x18\x04 \x01(\x0e\x32\x32.aalyria.spacetime.api.common.BeamUpdate.OperationR\toperation\x12\x32\n\x13source_interface_id\x18\x01 \x01(\tB\x02\x18\x01R\x11sourceInterfaceId\x12S\n\x0cinterface_id\x18\n \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x0binterfaceId\x12L\n\x0cradio_config\x18\x0b \x01(\x0b\x32).aalyria.spacetime.api.common.RadioConfigR\x0bradioConfig\x12\x32\n\x13target_interface_id\x18\x02 \x01(\tB\x02\x18\x01R\x11targetInterfaceId\x12M\n\ttarget_id\x18\x08 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x08targetId\x12^\n\x10\x61\x63quisition_info\x18\x05 \x01(\x0b\x32\x33.aalyria.spacetime.api.common.TargetAcquisitionInfoR\x0f\x61\x63quisitionInfo\x12T\n\x0bsignal_info\x18\x0c \x01(\x0b\x32\x33.aalyria.spacetime.api.common.SignalAcquisitionInfoR\nsignalInfo\x12\x41\n\x1dper_interface_sequence_number\x18\x07 \x01(\x03R\x1aperInterfaceSequenceNumber\x12N\n\x15\x65stablishment_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationR\x14\x65stablishmentTimeout\"-\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02J\x08\x08\r\x10\x80\x80\x80\x80\x02J\x04\x08\x06\x10\x07\"\xbe\x02\n\x0bRadioConfig\x12P\n\ntx_channel\x18\x01 \x01(\x0b\x32\x31.aalyria.spacetime.api.common.RadioConfig.ChannelR\ttxChannel\x12P\n\nrx_channel\x18\x02 \x01(\x0b\x32\x31.aalyria.spacetime.api.common.RadioConfig.ChannelR\trxChannel\x12&\n\x0fmodem_config_id\x18\x03 \x01(\tR\rmodemConfigId\x1a\x63\n\x07\x43hannel\x12.\n\x13\x63\x65nter_frequency_hz\x18\x01 \x01(\x04R\x11\x63\x65nterFrequencyHz\x12(\n\x10\x63hannel_width_hz\x18\x02 \x01(\x04R\x0e\x63hannelWidthHz\"f\n\x15SignalAcquisitionInfo\x12M\n$modeled_power_at_receiver_output_dbw\x18\x01 \x01(\x01R\x1fmodeledPowerAtReceiverOutputDbw\"\xf0\x02\n\x15TargetAcquisitionInfo\x12 \n\tlongitude\x18\x03 \x01(\x01\x42\x02\x18\x01R\tlongitude\x12\x1e\n\x08latitude\x18\x04 \x01(\x01\x42\x02\x18\x01R\x08latitude\x12\x1a\n\x06height\x18\x05 \x01(\x01\x42\x02\x18\x01R\x06height\x12\x46\n\x0b\x63oordinates\x18\x0c \x01(\x0b\x32$.aalyria.spacetime.api.common.MotionR\x0b\x63oordinates\x12X\n\x10\x61\x64sb_transponder\x18\t \x01(\x0b\x32-.aalyria.spacetime.api.common.AdsbTransponderR\x0f\x61\x64sbTransponder\x12)\n\x10physical_address\x18\n \x01(\x0cR\x0fphysicalAddressJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\x0b\x10\x0cJ\x08\x08\r\x10\x80\x80\x80\x80\x02\"\xba\x01\n\x08\x42\x65\x61mTask\x12!\n\x0cinterface_id\x18\x01 \x01(\tR\x0binterfaceId\x12\x32\n\x13target_interface_id\x18\x02 \x01(\tB\x02\x18\x01R\x11targetInterfaceId\x12M\n\ttarget_id\x18\x03 \x01(\x0b\x32\x30.aalyria.spacetime.api.common.NetworkInterfaceIdR\x08targetIdJ\x08\x08\x04\x10\x80\x80\x80\x80\x02\"\x8c\x01\n\nBeamStates\x12\x44\n\ttimestamp\x18\x03 \x01(\x0b\x32&.aalyria.spacetime.api.common.DateTimeR\ttimestamp\x12\"\n\rbeam_task_ids\x18\x04 \x03(\tR\x0b\x62\x65\x61mTaskIdsJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x08\x08\x05\x10\x80\x80\x80\x80\x02\x42\x44\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.common.control_beam_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common'
  _BEAMUPDATE.fields_by_name['source_interface_id']._options = None
  _BEAMUPDATE.fields_by_name['source_interface_id']._serialized_options = b'\030\001'
  _BEAMUPDATE.fields_by_name['target_interface_id']._options = None
  _BEAMUPDATE.fields_by_name['target_interface_id']._serialized_options = b'\030\001'
  _TARGETACQUISITIONINFO.fields_by_name['longitude']._options = None
  _TARGETACQUISITIONINFO.fields_by_name['longitude']._serialized_options = b'\030\001'
  _TARGETACQUISITIONINFO.fields_by_name['latitude']._options = None
  _TARGETACQUISITIONINFO.fields_by_name['latitude']._serialized_options = b'\030\001'
  _TARGETACQUISITIONINFO.fields_by_name['height']._options = None
  _TARGETACQUISITIONINFO.fields_by_name['height']._serialized_options = b'\030\001'
  _BEAMTASK.fields_by_name['target_interface_id']._options = None
  _BEAMTASK.fields_by_name['target_interface_id']._serialized_options = b'\030\001'
  _globals['_BEAMUPDATE']._serialized_start=202
  _globals['_BEAMUPDATE']._serialized_end=1068
  _globals['_BEAMUPDATE_OPERATION']._serialized_start=1007
  _globals['_BEAMUPDATE_OPERATION']._serialized_end=1052
  _globals['_RADIOCONFIG']._serialized_start=1071
  _globals['_RADIOCONFIG']._serialized_end=1389
  _globals['_RADIOCONFIG_CHANNEL']._serialized_start=1290
  _globals['_RADIOCONFIG_CHANNEL']._serialized_end=1389
  _globals['_SIGNALACQUISITIONINFO']._serialized_start=1391
  _globals['_SIGNALACQUISITIONINFO']._serialized_end=1493
  _globals['_TARGETACQUISITIONINFO']._serialized_start=1496
  _globals['_TARGETACQUISITIONINFO']._serialized_end=1864
  _globals['_BEAMTASK']._serialized_start=1867
  _globals['_BEAMTASK']._serialized_end=2053
  _globals['_BEAMSTATES']._serialized_start=2056
  _globals['_BEAMSTATES']._serialized_end=2196
# @@protoc_insertion_point(module_scope)
