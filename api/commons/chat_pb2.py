# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/chat.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/commons/chat.proto\x12\x0b\x61pi.commons\"\x98\x01\n\x13\x43hatColorProperties\x12#\n\rprimary_color\x18\x01 \x01(\tR\x0cprimaryColor\x12*\n\x11header_text_color\x18\x02 \x01(\tR\x0fheaderTextColor\x12\x30\n\x14paragraph_text_color\x18\x03 \x01(\tR\x12paragraphTextColor\"B\n\nChatHeader\x12\x16\n\x06header\x18\x01 \x01(\tR\x06header\x12\x1c\n\tsubheader\x18\x02 \x01(\tR\tsubheader\"\xc6\x03\n\x10HoursOfOperation\x12:\n\x06monday\x18\x01 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x06monday\x12<\n\x07tuesday\x18\x02 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x07tuesday\x12@\n\twednesday\x18\x03 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\twednesday\x12>\n\x08thursday\x18\x04 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x08thursday\x12:\n\x06\x66riday\x18\x05 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x06\x66riday\x12>\n\x08saturday\x18\x06 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x08saturday\x12:\n\x06sunday\x18\x07 \x03(\x0b\x32\".api.commons.HoursOfOperationRangeR\x06sunday\"\x93\x01\n\x15HoursOfOperationRange\x12\x1d\n\nstart_hour\x18\x01 \x01(\x03R\tstartHour\x12!\n\x0cstart_minute\x18\x02 \x01(\x03R\x0bstartMinute\x12\x19\n\x08\x65nd_hour\x18\x03 \x01(\x03R\x07\x65ndHour\x12\x1d\n\nend_minute\x18\x04 \x01(\x03R\tendMinute*\x88\x01\n\x15\x43hatMessageSenderType\x12\"\n\x1e\x43HAT_MESSAGE_SENDER_TYPE_AGENT\x10\x00\x12%\n!CHAT_MESSAGE_SENDER_TYPE_CUSTOMER\x10\x01\x12$\n CHAT_MESSAGE_SENDER_TYPE_MANAGER\x10\x02*\x9f\x01\n\x12\x43hatCampaignStatus\x12\x19\n\x15\x43HAT_CAMPAIGN_UNKNOWN\x10\x00\x12\x1a\n\x15\x43HAT_CAMPAIGN_RUNNING\x10\xa2u\x12\x1a\n\x15\x43HAT_CAMPAIGN_STOPPED\x10\xcau\x12\x1b\n\x16\x43HAT_CAMPAIGN_ARCHIVED\x10\xd4u\x12\x19\n\x14\x43HAT_CAMPAIGN_PAUSED\x10\xdeu*\xba\x01\n\x11\x43hatCampaignEvent\x12\x1f\n\x1b\x43HAT_CAMPAIGN_EVENT_UNKNOWN\x10\x00\x12!\n\x1d\x43HAT_CAMPAIGN_EVENT_SCHEDULED\x10\x01\x12\x1f\n\x1b\x43HAT_CAMPAIGN_EVENT_STOPPED\x10\x02\x12 \n\x1c\x43HAT_CAMPAIGN_EVENT_ARCHIVED\x10\x03\x12\x1e\n\x1a\x43HAT_CAMPAIGN_EVENT_PAUSED\x10\x04*J\n\x0f\x43hatMessageType\x12\x1c\n\x18\x43HAT_REPLY_FROM_CUSTOMER\x10\x00\x12\x19\n\x15\x43HAT_REPLY_FROM_AGENT\x10\x01\x42i\n\x0f\x63om.api.commonsB\tChatProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\tChatProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CHATMESSAGESENDERTYPE']._serialized_start=870
  _globals['_CHATMESSAGESENDERTYPE']._serialized_end=1006
  _globals['_CHATCAMPAIGNSTATUS']._serialized_start=1009
  _globals['_CHATCAMPAIGNSTATUS']._serialized_end=1168
  _globals['_CHATCAMPAIGNEVENT']._serialized_start=1171
  _globals['_CHATCAMPAIGNEVENT']._serialized_end=1357
  _globals['_CHATMESSAGETYPE']._serialized_start=1359
  _globals['_CHATMESSAGETYPE']._serialized_end=1433
  _globals['_CHATCOLORPROPERTIES']._serialized_start=40
  _globals['_CHATCOLORPROPERTIES']._serialized_end=192
  _globals['_CHATHEADER']._serialized_start=194
  _globals['_CHATHEADER']._serialized_end=260
  _globals['_HOURSOFOPERATION']._serialized_start=263
  _globals['_HOURSOFOPERATION']._serialized_end=717
  _globals['_HOURSOFOPERATIONRANGE']._serialized_start=720
  _globals['_HOURSOFOPERATIONRANGE']._serialized_end=867
# @@protoc_insertion_point(module_scope)
