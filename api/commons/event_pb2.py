# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import asm_pb2 as api_dot_commons_dot_asm__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/commons/event.proto\x12\x0b\x61pi.commons\x1a\x15\x61pi/commons/asm.proto\x1a\x1d\x61pi/commons/omnichannel.proto\"\xd5\x04\n\x05\x45vent\x12.\n\x05state\x18\x01 \x01(\x0e\x32\x18.api.commons.StatusStateR\x05state\x12\x1d\n\nevent_time\x18\x02 \x01(\x03R\teventTime\x12k\n\x1c\x61\x63tivated_conversation_event\x18\x05 \x01(\x0b\x32\'.api.commons.ActivatedConversationEventH\x00R\x1a\x61\x63tivatedConversationEvent\x12q\n\x1e\x64\x65\x61\x63tivated_conversation_event\x18\x06 \x01(\x0b\x32).api.commons.DeactivatedConversationEventH\x00R\x1c\x64\x65\x61\x63tivatedConversationEvent\x12M\n\x12sent_message_event\x18\x07 \x01(\x0b\x32\x1d.api.commons.SentMessageEventH\x00R\x10sentMessageEvent\x12J\n\x11send_status_event\x18\x08 \x01(\x0b\x32\x1c.api.commons.SendStatusEventH\x00R\x0fsendStatusEvent\x12:\n\x0bpause_event\x18\t \x01(\x0b\x32\x17.api.commons.PauseEventH\x00R\npauseEvent\x12=\n\x0cresume_event\x18\n \x01(\x0b\x32\x18.api.commons.ResumeEventH\x00R\x0bresumeEventB\x07\n\x05\x65vent\"_\n\x1a\x41\x63tivatedConversationEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"a\n\x1c\x44\x65\x61\x63tivatedConversationEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xc2\x01\n\x10SentMessageEvent\x12\x32\n\x15response_time_seconds\x18\x01 \x01(\x03R\x13responseTimeSeconds\x12\x37\n\x18is_initial_agent_message\x18\x02 \x01(\x08R\x15isInitialAgentMessage\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"C\n\x0fSendStatusEvent\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32\x18.api.commons.StatusStateR\x06status\"\xe4\x05\n\x08\x41smEvent\x12.\n\x05state\x18\x01 \x01(\x0e\x32\x18.api.commons.StatusStateR\x05state\x12\x1d\n\nevent_time\x18\x02 \x01(\x03R\teventTime\x12u\n activated_conversation_asm_event\x18\x05 \x01(\x0b\x32*.api.commons.ActivatedConversationAsmEventH\x00R\x1d\x61\x63tivatedConversationAsmEvent\x12{\n\"deactivated_conversation_asm_event\x18\x06 \x01(\x0b\x32,.api.commons.DeactivatedConversationAsmEventH\x00R\x1f\x64\x65\x61\x63tivatedConversationAsmEvent\x12W\n\x16sent_message_asm_event\x18\x07 \x01(\x0b\x32 .api.commons.SentMessageAsmEventH\x00R\x13sentMessageAsmEvent\x12T\n\x15send_status_asm_event\x18\x08 \x01(\x0b\x32\x1f.api.commons.SendStatusAsmEventH\x00R\x12sendStatusAsmEvent\x12:\n\x0bpause_event\x18\t \x01(\x0b\x32\x17.api.commons.PauseEventH\x00R\npauseEvent\x12=\n\x0cresume_event\x18\n \x01(\x0b\x32\x18.api.commons.ResumeEventH\x00R\x0bresumeEvent\x12\x62\n\x19\x63onversation_pulled_event\x18\x0b \x01(\x0b\x32$.api.commons.ConversationPulledEventH\x00R\x17\x63onversationPulledEventB\x07\n\x05\x65vent\"b\n\x1d\x41\x63tivatedConversationAsmEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"d\n\x1f\x44\x65\x61\x63tivatedConversationAsmEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xc5\x01\n\x13SentMessageAsmEvent\x12\x32\n\x15response_time_seconds\x18\x01 \x01(\x03R\x13responseTimeSeconds\x12\x37\n\x18is_initial_agent_message\x18\x02 \x01(\x08R\x15isInitialAgentMessage\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\x14\n\x12SendStatusAsmEvent\"\x0c\n\nPauseEvent\"\r\n\x0bResumeEvent\"\\\n\x17\x43onversationPulledEvent\x12\x41\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversationBj\n\x0f\x63om.api.commonsB\nEventProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\nEventProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_EVENT']._serialized_start=95
  _globals['_EVENT']._serialized_end=692
  _globals['_ACTIVATEDCONVERSATIONEVENT']._serialized_start=694
  _globals['_ACTIVATEDCONVERSATIONEVENT']._serialized_end=789
  _globals['_DEACTIVATEDCONVERSATIONEVENT']._serialized_start=791
  _globals['_DEACTIVATEDCONVERSATIONEVENT']._serialized_end=888
  _globals['_SENTMESSAGEEVENT']._serialized_start=891
  _globals['_SENTMESSAGEEVENT']._serialized_end=1085
  _globals['_SENDSTATUSEVENT']._serialized_start=1087
  _globals['_SENDSTATUSEVENT']._serialized_end=1154
  _globals['_ASMEVENT']._serialized_start=1157
  _globals['_ASMEVENT']._serialized_end=1897
  _globals['_ACTIVATEDCONVERSATIONASMEVENT']._serialized_start=1899
  _globals['_ACTIVATEDCONVERSATIONASMEVENT']._serialized_end=1997
  _globals['_DEACTIVATEDCONVERSATIONASMEVENT']._serialized_start=1999
  _globals['_DEACTIVATEDCONVERSATIONASMEVENT']._serialized_end=2099
  _globals['_SENTMESSAGEASMEVENT']._serialized_start=2102
  _globals['_SENTMESSAGEASMEVENT']._serialized_end=2299
  _globals['_SENDSTATUSASMEVENT']._serialized_start=2301
  _globals['_SENDSTATUSASMEVENT']._serialized_end=2321
  _globals['_PAUSEEVENT']._serialized_start=2323
  _globals['_PAUSEEVENT']._serialized_end=2335
  _globals['_RESUMEEVENT']._serialized_start=2337
  _globals['_RESUMEEVENT']._serialized_end=2350
  _globals['_CONVERSATIONPULLEDEVENT']._serialized_start=2352
  _globals['_CONVERSATIONPULLEDEVENT']._serialized_end=2444
# @@protoc_insertion_point(module_scope)
