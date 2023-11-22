# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/billing/v1alpha1/plans.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha1 import plan_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_plan__pb2
from services.billing.v1alpha1 import core_pb2 as services_dot_billing_dot_v1alpha1_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%services/billing/v1alpha1/plans.proto\x12\x19services.billing.v1alpha1\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-services/billing/entities/v1alpha1/plan.proto\x1a$services/billing/v1alpha1/core.proto\"B\n\x18\x43ommitBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\x1b\n\x19\x43ommitBillingPlanResponse\"I\n\x1f\x43ommitDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\"\n CommitDefaultBillingPlanResponse\"\x96\x01\n\x18\x43reateBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"C\n\x19\x43reateBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\x9d\x01\n\x1f\x43reateDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"J\n CreateDefaultBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"B\n\x18\x44\x65leteBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\x1b\n\x19\x44\x65leteBillingPlanResponse\"I\n\x1f\x44\x65leteDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\"\n DeleteDefaultBillingPlanResponse\"\x99\x01\n\x1b\x44uplicateBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"F\n\x1c\x44uplicateBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"\xa0\x01\n\"DuplicateDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"M\n#DuplicateDefaultBillingPlanResponse\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"w\n\x1bGetActiveBillingPlanRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x41\n\x0e\x65\x66\x66\x65\x63tive_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\reffectiveTime\"r\n\x1cGetActiveBillingPlanResponse\x12R\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"?\n\x15GetBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\"l\n\x16GetBillingPlanResponse\x12R\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\"\xf7\x01\n\x17ListBillingPlansRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x06\x66ields\x12\x33\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha1.SortR\x04sort\x12\x33\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha1.PageR\x04page\"\x86\x01\n\x18ListBillingPlansResponse\x12T\n\rbilling_plans\x18\x01 \x03(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0c\x62illingPlans\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\xd7\x01\n\x18UpdateBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"\x1b\n\x19UpdateBillingPlanResponse\"\xde\x01\n\x1fUpdateDefaultBillingPlanRequest\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12R\n\x0c\x62illing_plan\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BillingPlanR\x0b\x62illingPlan\x12?\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cupdateFields\"\"\n UpdateDefaultBillingPlanResponseB\xb1\x01\n\x1d\x63om.services.billing.v1alpha1B\nPlansProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha1\xca\x02\x19Services\\Billing\\V1alpha1\xe2\x02%Services\\Billing\\V1alpha1\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha1.plans_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha1B\nPlansProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha1\312\002\031Services\\Billing\\V1alpha1\342\002%Services\\Billing\\V1alpha1\\GPBMetadata\352\002\033Services::Billing::V1alpha1'
  _globals['_COMMITBILLINGPLANREQUEST']._serialized_start=220
  _globals['_COMMITBILLINGPLANREQUEST']._serialized_end=286
  _globals['_COMMITBILLINGPLANRESPONSE']._serialized_start=288
  _globals['_COMMITBILLINGPLANRESPONSE']._serialized_end=315
  _globals['_COMMITDEFAULTBILLINGPLANREQUEST']._serialized_start=317
  _globals['_COMMITDEFAULTBILLINGPLANREQUEST']._serialized_end=390
  _globals['_COMMITDEFAULTBILLINGPLANRESPONSE']._serialized_start=392
  _globals['_COMMITDEFAULTBILLINGPLANRESPONSE']._serialized_end=426
  _globals['_CREATEBILLINGPLANREQUEST']._serialized_start=429
  _globals['_CREATEBILLINGPLANREQUEST']._serialized_end=579
  _globals['_CREATEBILLINGPLANRESPONSE']._serialized_start=581
  _globals['_CREATEBILLINGPLANRESPONSE']._serialized_end=648
  _globals['_CREATEDEFAULTBILLINGPLANREQUEST']._serialized_start=651
  _globals['_CREATEDEFAULTBILLINGPLANREQUEST']._serialized_end=808
  _globals['_CREATEDEFAULTBILLINGPLANRESPONSE']._serialized_start=810
  _globals['_CREATEDEFAULTBILLINGPLANRESPONSE']._serialized_end=884
  _globals['_DELETEBILLINGPLANREQUEST']._serialized_start=886
  _globals['_DELETEBILLINGPLANREQUEST']._serialized_end=952
  _globals['_DELETEBILLINGPLANRESPONSE']._serialized_start=954
  _globals['_DELETEBILLINGPLANRESPONSE']._serialized_end=981
  _globals['_DELETEDEFAULTBILLINGPLANREQUEST']._serialized_start=983
  _globals['_DELETEDEFAULTBILLINGPLANREQUEST']._serialized_end=1056
  _globals['_DELETEDEFAULTBILLINGPLANRESPONSE']._serialized_start=1058
  _globals['_DELETEDEFAULTBILLINGPLANRESPONSE']._serialized_end=1092
  _globals['_DUPLICATEBILLINGPLANREQUEST']._serialized_start=1095
  _globals['_DUPLICATEBILLINGPLANREQUEST']._serialized_end=1248
  _globals['_DUPLICATEBILLINGPLANRESPONSE']._serialized_start=1250
  _globals['_DUPLICATEBILLINGPLANRESPONSE']._serialized_end=1320
  _globals['_DUPLICATEDEFAULTBILLINGPLANREQUEST']._serialized_start=1323
  _globals['_DUPLICATEDEFAULTBILLINGPLANREQUEST']._serialized_end=1483
  _globals['_DUPLICATEDEFAULTBILLINGPLANRESPONSE']._serialized_start=1485
  _globals['_DUPLICATEDEFAULTBILLINGPLANRESPONSE']._serialized_end=1562
  _globals['_GETACTIVEBILLINGPLANREQUEST']._serialized_start=1564
  _globals['_GETACTIVEBILLINGPLANREQUEST']._serialized_end=1683
  _globals['_GETACTIVEBILLINGPLANRESPONSE']._serialized_start=1685
  _globals['_GETACTIVEBILLINGPLANRESPONSE']._serialized_end=1799
  _globals['_GETBILLINGPLANREQUEST']._serialized_start=1801
  _globals['_GETBILLINGPLANREQUEST']._serialized_end=1864
  _globals['_GETBILLINGPLANRESPONSE']._serialized_start=1866
  _globals['_GETBILLINGPLANRESPONSE']._serialized_end=1974
  _globals['_LISTBILLINGPLANSREQUEST']._serialized_start=1977
  _globals['_LISTBILLINGPLANSREQUEST']._serialized_end=2224
  _globals['_LISTBILLINGPLANSRESPONSE']._serialized_start=2227
  _globals['_LISTBILLINGPLANSRESPONSE']._serialized_end=2361
  _globals['_UPDATEBILLINGPLANREQUEST']._serialized_start=2364
  _globals['_UPDATEBILLINGPLANREQUEST']._serialized_end=2579
  _globals['_UPDATEBILLINGPLANRESPONSE']._serialized_start=2581
  _globals['_UPDATEBILLINGPLANRESPONSE']._serialized_end=2608
  _globals['_UPDATEDEFAULTBILLINGPLANREQUEST']._serialized_start=2611
  _globals['_UPDATEDEFAULTBILLINGPLANREQUEST']._serialized_end=2833
  _globals['_UPDATEDEFAULTBILLINGPLANRESPONSE']._serialized_start=2835
  _globals['_UPDATEDEFAULTBILLINGPLANRESPONSE']._serialized_end=2869
# @@protoc_insertion_point(module_scope)