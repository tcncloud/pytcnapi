# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/soundboard/service.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'api/v1alpha1/soundboard/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.soundboard import entities_pb2 as api_dot_v1alpha1_dot_soundboard_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/soundboard/service.proto\x12\x17\x61pi.v1alpha1.soundboard\x1a\x17\x61nnotations/authz.proto\x1a&api/v1alpha1/soundboard/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xe4\x06\n\nSoundboard\x12\xae\x01\n\x11GetSoundboardFile\x12-.api.v1alpha1.soundboard.GetSoundboardFileReq\x1a-.api.v1alpha1.soundboard.GetSoundboardFileRes\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa4\r\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/soundboard/getfile:\x01*0\x01\x12\xa8\x01\n\x10\x43reateSoundboard\x12,.api.v1alpha1.soundboard.CreateSoundboardReq\x1a,.api.v1alpha1.soundboard.CreateSoundboardRes\"8\xba\xb8\x91\x02\x05\n\x03\x08\xa5\r\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/soundboard/create:\x01*\x12\xa3\x01\n\x0fListSoundboards\x12+.api.v1alpha1.soundboard.ListSoundboardsReq\x1a+.api.v1alpha1.soundboard.ListSoundboardsRes\"6\xba\xb8\x91\x02\x05\n\x03\x08\xa4\r\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/org/soundboard/list:\x01*\x12\xa8\x01\n\x10UpdateSoundboard\x12,.api.v1alpha1.soundboard.UpdateSoundboardReq\x1a,.api.v1alpha1.soundboard.UpdateSoundboardRes\"8\xba\xb8\x91\x02\x05\n\x03\x08\xa5\r\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/soundboard/update:\x01*\x12\xa8\x01\n\x10\x44\x65leteSoundboard\x12,.api.v1alpha1.soundboard.DeleteSoundboardReq\x1a,.api.v1alpha1.soundboard.DeleteSoundboardRes\"8\xba\xb8\x91\x02\x05\n\x03\x08\xa5\r\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/soundboard/delete:\x01*B\xa9\x01\n\x1b\x63om.api.v1alpha1.soundboardB\x0cServiceProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Soundboard\xca\x02\x17\x41pi\\V1alpha1\\Soundboard\xe2\x02#Api\\V1alpha1\\Soundboard\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Soundboardb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.soundboard.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.soundboardB\014ServiceProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Soundboard\312\002\027Api\\V1alpha1\\Soundboard\342\002#Api\\V1alpha1\\Soundboard\\GPBMetadata\352\002\031Api::V1alpha1::Soundboard'
  _globals['_SOUNDBOARD'].methods_by_name['GetSoundboardFile']._loaded_options = None
  _globals['_SOUNDBOARD'].methods_by_name['GetSoundboardFile']._serialized_options = b'\272\270\221\002\005\n\003\010\244\r\202\323\344\223\002)\"$/api/v1alpha1/org/soundboard/getfile:\001*'
  _globals['_SOUNDBOARD'].methods_by_name['CreateSoundboard']._loaded_options = None
  _globals['_SOUNDBOARD'].methods_by_name['CreateSoundboard']._serialized_options = b'\272\270\221\002\005\n\003\010\245\r\202\323\344\223\002(\"#/api/v1alpha1/org/soundboard/create:\001*'
  _globals['_SOUNDBOARD'].methods_by_name['ListSoundboards']._loaded_options = None
  _globals['_SOUNDBOARD'].methods_by_name['ListSoundboards']._serialized_options = b'\272\270\221\002\005\n\003\010\244\r\202\323\344\223\002&\"!/api/v1alpha1/org/soundboard/list:\001*'
  _globals['_SOUNDBOARD'].methods_by_name['UpdateSoundboard']._loaded_options = None
  _globals['_SOUNDBOARD'].methods_by_name['UpdateSoundboard']._serialized_options = b'\272\270\221\002\005\n\003\010\245\r\202\323\344\223\002(\"#/api/v1alpha1/org/soundboard/update:\001*'
  _globals['_SOUNDBOARD'].methods_by_name['DeleteSoundboard']._loaded_options = None
  _globals['_SOUNDBOARD'].methods_by_name['DeleteSoundboard']._serialized_options = b'\272\270\221\002\005\n\003\010\245\r\202\323\344\223\002(\"#/api/v1alpha1/org/soundboard/delete:\001*'
  _globals['_SOUNDBOARD']._serialized_start=162
  _globals['_SOUNDBOARD']._serialized_end=1030
# @@protoc_insertion_point(module_scope)
