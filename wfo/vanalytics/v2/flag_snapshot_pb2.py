# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/flag_snapshot.proto
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
    'wfo/vanalytics/v2/flag_snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from wfo.vanalytics.v2 import dncl_list_pb2 as wfo_dot_vanalytics_dot_v2_dot_dncl__list__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%wfo/vanalytics/v2/flag_snapshot.proto\x12\x11wfo.vanalytics.v2\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!wfo/vanalytics/v2/dncl_list.proto\"\xf6\x01\n\x18ListFlagSnapshotsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12,\n\x12\x66lag_snapshot_sids\x18\x05 \x03(\x03R\x10\x66lagSnapshotSids\x12.\n\x04mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12%\n\x0etranscript_sid\x18\x07 \x01(\x03R\rtranscriptSid\"\x8b\x01\n\x19ListFlagSnapshotsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x46\n\x0e\x66lag_snapshots\x18\x02 \x03(\x0b\x32\x1f.wfo.vanalytics.v2.FlagSnapshotR\rflagSnapshots\"\xa0\x06\n\x0c\x46lagSnapshot\x12*\n\x11\x66lag_snapshot_sid\x18\x01 \x01(\x03R\x0f\x66lagSnapshotSid\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12&\n\x0freview_group_id\x18\x05 \x01(\tR\rreviewGroupId\x12&\n\x0fnotify_group_id\x18\x06 \x01(\tR\rnotifyGroupId\x12\x1a\n\x08priority\x18\x07 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x08 \x01(\x03R\x07version\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x1f\n\x0bmust_review\x18\n \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x0b \x01(\x08R\nmustNotify\x12\x45\n\tbool_expr\x18\x0c \x01(\x0b\x32(.wfo.vanalytics.v2.FlagSnapshot.BoolExprR\x08\x62oolExpr\x12\x38\n\tdncl_list\x18\r \x03(\x0b\x32\x1b.wfo.vanalytics.v2.DnclListR\x08\x64nclList\x1a\xae\x02\n\x08\x42oolExpr\x12:\n\x03\x61nd\x18\x01 \x03(\x0b\x32(.wfo.vanalytics.v2.FlagSnapshot.BoolExprR\x03\x61nd\x12\x38\n\x02or\x18\x02 \x03(\x0b\x32(.wfo.vanalytics.v2.FlagSnapshot.BoolExprR\x02or\x12G\n\x06\x66ilter\x18\x03 \x01(\x0b\x32/.wfo.vanalytics.v2.FlagSnapshot.BoolExpr.FilterR\x06\x66ilter\x12:\n\x03not\x18\x04 \x01(\x0b\x32(.wfo.vanalytics.v2.FlagSnapshot.BoolExprR\x03not\x1a\'\n\x06\x46ilter\x12\x1d\n\nfilter_sid\x18\x01 \x01(\x03R\tfilterSidB\x90\x01\n\x15\x63om.wfo.vanalytics.v2B\x11\x46lagSnapshotProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.flag_snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\021FlagSnapshotProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_LISTFLAGSNAPSHOTSREQUEST']._serialized_start=163
  _globals['_LISTFLAGSNAPSHOTSREQUEST']._serialized_end=409
  _globals['_LISTFLAGSNAPSHOTSRESPONSE']._serialized_start=412
  _globals['_LISTFLAGSNAPSHOTSRESPONSE']._serialized_end=551
  _globals['_FLAGSNAPSHOT']._serialized_start=554
  _globals['_FLAGSNAPSHOT']._serialized_end=1354
  _globals['_FLAGSNAPSHOT_BOOLEXPR']._serialized_start=1052
  _globals['_FLAGSNAPSHOT_BOOLEXPR']._serialized_end=1354
  _globals['_FLAGSNAPSHOT_BOOLEXPR_FILTER']._serialized_start=1315
  _globals['_FLAGSNAPSHOT_BOOLEXPR_FILTER']._serialized_end=1354
# @@protoc_insertion_point(module_scope)
