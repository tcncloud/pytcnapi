# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/sentinel/entities.proto
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
    'api/v1alpha1/sentinel/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import logging_pb2 as api_dot_commons_dot_logging__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/sentinel/entities.proto\x12\x15\x61pi.v1alpha1.sentinel\x1a\x19\x61pi/commons/logging.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"X\n\rSentinelEvent\x12>\n\tlog_event\x18\x01 \x01(\x0b\x32\x1f.api.v1alpha1.sentinel.LogEventH\x00R\x08logEventB\x07\n\x05\x65vent\"\x8d\x03\n\x08LogEvent\x12\x19\n\x08trace_id\x18\x03 \x01(\tR\x07traceId\x12\x1d\n\nsession_id\x18\x04 \x01(\tR\tsessionId\x12\x18\n\x07message\x18\x05 \x01(\tR\x07message\x12\x1a\n\x08location\x18\x06 \x01(\tR\x08location\x12\x1f\n\x0bstack_trace\x18\x07 \x01(\tR\nstackTrace\x12\x38\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12I\n\x08metadata\x18\t \x03(\x0b\x32-.api.v1alpha1.sentinel.LogEvent.MetadataEntryR\x08metadata\x12.\n\x08severity\x18\n \x01(\x0e\x32\x12.api.commons.LevelR\x08severity\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"M\n\rSendEventsReq\x12<\n\x06\x65vents\x18\x01 \x03(\x0b\x32$.api.v1alpha1.sentinel.SentinelEventR\x06\x65vents\"\x0f\n\rSendEventsResB\xa0\x01\n\x19\x63om.api.v1alpha1.sentinelB\rEntitiesProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x15\x41pi.V1alpha1.Sentinel\xca\x02\x15\x41pi\\V1alpha1\\Sentinel\xe2\x02!Api\\V1alpha1\\Sentinel\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Sentinelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.sentinel.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.sentinelB\rEntitiesProtoP\001\242\002\003AVS\252\002\025Api.V1alpha1.Sentinel\312\002\025Api\\V1alpha1\\Sentinel\342\002!Api\\V1alpha1\\Sentinel\\GPBMetadata\352\002\027Api::V1alpha1::Sentinel'
  _globals['_LOGEVENT_METADATAENTRY']._loaded_options = None
  _globals['_LOGEVENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_SENTINELEVENT']._serialized_start=123
  _globals['_SENTINELEVENT']._serialized_end=211
  _globals['_LOGEVENT']._serialized_start=214
  _globals['_LOGEVENT']._serialized_end=611
  _globals['_LOGEVENT_METADATAENTRY']._serialized_start=552
  _globals['_LOGEVENT_METADATAENTRY']._serialized_end=611
  _globals['_SENDEVENTSREQ']._serialized_start=613
  _globals['_SENDEVENTSREQ']._serialized_end=690
  _globals['_SENDEVENTSRES']._serialized_start=692
  _globals['_SENDEVENTSRES']._serialized_end=707
# @@protoc_insertion_point(module_scope)
