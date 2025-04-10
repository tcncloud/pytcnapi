# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/sms.proto
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
    'api/commons/sms.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/sms.proto\x12\x0b\x61pi.commons\"\xc1\x03\n\x10SimpleSmsMamData\x12\x10\n\x03src\x18\x01 \x01(\tR\x03src\x12\x10\n\x03\x64st\x18\x02 \x01(\tR\x03\x64st\x12\x10\n\x03msg\x18\x03 \x01(\tR\x03msg\x12\"\n\rsms_group_sid\x18\x04 \x01(\x03R\x0bsmsGroupSid\x12 \n\x0csms_task_sid\x18\x05 \x01(\x03R\nsmsTaskSid\x12 \n\x0cis_toll_free\x18\x06 \x01(\tR\nisTollFree\x12 \n\x0cis_time_zone\x18\x07 \x01(\tR\nisTimeZone\x12#\n\rprovider_name\x18\x08 \x01(\tR\x0cproviderName\x12$\n\x0ehunt_group_sid\x18\t \x01(\x03R\x0chuntGroupSid\x12\x1d\n\nclient_sid\x18\n \x01(\x03R\tclientSid\x12Y\n\x18simple_sms_mam_meta_data\x18\x0b \x03(\x0b\x32!.api.commons.SimpleSmsMamKeyValueR\x14simpleSmsMamMetaData\x12(\n\x10\x64st_country_code\x18\x0c \x01(\x03R\x0e\x64stCountryCode\">\n\x14SimpleSmsMamKeyValue\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value*\xe4\x03\n\tSMSStatus\x12\x0f\n\x0bSMS_UNKWNON\x10\x00\x12\x12\n\rSMS_PREPARING\x10\xd8\x36\x12\x12\n\rSMS_SCHEDULED\x10\xbc\x37\x12\x0f\n\nSMS_RESUME\x10\xee\x37\x12\x10\n\x0bSMS_RUNNING\x10\xa0\x38\x12\x12\n\rSMS_COMPLETED\x10\x84\x39\x12\x12\n\rSMS_CANCELLED\x10\x8e\x39\x12\x18\n\x13SMS_CANCELLED_ADMIN\x10\x98\x39\x12\x19\n\x14SMS_SUMMED_COMPLETED\x10\xe8\x39\x12\x19\n\x14SMS_SUMMED_CANCELLED\x10\xf2\x39\x12\x1f\n\x1aSMS_SUMMED_CANCELLED_ADMIN\x10\xfc\x39\x12\x0f\n\nSMS_PAUSED\x10\xcc:\x12\x15\n\x10SMS_TASK_WAITING\x10\xb0;\x12\x18\n\x13SMS_TASK_PROCESSING\x10\x94<\x12\x11\n\x0cSMS_TASK_DNC\x10\x9e<\x12\x15\n\x10SMS_TASK_INVALID\x10\xa8<\x12\x14\n\x0fSMS_TASK_QUEUED\x10\xf8<\x12\x12\n\rSMS_TASK_SENT\x10\xdc=\x12\x17\n\x12SMS_TASK_DELIVERED\x10\xe6=\x12\x1b\n\x16SMS_TASK_NOT_DELIVERED\x10\xf0=\x12\x16\n\x11SMS_TASK_CANCELED\x10\xfa=*\x8e\x03\n\x10SMSIBGroupStatus\x12\x18\n\x14IB_SMS_GROUP_UNKNOWN\x10\x00\x12\x1b\n\x16IB_SMS_GROUP_PREPARING\x10\xf8U\x12\x1b\n\x16IB_SMS_GROUP_SCHEDULED\x10\x82V\x12\x19\n\x14IB_SMS_GROUP_RUNNING\x10\x8cV\x12\x18\n\x13IB_SMS_GROUP_PAUSED\x10\x96V\x12\x18\n\x13IB_SMS_GROUP_RESUME\x10\xa0V\x12\x1b\n\x16IB_SMS_GROUP_COMPLETED\x10\xaaV\x12 \n\x1bIB_SMS_GROUP_CANCELLED_USER\x10\xb4V\x12!\n\x1cIB_SMS_GROUP_CANCELLED_ADMIN\x10\xbeV\x12\"\n\x1dIB_SMS_GROUP_SUMMED_COMPLETED\x10\x8eW\x12\'\n\"IB_SMS_GROUP_SUMMED_CANCELLED_USER\x10\x98W\x12(\n#IB_SMS_GROUP_SUMMED_CANCELLED_ADMIN\x10\xa2W*F\n\x0fSMSIBTaskStatus\x12\x17\n\x13IB_SMS_TASK_UNKNOWN\x10\x00\x12\x1a\n\x15IB_SMS_TASK_COMPLETED\x10\xc8\x65*\xa6\x02\n\x1aSMSConversationAuditAction\x12\'\n#SMS_AUDIT_ACTION_CONVERSATION_START\x10\x00\x12*\n&SMS_AUDIT_ACTION_CONVERSATION_MSG_SENT\x10\x01\x12*\n&SMS_AUDIT_ACTION_CONVERSATION_MSG_READ\x10\x02\x12,\n(SMS_AUDIT_ACTION_CONVERSATION_UNASSIGNED\x10\x03\x12*\n&SMS_AUDIT_ACTION_CONVERSATION_ASSIGNED\x10\x04\x12-\n)SMS_AUDIT_ACTION_CONVERSATION_TRANSFERRED\x10\x05*6\n\x0cSMSMamStatus\x12\n\n\x06QUEUED\x10\x00\x12\x0c\n\x08\x41PPROVED\x10\x01\x12\x0c\n\x08REJECTED\x10\x02\x42h\n\x0f\x63om.api.commonsB\x08SmsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.sms_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\010SmsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_SMSSTATUS']._serialized_start=555
  _globals['_SMSSTATUS']._serialized_end=1039
  _globals['_SMSIBGROUPSTATUS']._serialized_start=1042
  _globals['_SMSIBGROUPSTATUS']._serialized_end=1440
  _globals['_SMSIBTASKSTATUS']._serialized_start=1442
  _globals['_SMSIBTASKSTATUS']._serialized_end=1512
  _globals['_SMSCONVERSATIONAUDITACTION']._serialized_start=1515
  _globals['_SMSCONVERSATIONAUDITACTION']._serialized_end=1809
  _globals['_SMSMAMSTATUS']._serialized_start=1811
  _globals['_SMSMAMSTATUS']._serialized_end=1865
  _globals['_SIMPLESMSMAMDATA']._serialized_start=39
  _globals['_SIMPLESMSMAMDATA']._serialized_end=488
  _globals['_SIMPLESMSMAMKEYVALUE']._serialized_start=490
  _globals['_SIMPLESMSMAMKEYVALUE']._serialized_end=552
# @@protoc_insertion_point(module_scope)
