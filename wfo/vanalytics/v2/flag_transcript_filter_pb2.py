# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/flag_transcript_filter.proto
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
    'wfo/vanalytics/v2/flag_transcript_filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from wfo.vanalytics.v2 import filter_snapshot_pb2 as wfo_dot_vanalytics_dot_v2_dot_filter__snapshot__pb2
from wfo.vanalytics.v2 import flag_snapshot_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__snapshot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.wfo/vanalytics/v2/flag_transcript_filter.proto\x12\x11wfo.vanalytics.v2\x1a google/protobuf/field_mask.proto\x1a\'wfo/vanalytics/v2/filter_snapshot.proto\x1a%wfo/vanalytics/v2/flag_snapshot.proto\"\xe1\x01\n ListFlagTranscriptFiltersRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\x12H\n\x12\x66lag_snapshot_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x66lagSnapshotMask\x12L\n\x14\x66ilter_snapshot_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x12\x66ilterSnapshotMask\"\x84\x01\n!ListFlagTranscriptFiltersResponse\x12_\n\x17\x66lag_transcript_filters\x18\x01 \x03(\x0b\x32\'.wfo.vanalytics.v2.FlagTranscriptFilterR\x15\x66lagTranscriptFilters\"\xa8\x01\n\x14\x46lagTranscriptFilter\x12\x44\n\rflag_snapshot\x18\x01 \x01(\x0b\x32\x1f.wfo.vanalytics.v2.FlagSnapshotR\x0c\x66lagSnapshot\x12J\n\x0f\x66ilter_snapshot\x18\x02 \x01(\x0b\x32!.wfo.vanalytics.v2.FilterSnapshotR\x0e\x66ilterSnapshotB\x98\x01\n\x15\x63om.wfo.vanalytics.v2B\x19\x46lagTranscriptFilterProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.flag_transcript_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\031FlagTranscriptFilterProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_LISTFLAGTRANSCRIPTFILTERSREQUEST']._serialized_start=184
  _globals['_LISTFLAGTRANSCRIPTFILTERSREQUEST']._serialized_end=409
  _globals['_LISTFLAGTRANSCRIPTFILTERSRESPONSE']._serialized_start=412
  _globals['_LISTFLAGTRANSCRIPTFILTERSRESPONSE']._serialized_end=544
  _globals['_FLAGTRANSCRIPTFILTER']._serialized_start=547
  _globals['_FLAGTRANSCRIPTFILTER']._serialized_end=715
# @@protoc_insertion_point(module_scope)
