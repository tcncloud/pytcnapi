import datetime

from api.commons import chat_pb2 as _chat_pb2
from api.commons import enums_pb2 as _enums_pb2
from api.commons import lms_pb2 as _lms_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import types_pb2 as _types_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmsNumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMS_SHORT_CODE_TYPE: _ClassVar[SmsNumberType]
    SMS_ALPHANUMERIC_TYPE: _ClassVar[SmsNumberType]
    SMS_NUMBER_TYPE: _ClassVar[SmsNumberType]

class SmsNumberProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_PROVIDER: _ClassVar[SmsNumberProvider]
    BANDWIDTH_PROVIDER: _ClassVar[SmsNumberProvider]
    BURST_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    PLIVO_PROVIDER: _ClassVar[SmsNumberProvider]
    APEIRON_PROVIDER: _ClassVar[SmsNumberProvider]
    AUSBURST_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    MEDIASAT_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    TEXTLOCAL_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    SMARTPING_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    SINCH_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    PRONTO_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN1_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN2_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN3_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN4_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN5_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN6_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN7_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN8_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN9_SMS_PROVIDER: _ClassVar[SmsNumberProvider]
    UNKNOWN10_SMS_PROVIDER: _ClassVar[SmsNumberProvider]

class OmniCampaignModuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODULE_TYPE_INBOUND: _ClassVar[OmniCampaignModuleType]
    MODULE_TYPE_OUTBOUND: _ClassVar[OmniCampaignModuleType]
    MODULE_TYPE_MANUAL_APPROVAL: _ClassVar[OmniCampaignModuleType]
    MODULE_TYPE_MANUAL: _ClassVar[OmniCampaignModuleType]

class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_TYPE_EMAIL: _ClassVar[ChannelType]
    CHANNEL_TYPE_SMS: _ClassVar[ChannelType]
    CHANNEL_TYPE_CHAT: _ClassVar[ChannelType]
    CHANNEL_TYPE_VOICE: _ClassVar[ChannelType]
    CHANNEL_TYPE_WHATSAPP: _ClassVar[ChannelType]

class OmniCampaignDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INBOUND: _ClassVar[OmniCampaignDirection]
    OUTBOUND: _ClassVar[OmniCampaignDirection]

class OmniCampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULING: _ClassVar[OmniCampaignStatus]
    RUNNING: _ClassVar[OmniCampaignStatus]
    PAUSED: _ClassVar[OmniCampaignStatus]
    COMPLETED: _ClassVar[OmniCampaignStatus]
    ARCHIVED: _ClassVar[OmniCampaignStatus]

class OmniCampaignModuleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODULE_PREPARING: _ClassVar[OmniCampaignModuleStatus]
    MODULE_SCHEDULING: _ClassVar[OmniCampaignModuleStatus]
    MODULE_RUNNING: _ClassVar[OmniCampaignModuleStatus]
    MODULE_RUNNING_ERROR: _ClassVar[OmniCampaignModuleStatus]
    MODULE_ERROR_STANDBY: _ClassVar[OmniCampaignModuleStatus]
    MODULE_PAUSED: _ClassVar[OmniCampaignModuleStatus]
    MODULE_RESUMING: _ClassVar[OmniCampaignModuleStatus]
    MODULE_COMPLETED: _ClassVar[OmniCampaignModuleStatus]
    MODULE_ARCHIVED: _ClassVar[OmniCampaignModuleStatus]

class ConversationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_STATUS_NEW: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_AWAITING_REPLY_FROM_CUSTOMER: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_AWAITING_REPLY_FROM_AGENT: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_CLOSED_TIMEOUT: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_CLOSED_AGENT: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_CLOSED_CUSTOMER: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_SUSPENDED_AWAITING_REPLY_FROM_CUSTOMER: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_AWAITING_ASSIGNMENT: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_NEWLY_ASSIGNED: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_WRAP_UP_CUSTOMER: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_WRAP_UP_TIMEOUT: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_CLOSED_MANAGER: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_NEW_PENDING_CUSTOMER_REPLY: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_FLOW: _ClassVar[ConversationStatus]
    CONVERSATION_STATUS_CLOSED_DUPLICATE_THREAD: _ClassVar[ConversationStatus]

class AgentAssignmentActiveSearchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_ACTIVE: _ClassVar[AgentAssignmentActiveSearchType]
    AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_INACTIVE: _ClassVar[AgentAssignmentActiveSearchType]
    AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_ALL: _ClassVar[AgentAssignmentActiveSearchType]

class AgentConversationAssignmentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVE_AGENT: _ClassVar[AgentConversationAssignmentStatus]
    INACTIVE_AGENT: _ClassVar[AgentConversationAssignmentStatus]

class AgentConversationAssignmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIMARY_AGENT: _ClassVar[AgentConversationAssignmentType]
    SECONDARY_AGENT: _ClassVar[AgentConversationAssignmentType]

class MessageFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_FORMAT_UNSPECIFIED: _ClassVar[MessageFormat]
    MESSAGE_FORMAT_HTML: _ClassVar[MessageFormat]
    MESSAGE_FORMAT_HTML_FORM: _ClassVar[MessageFormat]

class OmniMessageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OMNI_MESSAGE_CREATED: _ClassVar[OmniMessageStatus]
    OMNI_INBOUND_MESSAGE_RECEIVED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_RECEIVED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_WAITING: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_PROCESSING: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_DNC: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_INVALID: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_ATTACHMENT_ERROR: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_CANCELLED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_QUEUED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_DELIVERED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_DROPPED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_DEFERRED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_BOUNCED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_OPENED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_CLICKED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_UNSUBSCRIBED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_MARKED_AS_SPAM: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_BLOCKED: _ClassVar[OmniMessageStatus]
    OMNI_OUTBOUND_MESSAGE_UNCONFIRMED_DELIVERY: _ClassVar[OmniMessageStatus]
    OMNI_SYSTEM_MESSAGE: _ClassVar[OmniMessageStatus]

class OmniConversationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[OmniConversationResult]
    ABANDONED: _ClassVar[OmniConversationResult]

class OmniTaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OMNI_TASK_WAITING: _ClassVar[OmniTaskStatus]
    OMNI_TASK_WAITING_FOR_QUEUE: _ClassVar[OmniTaskStatus]
    OMNI_TASK_WAITING_FOR_APPROVAL: _ClassVar[OmniTaskStatus]
    OMNI_TASK_SENDING: _ClassVar[OmniTaskStatus]
    OMNI_TASK_SENDING_FAILED: _ClassVar[OmniTaskStatus]
    OMNI_TASK_SENDING_INCOMPLETE: _ClassVar[OmniTaskStatus]
    OMNI_TASK_SENDING_INVALID: _ClassVar[OmniTaskStatus]
    OMNI_TASK_SENT: _ClassVar[OmniTaskStatus]
    OMNI_TASK_RECEIVED: _ClassVar[OmniTaskStatus]
    OMNI_TASK_CANCELLED: _ClassVar[OmniTaskStatus]

class OmniSenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OMNI_SENDER_TYPE_AGENT: _ClassVar[OmniSenderType]
    OMNI_SENDER_TYPE_CUSTOMER: _ClassVar[OmniSenderType]
    OMNI_SENDER_TYPE_SYSTEM: _ClassVar[OmniSenderType]
    OMNI_SENDER_TYPE_MANAGER: _ClassVar[OmniSenderType]
    OMNI_SENDER_TYPE_FLOW: _ClassVar[OmniSenderType]

class ConnectedInboxAuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTED_INBOX_AUTHENTICATION_TYPE_PASSWORD: _ClassVar[ConnectedInboxAuthenticationType]
    CONNECTED_INBOX_AUTHENTICATION_TYPE_GOOGLE_XOAUTH2: _ClassVar[ConnectedInboxAuthenticationType]
    CONNECTED_INBOX_AUTHENTICATION_TYPE_MICROSOFT_365: _ClassVar[ConnectedInboxAuthenticationType]

class ConversationStateChangeTimerName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_STATE_CHANGE_TIMER_NAME_WAIT: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_INITIAL_AGENT_RESPONSE: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_AGENT_RESPONSE: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_CUSTOMER_RESPONSE: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_SUSPENDED: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_WRAP_UP: _ClassVar[ConversationStateChangeTimerName]
    CONVERSATION_STATE_CHANGE_TIMER_NAME_IDLE: _ClassVar[ConversationStateChangeTimerName]

class OmniConversationMetadataName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_RESPONSE_TIME: _ClassVar[OmniConversationMetadataName]
    CUSTOMER_WAIT_TIME: _ClassVar[OmniConversationMetadataName]
    HANDLE_TIME: _ClassVar[OmniConversationMetadataName]
    TRANSCRIPT_PATH: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_FLOW_DATA: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_VOICE_DATA: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_WAIT: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_INITIAL_AGENT_RESPONSE: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_AGENT_RESPONSE: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_CUSTOMER_RESPONSE: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_SUSPENDED: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_WRAP_UP: _ClassVar[OmniConversationMetadataName]
    OMNI_CONVERSATION_METADATA_NAME_TIMER_IDLE: _ClassVar[OmniConversationMetadataName]

class ProjectStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROJECT_STATUS_UNKNOWN: _ClassVar[ProjectStatus]
    PROJECT_STATUS_OPEN: _ClassVar[ProjectStatus]
    PROJECT_STATUS_CLOSED: _ClassVar[ProjectStatus]

class CampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAMPAIGN_STATUS_SCHEDULED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_RUNNING: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_PAUSED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_COMPLETED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_CANCELED: _ClassVar[CampaignStatus]
    CAMPAIGN_STATUS_ERROR_PAUSED: _ClassVar[CampaignStatus]

class CampaignDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAMPAIGN_DIRECTION_INBOUND: _ClassVar[CampaignDirection]
    CAMPAIGN_DIRECTION_OUTBOUND: _ClassVar[CampaignDirection]

class WhatsAppNumberProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_WHATSAPP_PROVIDER: _ClassVar[WhatsAppNumberProvider]
    WHATSAPP_SMS_PROVIDER: _ClassVar[WhatsAppNumberProvider]

class OmniMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OMNI_MESSAGE_TYPE_TEXT_MESSAGE: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_TYPING_NOTIFICATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_REASSIGNMENT_NOTIFICATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_ASSIGN_CONVERSATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_UNASSIGN_CONVERSATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_ATTACHMENT: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_ATTACHMENT_UPLOAD_URL: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_REQUEST_ATTACHMENT_UPLOAD_URL: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_CLOSE_CONVERSATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_START_WRAP_UP: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_FINISH_WRAP_UP: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_UNKNOWN: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_SUSPEND: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_QUEUE_INFORMATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_REQUEST_QUEUE_INFORMATION: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_OFFLOADED_TEXT_MESSAGE: _ClassVar[OmniMessageType]
    OMNI_MESSAGE_TYPE_CANNED_MESSAGE: _ClassVar[OmniMessageType]

class OmniTaskCarryOverBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OMNI_TASK_CARRY_OVER_PAUSE: _ClassVar[OmniTaskCarryOverBehavior]
    OMNI_TASK_CARRY_OVER_CANCEL: _ClassVar[OmniTaskCarryOverBehavior]
