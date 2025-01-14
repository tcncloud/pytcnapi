# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/support_service.proto
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
    'api/v1alpha1/scorecards/support_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.scorecards import auto_evaluation_pb2 as api_dot_v1alpha1_dot_scorecards_dot_auto__evaluation__pb2
from api.v1alpha1.scorecards import category_pb2 as api_dot_v1alpha1_dot_scorecards_dot_category__pb2
from api.v1alpha1.scorecards import evaluation_pb2 as api_dot_v1alpha1_dot_scorecards_dot_evaluation__pb2
from api.v1alpha1.scorecards import scorecard_pb2 as api_dot_v1alpha1_dot_scorecards_dot_scorecard__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/scorecards/support_service.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x17\x61nnotations/authz.proto\x1a-api/v1alpha1/scorecards/auto_evaluation.proto\x1a&api/v1alpha1/scorecards/category.proto\x1a(api/v1alpha1/scorecards/evaluation.proto\x1a\'api/v1alpha1/scorecards/scorecard.proto\x1a\x1cgoogle/api/annotations.proto2\xb1\x0e\n\x11ScorecardsSupport\x12\xda\x01\n\x16ListEvaluationsByOrgId\x12\x36.api.v1alpha1.scorecards.ListEvaluationsByOrgIdRequest\x1a\x30.api.v1alpha1.scorecards.ListEvaluationsResponse\"V\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x46\"A/api/v1alpha1/scorecards/scorecardssupport/listevaluationsbyorgid:\x01*\x12\xea\x01\n\x1aListAutoEvaluationsByOrgId\x12:.api.v1alpha1.scorecards.ListAutoEvaluationsByOrgIdRequest\x1a\x34.api.v1alpha1.scorecards.ListAutoEvaluationsResponse\"Z\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02J\"E/api/v1alpha1/scorecards/scorecardssupport/listautoevaluationsbyorgid:\x01*\x12\xdd\x01\n\x15\x42ulkDeleteEvaluations\x12\x35.api.v1alpha1.scorecards.BulkDeleteEvaluationsRequest\x1a\x36.api.v1alpha1.scorecards.BulkDeleteEvaluationsResponse\"U\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x45\"@/api/v1alpha1/scorecards/scorecardssupport/bulkdeleteevaluations:\x01*\x12\xed\x01\n\x19\x42ulkDeleteAutoEvaluations\x12\x39.api.v1alpha1.scorecards.BulkDeleteAutoEvaluationsRequest\x1a:.api.v1alpha1.scorecards.BulkDeleteAutoEvaluationsResponse\"Y\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02I\"D/api/v1alpha1/scorecards/scorecardssupport/bulkdeleteautoevaluations:\x01*\x12\xde\x01\n\x17\x44\x65leteEvaluationByOrgId\x12\x37.api.v1alpha1.scorecards.DeleteEvaluationByOrgIdRequest\x1a\x31.api.v1alpha1.scorecards.DeleteEvaluationResponse\"W\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02G\"B/api/v1alpha1/scorecards/scorecardssupport/deleteevaluationbyorgid:\x01*\x12\xee\x01\n\x1b\x44\x65leteAutoEvaluationByOrgId\x12;.api.v1alpha1.scorecards.DeleteAutoEvaluationByOrgIdRequest\x1a\x35.api.v1alpha1.scorecards.DeleteAutoEvaluationResponse\"[\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02K\"F/api/v1alpha1/scorecards/scorecardssupport/deleteautoevaluationbyorgid:\x01*\x12\xd6\x01\n\x15ListScorecardsByOrgId\x12\x35.api.v1alpha1.scorecards.ListScorecardsByOrgIdRequest\x1a/.api.v1alpha1.scorecards.ListScorecardsResponse\"U\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x45\"@/api/v1alpha1/scorecards/scorecardssupport/listscorecardsbyorgid:\x01*\x12\xd6\x01\n\x15ListCategoriesByOrgId\x12\x35.api.v1alpha1.scorecards.ListCategoriesByOrgIdRequest\x1a/.api.v1alpha1.scorecards.ListCategoriesResponse\"U\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x45\"@/api/v1alpha1/scorecards/scorecardssupport/listcategoriesbyorgid:\x01*B\xb0\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x13SupportServiceProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.support_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\023SupportServiceProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListEvaluationsByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListEvaluationsByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002F\"A/api/v1alpha1/scorecards/scorecardssupport/listevaluationsbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListAutoEvaluationsByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListAutoEvaluationsByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002J\"E/api/v1alpha1/scorecards/scorecardssupport/listautoevaluationsbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['BulkDeleteEvaluations']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['BulkDeleteEvaluations']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002E\"@/api/v1alpha1/scorecards/scorecardssupport/bulkdeleteevaluations:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['BulkDeleteAutoEvaluations']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['BulkDeleteAutoEvaluations']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002I\"D/api/v1alpha1/scorecards/scorecardssupport/bulkdeleteautoevaluations:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['DeleteEvaluationByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['DeleteEvaluationByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002G\"B/api/v1alpha1/scorecards/scorecardssupport/deleteevaluationbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['DeleteAutoEvaluationByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['DeleteAutoEvaluationByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002K\"F/api/v1alpha1/scorecards/scorecardssupport/deleteautoevaluationbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListScorecardsByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListScorecardsByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002E\"@/api/v1alpha1/scorecards/scorecardssupport/listscorecardsbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListCategoriesByOrgId']._loaded_options = None
  _globals['_SCORECARDSSUPPORT'].methods_by_name['ListCategoriesByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002E\"@/api/v1alpha1/scorecards/scorecardssupport/listcategoriesbyorgid:\001*'
  _globals['_SCORECARDSSUPPORT']._serialized_start=300
  _globals['_SCORECARDSSUPPORT']._serialized_end=2141
# @@protoc_insertion_point(module_scope)
