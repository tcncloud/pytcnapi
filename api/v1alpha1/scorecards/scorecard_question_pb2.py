# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/scorecards/scorecard_question.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/scorecards/scorecard_question.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"Q\n\x1bGetScorecardQuestionRequest\x12\x32\n\x15scorecard_question_id\x18\x02 \x01(\x03R\x13scorecardQuestionId\"m\n\x1cGetScorecardQuestionResponse\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestion\"o\n\x1e\x43reateScorecardQuestionRequest\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestion\"p\n\x1f\x43reateScorecardQuestionResponse\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestion\"\xac\x01\n\x1eUpdateScorecardQuestionRequest\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestion\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"p\n\x1fUpdateScorecardQuestionResponse\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestion\"T\n\x1e\x44\x65leteScorecardQuestionRequest\x12\x32\n\x15scorecard_question_id\x18\x02 \x01(\x03R\x13scorecardQuestionId\"p\n\x1f\x44\x65leteScorecardQuestionResponse\x12M\n\x12scorecard_question\x18\x01 \x01(\x0b\x32\x1e.api.commons.ScorecardQuestionR\x11scorecardQuestionB\xb3\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x16ScorecardQuestionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.scorecard_question_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\026ScorecardQuestionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_GETSCORECARDQUESTIONREQUEST']._serialized_start=141
  _globals['_GETSCORECARDQUESTIONREQUEST']._serialized_end=222
  _globals['_GETSCORECARDQUESTIONRESPONSE']._serialized_start=224
  _globals['_GETSCORECARDQUESTIONRESPONSE']._serialized_end=333
  _globals['_CREATESCORECARDQUESTIONREQUEST']._serialized_start=335
  _globals['_CREATESCORECARDQUESTIONREQUEST']._serialized_end=446
  _globals['_CREATESCORECARDQUESTIONRESPONSE']._serialized_start=448
  _globals['_CREATESCORECARDQUESTIONRESPONSE']._serialized_end=560
  _globals['_UPDATESCORECARDQUESTIONREQUEST']._serialized_start=563
  _globals['_UPDATESCORECARDQUESTIONREQUEST']._serialized_end=735
  _globals['_UPDATESCORECARDQUESTIONRESPONSE']._serialized_start=737
  _globals['_UPDATESCORECARDQUESTIONRESPONSE']._serialized_end=849
  _globals['_DELETESCORECARDQUESTIONREQUEST']._serialized_start=851
  _globals['_DELETESCORECARDQUESTIONREQUEST']._serialized_end=935
  _globals['_DELETESCORECARDQUESTIONRESPONSE']._serialized_start=937
  _globals['_DELETESCORECARDQUESTIONRESPONSE']._serialized_end=1049
# @@protoc_insertion_point(module_scope)
