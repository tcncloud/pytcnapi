# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/skills/service.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'api/v1alpha1/org/skills/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.skills import entities_pb2 as api_dot_v1alpha1_dot_org_dot_skills_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/org/skills/service.proto\x12\x17\x61pi.v1alpha1.org.skills\x1a\x17\x61nnotations/authz.proto\x1a&api/v1alpha1/org/skills/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xf9\x1a\n\rSkillsService\x12\xb2\x01\n\x10\x43reateSkillGroup\x12\x30.api.v1alpha1.org.skills.CreateSkillGroupRequest\x1a\x31.api.v1alpha1.org.skills.CreateSkillGroupResponse\"9\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/skills/createskillgroup:\x01*\x12\xb3\x01\n\x0fListSkillGroups\x12/.api.v1alpha1.org.skills.ListSkillGroupsRequest\x1a\x30.api.v1alpha1.org.skills.ListSkillGroupsResponse\"=\xba\xb8\x91\x02\t\n\x02\x08\x65\n\x03\x08\xe9\x02\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/skills/listskillgroups:\x01*\x12\xb2\x01\n\x10UpdateSkillGroup\x12\x30.api.v1alpha1.org.skills.UpdateSkillGroupRequest\x1a\x31.api.v1alpha1.org.skills.UpdateSkillGroupResponse\"9\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/skills/updateskillgroup:\x01*\x12\xa6\x01\n\rGetSkillGroup\x12-.api.v1alpha1.org.skills.GetSkillGroupRequest\x1a..api.v1alpha1.org.skills.GetSkillGroupResponse\"6\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02\'\"\"/api/v1alpha1/skills/getskillgroup:\x01*\x12\xb2\x01\n\x10\x44\x65leteSkillGroup\x12\x30.api.v1alpha1.org.skills.DeleteSkillGroupRequest\x1a\x31.api.v1alpha1.org.skills.DeleteSkillGroupResponse\"9\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/skills/deleteskillgroup:\x01*\x12\xd2\x01\n\x18RemoveSkillFromAllGroups\x12\x38.api.v1alpha1.org.skills.RemoveSkillFromAllGroupsRequest\x1a\x39.api.v1alpha1.org.skills.RemoveSkillFromAllGroupsResponse\"A\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/skills/removeskillfromallgroups:\x01*\x12\xb6\x01\n\x11\x41ssignSkillGroups\x12\x31.api.v1alpha1.org.skills.AssignSkillGroupsRequest\x1a\x32.api.v1alpha1.org.skills.AssignSkillGroupsResponse\":\xba\xb8\x91\x02\x04\n\x02\x08w\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/skills/assignskillgroups:\x01*\x12\xcd\x01\n\x17UpdateUsersOnSkillGroup\x12\x37.api.v1alpha1.org.skills.UpdateUsersOnSkillGroupRequest\x1a\x38.api.v1alpha1.org.skills.UpdateUsersOnSkillGroupResponse\"?\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/skills/updateuseronskillgroup:\x01*\x12\xb6\x01\n\x11RevokeSkillGroups\x12\x31.api.v1alpha1.org.skills.RevokeSkillGroupsRequest\x1a\x32.api.v1alpha1.org.skills.RevokeSkillGroupsResponse\":\xba\xb8\x91\x02\x04\n\x02\x08w\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/skills/revokeskillgroups:\x01*\x12\xba\x01\n\x12GetUserSkillGroups\x12\x32.api.v1alpha1.org.skills.GetUserSkillGroupsRequest\x1a\x33.api.v1alpha1.org.skills.GetUserSkillGroupsResponse\";\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/skills/getuserskillgroups:\x01*\x12\xa6\x01\n\rGetUserSkills\x12-.api.v1alpha1.org.skills.GetUserSkillsRequest\x1a..api.v1alpha1.org.skills.GetUserSkillsResponse\"6\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02\'\"\"/api/v1alpha1/skills/getuserskills:\x01*\x12\xc2\x01\n\x14GetSkillGroupMembers\x12\x34.api.v1alpha1.org.skills.GetSkillGroupMembersRequest\x1a\x35.api.v1alpha1.org.skills.GetSkillGroupMembersResponse\"=\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/skills/getskillgroupmembers:\x01*\x12\xca\x01\n\x16ListSkillGroupsMembers\x12\x36.api.v1alpha1.org.skills.ListSkillGroupsMembersRequest\x1a\x37.api.v1alpha1.org.skills.ListSkillGroupsMembersResponse\"?\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/skills/listskillgroupsmembers:\x01*\x12\xa8\x01\n\x0eGetAgentSkills\x12..api.v1alpha1.org.skills.GetAgentSkillsRequest\x1a/.api.v1alpha1.org.skills.GetAgentSkillsResponse\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/skills/getagentskills:\x01*\x12\xd4\x01\n\x19ListSkillsForCurrentAgent\x12\x39.api.v1alpha1.org.skills.ListSkillsForCurrentAgentRequest\x1a:.api.v1alpha1.org.skills.ListSkillsForCurrentAgentResponse\"@\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/skills/listskillsforcurrentagent:\x01*\x12\xcc\x01\n\x17ListAssignedSkillGroups\x12\x37.api.v1alpha1.org.skills.ListAssignedSkillGroupsRequest\x1a\x38.api.v1alpha1.org.skills.ListAssignedSkillGroupsResponse\">\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/skills/listassignedskillgroups:\x01*\x12\xc3\x01\n\x14\x41ssignOwnSkillGroups\x12\x34.api.v1alpha1.org.skills.AssignOwnSkillGroupsRequest\x1a\x35.api.v1alpha1.org.skills.AssignOwnSkillGroupsResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x02\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/skills/assignownskillgroups:\x01*\x12\xc3\x01\n\x14RevokeOwnSkillGroups\x12\x34.api.v1alpha1.org.skills.RevokeOwnSkillGroupsRequest\x1a\x35.api.v1alpha1.org.skills.RevokeOwnSkillGroupsResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xe9\x02\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/skills/revokeownskillgroups:\x01*B\xab\x01\n\x1b\x63om.api.v1alpha1.org.skillsB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOS\xaa\x02\x17\x41pi.V1alpha1.Org.Skills\xca\x02\x17\x41pi\\V1alpha1\\Org\\Skills\xe2\x02#Api\\V1alpha1\\Org\\Skills\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Skillsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.skills.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.skillsB\014ServiceProtoP\001\242\002\004AVOS\252\002\027Api.V1alpha1.Org.Skills\312\002\027Api\\V1alpha1\\Org\\Skills\342\002#Api\\V1alpha1\\Org\\Skills\\GPBMetadata\352\002\032Api::V1alpha1::Org::Skills'
  _globals['_SKILLSSERVICE'].methods_by_name['CreateSkillGroup']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['CreateSkillGroup']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002*\"%/api/v1alpha1/skills/createskillgroup:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillGroups']._serialized_options = b'\272\270\221\002\t\n\002\010e\n\003\010\351\002\202\323\344\223\002)\"$/api/v1alpha1/skills/listskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['UpdateSkillGroup']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['UpdateSkillGroup']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002*\"%/api/v1alpha1/skills/updateskillgroup:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['GetSkillGroup']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['GetSkillGroup']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002\'\"\"/api/v1alpha1/skills/getskillgroup:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['DeleteSkillGroup']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['DeleteSkillGroup']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002*\"%/api/v1alpha1/skills/deleteskillgroup:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['RemoveSkillFromAllGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['RemoveSkillFromAllGroups']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\0022\"-/api/v1alpha1/skills/removeskillfromallgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['AssignSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['AssignSkillGroups']._serialized_options = b'\272\270\221\002\004\n\002\010w\202\323\344\223\002+\"&/api/v1alpha1/skills/assignskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['UpdateUsersOnSkillGroup']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['UpdateUsersOnSkillGroup']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\0020\"+/api/v1alpha1/skills/updateuseronskillgroup:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['RevokeSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['RevokeSkillGroups']._serialized_options = b'\272\270\221\002\004\n\002\010w\202\323\344\223\002+\"&/api/v1alpha1/skills/revokeskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['GetUserSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['GetUserSkillGroups']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002,\"\'/api/v1alpha1/skills/getuserskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['GetUserSkills']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['GetUserSkills']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002\'\"\"/api/v1alpha1/skills/getuserskills:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['GetSkillGroupMembers']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['GetSkillGroupMembers']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002.\")/api/v1alpha1/skills/getskillgroupmembers:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillGroupsMembers']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillGroupsMembers']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\0020\"+/api/v1alpha1/skills/listskillgroupsmembers:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['GetAgentSkills']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['GetAgentSkills']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v1alpha1/skills/getagentskills:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillsForCurrentAgent']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['ListSkillsForCurrentAgent']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0023\"./api/v1alpha1/skills/listskillsforcurrentagent:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['ListAssignedSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['ListAssignedSkillGroups']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0021\",/api/v1alpha1/skills/listassignedskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['AssignOwnSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['AssignOwnSkillGroups']._serialized_options = b'\272\270\221\002\005\n\003\010\351\002\202\323\344\223\002.\")/api/v1alpha1/skills/assignownskillgroups:\001*'
  _globals['_SKILLSSERVICE'].methods_by_name['RevokeOwnSkillGroups']._loaded_options = None
  _globals['_SKILLSSERVICE'].methods_by_name['RevokeOwnSkillGroups']._serialized_options = b'\272\270\221\002\005\n\003\010\351\002\202\323\344\223\002.\")/api/v1alpha1/skills/revokeownskillgroups:\001*'
  _globals['_SKILLSSERVICE']._serialized_start=162
  _globals['_SKILLSSERVICE']._serialized_end=3611
# @@protoc_insertion_point(module_scope)
