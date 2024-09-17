# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/auth_token.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'api/v1alpha1/org/auth_token.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import auth_token_pb2 as api_dot_commons_dot_org_dot_auth__token__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/v1alpha1/org/auth_token.proto\x12\x10\x61pi.v1alpha1.org\x1a api/commons/org/auth_token.proto\"\x18\n\x16\x43reateAuthTokenRequest\"T\n\x17\x43reateAuthTokenResponse\x12\x39\n\nauth_token\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.AuthTokenR\tauthToken\"9\n\x1e\x43reateAuthTokenByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\\\n\x1f\x43reateAuthTokenByUserIdResponse\x12\x39\n\nauth_token\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.AuthTokenR\tauthToken\"\x17\n\x15ListAuthTokensRequest\"U\n\x16ListAuthTokensResponse\x12;\n\x0b\x61uth_tokens\x18\x01 \x03(\x0b\x32\x1a.api.commons.org.AuthTokenR\nauthTokens\"8\n\x1dListAuthTokensByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"]\n\x1eListAuthTokensByUserIdResponse\x12;\n\x0b\x61uth_tokens\x18\x01 \x03(\x0b\x32\x1a.api.commons.org.AuthTokenR\nauthTokens\"5\n\x1dSetAuthTokenExpirationRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\" \n\x1eSetAuthTokenExpirationResponse\"V\n%SetAuthTokenExpirationByUserIdRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"(\n&SetAuthTokenExpirationByUserIdResponse\".\n\x16\x44\x65leteAuthTokenRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"\x19\n\x17\x44\x65leteAuthTokenResponse\"O\n\x1e\x44\x65leteAuthTokenByUserIdRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"!\n\x1f\x44\x65leteAuthTokenByUserIdResponseB\x88\x01\n\x14\x63om.api.v1alpha1.orgB\x0e\x41uthTokenProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.auth_token_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\016AuthTokenProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_CREATEAUTHTOKENREQUEST']._serialized_start=89
  _globals['_CREATEAUTHTOKENREQUEST']._serialized_end=113
  _globals['_CREATEAUTHTOKENRESPONSE']._serialized_start=115
  _globals['_CREATEAUTHTOKENRESPONSE']._serialized_end=199
  _globals['_CREATEAUTHTOKENBYUSERIDREQUEST']._serialized_start=201
  _globals['_CREATEAUTHTOKENBYUSERIDREQUEST']._serialized_end=258
  _globals['_CREATEAUTHTOKENBYUSERIDRESPONSE']._serialized_start=260
  _globals['_CREATEAUTHTOKENBYUSERIDRESPONSE']._serialized_end=352
  _globals['_LISTAUTHTOKENSREQUEST']._serialized_start=354
  _globals['_LISTAUTHTOKENSREQUEST']._serialized_end=377
  _globals['_LISTAUTHTOKENSRESPONSE']._serialized_start=379
  _globals['_LISTAUTHTOKENSRESPONSE']._serialized_end=464
  _globals['_LISTAUTHTOKENSBYUSERIDREQUEST']._serialized_start=466
  _globals['_LISTAUTHTOKENSBYUSERIDREQUEST']._serialized_end=522
  _globals['_LISTAUTHTOKENSBYUSERIDRESPONSE']._serialized_start=524
  _globals['_LISTAUTHTOKENSBYUSERIDRESPONSE']._serialized_end=617
  _globals['_SETAUTHTOKENEXPIRATIONREQUEST']._serialized_start=619
  _globals['_SETAUTHTOKENEXPIRATIONREQUEST']._serialized_end=672
  _globals['_SETAUTHTOKENEXPIRATIONRESPONSE']._serialized_start=674
  _globals['_SETAUTHTOKENEXPIRATIONRESPONSE']._serialized_end=706
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDREQUEST']._serialized_start=708
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDREQUEST']._serialized_end=794
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDRESPONSE']._serialized_start=796
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDRESPONSE']._serialized_end=836
  _globals['_DELETEAUTHTOKENREQUEST']._serialized_start=838
  _globals['_DELETEAUTHTOKENREQUEST']._serialized_end=884
  _globals['_DELETEAUTHTOKENRESPONSE']._serialized_start=886
  _globals['_DELETEAUTHTOKENRESPONSE']._serialized_end=911
  _globals['_DELETEAUTHTOKENBYUSERIDREQUEST']._serialized_start=913
  _globals['_DELETEAUTHTOKENBYUSERIDREQUEST']._serialized_end=992
  _globals['_DELETEAUTHTOKENBYUSERIDRESPONSE']._serialized_start=994
  _globals['_DELETEAUTHTOKENBYUSERIDRESPONSE']._serialized_end=1027
# @@protoc_insertion_point(module_scope)
