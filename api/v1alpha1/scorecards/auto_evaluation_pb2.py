# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/auto_evaluation.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/v1alpha1/scorecards/auto_evaluation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/scorecards/auto_evaluation.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1c\x61pi/commons/scorecards.proto\"H\n\x18GetAutoEvaluationRequest\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\"a\n\x19GetAutoEvaluationResponse\x12\x44\n\x0f\x61uto_evaluation\x18\x01 \x01(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0e\x61utoEvaluation\"\xef\x04\n\x1aListAutoEvaluationsRequest\x12#\n\rscorecard_ids\x18\x02 \x03(\x03R\x0cscorecardIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x05 \x03(\x03R\x0b\x63\x61tegoryIds\x12\\\n\x08\x63\x61ll_sid\x18\x06 \x01(\x0b\x32\x41.api.v1alpha1.scorecards.ListAutoEvaluationsRequest.CallSidFilterR\x07\x63\x61llSid\x12$\n\x0e\x61gent_user_ids\x18\x07 \x03(\tR\x0c\x61gentUserIds\x12\x1b\n\tpage_size\x18\x08 \x01(\x05R\x08pageSize\x12\x19\n\x08order_by\x18\t \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\n \x01(\tR\tpageToken\x12\x37\n\x0brisk_levels\x18\x0b \x03(\x0e\x32\x16.api.commons.RiskLevelR\nriskLevels\x12=\n\rchannel_types\x18\x0c \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x0c\x63hannelTypes\x1az\n\rCallSidFilter\x12\x15\n\x06\x61ny_of\x18\x01 \x03(\x03R\x05\x61nyOf\x12\x0e\n\x02\x65q\x18\x02 \x01(\x03R\x02\x65q\x12\x10\n\x03gte\x18\x03 \x01(\x03R\x03gte\x12\x10\n\x03lte\x18\x04 \x01(\x03R\x03lte\x12\x0e\n\x02gt\x18\x05 \x01(\x03R\x02gt\x12\x0e\n\x02lt\x18\x06 \x01(\x03R\x02lt\"\x8d\x01\n\x1bListAutoEvaluationsResponse\x12\x46\n\x10\x61uto_evaluations\x18\x01 \x03(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0f\x61utoEvaluations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"K\n\x1b\x44\x65leteAutoEvaluationRequest\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\"d\n\x1c\x44\x65leteAutoEvaluationResponse\x12\x44\n\x0f\x61uto_evaluation\x18\x01 \x01(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0e\x61utoEvaluation\"\x7f\n\x1cStreamAutoEvaluationsRequest\x12#\n\rscorecard_ids\x18\x02 \x03(\x03R\x0cscorecardIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\"e\n\x1dStreamAutoEvaluationsResponse\x12\x44\n\x0f\x61uto_evaluation\x18\x01 \x01(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0e\x61utoEvaluation\"\xd5\x04\n!ListAutoEvaluationsByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12#\n\rscorecard_ids\x18\x02 \x03(\x03R\x0cscorecardIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x05 \x03(\x03R\x0b\x63\x61tegoryIds\x12\x63\n\x08\x63\x61ll_sid\x18\x06 \x01(\x0b\x32H.api.v1alpha1.scorecards.ListAutoEvaluationsByOrgIdRequest.CallSidFilterR\x07\x63\x61llSid\x12$\n\x0e\x61gent_user_ids\x18\x07 \x03(\tR\x0c\x61gentUserIds\x12\x1b\n\tpage_size\x18\x08 \x01(\x05R\x08pageSize\x12\x19\n\x08order_by\x18\t \x01(\tR\x07orderBy\x12\x1d\n\npage_token\x18\n \x01(\tR\tpageToken\x12\x37\n\x0brisk_levels\x18\x0b \x03(\x0e\x32\x16.api.commons.RiskLevelR\nriskLevels\x1az\n\rCallSidFilter\x12\x15\n\x06\x61ny_of\x18\x01 \x03(\x03R\x05\x61nyOf\x12\x0e\n\x02\x65q\x18\x02 \x01(\x03R\x02\x65q\x12\x10\n\x03gte\x18\x03 \x01(\x03R\x03gte\x12\x10\n\x03lte\x18\x04 \x01(\x03R\x03lte\x12\x0e\n\x02gt\x18\x05 \x01(\x03R\x02gt\x12\x0e\n\x02lt\x18\x06 \x01(\x03R\x02lt\"i\n\"DeleteAutoEvaluationByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\"\xcc\x02\n BulkDeleteAutoEvaluationsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12.\n\x13\x61uto_evaluation_ids\x18\x02 \x03(\x03R\x11\x61utoEvaluationIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12#\n\rscorecard_ids\x18\x04 \x03(\x03R\x0cscorecardIds\x12!\n\x0c\x63\x61tegory_ids\x18\x05 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x06 \x03(\tR\x0c\x61gentUserIds\x12\x37\n\x0brisk_levels\x18\x07 \x03(\x0e\x32\x16.api.commons.RiskLevelR\nriskLevels\"9\n!BulkDeleteAutoEvaluationsResponse\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ountB\xb0\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x13\x41utoEvaluationProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.auto_evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\023AutoEvaluationProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_GETAUTOEVALUATIONREQUEST']._serialized_start=135
  _globals['_GETAUTOEVALUATIONREQUEST']._serialized_end=207
  _globals['_GETAUTOEVALUATIONRESPONSE']._serialized_start=209
  _globals['_GETAUTOEVALUATIONRESPONSE']._serialized_end=306
  _globals['_LISTAUTOEVALUATIONSREQUEST']._serialized_start=309
  _globals['_LISTAUTOEVALUATIONSREQUEST']._serialized_end=932
  _globals['_LISTAUTOEVALUATIONSREQUEST_CALLSIDFILTER']._serialized_start=810
  _globals['_LISTAUTOEVALUATIONSREQUEST_CALLSIDFILTER']._serialized_end=932
  _globals['_LISTAUTOEVALUATIONSRESPONSE']._serialized_start=935
  _globals['_LISTAUTOEVALUATIONSRESPONSE']._serialized_end=1076
  _globals['_DELETEAUTOEVALUATIONREQUEST']._serialized_start=1078
  _globals['_DELETEAUTOEVALUATIONREQUEST']._serialized_end=1153
  _globals['_DELETEAUTOEVALUATIONRESPONSE']._serialized_start=1155
  _globals['_DELETEAUTOEVALUATIONRESPONSE']._serialized_end=1255
  _globals['_STREAMAUTOEVALUATIONSREQUEST']._serialized_start=1257
  _globals['_STREAMAUTOEVALUATIONSREQUEST']._serialized_end=1384
  _globals['_STREAMAUTOEVALUATIONSRESPONSE']._serialized_start=1386
  _globals['_STREAMAUTOEVALUATIONSRESPONSE']._serialized_end=1487
  _globals['_LISTAUTOEVALUATIONSBYORGIDREQUEST']._serialized_start=1490
  _globals['_LISTAUTOEVALUATIONSBYORGIDREQUEST']._serialized_end=2087
  _globals['_LISTAUTOEVALUATIONSBYORGIDREQUEST_CALLSIDFILTER']._serialized_start=810
  _globals['_LISTAUTOEVALUATIONSBYORGIDREQUEST_CALLSIDFILTER']._serialized_end=932
  _globals['_DELETEAUTOEVALUATIONBYORGIDREQUEST']._serialized_start=2089
  _globals['_DELETEAUTOEVALUATIONBYORGIDREQUEST']._serialized_end=2194
  _globals['_BULKDELETEAUTOEVALUATIONSREQUEST']._serialized_start=2197
  _globals['_BULKDELETEAUTOEVALUATIONSREQUEST']._serialized_end=2529
  _globals['_BULKDELETEAUTOEVALUATIONSRESPONSE']._serialized_start=2531
  _globals['_BULKDELETEAUTOEVALUATIONSRESPONSE']._serialized_end=2588
# @@protoc_insertion_point(module_scope)
