# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/types.proto
# Protobuf Python Version: 5.27.3
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
    3,
    '',
    'api/commons/types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/commons/types.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x07\n\x05\x45mpty\"\xc3\x01\n\x0e\x43ronExpression\x12%\n\x0erepeat_minutes\x18\x01 \x01(\tR\rrepeatMinutes\x12 \n\x0chours_of_day\x18\x02 \x01(\tR\nhoursOfDay\x12\"\n\rdays_of_month\x18\x03 \x01(\tR\x0b\x64\x61ysOfMonth\x12$\n\x0emonths_of_year\x18\x04 \x01(\tR\x0cmonthsOfYear\x12\x1e\n\x0b\x64\x61y_of_week\x18\x05 \x01(\tR\tdayOfWeek\">\n\rInt32Nullable\x12\x17\n\x07is_null\x18\x01 \x01(\x08R\x06isNull\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value\">\n\rInt64Nullable\x12\x17\n\x07is_null\x18\x01 \x01(\x08R\x06isNull\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value\"\xaa\x01\n\x15SomeSidAndDateCompare\x12\x19\n\x08some_sid\x18\x01 \x01(\x03R\x07someSid\x12=\n\x0c\x64\x61te_greater\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teGreater\x12\x37\n\tdate_less\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08\x64\x61teLess\"\'\n\rInt64ArraySql\x12\x16\n\x06values\x18\x01 \x03(\x03R\x06values\"\'\n\rInt32ArraySql\x12\x16\n\x06values\x18\x01 \x03(\x05R\x06values\"(\n\x0eStringArraySql\x12\x16\n\x06values\x18\x02 \x03(\tR\x06values\"&\n\x0c\x42oolArraySql\x12\x16\n\x06values\x18\x01 \x03(\x08R\x06values\"I\n\x12Int32ValueArraySql\x12\x33\n\x06values\x18\x01 \x03(\x0b\x32\x1b.google.protobuf.Int32ValueR\x06values\"#\n\x07Int64Id\x12\x18\n\x05value\x18\x01 \x01(\x03\x42\x02\x30\x01R\x05valueBj\n\x0f\x63om.api.commonsB\nTypesProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\nTypesProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_INT64ID'].fields_by_name['value']._loaded_options = None
  _globals['_INT64ID'].fields_by_name['value']._serialized_options = b'0\001'
  _globals['_EMPTY']._serialized_start=105
  _globals['_EMPTY']._serialized_end=112
  _globals['_CRONEXPRESSION']._serialized_start=115
  _globals['_CRONEXPRESSION']._serialized_end=310
  _globals['_INT32NULLABLE']._serialized_start=312
  _globals['_INT32NULLABLE']._serialized_end=374
  _globals['_INT64NULLABLE']._serialized_start=376
  _globals['_INT64NULLABLE']._serialized_end=438
  _globals['_SOMESIDANDDATECOMPARE']._serialized_start=441
  _globals['_SOMESIDANDDATECOMPARE']._serialized_end=611
  _globals['_INT64ARRAYSQL']._serialized_start=613
  _globals['_INT64ARRAYSQL']._serialized_end=652
  _globals['_INT32ARRAYSQL']._serialized_start=654
  _globals['_INT32ARRAYSQL']._serialized_end=693
  _globals['_STRINGARRAYSQL']._serialized_start=695
  _globals['_STRINGARRAYSQL']._serialized_end=735
  _globals['_BOOLARRAYSQL']._serialized_start=737
  _globals['_BOOLARRAYSQL']._serialized_end=775
  _globals['_INT32VALUEARRAYSQL']._serialized_start=777
  _globals['_INT32VALUEARRAYSQL']._serialized_end=850
  _globals['_INT64ID']._serialized_start=852
  _globals['_INT64ID']._serialized_end=887
# @@protoc_insertion_point(module_scope)
