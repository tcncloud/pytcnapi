# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/skills/entities.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import skill_group_pb2 as api_dot_commons_dot_org_dot_skill__group__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/org/skills/entities.proto\x12\x17\x61pi.v1alpha1.org.skills\x1a!api/commons/org/skill_group.proto\"W\n\x17\x43reateSkillGroupRequest\x12<\n\x0bskill_group\x18\x01 \x01(\x0b\x32\x1b.api.commons.org.SkillGroupR\nskillGroup\"@\n\x18\x43reateSkillGroupResponse\x12$\n\x0eskill_group_id\x18\x01 \x01(\tR\x0cskillGroupId\"7\n\x16ListSkillGroupsRequest\x12\x1d\n\nfield_mask\x18\x01 \x03(\tR\tfieldMask\"Y\n\x17ListSkillGroupsResponse\x12>\n\x0cskill_groups\x18\x01 \x03(\x0b\x32\x1b.api.commons.org.SkillGroupR\x0bskillGroups\"v\n\x17UpdateSkillGroupRequest\x12<\n\x0bskill_group\x18\x01 \x01(\x0b\x32\x1b.api.commons.org.SkillGroupR\nskillGroup\x12\x1d\n\nfield_mask\x18\x02 \x03(\tR\tfieldMask\"\x1a\n\x18UpdateSkillGroupResponse\"[\n\x14GetSkillGroupRequest\x12$\n\x0eskill_group_id\x18\x01 \x01(\tR\x0cskillGroupId\x12\x1d\n\nfield_mask\x18\x02 \x03(\tR\tfieldMask\"U\n\x15GetSkillGroupResponse\x12<\n\x0bskill_group\x18\x01 \x01(\x0b\x32\x1b.api.commons.org.SkillGroupR\nskillGroup\"?\n\x17\x44\x65leteSkillGroupRequest\x12$\n\x0eskill_group_id\x18\x01 \x01(\tR\x0cskillGroupId\"\x1a\n\x18\x44\x65leteSkillGroupResponse\"[\n\x18\x41ssignSkillGroupsRequest\x12&\n\x0fskill_group_ids\x18\x01 \x03(\tR\rskillGroupIds\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1b\n\x19\x41ssignSkillGroupsResponse\"[\n\x18RevokeSkillGroupsRequest\x12&\n\x0fskill_group_ids\x18\x01 \x03(\tR\rskillGroupIds\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1b\n\x19RevokeSkillGroupsResponse\"4\n\x19GetUserSkillGroupsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"D\n\x1aGetUserSkillGroupsResponse\x12&\n\x0fskill_group_ids\x18\x01 \x03(\tR\rskillGroupIds\"/\n\x14GetUserSkillsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"Q\n\x15GetUserSkillsResponse\x12\x38\n\nskill_sets\x18\x01 \x03(\x0b\x32\x19.api.commons.org.SkillSetR\tskillSets\"C\n\x1bGetSkillGroupMembersRequest\x12$\n\x0eskill_group_id\x18\x01 \x01(\tR\x0cskillGroupId\"9\n\x1cGetSkillGroupMembersResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIdsB\xac\x01\n\x1b\x63om.api.v1alpha1.org.skillsB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOS\xaa\x02\x17\x41pi.V1alpha1.Org.Skills\xca\x02\x17\x41pi\\V1alpha1\\Org\\Skills\xe2\x02#Api\\V1alpha1\\Org\\Skills\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Skillsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.skills.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.skillsB\rEntitiesProtoP\001\242\002\004AVOS\252\002\027Api.V1alpha1.Org.Skills\312\002\027Api\\V1alpha1\\Org\\Skills\342\002#Api\\V1alpha1\\Org\\Skills\\GPBMetadata\352\002\032Api::V1alpha1::Org::Skills'
  _globals['_CREATESKILLGROUPREQUEST']._serialized_start=102
  _globals['_CREATESKILLGROUPREQUEST']._serialized_end=189
  _globals['_CREATESKILLGROUPRESPONSE']._serialized_start=191
  _globals['_CREATESKILLGROUPRESPONSE']._serialized_end=255
  _globals['_LISTSKILLGROUPSREQUEST']._serialized_start=257
  _globals['_LISTSKILLGROUPSREQUEST']._serialized_end=312
  _globals['_LISTSKILLGROUPSRESPONSE']._serialized_start=314
  _globals['_LISTSKILLGROUPSRESPONSE']._serialized_end=403
  _globals['_UPDATESKILLGROUPREQUEST']._serialized_start=405
  _globals['_UPDATESKILLGROUPREQUEST']._serialized_end=523
  _globals['_UPDATESKILLGROUPRESPONSE']._serialized_start=525
  _globals['_UPDATESKILLGROUPRESPONSE']._serialized_end=551
  _globals['_GETSKILLGROUPREQUEST']._serialized_start=553
  _globals['_GETSKILLGROUPREQUEST']._serialized_end=644
  _globals['_GETSKILLGROUPRESPONSE']._serialized_start=646
  _globals['_GETSKILLGROUPRESPONSE']._serialized_end=731
  _globals['_DELETESKILLGROUPREQUEST']._serialized_start=733
  _globals['_DELETESKILLGROUPREQUEST']._serialized_end=796
  _globals['_DELETESKILLGROUPRESPONSE']._serialized_start=798
  _globals['_DELETESKILLGROUPRESPONSE']._serialized_end=824
  _globals['_ASSIGNSKILLGROUPSREQUEST']._serialized_start=826
  _globals['_ASSIGNSKILLGROUPSREQUEST']._serialized_end=917
  _globals['_ASSIGNSKILLGROUPSRESPONSE']._serialized_start=919
  _globals['_ASSIGNSKILLGROUPSRESPONSE']._serialized_end=946
  _globals['_REVOKESKILLGROUPSREQUEST']._serialized_start=948
  _globals['_REVOKESKILLGROUPSREQUEST']._serialized_end=1039
  _globals['_REVOKESKILLGROUPSRESPONSE']._serialized_start=1041
  _globals['_REVOKESKILLGROUPSRESPONSE']._serialized_end=1068
  _globals['_GETUSERSKILLGROUPSREQUEST']._serialized_start=1070
  _globals['_GETUSERSKILLGROUPSREQUEST']._serialized_end=1122
  _globals['_GETUSERSKILLGROUPSRESPONSE']._serialized_start=1124
  _globals['_GETUSERSKILLGROUPSRESPONSE']._serialized_end=1192
  _globals['_GETUSERSKILLSREQUEST']._serialized_start=1194
  _globals['_GETUSERSKILLSREQUEST']._serialized_end=1241
  _globals['_GETUSERSKILLSRESPONSE']._serialized_start=1243
  _globals['_GETUSERSKILLSRESPONSE']._serialized_end=1324
  _globals['_GETSKILLGROUPMEMBERSREQUEST']._serialized_start=1326
  _globals['_GETSKILLGROUPMEMBERSREQUEST']._serialized_end=1393
  _globals['_GETSKILLGROUPMEMBERSRESPONSE']._serialized_start=1395
  _globals['_GETSKILLGROUPMEMBERSRESPONSE']._serialized_end=1452
# @@protoc_insertion_point(module_scope)
