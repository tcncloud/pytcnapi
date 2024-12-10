# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/flag_snapshot.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'api/v1alpha1/vanalytics/flag_snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import dncl_list_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_dncl__list__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+api/v1alpha1/vanalytics/flag_snapshot.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\'api/v1alpha1/vanalytics/dncl_list.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf6\x01\n\x18ListFlagSnapshotsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12,\n\x12\x66lag_snapshot_sids\x18\x05 \x03(\x03R\x10\x66lagSnapshotSids\x12.\n\x04mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12%\n\x0etranscript_sid\x18\x07 \x01(\x03R\rtranscriptSid\"\x91\x01\n\x19ListFlagSnapshotsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12L\n\x0e\x66lag_snapshots\x18\x02 \x03(\x0b\x32%.api.v1alpha1.vanalytics.FlagSnapshotR\rflagSnapshots\"\xc4\x06\n\x0c\x46lagSnapshot\x12*\n\x11\x66lag_snapshot_sid\x18\x01 \x01(\x03R\x0f\x66lagSnapshotSid\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12&\n\x0freview_group_id\x18\x05 \x01(\tR\rreviewGroupId\x12&\n\x0fnotify_group_id\x18\x06 \x01(\tR\rnotifyGroupId\x12\x1a\n\x08priority\x18\x07 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x08 \x01(\x03R\x07version\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x1f\n\x0bmust_review\x18\n \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x0b \x01(\x08R\nmustNotify\x12K\n\tbool_expr\x18\x0c \x01(\x0b\x32..api.v1alpha1.vanalytics.FlagSnapshot.BoolExprR\x08\x62oolExpr\x12>\n\tdncl_list\x18\r \x03(\x0b\x32!.api.v1alpha1.vanalytics.DnclListR\x08\x64nclList\x1a\xc6\x02\n\x08\x42oolExpr\x12@\n\x03\x61nd\x18\x01 \x03(\x0b\x32..api.v1alpha1.vanalytics.FlagSnapshot.BoolExprR\x03\x61nd\x12>\n\x02or\x18\x02 \x03(\x0b\x32..api.v1alpha1.vanalytics.FlagSnapshot.BoolExprR\x02or\x12M\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x35.api.v1alpha1.vanalytics.FlagSnapshot.BoolExpr.FilterR\x06\x66ilter\x12@\n\x03not\x18\x04 \x01(\x0b\x32..api.v1alpha1.vanalytics.FlagSnapshot.BoolExprR\x03not\x1a\'\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSidB\xae\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x11\x46lagSnapshotProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\021FlagSnapshotProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_LISTFLAGSNAPSHOTSREQUEST']._serialized_start=181
  _globals['_LISTFLAGSNAPSHOTSREQUEST']._serialized_end=427
  _globals['_LISTFLAGSNAPSHOTSRESPONSE']._serialized_start=430
  _globals['_LISTFLAGSNAPSHOTSRESPONSE']._serialized_end=575
  _globals['_FLAGSNAPSHOT']._serialized_start=578
  _globals['_FLAGSNAPSHOT']._serialized_end=1414
  _globals['_FLAGSNAPSHOT_BOOLEXPR']._serialized_start=1088
  _globals['_FLAGSNAPSHOT_BOOLEXPR']._serialized_end=1414
  _globals['_FLAGSNAPSHOT_BOOLEXPR_FILTER']._serialized_start=1375
  _globals['_FLAGSNAPSHOT_BOOLEXPR_FILTER']._serialized_end=1414
# @@protoc_insertion_point(module_scope)
