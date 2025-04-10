# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/users/auth_token.proto
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
    'api/v1alpha1/org/users/auth_token.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import auth_token_pb2 as api_dot_commons_dot_org_dot_auth__token__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/v1alpha1/org/users/auth_token.proto\x12\x16\x61pi.v1alpha1.org.users\x1a api/commons/org/auth_token.proto\"\x18\n\x16\x43reateAuthTokenRequest\"T\n\x17\x43reateAuthTokenResponse\x12\x39\n\nauth_token\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.AuthTokenR\tauthToken\"9\n\x1e\x43reateAuthTokenByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\\\n\x1f\x43reateAuthTokenByUserIdResponse\x12\x39\n\nauth_token\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.AuthTokenR\tauthToken\"\x17\n\x15ListAuthTokensRequest\"U\n\x16ListAuthTokensResponse\x12;\n\x0b\x61uth_tokens\x18\x01 \x03(\x0b\x32\x1a.api.commons.org.AuthTokenR\nauthTokens\"8\n\x1dListAuthTokensByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"]\n\x1eListAuthTokensByUserIdResponse\x12;\n\x0b\x61uth_tokens\x18\x01 \x03(\x0b\x32\x1a.api.commons.org.AuthTokenR\nauthTokens\"5\n\x1dSetAuthTokenExpirationRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\" \n\x1eSetAuthTokenExpirationResponse\"V\n%SetAuthTokenExpirationByUserIdRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"(\n&SetAuthTokenExpirationByUserIdResponse\".\n\x16\x44\x65leteAuthTokenRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"\x19\n\x17\x44\x65leteAuthTokenResponse\"O\n\x1e\x44\x65leteAuthTokenByUserIdRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"!\n\x1f\x44\x65leteAuthTokenByUserIdResponseB\xa8\x01\n\x1a\x63om.api.v1alpha1.org.usersB\x0e\x41uthTokenProtoP\x01\xa2\x02\x04\x41VOU\xaa\x02\x16\x41pi.V1alpha1.Org.Users\xca\x02\x16\x41pi\\V1alpha1\\Org\\Users\xe2\x02\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Org::Usersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.users.auth_token_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.api.v1alpha1.org.usersB\016AuthTokenProtoP\001\242\002\004AVOU\252\002\026Api.V1alpha1.Org.Users\312\002\026Api\\V1alpha1\\Org\\Users\342\002\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\352\002\031Api::V1alpha1::Org::Users'
  _globals['_CREATEAUTHTOKENREQUEST']._serialized_start=101
  _globals['_CREATEAUTHTOKENREQUEST']._serialized_end=125
  _globals['_CREATEAUTHTOKENRESPONSE']._serialized_start=127
  _globals['_CREATEAUTHTOKENRESPONSE']._serialized_end=211
  _globals['_CREATEAUTHTOKENBYUSERIDREQUEST']._serialized_start=213
  _globals['_CREATEAUTHTOKENBYUSERIDREQUEST']._serialized_end=270
  _globals['_CREATEAUTHTOKENBYUSERIDRESPONSE']._serialized_start=272
  _globals['_CREATEAUTHTOKENBYUSERIDRESPONSE']._serialized_end=364
  _globals['_LISTAUTHTOKENSREQUEST']._serialized_start=366
  _globals['_LISTAUTHTOKENSREQUEST']._serialized_end=389
  _globals['_LISTAUTHTOKENSRESPONSE']._serialized_start=391
  _globals['_LISTAUTHTOKENSRESPONSE']._serialized_end=476
  _globals['_LISTAUTHTOKENSBYUSERIDREQUEST']._serialized_start=478
  _globals['_LISTAUTHTOKENSBYUSERIDREQUEST']._serialized_end=534
  _globals['_LISTAUTHTOKENSBYUSERIDRESPONSE']._serialized_start=536
  _globals['_LISTAUTHTOKENSBYUSERIDRESPONSE']._serialized_end=629
  _globals['_SETAUTHTOKENEXPIRATIONREQUEST']._serialized_start=631
  _globals['_SETAUTHTOKENEXPIRATIONREQUEST']._serialized_end=684
  _globals['_SETAUTHTOKENEXPIRATIONRESPONSE']._serialized_start=686
  _globals['_SETAUTHTOKENEXPIRATIONRESPONSE']._serialized_end=718
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDREQUEST']._serialized_start=720
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDREQUEST']._serialized_end=806
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDRESPONSE']._serialized_start=808
  _globals['_SETAUTHTOKENEXPIRATIONBYUSERIDRESPONSE']._serialized_end=848
  _globals['_DELETEAUTHTOKENREQUEST']._serialized_start=850
  _globals['_DELETEAUTHTOKENREQUEST']._serialized_end=896
  _globals['_DELETEAUTHTOKENRESPONSE']._serialized_start=898
  _globals['_DELETEAUTHTOKENRESPONSE']._serialized_end=923
  _globals['_DELETEAUTHTOKENBYUSERIDREQUEST']._serialized_start=925
  _globals['_DELETEAUTHTOKENBYUSERIDREQUEST']._serialized_end=1004
  _globals['_DELETEAUTHTOKENBYUSERIDRESPONSE']._serialized_start=1006
  _globals['_DELETEAUTHTOKENBYUSERIDRESPONSE']._serialized_end=1039
# @@protoc_insertion_point(module_scope)
