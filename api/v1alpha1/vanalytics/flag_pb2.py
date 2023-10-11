# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vanalytics/flag.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import filter_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_filter__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/vanalytics/flag.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a$api/v1alpha1/vanalytics/filter.proto\x1a google/protobuf/field_mask.proto\"F\n\x11\x43reateFlagRequest\x12\x31\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x04\x66lag\"\xe1\x02\n\x10ListFlagsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x1f\n\nfilter_sid\x18\x05 \x01(\x03H\x00R\tfilterSid\x12\x1b\n\tflag_sids\x18\x06 \x03(\x03R\x08\x66lagSids\x12\x37\n\tread_mask\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12\x14\n\x05names\x18\x08 \x03(\tR\x05names\x12\x1e\n\npriorities\x18\t \x03(\x05R\npriorities\x12\x1f\n\x0bmust_review\x18\n \x03(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x0b \x03(\x08R\nmustNotifyB\x07\n\x05where\"\x86\x01\n\x11ListFlagsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x33\n\x05\x66lags\x18\x02 \x03(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x05\x66lags\x12\x14\n\x05total\x18\x03 \x01(\x04R\x05total\"\x9e\x01\n\x11UpdateFlagRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x31\n\x04\x66lag\x18\x02 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x04\x66lag\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"F\n\x11\x44\x65leteFlagRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x16\n\x06return\x18\x03 \x01(\x08R\x06return\"G\n\x12\x44\x65leteFlagResponse\x12\x31\n\x04\x66lag\x18\x01 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x04\x66lag\"L\n\x0eGetFlagRequest\x12\x14\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x12\x1b\n\x08\x66lag_sid\x18\x03 \x01(\x03H\x00R\x07\x66lagSidB\x07\n\x05where\"\xa6\x05\n\x04\x46lag\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12&\n\x0freview_group_id\x18\x04 \x01(\tR\rreviewGroupId\x12&\n\x0fnotify_group_id\x18\x05 \x01(\tR\rnotifyGroupId\x12\x1a\n\x08priority\x18\x06 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x07 \x01(\x03R\x07version\x12\x39\n\x07\x66ilters\x18\x08 \x03(\x0b\x32\x1f.api.v1alpha1.vanalytics.FilterR\x07\x66ilters\x12\x1f\n\x0bmust_review\x18\t \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\n \x01(\x08R\nmustNotify\x12\x43\n\tbool_expr\x18\x0b \x01(\x0b\x32&.api.v1alpha1.vanalytics.Flag.BoolExprR\x08\x62oolExpr\x1a\xa6\x02\n\x08\x42oolExpr\x12\x38\n\x03\x61nd\x18\x01 \x03(\x0b\x32&.api.v1alpha1.vanalytics.Flag.BoolExprR\x03\x61nd\x12\x36\n\x02or\x18\x02 \x03(\x0b\x32&.api.v1alpha1.vanalytics.Flag.BoolExprR\x02or\x12\x45\n\x06\x66ilter\x18\x03 \x01(\x0b\x32-.api.v1alpha1.vanalytics.Flag.BoolExpr.FilterR\x06\x66ilter\x12\x38\n\x03not\x18\x04 \x01(\x0b\x32&.api.v1alpha1.vanalytics.Flag.BoolExprR\x03not\x1a\'\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSidB\xa6\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\tFlagProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\tFlagProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_CREATEFLAGREQUEST']._serialized_start=135
  _globals['_CREATEFLAGREQUEST']._serialized_end=205
  _globals['_LISTFLAGSREQUEST']._serialized_start=208
  _globals['_LISTFLAGSREQUEST']._serialized_end=561
  _globals['_LISTFLAGSRESPONSE']._serialized_start=564
  _globals['_LISTFLAGSRESPONSE']._serialized_end=698
  _globals['_UPDATEFLAGREQUEST']._serialized_start=701
  _globals['_UPDATEFLAGREQUEST']._serialized_end=859
  _globals['_DELETEFLAGREQUEST']._serialized_start=861
  _globals['_DELETEFLAGREQUEST']._serialized_end=931
  _globals['_DELETEFLAGRESPONSE']._serialized_start=933
  _globals['_DELETEFLAGRESPONSE']._serialized_end=1004
  _globals['_GETFLAGREQUEST']._serialized_start=1006
  _globals['_GETFLAGREQUEST']._serialized_end=1082
  _globals['_FLAG']._serialized_start=1085
  _globals['_FLAG']._serialized_end=1763
  _globals['_FLAG_BOOLEXPR']._serialized_start=1469
  _globals['_FLAG_BOOLEXPR']._serialized_end=1763
  _globals['_FLAG_BOOLEXPR_FILTER']._serialized_start=1724
  _globals['_FLAG_BOOLEXPR_FILTER']._serialized_end=1763
# @@protoc_insertion_point(module_scope)
