# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha3/invoice.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'services/billing/entities/v1alpha3/invoice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import decimal_pb2 as google_dot_type_dot_decimal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0services/billing/entities/v1alpha3/invoice.proto\x12\"services.billing.entities.v1alpha3\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19google/type/decimal.proto\"\xf0\x01\n\x07Invoice\x12#\n\rbilling_cycle\x18\x01 \x01(\tR\x0c\x62illingCycle\x12;\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x42\n\x04rows\x18\x03 \x03(\x0b\x32..services.billing.entities.v1alpha3.InvoiceRowR\x04rows\x12?\n\x0c\x64ownload_url\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0b\x64ownloadUrl\"\xa0\x02\n\nInvoiceRow\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x1d\n\nproduct_id\x18\x02 \x01(\tR\tproductId\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12.\n\x04\x64\x61te\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x64\x61te\x12K\n\x07\x63olumns\x18\x05 \x03(\x0b\x32\x31.services.billing.entities.v1alpha3.InvoiceColumnR\x07\x63olumns\x12\x37\n\x0crated_amount\x18\x06 \x01(\x0b\x32\x14.google.type.DecimalR\x0bratedAmount\"9\n\rInvoiceColumn\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05valueB\xe1\x01\n&com.services.billing.entities.v1alpha3B\x0cInvoiceProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha3\xca\x02\"Services\\Billing\\Entities\\V1alpha3\xe2\x02.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha3.invoice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha3B\014InvoiceProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha3\312\002\"Services\\Billing\\Entities\\V1alpha3\342\002.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha3'
  _globals['_INVOICE']._serialized_start=181
  _globals['_INVOICE']._serialized_end=421
  _globals['_INVOICEROW']._serialized_start=424
  _globals['_INVOICEROW']._serialized_end=712
  _globals['_INVOICECOLUMN']._serialized_start=714
  _globals['_INVOICECOLUMN']._serialized_end=771
# @@protoc_insertion_point(module_scope)
