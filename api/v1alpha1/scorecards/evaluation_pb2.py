# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/evaluation.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'api/v1alpha1/scorecards/evaluation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/scorecards/evaluation.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"R\n\x17\x43reateEvaluationRequest\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"S\n\x18\x43reateEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\x8f\x01\n\x17UpdateEvaluationRequest\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"S\n\x18UpdateEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\">\n\x17\x44\x65leteEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"S\n\x18\x44\x65leteEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\";\n\x14GetEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"P\n\x15GetEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"=\n\x16ScoreEvaluationRequest\x12#\n\revaluation_id\x18\x03 \x01(\x03R\x0c\x65valuationId\"R\n\x17ScoreEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\xbf\x02\n\x16ListEvaluationsRequest\x12\x1b\n\tscorer_id\x18\x02 \x03(\tR\x08scorerId\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12?\n\rreturn_fields\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0creturnFields\x12\x1d\n\nis_deleted\x18\x0b \x01(\x08R\tisDeleted\"T\n\x17ListEvaluationsResponse\x12\x39\n\x0b\x65valuations\x18\x01 \x03(\x0b\x32\x17.api.commons.EvaluationR\x0b\x65valuations\"\x8e\x01\n\x1dPreviewEvaluationScoreRequest\x12\x37\n\nevaluation\x18\x02 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\x12\x34\n\tscorecard\x18\x03 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"Y\n\x1ePreviewEvaluationScoreResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\xbe\x02\n\x1dListEvaluationsByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tscorer_id\x18\x02 \x03(\tR\x08scorerId\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12?\n\rreturn_fields\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0creturnFields\"\\\n\x1e\x44\x65leteEvaluationByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"\xa3\x02\n\x1c\x42ulkDeleteEvaluationsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12%\n\x0e\x65valuation_ids\x18\x02 \x03(\x03R\revaluationIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12\x1b\n\tscorer_id\x18\x07 \x03(\tR\x08scorerId\"5\n\x1d\x42ulkDeleteEvaluationsResponse\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\"X\n\x18RestoreEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\"T\n\x19RestoreEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluationB\xac\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x0f\x45valuationProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\017EvaluationProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATEEVALUATIONREQUEST']._serialized_start=133
  _globals['_CREATEEVALUATIONREQUEST']._serialized_end=215
  _globals['_CREATEEVALUATIONRESPONSE']._serialized_start=217
  _globals['_CREATEEVALUATIONRESPONSE']._serialized_end=300
  _globals['_UPDATEEVALUATIONREQUEST']._serialized_start=303
  _globals['_UPDATEEVALUATIONREQUEST']._serialized_end=446
  _globals['_UPDATEEVALUATIONRESPONSE']._serialized_start=448
  _globals['_UPDATEEVALUATIONRESPONSE']._serialized_end=531
  _globals['_DELETEEVALUATIONREQUEST']._serialized_start=533
  _globals['_DELETEEVALUATIONREQUEST']._serialized_end=595
  _globals['_DELETEEVALUATIONRESPONSE']._serialized_start=597
  _globals['_DELETEEVALUATIONRESPONSE']._serialized_end=680
  _globals['_GETEVALUATIONREQUEST']._serialized_start=682
  _globals['_GETEVALUATIONREQUEST']._serialized_end=741
  _globals['_GETEVALUATIONRESPONSE']._serialized_start=743
  _globals['_GETEVALUATIONRESPONSE']._serialized_end=823
  _globals['_SCOREEVALUATIONREQUEST']._serialized_start=825
  _globals['_SCOREEVALUATIONREQUEST']._serialized_end=886
  _globals['_SCOREEVALUATIONRESPONSE']._serialized_start=888
  _globals['_SCOREEVALUATIONRESPONSE']._serialized_end=970
  _globals['_LISTEVALUATIONSREQUEST']._serialized_start=973
  _globals['_LISTEVALUATIONSREQUEST']._serialized_end=1292
  _globals['_LISTEVALUATIONSRESPONSE']._serialized_start=1294
  _globals['_LISTEVALUATIONSRESPONSE']._serialized_end=1378
  _globals['_PREVIEWEVALUATIONSCOREREQUEST']._serialized_start=1381
  _globals['_PREVIEWEVALUATIONSCOREREQUEST']._serialized_end=1523
  _globals['_PREVIEWEVALUATIONSCORERESPONSE']._serialized_start=1525
  _globals['_PREVIEWEVALUATIONSCORERESPONSE']._serialized_end=1614
  _globals['_LISTEVALUATIONSBYORGIDREQUEST']._serialized_start=1617
  _globals['_LISTEVALUATIONSBYORGIDREQUEST']._serialized_end=1935
  _globals['_DELETEEVALUATIONBYORGIDREQUEST']._serialized_start=1937
  _globals['_DELETEEVALUATIONBYORGIDREQUEST']._serialized_end=2029
  _globals['_BULKDELETEEVALUATIONSREQUEST']._serialized_start=2032
  _globals['_BULKDELETEEVALUATIONSREQUEST']._serialized_end=2323
  _globals['_BULKDELETEEVALUATIONSRESPONSE']._serialized_start=2325
  _globals['_BULKDELETEEVALUATIONSRESPONSE']._serialized_end=2378
  _globals['_RESTOREEVALUATIONREQUEST']._serialized_start=2380
  _globals['_RESTOREEVALUATIONREQUEST']._serialized_end=2468
  _globals['_RESTOREEVALUATIONRESPONSE']._serialized_start=2470
  _globals['_RESTOREEVALUATIONRESPONSE']._serialized_end=2554
# @@protoc_insertion_point(module_scope)
