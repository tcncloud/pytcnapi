# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/org/auth_connections.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/commons/org/auth_connections.proto\x12\x0f\x61pi.commons.org\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa5\x04\n\x16\x41uthConnectionSettings\x12\x1d\n\nissuer_url\x18\x01 \x01(\tR\tissuerUrl\x12\x1d\n\ntenant_url\x18\x02 \x01(\tR\ttenantUrl\x12\x1b\n\tclient_id\x18\x03 \x01(\tR\x08\x63lientId\x12#\n\rconnection_id\x18\x04 \x01(\tR\x0c\x63onnectionId\x12\x65\n\x11secret_expiration\x18\x05 \x01(\x0b\x32\x38.api.commons.org.AuthConnectionSettings.SecretExpirationR\x10secretExpiration\x12?\n\rdefault_group\x18\x06 \x01(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x64\x65\x66\x61ultGroup\x12?\n\rcustom_groups\x18\x07 \x03(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x63ustomGroups\x12\x15\n\x06org_id\x18\x08 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\t \x01(\tR\x04name\x12\x33\n\x04type\x18\n \x01(\x0e\x32\x1f.api.commons.org.ConnectionTypeR\x04type\x1a\x42\n\x10SecretExpiration\x12.\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x64\x61te\"\xec\x01\n\tGroupItem\x12\x1d\n\ngroup_name\x18\x01 \x01(\tR\tgroupName\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12\x33\n\x16\x61gent_profile_group_id\x18\x03 \x01(\tR\x13\x61gentProfileGroupId\x12\x33\n\x16p3_permission_group_id\x18\x04 \x01(\tR\x13p3PermissionGroupId\x12\x30\n\x14permission_group_ids\x18\x05 \x03(\tR\x12permissionGroupIds*_\n\x0e\x43onnectionType\x12\x18\n\x14\x43ONNECTION_TYPE_NONE\x10\x00\x12\x18\n\x14\x43ONNECTION_TYPE_OIDC\x10\x01\x12\x19\n\x15\x43ONNECTION_TYPE_AZURE\x10\x02\x42\x89\x01\n\x13\x63om.api.commons.orgB\x14\x41uthConnectionsProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.auth_connections_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.api.commons.orgB\024AuthConnectionsProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_CONNECTIONTYPE']._serialized_start=883
  _globals['_CONNECTIONTYPE']._serialized_end=978
  _globals['_AUTHCONNECTIONSETTINGS']._serialized_start=93
  _globals['_AUTHCONNECTIONSETTINGS']._serialized_end=642
  _globals['_AUTHCONNECTIONSETTINGS_SECRETEXPIRATION']._serialized_start=576
  _globals['_AUTHCONNECTIONSETTINGS_SECRETEXPIRATION']._serialized_end=642
  _globals['_GROUPITEM']._serialized_start=645
  _globals['_GROUPITEM']._serialized_end=881
# @@protoc_insertion_point(module_scope)
