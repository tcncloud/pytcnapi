# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tcnapi/omni/projects/v1/service.proto
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
    'tcnapi/omni/projects/v1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from tcnapi.omni.projects.v1 import entities_pb2 as tcnapi_dot_omni_dot_projects_dot_v1_dot_entities__pb2
from tcnapi.omni.projects.v1 import projects_pb2 as tcnapi_dot_omni_dot_projects_dot_v1_dot_projects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%tcnapi/omni/projects/v1/service.proto\x12\x17tcnapi.omni.projects.v1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a&tcnapi/omni/projects/v1/entities.proto\x1a&tcnapi/omni/projects/v1/projects.proto2\xd7\x07\n\x08Projects\x12\xc1\x01\n\x0cListProjects\x12,.tcnapi.omni.projects.v1.ListProjectsRequest\x1a-.tcnapi.omni.projects.v1.ListProjectsResponse\"T\xda\x41\x06parent\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02;\x12\x39/tcnapi/omni/projects/v1/{parent=org/*/region/*}/projects\x12\xae\x01\n\nGetProject\x12*.tcnapi.omni.projects.v1.GetProjectRequest\x1a .tcnapi.omni.projects.v1.Project\"R\xda\x41\x04name\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02;\x12\x39/tcnapi/omni/projects/v1/{name=org/*/region/*/projects/*}\x12\xc7\x01\n\rCreateProject\x12-.tcnapi.omni.projects.v1.CreateProjectRequest\x1a .tcnapi.omni.projects.v1.Project\"e\xda\x41\x0eparent,project\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02\x44\"9/tcnapi/omni/projects/v1/{parent=org/*/region/*}/projects:\x07project\x12\xd4\x01\n\rUpdateProject\x12-.tcnapi.omni.projects.v1.UpdateProjectRequest\x1a .tcnapi.omni.projects.v1.Project\"r\xda\x41\x13project,update_mask\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02L2A/tcnapi/omni/projects/v1/{project.name=org/*/region/*/projects/*}:\x07project\x12\xb4\x01\n\rDeleteProject\x12-.tcnapi.omni.projects.v1.DeleteProjectRequest\x1a .tcnapi.omni.projects.v1.Project\"R\xda\x41\x04name\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02;*9/tcnapi/omni/projects/v1/{name=org/*/region/*/projects/*}B\xaa\x01\n\x1b\x63om.tcnapi.omni.projects.v1B\x0cServiceProtoP\x01\xa2\x02\x03TOP\xaa\x02\x17Tcnapi.Omni.Projects.V1\xca\x02\x17Tcnapi\\Omni\\Projects\\V1\xe2\x02#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\xea\x02\x1aTcnapi::Omni::Projects::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tcnapi.omni.projects.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.tcnapi.omni.projects.v1B\014ServiceProtoP\001\242\002\003TOP\252\002\027Tcnapi.Omni.Projects.V1\312\002\027Tcnapi\\Omni\\Projects\\V1\342\002#Tcnapi\\Omni\\Projects\\V1\\GPBMetadata\352\002\032Tcnapi::Omni::Projects::V1'
  _globals['_PROJECTS'].methods_by_name['ListProjects']._loaded_options = None
  _globals['_PROJECTS'].methods_by_name['ListProjects']._serialized_options = b'\332A\006parent\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002;\0229/tcnapi/omni/projects/v1/{parent=org/*/region/*}/projects'
  _globals['_PROJECTS'].methods_by_name['GetProject']._loaded_options = None
  _globals['_PROJECTS'].methods_by_name['GetProject']._serialized_options = b'\332A\004name\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002;\0229/tcnapi/omni/projects/v1/{name=org/*/region/*/projects/*}'
  _globals['_PROJECTS'].methods_by_name['CreateProject']._loaded_options = None
  _globals['_PROJECTS'].methods_by_name['CreateProject']._serialized_options = b'\332A\016parent,project\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002D\"9/tcnapi/omni/projects/v1/{parent=org/*/region/*}/projects:\007project'
  _globals['_PROJECTS'].methods_by_name['UpdateProject']._loaded_options = None
  _globals['_PROJECTS'].methods_by_name['UpdateProject']._serialized_options = b'\332A\023project,update_mask\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002L2A/tcnapi/omni/projects/v1/{project.name=org/*/region/*/projects/*}:\007project'
  _globals['_PROJECTS'].methods_by_name['DeleteProject']._loaded_options = None
  _globals['_PROJECTS'].methods_by_name['DeleteProject']._serialized_options = b'\332A\004name\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002;*9/tcnapi/omni/projects/v1/{name=org/*/region/*/projects/*}'
  _globals['_PROJECTS']._serialized_start=227
  _globals['_PROJECTS']._serialized_end=1210
# @@protoc_insertion_point(module_scope)