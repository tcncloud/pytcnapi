# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/expr.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'api/v1alpha1/vanalytics/expr.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import vanalytics_pb2 as api_dot_commons_dot_vanalytics__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/vanalytics/expr.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x1c\x61pi/commons/vanalytics.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xca\x01\n\nUint32Expr\x12\x10\n\x02gt\x18\x01 \x01(\rH\x00R\x02gt\x12\x12\n\x03gte\x18\x02 \x01(\rH\x00R\x03gte\x12\x10\n\x02lt\x18\x03 \x01(\rH\x00R\x02lt\x12\x12\n\x03lte\x18\x04 \x01(\rH\x00R\x03lte\x12\x10\n\x02\x65q\x18\x05 \x01(\rH\x00R\x02\x65q\x12\x17\n\x06not_eq\x18\x06 \x01(\rH\x00R\x05notEq\x12<\n\x05range\x18\x07 \x01(\x0b\x32$.api.v1alpha1.vanalytics.Uint32RangeH\x00R\x05rangeB\x07\n\x05where\"s\n\x0bUint32Range\x12\x12\n\x04\x66rom\x18\x01 \x01(\rR\x04\x66rom\x12\x0e\n\x02to\x18\x02 \x01(\rR\x02to\x12!\n\x0cinclude_from\x18\x03 \x01(\x08R\x0bincludeFrom\x12\x1d\n\ninclude_to\x18\x04 \x01(\x08R\tincludeTo\"\x94\x01\n\rTimestampExpr\x12?\n\x05range\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.vanalytics.TimestampRangeH\x00R\x05range\x12\x39\n\x06moment\x18\x02 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.MomentH\x00R\x06momentB\x07\n\x05where\"X\n\x06Moment\x12\x1b\n\ttime_zone\x18\x01 \x01(\tR\x08timeZone\x12\x31\n\x08interval\x18\x02 \x01(\x0e\x32\x15.api.commons.IntervalR\x08interval\"\xae\x01\n\x0eTimestampRange\x12.\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x66rom\x12*\n\x02to\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02to\x12!\n\x0cinclude_from\x18\x03 \x01(\x08R\x0bincludeFrom\x12\x1d\n\ninclude_to\x18\x04 \x01(\x08R\tincludeToB\xa6\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\tExprProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.expr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\tExprProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_UINT32EXPR']._serialized_start=127
  _globals['_UINT32EXPR']._serialized_end=329
  _globals['_UINT32RANGE']._serialized_start=331
  _globals['_UINT32RANGE']._serialized_end=446
  _globals['_TIMESTAMPEXPR']._serialized_start=449
  _globals['_TIMESTAMPEXPR']._serialized_end=597
  _globals['_MOMENT']._serialized_start=599
  _globals['_MOMENT']._serialized_end=687
  _globals['_TIMESTAMPRANGE']._serialized_start=690
  _globals['_TIMESTAMPRANGE']._serialized_end=864
# @@protoc_insertion_point(module_scope)
