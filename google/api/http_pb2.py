# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/http.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15google/api/http.proto\x12\ngoogle.api\"y\n\x04Http\x12*\n\x05rules\x18\x01 \x03(\x0b\x32\x14.google.api.HttpRuleR\x05rules\x12\x45\n\x1f\x66ully_decode_reserved_expansion\x18\x02 \x01(\x08R\x1c\x66ullyDecodeReservedExpansion\"\xda\x02\n\x08HttpRule\x12\x1a\n\x08selector\x18\x01 \x01(\tR\x08selector\x12\x12\n\x03get\x18\x02 \x01(\tH\x00R\x03get\x12\x12\n\x03put\x18\x03 \x01(\tH\x00R\x03put\x12\x14\n\x04post\x18\x04 \x01(\tH\x00R\x04post\x12\x18\n\x06\x64\x65lete\x18\x05 \x01(\tH\x00R\x06\x64\x65lete\x12\x16\n\x05patch\x18\x06 \x01(\tH\x00R\x05patch\x12\x37\n\x06\x63ustom\x18\x08 \x01(\x0b\x32\x1d.google.api.CustomHttpPatternH\x00R\x06\x63ustom\x12\x12\n\x04\x62ody\x18\x07 \x01(\tR\x04\x62ody\x12#\n\rresponse_body\x18\x0c \x01(\tR\x0cresponseBody\x12\x45\n\x13\x61\x64\x64itional_bindings\x18\x0b \x03(\x0b\x32\x14.google.api.HttpRuleR\x12\x61\x64\x64itionalBindingsB\t\n\x07pattern\";\n\x11\x43ustomHttpPattern\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x12\n\x04path\x18\x02 \x01(\tR\x04pathB\xaa\x01\n\x0e\x63om.google.apiB\tHttpProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xf8\x01\x01\xa2\x02\x03GAX\xaa\x02\nGoogle.Api\xca\x02\nGoogle\\Api\xe2\x02\x16Google\\Api\\GPBMetadata\xea\x02\x0bGoogle::Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.http_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.google.apiB\tHttpProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\370\001\001\242\002\003GAX\252\002\nGoogle.Api\312\002\nGoogle\\Api\342\002\026Google\\Api\\GPBMetadata\352\002\013Google::Api'
  _globals['_HTTP']._serialized_start=37
  _globals['_HTTP']._serialized_end=158
  _globals['_HTTPRULE']._serialized_start=161
  _globals['_HTTPRULE']._serialized_end=507
  _globals['_CUSTOMHTTPPATTERN']._serialized_start=509
  _globals['_CUSTOMHTTPPATTERN']._serialized_end=568
# @@protoc_insertion_point(module_scope)
