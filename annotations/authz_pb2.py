# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: annotations/authz.proto
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
    'annotations/authz.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61nnotations/authz.proto\x12\x0b\x61nnotations\x1a\x1c\x61pi/commons/auth/perms.proto\x1a google/protobuf/descriptor.proto\"\x88\x01\n\x0bPermissions\x12.\n\x04sets\x18\x01 \x03(\x0b\x32\x1a.annotations.PermissionSetR\x04sets\x12\x1b\n\x03wip\x18\x02 \x01(\x08:\x05\x66\x61lseB\x02\x18\x01R\x03wip\x12,\n\x0eno_permissions\x18\x03 \x01(\x08:\x05\x66\x61lseR\rnoPermissions\"y\n\rPermissionSet\x12>\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12(\n\x05taint\x18\x02 \x01(\x0b\x32\x12.annotations.TaintR\x05taint\"-\n\x05Taint\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:P\n\x05\x61uthz\x12\x1e.google.protobuf.MethodOptions\x18\x87\x97\" \x01(\x0b\x32\x18.annotations.PermissionsR\x05\x61uthzBi\n\x0f\x63om.annotationsB\nAuthzProtoP\x01\xa2\x02\x03\x41XX\xaa\x02\x0b\x41nnotations\xca\x02\x0b\x41nnotations\xe2\x02\x17\x41nnotations\\GPBMetadata\xea\x02\x0b\x41nnotations')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'annotations.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.annotationsB\nAuthzProtoP\001\242\002\003AXX\252\002\013Annotations\312\002\013Annotations\342\002\027Annotations\\GPBMetadata\352\002\013Annotations'
  _globals['_PERMISSIONS'].fields_by_name['wip']._loaded_options = None
  _globals['_PERMISSIONS'].fields_by_name['wip']._serialized_options = b'\030\001'
  _globals['_PERMISSIONS']._serialized_start=105
  _globals['_PERMISSIONS']._serialized_end=241
  _globals['_PERMISSIONSET']._serialized_start=243
  _globals['_PERMISSIONSET']._serialized_end=364
  _globals['_TAINT']._serialized_start=366
  _globals['_TAINT']._serialized_end=411
# @@protoc_insertion_point(module_scope)