SMS_SHORT_CODE_TYPE: SmsNumberType
SMS_ALPHANUMERIC_TYPE: SmsNumberType
SMS_NUMBER_TYPE: SmsNumberType
UNKNOWN_PROVIDER: SmsNumberProvider
BANDWIDTH_PROVIDER: SmsNumberProvider
BURST_SMS_PROVIDER: SmsNumberProvider
PLIVO_PROVIDER: SmsNumberProvider
APEIRON_PROVIDER: SmsNumberProvider
AUSBURST_SMS_PROVIDER: SmsNumberProvider
MEDIASAT_SMS_PROVIDER: SmsNumberProvider
TEXTLOCAL_SMS_PROVIDER: SmsNumberProvider
SMARTPING_SMS_PROVIDER: SmsNumberProvider
SINCH_SMS_PROVIDER: SmsNumberProvider
PRONTO_SMS_PROVIDER: SmsNumberProvider
UNKNOWN1_SMS_PROVIDER: SmsNumberProvider
UNKNOWN2_SMS_PROVIDER: SmsNumberProvider
UNKNOWN3_SMS_PROVIDER: SmsNumberProvider
UNKNOWN4_SMS_PROVIDER: SmsNumberProvider
UNKNOWN5_SMS_PROVIDER: SmsNumberProvider
UNKNOWN6_SMS_PROVIDER: SmsNumberProvider
UNKNOWN7_SMS_PROVIDER: SmsNumberProvider
UNKNOWN8_SMS_PROVIDER: SmsNumberProvider
UNKNOWN9_SMS_PROVIDER: SmsNumberProvider
UNKNOWN10_SMS_PROVIDER: SmsNumberProvider
MODULE_TYPE_INBOUND: OmniCampaignModuleType
MODULE_TYPE_OUTBOUND: OmniCampaignModuleType
MODULE_TYPE_MANUAL_APPROVAL: OmniCampaignModuleType
MODULE_TYPE_MANUAL: OmniCampaignModuleType
CHANNEL_TYPE_EMAIL: ChannelType
CHANNEL_TYPE_SMS: ChannelType
CHANNEL_TYPE_CHAT: ChannelType
CHANNEL_TYPE_VOICE: ChannelType
CHANNEL_TYPE_WHATSAPP: ChannelType
INBOUND: OmniCampaignDirection
OUTBOUND: OmniCampaignDirection
SCHEDULING: OmniCampaignStatus
RUNNING: OmniCampaignStatus
PAUSED: OmniCampaignStatus
COMPLETED: OmniCampaignStatus
ARCHIVED: OmniCampaignStatus
MODULE_PREPARING: OmniCampaignModuleStatus
MODULE_SCHEDULING: OmniCampaignModuleStatus
MODULE_RUNNING: OmniCampaignModuleStatus
MODULE_RUNNING_ERROR: OmniCampaignModuleStatus
MODULE_ERROR_STANDBY: OmniCampaignModuleStatus
MODULE_PAUSED: OmniCampaignModuleStatus
MODULE_RESUMING: OmniCampaignModuleStatus
MODULE_COMPLETED: OmniCampaignModuleStatus
MODULE_ARCHIVED: OmniCampaignModuleStatus
CONVERSATION_STATUS_NEW: ConversationStatus
CONVERSATION_STATUS_AWAITING_REPLY_FROM_CUSTOMER: ConversationStatus
CONVERSATION_STATUS_AWAITING_REPLY_FROM_AGENT: ConversationStatus
CONVERSATION_STATUS_CLOSED_TIMEOUT: ConversationStatus
CONVERSATION_STATUS_CLOSED_AGENT: ConversationStatus
CONVERSATION_STATUS_CLOSED_CUSTOMER: ConversationStatus
CONVERSATION_STATUS_SUSPENDED_AWAITING_REPLY_FROM_CUSTOMER: ConversationStatus
CONVERSATION_STATUS_AWAITING_ASSIGNMENT: ConversationStatus
CONVERSATION_STATUS_NEWLY_ASSIGNED: ConversationStatus
CONVERSATION_STATUS_WRAP_UP_CUSTOMER: ConversationStatus
CONVERSATION_STATUS_WRAP_UP_TIMEOUT: ConversationStatus
CONVERSATION_STATUS_CLOSED_MANAGER: ConversationStatus
CONVERSATION_STATUS_NEW_PENDING_CUSTOMER_REPLY: ConversationStatus
CONVERSATION_STATUS_FLOW: ConversationStatus
CONVERSATION_STATUS_CLOSED_DUPLICATE_THREAD: ConversationStatus
AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_ACTIVE: AgentAssignmentActiveSearchType
AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_INACTIVE: AgentAssignmentActiveSearchType
AGENT_ASSIGNMENT_ACTIVE_SEARCH_TYPE_ALL: AgentAssignmentActiveSearchType
ACTIVE_AGENT: AgentConversationAssignmentStatus
INACTIVE_AGENT: AgentConversationAssignmentStatus
PRIMARY_AGENT: AgentConversationAssignmentType
SECONDARY_AGENT: AgentConversationAssignmentType
MESSAGE_FORMAT_UNSPECIFIED: MessageFormat
MESSAGE_FORMAT_HTML: MessageFormat
MESSAGE_FORMAT_HTML_FORM: MessageFormat
OMNI_MESSAGE_CREATED: OmniMessageStatus
OMNI_INBOUND_MESSAGE_RECEIVED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_RECEIVED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_WAITING: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_PROCESSING: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_DNC: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_INVALID: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_ATTACHMENT_ERROR: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_CANCELLED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_QUEUED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_DELIVERED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_DROPPED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_DEFERRED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_BOUNCED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_OPENED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_CLICKED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_UNSUBSCRIBED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_MARKED_AS_SPAM: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_BLOCKED: OmniMessageStatus
OMNI_OUTBOUND_MESSAGE_UNCONFIRMED_DELIVERY: OmniMessageStatus
OMNI_SYSTEM_MESSAGE: OmniMessageStatus
NONE: OmniConversationResult
ABANDONED: OmniConversationResult
OMNI_TASK_WAITING: OmniTaskStatus
OMNI_TASK_WAITING_FOR_QUEUE: OmniTaskStatus
OMNI_TASK_WAITING_FOR_APPROVAL: OmniTaskStatus
OMNI_TASK_SENDING: OmniTaskStatus
OMNI_TASK_SENDING_FAILED: OmniTaskStatus
OMNI_TASK_SENDING_INCOMPLETE: OmniTaskStatus
OMNI_TASK_SENDING_INVALID: OmniTaskStatus
OMNI_TASK_SENT: OmniTaskStatus
OMNI_TASK_RECEIVED: OmniTaskStatus
OMNI_TASK_CANCELLED: OmniTaskStatus
OMNI_SENDER_TYPE_AGENT: OmniSenderType
OMNI_SENDER_TYPE_CUSTOMER: OmniSenderType
OMNI_SENDER_TYPE_SYSTEM: OmniSenderType
OMNI_SENDER_TYPE_MANAGER: OmniSenderType
OMNI_SENDER_TYPE_FLOW: OmniSenderType
CONNECTED_INBOX_AUTHENTICATION_TYPE_PASSWORD: ConnectedInboxAuthenticationType
CONNECTED_INBOX_AUTHENTICATION_TYPE_GOOGLE_XOAUTH2: ConnectedInboxAuthenticationType
CONNECTED_INBOX_AUTHENTICATION_TYPE_MICROSOFT_365: ConnectedInboxAuthenticationType
CONVERSATION_STATE_CHANGE_TIMER_NAME_WAIT: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_INITIAL_AGENT_RESPONSE: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_AGENT_RESPONSE: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_CUSTOMER_RESPONSE: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_TALK_SUSPENDED: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_WRAP_UP: ConversationStateChangeTimerName
CONVERSATION_STATE_CHANGE_TIMER_NAME_IDLE: ConversationStateChangeTimerName
AGENT_RESPONSE_TIME: OmniConversationMetadataName
CUSTOMER_WAIT_TIME: OmniConversationMetadataName
HANDLE_TIME: OmniConversationMetadataName
TRANSCRIPT_PATH: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_FLOW_DATA: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_VOICE_DATA: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_WAIT: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_INITIAL_AGENT_RESPONSE: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_AGENT_RESPONSE: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_CUSTOMER_RESPONSE: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_TALK_SUSPENDED: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_WRAP_UP: OmniConversationMetadataName
OMNI_CONVERSATION_METADATA_NAME_TIMER_IDLE: OmniConversationMetadataName
PROJECT_STATUS_UNKNOWN: ProjectStatus
PROJECT_STATUS_OPEN: ProjectStatus
PROJECT_STATUS_CLOSED: ProjectStatus
CAMPAIGN_STATUS_SCHEDULED: CampaignStatus
CAMPAIGN_STATUS_RUNNING: CampaignStatus
CAMPAIGN_STATUS_PAUSED: CampaignStatus
CAMPAIGN_STATUS_COMPLETED: CampaignStatus
CAMPAIGN_STATUS_CANCELED: CampaignStatus
CAMPAIGN_STATUS_ERROR_PAUSED: CampaignStatus
CAMPAIGN_DIRECTION_INBOUND: CampaignDirection
CAMPAIGN_DIRECTION_OUTBOUND: CampaignDirection
UNKNOWN_WHATSAPP_PROVIDER: WhatsAppNumberProvider
WHATSAPP_SMS_PROVIDER: WhatsAppNumberProvider
OMNI_MESSAGE_TYPE_TEXT_MESSAGE: OmniMessageType
OMNI_MESSAGE_TYPE_TYPING_NOTIFICATION: OmniMessageType
OMNI_MESSAGE_TYPE_REASSIGNMENT_NOTIFICATION: OmniMessageType
OMNI_MESSAGE_TYPE_ASSIGN_CONVERSATION: OmniMessageType
OMNI_MESSAGE_TYPE_UNASSIGN_CONVERSATION: OmniMessageType
OMNI_MESSAGE_TYPE_ATTACHMENT: OmniMessageType
OMNI_MESSAGE_TYPE_ATTACHMENT_UPLOAD_URL: OmniMessageType
OMNI_MESSAGE_TYPE_REQUEST_ATTACHMENT_UPLOAD_URL: OmniMessageType
OMNI_MESSAGE_TYPE_CLOSE_CONVERSATION: OmniMessageType
OMNI_MESSAGE_TYPE_START_WRAP_UP: OmniMessageType
OMNI_MESSAGE_TYPE_FINISH_WRAP_UP: OmniMessageType
OMNI_MESSAGE_TYPE_UNKNOWN: OmniMessageType
OMNI_MESSAGE_TYPE_SUSPEND: OmniMessageType
OMNI_MESSAGE_TYPE_QUEUE_INFORMATION: OmniMessageType
OMNI_MESSAGE_TYPE_REQUEST_QUEUE_INFORMATION: OmniMessageType
OMNI_MESSAGE_TYPE_OFFLOADED_TEXT_MESSAGE: OmniMessageType
OMNI_MESSAGE_TYPE_CANNED_MESSAGE: OmniMessageType
OMNI_TASK_CARRY_OVER_PAUSE: OmniTaskCarryOverBehavior
OMNI_TASK_CARRY_OVER_CANCEL: OmniTaskCarryOverBehavior

