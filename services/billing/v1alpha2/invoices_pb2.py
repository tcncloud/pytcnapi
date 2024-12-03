# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha2/invoices.proto
# Protobuf Python Version: 5.29.0
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
    0,
    '',
    'services/billing/v1alpha2/invoices.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha2 import invoice_pb2 as services_dot_billing_dot_entities_dot_v1alpha2_dot_invoice__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(services/billing/v1alpha2/invoices.proto\x12\x19services.billing.v1alpha2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x30services/billing/entities/v1alpha2/invoice.proto\"\x97\x01\n\x14\x45xportInvoiceRequest\x12@\n\x06\x66ormat\x18\x01 \x01(\x0e\x32(.services.billing.v1alpha2.InvoiceFormatR\x06\x66ormat\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0binvoiceDate\"^\n\x15\x45xportInvoiceResponse\x12\x45\n\x07invoice\x18\x01 \x01(\x0b\x32+.services.billing.entities.v1alpha2.InvoiceR\x07invoice*G\n\rInvoiceFormat\x12\x1e\n\x1aINVOICE_FORMAT_UNSPECIFIED\x10\x00\x12\x16\n\x12INVOICE_FORMAT_CSV\x10\x01\x42\xb4\x01\n\x1d\x63om.services.billing.v1alpha2B\rInvoicesProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha2\xca\x02\x19Services\\Billing\\V1alpha2\xe2\x02%Services\\Billing\\V1alpha2\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha2.invoices_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha2B\rInvoicesProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha2\312\002\031Services\\Billing\\V1alpha2\342\002%Services\\Billing\\V1alpha2\\GPBMetadata\352\002\033Services::Billing::V1alpha2'
  _globals['_INVOICEFORMAT']._serialized_start=404
  _globals['_INVOICEFORMAT']._serialized_end=475
  _globals['_EXPORTINVOICEREQUEST']._serialized_start=155
  _globals['_EXPORTINVOICEREQUEST']._serialized_end=306
  _globals['_EXPORTINVOICERESPONSE']._serialized_start=308
  _globals['_EXPORTINVOICERESPONSE']._serialized_end=402
# @@protoc_insertion_point(module_scope)
