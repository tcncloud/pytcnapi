# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha4/omni.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'services/billing/entities/v1alpha4/omni.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from services.billing.entities.v1alpha4 import matching_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_matching__pb2
from services.billing.entities.v1alpha4 import modules_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_modules__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-services/billing/entities/v1alpha4/omni.proto\x12\"services.billing.entities.v1alpha4\x1a\x31services/billing/entities/v1alpha4/matching.proto\x1a\x30services/billing/entities/v1alpha4/modules.proto\"\xc3\x01\n\rOmniSmsConfig\x12\x16\n\x04name\x18\x01 \x01(\tB\x02\x18\x01R\x04name\x12Q\n\x08prefixes\x18\x02 \x01(\x0b\x32\x35.services.billing.entities.v1alpha4.CountryCodePrefixR\x08prefixes\x12G\n\x06\x63onfig\x18\x03 \x01(\x0b\x32/.services.billing.entities.v1alpha4.BasicConfigR\x06\x63onfig\"\xcb\x01\n\x11OmniSmsUnitConfig\x12\x16\n\x04name\x18\x01 \x01(\tB\x02\x18\x01R\x04name\x12Q\n\x08prefixes\x18\x02 \x01(\x0b\x32\x35.services.billing.entities.v1alpha4.CountryCodePrefixR\x08prefixes\x12K\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x33.services.billing.entities.v1alpha4.BasicUnitConfigR\x06\x63onfigB\xde\x01\n&com.services.billing.entities.v1alpha4B\tOmniProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha4\xca\x02\"Services\\Billing\\Entities\\V1alpha4\xe2\x02.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha4.omni_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha4B\tOmniProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha4\312\002\"Services\\Billing\\Entities\\V1alpha4\342\002.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha4'
  _globals['_OMNISMSCONFIG'].fields_by_name['name']._loaded_options = None
  _globals['_OMNISMSCONFIG'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_OMNISMSUNITCONFIG'].fields_by_name['name']._loaded_options = None
  _globals['_OMNISMSUNITCONFIG'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_OMNISMSCONFIG']._serialized_start=187
  _globals['_OMNISMSCONFIG']._serialized_end=382
  _globals['_OMNISMSUNITCONFIG']._serialized_start=385
  _globals['_OMNISMSUNITCONFIG']._serialized_end=588
# @@protoc_insertion_point(module_scope)
