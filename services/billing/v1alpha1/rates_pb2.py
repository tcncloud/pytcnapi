# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha1/rates.proto
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
    'services/billing/v1alpha1/rates.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from services.billing.entities.v1alpha1 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_rates__pb2
from services.billing.v1alpha1 import core_pb2 as services_dot_billing_dot_v1alpha1_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%services/billing/v1alpha1/rates.proto\x12\x19services.billing.v1alpha1\x1a google/protobuf/field_mask.proto\x1a.services/billing/entities/v1alpha1/rates.proto\x1a$services/billing/v1alpha1/core.proto\"\xaf\x01\n\"CreateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0erateDefinition\"S\n#CreateDefaultRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"\xa8\x01\n\x1b\x43reateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0erateDefinition\"L\n\x1c\x43reateRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"R\n\"DeleteDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"%\n#DeleteDefaultRateDefinitionResponse\"K\n\x1b\x44\x65leteRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"\x1e\n\x1c\x44\x65leteRateDefinitionResponse\"H\n\x18GetRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"x\n\x19GetRateDefinitionResponse\x12[\n\x0frate_definition\x18\x01 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0erateDefinition\"\x80\x02\n\x1aListRateDefinitionsRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha1.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha1.PageR\x04page\"\x92\x01\n\x1bListRateDefinitionsResponse\x12]\n\x10rate_definitions\x18\x01 \x03(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0frateDefinitions\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xf0\x01\n\"UpdateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0erateDefinition\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"%\n#UpdateDefaultRateDefinitionResponse\"\xe9\x01\n\x1bUpdateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x0erateDefinition\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"\x1e\n\x1cUpdateRateDefinitionResponseB\xb1\x01\n\x1d\x63om.services.billing.v1alpha1B\nRatesProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha1\xca\x02\x19Services\\Billing\\V1alpha1\xe2\x02%Services\\Billing\\V1alpha1\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha1.rates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha1B\nRatesProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha1\312\002\031Services\\Billing\\V1alpha1\342\002%Services\\Billing\\V1alpha1\\GPBMetadata\352\002\033Services::Billing::V1alpha1'
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=189
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=364
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=366
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=449
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_start=452
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_end=620
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_start=622
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_end=698
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=700
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=782
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=784
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=821
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_start=823
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_end=898
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_start=900
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_end=930
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_start=932
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_end=1004
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_start=1006
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_end=1126
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_start=1129
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_end=1385
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_start=1388
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_end=1534
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=1537
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=1777
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=1779
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=1816
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_start=1819
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_end=2052
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_start=2054
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_end=2084
# @@protoc_insertion_point(module_scope)
