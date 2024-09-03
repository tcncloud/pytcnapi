# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha2/rates.proto
# Protobuf Python Version: 5.28.0
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
    0,
    '',
    'services/billing/v1alpha2/rates.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha2 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha2_dot_rates__pb2
from services.billing.v1alpha2 import core_pb2 as services_dot_billing_dot_v1alpha2_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%services/billing/v1alpha2/rates.proto\x12\x19services.billing.v1alpha2\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.services/billing/entities/v1alpha2/rates.proto\x1a$services/billing/v1alpha2/core.proto\"\xaf\x01\n\"CreateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0erateDefinition\"S\n#CreateDefaultRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"z\n#CreateDefaultRateDefinitionsRequest\x12S\n\x05rates\x18\x01 \x03(\x0b\x32=.services.billing.v1alpha2.CreateDefaultRateDefinitionRequestR\x05rates\"|\n$CreateDefaultRateDefinitionsResponse\x12T\n\x05rates\x18\x01 \x03(\x0b\x32>.services.billing.v1alpha2.CreateDefaultRateDefinitionResponseR\x05rates\"\xe5\x01\n\x1b\x43reateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0erateDefinition\x12;\n\x1a\x64\x65\x66\x61ult_rate_definition_id\x18\x03 \x01(\tR\x17\x64\x65\x66\x61ultRateDefinitionId\"L\n\x1c\x43reateRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"l\n\x1c\x43reateRateDefinitionsRequest\x12L\n\x05rates\x18\x01 \x03(\x0b\x32\x36.services.billing.v1alpha2.CreateRateDefinitionRequestR\x05rates\"n\n\x1d\x43reateRateDefinitionsResponse\x12M\n\x05rates\x18\x01 \x03(\x0b\x32\x37.services.billing.v1alpha2.CreateRateDefinitionResponseR\x05rates\"R\n\"DeleteDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"%\n#DeleteDefaultRateDefinitionResponse\"U\n#DeleteDefaultRateDefinitionsRequest\x12.\n\x13rate_definition_ids\x18\x01 \x03(\tR\x11rateDefinitionIds\"&\n$DeleteDefaultRateDefinitionsResponse\"K\n\x1b\x44\x65leteRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"\x1e\n\x1c\x44\x65leteRateDefinitionResponse\"N\n\x1c\x44\x65leteRateDefinitionsRequest\x12.\n\x13rate_definition_ids\x18\x01 \x03(\tR\x11rateDefinitionIds\"\x1f\n\x1d\x44\x65leteRateDefinitionsResponse\"H\n\x18GetRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"x\n\x19GetRateDefinitionResponse\x12[\n\x0frate_definition\x18\x01 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0erateDefinition\"\xbd\x01\n\x15GetRateHistoryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tgroup_ids\x18\x02 \x03(\tR\x08groupIds\x12\x39\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\"h\n\x16GetRateHistoryResponse\x12N\n\tsnapshots\x18\x01 \x03(\x0b\x32\x30.services.billing.entities.v1alpha2.RateSnapshotR\tsnapshots\"\x86\x02\n ListActiveRateDefinitionsRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha2.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha2.PageR\x04page\"\x98\x01\n!ListActiveRateDefinitionsResponse\x12]\n\x10rate_definitions\x18\x01 \x03(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0frateDefinitions\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\x80\x02\n\x1aListRateDefinitionsRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha2.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha2.PageR\x04page\"\x92\x01\n\x1bListRateDefinitionsResponse\x12]\n\x10rate_definitions\x18\x01 \x03(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0frateDefinitions\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xf0\x01\n\"UpdateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0erateDefinition\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"%\n#UpdateDefaultRateDefinitionResponse\"\xe9\x01\n\x1bUpdateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x0erateDefinition\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"\x1e\n\x1cUpdateRateDefinitionResponseB\xb1\x01\n\x1d\x63om.services.billing.v1alpha2B\nRatesProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha2\xca\x02\x19Services\\Billing\\V1alpha2\xe2\x02%Services\\Billing\\V1alpha2\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha2.rates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha2B\nRatesProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha2\312\002\031Services\\Billing\\V1alpha2\342\002%Services\\Billing\\V1alpha2\\GPBMetadata\352\002\033Services::Billing::V1alpha2'
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=222
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=397
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=399
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=482
  _globals['_CREATEDEFAULTRATEDEFINITIONSREQUEST']._serialized_start=484
  _globals['_CREATEDEFAULTRATEDEFINITIONSREQUEST']._serialized_end=606
  _globals['_CREATEDEFAULTRATEDEFINITIONSRESPONSE']._serialized_start=608
  _globals['_CREATEDEFAULTRATEDEFINITIONSRESPONSE']._serialized_end=732
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_start=735
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_end=964
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_start=966
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_end=1042
  _globals['_CREATERATEDEFINITIONSREQUEST']._serialized_start=1044
  _globals['_CREATERATEDEFINITIONSREQUEST']._serialized_end=1152
  _globals['_CREATERATEDEFINITIONSRESPONSE']._serialized_start=1154
  _globals['_CREATERATEDEFINITIONSRESPONSE']._serialized_end=1264
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=1266
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=1348
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=1350
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=1387
  _globals['_DELETEDEFAULTRATEDEFINITIONSREQUEST']._serialized_start=1389
  _globals['_DELETEDEFAULTRATEDEFINITIONSREQUEST']._serialized_end=1474
  _globals['_DELETEDEFAULTRATEDEFINITIONSRESPONSE']._serialized_start=1476
  _globals['_DELETEDEFAULTRATEDEFINITIONSRESPONSE']._serialized_end=1514
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_start=1516
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_end=1591
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_start=1593
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_end=1623
  _globals['_DELETERATEDEFINITIONSREQUEST']._serialized_start=1625
  _globals['_DELETERATEDEFINITIONSREQUEST']._serialized_end=1703
  _globals['_DELETERATEDEFINITIONSRESPONSE']._serialized_start=1705
  _globals['_DELETERATEDEFINITIONSRESPONSE']._serialized_end=1736
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_start=1738
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_end=1810
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_start=1812
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_end=1932
  _globals['_GETRATEHISTORYREQUEST']._serialized_start=1935
  _globals['_GETRATEHISTORYREQUEST']._serialized_end=2124
  _globals['_GETRATEHISTORYRESPONSE']._serialized_start=2126
  _globals['_GETRATEHISTORYRESPONSE']._serialized_end=2230
  _globals['_LISTACTIVERATEDEFINITIONSREQUEST']._serialized_start=2233
  _globals['_LISTACTIVERATEDEFINITIONSREQUEST']._serialized_end=2495
  _globals['_LISTACTIVERATEDEFINITIONSRESPONSE']._serialized_start=2498
  _globals['_LISTACTIVERATEDEFINITIONSRESPONSE']._serialized_end=2650
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_start=2653
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_end=2909
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_start=2912
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_end=3058
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=3061
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=3301
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=3303
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=3340
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_start=3343
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_end=3576
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_start=3578
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_end=3608
# @@protoc_insertion_point(module_scope)
