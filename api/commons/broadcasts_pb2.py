# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/broadcasts.proto
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
    'api/commons/broadcasts.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/broadcasts.proto\x12\x0b\x61pi.commons\"\x83\x01\n\x0cTemplateType\"s\n\x04\x45num\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x0b\n\x07LAYERED\x10\x02\x12\x0b\n\x07INBOUND\x10\x03\x12\x0c\n\x08MAC_ONLY\x10\x04\x12\x10\n\x0cPREVIEW_ONLY\x10\x05\x12\x16\n\x12RINGLESS_VOICEMAIL\x10\x06*\xd3\x02\n\rBroadcastType\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x12\n\rTYPE_OUTBOUND\x10\xe8\x07\x12\x1f\n\x1aTYPE_OUTBOUND_PREVIEW_ONLY\x10\xcc\x08\x12\x1b\n\x16TYPE_OUTBOUND_MAC_ONLY\x10\xb0\t\x12%\n TYPE_OUTBOUND_RINGLESS_VOICEMAIL\x10\x94\n\x12\x11\n\x0cTYPE_INBOUND\x10\xd0\x0f\x12\x10\n\x0bTYPE_MANUAL\x10\xb8\x17\x12\r\n\x08TYPE_SMS\x10\xa0\x1f\x12\x0f\n\nTYPE_EMAIL\x10\x88\'\x12\x1a\n\x15TYPE_OUTBOUND_INBOUND\x10\xd8\x36\x12\x19\n\x14TYPE_OUTBOUND_MANUAL\x10\xc0>\x12\x18\n\x13TYPE_INBOUND_MANUAL\x10\xa8\x46\x12!\n\x1cTYPE_OUTBOUND_INBOUND_MANUAL\x10\x90NBo\n\x0f\x63om.api.commonsB\x0f\x42roadcastsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.broadcasts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\017BroadcastsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_BROADCASTTYPE']._serialized_start=180
  _globals['_BROADCASTTYPE']._serialized_end=519
  _globals['_TEMPLATETYPE']._serialized_start=46
  _globals['_TEMPLATETYPE']._serialized_end=177
  _globals['_TEMPLATETYPE_ENUM']._serialized_start=62
  _globals['_TEMPLATETYPE_ENUM']._serialized_end=177
# @@protoc_insertion_point(module_scope)
