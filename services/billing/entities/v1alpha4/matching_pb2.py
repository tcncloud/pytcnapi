# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha4/matching.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'services/billing/entities/v1alpha4/matching.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1services/billing/entities/v1alpha4/matching.proto\x12\"services.billing.entities.v1alpha4\"\x83\x01\n\x0eMatchingConfig\x12g\n\x13\x63ountry_code_prefix\x18\x01 \x01(\x0b\x32\x35.services.billing.entities.v1alpha4.CountryCodePrefixH\x00R\x11\x63ountryCodePrefixB\x08\n\x06\x63onfig\"\x90\x01\n\x11\x43ountryCodePrefix\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\x05R\x0b\x63ountryCode\x12\x1a\n\x08prefixes\x18\x02 \x03(\tR\x08prefixes\x12(\n\x10matching_rule_id\x18\x03 \x01(\tR\x0ematchingRuleId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04nameB\xe2\x01\n&com.services.billing.entities.v1alpha4B\rMatchingProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha4\xca\x02\"Services\\Billing\\Entities\\V1alpha4\xe2\x02.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha4.matching_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha4B\rMatchingProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha4\312\002\"Services\\Billing\\Entities\\V1alpha4\342\002.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha4'
  _globals['_MATCHINGCONFIG']._serialized_start=90
  _globals['_MATCHINGCONFIG']._serialized_end=221
  _globals['_COUNTRYCODEPREFIX']._serialized_start=224
  _globals['_COUNTRYCODEPREFIX']._serialized_end=368
# @@protoc_insertion_point(module_scope)
