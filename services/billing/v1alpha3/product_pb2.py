# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha3/product.proto
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
    'services/billing/v1alpha3/product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from services.billing.entities.v1alpha3 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha3_dot_rates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'services/billing/v1alpha3/product.proto\x12\x19services.billing.v1alpha3\x1a.services/billing/entities/v1alpha3/rates.proto\"\x15\n\x13ListProductsRequest\"_\n\x14ListProductsResponse\x12G\n\x08products\x18\x01 \x03(\x0b\x32+.services.billing.entities.v1alpha3.ProductR\x08productsB\xb3\x01\n\x1d\x63om.services.billing.v1alpha3B\x0cProductProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha3\xca\x02\x19Services\\Billing\\V1alpha3\xe2\x02%Services\\Billing\\V1alpha3\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha3.product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha3B\014ProductProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha3\312\002\031Services\\Billing\\V1alpha3\342\002%Services\\Billing\\V1alpha3\\GPBMetadata\352\002\033Services::Billing::V1alpha3'
  _globals['_LISTPRODUCTSREQUEST']._serialized_start=118
  _globals['_LISTPRODUCTSREQUEST']._serialized_end=139
  _globals['_LISTPRODUCTSRESPONSE']._serialized_start=141
  _globals['_LISTPRODUCTSRESPONSE']._serialized_end=236
# @@protoc_insertion_point(module_scope)
