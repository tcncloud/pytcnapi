# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/authconnection/service.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'api/v1alpha1/org/authconnection/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.authconnection import entities_pb2 as api_dot_v1alpha1_dot_org_dot_authconnection_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/org/authconnection/service.proto\x12\x1f\x61pi.v1alpha1.org.authconnection\x1a\x17\x61nnotations/authz.proto\x1a.api/v1alpha1/org/authconnection/entities.proto\x1a\x1cgoogle/api/annotations.proto2\x82\x0c\n\x15\x41uthConnectionService\x12\xcd\x01\n\x14\x43reateAuthConnection\x12<.api.v1alpha1.org.authconnection.CreateAuthConnectionRequest\x1a=.api.v1alpha1.org.authconnection.CreateAuthConnectionResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/connection/create:\x01*\x12\xce\x01\n\x15ListAuthConnectionIds\x12=.api.v1alpha1.org.authconnection.ListAuthConnectionIdsRequest\x1a>.api.v1alpha1.org.authconnection.ListAuthConnectionIdsResponse\"6\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/org/connection/list:\x01*\x12\xe1\x01\n\x19GetAuthConnectionSettings\x12\x41.api.v1alpha1.org.authconnection.GetAuthConnectionSettingsRequest\x1a\x42.api.v1alpha1.org.authconnection.GetAuthConnectionSettingsResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/org/connection/getsettings:\x01*\x12\xc1\x01\n\x11GetAuthConnection\x12\x39.api.v1alpha1.org.authconnection.GetAuthConnectionRequest\x1a:.api.v1alpha1.org.authconnection.GetAuthConnectionResponse\"5\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02%\" /api/v1alpha1/org/connection/get:\x01*\x12\xcd\x01\n\x14\x44\x65leteAuthConnection\x12<.api.v1alpha1.org.authconnection.DeleteAuthConnectionRequest\x1a=.api.v1alpha1.org.authconnection.DeleteAuthConnectionResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/connection/delete:\x01*\x12\xe6\x01\n\x1aUpdateAuthConnectionSecret\x12\x42.api.v1alpha1.org.authconnection.UpdateAuthConnectionSecretRequest\x1a\x43.api.v1alpha1.org.authconnection.UpdateAuthConnectionSecretResponse\"?\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/org/connection/update/secret:\x01*\x12\xe6\x01\n\x1aUpdateAuthConnectionGroups\x12\x42.api.v1alpha1.org.authconnection.UpdateAuthConnectionGroupsRequest\x1a\x43.api.v1alpha1.org.authconnection.UpdateAuthConnectionGroupsResponse\"?\xba\xb8\x91\x02\x05\n\x03\x08\x84\x02\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/org/connection/update/groups:\x01*B\xd3\x01\n#com.api.v1alpha1.org.authconnectionB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOA\xaa\x02\x1f\x41pi.V1alpha1.Org.Authconnection\xca\x02\x1f\x41pi\\V1alpha1\\Org\\Authconnection\xe2\x02+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\xea\x02\"Api::V1alpha1::Org::Authconnectionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.authconnection.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.api.v1alpha1.org.authconnectionB\014ServiceProtoP\001\242\002\004AVOA\252\002\037Api.V1alpha1.Org.Authconnection\312\002\037Api\\V1alpha1\\Org\\Authconnection\342\002+Api\\V1alpha1\\Org\\Authconnection\\GPBMetadata\352\002\"Api::V1alpha1::Org::Authconnection'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['CreateAuthConnection']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['CreateAuthConnection']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002(\"#/api/v1alpha1/org/connection/create:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['ListAuthConnectionIds']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['ListAuthConnectionIds']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002&\"!/api/v1alpha1/org/connection/list:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['GetAuthConnectionSettings']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['GetAuthConnectionSettings']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002-\"(/api/v1alpha1/org/connection/getsettings:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['GetAuthConnection']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['GetAuthConnection']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002%\" /api/v1alpha1/org/connection/get:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['DeleteAuthConnection']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['DeleteAuthConnection']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002(\"#/api/v1alpha1/org/connection/delete:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['UpdateAuthConnectionSecret']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['UpdateAuthConnectionSecret']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002/\"*/api/v1alpha1/org/connection/update/secret:\001*'
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['UpdateAuthConnectionGroups']._loaded_options = None
  _globals['_AUTHCONNECTIONSERVICE'].methods_by_name['UpdateAuthConnectionGroups']._serialized_options = b'\272\270\221\002\005\n\003\010\204\002\202\323\344\223\002/\"*/api/v1alpha1/org/connection/update/groups:\001*'
  _globals['_AUTHCONNECTIONSERVICE']._serialized_start=186
  _globals['_AUTHCONNECTIONSERVICE']._serialized_end=1724
# @@protoc_insertion_point(module_scope)
