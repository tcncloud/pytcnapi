# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/scorecards/question.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/scorecards/question.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"J\n\x15\x43reateQuestionRequest\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\"K\n\x16\x43reateQuestionResponse\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\"X\n\x14ListQuestionsRequest\x12\x1d\n\nauthor_ids\x18\x02 \x03(\tR\tauthorIds\x12!\n\x0c\x63\x61tegory_ids\x18\x03 \x03(\x03R\x0b\x63\x61tegoryIds\"L\n\x15ListQuestionsResponse\x12\x33\n\tquestions\x18\x01 \x03(\x0b\x32\x15.api.commons.QuestionR\tquestions\"\x87\x01\n\x15UpdateQuestionRequest\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"K\n\x16UpdateQuestionResponse\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\"8\n\x15\x44\x65leteQuestionRequest\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\"K\n\x16\x44\x65leteQuestionResponse\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\"Q\n\x12GetQuestionRequest\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\x12\x1a\n\x08question\x18\x03 \x01(\tR\x08question\"H\n\x13GetQuestionResponse\x12\x31\n\x08question\x18\x01 \x01(\x0b\x32\x15.api.commons.QuestionR\x08question\"a\n\x1d\x43reateQuestionCategoryRequest\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\x12\x1f\n\x0b\x63\x61tegory_id\x18\x03 \x01(\x03R\ncategoryId\"\x94\x01\n\x1e\x43reateQuestionCategoryResponse\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\x12\x1f\n\x0b\x63\x61tegory_id\x18\x03 \x01(\x03R\ncategoryId\x12\x30\n\x14question_category_id\x18\x04 \x01(\x03R\x12questionCategoryId\"\x86\x02\n\x1d\x44\x65leteQuestionCategoryRequest\x12\x32\n\x14question_category_id\x18\x02 \x01(\x03H\x00R\x12questionCategoryId\x12[\n\x08\x62oth_ids\x18\x03 \x01(\x0b\x32>.api.v1alpha1.scorecards.DeleteQuestionCategoryRequest.BothIdsH\x00R\x07\x62othIds\x1aK\n\x07\x42othIds\x12\x1f\n\x0bquestion_id\x18\x01 \x01(\x03R\nquestionId\x12\x1f\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x03R\ncategoryIdB\x07\n\x05where\"\x94\x01\n\x1e\x44\x65leteQuestionCategoryResponse\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\x12\x1f\n\x0b\x63\x61tegory_id\x18\x03 \x01(\x03R\ncategoryId\x12\x30\n\x14question_category_id\x18\x04 \x01(\x03R\x12questionCategoryId\"`\n\x1a\x42ulkCreateQuestionsRequest\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x1f\n\x0buse_default\x18\x04 \x01(\x08R\nuseDefault\"R\n\x1b\x42ulkCreateQuestionsResponse\x12\x33\n\tquestions\x18\x01 \x03(\x0b\x32\x15.api.commons.QuestionR\tquestionsB\xaa\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\rQuestionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.question_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\rQuestionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATEQUESTIONREQUEST']._serialized_start=131
  _globals['_CREATEQUESTIONREQUEST']._serialized_end=205
  _globals['_CREATEQUESTIONRESPONSE']._serialized_start=207
  _globals['_CREATEQUESTIONRESPONSE']._serialized_end=282
  _globals['_LISTQUESTIONSREQUEST']._serialized_start=284
  _globals['_LISTQUESTIONSREQUEST']._serialized_end=372
  _globals['_LISTQUESTIONSRESPONSE']._serialized_start=374
  _globals['_LISTQUESTIONSRESPONSE']._serialized_end=450
  _globals['_UPDATEQUESTIONREQUEST']._serialized_start=453
  _globals['_UPDATEQUESTIONREQUEST']._serialized_end=588
  _globals['_UPDATEQUESTIONRESPONSE']._serialized_start=590
  _globals['_UPDATEQUESTIONRESPONSE']._serialized_end=665
  _globals['_DELETEQUESTIONREQUEST']._serialized_start=667
  _globals['_DELETEQUESTIONREQUEST']._serialized_end=723
  _globals['_DELETEQUESTIONRESPONSE']._serialized_start=725
  _globals['_DELETEQUESTIONRESPONSE']._serialized_end=800
  _globals['_GETQUESTIONREQUEST']._serialized_start=802
  _globals['_GETQUESTIONREQUEST']._serialized_end=883
  _globals['_GETQUESTIONRESPONSE']._serialized_start=885
  _globals['_GETQUESTIONRESPONSE']._serialized_end=957
  _globals['_CREATEQUESTIONCATEGORYREQUEST']._serialized_start=959
  _globals['_CREATEQUESTIONCATEGORYREQUEST']._serialized_end=1056
  _globals['_CREATEQUESTIONCATEGORYRESPONSE']._serialized_start=1059
  _globals['_CREATEQUESTIONCATEGORYRESPONSE']._serialized_end=1207
  _globals['_DELETEQUESTIONCATEGORYREQUEST']._serialized_start=1210
  _globals['_DELETEQUESTIONCATEGORYREQUEST']._serialized_end=1472
  _globals['_DELETEQUESTIONCATEGORYREQUEST_BOTHIDS']._serialized_start=1388
  _globals['_DELETEQUESTIONCATEGORYREQUEST_BOTHIDS']._serialized_end=1463
  _globals['_DELETEQUESTIONCATEGORYRESPONSE']._serialized_start=1475
  _globals['_DELETEQUESTIONCATEGORYRESPONSE']._serialized_end=1623
  _globals['_BULKCREATEQUESTIONSREQUEST']._serialized_start=1625
  _globals['_BULKCREATEQUESTIONSREQUEST']._serialized_end=1721
  _globals['_BULKCREATEQUESTIONSRESPONSE']._serialized_start=1723
  _globals['_BULKCREATEQUESTIONSRESPONSE']._serialized_end=1805
# @@protoc_insertion_point(module_scope)
