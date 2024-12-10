# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha1/invoices.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'services/billing/v1alpha1/invoices.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha1 import invoice_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_invoice__pb2
from services.billing.v1alpha1 import core_pb2 as services_dot_billing_dot_v1alpha1_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(services/billing/v1alpha1/invoices.proto\x12\x19services.billing.v1alpha1\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x30services/billing/entities/v1alpha1/invoice.proto\x1a$services/billing/v1alpha1/core.proto\"\x88\x01\n\x14\x43reateInvoiceRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId\x12I\n\x07invoice\x18\x02 \x01(\x0b\x32+.services.billing.entities.v1alpha1.InvoiceB\x02\x18\x01R\x07invoice:\x02\x18\x01\">\n\x15\x43reateInvoiceResponse\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId:\x02\x18\x01\"=\n\x14\x44\x65leteInvoiceRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId:\x02\x18\x01\"\x1b\n\x15\x44\x65leteInvoiceResponse:\x02\x18\x01\"\xba\x01\n\x14\x45xportInvoiceRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId\x12@\n\x06\x66ormat\x18\x02 \x01(\x0e\x32(.services.billing.v1alpha1.InvoiceFormatR\x06\x66ormat\x12=\n\x0cinvoice_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0binvoiceDate\"^\n\x15\x45xportInvoiceResponse\x12\x45\n\x07invoice\x18\x01 \x01(\x0b\x32+.services.billing.entities.v1alpha1.InvoiceR\x07invoice\":\n\x11GetInvoiceRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId:\x02\x18\x01\"c\n\x12GetInvoiceResponse\x12I\n\x07invoice\x18\x01 \x01(\x0b\x32+.services.billing.entities.v1alpha1.InvoiceB\x02\x18\x01R\x07invoice:\x02\x18\x01\"\x82\x02\n\x13ListInvoicesRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\x02\x18\x01R\x06\x66ilter\x12\x36\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x02\x18\x01R\x06\x66ields\x12\x37\n\x04sort\x18\x04 \x03(\x0b\x32\x1f.services.billing.v1alpha1.SortB\x02\x18\x01R\x04sort\x12\x37\n\x04page\x18\x05 \x01(\x0b\x32\x1f.services.billing.v1alpha1.PageB\x02\x18\x01R\x04page:\x02\x18\x01\"\x81\x01\n\x14ListInvoicesResponse\x12K\n\x08invoices\x18\x01 \x03(\x0b\x32+.services.billing.entities.v1alpha1.InvoiceB\x02\x18\x01R\x08invoices\x12\x18\n\x05token\x18\x02 \x01(\tB\x02\x18\x01R\x05token:\x02\x18\x01\"\xcd\x01\n\x14UpdateInvoiceRequest\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId\x12I\n\x07invoice\x18\x02 \x01(\x0b\x32+.services.billing.entities.v1alpha1.InvoiceB\x02\x18\x01R\x07invoice\x12\x43\n\rupdate_fields\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x02\x18\x01R\x0cupdateFields:\x02\x18\x01\"\x1b\n\x15UpdateInvoiceResponse:\x02\x18\x01*G\n\rInvoiceFormat\x12\x1e\n\x1aINVOICE_FORMAT_UNSPECIFIED\x10\x00\x12\x16\n\x12INVOICE_FORMAT_CSV\x10\x01\x42\xb4\x01\n\x1d\x63om.services.billing.v1alpha1B\rInvoicesProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha1\xca\x02\x19Services\\Billing\\V1alpha1\xe2\x02%Services\\Billing\\V1alpha1\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha1.invoices_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha1B\rInvoicesProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha1\312\002\031Services\\Billing\\V1alpha1\342\002%Services\\Billing\\V1alpha1\\GPBMetadata\352\002\033Services::Billing::V1alpha1'
  _globals['_CREATEINVOICEREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_CREATEINVOICEREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_CREATEINVOICEREQUEST'].fields_by_name['invoice']._loaded_options = None
  _globals['_CREATEINVOICEREQUEST'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_CREATEINVOICEREQUEST']._loaded_options = None
  _globals['_CREATEINVOICEREQUEST']._serialized_options = b'\030\001'
  _globals['_CREATEINVOICERESPONSE'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_CREATEINVOICERESPONSE'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_CREATEINVOICERESPONSE']._loaded_options = None
  _globals['_CREATEINVOICERESPONSE']._serialized_options = b'\030\001'
  _globals['_DELETEINVOICEREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_DELETEINVOICEREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_DELETEINVOICEREQUEST']._loaded_options = None
  _globals['_DELETEINVOICEREQUEST']._serialized_options = b'\030\001'
  _globals['_DELETEINVOICERESPONSE']._loaded_options = None
  _globals['_DELETEINVOICERESPONSE']._serialized_options = b'\030\001'
  _globals['_EXPORTINVOICEREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_EXPORTINVOICEREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_GETINVOICEREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_GETINVOICEREQUEST']._loaded_options = None
  _globals['_GETINVOICEREQUEST']._serialized_options = b'\030\001'
  _globals['_GETINVOICERESPONSE'].fields_by_name['invoice']._loaded_options = None
  _globals['_GETINVOICERESPONSE'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_GETINVOICERESPONSE']._loaded_options = None
  _globals['_GETINVOICERESPONSE']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_LISTINVOICESREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTINVOICESREQUEST'].fields_by_name['filter']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST'].fields_by_name['fields']._loaded_options = None
  _globals['_LISTINVOICESREQUEST'].fields_by_name['fields']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST'].fields_by_name['sort']._loaded_options = None
  _globals['_LISTINVOICESREQUEST'].fields_by_name['sort']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_LISTINVOICESREQUEST'].fields_by_name['page']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESREQUEST']._loaded_options = None
  _globals['_LISTINVOICESREQUEST']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESRESPONSE'].fields_by_name['invoices']._loaded_options = None
  _globals['_LISTINVOICESRESPONSE'].fields_by_name['invoices']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESRESPONSE'].fields_by_name['token']._loaded_options = None
  _globals['_LISTINVOICESRESPONSE'].fields_by_name['token']._serialized_options = b'\030\001'
  _globals['_LISTINVOICESRESPONSE']._loaded_options = None
  _globals['_LISTINVOICESRESPONSE']._serialized_options = b'\030\001'
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['invoice']._loaded_options = None
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['update_fields']._loaded_options = None
  _globals['_UPDATEINVOICEREQUEST'].fields_by_name['update_fields']._serialized_options = b'\030\001'
  _globals['_UPDATEINVOICEREQUEST']._loaded_options = None
  _globals['_UPDATEINVOICEREQUEST']._serialized_options = b'\030\001'
  _globals['_UPDATEINVOICERESPONSE']._loaded_options = None
  _globals['_UPDATEINVOICERESPONSE']._serialized_options = b'\030\001'
  _globals['_INVOICEFORMAT']._serialized_start=1597
  _globals['_INVOICEFORMAT']._serialized_end=1668
  _globals['_CREATEINVOICEREQUEST']._serialized_start=227
  _globals['_CREATEINVOICEREQUEST']._serialized_end=363
  _globals['_CREATEINVOICERESPONSE']._serialized_start=365
  _globals['_CREATEINVOICERESPONSE']._serialized_end=427
  _globals['_DELETEINVOICEREQUEST']._serialized_start=429
  _globals['_DELETEINVOICEREQUEST']._serialized_end=490
  _globals['_DELETEINVOICERESPONSE']._serialized_start=492
  _globals['_DELETEINVOICERESPONSE']._serialized_end=519
  _globals['_EXPORTINVOICEREQUEST']._serialized_start=522
  _globals['_EXPORTINVOICEREQUEST']._serialized_end=708
  _globals['_EXPORTINVOICERESPONSE']._serialized_start=710
  _globals['_EXPORTINVOICERESPONSE']._serialized_end=804
  _globals['_GETINVOICEREQUEST']._serialized_start=806
  _globals['_GETINVOICEREQUEST']._serialized_end=864
  _globals['_GETINVOICERESPONSE']._serialized_start=866
  _globals['_GETINVOICERESPONSE']._serialized_end=965
  _globals['_LISTINVOICESREQUEST']._serialized_start=968
  _globals['_LISTINVOICESREQUEST']._serialized_end=1226
  _globals['_LISTINVOICESRESPONSE']._serialized_start=1229
  _globals['_LISTINVOICESRESPONSE']._serialized_end=1358
  _globals['_UPDATEINVOICEREQUEST']._serialized_start=1361
  _globals['_UPDATEINVOICEREQUEST']._serialized_end=1566
  _globals['_UPDATEINVOICERESPONSE']._serialized_start=1568
  _globals['_UPDATEINVOICERESPONSE']._serialized_end=1595
# @@protoc_insertion_point(module_scope)
