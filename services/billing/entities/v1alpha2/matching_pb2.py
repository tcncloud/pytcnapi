# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/billing/entities/v1alpha2/matching.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1services/billing/entities/v1alpha2/matching.proto\x12\"services.billing.entities.v1alpha2\"\x98\x01\n\x0eMatchingConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12h\n\x0e\x63ountry_prefix\x18\x64 \x01(\x0b\x32?.services.billing.entities.v1alpha2.MatchingConfigCountryPrefixH\x00R\rcountryPrefixB\x08\n\x06\x63onfig\"\\\n\x1bMatchingConfigCountryPrefix\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\x05R\x0b\x63ountryCode\x12\x1a\n\x08prefixes\x18\x02 \x03(\tR\x08prefixes*O\n\x0cMatchingRule\x12\x1d\n\x19MATCHING_RULE_UNSPECIFIED\x10\x00\x12 \n\x1cMATCHING_RULE_COUNTRY_PREFIX\x10\x01\x42\xe2\x01\n&com.services.billing.entities.v1alpha2B\rMatchingProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha2\xca\x02\"Services\\Billing\\Entities\\V1alpha2\xe2\x02.Services\\Billing\\Entities\\V1alpha2\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha2.matching_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha2B\rMatchingProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha2\312\002\"Services\\Billing\\Entities\\V1alpha2\342\002.Services\\Billing\\Entities\\V1alpha2\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha2'
  _globals['_MATCHINGRULE']._serialized_start=338
  _globals['_MATCHINGRULE']._serialized_end=417
  _globals['_MATCHINGCONFIG']._serialized_start=90
  _globals['_MATCHINGCONFIG']._serialized_end=242
  _globals['_MATCHINGCONFIGCOUNTRYPREFIX']._serialized_start=244
  _globals['_MATCHINGCONFIGCOUNTRYPREFIX']._serialized_end=336
# @@protoc_insertion_point(module_scope)