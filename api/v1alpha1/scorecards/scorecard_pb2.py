# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/scorecard.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'api/v1alpha1/scorecards/scorecard.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/v1alpha1/scorecards/scorecard.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x15\x61pi/commons/acd.proto\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"N\n\x16\x43reateScorecardRequest\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"O\n\x17\x43reateScorecardResponse\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"\x91\x02\n\x15ListScorecardsRequest\x12\x1d\n\nauthor_ids\x18\x02 \x03(\tR\tauthorIds\x12!\n\x0c\x63\x61tegory_ids\x18\x03 \x03(\x03R\x0b\x63\x61tegoryIds\x12\x33\n\x06states\x18\x04 \x03(\x0e\x32\x1b.api.commons.ScorecardStateR\x06states\x12\x46\n\x10\x65valuation_types\x18\x05 \x03(\x0e\x32\x1b.api.commons.EvaluationTypeR\x0f\x65valuationTypes\x12\x39\n\ncall_types\x18\x06 \x03(\x0e\x32\x1a.api.commons.CallType.EnumR\tcallTypes\"P\n\x16ListScorecardsResponse\x12\x36\n\nscorecards\x18\x01 \x03(\x0b\x32\x16.api.commons.ScorecardR\nscorecards\"\x8b\x01\n\x16UpdateScorecardRequest\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"O\n\x17UpdateScorecardResponse\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\";\n\x16\x44\x65leteScorecardRequest\x12!\n\x0cscorecard_id\x18\x02 \x01(\x03R\x0bscorecardId\"O\n\x17\x44\x65leteScorecardResponse\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"Y\n\x13GetScorecardRequest\x12!\n\x0cscorecard_id\x18\x02 \x01(\x03R\x0bscorecardId\x12\x1f\n\x0buse_default\x18\x03 \x01(\x08R\nuseDefault\"L\n\x14GetScorecardResponse\x12\x34\n\tscorecard\x18\x01 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"\xaf\x02\n\x1cListScorecardsByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nauthor_ids\x18\x02 \x03(\tR\tauthorIds\x12!\n\x0c\x63\x61tegory_ids\x18\x03 \x03(\x03R\x0b\x63\x61tegoryIds\x12\x33\n\x06states\x18\x04 \x03(\x0e\x32\x1b.api.commons.ScorecardStateR\x06states\x12\x46\n\x10\x65valuation_types\x18\x05 \x03(\x0e\x32\x1b.api.commons.EvaluationTypeR\x0f\x65valuationTypes\x12\x39\n\ncall_types\x18\x06 \x03(\x0e\x32\x1a.api.commons.CallType.EnumR\tcallTypesB\xab\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x0eScorecardProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.scorecard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\016ScorecardProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATESCORECARDREQUEST']._serialized_start=155
  _globals['_CREATESCORECARDREQUEST']._serialized_end=233
  _globals['_CREATESCORECARDRESPONSE']._serialized_start=235
  _globals['_CREATESCORECARDRESPONSE']._serialized_end=314
  _globals['_LISTSCORECARDSREQUEST']._serialized_start=317
  _globals['_LISTSCORECARDSREQUEST']._serialized_end=590
  _globals['_LISTSCORECARDSRESPONSE']._serialized_start=592
  _globals['_LISTSCORECARDSRESPONSE']._serialized_end=672
  _globals['_UPDATESCORECARDREQUEST']._serialized_start=675
  _globals['_UPDATESCORECARDREQUEST']._serialized_end=814
  _globals['_UPDATESCORECARDRESPONSE']._serialized_start=816
  _globals['_UPDATESCORECARDRESPONSE']._serialized_end=895
  _globals['_DELETESCORECARDREQUEST']._serialized_start=897
  _globals['_DELETESCORECARDREQUEST']._serialized_end=956
  _globals['_DELETESCORECARDRESPONSE']._serialized_start=958
  _globals['_DELETESCORECARDRESPONSE']._serialized_end=1037
  _globals['_GETSCORECARDREQUEST']._serialized_start=1039
  _globals['_GETSCORECARDREQUEST']._serialized_end=1128
  _globals['_GETSCORECARDRESPONSE']._serialized_start=1130
  _globals['_GETSCORECARDRESPONSE']._serialized_end=1206
  _globals['_LISTSCORECARDSBYORGIDREQUEST']._serialized_start=1209
  _globals['_LISTSCORECARDSBYORGIDREQUEST']._serialized_end=1512
# @@protoc_insertion_point(module_scope)
