# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/billing/modules/modules.proto
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
    'api/commons/billing/modules/modules.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/commons/billing/modules/modules.proto\x12\x1b\x61pi.commons.billing.modules\x1a\x1egoogle/protobuf/wrappers.proto\")\n\x0b\x42\x61sicConfig\x12\x16\n\x04rate\x18\x01 \x01(\x01\x42\x02\x18\x01R\x04rate:\x02\x18\x01\"\xd7\x01\n\x11\x42\x61sicAmountConfig\x12\x1a\n\x06\x61mount\x18\x01 \x01(\x03\x42\x02\x18\x01R\x06\x61mount\x12\x16\n\x04rate\x18\x02 \x01(\x01\x42\x02\x18\x01R\x04rate\x12\x44\n\rmin_increment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x02\x18\x01R\x0cminIncrement\x12\x44\n\rmax_increment\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x02\x18\x01R\x0cmaxIncrement:\x02\x18\x01\x42\xbf\x01\n\x1f\x63om.api.commons.billing.modulesB\x0cModulesProtoP\x01\xa2\x02\x04\x41\x43\x42M\xaa\x02\x1b\x41pi.Commons.Billing.Modules\xca\x02\x1b\x41pi\\Commons\\Billing\\Modules\xe2\x02\'Api\\Commons\\Billing\\Modules\\GPBMetadata\xea\x02\x1e\x41pi::Commons::Billing::Modulesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.billing.modules.modules_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.api.commons.billing.modulesB\014ModulesProtoP\001\242\002\004ACBM\252\002\033Api.Commons.Billing.Modules\312\002\033Api\\Commons\\Billing\\Modules\342\002\'Api\\Commons\\Billing\\Modules\\GPBMetadata\352\002\036Api::Commons::Billing::Modules'
  _globals['_BASICCONFIG'].fields_by_name['rate']._loaded_options = None
  _globals['_BASICCONFIG'].fields_by_name['rate']._serialized_options = b'\030\001'
  _globals['_BASICCONFIG']._loaded_options = None
  _globals['_BASICCONFIG']._serialized_options = b'\030\001'
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['amount']._loaded_options = None
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['amount']._serialized_options = b'\030\001'
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['rate']._loaded_options = None
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['rate']._serialized_options = b'\030\001'
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['min_increment']._loaded_options = None
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['min_increment']._serialized_options = b'\030\001'
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['max_increment']._loaded_options = None
  _globals['_BASICAMOUNTCONFIG'].fields_by_name['max_increment']._serialized_options = b'\030\001'
  _globals['_BASICAMOUNTCONFIG']._loaded_options = None
  _globals['_BASICAMOUNTCONFIG']._serialized_options = b'\030\001'
  _globals['_BASICCONFIG']._serialized_start=106
  _globals['_BASICCONFIG']._serialized_end=147
  _globals['_BASICAMOUNTCONFIG']._serialized_start=150
  _globals['_BASICAMOUNTCONFIG']._serialized_end=365
# @@protoc_insertion_point(module_scope)
