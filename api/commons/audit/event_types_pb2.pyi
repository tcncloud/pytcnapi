from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUMMY_APPLICATION: _ClassVar[EventType]
    DUMMY_APPLICATION_STORAGE: _ClassVar[EventType]
    DUMMY_APPLICATION_COMPUTE: _ClassVar[EventType]
    VOICE_ANALYTICS: _ClassVar[EventType]
    VOICE_ANALYTICS_FLAG_OCCURRENCE: _ClassVar[EventType]
    VOICE_ANALYTICS_FLAG_NEEDS_REVIEW: _ClassVar[EventType]
    VOICE_ANALYTICS_BILLING_REPORT: _ClassVar[EventType]
    VOICE_ANALYTICS_FLAG_SUMMARY: _ClassVar[EventType]
    VOICE_ANALYTICS_PHRASE_CORRECTION: _ClassVar[EventType]
    OMNICHANNEL: _ClassVar[EventType]
    OMNICHANNEL_PROJECT: _ClassVar[EventType]
    OMNICHANNEL_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_DAILY_PROJECT_REPORT: _ClassVar[EventType]
    OMNICHANNEL_DAILY_CONVERSATION_REPORT: _ClassVar[EventType]
    OMNICHANNEL_AGENT_ASSIGN_CONVERSATION: _ClassVar[EventType]
    OMNICHANNEL_AGENT_UNASSIGN_CONVERSATION: _ClassVar[EventType]
    OMNICHANNEL_AGENT_REASSIGN_CONVERSATION: _ClassVar[EventType]
    OMNICHANNEL_T10: _ClassVar[EventType]
    OMNICHANNEL_CUSTOMER_TEXT_MESSAGE: _ClassVar[EventType]
    OMNICHANNEL_AGENT_TEXT_MESSAGE: _ClassVar[EventType]
    OMNICHANNEL_FINISH_WRAP_UP: _ClassVar[EventType]
    OMNICHANNEL_BEGIN_WRAP_UP: _ClassVar[EventType]
    OMNICHANNEL_T11: _ClassVar[EventType]
    OMNICHANNEL_CREATE_CONVERSATION: _ClassVar[EventType]
    OMNICHANNEL_AGENT_SUSPEND: _ClassVar[EventType]
    OMNICHANNEL_CLOSE_CONVERSATION: _ClassVar[EventType]
    OMNICHANNEL_MANAGER_TEXT_MESSAGE: _ClassVar[EventType]
    OMNICHANNEL_UPDATE_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_SET_CONVERSATION_COLLECTED_DATA: _ClassVar[EventType]
    OMNICHANNEL_ARCHIVE_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_PAUSE_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_RESUME_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_START_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_SCHEDULE_MODULE: _ClassVar[EventType]
    OMNICHANNEL_START_MODULE: _ClassVar[EventType]
    OMNICHANNEL_PAUSE_MODULE: _ClassVar[EventType]
    OMNICHANNEL_RESUME_MODULE: _ClassVar[EventType]
    OMNICHANNEL_ERROR_MODULE: _ClassVar[EventType]
    OMNICHANNEL_SUCCESS_MODULE: _ClassVar[EventType]
    OMNICHANNEL_FAIL_MODULE: _ClassVar[EventType]
    OMNICHANNEL_COMPLETE_MODULE: _ClassVar[EventType]
    OMNICHANNEL_ARCHIVE_MODULE: _ClassVar[EventType]
    OMNICHANNEL_UPDATE_MODULE: _ClassVar[EventType]
    OMNICHANNEL_MODULE_SMS_MESSAGE_SENT: _ClassVar[EventType]
    OMNICHANNEL_COMPLETE_CAMPAIGN: _ClassVar[EventType]
    OMNICHANNEL_MODULE_INITIAL_REPLY: _ClassVar[EventType]
    OMNICHANNEL_TASK_MESSAGE_SENT: _ClassVar[EventType]
    OMNICHANNEL_CONNECTED_INBOX_POLL: _ClassVar[EventType]
    OMNICHANNEL_CONNECTED_INBOX_CREATED: _ClassVar[EventType]
    OMNICHANNEL_AGENT_MESSAGE_UNITS: _ClassVar[EventType]
    OMNICHANNEL_MANAGER_MESSAGE_UNITS: _ClassVar[EventType]
    OMNICHANNEL_CUSTOMER_MESSAGE_UNITS: _ClassVar[EventType]
    OMNICHANNEL_SYSTEM_MESSAGE_UNITS: _ClassVar[EventType]
    OMNICHANNEL_PAYMENT_LINK_SENT: _ClassVar[EventType]
    OMNICHANNEL_MANUAL_APPROVE_TASK_ACCEPTED: _ClassVar[EventType]
    OMNICHANNEL_MANUAL_APPROVE_TASK_REJECTED: _ClassVar[EventType]
    OMNICHANNEL_MANUAL_APPROVE_TASK_TIMEOUT: _ClassVar[EventType]
    OMNICHANNEL_MANUAL_APPROVE_TASK_REQUEUE: _ClassVar[EventType]
    ASM_AGENT_LOGIN: _ClassVar[EventType]
    ASM_OPEN_VOICE: _ClassVar[EventType]
    ASM_OPEN_OMNI_AGENT: _ClassVar[EventType]
    ASM_ACTIVATE_CONVERSATION: _ClassVar[EventType]
    ASM_DEACTIVATE_CONVERSATION: _ClassVar[EventType]
    ASM_AGENT_STATE_CHANGED: _ClassVar[EventType]
    ASM_AGENT_LOGOUT: _ClassVar[EventType]
    ASM_PAUSE_EVENT: _ClassVar[EventType]
    ASM_RESUME_EVENT: _ClassVar[EventType]
    ASM_CONVERSATION_PULLED_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_SCORECARD_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_SCORECARD_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_SCORECARD_EVENT: _ClassVar[EventType]
    SCORECARDS_CLONE_SCORECARD_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_EVALUATION_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_EVALUATION_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_SECTION_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_SECTION_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_SECTION_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_CATEGORY_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_CATEGORY_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_CATEGORY_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_EVALUATION_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_EVALUATION_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_EVALUATION_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_SCORECARD_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_SCORECARD_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_DELETE_SCORECARD_QUESTION_EVENT: _ClassVar[EventType]
    SCORECARDS_CREATE_AUTO_EVALUATION_EVENT: _ClassVar[EventType]
    SCORECARDS_UPDATE_EVALUATION_EVENT: _ClassVar[EventType]
    TICKET_CREATE_EVENT: _ClassVar[EventType]
    TICKET_EDIT_EVENT: _ClassVar[EventType]
    TICKET_CLOSE_EVENT: _ClassVar[EventType]
    TICKET_ACTION_CREATE_EVENT: _ClassVar[EventType]
    TICKET_ACTION_EDIT_EVENT: _ClassVar[EventType]
    TICKET_ACTION_STATE_CHANGE_EVENT: _ClassVar[EventType]
    TICKET_PARTICIPANT_EVENT: _ClassVar[EventType]
    TICKET_CREATE_COMMENT_EVENT: _ClassVar[EventType]
    TICKET_REPLY_COMMENT_EVENT: _ClassVar[EventType]
    COMPLIANCE_RND_QUERY_EVENT: _ClassVar[EventType]
    COMPLIANCE_RND_QUERY_CACHED_EVENT: _ClassVar[EventType]
    AGENT_TRAINING_CREATE_LEARNING_OPPORTUNITY_EVENT: _ClassVar[EventType]
    LMS_PIPELINE_FAILURE_EVENT: _ClassVar[EventType]
    EVENT_TYPE_BILLING_COMMIT_BILLING_PLAN: _ClassVar[EventType]
    EVENT_TYPE_BILLING_CREATE_BILLING_PLAN: _ClassVar[EventType]
    EVENT_TYPE_BILLING_CREATE_INVOICE: _ClassVar[EventType]
    EVENT_TYPE_BILLING_CREATE_RATE_DEFINITION: _ClassVar[EventType]
    EVENT_TYPE_BILLING_DELETE_BILLING_PLAN: _ClassVar[EventType]
    EVENT_TYPE_BILLING_DELETE_INVOICE: _ClassVar[EventType]
    EVENT_TYPE_BILLING_DELETE_RATE_DEFINITION: _ClassVar[EventType]
    EVENT_TYPE_BILLING_EXPORT_INVOICE: _ClassVar[EventType]
    EVENT_TYPE_BILLING_UPDATE_BILLING_PLAN: _ClassVar[EventType]
    EVENT_TYPE_BILLING_UPDATE_INVOICE: _ClassVar[EventType]
    EVENT_TYPE_BILLING_UPDATE_RATE_DEFINITION: _ClassVar[EventType]
