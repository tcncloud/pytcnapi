# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/fts/service.proto
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
    'api/v1alpha1/fts/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/v1alpha1/fts/service.proto\x12\x10\x61pi.v1alpha1.fts\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\"-\n\x13GetUploadFileUrlReq\x12\x16\n\x06prefix\x18\x01 \x01(\tR\x06prefix\"7\n\x13GetUploadFileUrlRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x0e\n\x02id\x18\x03 \x01(\tR\x02id2\x9b\x01\n\x06\x46tsApi\x12\x90\x01\n\x10GetUploadFileUrl\x12%.api.v1alpha1.fts.GetUploadFileUrlReq\x1a%.api.v1alpha1.fts.GetUploadFileUrlRes\".\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02!\"\x1c/api/v1alpha1/fts/upload_url:\x01*B\x86\x01\n\x14\x63om.api.v1alpha1.ftsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VF\xaa\x02\x10\x41pi.V1alpha1.Fts\xca\x02\x10\x41pi\\V1alpha1\\Fts\xe2\x02\x1c\x41pi\\V1alpha1\\Fts\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Ftsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.fts.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.ftsB\014ServiceProtoP\001\242\002\003AVF\252\002\020Api.V1alpha1.Fts\312\002\020Api\\V1alpha1\\Fts\342\002\034Api\\V1alpha1\\Fts\\GPBMetadata\352\002\022Api::V1alpha1::Fts'
  _globals['_FTSAPI'].methods_by_name['GetUploadFileUrl']._loaded_options = None
  _globals['_FTSAPI'].methods_by_name['GetUploadFileUrl']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002!\"\034/api/v1alpha1/fts/upload_url:\001*'
  _globals['_GETUPLOADFILEURLREQ']._serialized_start=107
  _globals['_GETUPLOADFILEURLREQ']._serialized_end=152
  _globals['_GETUPLOADFILEURLRES']._serialized_start=154
  _globals['_GETUPLOADFILEURLRES']._serialized_end=209
  _globals['_FTSAPI']._serialized_start=212
  _globals['_FTSAPI']._serialized_end=367
# @@protoc_insertion_point(module_scope)
