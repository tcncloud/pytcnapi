# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/agent_training_events.proto
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
    'api/commons/audit/agent_training_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import agent_training_pb2 as api_dot_commons_dot_agent__training__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/commons/audit/agent_training_events.proto\x12\x11\x61pi.commons.audit\x1a api/commons/agent_training.proto\"\x82\x01\n+AgentTrainingCreateLearningOpportunityEvent\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunityB\x97\x01\n\x15\x63om.api.commons.auditB\x18\x41gentTrainingEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.agent_training_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\030AgentTrainingEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_AGENTTRAININGCREATELEARNINGOPPORTUNITYEVENT']._serialized_start=103
  _globals['_AGENTTRAININGCREATELEARNINGOPPORTUNITYEVENT']._serialized_end=233
# @@protoc_insertion_point(module_scope)
