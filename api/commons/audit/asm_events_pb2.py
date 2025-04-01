# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/asm_events.proto
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
    'api/commons/audit/asm_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import asm_pb2 as api_dot_commons_dot_asm__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/commons/audit/asm_events.proto\x12\x11\x61pi.commons.audit\x1a\x15\x61pi/commons/asm.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"U\n\x12\x41smAgentLoginEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\"\x80\x01\n\x11\x41smOpenVoiceEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\x12*\n\x11voice_session_sid\x18\x03 \x01(\x03R\x0fvoiceSessionSid\"X\n\x15\x41smOpenOmniAgentEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\"\xa2\x01\n\x1c\x41smActivateConversationEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xa4\x01\n\x1e\x41smDeactivateConversationEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\x97\x02\n\x19\x41smAgentStateChangedEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\x12\x37\n\nnew_status\x18\x03 \x01(\x0e\x32\x18.api.commons.StatusStateR\tnewStatus\x12\x37\n\nold_status\x18\x04 \x01(\x0e\x32\x18.api.commons.StatusStateR\toldStatus\x12G\n old_status_duration_milliseconds\x18\x05 \x01(\x03R\x1doldStatusDurationMilliseconds\"n\n\x13\x41smAgentLogoutEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\x12\x16\n\x06reason\x18\x03 \x01(\tR\x06reason\"P\n\rAsmPauseEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\"Q\n\x0e\x41smResumeEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03R\rasmSessionSid\"_\n\x1a\x41smConversationPulledEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversationB\x8d\x01\n\x15\x63om.api.commons.auditB\x0e\x41smEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.asm_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\016AsmEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_ASMAGENTLOGINEVENT']._serialized_start=144
  _globals['_ASMAGENTLOGINEVENT']._serialized_end=229
  _globals['_ASMOPENVOICEEVENT']._serialized_start=232
  _globals['_ASMOPENVOICEEVENT']._serialized_end=360
  _globals['_ASMOPENOMNIAGENTEVENT']._serialized_start=362
  _globals['_ASMOPENOMNIAGENTEVENT']._serialized_end=450
  _globals['_ASMACTIVATECONVERSATIONEVENT']._serialized_start=453
  _globals['_ASMACTIVATECONVERSATIONEVENT']._serialized_end=615
  _globals['_ASMDEACTIVATECONVERSATIONEVENT']._serialized_start=618
  _globals['_ASMDEACTIVATECONVERSATIONEVENT']._serialized_end=782
  _globals['_ASMAGENTSTATECHANGEDEVENT']._serialized_start=785
  _globals['_ASMAGENTSTATECHANGEDEVENT']._serialized_end=1064
  _globals['_ASMAGENTLOGOUTEVENT']._serialized_start=1066
  _globals['_ASMAGENTLOGOUTEVENT']._serialized_end=1176
  _globals['_ASMPAUSEEVENT']._serialized_start=1178
  _globals['_ASMPAUSEEVENT']._serialized_end=1258
  _globals['_ASMRESUMEEVENT']._serialized_start=1260
  _globals['_ASMRESUMEEVENT']._serialized_end=1341
  _globals['_ASMCONVERSATIONPULLEDEVENT']._serialized_start=1343
  _globals['_ASMCONVERSATIONPULLEDEVENT']._serialized_end=1438
# @@protoc_insertion_point(module_scope)
