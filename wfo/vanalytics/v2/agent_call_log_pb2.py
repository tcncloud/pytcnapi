# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/agent_call_log.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'wfo/vanalytics/v2/agent_call_log.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&wfo/vanalytics/v2/agent_call_log.proto\x12\x11wfo.vanalytics.v2\x1a\x15\x61pi/commons/acd.proto\"\xa6\x02\n\x0c\x41gentCallLog\x12@\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32&.wfo.vanalytics.v2.AgentCallLog.ActionR\x07\x61\x63tions\x1a\x96\x01\n\x06\x41\x63tion\x12\x63\n\x13\x63\x61ll_skills_initial\x18\x01 \x01(\x0b\x32\x31.wfo.vanalytics.v2.AgentCallLog.CallSkillsInitialH\x00R\x11\x63\x61llSkillsInitial\x12\x1f\n\ncall_ended\x18\x02 \x01(\tH\x00R\tcallEndedB\x06\n\x04kind\x1a;\n\x11\x43\x61llSkillsInitial\x12\x12\n\x04need\x18\x01 \x03(\tR\x04need\x12\x12\n\x04want\x18\x02 \x03(\tR\x04want\"\xb1\x04\n\x11\x41gentCallLogQuery\x12\x66\n\x13\x63\x61ll_skills_initial\x18\x01 \x01(\x0b\x32\x36.wfo.vanalytics.v2.AgentCallLogQuery.CallSkillsInitialR\x11\x63\x61llSkillsInitial\x12M\n\ncall_ended\x18\x02 \x01(\x0b\x32..wfo.vanalytics.v2.AgentCallLogQuery.CallEndedR\tcallEnded\x1a\x99\x02\n\x11\x43\x61llSkillsInitial\x12O\n\x04need\x18\x01 \x01(\x0b\x32;.wfo.vanalytics.v2.AgentCallLogQuery.CallSkillsInitial.NeedR\x04need\x12O\n\x04want\x18\x02 \x01(\x0b\x32;.wfo.vanalytics.v2.AgentCallLogQuery.CallSkillsInitial.WantR\x04want\x1a\x30\n\x04Need\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values\x12\x10\n\x03\x61ll\x18\x02 \x01(\x08R\x03\x61ll\x1a\x30\n\x04Want\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values\x12\x10\n\x03\x61ll\x18\x02 \x01(\x08R\x03\x61ll\x1aI\n\tCallEnded\x12<\n\x07reasons\x18\x01 \x03(\x0e\x32\".api.commons.AgentCallLogCallEndedR\x07reasonsB\x90\x01\n\x15\x63om.wfo.vanalytics.v2B\x11\x41gentCallLogProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.agent_call_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\021AgentCallLogProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_AGENTCALLLOG']._serialized_start=85
  _globals['_AGENTCALLLOG']._serialized_end=379
  _globals['_AGENTCALLLOG_ACTION']._serialized_start=168
  _globals['_AGENTCALLLOG_ACTION']._serialized_end=318
  _globals['_AGENTCALLLOG_CALLSKILLSINITIAL']._serialized_start=320
  _globals['_AGENTCALLLOG_CALLSKILLSINITIAL']._serialized_end=379
  _globals['_AGENTCALLLOGQUERY']._serialized_start=382
  _globals['_AGENTCALLLOGQUERY']._serialized_end=943
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL']._serialized_start=587
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL']._serialized_end=868
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL_NEED']._serialized_start=770
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL_NEED']._serialized_end=818
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL_WANT']._serialized_start=820
  _globals['_AGENTCALLLOGQUERY_CALLSKILLSINITIAL_WANT']._serialized_end=868
  _globals['_AGENTCALLLOGQUERY_CALLENDED']._serialized_start=870
  _globals['_AGENTCALLLOGQUERY_CALLENDED']._serialized_end=943
# @@protoc_insertion_point(module_scope)
