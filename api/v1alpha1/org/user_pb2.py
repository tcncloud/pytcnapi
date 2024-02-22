# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/user.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import labels_pb2 as api_dot_commons_dot_org_dot_labels__pb2
from api.commons.org import permissions_pb2 as api_dot_commons_dot_org_dot_permissions__pb2
from api.commons.org import trusts_pb2 as api_dot_commons_dot_org_dot_trusts__pb2
from api.commons.org import user_pb2 as api_dot_commons_dot_org_dot_user__pb2
from api.commons import perms_pb2 as api_dot_commons_dot_perms__pb2
from api.commons import user_pb2 as api_dot_commons_dot_user__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pi/v1alpha1/org/user.proto\x12\x10\x61pi.v1alpha1.org\x1a\x15\x61pi/commons/org.proto\x1a\x1c\x61pi/commons/org/labels.proto\x1a!api/commons/org/permissions.proto\x1a\x1c\x61pi/commons/org/trusts.proto\x1a\x1a\x61pi/commons/org/user.proto\x1a\x17\x61pi/commons/perms.proto\x1a\x16\x61pi/commons/user.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xbe\x05\n\x11\x43reateUserRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastName\x12\x14\n\x05\x65mail\x18\x04 \x01(\tR\x05\x65mail\x12\x1b\n\tuser_name\x18\x05 \x01(\tR\x08userName\x12\x1a\n\x08password\x18\x06 \x01(\tR\x08password\x12\x30\n\x14permission_group_ids\x18\x07 \x03(\tR\x12permissionGroupIds\x12(\n\x10partner_agent_id\x18\t \x01(\tR\x0epartnerAgentId\x12\x33\n\x16p3_permission_group_id\x18\n \x01(\tR\x13p3PermissionGroupId\x12)\n\x10linkback_numbers\x18\x0b \x03(\tR\x0flinkbackNumbers\x12\x1d\n\ncaller_ids\x18\x0c \x03(\tR\tcallerIds\x12\x42\n\x0b\x64\x65\x66\x61ult_app\x18\r \x01(\x0e\x32!.api.commons.OperatorApplicationsR\ndefaultApp\x12$\n\x0euser_caller_id\x18\x0e \x01(\tR\x0cuserCallerId\x12\x33\n\x16\x61gent_profile_group_id\x18\x0f \x01(\tR\x13\x61gentProfileGroupId\x12\x1b\n\tlabel_ids\x18\x10 \x03(\tR\x08labelIds\x12J\n\x12time_zone_override\x18\x11 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12$\n\x0ehunt_group_sid\x18\x12 \x01(\x03R\x0chuntGroupSid\"-\n\x12\x43reateUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x80\x02\n\x1a\x43reateDelegatedUserRequest\x12 \n\x0c\x61uth_user_id\x18\x01 \x01(\tR\nauthUserId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\x12\x1a\n\x08username\x18\x04 \x01(\tR\x08username\x12\x1d\n\nfirst_name\x18\x05 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x06 \x01(\tR\x08lastName\x12\x16\n\x06groups\x18\x07 \x03(\tR\x06groups\x12#\n\rconnection_id\x18\x08 \x01(\tR\x0c\x63onnectionId\"6\n\x1b\x43reateDelegatedUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x12\n\x10GetMyUserRequest\"\xab\x07\n\x11GetMyUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1a\n\x08username\x18\r \x01(\tR\x08username\x12\x1c\n\tdelegated\x18\x03 \x01(\x08R\tdelegated\x12\x19\n\x08org_name\x18\x04 \x01(\tR\x07orgName\x12L\n\nhunt_group\x18\x05 \x01(\x0b\x32-.api.v1alpha1.org.GetMyUserResponse.HuntGroupR\thuntGroup\x12.\n\x06labels\x18\x06 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12.\n\x06skills\x18\x07 \x03(\x0b\x32\x16.api.commons.org.SkillR\x06skills\x12M\n\x11permission_groups\x18\x08 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\x12R\n\x13p3_permission_group\x18\t \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\x12\x65\n\x13\x61gent_profile_group\x18\n \x01(\x0b\x32\x35.api.v1alpha1.org.GetMyUserResponse.AgentProfileGroupR\x11\x61gentProfileGroup\x12.\n\x06trusts\x18\x0b \x03(\x0b\x32\x16.api.commons.org.TrustR\x06trusts\x12#\n\raccount_owner\x18\x0c \x01(\x08R\x0c\x61\x63\x63ountOwner\x12%\n\x0e\x65mail_verified\x18\x0e \x01(\x08R\remailVerified\x1aY\n\tHuntGroup\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12&\n\x0fhunt_group_name\x18\x02 \x01(\tR\rhuntGroupName\x1a\x81\x01\n\x11\x41gentProfileGroup\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\x12\x37\n\x18\x61gent_profile_group_name\x18\x02 \x01(\tR\x15\x61gentProfileGroupName\")\n\x0eGetUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\xdb\x0c\n\x0fGetUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1c\n\tdelegated\x18\x03 \x01(\x08R\tdelegated\x12J\n\x12time_zone_override\x18\x04 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12J\n\nhunt_group\x18\x05 \x01(\x0b\x32+.api.v1alpha1.org.GetUserResponse.HuntGroupR\thuntGroup\x12.\n\x06labels\x18\x06 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12.\n\x06skills\x18\x07 \x03(\x0b\x32\x16.api.commons.org.SkillR\x06skills\x12M\n\x11permission_groups\x18\x08 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\x12R\n\x13p3_permission_group\x18\t \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\x12\x63\n\x13\x61gent_profile_group\x18\n \x01(\x0b\x32\x33.api.v1alpha1.org.GetUserResponse.AgentProfileGroupR\x11\x61gentProfileGroup\x12\x19\n\x08org_name\x18\x0b \x01(\tR\x07orgName\x12\x1d\n\nfirst_name\x18\x0c \x01(\tR\tfirstName\x12\x1a\n\x08username\x18\r \x01(\tR\x08username\x12\x1b\n\tlast_name\x18\x0e \x01(\tR\x08lastName\x12%\n\x0elogin_disabled\x18\x0f \x01(\x08R\rloginDisabled\x12(\n\x10partner_agent_id\x18\x10 \x01(\tR\x0epartnerAgentId\x12$\n\x0euser_caller_id\x18\x11 \x01(\tR\x0cuserCallerId\x12)\n\x10linkback_numbers\x18\x12 \x03(\tR\x0flinkbackNumbers\x12\x1d\n\ncaller_ids\x18\x13 \x03(\tR\tcallerIds\x12\x42\n\x0b\x64\x65\x66\x61ult_app\x18\x14 \x01(\x0e\x32!.api.commons.OperatorApplicationsR\ndefaultApp\x12\x1b\n\tlogin_sid\x18\x15 \x01(\x03R\x08loginSid\x12\x1b\n\tagent_sid\x18\x16 \x01(\x03R\x08\x61gentSid\x12.\n\x06trusts\x18\x17 \x03(\x0b\x32\x16.api.commons.org.TrustR\x06trusts\x12\x14\n\x05\x65mail\x18\x18 \x01(\tR\x05\x65mail\x12%\n\x0e\x64\x65\x66\x61ult_region\x18\x19 \x01(\tR\rdefaultRegion\x12\x39\n\ncreated_at\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12=\n\x0clast_updated\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\x12\x36\n\x17password_reset_required\x18\x1c \x01(\x08R\x15passwordResetRequired\x12#\n\raccount_owner\x18\x1d \x01(\x08R\x0c\x61\x63\x63ountOwner\x12%\n\x0e\x65mail_verified\x18\x1e \x01(\x08R\remailVerified\x1aY\n\tHuntGroup\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12&\n\x0fhunt_group_name\x18\x02 \x01(\tR\rhuntGroupName\x1a\x81\x01\n\x11\x41gentProfileGroup\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\x12\x37\n\x18\x61gent_profile_group_name\x18\x02 \x01(\tR\x15\x61gentProfileGroupName\"G\n\x15GetUserByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\"\xba\x07\n\x16GetUserByOrgIdResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1a\n\x08username\x18\r \x01(\tR\x08username\x12\x1c\n\tdelegated\x18\x03 \x01(\x08R\tdelegated\x12\x19\n\x08org_name\x18\x04 \x01(\tR\x07orgName\x12Q\n\nhunt_group\x18\x05 \x01(\x0b\x32\x32.api.v1alpha1.org.GetUserByOrgIdResponse.HuntGroupR\thuntGroup\x12.\n\x06labels\x18\x06 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12.\n\x06skills\x18\x07 \x03(\x0b\x32\x16.api.commons.org.SkillR\x06skills\x12M\n\x11permission_groups\x18\x08 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\x12R\n\x13p3_permission_group\x18\t \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\x12j\n\x13\x61gent_profile_group\x18\n \x01(\x0b\x32:.api.v1alpha1.org.GetUserByOrgIdResponse.AgentProfileGroupR\x11\x61gentProfileGroup\x12.\n\x06trusts\x18\x15 \x03(\x0b\x32\x16.api.commons.org.TrustR\x06trusts\x12#\n\raccount_owner\x18\x16 \x01(\x08R\x0c\x61\x63\x63ountOwner\x12%\n\x0e\x65mail_verified\x18\x17 \x01(\x08R\remailVerified\x1aY\n\tHuntGroup\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12&\n\x0fhunt_group_name\x18\x02 \x01(\tR\rhuntGroupName\x1a\x81\x01\n\x11\x41gentProfileGroup\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\x12\x37\n\x18\x61gent_profile_group_name\x18\x02 \x01(\tR\x15\x61gentProfileGroupName\"\x13\n\x11ListAgentsRequest\"\x83\x0b\n\x12ListAgentsResponse\x12I\n\x06\x61gents\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.org.ListAgentsResponse.AgentDetailsR\x06\x61gents\x1a\xa1\n\n\x0c\x41gentDetails\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1d\n\nfirst_name\x18\x03 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x04 \x01(\tR\x08lastName\x12\x1a\n\x08username\x18\x05 \x01(\tR\x08username\x12.\n\x06skills\x18\x06 \x03(\x0b\x32\x16.api.commons.org.SkillR\x06skills\x12%\n\x0elogin_disabled\x18\x07 \x01(\x08R\rloginDisabled\x12Z\n\nhunt_group\x18\x08 \x01(\x0b\x32;.api.v1alpha1.org.ListAgentsResponse.AgentDetails.HuntGroupR\thuntGroup\x12.\n\x06labels\x18\t \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12\x1c\n\tdelegated\x18\n \x01(\x08R\tdelegated\x12\x1b\n\ttrust_ids\x18\x0b \x03(\tR\x08trustIds\x12M\n\x11permission_groups\x18\x0c \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\x12\x1b\n\tagent_sid\x18\r \x01(\x03R\x08\x61gentSid\x12\x12\n\x04name\x18\x0e \x01(\tR\x04name\x12(\n\x10partner_agent_id\x18\x0f \x01(\tR\x0epartnerAgentId\x12$\n\x0euser_caller_id\x18\x10 \x01(\tR\x0cuserCallerId\x12\x34\n\x07\x63reated\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12=\n\x0clast_updated\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\x12s\n\x13\x61gent_profile_group\x18\x13 \x01(\x0b\x32\x43.api.v1alpha1.org.ListAgentsResponse.AgentDetails.AgentProfileGroupR\x11\x61gentProfileGroup\x12\x14\n\x05\x61gent\x18\x14 \x01(\x08R\x05\x61gent\x12J\n\x12time_zone_override\x18\x15 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12\x14\n\x05\x65mail\x18\x16 \x01(\tR\x05\x65mail\x12%\n\x0e\x65mail_verified\x18\x17 \x01(\x08R\remailVerified\x12\x33\n\x08mfa_info\x18\x18 \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x07mfaInfo\x1aY\n\tHuntGroup\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12&\n\x0fhunt_group_name\x18\x02 \x01(\tR\rhuntGroupName\x1a\x81\x01\n\x11\x41gentProfileGroup\x12\x33\n\x16\x61gent_profile_group_id\x18\x01 \x01(\tR\x13\x61gentProfileGroupId\x12\x37\n\x18\x61gent_profile_group_name\x18\x02 \x01(\tR\x15\x61gentProfileGroupName\"\x8a\x01\n\x16ListPublicUsersRequest\x12!\n\x0c\x61gent_filter\x18\x01 \x01(\x08R\x0b\x61gentFilter\x12M\n\x0f\x61rchived_filter\x18\x02 \x01(\x0e\x32$.api.commons.UserArchivedStateFilterR\x0e\x61rchivedFilter\"\xd9\x02\n\x17ListPublicUsersResponse\x12\x1b\n\x07user_id\x18\x01 \x01(\tB\x02\x18\x01R\x06userId\x12!\n\nfirst_name\x18\x02 \x01(\tB\x02\x18\x01R\tfirstName\x12\x1f\n\tlast_name\x18\x03 \x01(\tB\x02\x18\x01R\x08lastName\x12\x1e\n\x08username\x18\x04 \x01(\tB\x02\x18\x01R\x08username\x12\x44\n\x05users\x18\x05 \x03(\x0b\x32..api.v1alpha1.org.ListPublicUsersResponse.UserR\x05users\x1aw\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastName\x12\x1a\n\x08username\x18\x04 \x01(\tR\x08username\"\x12\n\x10ListUsersRequest\"\xaf\x04\n\x11ListUsersResponse\x12\x45\n\x05users\x18\x01 \x03(\x0b\x32/.api.v1alpha1.org.ListUsersResponse.UserDetailsR\x05users\x1a\xd2\x03\n\x0bUserDetails\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1d\n\nfirst_name\x18\x03 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x04 \x01(\tR\x08lastName\x12\x1a\n\x08username\x18\x05 \x01(\tR\x08username\x12%\n\x0elogin_disabled\x18\x07 \x01(\x08R\rloginDisabled\x12\x30\n\x14permission_group_ids\x18\t \x03(\tR\x12permissionGroupIds\x12.\n\x06labels\x18\n \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12#\n\raccount_owner\x18\x0b \x01(\x08R\x0c\x61\x63\x63ountOwner\x12\x14\n\x05\x61gent\x18\x0c \x01(\x08R\x05\x61gent\x12\x1b\n\ttrust_ids\x18\r \x03(\tR\x08trustIds\x12\x33\n\x08mfa_info\x18\x0e \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x07mfaInfo\x12%\n\x0e\x65mail_verified\x18\x0f \x01(\x08R\remailVerified\"\x7f\n\x17ListUsersByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12M\n\x0f\x61rchived_filter\x18\x02 \x01(\x0e\x32$.api.commons.UserArchivedStateFilterR\x0e\x61rchivedFilter\"\xd8\x04\n\x18ListUsersByOrgIdResponse\x12L\n\x05users\x18\x01 \x03(\x0b\x32\x36.api.v1alpha1.org.ListUsersByOrgIdResponse.UserDetailsR\x05users\x1a\xed\x03\n\x0bUserDetails\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x19\n\x08org_name\x18\x03 \x01(\tR\x07orgName\x12\x1d\n\nfirst_name\x18\x04 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x05 \x01(\tR\x08lastName\x12\x1a\n\x08username\x18\x06 \x01(\tR\x08username\x12%\n\x0elogin_disabled\x18\x07 \x01(\x08R\rloginDisabled\x12\x30\n\x14permission_group_ids\x18\x08 \x03(\tR\x12permissionGroupIds\x12.\n\x06labels\x18\t \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12#\n\raccount_owner\x18\n \x01(\x08R\x0c\x61\x63\x63ountOwner\x12\x14\n\x05\x61gent\x18\x0b \x01(\x08R\x05\x61gent\x12\x1b\n\ttrust_ids\x18\x0c \x03(\tR\x08trustIds\x12\x33\n\x08mfa_info\x18\x0e \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x07mfaInfo\x12%\n\x0e\x65mail_verified\x18\x0f \x01(\x08R\remailVerified\"\x9c\x01\n\x18ListUsersByRegionRequest\x12\x1b\n\tregion_id\x18\x01 \x01(\tR\x08regionId\x12\x14\n\x05\x61gent\x18\x02 \x01(\x08R\x05\x61gent\x12M\n\x0f\x61rchived_filter\x18\x03 \x01(\x0e\x32$.api.commons.UserArchivedStateFilterR\x0e\x61rchivedFilter\"\xbf\x04\n\x19ListUsersByRegionResponse\x12M\n\x05users\x18\x01 \x03(\x0b\x32\x37.api.v1alpha1.org.ListUsersByRegionResponse.UserDetailsR\x05users\x1a\xd2\x03\n\x0bUserDetails\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1d\n\nfirst_name\x18\x03 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x04 \x01(\tR\x08lastName\x12\x1a\n\x08username\x18\x05 \x01(\tR\x08username\x12%\n\x0elogin_disabled\x18\x07 \x01(\x08R\rloginDisabled\x12\x30\n\x14permission_group_ids\x18\t \x03(\tR\x12permissionGroupIds\x12.\n\x06labels\x18\n \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12#\n\raccount_owner\x18\x0b \x01(\x08R\x0c\x61\x63\x63ountOwner\x12\x14\n\x05\x61gent\x18\x0c \x01(\x08R\x05\x61gent\x12\x1b\n\ttrust_ids\x18\r \x03(\tR\x08trustIds\x12\x33\n\x08mfa_info\x18\x0e \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x07mfaInfo\x12%\n\x0e\x65mail_verified\x18\x0f \x01(\x08R\remailVerified\"\x8e\x02\n\x13UpdateMyUserRequest\x12)\n\x10linkback_numbers\x18\x01 \x03(\tR\x0flinkbackNumbers\x12\x1d\n\ncaller_ids\x18\x02 \x03(\tR\tcallerIds\x12J\n\x12time_zone_override\x18\x03 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12\x42\n\x0b\x64\x65\x66\x61ult_app\x18\x04 \x01(\x0e\x32!.api.commons.OperatorApplicationsR\ndefaultApp\x12\x1d\n\nfield_mask\x18\n \x03(\tR\tfieldMask\"\x16\n\x14UpdateMyUserResponse\"\xed\x04\n\x11UpdateUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastName\x12(\n\x10partner_agent_id\x18\x04 \x01(\tR\x0epartnerAgentId\x12J\n\x12time_zone_override\x18\x05 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12)\n\x10linkback_numbers\x18\x06 \x03(\tR\x0flinkbackNumbers\x12\x1d\n\ncaller_ids\x18\x07 \x03(\tR\tcallerIds\x12\x42\n\x0b\x64\x65\x66\x61ult_app\x18\x08 \x01(\x0e\x32!.api.commons.OperatorApplicationsR\ndefaultApp\x12\x36\n\x17password_reset_required\x18\t \x01(\x08R\x15passwordResetRequired\x12\x33\n\x16\x61gent_profile_group_id\x18\n \x01(\tR\x13\x61gentProfileGroupId\x12\x1a\n\x08username\x18\x0b \x01(\tR\x08username\x12\x14\n\x05\x65mail\x18\x0c \x01(\tR\x05\x65mail\x12$\n\x0euser_caller_id\x18\r \x01(\tR\x0cuserCallerId\x12\x1b\n\tlabel_ids\x18\x0e \x03(\tR\x08labelIds\x12\x1d\n\nfield_mask\x18\x14 \x03(\tR\tfieldMask\"\x14\n\x12UpdateUserResponse\"f\n\x17UpdateUserLabelsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1b\n\tlabel_ids\x18\x03 \x03(\tR\x08labelIds\"\x1a\n\x18UpdateUserLabelsResponse\"Z\n\x19UpdateUserCallerIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12$\n\x0euser_caller_id\x18\x02 \x01(\tR\x0cuserCallerId\"\x1c\n\x1aUpdateUserCallerIdResponse\"[\n\x19UpdateUserDisabledRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12%\n\x0elogin_disabled\x18\x02 \x01(\x08R\rloginDisabled\"\x1c\n\x1aUpdateUserDisabledResponse\"y\n UpdateUserDisabledByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12%\n\x0elogin_disabled\x18\x03 \x01(\x08R\rloginDisabled\"#\n!UpdateUserDisabledByOrgIdResponse\"5\n!GetMyUserPasswordResetLinkRequest\x12\x10\n\x03ttl\x18\x01 \x01(\x03R\x03ttl\"6\n\"GetMyUserPasswordResetLinkResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"L\n\x1fGetUserPasswordResetLinkRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x10\n\x03ttl\x18\x02 \x01(\x03R\x03ttl\"4\n GetUserPasswordResetLinkResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"j\n&GetUserPasswordResetLinkByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x10\n\x03ttl\x18\x03 \x01(\x03R\x03ttl\";\n\'GetUserPasswordResetLinkByOrgIdResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"u\n\x1e\x43reatePasswordResetLinkRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12:\n\nexpiration\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nexpiration\"3\n\x1f\x43reatePasswordResetLinkResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"W\n%CreatePasswordResetLinkByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\":\n&CreatePasswordResetLinkByOrgIdResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"I\n\x17GetUserLoginInfoRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\"\x95\x03\n\x18GetUserLoginInfoResponse\x12\x18\n\x07\x62locked\x18\x01 \x01(\x08R\x07\x62locked\x12\x17\n\x07last_ip\x18\x02 \x01(\tR\x06lastIp\x12\x39\n\nlast_login\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tlastLogin\x12J\n\x13last_password_reset\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastPasswordReset\x12!\n\x0clogins_count\x18\x05 \x01(\x03R\x0bloginsCount\x12\x39\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x39\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tupdatedAt\x12&\n\x0fhas_blocked_ips\x18\x08 \x01(\x08R\rhasBlockedIps\"0\n\x18SendPasswordResetRequest\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\"\x1b\n\x19SendPasswordResetResponse\"N\n\x1fSendPasswordResetByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x14\n\x05\x65mail\x18\x02 \x01(\tR\x05\x65mail\"\"\n SendPasswordResetByOrgIdResponse\"4\n\x16ResetMyPasswordRequest\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"\x19\n\x17ResetMyPasswordResponse\"O\n\x18ResetUserPasswordRequest\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1b\n\x19ResetUserPasswordResponse\"m\n\x1fResetUserPasswordByOrgIdRequest\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x03 \x01(\tR\x05orgId\"\"\n ResetUserPasswordByOrgIdResponse\"6\n\x1bGetUserEmailVerifiedRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"E\n\x1cGetUserEmailVerifiedResponse\x12%\n\x0e\x65mail_verified\x18\x01 \x01(\x08R\remailVerified\"T\n\"GetUserEmailVerifiedByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\"L\n#GetUserEmailVerifiedByOrgIdResponse\x12%\n\x0e\x65mail_verified\x18\x01 \x01(\x08R\remailVerified\";\n SendUserEmailVerificationRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"#\n!SendUserEmailVerificationResponse\"Y\n\'SendUserEmailVerificationByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\"*\n(SendUserEmailVerificationByOrgIdResponse\"\x1b\n\x19GetUserSessionDataRequest\"\xe4\x0e\n\x1aGetUserSessionDataResponse\x12\x45\n\x04user\x18\x01 \x01(\x0b\x32\x31.api.v1alpha1.org.GetUserSessionDataResponse.UserR\x04user\x12\x19\n\x08org_name\x18\x02 \x01(\tR\x07orgName\x12>\n\x0ep3_permissions\x18\x03 \x03(\x0e\x32\x17.api.commons.PermissionR\rp3Permissions\x12M\n\x11permission_groups\x18\x04 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\x12.\n\x06labels\x18\x05 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12&\n\x0forg_allowed_mfa\x18\x06 \x01(\x08R\rorgAllowedMfa\x1a\xfc\x0b\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1a\n\x08username\x18\x03 \x01(\tR\x08username\x12\x33\n\x16p3_permission_group_id\x18\x04 \x01(\tR\x13p3PermissionGroupId\x12(\n\x10partner_agent_id\x18\x08 \x01(\tR\x0epartnerAgentId\x12i\n\x0eregion_sid_map\x18\n \x03(\x0b\x32\x43.api.v1alpha1.org.GetUserSessionDataResponse.User.RegionSidMapEntryR\x0cregionSidMap\x12%\n\x0e\x64\x65\x66\x61ult_region\x18\x0b \x01(\tR\rdefaultRegion\x12\x17\n\x07\x61pi_key\x18\x0c \x01(\tR\x06\x61piKey\x12\x14\n\x05\x65mail\x18\r \x01(\tR\x05\x65mail\x12%\n\x0elogin_disabled\x18\x0e \x01(\x08R\rloginDisabled\x12\x1d\n\ncaller_ids\x18\x0f \x03(\tR\tcallerIds\x12)\n\x10linkback_numbers\x18\x10 \x03(\tR\x0flinkbackNumbers\x12 \n\x0c\x61uth_user_id\x18\x11 \x01(\tR\nauthUserId\x12\x1d\n\nenable_mfa\x18\x12 \x01(\x08R\tenableMfa\x12\x1d\n\nfirst_name\x18\x13 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x14 \x01(\tR\x08lastName\x12\x34\n\x07\x63reated\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12=\n\x0clast_updated\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\x12\x36\n\x17password_reset_required\x18\x17 \x01(\x08R\x15passwordResetRequired\x12\x41\n\rconnection_id\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0c\x63onnectionId\x12J\n\x12time_zone_override\x18\x19 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12\x30\n\x14permission_group_ids\x18\x1a \x03(\tR\x12permissionGroupIds\x12\x1b\n\ttrust_ids\x18\x1b \x03(\tR\x08trustIds\x12R\n\x13\x64\x65\x66\x61ult_application\x18\x1c \x01(\x0e\x32!.api.commons.OperatorApplicationsR\x12\x64\x65\x66\x61ultApplication\x12$\n\x0euser_caller_id\x18\x1d \x01(\tR\x0cuserCallerId\x12\x33\n\x16\x61gent_profile_group_id\x18\x1e \x01(\tR\x13\x61gentProfileGroupId\x12\x14\n\x05\x61gent\x18\x1f \x01(\x08R\x05\x61gent\x12#\n\raccount_owner\x18  \x01(\x08R\x0c\x61\x63\x63ountOwner\x12?\n\rmfa_timestamp\x18! \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cmfaTimestamp\x1a\x65\n\nRegionSids\x12\x1b\n\tlogin_sid\x18\x01 \x01(\x03R\x08loginSid\x12\x1b\n\tagent_sid\x18\x02 \x01(\x03R\x08\x61gentSid\x12\x1d\n\nclient_sid\x18\x03 \x01(\x03R\tclientSid\x1a}\n\x11RegionSidMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12R\n\x05value\x18\x02 \x01(\x0b\x32<.api.v1alpha1.org.GetUserSessionDataResponse.User.RegionSidsR\x05value:\x02\x38\x01\"3\n\x18RefreshMfaLockoutRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"Q\n\x19RefreshMfaLockoutResponse\x12\x34\n\x07timeout\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07timeout\"Q\n\x1fRefreshMfaLockoutByOrgIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\"X\n RefreshMfaLockoutByOrgIdResponse\x12\x34\n\x07timeout\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07timeout\"[\n\x11SetMfaTypeRequest\x12,\n\x04info\x18\x03 \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x04infoJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x03otpR\x07user_id\"\x14\n\x12SetMfaTypeResponse\"N\n\x13SetMyMfaTypeRequest\x12,\n\x04info\x18\x02 \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x04infoJ\x04\x08\x01\x10\x02R\x03otp\"\x16\n\x14SetMyMfaTypeResponse\"I\n\x14\x45nableUserMfaRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x18\n\x07\x65nabled\x18\x02 \x01(\x08R\x07\x65nabled\"\x17\n\x15\x45nableUserMfaResponse\"\x18\n\x16\x45nableMyUserMfaRequest\"\x19\n\x17\x45nableMyUserMfaResponse\"0\n\x15GetUserMfaInfoRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"F\n\x16GetUserMfaInfoResponse\x12,\n\x04info\x18\x01 \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x04info\"\x19\n\x17GetMyUserMfaInfoRequest\"H\n\x18GetMyUserMfaInfoResponse\x12,\n\x04info\x18\x01 \x01(\x0b\x32\x18.api.commons.org.MfaInfoR\x04infoB\x83\x01\n\x14\x63om.api.v1alpha1.orgB\tUserProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\tUserProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['user_id']._options = None
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['user_id']._serialized_options = b'\030\001'
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['first_name']._options = None
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['first_name']._serialized_options = b'\030\001'
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['last_name']._options = None
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['last_name']._serialized_options = b'\030\001'
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['username']._options = None
  _globals['_LISTPUBLICUSERSRESPONSE'].fields_by_name['username']._serialized_options = b'\030\001'
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDMAPENTRY']._options = None
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDMAPENTRY']._serialized_options = b'8\001'
  _globals['_CREATEUSERREQUEST']._serialized_start=310
  _globals['_CREATEUSERREQUEST']._serialized_end=1012
  _globals['_CREATEUSERRESPONSE']._serialized_start=1014
  _globals['_CREATEUSERRESPONSE']._serialized_end=1059
  _globals['_CREATEDELEGATEDUSERREQUEST']._serialized_start=1062
  _globals['_CREATEDELEGATEDUSERREQUEST']._serialized_end=1318
  _globals['_CREATEDELEGATEDUSERRESPONSE']._serialized_start=1320
  _globals['_CREATEDELEGATEDUSERRESPONSE']._serialized_end=1374
  _globals['_GETMYUSERREQUEST']._serialized_start=1376
  _globals['_GETMYUSERREQUEST']._serialized_end=1394
  _globals['_GETMYUSERRESPONSE']._serialized_start=1397
  _globals['_GETMYUSERRESPONSE']._serialized_end=2336
  _globals['_GETMYUSERRESPONSE_HUNTGROUP']._serialized_start=2115
  _globals['_GETMYUSERRESPONSE_HUNTGROUP']._serialized_end=2204
  _globals['_GETMYUSERRESPONSE_AGENTPROFILEGROUP']._serialized_start=2207
  _globals['_GETMYUSERRESPONSE_AGENTPROFILEGROUP']._serialized_end=2336
  _globals['_GETUSERREQUEST']._serialized_start=2338
  _globals['_GETUSERREQUEST']._serialized_end=2379
  _globals['_GETUSERRESPONSE']._serialized_start=2382
  _globals['_GETUSERRESPONSE']._serialized_end=4009
  _globals['_GETUSERRESPONSE_HUNTGROUP']._serialized_start=2115
  _globals['_GETUSERRESPONSE_HUNTGROUP']._serialized_end=2204
  _globals['_GETUSERRESPONSE_AGENTPROFILEGROUP']._serialized_start=2207
  _globals['_GETUSERRESPONSE_AGENTPROFILEGROUP']._serialized_end=2336
  _globals['_GETUSERBYORGIDREQUEST']._serialized_start=4011
  _globals['_GETUSERBYORGIDREQUEST']._serialized_end=4082
  _globals['_GETUSERBYORGIDRESPONSE']._serialized_start=4085
  _globals['_GETUSERBYORGIDRESPONSE']._serialized_end=5039
  _globals['_GETUSERBYORGIDRESPONSE_HUNTGROUP']._serialized_start=2115
  _globals['_GETUSERBYORGIDRESPONSE_HUNTGROUP']._serialized_end=2204
  _globals['_GETUSERBYORGIDRESPONSE_AGENTPROFILEGROUP']._serialized_start=2207
  _globals['_GETUSERBYORGIDRESPONSE_AGENTPROFILEGROUP']._serialized_end=2336
  _globals['_LISTAGENTSREQUEST']._serialized_start=5041
  _globals['_LISTAGENTSREQUEST']._serialized_end=5060
  _globals['_LISTAGENTSRESPONSE']._serialized_start=5063
  _globals['_LISTAGENTSRESPONSE']._serialized_end=6474
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS']._serialized_start=5161
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS']._serialized_end=6474
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS_HUNTGROUP']._serialized_start=2115
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS_HUNTGROUP']._serialized_end=2204
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS_AGENTPROFILEGROUP']._serialized_start=2207
  _globals['_LISTAGENTSRESPONSE_AGENTDETAILS_AGENTPROFILEGROUP']._serialized_end=2336
  _globals['_LISTPUBLICUSERSREQUEST']._serialized_start=6477
  _globals['_LISTPUBLICUSERSREQUEST']._serialized_end=6615
  _globals['_LISTPUBLICUSERSRESPONSE']._serialized_start=6618
  _globals['_LISTPUBLICUSERSRESPONSE']._serialized_end=6963
  _globals['_LISTPUBLICUSERSRESPONSE_USER']._serialized_start=6844
  _globals['_LISTPUBLICUSERSRESPONSE_USER']._serialized_end=6963
  _globals['_LISTUSERSREQUEST']._serialized_start=6965
  _globals['_LISTUSERSREQUEST']._serialized_end=6983
  _globals['_LISTUSERSRESPONSE']._serialized_start=6986
  _globals['_LISTUSERSRESPONSE']._serialized_end=7545
  _globals['_LISTUSERSRESPONSE_USERDETAILS']._serialized_start=7079
  _globals['_LISTUSERSRESPONSE_USERDETAILS']._serialized_end=7545
  _globals['_LISTUSERSBYORGIDREQUEST']._serialized_start=7547
  _globals['_LISTUSERSBYORGIDREQUEST']._serialized_end=7674
  _globals['_LISTUSERSBYORGIDRESPONSE']._serialized_start=7677
  _globals['_LISTUSERSBYORGIDRESPONSE']._serialized_end=8277
  _globals['_LISTUSERSBYORGIDRESPONSE_USERDETAILS']._serialized_start=7784
  _globals['_LISTUSERSBYORGIDRESPONSE_USERDETAILS']._serialized_end=8277
  _globals['_LISTUSERSBYREGIONREQUEST']._serialized_start=8280
  _globals['_LISTUSERSBYREGIONREQUEST']._serialized_end=8436
  _globals['_LISTUSERSBYREGIONRESPONSE']._serialized_start=8439
  _globals['_LISTUSERSBYREGIONRESPONSE']._serialized_end=9014
  _globals['_LISTUSERSBYREGIONRESPONSE_USERDETAILS']._serialized_start=7079
  _globals['_LISTUSERSBYREGIONRESPONSE_USERDETAILS']._serialized_end=7545
  _globals['_UPDATEMYUSERREQUEST']._serialized_start=9017
  _globals['_UPDATEMYUSERREQUEST']._serialized_end=9287
  _globals['_UPDATEMYUSERRESPONSE']._serialized_start=9289
  _globals['_UPDATEMYUSERRESPONSE']._serialized_end=9311
  _globals['_UPDATEUSERREQUEST']._serialized_start=9314
  _globals['_UPDATEUSERREQUEST']._serialized_end=9935
  _globals['_UPDATEUSERRESPONSE']._serialized_start=9937
  _globals['_UPDATEUSERRESPONSE']._serialized_end=9957
  _globals['_UPDATEUSERLABELSREQUEST']._serialized_start=9959
  _globals['_UPDATEUSERLABELSREQUEST']._serialized_end=10061
  _globals['_UPDATEUSERLABELSRESPONSE']._serialized_start=10063
  _globals['_UPDATEUSERLABELSRESPONSE']._serialized_end=10089
  _globals['_UPDATEUSERCALLERIDREQUEST']._serialized_start=10091
  _globals['_UPDATEUSERCALLERIDREQUEST']._serialized_end=10181
  _globals['_UPDATEUSERCALLERIDRESPONSE']._serialized_start=10183
  _globals['_UPDATEUSERCALLERIDRESPONSE']._serialized_end=10211
  _globals['_UPDATEUSERDISABLEDREQUEST']._serialized_start=10213
  _globals['_UPDATEUSERDISABLEDREQUEST']._serialized_end=10304
  _globals['_UPDATEUSERDISABLEDRESPONSE']._serialized_start=10306
  _globals['_UPDATEUSERDISABLEDRESPONSE']._serialized_end=10334
  _globals['_UPDATEUSERDISABLEDBYORGIDREQUEST']._serialized_start=10336
  _globals['_UPDATEUSERDISABLEDBYORGIDREQUEST']._serialized_end=10457
  _globals['_UPDATEUSERDISABLEDBYORGIDRESPONSE']._serialized_start=10459
  _globals['_UPDATEUSERDISABLEDBYORGIDRESPONSE']._serialized_end=10494
  _globals['_GETMYUSERPASSWORDRESETLINKREQUEST']._serialized_start=10496
  _globals['_GETMYUSERPASSWORDRESETLINKREQUEST']._serialized_end=10549
  _globals['_GETMYUSERPASSWORDRESETLINKRESPONSE']._serialized_start=10551
  _globals['_GETMYUSERPASSWORDRESETLINKRESPONSE']._serialized_end=10605
  _globals['_GETUSERPASSWORDRESETLINKREQUEST']._serialized_start=10607
  _globals['_GETUSERPASSWORDRESETLINKREQUEST']._serialized_end=10683
  _globals['_GETUSERPASSWORDRESETLINKRESPONSE']._serialized_start=10685
  _globals['_GETUSERPASSWORDRESETLINKRESPONSE']._serialized_end=10737
  _globals['_GETUSERPASSWORDRESETLINKBYORGIDREQUEST']._serialized_start=10739
  _globals['_GETUSERPASSWORDRESETLINKBYORGIDREQUEST']._serialized_end=10845
  _globals['_GETUSERPASSWORDRESETLINKBYORGIDRESPONSE']._serialized_start=10847
  _globals['_GETUSERPASSWORDRESETLINKBYORGIDRESPONSE']._serialized_end=10906
  _globals['_CREATEPASSWORDRESETLINKREQUEST']._serialized_start=10908
  _globals['_CREATEPASSWORDRESETLINKREQUEST']._serialized_end=11025
  _globals['_CREATEPASSWORDRESETLINKRESPONSE']._serialized_start=11027
  _globals['_CREATEPASSWORDRESETLINKRESPONSE']._serialized_end=11078
  _globals['_CREATEPASSWORDRESETLINKBYORGIDREQUEST']._serialized_start=11080
  _globals['_CREATEPASSWORDRESETLINKBYORGIDREQUEST']._serialized_end=11167
  _globals['_CREATEPASSWORDRESETLINKBYORGIDRESPONSE']._serialized_start=11169
  _globals['_CREATEPASSWORDRESETLINKBYORGIDRESPONSE']._serialized_end=11227
  _globals['_GETUSERLOGININFOREQUEST']._serialized_start=11229
  _globals['_GETUSERLOGININFOREQUEST']._serialized_end=11302
  _globals['_GETUSERLOGININFORESPONSE']._serialized_start=11305
  _globals['_GETUSERLOGININFORESPONSE']._serialized_end=11710
  _globals['_SENDPASSWORDRESETREQUEST']._serialized_start=11712
  _globals['_SENDPASSWORDRESETREQUEST']._serialized_end=11760
  _globals['_SENDPASSWORDRESETRESPONSE']._serialized_start=11762
  _globals['_SENDPASSWORDRESETRESPONSE']._serialized_end=11789
  _globals['_SENDPASSWORDRESETBYORGIDREQUEST']._serialized_start=11791
  _globals['_SENDPASSWORDRESETBYORGIDREQUEST']._serialized_end=11869
  _globals['_SENDPASSWORDRESETBYORGIDRESPONSE']._serialized_start=11871
  _globals['_SENDPASSWORDRESETBYORGIDRESPONSE']._serialized_end=11905
  _globals['_RESETMYPASSWORDREQUEST']._serialized_start=11907
  _globals['_RESETMYPASSWORDREQUEST']._serialized_end=11959
  _globals['_RESETMYPASSWORDRESPONSE']._serialized_start=11961
  _globals['_RESETMYPASSWORDRESPONSE']._serialized_end=11986
  _globals['_RESETUSERPASSWORDREQUEST']._serialized_start=11988
  _globals['_RESETUSERPASSWORDREQUEST']._serialized_end=12067
  _globals['_RESETUSERPASSWORDRESPONSE']._serialized_start=12069
  _globals['_RESETUSERPASSWORDRESPONSE']._serialized_end=12096
  _globals['_RESETUSERPASSWORDBYORGIDREQUEST']._serialized_start=12098
  _globals['_RESETUSERPASSWORDBYORGIDREQUEST']._serialized_end=12207
  _globals['_RESETUSERPASSWORDBYORGIDRESPONSE']._serialized_start=12209
  _globals['_RESETUSERPASSWORDBYORGIDRESPONSE']._serialized_end=12243
  _globals['_GETUSEREMAILVERIFIEDREQUEST']._serialized_start=12245
  _globals['_GETUSEREMAILVERIFIEDREQUEST']._serialized_end=12299
  _globals['_GETUSEREMAILVERIFIEDRESPONSE']._serialized_start=12301
  _globals['_GETUSEREMAILVERIFIEDRESPONSE']._serialized_end=12370
  _globals['_GETUSEREMAILVERIFIEDBYORGIDREQUEST']._serialized_start=12372
  _globals['_GETUSEREMAILVERIFIEDBYORGIDREQUEST']._serialized_end=12456
  _globals['_GETUSEREMAILVERIFIEDBYORGIDRESPONSE']._serialized_start=12458
  _globals['_GETUSEREMAILVERIFIEDBYORGIDRESPONSE']._serialized_end=12534
  _globals['_SENDUSEREMAILVERIFICATIONREQUEST']._serialized_start=12536
  _globals['_SENDUSEREMAILVERIFICATIONREQUEST']._serialized_end=12595
  _globals['_SENDUSEREMAILVERIFICATIONRESPONSE']._serialized_start=12597
  _globals['_SENDUSEREMAILVERIFICATIONRESPONSE']._serialized_end=12632
  _globals['_SENDUSEREMAILVERIFICATIONBYORGIDREQUEST']._serialized_start=12634
  _globals['_SENDUSEREMAILVERIFICATIONBYORGIDREQUEST']._serialized_end=12723
  _globals['_SENDUSEREMAILVERIFICATIONBYORGIDRESPONSE']._serialized_start=12725
  _globals['_SENDUSEREMAILVERIFICATIONBYORGIDRESPONSE']._serialized_end=12767
  _globals['_GETUSERSESSIONDATAREQUEST']._serialized_start=12769
  _globals['_GETUSERSESSIONDATAREQUEST']._serialized_end=12796
  _globals['_GETUSERSESSIONDATARESPONSE']._serialized_start=12799
  _globals['_GETUSERSESSIONDATARESPONSE']._serialized_end=14691
  _globals['_GETUSERSESSIONDATARESPONSE_USER']._serialized_start=13159
  _globals['_GETUSERSESSIONDATARESPONSE_USER']._serialized_end=14691
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDS']._serialized_start=14463
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDS']._serialized_end=14564
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDMAPENTRY']._serialized_start=14566
  _globals['_GETUSERSESSIONDATARESPONSE_USER_REGIONSIDMAPENTRY']._serialized_end=14691
  _globals['_REFRESHMFALOCKOUTREQUEST']._serialized_start=14693
  _globals['_REFRESHMFALOCKOUTREQUEST']._serialized_end=14744
  _globals['_REFRESHMFALOCKOUTRESPONSE']._serialized_start=14746
  _globals['_REFRESHMFALOCKOUTRESPONSE']._serialized_end=14827
  _globals['_REFRESHMFALOCKOUTBYORGIDREQUEST']._serialized_start=14829
  _globals['_REFRESHMFALOCKOUTBYORGIDREQUEST']._serialized_end=14910
  _globals['_REFRESHMFALOCKOUTBYORGIDRESPONSE']._serialized_start=14912
  _globals['_REFRESHMFALOCKOUTBYORGIDRESPONSE']._serialized_end=15000
  _globals['_SETMFATYPEREQUEST']._serialized_start=15002
  _globals['_SETMFATYPEREQUEST']._serialized_end=15093
  _globals['_SETMFATYPERESPONSE']._serialized_start=15095
  _globals['_SETMFATYPERESPONSE']._serialized_end=15115
  _globals['_SETMYMFATYPEREQUEST']._serialized_start=15117
  _globals['_SETMYMFATYPEREQUEST']._serialized_end=15195
  _globals['_SETMYMFATYPERESPONSE']._serialized_start=15197
  _globals['_SETMYMFATYPERESPONSE']._serialized_end=15219
  _globals['_ENABLEUSERMFAREQUEST']._serialized_start=15221
  _globals['_ENABLEUSERMFAREQUEST']._serialized_end=15294
  _globals['_ENABLEUSERMFARESPONSE']._serialized_start=15296
  _globals['_ENABLEUSERMFARESPONSE']._serialized_end=15319
  _globals['_ENABLEMYUSERMFAREQUEST']._serialized_start=15321
  _globals['_ENABLEMYUSERMFAREQUEST']._serialized_end=15345
  _globals['_ENABLEMYUSERMFARESPONSE']._serialized_start=15347
  _globals['_ENABLEMYUSERMFARESPONSE']._serialized_end=15372
  _globals['_GETUSERMFAINFOREQUEST']._serialized_start=15374
  _globals['_GETUSERMFAINFOREQUEST']._serialized_end=15422
  _globals['_GETUSERMFAINFORESPONSE']._serialized_start=15424
  _globals['_GETUSERMFAINFORESPONSE']._serialized_end=15494
  _globals['_GETMYUSERMFAINFOREQUEST']._serialized_start=15496
  _globals['_GETMYUSERMFAINFOREQUEST']._serialized_end=15521
  _globals['_GETMYUSERMFAINFORESPONSE']._serialized_start=15523
  _globals['_GETMYUSERMFAINFORESPONSE']._serialized_end=15595
# @@protoc_insertion_point(module_scope)
