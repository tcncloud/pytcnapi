# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/flag_transcript_filter.proto
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
    'api/v1alpha1/vanalytics/flag_transcript_filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import filter_snapshot_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_filter__snapshot__pb2
from api.v1alpha1.vanalytics import flag_snapshot_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__snapshot__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4api/v1alpha1/vanalytics/flag_transcript_filter.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a-api/v1alpha1/vanalytics/filter_snapshot.proto\x1a+api/v1alpha1/vanalytics/flag_snapshot.proto\x1a google/protobuf/field_mask.proto\"\xe1\x01\n ListFlagTranscriptFiltersRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\x12H\n\x12\x66lag_snapshot_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x66lagSnapshotMask\x12L\n\x14\x66ilter_snapshot_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x12\x66ilterSnapshotMask\"\x8a\x01\n!ListFlagTranscriptFiltersResponse\x12\x65\n\x17\x66lag_transcript_filters\x18\x01 \x03(\x0b\x32-.api.v1alpha1.vanalytics.FlagTranscriptFilterR\x15\x66lagTranscriptFilters\"\xb4\x01\n\x14\x46lagTranscriptFilter\x12J\n\rflag_snapshot\x18\x01 \x01(\x0b\x32%.api.v1alpha1.vanalytics.FlagSnapshotR\x0c\x66lagSnapshot\x12P\n\x0f\x66ilter_snapshot\x18\x02 \x01(\x0b\x32\'.api.v1alpha1.vanalytics.FilterSnapshotR\x0e\x66ilterSnapshotB\xb6\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x19\x46lagTranscriptFilterProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_transcript_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\031FlagTranscriptFilterProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_LISTFLAGTRANSCRIPTFILTERSREQUEST']._serialized_start=208
  _globals['_LISTFLAGTRANSCRIPTFILTERSREQUEST']._serialized_end=433
  _globals['_LISTFLAGTRANSCRIPTFILTERSRESPONSE']._serialized_start=436
  _globals['_LISTFLAGTRANSCRIPTFILTERSRESPONSE']._serialized_end=574
  _globals['_FLAGTRANSCRIPTFILTER']._serialized_start=577
  _globals['_FLAGTRANSCRIPTFILTER']._serialized_end=757
# @@protoc_insertion_point(module_scope)
