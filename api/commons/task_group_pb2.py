# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/task_group.proto
# Protobuf Python Version: 5.28.2
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
    2,
    '',
    'api/commons/task_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/task_group.proto\x12\x0b\x61pi.commons*\xa9\x04\n\x0fTaskGroupStatus\x12\x0e\n\nTG_UNKNOWN\x10\x00\x12\x0f\n\nTG_PREPARE\x10\xe8\x07\x12\x11\n\x0cTG_SCHEDULED\x10\xcc\x08\x12\x19\n\x14TG_SCHEDULED_LINKING\x10\xd6\x08\x12\x18\n\x13TG_SCHEDULED_PAUSED\x10\xe0\x08\x12\x0f\n\nTG_RUNNING\x10\xb0\t\x12\x0e\n\tTG_PAUSED\x10\xba\t\x12\x0f\n\nTG_WAITING\x10\xc4\t\x12\x11\n\x0cTG_COMPLETED\x10\x94\n\x12\x19\n\x14TG_CANCELLED_TIMEOUT\x10\x9e\n\x12\x16\n\x11TG_CANCELLED_USER\x10\xa8\n\x12\x17\n\x12TG_CANCELLED_ADMIN\x10\xb2\n\x12\x18\n\x13TG_SUMMED_COMPLETED\x10\xf8\n\x12 \n\x1bTG_SUMMED_CANCELLED_TIMEOUT\x10\x82\x0b\x12\x1d\n\x18TG_SUMMED_CANCELLED_USER\x10\x8c\x0b\x12\x1e\n\x19TG_SUMMED_CANCELLED_ADMIN\x10\x96\x0b\x12\"\n\x1dTG_ACCOUNTINGEXPORT_COMPLETED\x10\xdc\x0b\x12*\n%TG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT\x10\xe6\x0b\x12\'\n\"TG_ACCOUNTINGEXPORT_CANCELLED_USER\x10\xf0\x0b\x12(\n#TG_ACCOUNTINGEXPORT_CANCELLED_ADMIN\x10\xfa\x0b\x42n\n\x0f\x63om.api.commonsB\x0eTaskGroupProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.task_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\016TaskGroupProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_TASKGROUPSTATUS']._serialized_start=46
  _globals['_TASKGROUPSTATUS']._serialized_end=599
# @@protoc_insertion_point(module_scope)
