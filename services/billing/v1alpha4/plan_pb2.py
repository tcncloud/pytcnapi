# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha4/plan.proto
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
    'services/billing/v1alpha4/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha4 import plan_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_plan__pb2
from services.billing.entities.v1alpha4 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha4_dot_rates__pb2
from services.billing.v1alpha4 import core_pb2 as services_dot_billing_dot_v1alpha4_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$services/billing/v1alpha4/plan.proto\x12\x19services.billing.v1alpha4\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-services/billing/entities/v1alpha4/plan.proto\x1a.services/billing/entities/v1alpha4/rates.proto\x1a$services/billing/v1alpha4/core.proto\"\x9a\x01\n\x1c\x41pplyBillingPlanDraftRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x17\n\x07org_ids\x18\x03 \x03(\tR\x06orgIds\"I\n\x1d\x41pplyBillingPlanDraftResponse\x12(\n\x10\x62illing_plan_ids\x18\x01 \x03(\tR\x0e\x62illingPlanIds\"\x96\x01\n\x18\x43reateBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha4.BillingPlanR\x0b\x62illingPlan\"C\n\x19\x43reateBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"B\n\x18\x44\x65leteBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\x1b\n\x19\x44\x65leteBillingPlanResponse\"?\n\x15GetBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"l\n\x16GetBillingPlanResponse\x12R\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha4.BillingPlanR\x0b\x62illingPlan\"\xf7\x01\n\x17ListBillingPlansRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha4.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha4.PageR\x04page\"\x86\x01\n\x18ListBillingPlansResponse\x12T\n\rbilling_plans\x18\x01 \x03(\x0b\x32/.services.billing.entities.v1alpha4.BillingPlanR\x0c\x62illingPlans\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xd3\x01\n\x18UpdateBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha4.BillingPlanR\x0b\x62illingPlan\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x1b\n\x19UpdateBillingPlanResponse\"\xa8\x01\n\x1b\x43reateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha4.RateDefinitionR\x0erateDefinition\"L\n\x1c\x43reateRateDefinitionResponse\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"K\n\x1b\x44\x65leteRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"\x1e\n\x1c\x44\x65leteRateDefinitionResponse\"H\n\x18GetRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\"x\n\x19GetRateDefinitionResponse\x12[\n\x0frate_definition\x18\x01 \x01(\x0b\x32\x32.services.billing.entities.v1alpha4.RateDefinitionR\x0erateDefinition\"\x80\x02\n\x1aListRateDefinitionsRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha4.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha4.PageR\x04page\"\x92\x01\n\x1bListRateDefinitionsResponse\x12]\n\x10rate_definitions\x18\x01 \x03(\x0b\x32\x32.services.billing.entities.v1alpha4.RateDefinitionR\x0frateDefinitions\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xe5\x01\n\x1bUpdateRateDefinitionRequest\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12[\n\x0frate_definition\x18\x02 \x01(\x0b\x32\x32.services.billing.entities.v1alpha4.RateDefinitionR\x0erateDefinition\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x1e\n\x1cUpdateRateDefinitionResponseB\xb0\x01\n\x1d\x63om.services.billing.v1alpha4B\tPlanProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha4\xca\x02\x19Services\\Billing\\V1alpha4\xe2\x02%Services\\Billing\\V1alpha4\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha4.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha4B\tPlanProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha4\312\002\031Services\\Billing\\V1alpha4\342\002%Services\\Billing\\V1alpha4\\GPBMetadata\352\002\033Services::Billing::V1alpha4'
  _globals['_APPLYBILLINGPLANDRAFTREQUEST']._serialized_start=268
  _globals['_APPLYBILLINGPLANDRAFTREQUEST']._serialized_end=422
  _globals['_APPLYBILLINGPLANDRAFTRESPONSE']._serialized_start=424
  _globals['_APPLYBILLINGPLANDRAFTRESPONSE']._serialized_end=497
  _globals['_CREATEBILLINGPLANREQUEST']._serialized_start=500
  _globals['_CREATEBILLINGPLANREQUEST']._serialized_end=650
  _globals['_CREATEBILLINGPLANRESPONSE']._serialized_start=652
  _globals['_CREATEBILLINGPLANRESPONSE']._serialized_end=719
  _globals['_DELETEBILLINGPLANREQUEST']._serialized_start=721
  _globals['_DELETEBILLINGPLANREQUEST']._serialized_end=787
  _globals['_DELETEBILLINGPLANRESPONSE']._serialized_start=789
  _globals['_DELETEBILLINGPLANRESPONSE']._serialized_end=816
  _globals['_GETBILLINGPLANREQUEST']._serialized_start=818
  _globals['_GETBILLINGPLANREQUEST']._serialized_end=881
  _globals['_GETBILLINGPLANRESPONSE']._serialized_start=883
  _globals['_GETBILLINGPLANRESPONSE']._serialized_end=991
  _globals['_LISTBILLINGPLANSREQUEST']._serialized_start=994
  _globals['_LISTBILLINGPLANSREQUEST']._serialized_end=1241
  _globals['_LISTBILLINGPLANSRESPONSE']._serialized_start=1244
  _globals['_LISTBILLINGPLANSRESPONSE']._serialized_end=1378
  _globals['_UPDATEBILLINGPLANREQUEST']._serialized_start=1381
  _globals['_UPDATEBILLINGPLANREQUEST']._serialized_end=1592
  _globals['_UPDATEBILLINGPLANRESPONSE']._serialized_start=1594
  _globals['_UPDATEBILLINGPLANRESPONSE']._serialized_end=1621
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_start=1624
  _globals['_CREATERATEDEFINITIONREQUEST']._serialized_end=1792
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_start=1794
  _globals['_CREATERATEDEFINITIONRESPONSE']._serialized_end=1870
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_start=1872
  _globals['_DELETERATEDEFINITIONREQUEST']._serialized_end=1947
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_start=1949
  _globals['_DELETERATEDEFINITIONRESPONSE']._serialized_end=1979
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_start=1981
  _globals['_GETRATEDEFINITIONREQUEST']._serialized_end=2053
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_start=2055
  _globals['_GETRATEDEFINITIONRESPONSE']._serialized_end=2175
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_start=2178
  _globals['_LISTRATEDEFINITIONSREQUEST']._serialized_end=2434
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_start=2437
  _globals['_LISTRATEDEFINITIONSRESPONSE']._serialized_end=2583
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_start=2586
  _globals['_UPDATERATEDEFINITIONREQUEST']._serialized_end=2815
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_start=2817
  _globals['_UPDATERATEDEFINITIONRESPONSE']._serialized_end=2847
# @@protoc_insertion_point(module_scope)
