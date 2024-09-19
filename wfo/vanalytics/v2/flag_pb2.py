# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/flag.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'wfo/vanalytics/v2/flag.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from wfo.vanalytics.v2 import dncl_list_pb2 as wfo_dot_vanalytics_dot_v2_dot_dncl__list__pb2
from wfo.vanalytics.v2 import filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_filter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwfo/vanalytics/v2/flag.proto\x12\x11wfo.vanalytics.v2\x1a google/protobuf/field_mask.proto\x1a!wfo/vanalytics/v2/dncl_list.proto\x1a\x1ewfo/vanalytics/v2/filter.proto\"@\n\x11\x43reateFlagRequest\x12+\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x04\x66lag\"\xe1\x02\n\x10ListFlagsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1f\n\nfilter_sid\x18\x05 \x01(\x03H\x00R\tfilterSid\x12\x1b\n\tflag_sids\x18\x06 \x03(\x03R\x08\x66lagSids\x12\x37\n\tread_mask\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12\x14\n\x05names\x18\x08 \x03(\tR\x05names\x12\x1e\n\npriorities\x18\t \x03(\x05R\npriorities\x12\x1f\n\x0bmust_review\x18\n \x03(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x0b \x03(\x08R\nmustNotifyB\x07\n\x05where\"\x80\x01\n\x11ListFlagsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12-\n\x05\x66lags\x18\x02 \x03(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x05\x66lags\x12\x14\n\x05total\x18\x03 \x01(\x04R\x05total\"\x98\x01\n\x11UpdateFlagRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12+\n\x04\x66lag\x18\x02 \x01(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x04\x66lag\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"F\n\x11\x44\x65leteFlagRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x16\n\x06return\x18\x03 \x01(\x08R\x06return\"A\n\x12\x44\x65leteFlagResponse\x12+\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x04\x66lag\"L\n\x0eGetFlagRequest\x12\x14\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x12\x1b\n\x08\x66lag_sid\x18\x03 \x01(\x03H\x00R\x07\x66lagSidB\x07\n\x05where\"\xbc\x05\n\x04\x46lag\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12&\n\x0freview_group_id\x18\x04 \x01(\tR\rreviewGroupId\x12&\n\x0fnotify_group_id\x18\x05 \x01(\tR\rnotifyGroupId\x12\x1a\n\x08priority\x18\x06 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x07 \x01(\x03R\x07version\x12\x33\n\x07\x66ilters\x18\x08 \x03(\x0b\x32\x19.wfo.vanalytics.v2.FilterR\x07\x66ilters\x12\x1f\n\x0bmust_review\x18\t \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\n \x01(\x08R\nmustNotify\x12=\n\tbool_expr\x18\x0b \x01(\x0b\x32 .wfo.vanalytics.v2.Flag.BoolExprR\x08\x62oolExpr\x12\x38\n\tdncl_list\x18\x0c \x03(\x0b\x32\x1b.wfo.vanalytics.v2.DnclListR\x08\x64nclList\x1a\x8e\x02\n\x08\x42oolExpr\x12\x32\n\x03\x61nd\x18\x01 \x03(\x0b\x32 .wfo.vanalytics.v2.Flag.BoolExprR\x03\x61nd\x12\x30\n\x02or\x18\x02 \x03(\x0b\x32 .wfo.vanalytics.v2.Flag.BoolExprR\x02or\x12?\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\'.wfo.vanalytics.v2.Flag.BoolExpr.FilterR\x06\x66ilter\x12\x32\n\x03not\x18\x04 \x01(\x0b\x32 .wfo.vanalytics.v2.Flag.BoolExprR\x03not\x1a\'\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSidB\x88\x01\n\x15\x63om.wfo.vanalytics.v2B\tFlagProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.flag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\tFlagProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_CREATEFLAGREQUEST']._serialized_start=152
  _globals['_CREATEFLAGREQUEST']._serialized_end=216
  _globals['_LISTFLAGSREQUEST']._serialized_start=219
  _globals['_LISTFLAGSREQUEST']._serialized_end=572
  _globals['_LISTFLAGSRESPONSE']._serialized_start=575
  _globals['_LISTFLAGSRESPONSE']._serialized_end=703
  _globals['_UPDATEFLAGREQUEST']._serialized_start=706
  _globals['_UPDATEFLAGREQUEST']._serialized_end=858
  _globals['_DELETEFLAGREQUEST']._serialized_start=860
  _globals['_DELETEFLAGREQUEST']._serialized_end=930
  _globals['_DELETEFLAGRESPONSE']._serialized_start=932
  _globals['_DELETEFLAGRESPONSE']._serialized_end=997
  _globals['_GETFLAGREQUEST']._serialized_start=999
  _globals['_GETFLAGREQUEST']._serialized_end=1075
  _globals['_FLAG']._serialized_start=1078
  _globals['_FLAG']._serialized_end=1778
  _globals['_FLAG_BOOLEXPR']._serialized_start=1508
  _globals['_FLAG_BOOLEXPR']._serialized_end=1778
  _globals['_FLAG_BOOLEXPR_FILTER']._serialized_start=1739
  _globals['_FLAG_BOOLEXPR_FILTER']._serialized_end=1778
# @@protoc_insertion_point(module_scope)
