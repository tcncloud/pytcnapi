# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/legacy/service.proto
# Protobuf Python Version: 5.28.0
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
    0,
    '',
    'api/v1alpha1/org/legacy/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.legacy import entities_pb2 as api_dot_v1alpha1_dot_org_dot_legacy_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/org/legacy/service.proto\x12\x17\x61pi.v1alpha1.org.legacy\x1a\x17\x61nnotations/authz.proto\x1a&api/v1alpha1/org/legacy/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xd6\x01\n\tOrgLegacy\x12\xc8\x01\n\x14RegisterOrganization\x12\x34.api.v1alpha1.org.legacy.RegisterOrganizationRequest\x1a\x35.api.v1alpha1.org.legacy.RegisterOrganizationResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/org/legacy/organization/register:\x01*B\xab\x01\n\x1b\x63om.api.v1alpha1.org.legacyB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOL\xaa\x02\x17\x41pi.V1alpha1.Org.Legacy\xca\x02\x17\x41pi\\V1alpha1\\Org\\Legacy\xe2\x02#Api\\V1alpha1\\Org\\Legacy\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Legacyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.legacy.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.legacyB\014ServiceProtoP\001\242\002\004AVOL\252\002\027Api.V1alpha1.Org.Legacy\312\002\027Api\\V1alpha1\\Org\\Legacy\342\002#Api\\V1alpha1\\Org\\Legacy\\GPBMetadata\352\002\032Api::V1alpha1::Org::Legacy'
  _globals['_ORGLEGACY'].methods_by_name['RegisterOrganization']._loaded_options = None
  _globals['_ORGLEGACY'].methods_by_name['RegisterOrganization']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0023\"./api/v1alpha1/org/legacy/organization/register:\001*'
  _globals['_ORGLEGACY']._serialized_start=162
  _globals['_ORGLEGACY']._serialized_end=376
# @@protoc_insertion_point(module_scope)
