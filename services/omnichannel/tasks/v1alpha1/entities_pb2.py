# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/omnichannel/tasks/v1alpha1/entities.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'services/omnichannel/tasks/v1alpha1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2services/omnichannel/tasks/v1alpha1/entities.proto\x12#services.omnichannel.tasks.v1alpha1\x1a\x1d\x61pi/commons/omnichannel.proto\"3\n\x12\x43\x61ncelTasksRequest\x12\x1d\n\x08task_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\x07taskSid\"\x15\n\x13\x43\x61ncelTasksResponse\"0\n\x16\x42ulkCancelTasksRequest\x12\x16\n\x06\x66ilter\x18\x01 \x01(\tR\x06\x66ilter\"G\n\x17\x42ulkCancelTasksResponse\x12,\n\x12ghost_reference_id\x18\x01 \x01(\tR\x10ghostReferenceIdB\xe7\x01\n\'com.services.omnichannel.tasks.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOT\xaa\x02#Services.Omnichannel.Tasks.V1alpha1\xca\x02#Services\\Omnichannel\\Tasks\\V1alpha1\xe2\x02/Services\\Omnichannel\\Tasks\\V1alpha1\\GPBMetadata\xea\x02&Services::Omnichannel::Tasks::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.tasks.v1alpha1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.services.omnichannel.tasks.v1alpha1B\rEntitiesProtoP\001\242\002\003SOT\252\002#Services.Omnichannel.Tasks.V1alpha1\312\002#Services\\Omnichannel\\Tasks\\V1alpha1\342\002/Services\\Omnichannel\\Tasks\\V1alpha1\\GPBMetadata\352\002&Services::Omnichannel::Tasks::V1alpha1'
  _globals['_CANCELTASKSREQUEST'].fields_by_name['task_sid']._loaded_options = None
  _globals['_CANCELTASKSREQUEST'].fields_by_name['task_sid']._serialized_options = b'0\001'
  _globals['_CANCELTASKSREQUEST']._serialized_start=122
  _globals['_CANCELTASKSREQUEST']._serialized_end=173
  _globals['_CANCELTASKSRESPONSE']._serialized_start=175
  _globals['_CANCELTASKSRESPONSE']._serialized_end=196
  _globals['_BULKCANCELTASKSREQUEST']._serialized_start=198
  _globals['_BULKCANCELTASKSREQUEST']._serialized_end=246
  _globals['_BULKCANCELTASKSRESPONSE']._serialized_start=248
  _globals['_BULKCANCELTASKSRESPONSE']._serialized_end=319
# @@protoc_insertion_point(module_scope)
