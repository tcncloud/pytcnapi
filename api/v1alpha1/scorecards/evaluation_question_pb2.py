# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/evaluation_question.proto
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
    'api/v1alpha1/scorecards/evaluation_question.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1api/v1alpha1/scorecards/evaluation_question.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"s\n\x1f\x43reateEvaluationQuestionRequest\x12P\n\x13\x65valuation_question\x18\x01 \x01(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x12\x65valuationQuestion\"t\n CreateEvaluationQuestionResponse\x12P\n\x13\x65valuation_question\x18\x01 \x01(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x12\x65valuationQuestion\"\xb0\x01\n\x1fUpdateEvaluationQuestionRequest\x12P\n\x13\x65valuation_question\x18\x01 \x01(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x12\x65valuationQuestion\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"t\n UpdateEvaluationQuestionResponse\x12P\n\x13\x65valuation_question\x18\x01 \x01(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x12\x65valuationQuestion\"W\n\x1f\x44\x65leteEvaluationQuestionRequest\x12\x34\n\x16\x65valuation_question_id\x18\x02 \x01(\x03R\x14\x65valuationQuestionId\"t\n DeleteEvaluationQuestionResponse\x12P\n\x13\x65valuation_question\x18\x01 \x01(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x12\x65valuationQuestionB\xb4\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x17\x45valuationQuestionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.evaluation_question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\027EvaluationQuestionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATEEVALUATIONQUESTIONREQUEST']._serialized_start=142
  _globals['_CREATEEVALUATIONQUESTIONREQUEST']._serialized_end=257
  _globals['_CREATEEVALUATIONQUESTIONRESPONSE']._serialized_start=259
  _globals['_CREATEEVALUATIONQUESTIONRESPONSE']._serialized_end=375
  _globals['_UPDATEEVALUATIONQUESTIONREQUEST']._serialized_start=378
  _globals['_UPDATEEVALUATIONQUESTIONREQUEST']._serialized_end=554
  _globals['_UPDATEEVALUATIONQUESTIONRESPONSE']._serialized_start=556
  _globals['_UPDATEEVALUATIONQUESTIONRESPONSE']._serialized_end=672
  _globals['_DELETEEVALUATIONQUESTIONREQUEST']._serialized_start=674
  _globals['_DELETEEVALUATIONQUESTIONREQUEST']._serialized_end=761
  _globals['_DELETEEVALUATIONQUESTIONRESPONSE']._serialized_start=763
  _globals['_DELETEEVALUATIONQUESTIONRESPONSE']._serialized_end=879
# @@protoc_insertion_point(module_scope)
