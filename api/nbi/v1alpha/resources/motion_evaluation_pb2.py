# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/nbi/v1alpha/resources/motion_evaluation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common import coordinates_pb2 as api_dot_common_dot_coordinates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1api/nbi/v1alpha/resources/motion_evaluation.proto\x12+aalyria.spacetime.api.nbi.v1alpha.resources\x1a\x1c\x61pi/common/coordinates.proto\"\x9d\x02\n\x0e\x43omputedMotion\x12i\n\treference\x18\x01 \x01(\x0b\x32K.aalyria.spacetime.api.nbi.v1alpha.resources.ComputedMotion.ReferenceMotionR\treference\x12>\n\x07motions\x18\x02 \x03(\x0b\x32$.aalyria.spacetime.api.common.MotionR\x07motions\x1a`\n\x0fReferenceMotion\x12\"\n\rmotion_ref_id\x18\x01 \x01(\tR\x0bmotionRefId\x12)\n\x10\x63ommit_timestamp\x18\x02 \x01(\x03R\x0f\x63ommitTimestampBb\n/com.aalyria.spacetime.api.nbi.v1alpha.resourcesZ/aalyria.com/spacetime/api/nbi/v1alpha/resources')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.nbi.v1alpha.resources.motion_evaluation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n/com.aalyria.spacetime.api.nbi.v1alpha.resourcesZ/aalyria.com/spacetime/api/nbi/v1alpha/resources'
  _globals['_COMPUTEDMOTION']._serialized_start=129
  _globals['_COMPUTEDMOTION']._serialized_end=414
  _globals['_COMPUTEDMOTION_REFERENCEMOTION']._serialized_start=318
  _globals['_COMPUTEDMOTION_REFERENCEMOTION']._serialized_end=414
# @@protoc_insertion_point(module_scope)
