# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/filter_snapshot.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'api/v1alpha1/vanalytics/filter_snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/vanalytics/filter_snapshot.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a(api/v1alpha1/vanalytics/transcript.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x99\x02\n\x0e\x46ilterSnapshot\x12.\n\x13\x66ilter_snapshot_sid\x18\x01 \x01(\x03R\x11\x66ilterSnapshotSid\x12\x1d\n\nfilter_sid\x18\x02 \x01(\x03R\tfilterSid\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12M\n\x0esearch_request\x18\x05 \x01(\x0b\x32&.api.v1alpha1.vanalytics.SearchRequestR\rsearchRequest\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x18\n\x07version\x18\x07 \x01(\x03R\x07versionB\xb0\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x13\x46ilterSnapshotProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.filter_snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\023FilterSnapshotProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_FILTERSNAPSHOT']._serialized_start=150
  _globals['_FILTERSNAPSHOT']._serialized_end=431
# @@protoc_insertion_point(module_scope)
