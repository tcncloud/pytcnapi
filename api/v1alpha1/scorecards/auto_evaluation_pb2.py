# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/scorecards/auto_evaluation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/scorecards/auto_evaluation.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\"H\n\x18GetAutoEvaluationRequest\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\"a\n\x19GetAutoEvaluationResponse\x12\x44\n\x0f\x61uto_evaluation\x18\x01 \x01(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0e\x61utoEvaluation\"A\n\x1aListAutoEvaluationsRequest\x12#\n\rscorecard_ids\x18\x02 \x03(\x03R\x0cscorecardIds\"e\n\x1bListAutoEvaluationsResponse\x12\x46\n\x10\x61uto_evaluations\x18\x01 \x03(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0f\x61utoEvaluations\"K\n\x1b\x44\x65leteAutoEvaluationRequest\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\"d\n\x1c\x44\x65leteAutoEvaluationResponse\x12\x44\n\x0f\x61uto_evaluation\x18\x01 \x01(\x0b\x32\x1b.api.commons.AutoEvaluationR\x0e\x61utoEvaluationB\xb0\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x13\x41utoEvaluationProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.auto_evaluation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\023AutoEvaluationProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_GETAUTOEVALUATIONREQUEST']._serialized_start=104
  _globals['_GETAUTOEVALUATIONREQUEST']._serialized_end=176
  _globals['_GETAUTOEVALUATIONRESPONSE']._serialized_start=178
  _globals['_GETAUTOEVALUATIONRESPONSE']._serialized_end=275
  _globals['_LISTAUTOEVALUATIONSREQUEST']._serialized_start=277
  _globals['_LISTAUTOEVALUATIONSREQUEST']._serialized_end=342
  _globals['_LISTAUTOEVALUATIONSRESPONSE']._serialized_start=344
  _globals['_LISTAUTOEVALUATIONSRESPONSE']._serialized_end=445
  _globals['_DELETEAUTOEVALUATIONREQUEST']._serialized_start=447
  _globals['_DELETEAUTOEVALUATIONREQUEST']._serialized_end=522
  _globals['_DELETEAUTOEVALUATIONRESPONSE']._serialized_start=524
  _globals['_DELETEAUTOEVALUATIONRESPONSE']._serialized_end=624
# @@protoc_insertion_point(module_scope)
