# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/manual.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'api/commons/manual.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/commons/manual.proto\x12\x0b\x61pi.commons*\xe9\x03\n\x15ManualDialGroupStatus\x12\x0f\n\x0bMDG_UNKNOWN\x10\x00\x12\x10\n\x0bMDG_PREPARE\x10\xf0.\x12\x12\n\rMDG_SCHEDULED\x10\xd4/\x12\x10\n\x0bMDG_RUNNING\x10\xb8\x30\x12\x12\n\rMDG_COMPLETED\x10\x9c\x31\x12\x1a\n\x15MDG_CANCELLED_TIMEOUT\x10\xa6\x31\x12\x17\n\x12MDG_CANCELLED_USER\x10\xb0\x31\x12\x18\n\x13MDG_CANCELLED_ADMIN\x10\xba\x31\x12\x19\n\x14MDG_SUMMED_COMPLETED\x10\x80\x32\x12!\n\x1cMDG_SUMMED_CANCELLED_TIMEOUT\x10\x8a\x32\x12\x1e\n\x19MDG_SUMMED_CANCELLED_USER\x10\x94\x32\x12\x1f\n\x1aMDG_SUMMED_CANCELLED_ADMIN\x10\x9e\x32\x12#\n\x1eMDG_ACCOUNTINGEXPORT_COMPLETED\x10\xe4\x32\x12+\n&MDG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT\x10\xee\x32\x12(\n#MDG_ACCOUNTINGEXPORT_CANCELLED_USER\x10\xf8\x32\x12)\n$MDG_ACCOUNTINGEXPORT_CANCELLED_ADMIN\x10\x82\x33\x42k\n\x0f\x63om.api.commonsB\x0bManualProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.manual_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\013ManualProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_MANUALDIALGROUPSTATUS']._serialized_start=42
  _globals['_MANUALDIALGROUPSTATUS']._serialized_end=531
# @@protoc_insertion_point(module_scope)
