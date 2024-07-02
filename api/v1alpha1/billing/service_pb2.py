# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/billing/service.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'api/v1alpha1/billing/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.billing import entities_pb2 as api_dot_v1alpha1_dot_billing_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/billing/service.proto\x12\x14\x61pi.v1alpha1.billing\x1a\x17\x61nnotations/authz.proto\x1a#api/v1alpha1/billing/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xb6\x05\n\x07\x42illing\x12\xa0\x01\n\x0eGetBillingPlan\x12\'.api.v1alpha1.billing.GetBillingPlanReq\x1a\'.api.v1alpha1.billing.GetBillingPlanRes\"<\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/billing/getbillingplan:\x01*\x12\xac\x01\n\x11UpdateBillingPlan\x12*.api.v1alpha1.billing.UpdateBillingPlanReq\x1a*.api.v1alpha1.billing.UpdateBillingPlanRes\"?\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/billing/updatebillingplan:\x01*\x12\x90\x01\n\nGetInvoice\x12#.api.v1alpha1.billing.GetInvoiceReq\x1a#.api.v1alpha1.billing.GetInvoiceRes\"8\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02%\" /api/v1alpha1/billing/getinvoice:\x01*\x12\xc0\x01\n\x16\x45xportGeneratedInvoice\x12/.api.v1alpha1.billing.ExportGeneratedInvoiceReq\x1a/.api.v1alpha1.billing.ExportGeneratedInvoiceRes\"D\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/billing/exportgeneratedinvoice:\x01*\x1a\x03\x88\x02\x01\x42\x9a\x01\n\x18\x63om.api.v1alpha1.billingB\x0cServiceProtoP\x01\xa2\x02\x03\x41VB\xaa\x02\x14\x41pi.V1alpha1.Billing\xca\x02\x14\x41pi\\V1alpha1\\Billing\xe2\x02 Api\\V1alpha1\\Billing\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.billing.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.billingB\014ServiceProtoP\001\242\002\003AVB\252\002\024Api.V1alpha1.Billing\312\002\024Api\\V1alpha1\\Billing\342\002 Api\\V1alpha1\\Billing\\GPBMetadata\352\002\026Api::V1alpha1::Billing'
  _globals['_BILLING']._loaded_options = None
  _globals['_BILLING']._serialized_options = b'\210\002\001'
  _globals['_BILLING'].methods_by_name['GetBillingPlan']._loaded_options = None
  _globals['_BILLING'].methods_by_name['GetBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002)\"$/api/v1alpha1/billing/getbillingplan:\001*'
  _globals['_BILLING'].methods_by_name['UpdateBillingPlan']._loaded_options = None
  _globals['_BILLING'].methods_by_name['UpdateBillingPlan']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002,\"\'/api/v1alpha1/billing/updatebillingplan:\001*'
  _globals['_BILLING'].methods_by_name['GetInvoice']._loaded_options = None
  _globals['_BILLING'].methods_by_name['GetInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002%\" /api/v1alpha1/billing/getinvoice:\001*'
  _globals['_BILLING'].methods_by_name['ExportGeneratedInvoice']._loaded_options = None
  _globals['_BILLING'].methods_by_name['ExportGeneratedInvoice']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0021\",/api/v1alpha1/billing/exportgeneratedinvoice:\001*'
  _globals['_BILLING']._serialized_start=153
  _globals['_BILLING']._serialized_end=847
# @@protoc_insertion_point(module_scope)
