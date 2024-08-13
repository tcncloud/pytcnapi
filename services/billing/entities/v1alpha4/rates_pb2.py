# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha4/rates.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'services/billing/entities/v1alpha4/rates.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha4 import matching_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_matching__pb2
from services.billing.entities.v1alpha4 import products_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_products__pb2
from services.billing.entities.v1alpha4 import tags_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_tags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.services/billing/entities/v1alpha4/rates.proto\x12\"services.billing.entities.v1alpha4\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31services/billing/entities/v1alpha4/matching.proto\x1a\x31services/billing/entities/v1alpha4/products.proto\x1a-services/billing/entities/v1alpha4/tags.proto\"\x90\x04\n\x0eRateDefinition\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x15\n\x06sku_id\x18\x02 \x01(\tR\x05skuId\x12S\n\x0b\x62illing_tag\x18\x03 \x01(\x0b\x32..services.billing.entities.v1alpha4.BillingTagB\x02\x18\x01R\nbillingTag\x12I\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x31.services.billing.entities.v1alpha4.ProductConfigR\x06\x63onfig\x12\x19\n\x08is_draft\x18\x05 \x01(\x08R\x07isDraft\x12!\n\x0cis_overwrite\x18\x06 \x01(\x08R\x0bisOverwrite\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12$\n\x0e\x62illing_tag_id\x18\n \x01(\tR\x0c\x62illingTagId\"\xba\x03\n\x0cMatchingRule\x12(\n\x10matching_rule_id\x18\x01 \x01(\tR\x0ematchingRuleId\x12M\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x31.services.billing.entities.v1alpha4.ProductConfigB\x02\x18\x01R\x06\x63onfig\x12;\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0b\x64\x65lete_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12;\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12g\n\x13\x63ountry_code_prefix\x18\x64 \x01(\x0b\x32\x35.services.billing.entities.v1alpha4.CountryCodePrefixH\x00R\x11\x63ountryCodePrefixB\x11\n\x0fmatching_configB\xdf\x01\n&com.services.billing.entities.v1alpha4B\nRatesProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha4\xca\x02\"Services\\Billing\\Entities\\V1alpha4\xe2\x02.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha4.rates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha4B\nRatesProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha4\312\002\"Services\\Billing\\Entities\\V1alpha4\342\002.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha4'
  _globals['_RATEDEFINITION'].fields_by_name['billing_tag']._loaded_options = None
  _globals['_RATEDEFINITION'].fields_by_name['billing_tag']._serialized_options = b'\030\001'
  _globals['_MATCHINGRULE'].fields_by_name['config']._loaded_options = None
  _globals['_MATCHINGRULE'].fields_by_name['config']._serialized_options = b'\030\001'
  _globals['_RATEDEFINITION']._serialized_start=269
  _globals['_RATEDEFINITION']._serialized_end=797
  _globals['_MATCHINGRULE']._serialized_start=800
  _globals['_MATCHINGRULE']._serialized_end=1242
# @@protoc_insertion_point(module_scope)
