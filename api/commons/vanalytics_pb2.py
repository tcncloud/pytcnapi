# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/vanalytics.proto
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
    'api/commons/vanalytics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/vanalytics.proto\x12\x0b\x61pi.commons*\xbe\x01\n\x08Interval\x12\t\n\x05TODAY\x10\x00\x12\r\n\tYESTERDAY\x10\x01\x12\r\n\tTHIS_WEEK\x10\x02\x12\x0f\n\x0bLAST_7_DAYS\x10\x03\x12\r\n\tLAST_WEEK\x10\x04\x12\x10\n\x0cLAST_14_DAYS\x10\x05\x12\x0e\n\nTHIS_MONTH\x10\x06\x12\x10\n\x0cLAST_30_DAYS\x10\x07\x12\x10\n\x0cLAST_60_DAYS\x10\x08\x12\x10\n\x0cLAST_90_DAYS\x10\t\x12\x11\n\rLAST_180_DAYS\x10\n*\x82\x02\n\x17TranscriptSummaryStatus\x12$\n TRANSCRIPT_SUMMARY_STATUS_QUEUED\x10\x00\x12\x35\n(TRANSCRIPT_SUMMARY_STATUS_QUEUED_ERRORED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n$TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED\x10\x01\x12\x39\n,TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED_ERRORED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12%\n!TRANSCRIPT_SUMMARY_STATUS_VISIBLE\x10\x02*\xb7\x01\n\x17TranscriptSentimentTone\x12%\n!TRANSCRIPT_SENTIMENT_TONE_UNKNOWN\x10\x00\x12&\n\"TRANSCRIPT_SENTIMENT_TONE_NEGATIVE\x10\x01\x12%\n!TRANSCRIPT_SENTIMENT_TONE_NEUTRAL\x10\x02\x12&\n\"TRANSCRIPT_SENTIMENT_TONE_POSITIVE\x10\x03*b\n\rRecordingType\x12\x16\n\x12RECORDING_TYPE_TCN\x10\x00\x12\x1b\n\x17RECORDING_TYPE_EXTERNAL\x10\x01\x12\x1c\n\x18RECORDING_TYPE_VOICEMAIL\x10\x02\x42o\n\x0f\x63om.api.commonsB\x0fVanalyticsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.vanalytics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\017VanalyticsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_INTERVAL']._serialized_start=46
  _globals['_INTERVAL']._serialized_end=236
  _globals['_TRANSCRIPTSUMMARYSTATUS']._serialized_start=239
  _globals['_TRANSCRIPTSUMMARYSTATUS']._serialized_end=497
  _globals['_TRANSCRIPTSENTIMENTTONE']._serialized_start=500
  _globals['_TRANSCRIPTSENTIMENTTONE']._serialized_end=683
  _globals['_RECORDINGTYPE']._serialized_start=685
  _globals['_RECORDINGTYPE']._serialized_end=783
# @@protoc_insertion_point(module_scope)
