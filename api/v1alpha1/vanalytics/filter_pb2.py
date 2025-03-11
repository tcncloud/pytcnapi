# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/filter.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'api/v1alpha1/vanalytics/filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/vanalytics/filter.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a(api/v1alpha1/vanalytics/transcript.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"N\n\x13\x43reateFilterRequest\x12\x37\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x06\x66ilter\"\xd0\x01\n\x12ListFiltersRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12=\n\x08\x63onflict\x18\x05 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterH\x00R\x08\x63onflict\x12\x1b\n\x08\x66lag_sid\x18\x06 \x01(\x03H\x00R\x07\x66lagSidB\x07\n\x05where\"x\n\x13ListFiltersResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x39\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x07\x66ilters\"\xaa\x01\n\x13UpdateFilterRequest\x12\x37\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x06\x66ilter\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12\x1d\n\nfilter_sid\x18\x03 \x01(\x03R\tfilterSid\"L\n\x13\x44\x65leteFilterRequest\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSid\x12\x16\n\x06return\x18\x03 \x01(\x08R\x06return\"O\n\x14\x44\x65leteFilterResponse\x12\x37\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x06\x66ilter\"\xa3\x01\n\x10GetFilterRequest\x12O\n\x0esearch_request\x18\x02 \x01(\x0b\x32&.api.v1alpha1.vanalytics.SearchRequestH\x00R\rsearchRequest\x12\x14\n\x04name\x18\x03 \x01(\tH\x00R\x04name\x12\x1f\n\nfilter_sid\x18\x04 \x01(\x03H\x00R\tfilterSidB\x07\n\x05where\"\xe1\x01\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12M\n\x0esearch_request\x18\x04 \x01(\x0b\x32&.api.v1alpha1.vanalytics.SearchRequestR\rsearchRequest\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x18\n\x07version\x18\x06 \x01(\x03R\x07versionB\xa8\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0b\x46ilterProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\013FilterProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_CREATEFILTERREQUEST']._serialized_start=174
  _globals['_CREATEFILTERREQUEST']._serialized_end=252
  _globals['_LISTFILTERSREQUEST']._serialized_start=255
  _globals['_LISTFILTERSREQUEST']._serialized_end=463
  _globals['_LISTFILTERSRESPONSE']._serialized_start=465
  _globals['_LISTFILTERSRESPONSE']._serialized_end=585
  _globals['_UPDATEFILTERREQUEST']._serialized_start=588
  _globals['_UPDATEFILTERREQUEST']._serialized_end=758
  _globals['_DELETEFILTERREQUEST']._serialized_start=760
  _globals['_DELETEFILTERREQUEST']._serialized_end=836
  _globals['_DELETEFILTERRESPONSE']._serialized_start=838
  _globals['_DELETEFILTERRESPONSE']._serialized_end=917
  _globals['_GETFILTERREQUEST']._serialized_start=920
  _globals['_GETFILTERREQUEST']._serialized_end=1083
  _globals['_FILTER']._serialized_start=1086
  _globals['_FILTER']._serialized_end=1311
# @@protoc_insertion_point(module_scope)
