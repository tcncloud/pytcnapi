# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/v1alpha1/core.proto
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
    'services/billing/v1alpha1/core.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$services/billing/v1alpha1/core.proto\x12\x19services.billing.v1alpha1\"2\n\x04Page\x12\x14\n\x05limit\x18\x01 \x01(\x03R\x05limit\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"X\n\x04Sort\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\tdirection\x18\x02 \x01(\x0e\x32 .services.billing.v1alpha1.OrderR\tdirection*.\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\x0e\n\nORDER_DESC\x10\x01\x42\xb0\x01\n\x1d\x63om.services.billing.v1alpha1B\tCoreProtoP\x01\xa2\x02\x03SBX\xaa\x02\x19Services.Billing.V1alpha1\xca\x02\x19Services\\Billing\\V1alpha1\xe2\x02%Services\\Billing\\V1alpha1\\GPBMetadata\xea\x02\x1bServices::Billing::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.v1alpha1.core_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.services.billing.v1alpha1B\tCoreProtoP\001\242\002\003SBX\252\002\031Services.Billing.V1alpha1\312\002\031Services\\Billing\\V1alpha1\342\002%Services\\Billing\\V1alpha1\\GPBMetadata\352\002\033Services::Billing::V1alpha1'
  _globals['_ORDER']._serialized_start=209
  _globals['_ORDER']._serialized_end=255
  _globals['_PAGE']._serialized_start=67
  _globals['_PAGE']._serialized_end=117
  _globals['_SORT']._serialized_start=119
  _globals['_SORT']._serialized_end=207
# @@protoc_insertion_point(module_scope)
