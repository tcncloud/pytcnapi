# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/transcript_summary.proto
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
    'api/v1alpha1/vanalytics/transcript_summary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import vanalytics_pb2 as api_dot_commons_dot_vanalytics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/vanalytics/transcript_summary.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x1c\x61pi/commons/vanalytics.proto\"D\n\x1bGetTranscriptSummaryRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\"y\n\x1cGetTranscriptSummaryResponse\x12Y\n\x12transcript_summary\x18\x01 \x01(\x0b\x32*.api.v1alpha1.vanalytics.TranscriptSummaryR\x11transcriptSummary\"v\n\x11TranscriptSummary\x12#\n\rbullet_points\x18\x01 \x03(\tR\x0c\x62ulletPoints\x12<\n\x06status\x18\x02 \x01(\x0e\x32$.api.commons.TranscriptSummaryStatusR\x06statusB\xb3\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x16TranscriptSummaryProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.transcript_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\026TranscriptSummaryProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_GETTRANSCRIPTSUMMARYREQUEST']._serialized_start=107
  _globals['_GETTRANSCRIPTSUMMARYREQUEST']._serialized_end=175
  _globals['_GETTRANSCRIPTSUMMARYRESPONSE']._serialized_start=177
  _globals['_GETTRANSCRIPTSUMMARYRESPONSE']._serialized_end=298
  _globals['_TRANSCRIPTSUMMARY']._serialized_start=300
  _globals['_TRANSCRIPTSUMMARY']._serialized_end=418
# @@protoc_insertion_point(module_scope)
