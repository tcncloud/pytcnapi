# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/smart_question.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'api/v1alpha1/scorecards/smart_question.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,api/v1alpha1/scorecards/smart_question.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"_\n\x1a\x43reateSmartQuestionRequest\x12\x41\n\x0esmart_question\x18\x01 \x01(\x0b\x32\x1a.api.commons.SmartQuestionR\rsmartQuestion\"`\n\x1b\x43reateSmartQuestionResponse\x12\x41\n\x0esmart_question\x18\x01 \x01(\x0b\x32\x1a.api.commons.SmartQuestionR\rsmartQuestion\"\x9c\x01\n\x1aUpdateSmartQuestionRequest\x12\x41\n\x0esmart_question\x18\x01 \x01(\x0b\x32\x1a.api.commons.SmartQuestionR\rsmartQuestion\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"`\n\x1bUpdateSmartQuestionResponse\x12\x41\n\x0esmart_question\x18\x01 \x01(\x0b\x32\x1a.api.commons.SmartQuestionR\rsmartQuestion\"H\n\x1a\x44\x65leteSmartQuestionRequest\x12*\n\x11smart_question_id\x18\x02 \x01(\x03R\x0fsmartQuestionId\"`\n\x1b\x44\x65leteSmartQuestionResponse\x12\x41\n\x0esmart_question\x18\x01 \x01(\x0b\x32\x1a.api.commons.SmartQuestionR\rsmartQuestionB\xaf\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x12SmartQuestionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.smart_question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\022SmartQuestionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATESMARTQUESTIONREQUEST']._serialized_start=137
  _globals['_CREATESMARTQUESTIONREQUEST']._serialized_end=232
  _globals['_CREATESMARTQUESTIONRESPONSE']._serialized_start=234
  _globals['_CREATESMARTQUESTIONRESPONSE']._serialized_end=330
  _globals['_UPDATESMARTQUESTIONREQUEST']._serialized_start=333
  _globals['_UPDATESMARTQUESTIONREQUEST']._serialized_end=489
  _globals['_UPDATESMARTQUESTIONRESPONSE']._serialized_start=491
  _globals['_UPDATESMARTQUESTIONRESPONSE']._serialized_end=587
  _globals['_DELETESMARTQUESTIONREQUEST']._serialized_start=589
  _globals['_DELETESMARTQUESTIONREQUEST']._serialized_end=661
  _globals['_DELETESMARTQUESTIONRESPONSE']._serialized_start=663
  _globals['_DELETESMARTQUESTIONRESPONSE']._serialized_end=759
# @@protoc_insertion_point(module_scope)
