# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/omnichannel/oauth/v1alpha1/entities.proto
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
    'services/omnichannel/oauth/v1alpha1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2services/omnichannel/oauth/v1alpha1/entities.proto\x12#services.omnichannel.oauth.v1alpha1\x1a\x1d\x61pi/commons/omnichannel.proto\"\xb8\x01\n GetConnectedInboxOAuthURLRequest\x12^\n\x13\x61uthentication_type\x18\x01 \x01(\x0e\x32-.api.commons.ConnectedInboxAuthenticationTypeR\x12\x61uthenticationType\x12\x34\n\x16returning_redirect_uri\x18\x02 \x01(\tR\x14returningRedirectUri\"@\n!GetConnectedInboxOAuthURLResponse\x12\x1b\n\toauth_url\x18\x01 \x01(\tR\x08oauthUrlB\xe7\x01\n\'com.services.omnichannel.oauth.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOO\xaa\x02#Services.Omnichannel.Oauth.V1alpha1\xca\x02#Services\\Omnichannel\\Oauth\\V1alpha1\xe2\x02/Services\\Omnichannel\\Oauth\\V1alpha1\\GPBMetadata\xea\x02&Services::Omnichannel::Oauth::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.oauth.v1alpha1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.services.omnichannel.oauth.v1alpha1B\rEntitiesProtoP\001\242\002\003SOO\252\002#Services.Omnichannel.Oauth.V1alpha1\312\002#Services\\Omnichannel\\Oauth\\V1alpha1\342\002/Services\\Omnichannel\\Oauth\\V1alpha1\\GPBMetadata\352\002&Services::Omnichannel::Oauth::V1alpha1'
  _globals['_GETCONNECTEDINBOXOAUTHURLREQUEST']._serialized_start=123
  _globals['_GETCONNECTEDINBOXOAUTHURLREQUEST']._serialized_end=307
  _globals['_GETCONNECTEDINBOXOAUTHURLRESPONSE']._serialized_start=309
  _globals['_GETCONNECTEDINBOXOAUTHURLRESPONSE']._serialized_end=373
# @@protoc_insertion_point(module_scope)
