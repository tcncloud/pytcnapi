# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/delivery.proto
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
    'api/commons/delivery.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/commons/delivery.proto\x12\x0b\x61pi.commons\"\x0c\n\nEncryption*\xbe\x01\n\x0eTransferStatus\x12\x1b\n\x17TRANSFER_STATUS_WAITING\x10\x00\x12\x1b\n\x17TRANSFER_STATUS_RUNNING\x10\x01\x12 \n\x1cTRANSFER_STATUS_DONE_SUCCESS\x10\x02\x12(\n$TRANSFER_STATUS_DONE_PARTIAL_FAILURE\x10\x03\x12&\n\"TRANSFER_STATUS_DONE_TOTAL_FAILURE\x10\x04\x42m\n\x0f\x63om.api.commonsB\rDeliveryProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.delivery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\rDeliveryProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_TRANSFERSTATUS']._serialized_start=58
  _globals['_TRANSFERSTATUS']._serialized_end=248
  _globals['_ENCRYPTION']._serialized_start=43
  _globals['_ENCRYPTION']._serialized_end=55
# @@protoc_insertion_point(module_scope)
