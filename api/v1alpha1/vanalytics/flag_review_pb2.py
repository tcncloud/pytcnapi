# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/flag_review.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'api/v1alpha1/vanalytics/flag_review.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/v1alpha1/vanalytics/flag_review.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x1fgoogle/protobuf/timestamp.proto\"_\n\x17\x43reateFlagReviewRequest\x12\x44\n\x0b\x66lag_review\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.FlagReviewR\nflagReview\"N\n\x1b\x42ulkCreateFlagReviewRequest\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x14\n\x05notes\x18\x02 \x01(\tR\x05notes\"\x1e\n\x1c\x42ulkCreateFlagReviewResponse\"\x96\x01\n\x16ListFlagReviewsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12%\n\x0etranscript_sid\x18\x05 \x01(\x03R\rtranscriptSid\"\x89\x01\n\x17ListFlagReviewsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x46\n\x0c\x66lag_reviews\x18\x02 \x03(\x0b\x32#.api.v1alpha1.vanalytics.FlagReviewR\x0b\x66lagReviews\"\xf9\x01\n\nFlagReview\x12&\n\x0f\x66lag_review_sid\x18\x01 \x01(\x03R\rflagReviewSid\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\x12\x1d\n\x08\x66lag_sid\x18\x03 \x01(\x03\x42\x02\x18\x01R\x07\x66lagSid\x12;\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x14\n\x05notes\x18\x05 \x01(\tR\x05notes\x12*\n\x11\x66lag_snapshot_sid\x18\x08 \x01(\x03R\x0f\x66lagSnapshotSidB\xac\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0f\x46lagReviewProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_review_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\017FlagReviewProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_FLAGREVIEW'].fields_by_name['flag_sid']._loaded_options = None
  _globals['_FLAGREVIEW'].fields_by_name['flag_sid']._serialized_options = b'\030\001'
  _globals['_CREATEFLAGREVIEWREQUEST']._serialized_start=103
  _globals['_CREATEFLAGREVIEWREQUEST']._serialized_end=198
  _globals['_BULKCREATEFLAGREVIEWREQUEST']._serialized_start=200
  _globals['_BULKCREATEFLAGREVIEWREQUEST']._serialized_end=278
  _globals['_BULKCREATEFLAGREVIEWRESPONSE']._serialized_start=280
  _globals['_BULKCREATEFLAGREVIEWRESPONSE']._serialized_end=310
  _globals['_LISTFLAGREVIEWSREQUEST']._serialized_start=313
  _globals['_LISTFLAGREVIEWSREQUEST']._serialized_end=463
  _globals['_LISTFLAGREVIEWSRESPONSE']._serialized_start=466
  _globals['_LISTFLAGREVIEWSRESPONSE']._serialized_end=603
  _globals['_FLAGREVIEW']._serialized_start=606
  _globals['_FLAGREVIEW']._serialized_end=855
# @@protoc_insertion_point(module_scope)
