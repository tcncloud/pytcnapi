# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha4/service.proto
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
    'services/billing/v1alpha4/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.billing.v1alpha4 import defaults_pb2 as services_dot_billing_dot_v1alpha4_dot_defaults__pb2
from services.billing.v1alpha4 import invoice_pb2 as services_dot_billing_dot_v1alpha4_dot_invoice__pb2
from services.billing.v1alpha4 import matching_rule_pb2 as services_dot_billing_dot_v1alpha4_dot_matching__rule__pb2
from services.billing.v1alpha4 import plan_pb2 as services_dot_billing_dot_v1alpha4_dot_plan__pb2
from services.billing.v1alpha4 import tag_pb2 as services_dot_billing_dot_v1alpha4_dot_tag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'services/billing/v1alpha4/service.proto\x12\x19services.billing.v1alpha4\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a(services/billing/v1alpha4/defaults.proto\x1a\'services/billing/v1alpha4/invoice.proto\x1a-services/billing/v1alpha4/matching_rule.proto\x1a$services/billing/v1alpha4/plan.proto\x1a#services/billing/v1alpha4/tag.proto2\xef\x35\n\x0e\x42illingService\x12\xd1\x01\n\x15\x41pplyBillingPlanDraft\x12\x37.services.billing.v1alpha4.ApplyBillingPlanDraftRequest\x1a\x38.services.billing.v1alpha4.ApplyBillingPlanDraftResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/billing/v1alpha4/applybillingplandraft:\x01*\x12\xc1\x01\n\x11\x43reateBillingPlan\x12\x33.services.billing.v1alpha4.CreateBillingPlanRequest\x1a\x34.services.billing.v1alpha4.CreateBillingPlanResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha4/createbillingplan:\x01*\x12\xc1\x01\n\x11\x44\x65leteBillingPlan\x12\x33.services.billing.v1alpha4.DeleteBillingPlanRequest\x1a\x34.services.billing.v1alpha4.DeleteBillingPlanResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha4/deletebillingplan:\x01*\x12\xb5\x01\n\x0eGetBillingPlan\x12\x30.services.billing.v1alpha4.GetBillingPlanRequest\x1a\x31.services.billing.v1alpha4.GetBillingPlanResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02.\")/services/billing/v1alpha4/getbillingplan:\x01*\x12\xbd\x01\n\x10ListBillingPlans\x12\x32.services.billing.v1alpha4.ListBillingPlansRequest\x1a\x33.services.billing.v1alpha4.ListBillingPlansResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x30\"+/services/billing/v1alpha4/listbillingplans:\x01*\x12\xc1\x01\n\x11UpdateBillingPlan\x12\x33.services.billing.v1alpha4.UpdateBillingPlanRequest\x1a\x34.services.billing.v1alpha4.UpdateBillingPlanResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha4/updatebillingplan:\x01*\x12\xf0\x01\n\x1c\x41pplyDefaultBillingPlanDraft\x12>.services.billing.v1alpha4.ApplyDefaultBillingPlanDraftRequest\x1a?.services.billing.v1alpha4.ApplyDefaultBillingPlanDraftResponse\"O\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02<\"7/services/billing/v1alpha4/applydefaultbillingplandraft:\x01*\x12\xe0\x01\n\x18\x43reateDefaultBillingPlan\x12:.services.billing.v1alpha4.CreateDefaultBillingPlanRequest\x1a;.services.billing.v1alpha4.CreateDefaultBillingPlanResponse\"K\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha4/createdefaultbillingplan:\x01*\x12\xe0\x01\n\x18\x44\x65leteDefaultBillingPlan\x12:.services.billing.v1alpha4.DeleteDefaultBillingPlanRequest\x1a;.services.billing.v1alpha4.DeleteDefaultBillingPlanResponse\"K\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha4/deletedefaultbillingplan:\x01*\x12\xd4\x01\n\x15GetDefaultBillingPlan\x12\x37.services.billing.v1alpha4.GetDefaultBillingPlanRequest\x1a\x38.services.billing.v1alpha4.GetDefaultBillingPlanResponse\"H\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x35\"0/services/billing/v1alpha4/getdefaultbillingplan:\x01*\x12\xdc\x01\n\x17ListDefaultBillingPlans\x12\x39.services.billing.v1alpha4.ListDefaultBillingPlansRequest\x1a:.services.billing.v1alpha4.ListDefaultBillingPlansResponse\"J\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x37\"2/services/billing/v1alpha4/listdefaultbillingplans:\x01*\x12\xe0\x01\n\x18UpdateDefaultBillingPlan\x12:.services.billing.v1alpha4.UpdateDefaultBillingPlanRequest\x1a;.services.billing.v1alpha4.UpdateDefaultBillingPlanResponse\"K\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha4/updatedefaultbillingplan:\x01*\x12\xcd\x01\n\x14\x43reateRateDefinition\x12\x36.services.billing.v1alpha4.CreateRateDefinitionRequest\x1a\x37.services.billing.v1alpha4.CreateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha4/createratedefinition:\x01*\x12\xcd\x01\n\x14\x44\x65leteRateDefinition\x12\x36.services.billing.v1alpha4.DeleteRateDefinitionRequest\x1a\x37.services.billing.v1alpha4.DeleteRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha4/deleteratedefinition:\x01*\x12\xc1\x01\n\x11GetRateDefinition\x12\x33.services.billing.v1alpha4.GetRateDefinitionRequest\x1a\x34.services.billing.v1alpha4.GetRateDefinitionResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha4/getratedefinition:\x01*\x12\xc9\x01\n\x13ListRateDefinitions\x12\x35.services.billing.v1alpha4.ListRateDefinitionsRequest\x1a\x36.services.billing.v1alpha4.ListRateDefinitionsResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x33\"./services/billing/v1alpha4/listratedefinitions:\x01*\x12\xcd\x01\n\x14UpdateRateDefinition\x12\x36.services.billing.v1alpha4.UpdateRateDefinitionRequest\x1a\x37.services.billing.v1alpha4.UpdateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha4/updateratedefinition:\x01*\x12\xec\x01\n\x1b\x43reateDefaultRateDefinition\x12=.services.billing.v1alpha4.CreateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha4.CreateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha4/createdefaultratedefinition:\x01*\x12\xec\x01\n\x1b\x44\x65leteDefaultRateDefinition\x12=.services.billing.v1alpha4.DeleteDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha4.DeleteDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha4/deletedefaultratedefinition:\x01*\x12\xe0\x01\n\x18GetDefaultRateDefinition\x12:.services.billing.v1alpha4.GetDefaultRateDefinitionRequest\x1a;.services.billing.v1alpha4.GetDefaultRateDefinitionResponse\"K\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x38\"3/services/billing/v1alpha4/getdefaultratedefinition:\x01*\x12\xe8\x01\n\x1aListDefaultRateDefinitions\x12<.services.billing.v1alpha4.ListDefaultRateDefinitionsRequest\x1a=.services.billing.v1alpha4.ListDefaultRateDefinitionsResponse\"M\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02:\"5/services/billing/v1alpha4/listdefaultratedefinitions:\x01*\x12\xec\x01\n\x1bUpdateDefaultRateDefinition\x12=.services.billing.v1alpha4.UpdateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha4.UpdateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha4/updatedefaultratedefinition:\x01*\x12\xc8\x01\n\x12\x43reateMatchingRule\x12\x34.services.billing.v1alpha4.CreateMatchingRuleRequest\x1a\x35.services.billing.v1alpha4.CreateMatchingRuleResponse\"E\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x32\"-/services/billing/v1alpha4/creatematchingrule:\x01*\x12\xc8\x01\n\x12\x44\x65leteMatchingRule\x12\x34.services.billing.v1alpha4.DeleteMatchingRuleRequest\x1a\x35.services.billing.v1alpha4.DeleteMatchingRuleResponse\"E\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x32\"-/services/billing/v1alpha4/deletematchingrule:\x01*\x12\xbc\x01\n\x0fGetMatchingRule\x12\x31.services.billing.v1alpha4.GetMatchingRuleRequest\x1a\x32.services.billing.v1alpha4.GetMatchingRuleResponse\"B\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02/\"*/services/billing/v1alpha4/getmatchingrule:\x01*\x12\xc4\x01\n\x11ListMatchingRules\x12\x33.services.billing.v1alpha4.ListMatchingRulesRequest\x1a\x34.services.billing.v1alpha4.ListMatchingRulesResponse\"D\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha4/listmatchingrules:\x01*\x12\xc8\x01\n\x12UpdateMatchingRule\x12\x34.services.billing.v1alpha4.UpdateMatchingRuleRequest\x1a\x35.services.billing.v1alpha4.UpdateMatchingRuleResponse\"E\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x32\"-/services/billing/v1alpha4/updatematchingrule:\x01*\x12\xc0\x01\n\x10\x43reateBillingTag\x12\x32.services.billing.v1alpha4.CreateBillingTagRequest\x1a\x33.services.billing.v1alpha4.CreateBillingTagResponse\"C\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x30\"+/services/billing/v1alpha4/createbillingtag:\x01*\x12\xc0\x01\n\x10\x44\x65leteBillingTag\x12\x32.services.billing.v1alpha4.DeleteBillingTagRequest\x1a\x33.services.billing.v1alpha4.DeleteBillingTagResponse\"C\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x30\"+/services/billing/v1alpha4/deletebillingtag:\x01*\x12\xb4\x01\n\rGetBillingTag\x12/.services.billing.v1alpha4.GetBillingTagRequest\x1a\x30.services.billing.v1alpha4.GetBillingTagResponse\"@\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha4/getbillingtag:\x01*\x12\xbc\x01\n\x0fListBillingTags\x12\x31.services.billing.v1alpha4.ListBillingTagsRequest\x1a\x32.services.billing.v1alpha4.ListBillingTagsResponse\"B\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02/\"*/services/billing/v1alpha4/listbillingtags:\x01*\x12\xc0\x01\n\x10UpdateBillingTag\x12\x32.services.billing.v1alpha4.UpdateBillingTagRequest\x1a\x33.services.billing.v1alpha4.UpdateBillingTagResponse\"C\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02\x30\"+/services/billing/v1alpha4/updatebillingtag:\x01*\x12\xb1\x01\n\rExportInvoice\x12/.services.billing.v1alpha4.ExportInvoiceRequest\x1a\x30.services.billing.v1alpha4.ExportInvoiceResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xf1\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha4/exportinvoice:\x01*B\xb3\x01\n\x1d\x63om.services.billing.v1alpha4B\x0cServiceProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha4\xca\x02\x19Services\\Billing\\V1alpha4\xe2\x02%Services\\Billing\\V1alpha4\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha4.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha4B\014ServiceProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha4\312\002\031Services\\Billing\\V1alpha4\342\002%Services\\Billing\\V1alpha4\\GPBMetadata\352\002\033Services::Billing::V1alpha4'
  _globals['_BILLINGSERVICE'].methods_by_name['ApplyBillingPlanDraft']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ApplyBillingPlanDraft']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/billing/v1alpha4/applybillingplandraft:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingPlan']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha4/createbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingPlan']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha4/deletebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingPlan']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002.\")/services/billing/v1alpha4/getbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingPlans']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingPlans']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0020\"+/services/billing/v1alpha4/listbillingplans:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingPlan']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha4/updatebillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ApplyDefaultBillingPlanDraft']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ApplyDefaultBillingPlanDraft']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002<\"7/services/billing/v1alpha4/applydefaultbillingplandraft:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultBillingPlan']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha4/createdefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultBillingPlan']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha4/deletedefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetDefaultBillingPlan']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0025\"0/services/billing/v1alpha4/getdefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListDefaultBillingPlans']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListDefaultBillingPlans']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0027\"2/services/billing/v1alpha4/listdefaultbillingplans:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultBillingPlan']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultBillingPlan']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha4/updatedefaultbillingplan:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha4/createratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha4/deleteratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha4/getratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0023\"./services/billing/v1alpha4/listratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha4/updateratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha4/createdefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha4/deletedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0028\"3/services/billing/v1alpha4/getdefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListDefaultRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListDefaultRateDefinitions']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002:\"5/services/billing/v1alpha4/listdefaultratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha4/updatedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateMatchingRule']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateMatchingRule']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0022\"-/services/billing/v1alpha4/creatematchingrule:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteMatchingRule']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteMatchingRule']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0022\"-/services/billing/v1alpha4/deletematchingrule:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetMatchingRule']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetMatchingRule']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002/\"*/services/billing/v1alpha4/getmatchingrule:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListMatchingRules']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListMatchingRules']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0021\",/services/billing/v1alpha4/listmatchingrules:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateMatchingRule']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateMatchingRule']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0022\"-/services/billing/v1alpha4/updatematchingrule:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingTag']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateBillingTag']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0020\"+/services/billing/v1alpha4/createbillingtag:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingTag']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteBillingTag']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0020\"+/services/billing/v1alpha4/deletebillingtag:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingTag']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetBillingTag']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002-\"(/services/billing/v1alpha4/getbillingtag:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingTags']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListBillingTags']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002/\"*/services/billing/v1alpha4/listbillingtags:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingTag']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateBillingTag']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\0020\"+/services/billing/v1alpha4/updatebillingtag:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._serialized_options = b'\272\270\221\002\005\n\003\010\361\001\202\323\344\223\002-\"(/services/billing/v1alpha4/exportinvoice:\001*'
  _globals['_BILLINGSERVICE']._serialized_start=331
  _globals['_BILLINGSERVICE']._serialized_end=7226
# @@protoc_insertion_point(module_scope)
