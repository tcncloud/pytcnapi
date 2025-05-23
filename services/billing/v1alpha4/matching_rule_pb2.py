# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha4/matching_rule.proto
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
    'services/billing/v1alpha4/matching_rule.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from services.billing.entities.v1alpha4 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_rates__pb2
from services.billing.v1alpha4 import core_pb2 as services_dot_billing_dot_v1alpha4_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-services/billing/v1alpha4/matching_rule.proto\x12\x19services.billing.v1alpha4\x1a google/protobuf/field_mask.proto\x1a.services/billing/entities/v1alpha4/rates.proto\x1a$services/billing/v1alpha4/core.proto\"\x9c\x01\n\x19\x43reateMatchingRuleRequest\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\x12U\n\rmatching_rule\x18\x02 \x01(\x0b\x32\x30.services.billing.entities.v1alpha4.MatchingRuleR\x0cmatchingRule\"F\n\x1a\x43reateMatchingRuleResponse\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\"E\n\x19\x44\x65leteMatchingRuleRequest\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\"\x1c\n\x1a\x44\x65leteMatchingRuleResponse\"B\n\x16GetMatchingRuleRequest\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\"p\n\x17GetMatchingRuleResponse\x12U\n\rmatching_rule\x18\x01 \x01(\x0b\x32\x30.services.billing.entities.v1alpha4.MatchingRuleR\x0cmatchingRule\"\xfa\x01\n\x18ListMatchingRulesRequest\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha4.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha4.PageR\x04page\"\x8a\x01\n\x19ListMatchingRulesResponse\x12W\n\x0ematching_rules\x18\x01 \x03(\x0b\x32\x30.services.billing.entities.v1alpha4.MatchingRuleR\rmatchingRules\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xd9\x01\n\x19UpdateMatchingRuleRequest\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\x12U\n\rmatching_rule\x18\x02 \x01(\x0b\x32\x30.services.billing.entities.v1alpha4.MatchingRuleR\x0cmatchingRule\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x1c\n\x1aUpdateMatchingRuleResponseB\xb8\x01\n\x1d\x63om.services.billing.v1alpha4B\x11MatchingRuleProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha4\xca\x02\x19Services\\Billing\\V1alpha4\xe2\x02%Services\\Billing\\V1alpha4\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha4.matching_rule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha4B\021MatchingRuleProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha4\312\002\031Services\\Billing\\V1alpha4\342\002%Services\\Billing\\V1alpha4\\GPBMetadata\352\002\033Services::Billing::V1alpha4'
  _globals['_CREATEMATCHINGRULEREQUEST']._serialized_start=197
  _globals['_CREATEMATCHINGRULEREQUEST']._serialized_end=353
  _globals['_CREATEMATCHINGRULERESPONSE']._serialized_start=355
  _globals['_CREATEMATCHINGRULERESPONSE']._serialized_end=425
  _globals['_DELETEMATCHINGRULEREQUEST']._serialized_start=427
  _globals['_DELETEMATCHINGRULEREQUEST']._serialized_end=496
  _globals['_DELETEMATCHINGRULERESPONSE']._serialized_start=498
  _globals['_DELETEMATCHINGRULERESPONSE']._serialized_end=526
  _globals['_GETMATCHINGRULEREQUEST']._serialized_start=528
  _globals['_GETMATCHINGRULEREQUEST']._serialized_end=594
  _globals['_GETMATCHINGRULERESPONSE']._serialized_start=596
  _globals['_GETMATCHINGRULERESPONSE']._serialized_end=708
  _globals['_LISTMATCHINGRULESREQUEST']._serialized_start=711
  _globals['_LISTMATCHINGRULESREQUEST']._serialized_end=961
  _globals['_LISTMATCHINGRULESRESPONSE']._serialized_start=964
  _globals['_LISTMATCHINGRULESRESPONSE']._serialized_end=1102
  _globals['_UPDATEMATCHINGRULEREQUEST']._serialized_start=1105
  _globals['_UPDATEMATCHINGRULEREQUEST']._serialized_end=1322
  _globals['_UPDATEMATCHINGRULERESPONSE']._serialized_start=1324
  _globals['_UPDATEMATCHINGRULERESPONSE']._serialized_end=1352
# @@protoc_insertion_point(module_scope)
