# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/auth/user.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/commons/auth/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pi/commons/auth/user.proto\x12\x10\x61pi.commons.auth\"\xd4\x02\n\nAuthClaims\x12\"\n\rauth0_user_id\x18\x01 \x01(\tR\x0b\x61uth0UserId\x12\x1e\n\x0borg_user_id\x18\x02 \x01(\tR\torgUserId\x12\x15\n\x06org_id\x18\x03 \x01(\tR\x05orgId\x12\x17\n\x07\x61pi_key\x18\x04 \x01(\tR\x06\x61piKey\x12\x1b\n\tregion_id\x18\x05 \x01(\tR\x08regionId\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12 \n\x0bimpersonate\x18\x07 \x01(\tR\x0bimpersonate\x12\x1e\n\nclient_sid\x18\xe8\x07 \x01(\x03R\tclientSid\x12\x1c\n\tagent_sid\x18\xe9\x07 \x01(\x03R\x08\x61gentSid\x12\x1c\n\tlogin_sid\x18\xea\x07 \x01(\x03R\x08loginSid\x12#\n\ractive_org_id\x18\xcc\x08 \x01(\tR\x0b\x61\x63tiveOrgId\"I\n\x11\x41uthenticatedUser\x12\x34\n\x06\x63laims\x18\x01 \x01(\x0b\x32\x1c.api.commons.auth.AuthClaimsR\x06\x63laimsB\x83\x01\n\x14\x63om.api.commons.authB\tUserProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x10\x41pi.Commons.Auth\xca\x02\x10\x41pi\\Commons\\Auth\xe2\x02\x1c\x41pi\\Commons\\Auth\\GPBMetadata\xea\x02\x12\x41pi::Commons::Authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.auth.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.commons.authB\tUserProtoP\001\242\002\003ACA\252\002\020Api.Commons.Auth\312\002\020Api\\Commons\\Auth\342\002\034Api\\Commons\\Auth\\GPBMetadata\352\002\022Api::Commons::Auth'
  _globals['_AUTHCLAIMS']._serialized_start=50
  _globals['_AUTHCLAIMS']._serialized_end=390
  _globals['_AUTHENTICATEDUSER']._serialized_start=392
  _globals['_AUTHENTICATEDUSER']._serialized_end=465
# @@protoc_insertion_point(module_scope)
