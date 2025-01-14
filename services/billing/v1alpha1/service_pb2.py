# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha1/service.proto
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
    'services/billing/v1alpha1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.billing.v1alpha1 import invoices_pb2 as services_dot_billing_dot_v1alpha1_dot_invoices__pb2
from services.billing.v1alpha1 import plans_pb2 as services_dot_billing_dot_v1alpha1_dot_plans__pb2
from services.billing.v1alpha1 import rates_pb2 as services_dot_billing_dot_v1alpha1_dot_rates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'services/billing/v1alpha1/service.proto\x12\x19services.billing.v1alpha1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a(services/billing/v1alpha1/invoices.proto\x1a%services/billing/v1alpha1/plans.proto\x1a%services/billing/v1alpha1/rates.proto2\xb5-\n\x0e\x42illingService\x12\xc4\x01\n\x11\x43ommitBillingPlan\x12\x33.services.billing.v1alpha1.CommitBillingPlanRequest\x1a\x34.services.billing.v1alpha1.CommitBillingPlanResponse\"D\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha1/commitbillingplan:\x01*\x12\xe3\x01\n\x18\x43ommitDefaultBillingPlan\x12:.services.billing.v1alpha1.CommitDefaultBillingPlanRequest\x1a;.services.billing.v1alpha1.CommitDefaultBillingPlanResponse\"N\x88\x02\x01\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha1/commitdefaultbillingplan:\x01*\x12\xc4\x01\n\x11\x43reateBillingPlan\x12\x33.services.billing.v1alpha1.CreateBillingPlanRequest\x1a\x34.services.billing.v1alpha1.CreateBillingPlanResponse\"D\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha1/createbillingplan:\x01*\x12\xe3\x01\n\x18\x43reateDefaultBillingPlan\x12:.services.billing.v1alpha1.CreateDefaultBillingPlanRequest\x1a;.services.billing.v1alpha1.CreateDefaultBillingPlanResponse\"N\x88\x02\x01\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha1/createdefaultbillingplan:\x01*\x12\xec\x01\n\x1b\x43reateDefaultRateDefinition\x12=.services.billing.v1alpha1.CreateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha1.CreateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha1/createdefaultratedefinition:\x01*\x12\xb4\x01\n\rCreateInvoice\x12/.services.billing.v1alpha1.CreateInvoiceRequest\x1a\x30.services.billing.v1alpha1.CreateInvoiceResponse\"@\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha1/createinvoice:\x01*\x12\xcd\x01\n\x14\x43reateRateDefinition\x12\x36.services.billing.v1alpha1.CreateRateDefinitionRequest\x1a\x37.services.billing.v1alpha1.CreateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha1/createratedefinition:\x01*\x12\xc4\x01\n\x11\x44\x65leteBillingPlan\x12\x33.services.billing.v1alpha1.DeleteBillingPlanRequest\x1a\x34.services.billing.v1alpha1.DeleteBillingPlanResponse\"D\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha1/deletebillingplan:\x01*\x12\xe3\x01\n\x18\x44\x65leteDefaultBillingPlan\x12:.services.billing.v1alpha1.DeleteDefaultBillingPlanRequest\x1a;.services.billing.v1alpha1.DeleteDefaultBillingPlanResponse\"N\x88\x02\x01\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha1/deletedefaultbillingplan:\x01*\x12\xec\x01\n\x1b\x44\x65leteDefaultRateDefinition\x12=.services.billing.v1alpha1.DeleteDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha1.DeleteDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha1/deletedefaultratedefinition:\x01*\x12\xb4\x01\n\rDeleteInvoice\x12/.services.billing.v1alpha1.DeleteInvoiceRequest\x1a\x30.services.billing.v1alpha1.DeleteInvoiceResponse\"@\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha1/deleteinvoice:\x01*\x12\xcd\x01\n\x14\x44\x65leteRateDefinition\x12\x36.services.billing.v1alpha1.DeleteRateDefinitionRequest\x1a\x37.services.billing.v1alpha1.DeleteRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha1/deleteratedefinition:\x01*\x12\xd0\x01\n\x14\x44uplicateBillingPlan\x12\x36.services.billing.v1alpha1.DuplicateBillingPlanRequest\x1a\x37.services.billing.v1alpha1.DuplicateBillingPlanResponse\"G\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha1/duplicatebillingplan:\x01*\x12\xef\x01\n\x1b\x44uplicateDefaultBillingPlan\x12=.services.billing.v1alpha1.DuplicateDefaultBillingPlanRequest\x1a>.services.billing.v1alpha1.DuplicateDefaultBillingPlanResponse\"Q\x88\x02\x01\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha1/duplicatedefaultbillingplan:\x01*\x12\xb1\x01\n\rExportInvoice\x12/.services.billing.v1alpha1.ExportInvoiceRequest\x1a\x30.services.billing.v1alpha1.ExportInvoiceResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xf1\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha1/exportinvoice:\x01*\x12\xd0\x01\n\x14GetActiveBillingPlan\x12\x36.services.billing.v1alpha1.GetActiveBillingPlanRequest\x1a\x37.services.billing.v1alpha1.GetActiveBillingPlanResponse\"G\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha1/getactivebillingplan:\x01*\x12\xb8\x01\n\x0eGetBillingPlan\x12\x30.services.billing.v1alpha1.GetBillingPlanRequest\x1a\x31.services.billing.v1alpha1.GetBillingPlanResponse\"A\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02.\")/services/billing/v1alpha1/getbillingplan:\x01*\x12\xd4\x01\n\x15GetBillingPlanHistory\x12\x37.services.billing.v1alpha1.GetBillingPlanHistoryRequest\x1a\x38.services.billing.v1alpha1.GetBillingPlanHistoryResponse\"H\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/billing/v1alpha1/getbillingplanhistory:\x01*\x12\xa8\x01\n\nGetInvoice\x12,.services.billing.v1alpha1.GetInvoiceRequest\x1a-.services.billing.v1alpha1.GetInvoiceResponse\"=\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02*\"%/services/billing/v1alpha1/getinvoice:\x01*\x12\xc1\x01\n\x11GetRateDefinition\x12\x33.services.billing.v1alpha1.GetRateDefinitionRequest\x1a\x34.services.billing.v1alpha1.GetRateDefinitionResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha1/getratedefinition:\x01*\x12\xc0\x01\n\x10ListBillingPlans\x12\x32.services.billing.v1alpha1.ListBillingPlansRequest\x1a\x33.services.billing.v1alpha1.ListBillingPlansResponse\"C\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x30\"+/services/billing/v1alpha1/listbillingplans:\x01*\x12\xb0\x01\n\x0cListInvoices\x12..services.billing.v1alpha1.ListInvoicesRequest\x1a/.services.billing.v1alpha1.ListInvoicesResponse\"?\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02,\"\'/services/billing/v1alpha1/listinvoices:\x01*\x12\xc9\x01\n\x13ListRateDefinitions\x12\x35.services.billing.v1alpha1.ListRateDefinitionsRequest\x1a\x36.services.billing.v1alpha1.ListRateDefinitionsResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x33\"./services/billing/v1alpha1/listratedefinitions:\x01*\x12\xc4\x01\n\x11UpdateBillingPlan\x12\x33.services.billing.v1alpha1.UpdateBillingPlanRequest\x1a\x34.services.billing.v1alpha1.UpdateBillingPlanResponse\"D\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha1/updatebillingplan:\x01*\x12\xe3\x01\n\x18UpdateDefaultBillingPlan\x12:.services.billing.v1alpha1.UpdateDefaultBillingPlanRequest\x1a;.services.billing.v1alpha1.UpdateDefaultBillingPlanResponse\"N\x88\x02\x01\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha1/updatedefaultbillingplan:\x01*\x12\xec\x01\n\x1bUpdateDefaultRateDefinition\x12=.services.billing.v1alpha1.UpdateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha1.UpdateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha1/updatedefaultratedefinition:\x01*\x12\xb4\x01\n\rUpdateInvoice\x12/.services.billing.v1alpha1.UpdateInvoiceRequest\x1a\x30.services.billing.v1alpha1.UpdateInvoiceResponse\"@\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha1/updateinvoice:\x01*\x12\xcd\x01\n\x14UpdateRateDefinition\x12\x36.services.billing.v1alpha1.UpdateRateDefinitionRequest\x1a\x37.services.billing.v1alpha1.UpdateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha1/updateratedefinition:\x01*B\xb3\x01\n\x1d\x63om.services.billing.v1alpha1B\x0cServiceProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha1\xca\x02\x19Services\\Billing\\V1alpha1\xe2\x02%Services\\Billing\\V1alpha1\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha1B\014ServiceProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha1\312\002\031Services\\Billing\\V1alpha1\342\002%Services\\Billing\\V1alpha1\\GPBMetadata\352\002\033Services::Billing::V1alpha1'
  _globals['_BILLINGSERVICE'].methods_by_name['CommitBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CommitBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha1/commitbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CommitDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CommitDefaultBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha1/commitdefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha1/createbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha1/createdefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha1/createdefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002-\"(/services/billing/v1alpha1/createinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha1/createratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha1/deletebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha1/deletedefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha1/deletedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002-\"(/services/billing/v1alpha1/deleteinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha1/deleteratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DuplicateBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DuplicateBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha1/duplicatebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DuplicateDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DuplicateDefaultBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha1/duplicatedefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._serialized_options = b'\272\270\221\002\005\n\003\010\361\001\202\323\344\223\002-\"(/services/billing/v1alpha1/exportinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetActiveBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetActiveBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha1/getactivebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002.\")/services/billing/v1alpha1/getbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlanHistory']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlanHistory']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/billing/v1alpha1/getbillingplanhistory:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002*\"%/services/billing/v1alpha1/getinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha1/getratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingPlans']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingPlans']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0020\"+/services/billing/v1alpha1/listbillingplans:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListInvoices']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListInvoices']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002,\"\'/services/billing/v1alpha1/listinvoices:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0023\"./services/billing/v1alpha1/listratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha1/updatebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha1/updatedefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha1/updatedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002-\"(/services/billing/v1alpha1/updateinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha1/updateratedefinition:\001*'
  _globals['_BILLINGSERVICE']._serialized_start=246
  _globals['_BILLINGSERVICE']._serialized_end=6059
# @@protoc_insertion_point(module_scope)
