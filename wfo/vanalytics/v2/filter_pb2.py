# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/filter.proto
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
    'wfo/vanalytics/v2/filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from wfo.vanalytics.v2 import transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ewfo/vanalytics/v2/filter.proto\x12\x11wfo.vanalytics.v2\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"wfo/vanalytics/v2/transcript.proto\"H\n\x13\x43reateFilterRequest\x12\x31\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x06\x66ilter\"\xca\x01\n\x12ListFiltersRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x37\n\x08\x63onflict\x18\x05 \x01(\x0b\x32\x19.wfo.vanalytics.v2.FilterH\x00R\x08\x63onflict\x12\x1b\n\x08\x66lag_sid\x18\x06 \x01(\x03H\x00R\x07\x66lagSidB\x07\n\x05where\"r\n\x13ListFiltersResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x33\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x07\x66ilters\"\xa4\x01\n\x13UpdateFilterRequest\x12\x31\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x06\x66ilter\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12\x1d\n\nfilter_sid\x18\x03 \x01(\x03R\tfilterSid\"L\n\x13\x44\x65leteFilterRequest\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSid\x12\x16\n\x06return\x18\x03 \x01(\x08R\x06return\"I\n\x14\x44\x65leteFilterResponse\x12\x31\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x06\x66ilter\"R\n\x10GetFilterRequest\x12\x14\n\x04name\x18\x03 \x01(\tH\x00R\x04name\x12\x1f\n\nfilter_sid\x18\x04 \x01(\x03H\x00R\tfilterSidB\x07\n\x05where\"\xe1\x01\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x18\n\x07version\x18\x06 \x01(\x03R\x07version\x12M\n\x10transcript_query\x18\x07 \x01(\x0b\x32\".wfo.vanalytics.v2.TranscriptQueryR\x0ftranscriptQueryB\x8a\x01\n\x15\x63om.wfo.vanalytics.v2B\x0b\x46ilterProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\013FilterProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_CREATEFILTERREQUEST']._serialized_start=156
  _globals['_CREATEFILTERREQUEST']._serialized_end=228
  _globals['_LISTFILTERSREQUEST']._serialized_start=231
  _globals['_LISTFILTERSREQUEST']._serialized_end=433
  _globals['_LISTFILTERSRESPONSE']._serialized_start=435
  _globals['_LISTFILTERSRESPONSE']._serialized_end=549
  _globals['_UPDATEFILTERREQUEST']._serialized_start=552
  _globals['_UPDATEFILTERREQUEST']._serialized_end=716
  _globals['_DELETEFILTERREQUEST']._serialized_start=718
  _globals['_DELETEFILTERREQUEST']._serialized_end=794
  _globals['_DELETEFILTERRESPONSE']._serialized_start=796
  _globals['_DELETEFILTERRESPONSE']._serialized_end=869
  _globals['_GETFILTERREQUEST']._serialized_start=871
  _globals['_GETFILTERREQUEST']._serialized_end=953
  _globals['_FILTER']._serialized_start=956
  _globals['_FILTER']._serialized_end=1181
# @@protoc_insertion_point(module_scope)
