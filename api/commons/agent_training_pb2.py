# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/agent_training.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/commons/agent_training.proto\x12\x0b\x61pi.commons\x1a\x15\x61pi/commons/acd.proto\"\xd0\x02\n\x13LearningOpportunity\x12\x36\n\x17learning_opportunity_id\x18\x02 \x01(\x03R\x15learningOpportunityId\x12\x19\n\x08\x63\x61ll_sid\x18\x03 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12%\n\x0etranscript_sid\x18\x05 \x01(\x03R\rtranscriptSid\x12\"\n\ragent_user_id\x18\x06 \x01(\tR\x0b\x61gentUserId\x12!\n\x0cstart_offset\x18\x07 \x01(\x05R\x0bstartOffset\x12\x1d\n\nend_offset\x18\x08 \x01(\x05R\tendOffset\x12 \n\x0b\x64\x65scription\x18\t \x01(\tR\x0b\x64\x65scriptionBr\n\x0f\x63om.api.commonsB\x12\x41gentTrainingProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.agent_training_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.api.commonsB\022AgentTrainingProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_LEARNINGOPPORTUNITY']._serialized_start=73
  _globals['_LEARNINGOPPORTUNITY']._serialized_end=409
# @@protoc_insertion_point(module_scope)
