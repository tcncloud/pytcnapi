# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/inbound.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'api/commons/inbound.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/inbound.proto\x12\x0b\x61pi.commons*\xf7\x03\n\x12InboundGroupStatus\x12\x0f\n\x0bIBG_UNKNOWN\x10\x00\x12\x10\n\x0bIBG_PREPARE\x10\x88\'\x12\x12\n\rIBG_SCHEDULED\x10\xec\'\x12\x10\n\x0bIBG_RUNNING\x10\xd0(\x12\x0f\n\nIBG_PAUSED\x10\xda(\x12\x12\n\rIBG_COMPLETED\x10\xb4)\x12\x1a\n\x15IBG_CANCELLED_TIMEOUT\x10\xbe)\x12\x17\n\x12IBG_CANCELLED_USER\x10\xc8)\x12\x18\n\x13IBG_CANCELLED_ADMIN\x10\xd2)\x12\x19\n\x14IBG_SUMMED_COMPLETED\x10\x98*\x12!\n\x1cIBG_SUMMED_CANCELLED_TIMEOUT\x10\xa2*\x12\x1e\n\x19IBG_SUMMED_CANCELLED_USER\x10\xac*\x12\x1f\n\x1aIBG_SUMMED_CANCELLED_ADMIN\x10\xb6*\x12#\n\x1eIBG_ACCOUNTINGEXPORT_COMPLETED\x10\xfc*\x12+\n&IBG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT\x10\x86+\x12(\n#IBG_ACCOUNTINGEXPORT_CANCELLED_USER\x10\x90+\x12)\n$IBG_ACCOUNTINGEXPORT_CANCELLED_ADMIN\x10\x9a+Bl\n\x0f\x63om.api.commonsB\x0cInboundProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.inbound_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014InboundProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_INBOUNDGROUPSTATUS']._serialized_start=43
  _globals['_INBOUNDGROUPSTATUS']._serialized_end=546
# @@protoc_insertion_point(module_scope)
