# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/ghostnotifier/service.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'api/v1alpha1/ghostnotifier/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import ghostnotifier_pb2 as api_dot_commons_dot_ghostnotifier__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/ghostnotifier/service.proto\x12\x1a\x61pi.v1alpha1.ghostnotifier\x1a\x17\x61nnotations/authz.proto\x1a\x1f\x61pi/commons/ghostnotifier.proto\x1a\x1cgoogle/api/annotations.proto\"\x16\n\x14ListNotificationsReq2\xce\x01\n\x10GhostNotifierApi\x12\xb9\x01\n\x11ListNotifications\x12\x30.api.v1alpha1.ghostnotifier.ListNotificationsReq\x1a\x1e.api.commons.GhostNotification\"P\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x43\">/api/v1alpha1/ghostnotifier/ghostnotifierapi/listnotifications:\x01*0\x01\x42\xb8\x01\n\x1e\x63om.api.v1alpha1.ghostnotifierB\x0cServiceProtoP\x01\xa2\x02\x03\x41VG\xaa\x02\x1a\x41pi.V1alpha1.Ghostnotifier\xca\x02\x1a\x41pi\\V1alpha1\\Ghostnotifier\xe2\x02&Api\\V1alpha1\\Ghostnotifier\\GPBMetadata\xea\x02\x1c\x41pi::V1alpha1::Ghostnotifierb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.ghostnotifier.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.api.v1alpha1.ghostnotifierB\014ServiceProtoP\001\242\002\003AVG\252\002\032Api.V1alpha1.Ghostnotifier\312\002\032Api\\V1alpha1\\Ghostnotifier\342\002&Api\\V1alpha1\\Ghostnotifier\\GPBMetadata\352\002\034Api::V1alpha1::Ghostnotifier'
  _globals['_GHOSTNOTIFIERAPI'].methods_by_name['ListNotifications']._loaded_options = None
  _globals['_GHOSTNOTIFIERAPI'].methods_by_name['ListNotifications']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002C\">/api/v1alpha1/ghostnotifier/ghostnotifierapi/listnotifications:\001*'
  _globals['_LISTNOTIFICATIONSREQ']._serialized_start=160
  _globals['_LISTNOTIFICATIONSREQ']._serialized_end=182
  _globals['_GHOSTNOTIFIERAPI']._serialized_start=185
  _globals['_GHOSTNOTIFIERAPI']._serialized_end=391
# @@protoc_insertion_point(module_scope)