class OmniCampaign(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SHORTEN_URL_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    skills: OmniConversationSkills
    start_date: _timestamp_pb2.Timestamp
    status: OmniCampaignStatus
    channel_type: ChannelType
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    project_sid: int
    modules: _containers.RepeatedCompositeFieldContainer[OmniCampaignModule]
    time_zone: _org_pb2.TimeZoneWrapper
    shorten_url: bool
    compliance_config: OmniComplianceConfig
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skills: _Optional[_Union[OmniConversationSkills, _Mapping]] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[OmniCampaignStatus, str]] = ..., channel_type: _Optional[_Union[ChannelType, str]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., project_sid: _Optional[int] = ..., modules: _Optional[_Iterable[_Union[OmniCampaignModule, _Mapping]]] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., shorten_url: _Optional[bool] = ..., compliance_config: _Optional[_Union[OmniComplianceConfig, _Mapping]] = ...) -> None: ...

class OmniCampaignModule(_message.Message):
    __slots__ = ()
    class Details(_message.Message):
        __slots__ = ()
        TOTAL_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_INBOX_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        VERIFIED_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PENDING_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        FAILED_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        CANCELED_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
        total_task_count: _wrappers_pb2.Int64Value
        completed_task_count: _wrappers_pb2.Int64Value
        connected_inbox_address: _wrappers_pb2.StringValue
        verified_email_address: _wrappers_pb2.StringValue
        pending_task_count: _wrappers_pb2.Int64Value
        failed_task_count: _wrappers_pb2.Int64Value
        canceled_task_count: _wrappers_pb2.Int64Value
        def __init__(self, total_task_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., completed_task_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., connected_inbox_address: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., verified_email_address: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., pending_task_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., failed_task_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., canceled_task_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_STOP_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_STOP_DATE_FIELD_NUMBER: _ClassVar[int]
    HOURS_OF_OPERATION_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    HOURS_OF_OPERATION_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_TIMEZONE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    TASK_CARRY_OVER_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    campaign_module_sid: int
    campaign_sid: int
    module_type: OmniCampaignModuleType
    status: OmniCampaignModuleStatus
    config: OmniCampaignModuleConfig
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    scheduled_stop_date: _timestamp_pb2.Timestamp
    actual_stop_date: _timestamp_pb2.Timestamp
    hours_of_operation: WeekdayTimeRange
    details: OmniCampaignModule.Details
    attachments: _containers.RepeatedCompositeFieldContainer[OmniAttachment]
    hours_of_operation_timezone: WeekdayTimeRange
    global_timezone_ordering: bool
    task_carry_over_behavior: OmniTaskCarryOverBehavior
    def __init__(self, campaign_module_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., module_type: _Optional[_Union[OmniCampaignModuleType, str]] = ..., status: _Optional[_Union[OmniCampaignModuleStatus, str]] = ..., config: _Optional[_Union[OmniCampaignModuleConfig, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_stop_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actual_stop_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., hours_of_operation: _Optional[_Union[WeekdayTimeRange, _Mapping]] = ..., details: _Optional[_Union[OmniCampaignModule.Details, _Mapping]] = ..., attachments: _Optional[_Iterable[_Union[OmniAttachment, _Mapping]]] = ..., hours_of_operation_timezone: _Optional[_Union[WeekdayTimeRange, _Mapping]] = ..., global_timezone_ordering: _Optional[bool] = ..., task_carry_over_behavior: _Optional[_Union[OmniTaskCarryOverBehavior, str]] = ...) -> None: ...

class OmniCampaignModuleConfig(_message.Message):
    __slots__ = ()
    class ProviderMetadataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_KEY_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SECONDARY_FIELD_NUMBER: _ClassVar[int]
    COLOR_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_SID_FIELD_NUMBER: _ClassVar[int]
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SLA_TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    SENDS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    STOP_ON_TASK_DEPLETE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PORTAL_IDS_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_METADATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_SID_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    api_key_primary: _wrappers_pb2.StringValue
    api_key_secondary: _wrappers_pb2.StringValue
    color_properties: _chat_pb2.ChatColorProperties
    connected_inbox_sid: _types_pb2.Int64Id
    dispositions: _containers.RepeatedCompositeFieldContainer[Disposition]
    email: _wrappers_pb2.StringValue
    message_body: _wrappers_pb2.StringValue
    email_subject: _wrappers_pb2.StringValue
    sms_number: SmsNumber
    header: _chat_pb2.ChatHeader
    sla_timeouts: SLATimeouts
    sends_per_hour: _wrappers_pb2.Int64Value
    unsubscribe_link_sid: _types_pb2.Int64Id
    verified_email_sid: _types_pb2.Int64Id
    stop_on_task_deplete: _wrappers_pb2.BoolValue
    attachments: _containers.RepeatedCompositeFieldContainer[OmniAttachment]
    compliance_rule_set_id: _wrappers_pb2.StringValue
    payment_portal_ids: _containers.RepeatedScalarFieldContainer[str]
    flow_id: _types_pb2.Int64Id
    skills: OmniConversationSkills
    whatsapp_number: WhatsAppNumber
    provider_metadata: _containers.ScalarMap[str, str]
    country_code: int
    country_code_sid: int
    postal_code_field: str
    timeout_message_config: ConversationTimeoutMessageConfig
    def __init__(self, api_key_primary: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., api_key_secondary: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., color_properties: _Optional[_Union[_chat_pb2.ChatColorProperties, _Mapping]] = ..., connected_inbox_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., dispositions: _Optional[_Iterable[_Union[Disposition, _Mapping]]] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., message_body: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., email_subject: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sms_number: _Optional[_Union[SmsNumber, _Mapping]] = ..., header: _Optional[_Union[_chat_pb2.ChatHeader, _Mapping]] = ..., sla_timeouts: _Optional[_Union[SLATimeouts, _Mapping]] = ..., sends_per_hour: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., unsubscribe_link_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., verified_email_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., stop_on_task_deplete: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., attachments: _Optional[_Iterable[_Union[OmniAttachment, _Mapping]]] = ..., compliance_rule_set_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., payment_portal_ids: _Optional[_Iterable[str]] = ..., flow_id: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., skills: _Optional[_Union[OmniConversationSkills, _Mapping]] = ..., whatsapp_number: _Optional[_Union[WhatsAppNumber, _Mapping]] = ..., provider_metadata: _Optional[_Mapping[str, str]] = ..., country_code: _Optional[int] = ..., country_code_sid: _Optional[int] = ..., postal_code_field: _Optional[str] = ..., timeout_message_config: _Optional[_Union[ConversationTimeoutMessageConfig, _Mapping]] = ...) -> None: ...

class ConversationTimeoutMessageConfig(_message.Message):
    __slots__ = ()
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    is_disabled: bool
    msg: str
    def __init__(self, is_disabled: _Optional[bool] = ..., msg: _Optional[str] = ...) -> None: ...

class SmsNumber(_message.Message):
    __slots__ = ()
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    number: str
    type: SmsNumberType
    provider: SmsNumberProvider
    country_code: int
    def __init__(self, number: _Optional[str] = ..., type: _Optional[_Union[SmsNumberType, str]] = ..., provider: _Optional[_Union[SmsNumberProvider, str]] = ..., country_code: _Optional[int] = ...) -> None: ...

class ConversationCustomerInformation(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    phone_number: str
    email_address: str
    def __init__(self, name: _Optional[str] = ..., phone_number: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...

class SLATimeouts(_message.Message):
    __slots__ = ()
    T1_FIELD_NUMBER: _ClassVar[int]
    T2_FIELD_NUMBER: _ClassVar[int]
    T3_FIELD_NUMBER: _ClassVar[int]
    T10_FIELD_NUMBER: _ClassVar[int]
    T11_FIELD_NUMBER: _ClassVar[int]
    T12_FIELD_NUMBER: _ClassVar[int]
    t1: int
    t2: int
    t3: int
    t10: int
    t11: int
    t12: int
    def __init__(self, t1: _Optional[int] = ..., t2: _Optional[int] = ..., t3: _Optional[int] = ..., t10: _Optional[int] = ..., t11: _Optional[int] = ..., t12: _Optional[int] = ...) -> None: ...

class ConversationCollectedData(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ConversationCollectedData_Item]
    def __init__(self, items: _Optional[_Iterable[_Union[ConversationCollectedData_Item, _Mapping]]] = ...) -> None: ...

class ConversationCollectedData_Item(_message.Message):
    __slots__ = ()
    CONVERSATION_COLLECTED_DATA_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    DATA_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_collected_data_sid: int
    conversation_sid: int
    data_name: str
    data_value: str
    collection_time: _timestamp_pb2.Timestamp
    user_id: _wrappers_pb2.StringValue
    def __init__(self, conversation_collected_data_sid: _Optional[int] = ..., conversation_sid: _Optional[int] = ..., data_name: _Optional[str] = ..., data_value: _Optional[str] = ..., collection_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class OmniMessage(_message.Message):
    __slots__ = ()
    MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_FROM_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    UI_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    message_sid: int
    user_id: _wrappers_pb2.StringValue
    sent_from: str
    sent_to: str
    channel_type: ChannelType
    reference_id: _wrappers_pb2.StringValue
    ui_reference_id: str
    payload: OmniMessagePayload
    conversation_sid: _types_pb2.Int64Id
    status: OmniMessageStatus
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    campaign_sid: int
    subject: _wrappers_pb2.StringValue
    sender_type: OmniSenderType
    status_message: _wrappers_pb2.StringValue
    message_format: MessageFormat
    def __init__(self, message_sid: _Optional[int] = ..., user_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sent_from: _Optional[str] = ..., sent_to: _Optional[str] = ..., channel_type: _Optional[_Union[ChannelType, str]] = ..., reference_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ui_reference_id: _Optional[str] = ..., payload: _Optional[_Union[OmniMessagePayload, _Mapping]] = ..., conversation_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., status: _Optional[_Union[OmniMessageStatus, str]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., campaign_sid: _Optional[int] = ..., subject: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sender_type: _Optional[_Union[OmniSenderType, str]] = ..., status_message: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., message_format: _Optional[_Union[MessageFormat, str]] = ...) -> None: ...

class CustomerChatWidgetMessage(_message.Message):
    __slots__ = ()
    MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    UI_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    message_sid: int
    payload: OmniMessagePayload
    date_created: _timestamp_pb2.Timestamp
    ui_reference_id: str
    customer_information: ConversationCustomerInformation
    def __init__(self, message_sid: _Optional[int] = ..., payload: _Optional[_Union[OmniMessagePayload, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ui_reference_id: _Optional[str] = ..., customer_information: _Optional[_Union[ConversationCustomerInformation, _Mapping]] = ...) -> None: ...

class AgentChatWidgetMessage(_message.Message):
    __slots__ = ()
    MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    UI_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    message_sid: int
    payload: OmniMessagePayload
    date_created: _timestamp_pb2.Timestamp
    ui_reference_id: str
    user_information: OmniConversationUserInformation
    sender_type: OmniSenderType
    message_format: MessageFormat
    def __init__(self, message_sid: _Optional[int] = ..., payload: _Optional[_Union[OmniMessagePayload, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ui_reference_id: _Optional[str] = ..., user_information: _Optional[_Union[OmniConversationUserInformation, _Mapping]] = ..., sender_type: _Optional[_Union[OmniSenderType, str]] = ..., message_format: _Optional[_Union[MessageFormat, str]] = ...) -> None: ...

class OmniMessagePayload(_message.Message):
    __slots__ = ()
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TYPING_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ATTACHMENT_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    UNASSIGN_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    FINISH_WRAP_UP_FIELD_NUMBER: _ClassVar[int]
    SUSPEND_FIELD_NUMBER: _ClassVar[int]
    START_WRAP_UP_FIELD_NUMBER: _ClassVar[int]
    QUEUE_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_QUEUE_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    OFF_LOADED_TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CANNED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    text_message: OmniTextMessage
    typing_notification: OmniTypingNotification
    reassignment: OmniReassignmentNotification
    request_attachment_upload_url: OmniRequestAttachmentUploadURL
    attachment_upload_url: OmniAttachmentUploadURL
    attachment: OmniAttachment
    close_conversation: OmniCloseConversation
    assign_conversation: OmniAssignConversation
    unassign_conversation: OmniUnassignConversation
    finish_wrap_up: OmniFinishWrapUp
    suspend: OmniSuspend
    start_wrap_up: OmniStartWrapUp
    queue_information: OmniQueueInformation
    request_queue_information: OmniRequestQueueInformation
    off_loaded_text_message: OmniOffLoadedTextMessage
    canned_message: OmniCannedMessage
    data_message: OmniDataMessage
    def __init__(self, text_message: _Optional[_Union[OmniTextMessage, _Mapping]] = ..., typing_notification: _Optional[_Union[OmniTypingNotification, _Mapping]] = ..., reassignment: _Optional[_Union[OmniReassignmentNotification, _Mapping]] = ..., request_attachment_upload_url: _Optional[_Union[OmniRequestAttachmentUploadURL, _Mapping]] = ..., attachment_upload_url: _Optional[_Union[OmniAttachmentUploadURL, _Mapping]] = ..., attachment: _Optional[_Union[OmniAttachment, _Mapping]] = ..., close_conversation: _Optional[_Union[OmniCloseConversation, _Mapping]] = ..., assign_conversation: _Optional[_Union[OmniAssignConversation, _Mapping]] = ..., unassign_conversation: _Optional[_Union[OmniUnassignConversation, _Mapping]] = ..., finish_wrap_up: _Optional[_Union[OmniFinishWrapUp, _Mapping]] = ..., suspend: _Optional[_Union[OmniSuspend, _Mapping]] = ..., start_wrap_up: _Optional[_Union[OmniStartWrapUp, _Mapping]] = ..., queue_information: _Optional[_Union[OmniQueueInformation, _Mapping]] = ..., request_queue_information: _Optional[_Union[OmniRequestQueueInformation, _Mapping]] = ..., off_loaded_text_message: _Optional[_Union[OmniOffLoadedTextMessage, _Mapping]] = ..., canned_message: _Optional[_Union[OmniCannedMessage, _Mapping]] = ..., data_message: _Optional[_Union[OmniDataMessage, _Mapping]] = ...) -> None: ...

class OmniTextMessage(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    message: str
    attachments: _containers.RepeatedCompositeFieldContainer[OmniAttachment]
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, message: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[OmniAttachment, _Mapping]]] = ..., primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniOffLoadedTextMessage(_message.Message):
    __slots__ = ()
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    location: str
    attachments: _containers.RepeatedCompositeFieldContainer[OmniAttachment]
    def __init__(self, location: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[OmniAttachment, _Mapping]]] = ...) -> None: ...

class OmniTypingNotification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OmniAssignConversation(_message.Message):
    __slots__ = ()
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_name: str
    primary_asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., primary_asm_session_sid: _Optional[int] = ...) -> None: ...

class OmniReassignmentNotification(_message.Message):
    __slots__ = ()
    CURRENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    current_user_id: str
    current_user_name: str
    new_user_id: str
    new_user_name: str
    new_user_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, current_user_id: _Optional[str] = ..., current_user_name: _Optional[str] = ..., new_user_id: _Optional[str] = ..., new_user_name: _Optional[str] = ..., new_user_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniUnassignConversation(_message.Message):
    __slots__ = ()
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: _wrappers_pb2.StringValue
    user_name: str
    all: bool
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, user_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_name: _Optional[str] = ..., all: _Optional[bool] = ..., primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniRequestAttachmentUploadURL(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OmniAttachmentUploadURL(_message.Message):
    __slots__ = ()
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    id: str
    def __init__(self, upload_url: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class OmniAttachment(_message.Message):
    __slots__ = ()
    OMNI_ATTACHMENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TEMP_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    omni_attachment_sid: int
    name: str
    file_type: str
    file_size: int
    path: str
    temp_id: _wrappers_pb2.StringValue
    download_url: str
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    content_id: _wrappers_pb2.StringValue
    width: _wrappers_pb2.StringValue
    height: _wrappers_pb2.StringValue
    def __init__(self, omni_attachment_sid: _Optional[int] = ..., name: _Optional[str] = ..., file_type: _Optional[str] = ..., file_size: _Optional[int] = ..., path: _Optional[str] = ..., temp_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., download_url: _Optional[str] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., content_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., width: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., height: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class OmniStartWrapUp(_message.Message):
    __slots__ = ()
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniFinishWrapUp(_message.Message):
    __slots__ = ()
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniSuspend(_message.Message):
    __slots__ = ()
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniCloseConversation(_message.Message):
    __slots__ = ()
    PRIMARY_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    primary_asm_session_sid: _wrappers_pb2.Int64Value
    user_name: str
    def __init__(self, primary_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., user_name: _Optional[str] = ...) -> None: ...

class OmniQueueInformation(_message.Message):
    __slots__ = ()
    POSITION_FIELD_NUMBER: _ClassVar[int]
    position: int
    def __init__(self, position: _Optional[int] = ...) -> None: ...

class OmniRequestQueueInformation(_message.Message):
    __slots__ = ()
    POSITION_FIELD_NUMBER: _ClassVar[int]
    position: bool
    def __init__(self, position: _Optional[bool] = ...) -> None: ...

class OmniCannedMessage(_message.Message):
    __slots__ = ()
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    def __init__(self, canned_message_id: _Optional[str] = ...) -> None: ...

class OmniDataMessage(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    message: str
    message_sid: int
    def __init__(self, message: _Optional[str] = ..., message_sid: _Optional[int] = ...) -> None: ...

class OmniConversationUserInformation(_message.Message):
    __slots__ = ()
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CustomerCollectedData(_message.Message):
    __slots__ = ()
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CustomerCollectedDataItem]
    def __init__(self, items: _Optional[_Iterable[_Union[CustomerCollectedDataItem, _Mapping]]] = ...) -> None: ...

class CustomerCollectedDataItem(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class OmniConversation(_message.Message):
    __slots__ = ()
    class ConversationDetails(_message.Message):
        __slots__ = ()
        CAMPAIGN_NAME_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_EMAIL_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_SHORTEN_URL_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_PORTAL_IDS_FIELD_NUMBER: _ClassVar[int]
        campaign_name: str
        support_email: str
        campaign_shorten_url: bool
        payment_portal_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, campaign_name: _Optional[str] = ..., support_email: _Optional[str] = ..., campaign_shorten_url: _Optional[bool] = ..., payment_portal_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COLLECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    SLA_TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_GROUP_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_CHANGED_TIME_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    channel_type: ChannelType
    skills: OmniConversationSkills
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    status: ConversationStatus
    customer_email_address: _wrappers_pb2.StringValue
    customer_phone_number: _wrappers_pb2.StringValue
    customer_name: _wrappers_pb2.StringValue
    campaign_sid: int
    reference_id: _wrappers_pb2.StringValue
    last_message_time: _timestamp_pb2.Timestamp
    conversation_collected_data: ConversationCollectedData
    sla_timeouts: SLATimeouts
    conversation_assignments: _containers.RepeatedCompositeFieldContainer[OmniConversationAssignment]
    metadata: OmniConversation.ConversationDetails
    end_time: _timestamp_pb2.Timestamp
    campaign_module_sid: int
    last_message_group_time: _timestamp_pb2.Timestamp
    last_message_group_type: OmniSenderType
    result: OmniConversationResult
    last_state_changed_time: _timestamp_pb2.Timestamp
    task_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., channel_type: _Optional[_Union[ChannelType, str]] = ..., skills: _Optional[_Union[OmniConversationSkills, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[ConversationStatus, str]] = ..., customer_email_address: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., customer_phone_number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., customer_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., campaign_sid: _Optional[int] = ..., reference_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., last_message_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., conversation_collected_data: _Optional[_Union[ConversationCollectedData, _Mapping]] = ..., sla_timeouts: _Optional[_Union[SLATimeouts, _Mapping]] = ..., conversation_assignments: _Optional[_Iterable[_Union[OmniConversationAssignment, _Mapping]]] = ..., metadata: _Optional[_Union[OmniConversation.ConversationDetails, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., campaign_module_sid: _Optional[int] = ..., last_message_group_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_message_group_type: _Optional[_Union[OmniSenderType, str]] = ..., result: _Optional[_Union[OmniConversationResult, str]] = ..., last_state_changed_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., task_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmniConversationAssignment(_message.Message):
    __slots__ = ()
    class ConversationAssignmentDetails(_message.Message):
        __slots__ = ()
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        user_name: str
        def __init__(self, user_name: _Optional[str] = ...) -> None: ...
    CONVERSATION_ASSIGNMENT_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_assignment_sid: int
    conversation_sid: int
    is_active: bool
    assignment_type: AgentConversationAssignmentType
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    user_id: str
    metadata: OmniConversationAssignment.ConversationAssignmentDetails
    asm_session_sid: int
    def __init__(self, conversation_assignment_sid: _Optional[int] = ..., conversation_sid: _Optional[int] = ..., is_active: _Optional[bool] = ..., assignment_type: _Optional[_Union[AgentConversationAssignmentType, str]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., metadata: _Optional[_Union[OmniConversationAssignment.ConversationAssignmentDetails, _Mapping]] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class OmniConversationSkills(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.ScalarMap[str, bool]
    def __init__(self, skills: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class WeekdayTimeRange(_message.Message):
    __slots__ = ()
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[WeekdayTimeRangeEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[WeekdayTimeRangeEntry, _Mapping]]] = ...) -> None: ...

class WeekdayTimeRangeEntry(_message.Message):
    __slots__ = ()
    START_DAY_FIELD_NUMBER: _ClassVar[int]
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_DAY_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    start_day: _enums_pb2.Weekday.Enum
    start_hour: int
    start_minute: int
    end_day: _enums_pb2.Weekday.Enum
    end_hour: int
    end_minute: int
    def __init__(self, start_day: _Optional[_Union[_enums_pb2.Weekday.Enum, str]] = ..., start_hour: _Optional[int] = ..., start_minute: _Optional[int] = ..., end_day: _Optional[_Union[_enums_pb2.Weekday.Enum, str]] = ..., end_hour: _Optional[int] = ..., end_minute: _Optional[int] = ...) -> None: ...

class Disposition(_message.Message):
    __slots__ = ()
    DISPOSITION_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    disposition_sid: int
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    disposition: str
    deleted: bool
    def __init__(self, disposition_sid: _Optional[int] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., disposition: _Optional[str] = ..., deleted: _Optional[bool] = ...) -> None: ...

class GetQueuesDetailsRes(_message.Message):
    __slots__ = ()
    class QueueDetails(_message.Message):
        __slots__ = ()
        CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
        QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
        channel_type: ChannelType
        queueSize: int
        def __init__(self, channel_type: _Optional[_Union[ChannelType, str]] = ..., queueSize: _Optional[int] = ...) -> None: ...
    QUEUE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    queue_details: _containers.RepeatedCompositeFieldContainer[GetQueuesDetailsRes.QueueDetails]
    def __init__(self, queue_details: _Optional[_Iterable[_Union[GetQueuesDetailsRes.QueueDetails, _Mapping]]] = ...) -> None: ...

class OmniCustomUnsubscribeLink(_message.Message):
    __slots__ = ()
    CUSTOM_UNSUBSCRIBE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_URL_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DATE_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    custom_unsubscribe_link_sid: int
    link_name: str
    link_url: str
    validated: bool
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    date_validated: _timestamp_pb2.Timestamp
    description: str
    deleted: bool
    def __init__(self, custom_unsubscribe_link_sid: _Optional[int] = ..., link_name: _Optional[str] = ..., link_url: _Optional[str] = ..., validated: _Optional[bool] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_validated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., deleted: _Optional[bool] = ...) -> None: ...

class ContactList(_message.Message):
    __slots__ = ()
    class Metadata(_message.Message):
        __slots__ = ()
        ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        entry_count: int
        def __init__(self, entry_count: _Optional[int] = ...) -> None: ...
    CONTACT_LIST_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    contact_list_sid: int
    name: str
    description: str
    field_names: _containers.RepeatedScalarFieldContainer[str]
    project_sid: _types_pb2.Int64Id
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    contact_entries: _containers.RepeatedCompositeFieldContainer[ContactEntry]
    metadata: ContactList.Metadata
    def __init__(self, contact_list_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., field_names: _Optional[_Iterable[str]] = ..., project_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contact_entries: _Optional[_Iterable[_Union[ContactEntry, _Mapping]]] = ..., metadata: _Optional[_Union[ContactList.Metadata, _Mapping]] = ...) -> None: ...

class ContactEntry(_message.Message):
    __slots__ = ()
    CONTACT_ENTRY_SID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    contact_entry_sid: int
    contact_list_sid: int
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    field_names: _containers.RepeatedScalarFieldContainer[str]
    data_fields: _containers.RepeatedCompositeFieldContainer[OmniDataField]
    def __init__(self, contact_entry_sid: _Optional[int] = ..., contact_list_sid: _Optional[int] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., field_names: _Optional[_Iterable[str]] = ..., data_fields: _Optional[_Iterable[_Union[OmniDataField, _Mapping]]] = ...) -> None: ...

class OmniTask(_message.Message):
    __slots__ = ()
    class Details(_message.Message):
        __slots__ = ()
        CONTACT_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
        contact_list_name: _wrappers_pb2.StringValue
        def __init__(self, contact_list_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRY_SID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    TASK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    status: OmniTaskStatus
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    campaign_module_sid: int
    campaign_sid: int
    contact_entry_sid: _types_pb2.Int64Id
    state: OmniTaskState
    data_fields: _containers.RepeatedCompositeFieldContainer[OmniDataField]
    details: OmniTask.Details
    name: str
    status_message: _wrappers_pb2.StringValue
    scheduled_time: _timestamp_pb2.Timestamp
    task_config: OmniTaskConfig
    timezone_offset: float
    def __init__(self, task_sid: _Optional[int] = ..., status: _Optional[_Union[OmniTaskStatus, str]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., campaign_module_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., contact_entry_sid: _Optional[_Union[_types_pb2.Int64Id, _Mapping]] = ..., state: _Optional[_Union[OmniTaskState, _Mapping]] = ..., data_fields: _Optional[_Iterable[_Union[OmniDataField, _Mapping]]] = ..., details: _Optional[_Union[OmniTask.Details, _Mapping]] = ..., name: _Optional[str] = ..., status_message: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., scheduled_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., task_config: _Optional[_Union[OmniTaskConfig, _Mapping]] = ..., timezone_offset: _Optional[float] = ...) -> None: ...

class OmniTaskConfig(_message.Message):
    __slots__ = ()
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    AGENT_TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    skills: OmniConversationSkills
    absolute_timeout_duration: _duration_pb2.Duration
    agent_timeout_duration: _duration_pb2.Duration
    subject: str
    message: OmniMessagePayload
    user_id: str
    def __init__(self, skills: _Optional[_Union[OmniConversationSkills, _Mapping]] = ..., absolute_timeout_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., agent_timeout_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[OmniMessagePayload, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class OmniTaskState(_message.Message):
    __slots__ = ()
    class Entry(_message.Message):
        __slots__ = ()
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TIMES_USED_FIELD_NUMBER: _ClassVar[int]
        LAST_USED_FIELD_NUMBER: _ClassVar[int]
        address: str
        times_used: int
        last_used: _timestamp_pb2.Timestamp
        def __init__(self, address: _Optional[str] = ..., times_used: _Optional[int] = ..., last_used: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[OmniTaskState.Entry]
    sources: _containers.RepeatedCompositeFieldContainer[OmniTaskState.Entry]
    rule_set: ComplianceRuleSet
    scrub_list_id: _wrappers_pb2.StringValue
    def __init__(self, destinations: _Optional[_Iterable[_Union[OmniTaskState.Entry, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[OmniTaskState.Entry, _Mapping]]] = ..., rule_set: _Optional[_Union[ComplianceRuleSet, _Mapping]] = ..., scrub_list_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ComplianceRuleSet(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    sha: str
    rules: _containers.RepeatedCompositeFieldContainer[ComplianceRule]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., sha: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[ComplianceRule, _Mapping]]] = ...) -> None: ...

class ComplianceRule(_message.Message):
    __slots__ = ()
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMIT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    text: str
    permit: bool
    plugin_response: str
    def __init__(self, text: _Optional[str] = ..., permit: _Optional[bool] = ..., plugin_response: _Optional[str] = ...) -> None: ...

class OmniDataField(_message.Message):
    __slots__ = ()
    FIELD_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    field_sid: int
    parent_sid: int
    name: str
    value: str
    type: _lms_pb2.FieldType
    def __init__(self, field_sid: _Optional[int] = ..., parent_sid: _Optional[int] = ..., name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[_Union[_lms_pb2.FieldType, str]] = ...) -> None: ...

class ConnectedInbox(_message.Message):
    __slots__ = ()
    CONNECTED_INBOX_SID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CHECK_FREQUENCY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_FIELD_NUMBER: _ClassVar[int]
    PURGE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SALT_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSECUTIVE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    STANDBY_ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_XOAUTH2_REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_XOAUTH2_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_XOAUTH2_ACCESS_TOKEN_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    OAUTH_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    connected_inbox_sid: int
    email_address: str
    username: str
    password: str
    check_frequency_minutes: int
    server_name: str
    server_port: int
    last_scheduled_time: _timestamp_pb2.Timestamp
    last_checked: _timestamp_pb2.Timestamp
    purge_threshold: int
    email_salt: str
    num_consecutive_failures: int
    last_error: _wrappers_pb2.StringValue
    standby_error_time: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    max_message_size: int
    max_messages: int
    google_xoauth2_refresh_token: _wrappers_pb2.StringValue
    google_xoauth2_access_token: _wrappers_pb2.StringValue
    google_xoauth2_access_token_expiration: _timestamp_pb2.Timestamp
    authentication_type: ConnectedInboxAuthenticationType
    oauth_reference_id: ConnectedInboxOAuthConfig
    def __init__(self, connected_inbox_sid: _Optional[int] = ..., email_address: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., check_frequency_minutes: _Optional[int] = ..., server_name: _Optional[str] = ..., server_port: _Optional[int] = ..., last_scheduled_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_checked: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., purge_threshold: _Optional[int] = ..., email_salt: _Optional[str] = ..., num_consecutive_failures: _Optional[int] = ..., last_error: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., standby_error_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., max_message_size: _Optional[int] = ..., max_messages: _Optional[int] = ..., google_xoauth2_refresh_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., google_xoauth2_access_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., google_xoauth2_access_token_expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., authentication_type: _Optional[_Union[ConnectedInboxAuthenticationType, str]] = ..., oauth_reference_id: _Optional[_Union[ConnectedInboxOAuthConfig, _Mapping]] = ...) -> None: ...

class ConnectedInboxOAuthConfig(_message.Message):
    __slots__ = ()
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    expires_at: int
    reference_id: str
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_at: _Optional[int] = ..., reference_id: _Optional[str] = ...) -> None: ...

class VerifiedEmail(_message.Message):
    __slots__ = ()
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_ON_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    email_address: str
    verified: bool
    created_on: _timestamp_pb2.Timestamp
    verified_on: _timestamp_pb2.Timestamp
    deleted: bool
    description: _wrappers_pb2.StringValue
    def __init__(self, verified_email_sid: _Optional[int] = ..., email_address: _Optional[str] = ..., verified: _Optional[bool] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., verified_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: _Optional[bool] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ()
    SIGNATURE_SID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DELETED_ON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    signature_sid: int
    signature: str
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    deleted_on: _timestamp_pb2.Timestamp
    name: str
    description: str
    def __init__(self, signature_sid: _Optional[int] = ..., signature: _Optional[str] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class OmniProjectComplianceConfig(_message.Message):
    __slots__ = ()
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_FIELD_NUMBER: _ClassVar[int]
    email: OmniComplianceConfig
    sms: OmniComplianceConfig
    whatsapp: OmniComplianceConfig
    def __init__(self, email: _Optional[_Union[OmniComplianceConfig, _Mapping]] = ..., sms: _Optional[_Union[OmniComplianceConfig, _Mapping]] = ..., whatsapp: _Optional[_Union[OmniComplianceConfig, _Mapping]] = ...) -> None: ...

class OmniComplianceAction(_message.Message):
    __slots__ = ()
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_FUZZY_MATCH_FIELD_NUMBER: _ClassVar[int]
    keywords: _containers.RepeatedScalarFieldContainer[str]
    confirmation_message: str
    is_fuzzy_match: bool
    def __init__(self, keywords: _Optional[_Iterable[str]] = ..., confirmation_message: _Optional[str] = ..., is_fuzzy_match: _Optional[bool] = ...) -> None: ...

class OmniComplianceConfig(_message.Message):
    __slots__ = ()
    OPT_IN_FIELD_NUMBER: _ClassVar[int]
    OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    opt_in: OmniComplianceAction
    opt_out: OmniComplianceAction
    help: OmniComplianceAction
    information: OmniComplianceAction
    scrub_list_id: str
    rule_set_id: _wrappers_pb2.StringValue
    def __init__(self, opt_in: _Optional[_Union[OmniComplianceAction, _Mapping]] = ..., opt_out: _Optional[_Union[OmniComplianceAction, _Mapping]] = ..., help: _Optional[_Union[OmniComplianceAction, _Mapping]] = ..., information: _Optional[_Union[OmniComplianceAction, _Mapping]] = ..., scrub_list_id: _Optional[str] = ..., rule_set_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class WhatsAppNumber(_message.Message):
    __slots__ = ()
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    number: str
    provider: WhatsAppNumberProvider
    country_code: int
    whatsapp_number_sid: int
    display_name: str
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    def __init__(self, number: _Optional[str] = ..., provider: _Optional[_Union[WhatsAppNumberProvider, str]] = ..., country_code: _Optional[int] = ..., whatsapp_number_sid: _Optional[int] = ..., display_name: _Optional[str] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