DUMMY_APPLICATION: EventType
DUMMY_APPLICATION_STORAGE: EventType
DUMMY_APPLICATION_COMPUTE: EventType
VOICE_ANALYTICS: EventType
VOICE_ANALYTICS_FLAG_OCCURRENCE: EventType
VOICE_ANALYTICS_FLAG_NEEDS_REVIEW: EventType
VOICE_ANALYTICS_BILLING_REPORT: EventType
VOICE_ANALYTICS_FLAG_SUMMARY: EventType
VOICE_ANALYTICS_PHRASE_CORRECTION: EventType
OMNICHANNEL: EventType
OMNICHANNEL_PROJECT: EventType
OMNICHANNEL_CAMPAIGN: EventType
OMNICHANNEL_DAILY_PROJECT_REPORT: EventType
OMNICHANNEL_DAILY_CONVERSATION_REPORT: EventType
OMNICHANNEL_AGENT_ASSIGN_CONVERSATION: EventType
OMNICHANNEL_AGENT_UNASSIGN_CONVERSATION: EventType
OMNICHANNEL_AGENT_REASSIGN_CONVERSATION: EventType
OMNICHANNEL_T10: EventType
OMNICHANNEL_CUSTOMER_TEXT_MESSAGE: EventType
OMNICHANNEL_AGENT_TEXT_MESSAGE: EventType
OMNICHANNEL_FINISH_WRAP_UP: EventType
OMNICHANNEL_BEGIN_WRAP_UP: EventType
OMNICHANNEL_T11: EventType
OMNICHANNEL_CREATE_CONVERSATION: EventType
OMNICHANNEL_AGENT_SUSPEND: EventType
OMNICHANNEL_CLOSE_CONVERSATION: EventType
OMNICHANNEL_MANAGER_TEXT_MESSAGE: EventType
OMNICHANNEL_UPDATE_CAMPAIGN: EventType
OMNICHANNEL_SET_CONVERSATION_COLLECTED_DATA: EventType
OMNICHANNEL_ARCHIVE_CAMPAIGN: EventType
OMNICHANNEL_PAUSE_CAMPAIGN: EventType
OMNICHANNEL_RESUME_CAMPAIGN: EventType
OMNICHANNEL_START_CAMPAIGN: EventType
OMNICHANNEL_SCHEDULE_MODULE: EventType
OMNICHANNEL_START_MODULE: EventType
OMNICHANNEL_PAUSE_MODULE: EventType
OMNICHANNEL_RESUME_MODULE: EventType
OMNICHANNEL_ERROR_MODULE: EventType
OMNICHANNEL_SUCCESS_MODULE: EventType
OMNICHANNEL_FAIL_MODULE: EventType
OMNICHANNEL_COMPLETE_MODULE: EventType
OMNICHANNEL_ARCHIVE_MODULE: EventType
OMNICHANNEL_UPDATE_MODULE: EventType
OMNICHANNEL_MODULE_SMS_MESSAGE_SENT: EventType
OMNICHANNEL_COMPLETE_CAMPAIGN: EventType
OMNICHANNEL_MODULE_INITIAL_REPLY: EventType
OMNICHANNEL_TASK_MESSAGE_SENT: EventType
OMNICHANNEL_CONNECTED_INBOX_POLL: EventType
OMNICHANNEL_CONNECTED_INBOX_CREATED: EventType
OMNICHANNEL_AGENT_MESSAGE_UNITS: EventType
OMNICHANNEL_MANAGER_MESSAGE_UNITS: EventType
OMNICHANNEL_CUSTOMER_MESSAGE_UNITS: EventType
OMNICHANNEL_SYSTEM_MESSAGE_UNITS: EventType
OMNICHANNEL_PAYMENT_LINK_SENT: EventType
OMNICHANNEL_MANUAL_APPROVE_TASK_ACCEPTED: EventType
OMNICHANNEL_MANUAL_APPROVE_TASK_REJECTED: EventType
OMNICHANNEL_MANUAL_APPROVE_TASK_TIMEOUT: EventType
OMNICHANNEL_MANUAL_APPROVE_TASK_REQUEUE: EventType
ASM_AGENT_LOGIN: EventType
ASM_OPEN_VOICE: EventType
ASM_OPEN_OMNI_AGENT: EventType
ASM_ACTIVATE_CONVERSATION: EventType
ASM_DEACTIVATE_CONVERSATION: EventType
ASM_AGENT_STATE_CHANGED: EventType
ASM_AGENT_LOGOUT: EventType
ASM_PAUSE_EVENT: EventType
ASM_RESUME_EVENT: EventType
ASM_CONVERSATION_PULLED_EVENT: EventType
SCORECARDS_CREATE_QUESTION_EVENT: EventType
SCORECARDS_UPDATE_QUESTION_EVENT: EventType
SCORECARDS_DELETE_QUESTION_EVENT: EventType
SCORECARDS_CREATE_SCORECARD_EVENT: EventType
SCORECARDS_UPDATE_SCORECARD_EVENT: EventType
SCORECARDS_DELETE_SCORECARD_EVENT: EventType
SCORECARDS_CLONE_SCORECARD_EVENT: EventType
SCORECARDS_CREATE_EVALUATION_EVENT: EventType
SCORECARDS_DELETE_EVALUATION_EVENT: EventType
SCORECARDS_CREATE_SECTION_EVENT: EventType
SCORECARDS_UPDATE_SECTION_EVENT: EventType
SCORECARDS_DELETE_SECTION_EVENT: EventType
SCORECARDS_CREATE_CATEGORY_EVENT: EventType
SCORECARDS_UPDATE_CATEGORY_EVENT: EventType
SCORECARDS_DELETE_CATEGORY_EVENT: EventType
SCORECARDS_CREATE_EVALUATION_QUESTION_EVENT: EventType
SCORECARDS_UPDATE_EVALUATION_QUESTION_EVENT: EventType
SCORECARDS_DELETE_EVALUATION_QUESTION_EVENT: EventType
SCORECARDS_CREATE_SCORECARD_QUESTION_EVENT: EventType
SCORECARDS_UPDATE_SCORECARD_QUESTION_EVENT: EventType
SCORECARDS_DELETE_SCORECARD_QUESTION_EVENT: EventType
SCORECARDS_CREATE_AUTO_EVALUATION_EVENT: EventType
SCORECARDS_UPDATE_EVALUATION_EVENT: EventType
TICKET_CREATE_EVENT: EventType
TICKET_EDIT_EVENT: EventType
TICKET_CLOSE_EVENT: EventType
TICKET_ACTION_CREATE_EVENT: EventType
TICKET_ACTION_EDIT_EVENT: EventType
TICKET_ACTION_STATE_CHANGE_EVENT: EventType
TICKET_PARTICIPANT_EVENT: EventType
TICKET_CREATE_COMMENT_EVENT: EventType
TICKET_REPLY_COMMENT_EVENT: EventType
COMPLIANCE_RND_QUERY_EVENT: EventType
COMPLIANCE_RND_QUERY_CACHED_EVENT: EventType
AGENT_TRAINING_CREATE_LEARNING_OPPORTUNITY_EVENT: EventType
LMS_PIPELINE_FAILURE_EVENT: EventType
EVENT_TYPE_BILLING_COMMIT_BILLING_PLAN: EventType
EVENT_TYPE_BILLING_CREATE_BILLING_PLAN: EventType
EVENT_TYPE_BILLING_CREATE_INVOICE: EventType
EVENT_TYPE_BILLING_CREATE_RATE_DEFINITION: EventType
EVENT_TYPE_BILLING_DELETE_BILLING_PLAN: EventType
EVENT_TYPE_BILLING_DELETE_INVOICE: EventType
EVENT_TYPE_BILLING_DELETE_RATE_DEFINITION: EventType
EVENT_TYPE_BILLING_EXPORT_INVOICE: EventType
EVENT_TYPE_BILLING_UPDATE_BILLING_PLAN: EventType
EVENT_TYPE_BILLING_UPDATE_INVOICE: EventType
EVENT_TYPE_BILLING_UPDATE_RATE_DEFINITION: EventType
