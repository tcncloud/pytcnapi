# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/email.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/commons/email.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/commons/email.proto\x12\x0b\x61pi.commons*\xce\x03\n\x0b\x45mailResult\x12\x18\n\x14\x45MAIL_RESULT_UNKNOWN\x10\x00\x12\x17\n\x12\x45MAIL_TASK_WAITING\x10\x98\x43\x12\x1a\n\x15\x45MAIL_TASK_PROCESSING\x10\xfc\x43\x12\x13\n\x0e\x45MAIL_TASK_DNC\x10\x86\x44\x12\x17\n\x12\x45MAIL_TASK_INVALID\x10\x90\x44\x12 \n\x1b\x45MAIL_TASK_ATTACHMENT_ERROR\x10\x9a\x44\x12\x19\n\x14\x45MAIL_TASK_CANCELLED\x10\xa4\x44\x12\x16\n\x11\x45MAIL_TASK_QUEUED\x10\xe0\x44\x12\x19\n\x14\x45MAIL_TASK_DELIVERED\x10\xc4\x45\x12\x17\n\x12\x45MAIL_TASK_DROPPED\x10\xce\x45\x12\x18\n\x13\x45MAIL_TASK_DEFERRED\x10\xd8\x45\x12\x17\n\x12\x45MAIL_TASK_BOUNCED\x10\xe2\x45\x12\x16\n\x11\x45MAIL_TASK_OPENED\x10\xec\x45\x12\x17\n\x12\x45MAIL_TASK_CLICKED\x10\xf6\x45\x12\x1c\n\x17\x45MAIL_TASK_UNSUBSCRIBED\x10\x80\x46\x12\x1e\n\x19\x45MAIL_TASK_MARKED_AS_SPAM\x10\x8a\x46\x12\x17\n\x12\x45MAIL_TASK_BLOCKED\x10\x94\x46*\xb3\x02\n\x0b\x45mailStatus\x12\x19\n\x15\x45MAIL_STATUS_UNKKNOWN\x10\x00\x12\x14\n\x0f\x45MAIL_PREPARING\x10\xc0>\x12\x14\n\x0f\x45MAIL_SCHEDULED\x10\xa4?\x12\x11\n\x0c\x45MAIL_RESUME\x10\xd6?\x12\x12\n\rEMAIL_RUNNING\x10\x88@\x12\x14\n\x0f\x45MAIL_COMPLETED\x10\xec@\x12\x14\n\x0f\x45MAIL_CANCELLED\x10\xf6@\x12\x1a\n\x15\x45MAIL_CANCELLED_ADMIN\x10\x80\x41\x12\x1b\n\x16\x45MAIL_SUMMED_COMPLETED\x10\xd0\x41\x12\x1b\n\x16\x45MAIL_SUMMED_CANCELLED\x10\xda\x41\x12!\n\x1c\x45MAIL_SUMMED_CANCELLED_ADMIN\x10\xe4\x41\x12\x11\n\x0c\x45MAIL_PAUSED\x10\xb4\x42*\xf3\x03\n\x12\x45mailIBGroupStatus\x12\x1a\n\x16IB_EMAIL_GROUP_UNKNOWN\x10\x00\x12\x1d\n\x18IB_EMAIL_GROUP_PREPARING\x10\x90N\x12\x1d\n\x18IB_EMAIL_GROUP_SCHEDULED\x10\x9aN\x12\x1b\n\x16IB_EMAIL_GROUP_RUNNING\x10\xa4N\x12\x1a\n\x15IB_EMAIL_GROUP_PAUSED\x10\xaeN\x12\x1a\n\x15IB_EMAIL_GROUP_RESUME\x10\xb8N\x12&\n!IB_EMAIL_GROUP_RUNNING_WITH_ERROR\x10\xb9N\x12!\n\x1cIB_EMAIL_GROUP_ERROR_STANDBY\x10\xbaN\x12\x1d\n\x18IB_EMAIL_GROUP_COMPLETED\x10\xc2N\x12\"\n\x1dIB_EMAIL_GROUP_CANCELLED_USER\x10\xccN\x12#\n\x1eIB_EMAIL_GROUP_CANCELLED_ADMIN\x10\xd6N\x12$\n\x1fIB_EMAIL_GROUP_SUMMED_COMPLETED\x10\xa6O\x12)\n$IB_EMAIL_GROUP_SUMMED_CANCELLED_USER\x10\xb0O\x12*\n%IB_EMAIL_GROUP_SUMMED_CANCELLED_ADMIN\x10\xbaO*\xdf\x04\n\x12\x45mailIBReplyStatus\x12\x1a\n\x16IB_EMAIL_REPLY_UNKNOWN\x10\x00\x12\x1c\n\x17IB_EMAIL_REPLY_RECEIVED\x10\xe0]\x12!\n\x1cIB_EMAIL_AGENT_REPLY_SENDING\x10\xea]\x12(\n#IB_EMAIL_AGENT_REPLY_SENDING_FAILED\x10\xf4]\x12!\n\x1cIB_EMAIL_AGENT_REPLY_INVALID\x10\xfe]\x12\x1e\n\x19IB_EMAIL_AGENT_REPLY_SENT\x10\x88^\x12#\n\x1eIB_EMAIL_AGENT_REPLY_DELIVERED\x10\x92^\x12!\n\x1cIB_EMAIL_AGENT_REPLY_DROPPED\x10\x9c^\x12\"\n\x1dIB_EMAIL_AGENT_REPLY_DEFERRED\x10\xa6^\x12!\n\x1cIB_EMAIL_AGENT_REPLY_BOUNCED\x10\xb0^\x12 \n\x1bIB_EMAIL_AGENT_REPLY_OPENED\x10\xba^\x12!\n\x1cIB_EMAIL_AGENT_REPLY_CLICKED\x10\xc4^\x12&\n!IB_EMAIL_AGENT_REPLY_UNSUBSCRIBED\x10\xce^\x12(\n#IB_EMAIL_AGENT_REPLY_MARKED_AS_SPAM\x10\xd8^\x12!\n\x1cIB_EMAIL_AGENT_REPLY_BLOCKED\x10\xe2^\x12\x17\n\x12IB_EMAIL_REPLY_DNC\x10\xec^\x12\x1d\n\x18IB_EMAIL_REPLY_CANCELLED\x10\xf6^*\xe9\x03\n\x11\x45mailIBGroupEvent\x12!\n\x1dIB_EMAIL_GROUP_EVENT_PREPARED\x10\x00\x12\"\n\x1eIB_EMAIL_GROUP_EVENT_SCHEDULED\x10\x01\x12 \n\x1cIB_EMAIL_GROUP_EVENT_STARTED\x10\x02\x12 \n\x1cIB_EMAIL_GROUP_EVENT_RUNNING\x10\x03\x12 \n\x1cIB_EMAIL_GROUP_EVENT_STOPPED\x10\x04\x12\x1f\n\x1bIB_EMAIL_GROUP_EVENT_PAUSED\x10\x05\x12\x1f\n\x1bIB_EMAIL_GROUP_EVENT_RESUME\x10\x06\x12\"\n\x1eIB_EMAIL_GROUP_EVENT_CANCELLED\x10\x07\x12)\n%IB_EMAIL_GROUP_EVENT_MESSAGE_RECEIVED\x10\x08\x12$\n IB_EMAIL_GROUP_EVENT_LOGIN_ERROR\x10\t\x12$\n IB_EMAIL_GROUP_EVENT_FETCH_ERROR\x10\n\x12&\n\"IB_EMAIL_GROUP_EVENT_STANDBY_ERROR\x10\x0b\x12\"\n\x1eIB_EMAIL_GROUP_EVENT_COMPLETED\x10\x0c*\x95\x01\n\x10\x45mailIBReplyType\x12\x11\n\rREPLY_UNKNOWN\x10\x00\x12\x11\n\rEXISTING_CONV\x10\x01\x12\x12\n\x0eOUTBOUND_REPLY\x10\x02\x12\x0f\n\x0b\x41GENT_REPLY\x10\x03\x12\x10\n\x0cINBOUND_PURE\x10\x04\x12\x11\n\rOUTBOUND_TASK\x10\x05\x12\x11\n\rOUTBOUND_PURE\x10\x06\x42j\n\x0f\x63om.api.commonsB\nEmailProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.email_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\nEmailProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_EMAILRESULT']._serialized_start=41
  _globals['_EMAILRESULT']._serialized_end=503
  _globals['_EMAILSTATUS']._serialized_start=506
  _globals['_EMAILSTATUS']._serialized_end=813
  _globals['_EMAILIBGROUPSTATUS']._serialized_start=816
  _globals['_EMAILIBGROUPSTATUS']._serialized_end=1315
  _globals['_EMAILIBREPLYSTATUS']._serialized_start=1318
  _globals['_EMAILIBREPLYSTATUS']._serialized_end=1925
  _globals['_EMAILIBGROUPEVENT']._serialized_start=1928
  _globals['_EMAILIBGROUPEVENT']._serialized_end=2417
  _globals['_EMAILIBREPLYTYPE']._serialized_start=2420
  _globals['_EMAILIBREPLYTYPE']._serialized_end=2569
# @@protoc_insertion_point(module_scope)
