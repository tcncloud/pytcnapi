# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/agent_profile_group.proto
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
    'api/v1alpha1/org/agent_profile_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import agent_profile_group_pb2 as api_dot_commons_dot_org_dot_agent__profile__group__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/v1alpha1/org/agent_profile_group.proto\x12\x10\x61pi.v1alpha1.org\x1a)api/commons/org/agent_profile_group.proto\"R\n\x1bGetAgentProfileGroupRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x02 \x01(\tR\x13\x61gentProfileGroupId\"r\n\x1cGetAgentProfileGroupResponse\x12R\n\x13\x61gent_profile_group\x18\x01 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"t\n\x1eUpdateAgentProfileGroupRequest\x12R\n\x13\x61gent_profile_group\x18\x02 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"!\n\x1fUpdateAgentProfileGroupResponse\"\x1f\n\x1dListAgentProfileGroupsRequest\"v\n\x1eListAgentProfileGroupsResponse\x12T\n\x14\x61gent_profile_groups\x18\x01 \x03(\x0b\x32\".api.commons.org.AgentProfileGroupR\x12\x61gentProfileGroups\"t\n\x1e\x43reateAgentProfileGroupRequest\x12R\n\x13\x61gent_profile_group\x18\x02 \x01(\x0b\x32\".api.commons.org.AgentProfileGroupR\x11\x61gentProfileGroup\"V\n\x1f\x43reateAgentProfileGroupResponse\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\"U\n\x1e\x44\x65leteAgentProfileGroupRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x02 \x01(\tR\x13\x61gentProfileGroupId\"!\n\x1f\x44\x65leteAgentProfileGroupResponse\"q\n\x1f\x41ssignAgentProfileGroupsRequest\x12\x33\n\x16\x61gent_profile_group_id\x18\x02 \x01(\tR\x13\x61gentProfileGroupId\x12\x19\n\x08user_ids\x18\x03 \x03(\tR\x07userIds\"\"\n AssignAgentProfileGroupsResponseB\x90\x01\n\x14\x63om.api.v1alpha1.orgB\x16\x41gentProfileGroupProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.agent_profile_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\026AgentProfileGroupProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_GETAGENTPROFILEGROUPREQUEST']._serialized_start=107
  _globals['_GETAGENTPROFILEGROUPREQUEST']._serialized_end=189
  _globals['_GETAGENTPROFILEGROUPRESPONSE']._serialized_start=191
  _globals['_GETAGENTPROFILEGROUPRESPONSE']._serialized_end=305
  _globals['_UPDATEAGENTPROFILEGROUPREQUEST']._serialized_start=307
  _globals['_UPDATEAGENTPROFILEGROUPREQUEST']._serialized_end=423
  _globals['_UPDATEAGENTPROFILEGROUPRESPONSE']._serialized_start=425
  _globals['_UPDATEAGENTPROFILEGROUPRESPONSE']._serialized_end=458
  _globals['_LISTAGENTPROFILEGROUPSREQUEST']._serialized_start=460
  _globals['_LISTAGENTPROFILEGROUPSREQUEST']._serialized_end=491
  _globals['_LISTAGENTPROFILEGROUPSRESPONSE']._serialized_start=493
  _globals['_LISTAGENTPROFILEGROUPSRESPONSE']._serialized_end=611
  _globals['_CREATEAGENTPROFILEGROUPREQUEST']._serialized_start=613
  _globals['_CREATEAGENTPROFILEGROUPREQUEST']._serialized_end=729
  _globals['_CREATEAGENTPROFILEGROUPRESPONSE']._serialized_start=731
  _globals['_CREATEAGENTPROFILEGROUPRESPONSE']._serialized_end=817
  _globals['_DELETEAGENTPROFILEGROUPREQUEST']._serialized_start=819
  _globals['_DELETEAGENTPROFILEGROUPREQUEST']._serialized_end=904
  _globals['_DELETEAGENTPROFILEGROUPRESPONSE']._serialized_start=906
  _globals['_DELETEAGENTPROFILEGROUPRESPONSE']._serialized_end=939
  _globals['_ASSIGNAGENTPROFILEGROUPSREQUEST']._serialized_start=941
  _globals['_ASSIGNAGENTPROFILEGROUPSREQUEST']._serialized_end=1054
  _globals['_ASSIGNAGENTPROFILEGROUPSRESPONSE']._serialized_start=1056
  _globals['_ASSIGNAGENTPROFILEGROUPSRESPONSE']._serialized_end=1090
# @@protoc_insertion_point(module_scope)
