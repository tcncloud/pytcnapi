# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/billing/entities.proto
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
    'api/v1alpha1/billing/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons.billing import detail_pb2 as api_dot_commons_dot_billing_dot_detail__pb2
from api.commons.billing import invoice_pb2 as api_dot_commons_dot_billing_dot_invoice__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/billing/entities.proto\x12\x14\x61pi.v1alpha1.billing\x1a\x17\x61nnotations/authz.proto\x1a api/commons/billing/detail.proto\x1a!api/commons/billing/invoice.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"2\n\x11GetBillingPlanReq\x12\x19\n\x06org_id\x18\x01 \x01(\tB\x02\x18\x01R\x05orgId:\x02\x18\x01\"Y\n\x11GetBillingPlanRes\x12@\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32\x19.api.commons.billing.PlanB\x02\x18\x01R\x0b\x62illingPlan:\x02\x18\x01\"\x7f\n\x14UpdateBillingPlanReq\x12H\n\x0f\x62illing_details\x18\x01 \x03(\x0b\x32\x1b.api.commons.billing.DetailB\x02\x18\x01R\x0e\x62illingDetails\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId:\x02\x18\x01\"\\\n\x14UpdateBillingPlanRes\x12@\n\x0c\x62illing_plan\x18\x01 \x01(\x0b\x32\x19.api.commons.billing.PlanB\x02\x18\x01R\x0b\x62illingPlan:\x02\x18\x01\"\x81\x02\n\rGetInvoiceReq\x12\x41\n\x0cinvoice_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0binvoiceDate\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId\x12?\n\x06\x66ormat\x18\x03 \x01(\x0e\x32#.api.v1alpha1.billing.InvoiceFormatB\x02\x18\x01R\x06\x66ormat\x12M\n\x0einvoice_format\x18\x04 \x01(\x0e\x32\".api.commons.billing.InvoiceFormatB\x02\x18\x01R\rinvoiceFormat:\x02\x18\x01\"\xe2\x02\n\rGetInvoiceRes\x12:\n\x07invoice\x18\x01 \x01(\x0b\x32\x1c.api.commons.billing.InvoiceB\x02\x18\x01R\x07invoice\x12\x38\n\x05proto\x18\x02 \x01(\x0b\x32\x1c.api.commons.billing.InvoiceB\x02\x18\x01H\x00R\x05proto\x12\x1d\n\x07\x63sv_url\x18\x03 \x01(\tB\x02\x18\x01H\x00R\x06\x63svUrl\x12G\n\rinvoice_proto\x18\x64 \x01(\x0b\x32\x1c.api.commons.billing.InvoiceB\x02\x18\x01H\x01R\x0cinvoiceProto\x12,\n\x0finvoice_csv_url\x18\x65 \x01(\tB\x02\x18\x01H\x01R\rinvoiceCsvUrl\x12\'\n\rbilling_cycle\x18\x04 \x01(\tB\x02\x18\x01R\x0c\x62illingCycle:\x02\x18\x01\x42\x08\n\x06\x66ormatB\x0e\n\x0cinvoice_data\"\x8d\x02\n\x19\x45xportGeneratedInvoiceReq\x12\x41\n\x0cinvoice_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0binvoiceDate\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId\x12?\n\x06\x66ormat\x18\x03 \x01(\x0e\x32#.api.v1alpha1.billing.InvoiceFormatB\x02\x18\x01R\x06\x66ormat\x12M\n\x0einvoice_format\x18\x04 \x01(\x0e\x32\".api.commons.billing.InvoiceFormatB\x02\x18\x01R\rinvoiceFormat:\x02\x18\x01\"\xb2\x02\n\x19\x45xportGeneratedInvoiceRes\x12\x38\n\x05proto\x18\x01 \x01(\x0b\x32\x1c.api.commons.billing.InvoiceB\x02\x18\x01H\x00R\x05proto\x12\x1d\n\x07\x63sv_url\x18\x02 \x01(\tB\x02\x18\x01H\x00R\x06\x63svUrl\x12G\n\rinvoice_proto\x18\x64 \x01(\x0b\x32\x1c.api.commons.billing.InvoiceB\x02\x18\x01H\x01R\x0cinvoiceProto\x12,\n\x0finvoice_csv_url\x18\x65 \x01(\tB\x02\x18\x01H\x01R\rinvoiceCsvUrl\x12\'\n\rbilling_cycle\x18\x04 \x01(\tB\x02\x18\x01R\x0c\x62illingCycle:\x02\x18\x01\x42\x08\n\x06\x66ormatB\x0e\n\x0cinvoice_data*e\n\rInvoiceFormat\x12\x1e\n\x1aINVOICE_FORMAT_UNSPECIFIED\x10\x00\x12\x18\n\x14INVOICE_FORMAT_PROTO\x10\x01\x12\x16\n\x12INVOICE_FORMAT_CSV\x10\x02\x1a\x02\x18\x01\x42\x9b\x01\n\x18\x63om.api.v1alpha1.billingB\rEntitiesProtoP\x01\xa2\x02\x03\x41VB\xaa\x02\x14\x41pi.V1alpha1.Billing\xca\x02\x14\x41pi\\V1alpha1\\Billing\xe2\x02 Api\\V1alpha1\\Billing\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.billing.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.billingB\rEntitiesProtoP\001\242\002\003AVB\252\002\024Api.V1alpha1.Billing\312\002\024Api\\V1alpha1\\Billing\342\002 Api\\V1alpha1\\Billing\\GPBMetadata\352\002\026Api::V1alpha1::Billing'
  _globals['_INVOICEFORMAT']._loaded_options = None
  _globals['_INVOICEFORMAT']._serialized_options = b'\030\001'
  _globals['_GETBILLINGPLANREQ'].fields_by_name['org_id']._loaded_options = None
  _globals['_GETBILLINGPLANREQ'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_GETBILLINGPLANREQ']._loaded_options = None
  _globals['_GETBILLINGPLANREQ']._serialized_options = b'\030\001'
  _globals['_GETBILLINGPLANRES'].fields_by_name['billing_plan']._loaded_options = None
  _globals['_GETBILLINGPLANRES'].fields_by_name['billing_plan']._serialized_options = b'\030\001'
  _globals['_GETBILLINGPLANRES']._loaded_options = None
  _globals['_GETBILLINGPLANRES']._serialized_options = b'\030\001'
  _globals['_UPDATEBILLINGPLANREQ'].fields_by_name['billing_details']._loaded_options = None
  _globals['_UPDATEBILLINGPLANREQ'].fields_by_name['billing_details']._serialized_options = b'\030\001'
  _globals['_UPDATEBILLINGPLANREQ'].fields_by_name['org_id']._loaded_options = None
  _globals['_UPDATEBILLINGPLANREQ'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_UPDATEBILLINGPLANREQ']._loaded_options = None
  _globals['_UPDATEBILLINGPLANREQ']._serialized_options = b'\030\001'
  _globals['_UPDATEBILLINGPLANRES'].fields_by_name['billing_plan']._loaded_options = None
  _globals['_UPDATEBILLINGPLANRES'].fields_by_name['billing_plan']._serialized_options = b'\030\001'
  _globals['_UPDATEBILLINGPLANRES']._loaded_options = None
  _globals['_UPDATEBILLINGPLANRES']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQ'].fields_by_name['invoice_date']._loaded_options = None
  _globals['_GETINVOICEREQ'].fields_by_name['invoice_date']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQ'].fields_by_name['org_id']._loaded_options = None
  _globals['_GETINVOICEREQ'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQ'].fields_by_name['format']._loaded_options = None
  _globals['_GETINVOICEREQ'].fields_by_name['format']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQ'].fields_by_name['invoice_format']._loaded_options = None
  _globals['_GETINVOICEREQ'].fields_by_name['invoice_format']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQ']._loaded_options = None
  _globals['_GETINVOICEREQ']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['invoice']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['proto']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['proto']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['csv_url']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['csv_url']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['invoice_proto']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['invoice_proto']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['invoice_csv_url']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['invoice_csv_url']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES'].fields_by_name['billing_cycle']._loaded_options = None
  _globals['_GETINVOICERES'].fields_by_name['billing_cycle']._serialized_options = b'\030\001'
  _globals['_GETINVOICERES']._loaded_options = None
  _globals['_GETINVOICERES']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['invoice_date']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['invoice_date']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['org_id']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['format']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['format']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['invoice_format']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICEREQ'].fields_by_name['invoice_format']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICEREQ']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICEREQ']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['proto']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['proto']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['csv_url']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['csv_url']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['invoice_proto']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['invoice_proto']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['invoice_csv_url']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['invoice_csv_url']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['billing_cycle']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES'].fields_by_name['billing_cycle']._serialized_options = b'\030\001'
  _globals['_EXPORTGENERATEDINVOICERES']._loaded_options = None
  _globals['_EXPORTGENERATEDINVOICERES']._serialized_options = b'\030\001'
  _globals['_INVOICEFORMAT']._serialized_start=1782
  _globals['_INVOICEFORMAT']._serialized_end=1883
  _globals['_GETBILLINGPLANREQ']._serialized_start=218
  _globals['_GETBILLINGPLANREQ']._serialized_end=268
  _globals['_GETBILLINGPLANRES']._serialized_start=270
  _globals['_GETBILLINGPLANRES']._serialized_end=359
  _globals['_UPDATEBILLINGPLANREQ']._serialized_start=361
  _globals['_UPDATEBILLINGPLANREQ']._serialized_end=488
  _globals['_UPDATEBILLINGPLANRES']._serialized_start=490
  _globals['_UPDATEBILLINGPLANRES']._serialized_end=582
  _globals['_GETINVOICEREQ']._serialized_start=585
  _globals['_GETINVOICEREQ']._serialized_end=842
  _globals['_GETINVOICERES']._serialized_start=845
  _globals['_GETINVOICERES']._serialized_end=1199
  _globals['_EXPORTGENERATEDINVOICEREQ']._serialized_start=1202
  _globals['_EXPORTGENERATEDINVOICEREQ']._serialized_end=1471
  _globals['_EXPORTGENERATEDINVOICERES']._serialized_start=1474
  _globals['_EXPORTGENERATEDINVOICERES']._serialized_end=1780
# @@protoc_insertion_point(module_scope)
