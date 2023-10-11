# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/org/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x61pi/commons/org/user.proto\x12\x0f\x61pi.commons.org\x1a\x15\x61pi/commons/org.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xb9\x0c\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1a\n\x08username\x18\x03 \x01(\tR\x08username\x12\x33\n\x16p3_permission_group_id\x18\x04 \x01(\tR\x13p3PermissionGroupId\x12\x1b\n\tlogin_sid\x18\x05 \x01(\x03R\x08loginSid\x12\x1b\n\tagent_sid\x18\x06 \x01(\x03R\x08\x61gentSid\x12\x1b\n\tregion_id\x18\x07 \x01(\tR\x08regionId\x12(\n\x10partner_agent_id\x18\x08 \x01(\tR\x0epartnerAgentId\x12\x1d\n\nclient_sid\x18\x0b \x01(\x03R\tclientSid\x12M\n\x0eregion_sid_map\x18\x0f \x03(\x0b\x32\'.api.commons.org.User.RegionSidMapEntryR\x0cregionSidMap\x12\x17\n\x07\x61pi_key\x18\x65 \x01(\tR\x06\x61piKey\x12\x14\n\x05\x65mail\x18h \x01(\tR\x05\x65mail\x12%\n\x0elogin_disabled\x18p \x01(\x08R\rloginDisabled\x12\x1d\n\ncaller_ids\x18s \x03(\tR\tcallerIds\x12)\n\x10linkback_numbers\x18t \x03(\tR\x0flinkbackNumbers\x12 \n\x0c\x61uth_user_id\x18v \x01(\tR\nauthUserId\x12\x1d\n\nenable_mfa\x18{ \x01(\x08R\tenableMfa\x12\x1e\n\nfirst_name\x18\xa1\x01 \x01(\tR\tfirstName\x12\x1c\n\tlast_name\x18\xa2\x01 \x01(\tR\x08lastName\x12\x35\n\x07\x63reated\x18\xa3\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12>\n\x0clast_updated\x18\xa4\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\x12\x37\n\x17password_reset_required\x18\xa5\x01 \x01(\x08R\x15passwordResetRequired\x12\x42\n\rconnection_id\x18\xa6\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0c\x63onnectionId\x12K\n\x12time_zone_override\x18\xa7\x01 \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x10timeZoneOverride\x12\x31\n\x14permission_group_ids\x18\xc8\x01 \x03(\tR\x12permissionGroupIds\x12\x1c\n\ttrust_ids\x18\xd1\x01 \x03(\tR\x08trustIds\x12&\n\x0e\x64\x65\x66\x61ult_region\x18\xca\x01 \x01(\tR\rdefaultRegion\x12S\n\x13\x64\x65\x66\x61ult_application\x18\xcb\x01 \x01(\x0e\x32!.api.commons.OperatorApplicationsR\x12\x64\x65\x66\x61ultApplication\x12%\n\x0euser_caller_id\x18\xcd\x01 \x01(\tR\x0cuserCallerId\x12\x34\n\x16\x61gent_profile_group_id\x18\xcf\x01 \x01(\tR\x13\x61gentProfileGroupId\x12/\n\x06skills\x18\xd0\x01 \x03(\x0b\x32\x16.api.commons.org.SkillR\x06skills\x12\x15\n\x05\x61gent\x18\xac\x02 \x01(\x08R\x05\x61gent\x12$\n\raccount_owner\x18\x90\x03 \x01(\x08R\x0c\x61\x63\x63ountOwner\x1a\x61\n\x11RegionSidMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32 .api.commons.org.User.RegionSidsR\x05value:\x02\x38\x01\x1a\x65\n\nRegionSids\x12\x1b\n\tlogin_sid\x18\x01 \x01(\x03R\x08loginSid\x12\x1b\n\tagent_sid\x18\x02 \x01(\x03R\x08\x61gentSid\x12\x1d\n\nclient_sid\x18\x03 \x01(\x03R\tclientSid\"p\n\x05Skill\x12\x14\n\x05level\x18\x01 \x01(\x03R\x05level\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1b\n\tskill_sid\x18\x04 \x01(\x03R\x08skillSidB~\n\x13\x63om.api.commons.orgB\tUserProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\tUserProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_USER_REGIONSIDMAPENTRY']._options = None
  _globals['_USER_REGIONSIDMAPENTRY']._serialized_options = b'8\001'
  _globals['_USER']._serialized_start=136
  _globals['_USER']._serialized_end=1729
  _globals['_USER_REGIONSIDMAPENTRY']._serialized_start=1529
  _globals['_USER_REGIONSIDMAPENTRY']._serialized_end=1626
  _globals['_USER_REGIONSIDS']._serialized_start=1628
  _globals['_USER_REGIONSIDS']._serialized_end=1729
  _globals['_SKILL']._serialized_start=1731
  _globals['_SKILL']._serialized_end=1843
# @@protoc_insertion_point(module_scope)
