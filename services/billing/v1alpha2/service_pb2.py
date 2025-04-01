# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha2/service.proto
# Protobuf Python Version: 6.30.2
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
    2,
    '',
    'services/billing/v1alpha2/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from services.billing.v1alpha2 import invoices_pb2 as services_dot_billing_dot_v1alpha2_dot_invoices__pb2
from services.billing.v1alpha2 import rates_pb2 as services_dot_billing_dot_v1alpha2_dot_rates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'services/billing/v1alpha2/service.proto\x12\x19services.billing.v1alpha2\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a(services/billing/v1alpha2/invoices.proto\x1a%services/billing/v1alpha2/rates.proto2\xbb\x19\n\x0e\x42illingService\x12\xec\x01\n\x1b\x43reateDefaultRateDefinition\x12=.services.billing.v1alpha2.CreateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha2.CreateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha2/createdefaultratedefinition:\x01*\x12\xf0\x01\n\x1c\x43reateDefaultRateDefinitions\x12>.services.billing.v1alpha2.CreateDefaultRateDefinitionsRequest\x1a?.services.billing.v1alpha2.CreateDefaultRateDefinitionsResponse\"O\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02<\"7/services/billing/v1alpha2/createdefaultratedefinitions:\x01*\x12\xcd\x01\n\x14\x43reateRateDefinition\x12\x36.services.billing.v1alpha2.CreateRateDefinitionRequest\x1a\x37.services.billing.v1alpha2.CreateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha2/createratedefinition:\x01*\x12\xd1\x01\n\x15\x43reateRateDefinitions\x12\x37.services.billing.v1alpha2.CreateRateDefinitionsRequest\x1a\x38.services.billing.v1alpha2.CreateRateDefinitionsResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/billing/v1alpha2/createratedefinitions:\x01*\x12\xec\x01\n\x1b\x44\x65leteDefaultRateDefinition\x12=.services.billing.v1alpha2.DeleteDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha2.DeleteDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha2/deletedefaultratedefinition:\x01*\x12\xf0\x01\n\x1c\x44\x65leteDefaultRateDefinitions\x12>.services.billing.v1alpha2.DeleteDefaultRateDefinitionsRequest\x1a?.services.billing.v1alpha2.DeleteDefaultRateDefinitionsResponse\"O\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02<\"7/services/billing/v1alpha2/deletedefaultratedefinitions:\x01*\x12\xcd\x01\n\x14\x44\x65leteRateDefinition\x12\x36.services.billing.v1alpha2.DeleteRateDefinitionRequest\x1a\x37.services.billing.v1alpha2.DeleteRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha2/deleteratedefinition:\x01*\x12\xd1\x01\n\x15\x44\x65leteRateDefinitions\x12\x37.services.billing.v1alpha2.DeleteRateDefinitionsRequest\x1a\x38.services.billing.v1alpha2.DeleteRateDefinitionsResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x35\"0/services/billing/v1alpha2/deleteratedefinitions:\x01*\x12\xb1\x01\n\rExportInvoice\x12/.services.billing.v1alpha2.ExportInvoiceRequest\x1a\x30.services.billing.v1alpha2.ExportInvoiceResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xf1\x01\x82\xd3\xe4\x93\x02-\"(/services/billing/v1alpha2/exportinvoice:\x01*\x12\xc1\x01\n\x11GetRateDefinition\x12\x33.services.billing.v1alpha2.GetRateDefinitionRequest\x1a\x34.services.billing.v1alpha2.GetRateDefinitionResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/services/billing/v1alpha2/getratedefinition:\x01*\x12\xb5\x01\n\x0eGetRateHistory\x12\x30.services.billing.v1alpha2.GetRateHistoryRequest\x1a\x31.services.billing.v1alpha2.GetRateHistoryResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02.\")/services/billing/v1alpha2/getratehistory:\x01*\x12\xe1\x01\n\x19ListActiveRateDefinitions\x12;.services.billing.v1alpha2.ListActiveRateDefinitionsRequest\x1a<.services.billing.v1alpha2.ListActiveRateDefinitionsResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x39\"4/services/billing/v1alpha2/listactiveratedefinitions:\x01*\x12\xc9\x01\n\x13ListRateDefinitions\x12\x35.services.billing.v1alpha2.ListRateDefinitionsRequest\x1a\x36.services.billing.v1alpha2.ListRateDefinitionsResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x33\"./services/billing/v1alpha2/listratedefinitions:\x01*\x12\xec\x01\n\x1bUpdateDefaultRateDefinition\x12=.services.billing.v1alpha2.UpdateDefaultRateDefinitionRequest\x1a>.services.billing.v1alpha2.UpdateDefaultRateDefinitionResponse\"N\xba\xb8\x91\x02\x08\n\x06\x08\xc8\x01\x08\xf1\x01\x82\xd3\xe4\x93\x02;\"6/services/billing/v1alpha2/updatedefaultratedefinition:\x01*\x12\xcd\x01\n\x14UpdateRateDefinition\x12\x36.services.billing.v1alpha2.UpdateRateDefinitionRequest\x1a\x37.services.billing.v1alpha2.UpdateRateDefinitionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//services/billing/v1alpha2/updateratedefinition:\x01*B\xb3\x01\n\x1d\x63om.services.billing.v1alpha2B\x0cServiceProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha2\xca\x02\x19Services\\Billing\\V1alpha2\xe2\x02%Services\\Billing\\V1alpha2\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha2B\014ServiceProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha2\312\002\031Services\\Billing\\V1alpha2\342\002%Services\\Billing\\V1alpha2\\GPBMetadata\352\002\033Services::Billing::V1alpha2'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha2/createdefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateDefaultRateDefinitions']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002<\"7/services/billing/v1alpha2/createdefaultratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha2/createratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['CreateRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/billing/v1alpha2/createratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha2/deletedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteDefaultRateDefinitions']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002<\"7/services/billing/v1alpha2/deletedefaultratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha2/deleteratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['DeleteRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0025\"0/services/billing/v1alpha2/deleteratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ExportInvoice']._serialized_options = b'\272\270\221\002\005\n\003\010\361\001\202\323\344\223\002-\"(/services/billing/v1alpha2/exportinvoice:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/services/billing/v1alpha2/getratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateHistory']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['GetRateHistory']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002.\")/services/billing/v1alpha2/getratehistory:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListActiveRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListActiveRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0029\"4/services/billing/v1alpha2/listactiveratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['ListRateDefinitions']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0023\"./services/billing/v1alpha2/listratedefinitions:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateDefaultRateDefinition']._serialized_options = b'\272\270\221\002\010\n\006\010\310\001\010\361\001\202\323\344\223\002;\"6/services/billing/v1alpha2/updatedefaultratedefinition:\001*'
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._loaded_options = None
  _globals['_BILLINGSERVICE'].methods_by_name['UpdateRateDefinition']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//services/billing/v1alpha2/updateratedefinition:\001*'
  _globals['_BILLINGSERVICE']._serialized_start=207
  _globals['_BILLINGSERVICE']._serialized_end=3466
# @@protoc_insertion_point(module_scope)
