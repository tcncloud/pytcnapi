# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/filter_snapshot.proto
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
    'wfo/vanalytics/v2/filter_snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from wfo.vanalytics.v2 import transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'wfo/vanalytics/v2/filter_snapshot.proto\x12\x11wfo.vanalytics.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"wfo/vanalytics/v2/transcript.proto\"\x99\x02\n\x0e\x46ilterSnapshot\x12.\n\x13\x66ilter_snapshot_sid\x18\x01 \x01(\x03R\x11\x66ilterSnapshotSid\x12\x1d\n\nfilter_sid\x18\x02 \x01(\x03R\tfilterSid\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x18\n\x07version\x18\x07 \x01(\x03R\x07version\x12M\n\x10transcript_query\x18\x08 \x01(\x0b\x32\".wfo.vanalytics.v2.TranscriptQueryR\x0ftranscriptQueryB\x92\x01\n\x15\x63om.wfo.vanalytics.v2B\x13\x46ilterSnapshotProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.filter_snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\023FilterSnapshotProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_FILTERSNAPSHOT']._serialized_start=132
  _globals['_FILTERSNAPSHOT']._serialized_end=413
# @@protoc_insertion_point(module_scope)
