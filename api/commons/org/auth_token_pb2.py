# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/org/auth_token.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/commons/org/auth_token.proto\x12\x0f\x61pi.commons.org\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\x01\n\tAuthToken\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x03 \x01(\tR\x05orgId\x12:\n\nexpiration\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nexpirationB\x83\x01\n\x13\x63om.api.commons.orgB\x0e\x41uthTokenProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.auth_token_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\016AuthTokenProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_AUTHTOKEN']._serialized_start=87
  _globals['_AUTHTOKEN']._serialized_end=228
# @@protoc_insertion_point(module_scope)
