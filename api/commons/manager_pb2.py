# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/manager.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'api/commons/manager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/manager.proto\x12\x0b\x61pi.commons*\xa2\x02\n\tAgentInfo\x12\x1c\n\x18\x41GENT_INFO_ACTIVE_AGENTS\x10\x00\x12#\n\x1f\x41GENT_INFO_IN_CONFERENCE_AGENTS\x10\x01\x12\x1c\n\x18\x41GENT_INFO_MANUAL_AGENTS\x10\x02\x12\x1c\n\x18\x41GENT_INFO_PAUSED_AGENTS\x10\x03\x12\x1d\n\x19\x41GENT_INFO_PREVIEW_AGENTS\x10\x04\x12\x1b\n\x17\x41GENT_INFO_READY_AGENTS\x10\x05\x12\x1b\n\x17\x41GENT_INFO_TOTAL_AGENTS\x10\x06\x12\x1e\n\x1a\x41GENT_INFO_TRANSFER_AGENTS\x10\x07\x12\x1d\n\x19\x41GENT_INFO_WRAP_UP_AGENTS\x10\x08*\xf6\x05\n\nSkillStats\x12\"\n\x1eSKILL_STATS_AGENT_PEERED_CALLS\x10\x00\x12\x1e\n\x1aSKILL_STATS_AVERAGE_LENGTH\x10\x01\x12\x1a\n\x16SKILL_STATS_CALL_COUNT\x10\x02\x12\x1e\n\x1aSKILL_STATS_CALL_SKILL_MAP\x10\x03\x12\x19\n\x15SKILL_STATS_CALL_TYPE\x10\x04\x12\x1a\n\x16SKILL_STATS_CALLS_LIST\x10\x05\x12#\n\x1fSKILL_STATS_DAILY_BY_SKILLS_KEY\x10\x06\x12 \n\x1cSKILL_STATS_LONGEST_IN_QUEUE\x10\x07\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_MD\x10\x08\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_PC\x10\t\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_LI\x10\n\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_OC\x10\x0b\x12!\n\x1dSKILL_STATS_MATCHING_AGENTS_P\x10\x0c\x12!\n\x1dSKILL_STATS_MATCHING_AGENTS_W\x10\r\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_WU\x10\x0e\x12\"\n\x1eSKILL_STATS_MATCHING_AGENTS_TC\x10\x0f\x12\x1e\n\x1aSKILL_STATS_MAXIMUM_LENGTH\x10\x10\x12\x1e\n\x1aSKILL_STATS_MINIMUM_LENGTH\x10\x11\x12\x1d\n\x19SKILL_STATS_PBX_EXTENSION\x10\x12\x12(\n$SKILL_STATS_QUEUED_NOTIFICATION_TYPE\x10\x13\x12\x19\n\x15SKILL_STATS_SKILL_SET\x10\x14\x12(\n$SKILL_STATS_TOTAL_LENGTH_FOR_AVERAGE\x10\x15*\xc3\x01\n\x0bSkillQueues\x12\x1a\n\x16SKILL_QUEUES_ACD_QUEUE\x10\x00\x12\x1b\n\x17SKILL_QUEUES_MULTI_HOLD\x10\x01\x12\x1c\n\x18SKILL_QUEUES_SIMPLE_HOLD\x10\x02\x12\x19\n\x15SKILL_QUEUES_TRANSFER\x10\x03\x12#\n\x1fSKILL_QUEUES_SUSPENDED_CALLBACK\x10\x04\x12\x1d\n\x19SKILL_QUEUES_GRAND_TOTALS\x10\x05*\xe2\x03\n\nAgentStats\x12\x1a\n\x16\x41GENT_STATS_AGENT_NAME\x10\x00\x12\x1c\n\x18\x41GENT_STATS_AGENT_STATUS\x10\x01\x12\"\n\x1e\x41GENT_STATS_DURATION_IN_STATUS\x10\x02\x12\x1f\n\x1b\x41GENT_STATS_LOGIN_DATE_TIME\x10\x03\x12\x1e\n\x1a\x41GENT_STATS_LOGIN_DURATION\x10\x04\x12\x1c\n\x18\x41GENT_STATS_AGENT_SKILLS\x10\x05\x12\x19\n\x15\x41GENT_STATS_AGENT_SID\x10\x06\x12\x1a\n\x16\x41GENT_STATS_SESSION_ID\x10\x07\x12\x1f\n\x1b\x41GENT_STATS_HUNT_GROUP_NAME\x10\x08\x12\x1a\n\x16\x41GENT_STATS_CALL_COUNT\x10\t\x12\x1a\n\x16\x41GENT_STATS_PAUSE_CODE\x10\n\x12 \n\x1c\x41GENT_STATS_RECORDING_STATUS\x10\x0b\x12 \n\x1c\x41GENT_STATS_MULTI_HOLD_COUNT\x10\x0c\x12!\n\x1d\x41GENT_STATS_SIMPLE_HOLD_COUNT\x10\r\x12 \n\x1c\x41GENT_STATS_TOTAL_HOLD_COUNT\x10\x0e*I\n\x12ManagerBargeInMode\x12\x0b\n\x07MONITOR\x10\x00\x12\x13\n\x0f\x46ULL_CONFERENCE\x10\x01\x12\x11\n\rAGENT_WHISPER\x10\x02\x42l\n\x0f\x63om.api.commonsB\x0cManagerProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.manager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014ManagerProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_AGENTINFO']._serialized_start=43
  _globals['_AGENTINFO']._serialized_end=333
  _globals['_SKILLSTATS']._serialized_start=336
  _globals['_SKILLSTATS']._serialized_end=1094
  _globals['_SKILLQUEUES']._serialized_start=1097
  _globals['_SKILLQUEUES']._serialized_end=1292
  _globals['_AGENTSTATS']._serialized_start=1295
  _globals['_AGENTSTATS']._serialized_end=1777
  _globals['_MANAGERBARGEINMODE']._serialized_start=1779
  _globals['_MANAGERBARGEINMODE']._serialized_end=1852
# @@protoc_insertion_point(module_scope)
