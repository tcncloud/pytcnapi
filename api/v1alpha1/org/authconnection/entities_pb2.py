# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/authconnection/entities.proto
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
    'api/v1alpha1/org/authconnection/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import auth_connections_pb2 as api_dot_commons_dot_org_dot_auth__connections__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.api/v1alpha1/org/authconnection/entities.proto\x12\x1f\x61pi.v1alpha1.org.authconnection\x1a&api/commons/org/auth_connections.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x01\n\x1b\x43reateAuthConnectionRequest\x12\x43\n\x08settings\x18\x01 \x01(\x0b\x32\'.api.commons.org.AuthConnectionSettingsR\x08settings\x12#\n\rclient_secret\x18\x02 \x01(\tR\x0c\x63lientSecret\"C\n\x1c\x43reateAuthConnectionResponse\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\"\"\n GetAuthConnectionSettingsRequest\"h\n!GetAuthConnectionSettingsResponse\x12\x43\n\x08settings\x18\x01 \x01(\x0b\x32\'.api.commons.org.AuthConnectionSettingsR\x08settings\"?\n\x18GetAuthConnectionRequest\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\"`\n\x19GetAuthConnectionResponse\x12\x43\n\x08settings\x18\x01 \x01(\x0b\x32\'.api.commons.org.AuthConnectionSettingsR\x08settings\"B\n\x1b\x44\x65leteAuthConnectionRequest\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\"\x1e\n\x1c\x44\x65leteAuthConnectionResponse\"\xb4\x02\n!UpdateAuthConnectionSecretRequest\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\x12#\n\rclient_secret\x18\x02 \x01(\tR\x0c\x63lientSecret\x12\x80\x01\n\x11secret_expiration\x18\x03 \x01(\x0b\x32S.api.v1alpha1.org.authconnection.UpdateAuthConnectionSecretRequest.SecretExpirationR\x10secretExpiration\x1a\x42\n\x10SecretExpiration\x12.\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x64\x61te\"$\n\"UpdateAuthConnectionSecretResponse\"\xca\x01\n!UpdateAuthConnectionGroupsRequest\x12?\n\rdefault_group\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x64\x65\x66\x61ultGroup\x12?\n\rcustom_groups\x18\x02 \x03(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x63ustomGroups\x12#\n\rconnection_id\x18\x03 \x01(\tR\x0c\x63onnectionId\"$\n\"UpdateAuthConnectionGroupsResponse\"\x1e\n\x1cListAuthConnectionIdsRequest\"\xdc\x01\n\x1dListAuthConnectionIdsResponse\x12k\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32I.api.v1alpha1.org.authconnection.ListAuthConnectionIdsResponse.ConnectionR\x0b\x63onnections\x1aN\n\nConnection\x12,\n\x12\x61uth_connection_id\x18\x01 \x01(\tR\x10\x61uthConnectionId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04nameB\xd4\x01\n#com.api.v1alpha1.org.authconnectionB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOA\xaa\x02\x1f\x41pi.V1alpha1.Org.Authconnection\xca\x02\x1f\x41pi\\V1alpha1\\Org\\Authconnection\xe2\x02+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\xea\x02\"Api::V1alpha1::Org::Authconnectionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.authconnection.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.api.v1alpha1.org.authconnectionB\rEntitiesProtoP\001\242\002\004AVOA\252\002\037Api.V1alpha1.Org.Authconnection\312\002\037Api\\V1alpha1\\Org\\Authconnection\342\002+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\352\002\"Api::V1alpha1::Org::Authconnection'
  _globals['_CREATEAUTHCONNECTIONREQUEST']._serialized_start=157
  _globals['_CREATEAUTHCONNECTIONREQUEST']._serialized_end=292
  _globals['_CREATEAUTHCONNECTIONRESPONSE']._serialized_start=294
  _globals['_CREATEAUTHCONNECTIONRESPONSE']._serialized_end=361
  _globals['_GETAUTHCONNECTIONSETTINGSREQUEST']._serialized_start=363
  _globals['_GETAUTHCONNECTIONSETTINGSREQUEST']._serialized_end=397
  _globals['_GETAUTHCONNECTIONSETTINGSRESPONSE']._serialized_start=399
  _globals['_GETAUTHCONNECTIONSETTINGSRESPONSE']._serialized_end=503
  _globals['_GETAUTHCONNECTIONREQUEST']._serialized_start=505
  _globals['_GETAUTHCONNECTIONREQUEST']._serialized_end=568
  _globals['_GETAUTHCONNECTIONRESPONSE']._serialized_start=570
  _globals['_GETAUTHCONNECTIONRESPONSE']._serialized_end=666
  _globals['_DELETEAUTHCONNECTIONREQUEST']._serialized_start=668
  _globals['_DELETEAUTHCONNECTIONREQUEST']._serialized_end=734
  _globals['_DELETEAUTHCONNECTIONRESPONSE']._serialized_start=736
  _globals['_DELETEAUTHCONNECTIONRESPONSE']._serialized_end=766
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST']._serialized_start=769
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST']._serialized_end=1077
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST_SECRETEXPIRATION']._serialized_start=1011
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST_SECRETEXPIRATION']._serialized_end=1077
  _globals['_UPDATEAUTHCONNECTIONSECRETRESPONSE']._serialized_start=1079
  _globals['_UPDATEAUTHCONNECTIONSECRETRESPONSE']._serialized_end=1115
  _globals['_UPDATEAUTHCONNECTIONGROUPSREQUEST']._serialized_start=1118
  _globals['_UPDATEAUTHCONNECTIONGROUPSREQUEST']._serialized_end=1320
  _globals['_UPDATEAUTHCONNECTIONGROUPSRESPONSE']._serialized_start=1322
  _globals['_UPDATEAUTHCONNECTIONGROUPSRESPONSE']._serialized_end=1358
  _globals['_LISTAUTHCONNECTIONIDSREQUEST']._serialized_start=1360
  _globals['_LISTAUTHCONNECTIONIDSREQUEST']._serialized_end=1390
  _globals['_LISTAUTHCONNECTIONIDSRESPONSE']._serialized_start=1393
  _globals['_LISTAUTHCONNECTIONIDSRESPONSE']._serialized_end=1613
  _globals['_LISTAUTHCONNECTIONIDSRESPONSE_CONNECTION']._serialized_start=1535
  _globals['_LISTAUTHCONNECTIONIDSRESPONSE_CONNECTION']._serialized_end=1613
# @@protoc_insertion_point(module_scope)
