# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/callmonitor.proto
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
    'api/commons/callmonitor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/commons/callmonitor.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\x03\n\x12HoldQueueCallStats\x12\x17\n\x07\x63\x61ll_id\x18\x01 \x01(\tR\x06\x63\x61llId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x03 \x01(\tR\ncampaignId\x12!\n\x0cphone_number\x18\x04 \x01(\tR\x0bphoneNumber\x12;\n\x06status\x18\x05 \x01(\x0e\x32#.api.commons.HoldQueueMonitorStatusR\x06status\x12\x36\n\x17monitor_duration_millis\x18\x07 \x01(\x03R\x15monitorDurationMillis\x12H\n\x12monitor_start_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10monitorStartTime\x12\x44\n\x10monitor_end_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0emonitorEndTime*\xdf\x01\n\x16HoldQueueMonitorStatus\x12)\n%HOLD_QUEUE_MONITOR_STATUS_UNSPECIFIED\x10\x00\x12(\n$HOLD_QUEUE_MONITOR_STATUS_MONITORING\x10\x01\x12%\n!HOLD_QUEUE_MONITOR_STATUS_SUCCESS\x10\x02\x12$\n HOLD_QUEUE_MONITOR_STATUS_FAILED\x10\x03\x12#\n\x1fHOLD_QUEUE_MONITOR_STATUS_ENDED\x10\x04\x42p\n\x0f\x63om.api.commonsB\x10\x43\x61llmonitorProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.callmonitor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\020CallmonitorProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_HOLDQUEUEMONITORSTATUS']._serialized_start=480
  _globals['_HOLDQUEUEMONITORSTATUS']._serialized_end=703
  _globals['_HOLDQUEUECALLSTATS']._serialized_start=80
  _globals['_HOLDQUEUECALLSTATS']._serialized_end=477
# @@protoc_insertion_point(module_scope)
