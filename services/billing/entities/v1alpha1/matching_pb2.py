# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha1/matching.proto
# Protobuf Python Version: 5.28.2
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
    2,
    '',
    'services/billing/entities/v1alpha1/matching.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1services/billing/entities/v1alpha1/matching.proto\x12\"services.billing.entities.v1alpha1\"\xf7\x01\n\x0eMatchingConfig\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12]\n\tarea_code\x18\x01 \x01(\x0b\x32:.services.billing.entities.v1alpha1.MatchingConfigAreaCodeB\x02\x18\x01H\x00R\x08\x61reaCode\x12h\n\x0e\x63ountry_prefix\x18\x64 \x01(\x0b\x32?.services.billing.entities.v1alpha1.MatchingConfigCountryPrefixH\x00R\rcountryPrefixB\x08\n\x06\x63onfig\"W\n\x16MatchingConfigAreaCode\x12\x16\n\x04name\x18\x01 \x01(\tB\x02\x18\x01R\x04name\x12!\n\narea_codes\x18\x02 \x03(\tB\x02\x18\x01R\tareaCodes:\x02\x18\x01\"\\\n\x1bMatchingConfigCountryPrefix\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\x05R\x0b\x63ountryCode\x12\x1a\n\x08prefixes\x18\x02 \x03(\tR\x08prefixes*p\n\x0cMatchingRule\x12\x1d\n\x19MATCHING_RULE_UNSPECIFIED\x10\x00\x12\x1f\n\x17MATCHING_RULE_AREA_CODE\x10\x01\x1a\x02\x08\x01\x12 \n\x1cMATCHING_RULE_COUNTRY_PREFIX\x10\x02\x42\xe2\x01\n&com.services.billing.entities.v1alpha1B\rMatchingProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha1\xca\x02\"Services\\Billing\\Entities\\V1alpha1\xe2\x02.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha1.matching_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha1B\rMatchingProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha1\312\002\"Services\\Billing\\Entities\\V1alpha1\342\002.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha1'
  _globals['_MATCHINGRULE'].values_by_name["MATCHING_RULE_AREA_CODE"]._loaded_options = None
  _globals['_MATCHINGRULE'].values_by_name["MATCHING_RULE_AREA_CODE"]._serialized_options = b'\010\001'
  _globals['_MATCHINGCONFIG'].fields_by_name['area_code']._loaded_options = None
  _globals['_MATCHINGCONFIG'].fields_by_name['area_code']._serialized_options = b'\030\001'
  _globals['_MATCHINGCONFIGAREACODE'].fields_by_name['name']._loaded_options = None
  _globals['_MATCHINGCONFIGAREACODE'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_MATCHINGCONFIGAREACODE'].fields_by_name['area_codes']._loaded_options = None
  _globals['_MATCHINGCONFIGAREACODE'].fields_by_name['area_codes']._serialized_options = b'\030\001'
  _globals['_MATCHINGCONFIGAREACODE']._loaded_options = None
  _globals['_MATCHINGCONFIGAREACODE']._serialized_options = b'\030\001'
  _globals['_MATCHINGRULE']._serialized_start=522
  _globals['_MATCHINGRULE']._serialized_end=634
  _globals['_MATCHINGCONFIG']._serialized_start=90
  _globals['_MATCHINGCONFIG']._serialized_end=337
  _globals['_MATCHINGCONFIGAREACODE']._serialized_start=339
  _globals['_MATCHINGCONFIGAREACODE']._serialized_end=426
  _globals['_MATCHINGCONFIGCOUNTRYPREFIX']._serialized_start=428
  _globals['_MATCHINGCONFIGCOUNTRYPREFIX']._serialized_end=520
# @@protoc_insertion_point(module_scope)
