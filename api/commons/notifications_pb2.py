# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/notifications.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'api/commons/notifications.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/commons/notifications.proto\x12\x0b\x61pi.commons\":\n\x10\x46ieldValueFilter\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"b\n\x10NotificationType\"N\n\x04\x45num\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45MAIL\x10\x01\x12\x0f\n\x0bSERVER_PUSH\x10\x02\x12\x07\n\x03IOS\x10\x03\x12\x0b\n\x07\x41NDROID\x10\x04\x12\x07\n\x03SMS\x10\x05\x42r\n\x0f\x63om.api.commonsB\x12NotificationsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.notifications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\022NotificationsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_FIELDVALUEFILTER']._serialized_start=48
  _globals['_FIELDVALUEFILTER']._serialized_end=106
  _globals['_NOTIFICATIONTYPE']._serialized_start=108
  _globals['_NOTIFICATIONTYPE']._serialized_end=206
  _globals['_NOTIFICATIONTYPE_ENUM']._serialized_start=128
  _globals['_NOTIFICATIONTYPE_ENUM']._serialized_end=206
# @@protoc_insertion_point(module_scope)
