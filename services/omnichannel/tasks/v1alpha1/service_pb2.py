# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/omnichannel/tasks/v1alpha1/service.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'services/omnichannel/tasks/v1alpha1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.omnichannel.tasks.v1alpha1 import entities_pb2 as services_dot_omnichannel_dot_tasks_dot_v1alpha1_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1services/omnichannel/tasks/v1alpha1/service.proto\x12#services.omnichannel.tasks.v1alpha1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x32services/omnichannel/tasks/v1alpha1/entities.proto2\xb2\x03\n\x0cTasksService\x12\xc7\x01\n\x0b\x43\x61ncelTasks\x12\x37.services.omnichannel.tasks.v1alpha1.CancelTasksRequest\x1a\x38.services.omnichannel.tasks.v1alpha1.CancelTasksResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02\x35\"0/services/omnichannel/tasks/v1alpha1/canceltasks:\x01*\x12\xd7\x01\n\x0f\x42ulkCancelTasks\x12;.services.omnichannel.tasks.v1alpha1.BulkCancelTasksRequest\x1a<.services.omnichannel.tasks.v1alpha1.BulkCancelTasksResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02\x39\"4/services/omnichannel/tasks/v1alpha1/bulkcanceltasks:\x01*B\xe6\x01\n\'com.services.omnichannel.tasks.v1alpha1B\x0cServiceProtoP\x01\xa2\x02\x03SOT\xaa\x02#Services.Omnichannel.Tasks.V1alpha1\xca\x02#Services\\Omnichannel\\Tasks\\V1alpha1\xe2\x02/Services\\Omnichannel\\Tasks\\V1alpha1\\GPBMetadata\xea\x02&Services::Omnichannel::Tasks::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.tasks.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.services.omnichannel.tasks.v1alpha1B\014ServiceProtoP\001\242\002\003SOT\252\002#Services.Omnichannel.Tasks.V1alpha1\312\002#Services\\Omnichannel\\Tasks\\V1alpha1\342\002/Services\\Omnichannel\\Tasks\\V1alpha1\\GPBMetadata\352\002&Services::Omnichannel::Tasks::V1alpha1'
  _globals['_TASKSSERVICE'].methods_by_name['CancelTasks']._loaded_options = None
  _globals['_TASKSSERVICE'].methods_by_name['CancelTasks']._serialized_options = b'\272\270\221\002\005\n\003\010\260\t\202\323\344\223\0025\"0/services/omnichannel/tasks/v1alpha1/canceltasks:\001*'
  _globals['_TASKSSERVICE'].methods_by_name['BulkCancelTasks']._loaded_options = None
  _globals['_TASKSSERVICE'].methods_by_name['BulkCancelTasks']._serialized_options = b'\272\270\221\002\005\n\003\010\260\t\202\323\344\223\0029\"4/services/omnichannel/tasks/v1alpha1/bulkcanceltasks:\001*'
  _globals['_TASKSSERVICE']._serialized_start=198
  _globals['_TASKSSERVICE']._serialized_end=632
# @@protoc_insertion_point(module_scope)
