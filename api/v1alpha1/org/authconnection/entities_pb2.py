# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/authconnection/entities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import auth_connections_pb2 as api_dot_commons_dot_org_dot_auth__connections__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.api/v1alpha1/org/authconnection/entities.proto\x12\x1f\x61pi.v1alpha1.org.authconnection\x1a&api/commons/org/auth_connections.proto\"\x87\x01\n\x1b\x43reateAuthConnectionRequest\x12\x43\n\x08settings\x18\x01 \x01(\x0b\x32\'.api.commons.org.AuthConnectionSettingsR\x08settings\x12#\n\rclient_secret\x18\x02 \x01(\tR\x0c\x63lientSecret\"\x1e\n\x1c\x43reateAuthConnectionResponse\"\"\n GetAuthConnectionSettingsRequest\"h\n!GetAuthConnectionSettingsResponse\x12\x43\n\x08settings\x18\x01 \x01(\x0b\x32\'.api.commons.org.AuthConnectionSettingsR\x08settings\"B\n\x1b\x44\x65leteAuthConnectionRequest\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\"\x1e\n\x1c\x44\x65leteAuthConnectionResponse\"m\n!UpdateAuthConnectionSecretRequest\x12#\n\rconnection_id\x18\x01 \x01(\tR\x0c\x63onnectionId\x12#\n\rclient_secret\x18\x02 \x01(\tR\x0c\x63lientSecret\"$\n\"UpdateAuthConnectionSecretResponse\"\xa5\x01\n!UpdateAuthConnectionGroupsRequest\x12?\n\rdefault_group\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x64\x65\x66\x61ultGroup\x12?\n\rcustom_groups\x18\x02 \x03(\x0b\x32\x1a.api.commons.org.GroupItemR\x0c\x63ustomGroups\"$\n\"UpdateAuthConnectionGroupsResponseB\xd4\x01\n#com.api.v1alpha1.org.authconnectionB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOA\xaa\x02\x1f\x41pi.V1alpha1.Org.Authconnection\xca\x02\x1f\x41pi\\V1alpha1\\Org\\Authconnection\xe2\x02+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\xea\x02\"Api::V1alpha1::Org::Authconnectionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.authconnection.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.api.v1alpha1.org.authconnectionB\rEntitiesProtoP\001\242\002\004AVOA\252\002\037Api.V1alpha1.Org.Authconnection\312\002\037Api\\V1alpha1\\Org\\Authconnection\342\002+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\352\002\"Api::V1alpha1::Org::Authconnection'
  _globals['_CREATEAUTHCONNECTIONREQUEST']._serialized_start=124
  _globals['_CREATEAUTHCONNECTIONREQUEST']._serialized_end=259
  _globals['_CREATEAUTHCONNECTIONRESPONSE']._serialized_start=261
  _globals['_CREATEAUTHCONNECTIONRESPONSE']._serialized_end=291
  _globals['_GETAUTHCONNECTIONSETTINGSREQUEST']._serialized_start=293
  _globals['_GETAUTHCONNECTIONSETTINGSREQUEST']._serialized_end=327
  _globals['_GETAUTHCONNECTIONSETTINGSRESPONSE']._serialized_start=329
  _globals['_GETAUTHCONNECTIONSETTINGSRESPONSE']._serialized_end=433
  _globals['_DELETEAUTHCONNECTIONREQUEST']._serialized_start=435
  _globals['_DELETEAUTHCONNECTIONREQUEST']._serialized_end=501
  _globals['_DELETEAUTHCONNECTIONRESPONSE']._serialized_start=503
  _globals['_DELETEAUTHCONNECTIONRESPONSE']._serialized_end=533
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST']._serialized_start=535
  _globals['_UPDATEAUTHCONNECTIONSECRETREQUEST']._serialized_end=644
  _globals['_UPDATEAUTHCONNECTIONSECRETRESPONSE']._serialized_start=646
  _globals['_UPDATEAUTHCONNECTIONSECRETRESPONSE']._serialized_end=682
  _globals['_UPDATEAUTHCONNECTIONGROUPSREQUEST']._serialized_start=685
  _globals['_UPDATEAUTHCONNECTIONGROUPSREQUEST']._serialized_end=850
  _globals['_UPDATEAUTHCONNECTIONGROUPSRESPONSE']._serialized_start=852
  _globals['_UPDATEAUTHCONNECTIONGROUPSRESPONSE']._serialized_end=888
# @@protoc_insertion_point(module_scope)
