# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vanalytics/flag_filter.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import filter_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_filter__pb2
from api.v1alpha1.vanalytics import flag_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/v1alpha1/vanalytics/flag_filter.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a$api/v1alpha1/vanalytics/filter.proto\x1a\"api/v1alpha1/vanalytics/flag.proto\x1a google/protobuf/field_mask.proto\"_\n\x17\x43reateFlagFilterRequest\x12\x44\n\x0b\x66lag_filter\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.FlagFilterR\nflagFilter\"\xe7\x01\n\x16ListFlagFiltersRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x37\n\tflag_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08\x66lagMask\x12;\n\x0b\x66ilter_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nfilterMask\x12\x1b\n\tflag_sids\x18\x06 \x03(\x03R\x08\x66lagSids\"\x89\x01\n\x17ListFlagFiltersResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x46\n\x0c\x66lag_filters\x18\x02 \x03(\x0b\x32#.api.v1alpha1.vanalytics.FlagFilterR\x0b\x66lagFilters\"e\n\x17\x44\x65leteFlagFilterRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x1d\n\nfilter_sid\x18\x02 \x01(\x03R\tfilterSid\x12\x10\n\x03\x61ll\x18\x03 \x01(\x08R\x03\x61ll\"\x1a\n\x18\x44\x65leteFlagFilterResponse\"\xda\x01\n\nFlagFilter\x12&\n\x0f\x66lag_filter_sid\x18\x01 \x01(\x03R\rflagFilterSid\x12\x1d\n\nfilter_sid\x18\x02 \x01(\x03R\tfilterSid\x12\x19\n\x08\x66lag_sid\x18\x03 \x01(\x03R\x07\x66lagSid\x12\x31\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x04\x66lag\x12\x37\n\x06\x66ilter\x18\x06 \x01(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x06\x66ilterB\xac\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0f\x46lagFilterProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\017FlagFilterProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_CREATEFLAGFILTERREQUEST']._serialized_start=178
  _globals['_CREATEFLAGFILTERREQUEST']._serialized_end=273
  _globals['_LISTFLAGFILTERSREQUEST']._serialized_start=276
  _globals['_LISTFLAGFILTERSREQUEST']._serialized_end=507
  _globals['_LISTFLAGFILTERSRESPONSE']._serialized_start=510
  _globals['_LISTFLAGFILTERSRESPONSE']._serialized_end=647
  _globals['_DELETEFLAGFILTERREQUEST']._serialized_start=649
  _globals['_DELETEFLAGFILTERREQUEST']._serialized_end=750
  _globals['_DELETEFLAGFILTERRESPONSE']._serialized_start=752
  _globals['_DELETEFLAGFILTERRESPONSE']._serialized_end=778
  _globals['_FLAGFILTER']._serialized_start=781
  _globals['_FLAGFILTER']._serialized_end=999
# @@protoc_insertion_point(module_scope)
