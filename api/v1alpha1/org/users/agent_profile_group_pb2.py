# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/users/agent_profile_group.proto
# Protobuf Python Version: 5.28.2
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
    2,
    '',
    'api/v1alpha1/org/users/agent_profile_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import agent_profile_group_pb2 as api_dot_commons_dot_org_dot_agent__profile__group__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/org/users/agent_profile_group.proto\x12\x16\x61pi.v1alpha1.org.users\x1a)api/commons/org/agent_profile_group.proto\"R\n\x1bGetAgentProfileGroupRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\"r\n\x1cGetAgentProfileGroupResponse\x12R\n\x13\x61gent_profile_group\x18\x01 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"t\n\x1eUpdateAgentProfileGroupRequest\x12R\n\x13\x61gent_profile_group\x18\x01 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"!\n\x1fUpdateAgentProfileGroupResponse\"\x1f\n\x1dListAgentProfileGroupsRequest\"v\n\x1eListAgentProfileGroupsResponse\x12T\n\x14\x61gent_profile_groups\x18\x01 \x03(\x0b\x32\".api.commons.org.AgentProfileGroupR\x12\x61gentProfileGroups\"t\n\x1e\x43reateAgentProfileGroupRequest\x12R\n\x13\x61gent_profile_group\x18\x01 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"V\n\x1f\x43reateAgentProfileGroupResponse\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\"U\n\x1e\x44\x65leteAgentProfileGroupRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\"!\n\x1f\x44\x65leteAgentProfileGroupResponse\"q\n\x1f\x41ssignAgentProfileGroupsRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"\"\n AssignAgentProfileGroupsResponseB\xb0\x01\n\x1a\x63om.api.v1alpha1.org.usersB\x16\x41gentProfileGroupProtoP\x01\xa2\x02\x04\x41VOU\xaa\x02\x16\x41pi.V1alpha1.Org.Users\xca\x02\x16\x41pi\\V1alpha1\\Org\\Users\xe2\x02\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Org::Usersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.users.agent_profile_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.api.v1alpha1.org.usersB\026AgentProfileGroupProtoP\001\242\002\004AVOU\252\002\026Api.V1alpha1.Org.Users\312\002\026Api\\V1alpha1\\Org\\Users\342\002\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\352\002\031Api::V1alpha1::Org::Users'
  _globals['_GETAGENTPROFILEGROUPREQUEST']._serialized_start=119
  _globals['_GETAGENTPROFILEGROUPREQUEST']._serialized_end=201
  _globals['_GETAGENTPROFILEGROUPRESPONSE']._serialized_start=203
  _globals['_GETAGENTPROFILEGROUPRESPONSE']._serialized_end=317
  _globals['_UPDATEAGENTPROFILEGROUPREQUEST']._serialized_start=319
  _globals['_UPDATEAGENTPROFILEGROUPREQUEST']._serialized_end=435
  _globals['_UPDATEAGENTPROFILEGROUPRESPONSE']._serialized_start=437
  _globals['_UPDATEAGENTPROFILEGROUPRESPONSE']._serialized_end=470
  _globals['_LISTAGENTPROFILEGROUPSREQUEST']._serialized_start=472
  _globals['_LISTAGENTPROFILEGROUPSREQUEST']._serialized_end=503
  _globals['_LISTAGENTPROFILEGROUPSRESPONSE']._serialized_start=505
  _globals['_LISTAGENTPROFILEGROUPSRESPONSE']._serialized_end=623
  _globals['_CREATEAGENTPROFILEGROUPREQUEST']._serialized_start=625
  _globals['_CREATEAGENTPROFILEGROUPREQUEST']._serialized_end=741
  _globals['_CREATEAGENTPROFILEGROUPRESPONSE']._serialized_start=743
  _globals['_CREATEAGENTPROFILEGROUPRESPONSE']._serialized_end=829
  _globals['_DELETEAGENTPROFILEGROUPREQUEST']._serialized_start=831
  _globals['_DELETEAGENTPROFILEGROUPREQUEST']._serialized_end=916
  _globals['_DELETEAGENTPROFILEGROUPRESPONSE']._serialized_start=918
  _globals['_DELETEAGENTPROFILEGROUPRESPONSE']._serialized_end=951
  _globals['_ASSIGNAGENTPROFILEGROUPSREQUEST']._serialized_start=953
  _globals['_ASSIGNAGENTPROFILEGROUPSREQUEST']._serialized_end=1066
  _globals['_ASSIGNAGENTPROFILEGROUPSRESPONSE']._serialized_start=1068
  _globals['_ASSIGNAGENTPROFILEGROUPSRESPONSE']._serialized_end=1102
# @@protoc_insertion_point(module_scope)
