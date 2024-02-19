# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/ghostnotifier.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/commons/ghostnotifier.proto\x12\x0b\x61pi.commons\x1a\x15\x61pi/commons/acd.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf8\x04\n\x11GhostNotification\x12!\n\x0creference_id\x18\x01 \x01(\tR\x0breferenceId\x12(\n\x03\x61ny\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x03\x61ny\x12-\n\x06status\x18\x03 \x01(\x0b\x32\x13.api.commons.StatusH\x00R\x06status\x12L\n\x11omni_conversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationH\x00R\x10omniConversation\x12Y\n\x12\x62\x61\x63koffice_message\x18\x06 \x01(\x0b\x32(.api.commons.AgentBackofficeMessageAlertH\x00R\x11\x62\x61\x63kofficeMessage\x12`\n\x15\x64irected_call_ringing\x18\x07 \x01(\x0b\x32*.api.commons.AgentDirectedCallRingingAlertH\x00R\x13\x64irectedCallRinging\x12]\n\x14\x64irected_call_hangup\x18\x08 \x01(\x0b\x32).api.commons.AgentDirectedCallHangupAlertH\x00R\x12\x64irectedCallHangup\x12r\n\x1f\x61gent_queued_calls_notification\x18\t \x01(\x0b\x32).api.commons.AgentQueuedCallsNotificationH\x00R\x1c\x61gentQueuedCallsNotificationB\t\n\x07payload\"6\n\x06Status\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"\xf2\x05\n\x1c\x41gentQueuedCallsNotification\x12\x64\n\x11\x61gent_queue_calls\x18\x10 \x03(\x0b\x32\x38.api.commons.AgentQueuedCallsNotification.QueuedCallDataR\x0f\x61gentQueueCalls\x12\\\n\ron_hold_calls\x18\x11 \x03(\x0b\x32\x38.api.commons.AgentQueuedCallsNotification.QueuedCallDataR\x0bonHoldCalls\x12U\n\thqm_calls\x18\x12 \x03(\x0b\x32\x38.api.commons.AgentQueuedCallsNotification.QueuedCallDataR\x08hqmCalls\x1a\xb6\x03\n\x0eQueuedCallData\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x03 \x01(\tR\x08\x63\x61llerId\x12\x37\n\tcall_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x39\n\nstart_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartDate\x12\x37\n\thold_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08holdDate\x12\x16\n\x06skills\x18\x07 \x03(\tR\x06skills\x12%\n\x0e\x61gent_specific\x18\x08 \x01(\x08R\ragentSpecific\x12]\n\x18queued_notification_type\x18\t \x01(\x0e\x32#.api.commons.QueuedNotificationTypeR\x16queuedNotificationTypeBr\n\x0f\x63om.api.commonsB\x12GhostnotifierProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.ghostnotifier_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\022GhostnotifierProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_GHOSTNOTIFICATION']._serialized_start=163
  _globals['_GHOSTNOTIFICATION']._serialized_end=795
  _globals['_STATUS']._serialized_start=797
  _globals['_STATUS']._serialized_end=851
  _globals['_AGENTQUEUEDCALLSNOTIFICATION']._serialized_start=854
  _globals['_AGENTQUEUEDCALLSNOTIFICATION']._serialized_end=1608
  _globals['_AGENTQUEUEDCALLSNOTIFICATION_QUEUEDCALLDATA']._serialized_start=1170
  _globals['_AGENTQUEUEDCALLSNOTIFICATION_QUEUEDCALLDATA']._serialized_end=1608
# @@protoc_insertion_point(module_scope)
