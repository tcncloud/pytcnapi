# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/aclpb/aclpb.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'api/v1alpha1/vanalytics/aclpb/aclpb.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/v1alpha1/vanalytics/aclpb/aclpb.proto\x12\x1d\x61pi.v1alpha1.vanalytics.aclpb\"O\n\x0c\x41gentCallLog\x12?\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32%.api.v1alpha1.vanalytics.aclpb.ActionR\x07\x61\x63tions\"\x95\x01\n\x06\x41\x63tion\x12\x62\n\x13\x63\x61ll_skills_initial\x18\x01 \x01(\x0b\x32\x30.api.v1alpha1.vanalytics.aclpb.CallSkillsInitialH\x00R\x11\x63\x61llSkillsInitial\x12\x1f\n\ncall_ended\x18\x02 \x01(\tH\x00R\tcallEndedB\x06\n\x04kind\";\n\x11\x43\x61llSkillsInitial\x12\x12\n\x04need\x18\x01 \x03(\tR\x04need\x12\x12\n\x04want\x18\x02 \x03(\tR\x04wantB\xc7\x01\n!com.api.v1alpha1.vanalytics.aclpbB\nAclpbProtoP\x01\xa2\x02\x04\x41VVA\xaa\x02\x1d\x41pi.V1alpha1.Vanalytics.Aclpb\xca\x02\x1d\x41pi\\V1alpha1\\Vanalytics\\Aclpb\xe2\x02)Api\\V1alpha1\\Vanalytics\\Aclpb\\GPBMetadata\xea\x02 Api::V1alpha1::Vanalytics::Aclpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.aclpb.aclpb_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.api.v1alpha1.vanalytics.aclpbB\nAclpbProtoP\001\242\002\004AVVA\252\002\035Api.V1alpha1.Vanalytics.Aclpb\312\002\035Api\\V1alpha1\\Vanalytics\\Aclpb\342\002)Api\\V1alpha1\\Vanalytics\\Aclpb\\GPBMetadata\352\002 Api::V1alpha1::Vanalytics::Aclpb'
  _globals['_AGENTCALLLOG']._serialized_start=76
  _globals['_AGENTCALLLOG']._serialized_end=155
  _globals['_ACTION']._serialized_start=158
  _globals['_ACTION']._serialized_end=307
  _globals['_CALLSKILLSINITIAL']._serialized_start=309
  _globals['_CALLSKILLSINITIAL']._serialized_end=368
# @@protoc_insertion_point(module_scope)
