# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/common/control_flow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import network_pb2 as api_dot_common_dot_network__pb2
from api.common import time_pb2 as api_dot_common_dot_time__pb2
from api.types import ethernet_pb2 as api_dot_types_dot_ethernet__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/common/control_flow.proto\x12\x1c\x61\x61lyria.spacetime.api.common\x1a\x18\x61pi/common/network.proto\x1a\x15\x61pi/common/time.proto\x1a\x18\x61pi/types/ethernet.proto\"\x94\x02\n\nFlowUpdate\x12 \n\x0c\x66low_rule_id\x18\x01 \x01(\tR\nflowRuleId\x12P\n\toperation\x18\x02 \x01(\x0e\x32\x32.aalyria.spacetime.api.common.FlowUpdate.OperationR\toperation\x12:\n\x04rule\x18\x03 \x01(\x0b\x32&.aalyria.spacetime.api.common.FlowRuleR\x04rule\x12\'\n\x0fsequence_number\x18\x04 \x01(\x03R\x0esequenceNumber\"-\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\"\xb4\x0c\n\x08\x46lowRule\x12N\n\nclassifier\x18\x05 \x01(\x0b\x32..aalyria.spacetime.api.common.PacketClassifierR\nclassifier\x12X\n\raction_bucket\x18\x04 \x03(\x0b\x32\x33.aalyria.spacetime.api.common.FlowRule.ActionBucketR\x0c\x61\x63tionBucket\x1a\xed\n\n\x0c\x41\x63tionBucket\x12R\n\x06\x61\x63tion\x18\x01 \x03(\x0b\x32:.aalyria.spacetime.api.common.FlowRule.ActionBucket.ActionR\x06\x61\x63tion\x1a\x88\n\n\x06\x41\x63tion\x12\x62\n\tset_field\x18\x01 \x01(\x0b\x32\x43.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.SetFieldH\x00R\x08setField\x12^\n\x07\x66orward\x18\x02 \x01(\x0b\x32\x42.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.ForwardH\x00R\x07\x66orward\x12h\n\x0bpush_header\x18\x03 \x01(\x0b\x32\x45.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.PushHeaderH\x00R\npushHeader\x12\x65\n\npop_header\x18\x04 \x01(\x0b\x32\x44.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.PopHeaderH\x00R\tpopHeader\x1a\x8c\x02\n\x08SetField\x12_\n\x05\x66ield\x18\x01 \x01(\x0e\x32I.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.SetField.FieldR\x05\x66ield\x12\x1f\n\x0bvalue_ascii\x18\x03 \x01(\tR\nvalueAscii\"n\n\x05\x46ield\x12\x15\n\x11\x46IELD_UNSPECIFIED\x10\x00\x12\x11\n\rFIELD_ETH_DST\x10\x02\x12\x14\n\x10\x46IELD_MPLS_LABEL\x10\x03\x12\x11\n\rFIELD_VLAN_ID\x10\x04\x12\x12\n\x0e\x46IELD_PBB_ITAG\x10\x05J\x04\x08\x02\x10\x03J\x08\x08\x04\x10\x80\x80\x80\x80\x02\x1a\x33\n\x07\x46orward\x12(\n\x10out_interface_id\x18\x01 \x01(\tR\x0eoutInterfaceId\x1a\x85\x02\n\nPushHeader\x12\x61\n\x05\x66ield\x18\x01 \x01(\x0e\x32K.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.PushHeader.FieldR\x05\x66ield\x12\x45\n\nether_type\x18\x02 \x01(\x0b\x32&.aalyria.spacetime.api.types.EtherTypeR\tetherType\"M\n\x05\x46ield\x12\x15\n\x11\x46IELD_UNSPECIFIED\x10\x00\x12\x0e\n\nFIELD_MPLS\x10\x01\x12\x0e\n\nFIELD_VLAN\x10\x02\x12\r\n\tFIELD_PBB\x10\x03\x1a\x83\x02\n\tPopHeader\x12`\n\x05\x66ield\x18\x01 \x01(\x0e\x32J.aalyria.spacetime.api.common.FlowRule.ActionBucket.Action.PopHeader.FieldR\x05\x66ield\x12\x45\n\nether_type\x18\x02 \x01(\x0b\x32&.aalyria.spacetime.api.types.EtherTypeR\tetherType\"M\n\x05\x46ield\x12\x15\n\x11\x46IELD_UNSPECIFIED\x10\x00\x12\x0e\n\nFIELD_MPLS\x10\x01\x12\x0e\n\nFIELD_VLAN\x10\x02\x12\r\n\tFIELD_PBB\x10\x03\x42\r\n\x0b\x61\x63tion_typeJ\x08\x08\x05\x10\x80\x80\x80\x80\x02J\x04\x08\x01\x10\x04J\x08\x08\x08\x10\x80\x80\x80\x80\x02\"\x85\x01\n\tFlowState\x12\x44\n\ttimestamp\x18\x02 \x01(\x0b\x32&.aalyria.spacetime.api.common.DateTimeR\ttimestamp\x12\"\n\rflow_rule_ids\x18\x03 \x03(\tR\x0b\x66lowRuleIdsJ\x04\x08\x01\x10\x02J\x08\x08\x04\x10\x80\x80\x80\x80\x02\x42\x44\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.common.control_flow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.aalyria.spacetime.api.commonZ aalyria.com/spacetime/api/common'
  _globals['_FLOWUPDATE']._serialized_start=139
  _globals['_FLOWUPDATE']._serialized_end=415
  _globals['_FLOWUPDATE_OPERATION']._serialized_start=370
  _globals['_FLOWUPDATE_OPERATION']._serialized_end=415
  _globals['_FLOWRULE']._serialized_start=418
  _globals['_FLOWRULE']._serialized_end=2006
  _globals['_FLOWRULE_ACTIONBUCKET']._serialized_start=601
  _globals['_FLOWRULE_ACTIONBUCKET']._serialized_end=1990
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION']._serialized_start=702
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION']._serialized_end=1990
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_SETFIELD']._serialized_start=1118
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_SETFIELD']._serialized_end=1386
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_SETFIELD_FIELD']._serialized_start=1260
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_SETFIELD_FIELD']._serialized_end=1370
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_FORWARD']._serialized_start=1388
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_FORWARD']._serialized_end=1439
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_PUSHHEADER']._serialized_start=1442
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_PUSHHEADER']._serialized_end=1703
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_PUSHHEADER_FIELD']._serialized_start=1626
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_PUSHHEADER_FIELD']._serialized_end=1703
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_POPHEADER']._serialized_start=1706
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_POPHEADER']._serialized_end=1965
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_POPHEADER_FIELD']._serialized_start=1626
  _globals['_FLOWRULE_ACTIONBUCKET_ACTION_POPHEADER_FIELD']._serialized_end=1703
  _globals['_FLOWSTATE']._serialized_start=2009
  _globals['_FLOWSTATE']._serialized_end=2142
# @@protoc_insertion_point(module_scope)