# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vanalytics/support_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.vanalytics import flag_transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__transcript__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/vanalytics/support_service.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x17\x61nnotations/authz.proto\x1a-api/v1alpha1/vanalytics/flag_transcript.proto\x1a\x1cgoogle/api/annotations.proto2\xef\x01\n\x11VanalyticsSupport\x12\xd9\x01\n\x14\x44\x65leteFlagTranscript\x12\x34.api.v1alpha1.vanalytics.DeleteFlagTranscriptRequest\x1a\x35.api.v1alpha1.vanalytics.DeleteFlagTranscriptResponse\"T\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x44\"?/api/v1alpha1/vanalytics/vanalyticssupport/deleteflagtranscript:\x01*B\xb0\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x13SupportServiceProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.support_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\023SupportServiceProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_VANALYTICSSUPPORT'].methods_by_name['DeleteFlagTranscript']._loaded_options = None
  _globals['_VANALYTICSSUPPORT'].methods_by_name['DeleteFlagTranscript']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002D\"?/api/v1alpha1/vanalytics/vanalyticssupport/deleteflagtranscript:\001*'
  _globals['_VANALYTICSSUPPORT']._serialized_start=177
  _globals['_VANALYTICSSUPPORT']._serialized_end=416
# @@protoc_insertion_point(module_scope)
