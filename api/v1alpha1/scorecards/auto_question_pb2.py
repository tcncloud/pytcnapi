# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/auto_question.proto
# Protobuf Python Version: 6.30.2
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
    2,
    '',
    'api/v1alpha1/scorecards/auto_question.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+api/v1alpha1/scorecards/auto_question.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"B\n\x16GetAutoQuestionRequest\x12(\n\x10\x61uto_question_id\x18\x02 \x01(\x03R\x0e\x61utoQuestionId\"Y\n\x17GetAutoQuestionResponse\x12>\n\rauto_question\x18\x01 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestion\"[\n\x19\x43reateAutoQuestionRequest\x12>\n\rauto_question\x18\x02 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestion\"\\\n\x1a\x43reateAutoQuestionResponse\x12>\n\rauto_question\x18\x01 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestion\"\x98\x01\n\x19UpdateAutoQuestionRequest\x12>\n\rauto_question\x18\x02 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestion\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\\\n\x1aUpdateAutoQuestionResponse\x12>\n\rauto_question\x18\x01 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestion\"E\n\x19\x44\x65leteAutoQuestionRequest\x12(\n\x10\x61uto_question_id\x18\x03 \x01(\x03R\x0e\x61utoQuestionId\"\\\n\x1a\x44\x65leteAutoQuestionResponse\x12>\n\rauto_question\x18\x01 \x01(\x0b\x32\x19.api.commons.AutoQuestionR\x0c\x61utoQuestionB\xae\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x11\x41utoQuestionProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.auto_question_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\021AutoQuestionProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_GETAUTOQUESTIONREQUEST']._serialized_start=136
  _globals['_GETAUTOQUESTIONREQUEST']._serialized_end=202
  _globals['_GETAUTOQUESTIONRESPONSE']._serialized_start=204
  _globals['_GETAUTOQUESTIONRESPONSE']._serialized_end=293
  _globals['_CREATEAUTOQUESTIONREQUEST']._serialized_start=295
  _globals['_CREATEAUTOQUESTIONREQUEST']._serialized_end=386
  _globals['_CREATEAUTOQUESTIONRESPONSE']._serialized_start=388
  _globals['_CREATEAUTOQUESTIONRESPONSE']._serialized_end=480
  _globals['_UPDATEAUTOQUESTIONREQUEST']._serialized_start=483
  _globals['_UPDATEAUTOQUESTIONREQUEST']._serialized_end=635
  _globals['_UPDATEAUTOQUESTIONRESPONSE']._serialized_start=637
  _globals['_UPDATEAUTOQUESTIONRESPONSE']._serialized_end=729
  _globals['_DELETEAUTOQUESTIONREQUEST']._serialized_start=731
  _globals['_DELETEAUTOQUESTIONREQUEST']._serialized_end=800
  _globals['_DELETEAUTOQUESTIONRESPONSE']._serialized_start=802
  _globals['_DELETEAUTOQUESTIONRESPONSE']._serialized_end=894
# @@protoc_insertion_point(module_scope)
