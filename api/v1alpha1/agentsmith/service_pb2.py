# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/agentsmith/service.proto
# Protobuf Python Version: 5.28.0
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
    0,
    '',
    'api/v1alpha1/agentsmith/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/agentsmith/service.proto\x12\x17\x61pi.v1alpha1.agentsmith\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"[\n\x0e\x46ollowAgentReq\x12\x19\n\x07user_id\x18\x01 \x01(\tH\x00R\x06userId\x12(\n\x0f\x61sm_session_sid\x18\x02 \x01(\x03H\x00R\rasmSessionSidB\x04\n\x02id\"\xb6\x03\n\x0e\x46ollowAgentRes\x12*\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02ts\x12^\n\x12\x61gent_state_change\x18\n \x01(\x0b\x32..api.v1alpha1.agentsmith.AgentStateChangeEventH\x00R\x10\x61gentStateChange\x12[\n\x11\x61gent_voice_start\x18\x0b \x01(\x0b\x32-.api.v1alpha1.agentsmith.AgentVoiceStartEventH\x00R\x0f\x61gentVoiceStart\x12U\n\x0f\x61gent_voice_end\x18\x0c \x01(\x0b\x32+.api.v1alpha1.agentsmith.AgentVoiceEndEventH\x00R\ragentVoiceEnd\x12[\n\x11\x61gent_session_end\x18\r \x01(\x0b\x32-.api.v1alpha1.agentsmith.AgentSessionEndEventH\x00R\x0f\x61gentSessionEndB\x07\n\x05\x65vent\"\xe9\x01\n\x15\x41gentStateChangeEvent\x12@\n\told_state\x18\x01 \x01(\x0e\x32#.api.v1alpha1.agentsmith.AgentStateR\x08oldState\x12@\n\tnew_state\x18\x02 \x01(\x0e\x32#.api.v1alpha1.agentsmith.AgentStateR\x08newState\x12;\n\x05\x65mpty\x18\n \x01(\x0b\x32#.api.v1alpha1.agentsmith.EmptyStateH\x00R\x05\x65mptyB\x0f\n\rstate_details\"\x0c\n\nEmptyState\"8\n\x14\x41gentVoiceStartEvent\x12 \n\x0csip_dial_url\x18\x01 \x01(\tR\nsipDialUrl\"\x14\n\x12\x41gentVoiceEndEvent\"\x16\n\x14\x41gentSessionEndEvent*\x98\x01\n\nAgentState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bUNAVAILABLE\x10\x01\x12\x08\n\x04IDLE\x10\x02\x12\t\n\x05READY\x10\x03\x12\n\n\x06HUNGUP\x10\x04\x12\r\n\tDESTROYED\x10\x05\x12\n\n\x06PEERED\x10\x06\x12\n\n\x06PAUSED\x10\x07\x12\n\n\x06WRAPUP\x10\x08\x12\x18\n\x14PREPARING_AFTER_IDLE\x10\n2\xb6\x01\n\nAgentSmith\x12\xa7\x01\n\x0b\x46ollowAgent\x12\'.api.v1alpha1.agentsmith.FollowAgentReq\x1a\'.api.v1alpha1.agentsmith.FollowAgentRes\"D\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/agentsmith/agentsmith/followagent:\x01*0\x01\x42\xa9\x01\n\x1b\x63om.api.v1alpha1.agentsmithB\x0cServiceProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x17\x41pi.V1alpha1.Agentsmith\xca\x02\x17\x41pi\\V1alpha1\\Agentsmith\xe2\x02#Api\\V1alpha1\\Agentsmith\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Agentsmithb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.agentsmith.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.agentsmithB\014ServiceProtoP\001\242\002\003AVA\252\002\027Api.V1alpha1.Agentsmith\312\002\027Api\\V1alpha1\\Agentsmith\342\002#Api\\V1alpha1\\Agentsmith\\GPBMetadata\352\002\031Api::V1alpha1::Agentsmith'
  _globals['_AGENTSMITH'].methods_by_name['FollowAgent']._loaded_options = None
  _globals['_AGENTSMITH'].methods_by_name['FollowAgent']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\0024\"//api/v1alpha1/agentsmith/agentsmith/followagent:\001*'
  _globals['_AGENTSTATE']._serialized_start=1043
  _globals['_AGENTSTATE']._serialized_end=1195
  _globals['_FOLLOWAGENTREQ']._serialized_start=154
  _globals['_FOLLOWAGENTREQ']._serialized_end=245
  _globals['_FOLLOWAGENTRES']._serialized_start=248
  _globals['_FOLLOWAGENTRES']._serialized_end=686
  _globals['_AGENTSTATECHANGEEVENT']._serialized_start=689
  _globals['_AGENTSTATECHANGEEVENT']._serialized_end=922
  _globals['_EMPTYSTATE']._serialized_start=924
  _globals['_EMPTYSTATE']._serialized_end=936
  _globals['_AGENTVOICESTARTEVENT']._serialized_start=938
  _globals['_AGENTVOICESTARTEVENT']._serialized_end=994
  _globals['_AGENTVOICEENDEVENT']._serialized_start=996
  _globals['_AGENTVOICEENDEVENT']._serialized_end=1016
  _globals['_AGENTSESSIONENDEVENT']._serialized_start=1018
  _globals['_AGENTSESSIONENDEVENT']._serialized_end=1040
  _globals['_AGENTSMITH']._serialized_start=1198
  _globals['_AGENTSMITH']._serialized_end=1380
# @@protoc_insertion_point(module_scope)
