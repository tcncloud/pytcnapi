# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/transcript_summary.proto
# Protobuf Python Version: 5.27.0
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
    0,
    '',
    'wfo/vanalytics/v2/transcript_summary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*wfo/vanalytics/v2/transcript_summary.proto\x12\x11wfo.vanalytics.v2\"D\n\x1bGetTranscriptSummaryRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\"s\n\x1cGetTranscriptSummaryResponse\x12S\n\x12transcript_summary\x18\x01 \x01(\x0b\x32$.wfo.vanalytics.v2.TranscriptSummaryR\x11transcriptSummary\"8\n\x11TranscriptSummary\x12#\n\rbullet_points\x18\x01 \x03(\tR\x0c\x62ulletPointsB\x95\x01\n\x15\x63om.wfo.vanalytics.v2B\x16TranscriptSummaryProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.transcript_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\026TranscriptSummaryProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_GETTRANSCRIPTSUMMARYREQUEST']._serialized_start=65
  _globals['_GETTRANSCRIPTSUMMARYREQUEST']._serialized_end=133
  _globals['_GETTRANSCRIPTSUMMARYRESPONSE']._serialized_start=135
  _globals['_GETTRANSCRIPTSUMMARYRESPONSE']._serialized_end=250
  _globals['_TRANSCRIPTSUMMARY']._serialized_start=252
  _globals['_TRANSCRIPTSUMMARY']._serialized_end=308
# @@protoc_insertion_point(module_scope)
