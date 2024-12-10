# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tcnapi/omni/projects/v1/projects.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'tcnapi/omni/projects/v1/projects.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tcnapi/omni/projects/v1/projects.proto\x12\x17tcnapi.omni.projects.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x98\x03\n\x07Project\x12\x17\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x08R\x04name\x12\x19\n\x05title\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05title\x12%\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0b\x64\x65scription\x12\x41\n\x05state\x18\x04 \x01(\x0e\x32&.tcnapi.omni.projects.v1.Project.StateB\x03\xe0\x41\x03R\x05state\x12@\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\"D\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\nSTATE_OPEN\x10\xe8\x84\x01\x12\x12\n\x0cSTATE_CLOSED\x10\xf2\x84\x01:g\xea\x41\x64\n\x1ftcnapi.omni.projects.v1/Project\x12.regions/{region}/orgs/{org}/projects/{project}*\x08projects2\x07projectB\xab\x01\n\x1b\x63om.tcnapi.omni.projects.v1B\rProjectsProtoP\x01\xa2\x02\x03TOP\xaa\x02\x17Tcnapi.Omni.Projects.V1\xca\x02\x17Tcnapi\\Omni\\Projects\\V1\xe2\x02#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\xea\x02\x1aTcnapi::Omni::Projects::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tcnapi.omni.projects.v1.projects_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.tcnapi.omni.projects.v1B\rProjectsProtoP\001\242\002\003TOP\252\002\027Tcnapi.Omni.Projects.V1\312\002\027Tcnapi\\Omni\\Projects\\V1\342\002#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\352\002\032Tcnapi::Omni::Projects::V1'
  _globals['_PROJECT'].fields_by_name['name']._loaded_options = None
  _globals['_PROJECT'].fields_by_name['name']._serialized_options = b'\340A\010'
  _globals['_PROJECT'].fields_by_name['title']._loaded_options = None
  _globals['_PROJECT'].fields_by_name['title']._serialized_options = b'\340A\002'
  _globals['_PROJECT'].fields_by_name['description']._loaded_options = None
  _globals['_PROJECT'].fields_by_name['description']._serialized_options = b'\340A\002'
  _globals['_PROJECT'].fields_by_name['state']._loaded_options = None
  _globals['_PROJECT'].fields_by_name['state']._serialized_options = b'\340A\003'
  _globals['_PROJECT'].fields_by_name['create_time']._loaded_options = None
  _globals['_PROJECT'].fields_by_name['create_time']._serialized_options = b'\340A\003'
  _globals['_PROJECT']._loaded_options = None
  _globals['_PROJECT']._serialized_options = b'\352Ad\n\037tcnapi.omni.projects.v1/Project\022.regions/{region}/orgs/{org}/projects/{project}*\010projects2\007project'
  _globals['_PROJECT']._serialized_start=161
  _globals['_PROJECT']._serialized_end=569
  _globals['_PROJECT_STATE']._serialized_start=396
  _globals['_PROJECT_STATE']._serialized_end=464
# @@protoc_insertion_point(module_scope)
