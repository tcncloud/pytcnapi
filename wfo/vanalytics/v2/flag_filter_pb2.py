# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/flag_filter.proto
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
    'wfo/vanalytics/v2/flag_filter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from wfo.vanalytics.v2 import filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_filter__pb2
from wfo.vanalytics.v2 import flag_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#wfo/vanalytics/v2/flag_filter.proto\x12\x11wfo.vanalytics.v2\x1a google/protobuf/field_mask.proto\x1a\x1ewfo/vanalytics/v2/filter.proto\x1a\x1cwfo/vanalytics/v2/flag.proto\"\xe7\x01\n\x16ListFlagFiltersRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x37\n\tflag_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08\x66lagMask\x12;\n\x0b\x66ilter_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nfilterMask\x12\x1b\n\tflag_sids\x18\x06 \x03(\x03R\x08\x66lagSids\"\x83\x01\n\x17ListFlagFiltersResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12@\n\x0c\x66lag_filters\x18\x02 \x03(\x0b\x32\x1d.wfo.vanalytics.v2.FlagFilterR\x0b\x66lagFilters\"\xce\x01\n\nFlagFilter\x12&\n\x0f\x66lag_filter_sid\x18\x01 \x01(\x03R\rflagFilterSid\x12\x1d\n\nfilter_sid\x18\x02 \x01(\x03R\tfilterSid\x12\x19\n\x08\x66lag_sid\x18\x03 \x01(\x03R\x07\x66lagSid\x12+\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x04\x66lag\x12\x31\n\x06\x66ilter\x18\x06 \x01(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x06\x66ilterB\x8e\x01\n\x15\x63om.wfo.vanalytics.v2B\x0f\x46lagFilterProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.flag_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\017FlagFilterProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_LISTFLAGFILTERSREQUEST']._serialized_start=155
  _globals['_LISTFLAGFILTERSREQUEST']._serialized_end=386
  _globals['_LISTFLAGFILTERSRESPONSE']._serialized_start=389
  _globals['_LISTFLAGFILTERSRESPONSE']._serialized_end=520
  _globals['_FLAGFILTER']._serialized_start=523
  _globals['_FLAGFILTER']._serialized_end=729
# @@protoc_insertion_point(module_scope)
