# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha3/defaults.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'services/billing/v1alpha3/defaults.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha3 import plan_pb2 as services_dot_billing_dot_entities_dot_v1alpha3_dot_plan__pb2
from services.billing.entities.v1alpha3 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha3_dot_rates__pb2
from services.billing.v1alpha3 import core_pb2 as services_dot_billing_dot_v1alpha3_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(services/billing/v1alpha3/defaults.proto\x12\x19services.billing.v1alpha3\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-services/billing/entities/v1alpha3/plan.proto\x1a.services/billing/entities/v1alpha3/rates.proto\x1a$services/billing/v1alpha3/core.proto\"\xa1\x01\n#ApplyDefaultBillingPlanDraftRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x17\n\x07org_ids\x18\x03 \x03(\tR\x06orgIds\"P\n$ApplyDefaultBillingPlanDraftResponse\x12(\n\x10\x62illing_plan_ids\x18\x01 \x03(\tR\x0e\x62illingPlanIds\"\x9d\x01\n\x1f\x43reateDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BillingPlanR\x0b\x62illingPlan\"J\n CreateDefaultBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"I\n\x1f\x44\x65leteDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\"\n DeleteDefaultBillingPlanResponse\"F\n\x1cGetDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"s\n\x1dGetDefaultBillingPlanResponse\x12R\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BillingPlanR\x0b\x62illingPlan\"\xfe\x01\n\x1eListDefaultBillingPlansRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha3.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha3.PageR\x04page\"\x8d\x01\n\x1fListDefaultBillingPlansResponse\x12T\n\rbilling_plans\x18\x01 \x03(\x0b\x32/.services.billing.entities.v1alpha3.BillingPlanR\x0c\x62illingPlans\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xda\x01\n\x1fUpdateDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BillingPlanR\x0b\x62illingPlan\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\"\n UpdateDefaultBillingPlanResponse\"\xaf\x01\n\"CreateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha3.RateDefinitionR\x0erateDefinition\"S\n#CreateDefaultRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"R\n\"DeleteDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"%\n#DeleteDefaultRateDefinitionResponse\"O\n\x1fGetDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"\x7f\n GetDefaultRateDefinitionResponse\x12[\n\x0frate_definition\x18\x01 \x01(\x0b\x32\x32.services.billing.entities.v1alpha3.RateDefinitionR\x0erateDefinition\"\x87\x02\n!ListDefaultRateDefinitionsRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha3.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha3.PageR\x04page\"\x99\x01\n\"ListDefaultRateDefinitionsResponse\x12]\n\x10rate_definitions\x18\x01 \x03(\x0b\x32\x32.services.billing.entities.v1alpha3.RateDefinitionR\x0frateDefinitions\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xec\x01\n\"UpdateDefaultRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha3.RateDefinitionR\x0erateDefinition\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"%\n#UpdateDefaultRateDefinitionResponseB\xb4\x01\n\x1d\x63om.services.billing.v1alpha3B\rDefaultsProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha3\xca\x02\x19Services\\Billing\\V1alpha3\xe2\x02%Services\\Billing\\V1alpha3\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha3.defaults_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha3B\rDefaultsProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha3\312\002\031Services\\Billing\\V1alpha3\342\002%Services\\Billing\\V1alpha3\\GPBMetadata\352\002\033Services::Billing::V1alpha3'
  _globals['_APPLYDEFAULTBILLINGPLANDRAFTREQUEST']._serialized_start=272
  _globals['_APPLYDEFAULTBILLINGPLANDRAFTREQUEST']._serialized_end=433
  _globals['_APPLYDEFAULTBILLINGPLANDRAFTRESPONSE']._serialized_start=435
  _globals['_APPLYDEFAULTBILLINGPLANDRAFTRESPONSE']._serialized_end=515
  _globals['_CREATEDEFAULTBILLINGPLANREQUEST']._serialized_start=518
  _globals['_CREATEDEFAULTBILLINGPLANREQUEST']._serialized_end=675
  _globals['_CREATEDEFAULTBILLINGPLANRESPONSE']._serialized_start=677
  _globals['_CREATEDEFAULTBILLINGPLANRESPONSE']._serialized_end=751
  _globals['_DELETEDEFAULTBILLINGPLANREQUEST']._serialized_start=753
  _globals['_DELETEDEFAULTBILLINGPLANREQUEST']._serialized_end=826
  _globals['_DELETEDEFAULTBILLINGPLANRESPONSE']._serialized_start=828
  _globals['_DELETEDEFAULTBILLINGPLANRESPONSE']._serialized_end=862
  _globals['_GETDEFAULTBILLINGPLANREQUEST']._serialized_start=864
  _globals['_GETDEFAULTBILLINGPLANREQUEST']._serialized_end=934
  _globals['_GETDEFAULTBILLINGPLANRESPONSE']._serialized_start=936
  _globals['_GETDEFAULTBILLINGPLANRESPONSE']._serialized_end=1051
  _globals['_LISTDEFAULTBILLINGPLANSREQUEST']._serialized_start=1054
  _globals['_LISTDEFAULTBILLINGPLANSREQUEST']._serialized_end=1308
  _globals['_LISTDEFAULTBILLINGPLANSRESPONSE']._serialized_start=1311
  _globals['_LISTDEFAULTBILLINGPLANSRESPONSE']._serialized_end=1452
  _globals['_UPDATEDEFAULTBILLINGPLANREQUEST']._serialized_start=1455
  _globals['_UPDATEDEFAULTBILLINGPLANREQUEST']._serialized_end=1673
  _globals['_UPDATEDEFAULTBILLINGPLANRESPONSE']._serialized_start=1675
  _globals['_UPDATEDEFAULTBILLINGPLANRESPONSE']._serialized_end=1709
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=1712
  _globals['_CREATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=1887
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=1889
  _globals['_CREATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=1972
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=1974
  _globals['_DELETEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=2056
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=2058
  _globals['_DELETEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=2095
  _globals['_GETDEFAULTRATEDEFINITIONREQUEST']._serialized_start=2097
  _globals['_GETDEFAULTRATEDEFINITIONREQUEST']._serialized_end=2176
  _globals['_GETDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=2178
  _globals['_GETDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=2305
  _globals['_LISTDEFAULTRATEDEFINITIONSREQUEST']._serialized_start=2308
  _globals['_LISTDEFAULTRATEDEFINITIONSREQUEST']._serialized_end=2571
  _globals['_LISTDEFAULTRATEDEFINITIONSRESPONSE']._serialized_start=2574
  _globals['_LISTDEFAULTRATEDEFINITIONSRESPONSE']._serialized_end=2727
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_start=2730
  _globals['_UPDATEDEFAULTRATEDEFINITIONREQUEST']._serialized_end=2966
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_start=2968
  _globals['_UPDATEDEFAULTRATEDEFINITIONRESPONSE']._serialized_end=3005
# @@protoc_insertion_point(module_scope)
