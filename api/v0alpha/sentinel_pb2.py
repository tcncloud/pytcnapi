# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/sentinel.proto
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
    'api/v0alpha/sentinel.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import logging_pb2 as api_dot_commons_dot_logging__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/v0alpha/sentinel.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x19\x61pi/commons/logging.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"N\n\rSentinelEvent\x12\x34\n\tlog_event\x18\x01 \x01(\x0b\x32\x15.api.v0alpha.LogEventH\x00R\x08logEventB\x07\n\x05\x65vent\"\x83\x03\n\x08LogEvent\x12\x19\n\x08trace_id\x18\x03 \x01(\tR\x07traceId\x12\x1d\n\nsession_id\x18\x04 \x01(\tR\tsessionId\x12\x18\n\x07message\x18\x05 \x01(\tR\x07message\x12\x1a\n\x08location\x18\x06 \x01(\tR\x08location\x12\x1f\n\x0bstack_trace\x18\x07 \x01(\tR\nstackTrace\x12\x38\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12?\n\x08metadata\x18\t \x03(\x0b\x32#.api.v0alpha.LogEvent.MetadataEntryR\x08metadata\x12.\n\x08severity\x18\n \x01(\x0e\x32\x12.api.commons.LevelR\x08severity\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"C\n\rSendEventsReq\x12\x32\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1a.api.v0alpha.SentinelEventR\x06\x65vents\"\x0f\n\rSendEventsRes2\x84\x01\n\x08Sentinel\x12x\n\nSendEvents\x12\x1a.api.v0alpha.SendEventsReq\x1a\x1a.api.v0alpha.SendEventsRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v0alpha/sentinel/sendevents:\x01*Bm\n\x0f\x63om.api.v0alphaB\rSentinelProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.sentinel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\rSentinelProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_LOGEVENT_METADATAENTRY']._loaded_options = None
  _globals['_LOGEVENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SENTINEL'].methods_by_name['SendEvents']._loaded_options = None
  _globals['_SENTINEL'].methods_by_name['SendEvents']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v0alpha/sentinel/sendevents:\001*'
  _globals['_SENTINELEVENT']._serialized_start=158
  _globals['_SENTINELEVENT']._serialized_end=236
  _globals['_LOGEVENT']._serialized_start=239
  _globals['_LOGEVENT']._serialized_end=626
  _globals['_LOGEVENT_METADATAENTRY']._serialized_start=567
  _globals['_LOGEVENT_METADATAENTRY']._serialized_end=626
  _globals['_SENDEVENTSREQ']._serialized_start=628
  _globals['_SENDEVENTSREQ']._serialized_end=695
  _globals['_SENDEVENTSRES']._serialized_start=697
  _globals['_SENDEVENTSRES']._serialized_end=712
  _globals['_SENTINEL']._serialized_start=715
  _globals['_SENTINEL']._serialized_end=847
# @@protoc_insertion_point(module_scope)
