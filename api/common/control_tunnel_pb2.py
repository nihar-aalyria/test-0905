# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/common/control_tunnel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import network_pb2 as api_dot_common_dot_network__pb2
from api.common import time_pb2 as api_dot_common_dot_time__pb2
from api.common import tunnel_pb2 as api_dot_common_dot_tunnel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/common/control_tunnel.proto\x12\x1c\x61\x61lyria.spacetime.api.common\x1a\x18\x61pi/common/network.proto\x1a\x15\x61pi/common/time.proto\x1a\x17\x61pi/common/tunnel.proto\"\x9e\x02\n\x0cTunnelUpdate\x12$\n\x0etunnel_rule_id\x18\x01 \x01(\tR\x0ctunnelRuleId\x12R\n\toperation\x18\x02 \x01(\x0e\x32\x34.aalyria.spacetime.api.common.TunnelUpdate.OperationR\toperation\x12<\n\x04rule\x18\x03 \x01(\x0b\x32(.aalyria.spacetime.api.common.TunnelRuleR\x04rule\x12\'\n\x0fsequence_number\x18\x04 \x01(\x03R\x0esequenceNumber\"-\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\"\xda\x05\n\nTunnelRule\x12Q\n\nencap_rule\x18\n \x01(\x0b\x32\x32.aalyria.spacetime.api.common.TunnelRule.EncapRuleR\tencapRule\x12Q\n\ndecap_rule\x18\x0b \x01(\x0b\x32\x32.aalyria.spacetime.api.common.TunnelRule.DecapRuleR\tdecapRule\x1a\xf2\x02\n\tEncapRule\x12N\n\nclassifier\x18\x01 \x01(\x0b\x32..aalyria.spacetime.api.common.PacketClassifierR\nclassifier\x12.\n\x13\x65ncapsulated_src_ip\x18\x02 \x01(\tR\x11\x65ncapsulatedSrcIp\x12.\n\x13\x65ncapsulated_dst_ip\x18\x03 \x01(\tR\x11\x65ncapsulatedDstIp\x12\x32\n\x15\x65ncapsulated_src_port\x18\x04 \x01(\x05R\x13\x65ncapsulatedSrcPort\x12\x32\n\x15\x65ncapsulated_dst_port\x18\x05 \x01(\x05R\x13\x65ncapsulatedDstPort\x12?\n\x03\x65sp\x18\x06 \x01(\x0b\x32+.aalyria.spacetime.api.common.EspParametersH\x00R\x03\x65spB\x0c\n\nparameters\x1a\xaa\x01\n\tDecapRule\x12N\n\nclassifier\x18\x01 \x01(\x0b\x32..aalyria.spacetime.api.common.PacketClassifierR\nclassifier\x12?\n\x03\x65sp\x18\x02 \x01(\x0b\x32+.aalyria.spacetime.api.common.EspParametersH\x00R\x03\x65spB\x0c\n\nparametersJ\x04\x08\x01\x10\n\"\x8c\x01\n\x0cTunnelStates\x12\x44\n\ttimestamp\x18\x02 \x01(\x0b\x32&.aalyria.spacetime.api.common.DateTimeR\ttimestamp\x12&\n\x0ftunnel_rule_ids\x18\x03 \x03(\tR\rtunnelRuleIdsJ\x04\x08\x01\x10\x02J\x08\x08\x04\x10\x80\x80\x80\x80\x02\x42\x44\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.common.control_tunnel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common'
  _globals['_TUNNELUPDATE']._serialized_start=140
  _globals['_TUNNELUPDATE']._serialized_end=426
  _globals['_TUNNELUPDATE_OPERATION']._serialized_start=381
  _globals['_TUNNELUPDATE_OPERATION']._serialized_end=426
  _globals['_TUNNELRULE']._serialized_start=429
  _globals['_TUNNELRULE']._serialized_end=1159
  _globals['_TUNNELRULE_ENCAPRULE']._serialized_start=610
  _globals['_TUNNELRULE_ENCAPRULE']._serialized_end=980
  _globals['_TUNNELRULE_DECAPRULE']._serialized_start=983
  _globals['_TUNNELRULE_DECAPRULE']._serialized_end=1153
  _globals['_TUNNELSTATES']._serialized_start=1162
  _globals['_TUNNELSTATES']._serialized_end=1302
# @@protoc_insertion_point(module_scope)
