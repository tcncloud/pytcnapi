# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/task.proto
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
    'api/commons/task.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/commons/task.proto\x12\x0b\x61pi.commons*\xd5\x01\n\nTaskStatus\x12\x10\n\x0cTASK_UNKNOWN\x10\x00\x12\x13\n\x0eTASK_SCHEDULED\x10\xb4\x10\x12\x11\n\x0cTASK_WAITING\x10\xbe\x10\x12\x13\n\x0eTASK_PREPARING\x10\xc8\x10\x12\x11\n\x0cTASK_RUNNING\x10\x98\x11\x12\x13\n\x0eTASK_COMPLETED\x10\xfc\x11\x12\x1b\n\x16TASK_CANCELLED_TIMEOUT\x10\x86\x12\x12\x18\n\x13TASK_CANCELLED_USER\x10\x90\x12\x12\x19\n\x14TASK_CANCELLED_ADMIN\x10\x9a\x12\x42i\n\x0f\x63om.api.commonsB\tTaskProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\tTaskProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_TASKSTATUS']._serialized_start=40
  _globals['_TASKSTATUS']._serialized_end=253
# @@protoc_insertion_point(module_scope)
