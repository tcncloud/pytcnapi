# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/audit/event_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/commons/audit/event_types.proto\x12\x11\x61pi.commons.audit*\xe2\x19\n\tEventType\x12\x15\n\x11\x44UMMY_APPLICATION\x10\x00\x12\x1d\n\x19\x44UMMY_APPLICATION_STORAGE\x10\x01\x12\x1d\n\x19\x44UMMY_APPLICATION_COMPUTE\x10\x02\x12\x13\n\x0fVOICE_ANALYTICS\x10\x64\x12#\n\x1fVOICE_ANALYTICS_FLAG_OCCURRENCE\x10\x65\x12%\n!VOICE_ANALYTICS_FLAG_NEEDS_REVIEW\x10\x66\x12\"\n\x1eVOICE_ANALYTICS_BILLING_REPORT\x10g\x12 \n\x1cVOICE_ANALYTICS_FLAG_SUMMARY\x10h\x12\x10\n\x0bOMNICHANNEL\x10\xac\x02\x12\x18\n\x13OMNICHANNEL_PROJECT\x10\xad\x02\x12\x19\n\x14OMNICHANNEL_CAMPAIGN\x10\xae\x02\x12%\n OMNICHANNEL_DAILY_PROJECT_REPORT\x10\xaf\x02\x12*\n%OMNICHANNEL_DAILY_CONVERSATION_REPORT\x10\xb0\x02\x12*\n%OMNICHANNEL_AGENT_ASSIGN_CONVERSATION\x10\xb1\x02\x12,\n\'OMNICHANNEL_AGENT_UNASSIGN_CONVERSATION\x10\xb2\x02\x12,\n\'OMNICHANNEL_AGENT_REASSIGN_CONVERSATION\x10\xb3\x02\x12\x14\n\x0fOMNICHANNEL_T10\x10\xb4\x02\x12&\n!OMNICHANNEL_CUSTOMER_TEXT_MESSAGE\x10\xb5\x02\x12#\n\x1eOMNICHANNEL_AGENT_TEXT_MESSAGE\x10\xb6\x02\x12\x1f\n\x1aOMNICHANNEL_FINISH_WRAP_UP\x10\xb7\x02\x12\x1e\n\x19OMNICHANNEL_BEGIN_WRAP_UP\x10\xb8\x02\x12\x14\n\x0fOMNICHANNEL_T11\x10\xb9\x02\x12$\n\x1fOMNICHANNEL_CREATE_CONVERSATION\x10\xba\x02\x12\x1e\n\x19OMNICHANNEL_AGENT_SUSPEND\x10\xbb\x02\x12#\n\x1eOMNICHANNEL_CLOSE_CONVERSATION\x10\xbc\x02\x12%\n OMNICHANNEL_MANAGER_TEXT_MESSAGE\x10\xcc\x02\x12 \n\x1bOMNICHANNEL_UPDATE_CAMPAIGN\x10\xca\x02\x12\x30\n+OMNICHANNEL_SET_CONVERSATION_COLLECTED_DATA\x10\xcb\x02\x12!\n\x1cOMNICHANNEL_ARCHIVE_CAMPAIGN\x10\xcd\x02\x12\x1f\n\x1aOMNICHANNEL_PAUSE_CAMPAIGN\x10\xce\x02\x12 \n\x1bOMNICHANNEL_RESUME_CAMPAIGN\x10\xcf\x02\x12\x1f\n\x1aOMNICHANNEL_START_CAMPAIGN\x10\xd0\x02\x12 \n\x1bOMNICHANNEL_SCHEDULE_MODULE\x10\xd1\x02\x12\x1d\n\x18OMNICHANNEL_START_MODULE\x10\xd2\x02\x12\x1d\n\x18OMNICHANNEL_PAUSE_MODULE\x10\xd3\x02\x12\x1e\n\x19OMNICHANNEL_RESUME_MODULE\x10\xd4\x02\x12\x1d\n\x18OMNICHANNEL_ERROR_MODULE\x10\xd5\x02\x12\x1f\n\x1aOMNICHANNEL_SUCCESS_MODULE\x10\xd6\x02\x12\x1c\n\x17OMNICHANNEL_FAIL_MODULE\x10\xd7\x02\x12 \n\x1bOMNICHANNEL_COMPLETE_MODULE\x10\xd8\x02\x12\x1f\n\x1aOMNICHANNEL_ARCHIVE_MODULE\x10\xd9\x02\x12\x1e\n\x19OMNICHANNEL_UPDATE_MODULE\x10\xda\x02\x12(\n#OMNICHANNEL_MODULE_SMS_MESSAGE_SENT\x10\xdb\x02\x12\"\n\x1dOMNICHANNEL_COMPLETE_CAMPAIGN\x10\xdc\x02\x12%\n OMNICHANNEL_MODULE_INITIAL_REPLY\x10\xdd\x02\x12\"\n\x1dOMNICHANNEL_TASK_MESSAGE_SENT\x10\xde\x02\x12%\n OMNICHANNEL_CONNECTED_INBOX_POLL\x10\xdf\x02\x12(\n#OMNICHANNEL_CONNECTED_INBOX_CREATED\x10\xe0\x02\x12$\n\x1fOMNICHANNEL_AGENT_MESSAGE_UNITS\x10\xe1\x02\x12&\n!OMNICHANNEL_MANAGER_MESSAGE_UNITS\x10\xe2\x02\x12\'\n\"OMNICHANNEL_CUSTOMER_MESSAGE_UNITS\x10\xe3\x02\x12%\n OMNICHANNEL_SYSTEM_MESSAGE_UNITS\x10\xe4\x02\x12\"\n\x1dOMNICHANNEL_PAYMENT_LINK_SENT\x10\xe5\x02\x12\x14\n\x0f\x41SM_AGENT_LOGIN\x10\x90\x03\x12\x13\n\x0e\x41SM_OPEN_VOICE\x10\x91\x03\x12\x18\n\x13\x41SM_OPEN_OMNI_AGENT\x10\x92\x03\x12\x1e\n\x19\x41SM_ACTIVATE_CONVERSATION\x10\x93\x03\x12 \n\x1b\x41SM_DEACTIVATE_CONVERSATION\x10\x94\x03\x12\x1c\n\x17\x41SM_AGENT_STATE_CHANGED\x10\x95\x03\x12\x15\n\x10\x41SM_AGENT_LOGOUT\x10\x96\x03\x12\x14\n\x0f\x41SM_PAUSE_EVENT\x10\x97\x03\x12\x15\n\x10\x41SM_RESUME_EVENT\x10\x98\x03\x12\"\n\x1d\x41SM_CONVERSATION_PULLED_EVENT\x10\x99\x03\x12%\n SCORECARDS_CREATE_QUESTION_EVENT\x10\xf4\x03\x12%\n SCORECARDS_UPDATE_QUESTION_EVENT\x10\xf5\x03\x12%\n SCORECARDS_DELETE_QUESTION_EVENT\x10\xf6\x03\x12&\n!SCORECARDS_CREATE_SCORECARD_EVENT\x10\xf7\x03\x12&\n!SCORECARDS_UPDATE_SCORECARD_EVENT\x10\xf8\x03\x12&\n!SCORECARDS_DELETE_SCORECARD_EVENT\x10\xf9\x03\x12%\n SCORECARDS_CLONE_SCORECARD_EVENT\x10\xfa\x03\x12\'\n\"SCORECARDS_CREATE_EVALUATION_EVENT\x10\xfb\x03\x12\'\n\"SCORECARDS_DELETE_EVALUATION_EVENT\x10\xfc\x03\x12$\n\x1fSCORECARDS_CREATE_SECTION_EVENT\x10\xfd\x03\x12$\n\x1fSCORECARDS_UPDATE_SECTION_EVENT\x10\xfe\x03\x12$\n\x1fSCORECARDS_DELETE_SECTION_EVENT\x10\xff\x03\x12%\n SCORECARDS_CREATE_CATEGORY_EVENT\x10\x80\x04\x12%\n SCORECARDS_UPDATE_CATEGORY_EVENT\x10\x81\x04\x12%\n SCORECARDS_DELETE_CATEGORY_EVENT\x10\x82\x04\x12\x30\n+SCORECARDS_CREATE_EVALUATION_QUESTION_EVENT\x10\x83\x04\x12\x30\n+SCORECARDS_UPDATE_EVALUATION_QUESTION_EVENT\x10\x84\x04\x12\x30\n+SCORECARDS_DELETE_EVALUATION_QUESTION_EVENT\x10\x85\x04\x12/\n*SCORECARDS_CREATE_SCORECARD_QUESTION_EVENT\x10\x86\x04\x12/\n*SCORECARDS_UPDATE_SCORECARD_QUESTION_EVENT\x10\x87\x04\x12/\n*SCORECARDS_DELETE_SCORECARD_QUESTION_EVENT\x10\x88\x04\x12,\n\'SCORECARDS_CREATE_AUTO_EVALUATION_EVENT\x10\x89\x04\x12\'\n\"SCORECARDS_UPDATE_EVALUATION_EVENT\x10\x8a\x04\x12\x18\n\x13TICKET_CREATE_EVENT\x10\xd8\x04\x12\x16\n\x11TICKET_EDIT_EVENT\x10\xd9\x04\x12\x17\n\x12TICKET_CLOSE_EVENT\x10\xda\x04\x12\x1f\n\x1a\x43OMPLIANCE_RND_QUERY_EVENT\x10\xbc\x05\x12&\n!COMPLIANCE_RND_QUERY_CACHED_EVENT\x10\xbd\x05\x12\x35\n0AGENT_TRAINING_CREATE_LEARNING_OPPORTUNITY_EVENT\x10\xa0\x06\x42\x8e\x01\n\x15\x63om.api.commons.auditB\x0f\x45ventTypesProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.event_types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.api.commons.auditB\017EventTypesProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_EVENTTYPE']._serialized_start=59
  _globals['_EVENTTYPE']._serialized_end=3357
# @@protoc_insertion_point(module_scope)
