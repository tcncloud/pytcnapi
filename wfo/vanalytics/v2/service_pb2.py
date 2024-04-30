# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfo/vanalytics/v2/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from wfo.vanalytics.v2 import filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_filter__pb2
from wfo.vanalytics.v2 import flag_filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__filter__pb2
from wfo.vanalytics.v2 import flag_transcript_filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__transcript__filter__pb2
from wfo.vanalytics.v2 import transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwfo/vanalytics/v2/service.proto\x12\x11wfo.vanalytics.v2\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ewfo/vanalytics/v2/filter.proto\x1a#wfo/vanalytics/v2/flag_filter.proto\x1a.wfo/vanalytics/v2/flag_transcript_filter.proto\x1a\"wfo/vanalytics/v2/transcript.proto2\xe8\t\n\nVanalytics\x12\xa9\x01\n\x11SearchTranscripts\x12+.wfo.vanalytics.v2.SearchTranscriptsRequest\x1a,.wfo.vanalytics.v2.SearchTranscriptsResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02)\"$/wfo/vanalytics/v2/searchtranscripts:\x01*\x12\x87\x01\n\x0c\x43reateFilter\x12&.wfo.vanalytics.v2.CreateFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/createfilter:\x01*\x12\x91\x01\n\x0bListFilters\x12%.wfo.vanalytics.v2.ListFiltersRequest\x1a&.wfo.vanalytics.v2.ListFiltersResponse\"3\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02#\"\x1e/wfo/vanalytics/v2/listfilters:\x01*\x12\x87\x01\n\x0cUpdateFilter\x12&.wfo.vanalytics.v2.UpdateFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/updatefilter:\x01*\x12\x95\x01\n\x0c\x44\x65leteFilter\x12&.wfo.vanalytics.v2.DeleteFilterRequest\x1a\'.wfo.vanalytics.v2.DeleteFilterResponse\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/deletefilter:\x01*\x12~\n\tGetFilter\x12#.wfo.vanalytics.v2.GetFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"1\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02!\"\x1c/wfo/vanalytics/v2/getfilter:\x01*\x12\xc9\x01\n\x19ListFlagTranscriptFilters\x12\x33.wfo.vanalytics.v2.ListFlagTranscriptFiltersRequest\x1a\x34.wfo.vanalytics.v2.ListFlagTranscriptFiltersResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x31\",/wfo/vanalytics/v2/listflagtranscriptfilters:\x01*\x12\xa1\x01\n\x0fListFlagFilters\x12).wfo.vanalytics.v2.ListFlagFiltersRequest\x1a*.wfo.vanalytics.v2.ListFlagFiltersResponse\"7\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/listflagfilters:\x01*B\x8b\x01\n\x15\x63om.wfo.vanalytics.v2B\x0cServiceProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\014ServiceProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_VANALYTICS'].methods_by_name['SearchTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['SearchTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002)\"$/wfo/vanalytics/v2/searchtranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/createfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002#\"\036/wfo/vanalytics/v2/listfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/updatefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/deletefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002!\"\034/wfo/vanalytics/v2/getfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0021\",/wfo/vanalytics/v2/listflagtranscriptfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/listflagfilters:\001*'
  _globals['_VANALYTICS']._serialized_start=263
  _globals['_VANALYTICS']._serialized_end=1519
# @@protoc_insertion_point(module_scope)
