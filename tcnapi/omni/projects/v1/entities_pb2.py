# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tcnapi/omni/projects/v1/entities.proto
# Protobuf Python Version: 5.27.3
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
    3,
    '',
    'tcnapi/omni/projects/v1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from tcnapi.omni.projects.v1 import projects_pb2 as tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tcnapi/omni/projects/v1/entities.proto\x12\x17tcnapi.omni.projects.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a&tcnapi/omni/projects/v1/projects.proto\"\x9d\x01\n\x13ListProjectsRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\x12 projects.omni.tcnapi.com/ProjectR\x06parent\x12 \n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01R\x08pageSize\x12\"\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01R\tpageToken\"|\n\x14ListProjectsResponse\x12<\n\x08projects\x18\x01 \x03(\x0b\x32 .tcnapi.omni.projects.v1.ProjectR\x08projects\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"Q\n\x11GetProjectRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n projects.omni.tcnapi.com/ProjectR\x04name\"\x99\x01\n\x14\x43reateProjectRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\x12 projects.omni.tcnapi.com/ProjectR\x06parent\x12?\n\x07project\x18\x03 \x01(\x0b\x32 .tcnapi.omni.projects.v1.ProjectB\x03\xe0\x41\x02R\x07project\"\x99\x01\n\x14UpdateProjectRequest\x12?\n\x07project\x18\x01 \x01(\x0b\x32 .tcnapi.omni.projects.v1.ProjectB\x03\xe0\x41\x02R\x07project\x12@\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x01R\nupdateMask\"T\n\x14\x44\x65leteProjectRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe0\x41\x02\xfa\x41\"\n projects.omni.tcnapi.com/ProjectR\x04nameB\xab\x01\n\x1b\x63om.tcnapi.omni.projects.v1B\rEntitiesProtoP\x01\xa2\x02\x03TOP\xaa\x02\x17Tcnapi.Omni.Projects.V1\xca\x02\x17Tcnapi\\Omni\\Projects\\V1\xe2\x02#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\xea\x02\x1aTcnapi::Omni::Projects::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tcnapi.omni.projects.v1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.tcnapi.omni.projects.v1B\rEntitiesProtoP\001\242\002\003TOP\252\002\027Tcnapi.Omni.Projects.V1\312\002\027Tcnapi\\Omni\\Projects\\V1\342\002#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\352\002\032Tcnapi::Omni::Projects::V1'
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['parent']._serialized_options = b'\340A\002\372A\"\022 projects.omni.tcnapi.com/Project'
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\340A\001'
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTPROJECTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\340A\001'
  _globals['_GETPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n projects.omni.tcnapi.com/Project'
  _globals['_CREATEPROJECTREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_CREATEPROJECTREQUEST'].fields_by_name['parent']._serialized_options = b'\340A\002\372A\"\022 projects.omni.tcnapi.com/Project'
  _globals['_CREATEPROJECTREQUEST'].fields_by_name['project']._loaded_options = None
  _globals['_CREATEPROJECTREQUEST'].fields_by_name['project']._serialized_options = b'\340A\002'
  _globals['_UPDATEPROJECTREQUEST'].fields_by_name['project']._loaded_options = None
  _globals['_UPDATEPROJECTREQUEST'].fields_by_name['project']._serialized_options = b'\340A\002'
  _globals['_UPDATEPROJECTREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEPROJECTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\340A\001'
  _globals['_DELETEPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_DELETEPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\340A\002\372A\"\n projects.omni.tcnapi.com/Project'
  _globals['_LISTPROJECTSREQUEST']._serialized_start=202
  _globals['_LISTPROJECTSREQUEST']._serialized_end=359
  _globals['_LISTPROJECTSRESPONSE']._serialized_start=361
  _globals['_LISTPROJECTSRESPONSE']._serialized_end=485
  _globals['_GETPROJECTREQUEST']._serialized_start=487
  _globals['_GETPROJECTREQUEST']._serialized_end=568
  _globals['_CREATEPROJECTREQUEST']._serialized_start=571
  _globals['_CREATEPROJECTREQUEST']._serialized_end=724
  _globals['_UPDATEPROJECTREQUEST']._serialized_start=727
  _globals['_UPDATEPROJECTREQUEST']._serialized_end=880
  _globals['_DELETEPROJECTREQUEST']._serialized_start=882
  _globals['_DELETEPROJECTREQUEST']._serialized_end=966
# @@protoc_insertion_point(module_scope)