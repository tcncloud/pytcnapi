# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha4/modules.proto
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
    'services/billing/entities/v1alpha4/modules.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import decimal_pb2 as google_dot_type_dot_decimal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0services/billing/entities/v1alpha4/modules.proto\x12\"services.billing.entities.v1alpha4\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19google/type/decimal.proto\"U\n\x0b\x42\x61sicConfig\x12(\n\x04rate\x18\x01 \x01(\x0b\x32\x14.google.type.DecimalR\x04rate\x12\x1c\n\tprecision\x18\x02 \x01(\x05R\tprecision\"\xea\x01\n\x0f\x42\x61sicUnitConfig\x12\x1b\n\tunit_size\x18\x01 \x01(\x03R\x08unitSize\x12\x38\n\tmin_units\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x08minUnits\x12\x38\n\tmax_units\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x08maxUnits\x12(\n\x04rate\x18\x04 \x01(\x0b\x32\x14.google.type.DecimalR\x04rate\x12\x1c\n\tprecision\x18\x05 \x01(\x05R\tprecisionB\xe1\x01\n&com.services.billing.entities.v1alpha4B\x0cModulesProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha4\xca\x02\"Services\\Billing\\Entities\\V1alpha4\xe2\x02.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha4.modules_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha4B\014ModulesProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha4\312\002\"Services\\Billing\\Entities\\V1alpha4\342\002.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha4'
  _globals['_BASICCONFIG']._serialized_start=147
  _globals['_BASICCONFIG']._serialized_end=232
  _globals['_BASICUNITCONFIG']._serialized_start=235
  _globals['_BASICUNITCONFIG']._serialized_end=469
# @@protoc_insertion_point(module_scope)
