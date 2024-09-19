# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/billing/invoice.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'api/commons/billing/invoice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/commons/billing/invoice.proto\x12\x13\x61pi.commons.billing\x1a\x1fgoogle/protobuf/timestamp.proto\"\x99\x02\n\x07Invoice\x12:\n\x05items\x18\x01 \x03(\x0b\x32 .api.commons.billing.InvoiceItemB\x02\x18\x01R\x05items\x12#\n\ninvoice_id\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\tinvoiceId\x12\'\n\rbilling_cycle\x18\x03 \x01(\tB\x02\x18\x01R\x0c\x62illingCycle\x12?\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\ncreateTime\x12?\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\nupdateTime:\x02\x18\x01\"\xc4\x02\n\x0bInvoiceItem\x12,\n\x10invoice_item_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x0einvoiceItemSid\x12:\n\x07product\x18\x02 \x01(\x0e\x32\x1c.api.commons.billing.ProductB\x02\x18\x01R\x07product\x12\x1a\n\x06\x61mount\x18\x03 \x01(\x01\x42\x02\x18\x01R\x06\x61mount\x12\x41\n\x0c\x64\x61te_created\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0b\x64\x61teCreated\x12\x43\n\rdate_modified\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0c\x64\x61teModified\x12#\n\ninvoice_id\x18\x06 \x01(\x03\x42\x04\x18\x01\x30\x01R\tinvoiceId:\x02\x18\x01*\xaf\x02\n\x07Product\x12\x17\n\x13PRODUCT_UNSPECIFIED\x10\x00\x12\x11\n\rPRODUCT_OTHER\x10\x01\x12\x17\n\x13PRODUCT_AGENT_SEATS\x10\x64\x12\x18\n\x13PRODUCT_EMAILS_SENT\x10\xc8\x01\x12\x1c\n\x17PRODUCT_EMAILS_RECEIVED\x10\xc9\x01\x12\x15\n\x10PRODUCT_SMS_SENT\x10\xca\x01\x12\x19\n\x14PRODUCT_SMS_RECEIVED\x10\xcb\x01\x12\x16\n\x11PRODUCT_CHAT_SENT\x10\xcc\x01\x12\x1a\n\x15PRODUCT_CHAT_RECEIVED\x10\xcd\x01\x12\x11\n\x0cPRODUCT_OMNI\x10\xac\x02\x12\x11\n\x0cPRODUCT_VANA\x10\x90\x03\x12\x17\n\x12PRODUCT_COMPLIANCE\x10\xf4\x03\x1a\x02\x18\x01*e\n\rInvoiceFormat\x12\x1e\n\x1aINVOICE_FORMAT_UNSPECIFIED\x10\x00\x12\x18\n\x14INVOICE_FORMAT_PROTO\x10\x01\x12\x16\n\x12INVOICE_FORMAT_CSV\x10\x02\x1a\x02\x18\x01\x42\x95\x01\n\x17\x63om.api.commons.billingB\x0cInvoiceProtoP\x01\xa2\x02\x03\x41\x43\x42\xaa\x02\x13\x41pi.Commons.Billing\xca\x02\x13\x41pi\\Commons\\Billing\xe2\x02\x1f\x41pi\\Commons\\Billing\\GPBMetadata\xea\x02\x15\x41pi::Commons::Billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.billing.invoice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.api.commons.billingB\014InvoiceProtoP\001\242\002\003ACB\252\002\023Api.Commons.Billing\312\002\023Api\\Commons\\Billing\342\002\037Api\\Commons\\Billing\\GPBMetadata\352\002\025Api::Commons::Billing'
  _globals['_PRODUCT']._loaded_options = None
  _globals['_PRODUCT']._serialized_options = b'\030\001'
  _globals['_INVOICEFORMAT']._loaded_options = None
  _globals['_INVOICEFORMAT']._serialized_options = b'\030\001'
  _globals['_INVOICE'].fields_by_name['items']._loaded_options = None
  _globals['_INVOICE'].fields_by_name['items']._serialized_options = b'\030\001'
  _globals['_INVOICE'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_INVOICE'].fields_by_name['invoice_id']._serialized_options = b'\030\0010\001'
  _globals['_INVOICE'].fields_by_name['billing_cycle']._loaded_options = None
  _globals['_INVOICE'].fields_by_name['billing_cycle']._serialized_options = b'\030\001'
  _globals['_INVOICE'].fields_by_name['create_time']._loaded_options = None
  _globals['_INVOICE'].fields_by_name['create_time']._serialized_options = b'\030\001'
  _globals['_INVOICE'].fields_by_name['update_time']._loaded_options = None
  _globals['_INVOICE'].fields_by_name['update_time']._serialized_options = b'\030\001'
  _globals['_INVOICE']._loaded_options = None
  _globals['_INVOICE']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['invoice_item_sid']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['invoice_item_sid']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['product']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['product']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['amount']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['amount']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['date_created']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['date_created']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['date_modified']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['date_modified']._serialized_options = b'\030\001'
  _globals['_INVOICEITEM'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_INVOICEITEM'].fields_by_name['invoice_id']._serialized_options = b'\030\0010\001'
  _globals['_INVOICEITEM']._loaded_options = None
  _globals['_INVOICEITEM']._serialized_options = b'\030\001'
  _globals['_PRODUCT']._serialized_start=703
  _globals['_PRODUCT']._serialized_end=1006
  _globals['_INVOICEFORMAT']._serialized_start=1008
  _globals['_INVOICEFORMAT']._serialized_end=1109
  _globals['_INVOICE']._serialized_start=92
  _globals['_INVOICE']._serialized_end=373
  _globals['_INVOICEITEM']._serialized_start=376
  _globals['_INVOICEITEM']._serialized_end=700
# @@protoc_insertion_point(module_scope)
