from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EmailResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EMAIL_RESULT_UNKNOWN: _ClassVar[EmailResult]
    EMAIL_TASK_WAITING: _ClassVar[EmailResult]
    EMAIL_TASK_PROCESSING: _ClassVar[EmailResult]
    EMAIL_TASK_DNC: _ClassVar[EmailResult]
    EMAIL_TASK_INVALID: _ClassVar[EmailResult]
    EMAIL_TASK_ATTACHMENT_ERROR: _ClassVar[EmailResult]
    EMAIL_TASK_CANCELLED: _ClassVar[EmailResult]
    EMAIL_TASK_QUEUED: _ClassVar[EmailResult]
    EMAIL_TASK_DELIVERED: _ClassVar[EmailResult]
    EMAIL_TASK_DROPPED: _ClassVar[EmailResult]
    EMAIL_TASK_DEFERRED: _ClassVar[EmailResult]
    EMAIL_TASK_BOUNCED: _ClassVar[EmailResult]
    EMAIL_TASK_OPENED: _ClassVar[EmailResult]
    EMAIL_TASK_CLICKED: _ClassVar[EmailResult]
    EMAIL_TASK_UNSUBSCRIBED: _ClassVar[EmailResult]
    EMAIL_TASK_MARKED_AS_SPAM: _ClassVar[EmailResult]
    EMAIL_TASK_BLOCKED: _ClassVar[EmailResult]

class EmailStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EMAIL_STATUS_UNKKNOWN: _ClassVar[EmailStatus]
    EMAIL_PREPARING: _ClassVar[EmailStatus]
    EMAIL_SCHEDULED: _ClassVar[EmailStatus]
    EMAIL_RESUME: _ClassVar[EmailStatus]
    EMAIL_RUNNING: _ClassVar[EmailStatus]
    EMAIL_COMPLETED: _ClassVar[EmailStatus]
    EMAIL_CANCELLED: _ClassVar[EmailStatus]
    EMAIL_CANCELLED_ADMIN: _ClassVar[EmailStatus]
    EMAIL_SUMMED_COMPLETED: _ClassVar[EmailStatus]
    EMAIL_SUMMED_CANCELLED: _ClassVar[EmailStatus]
    EMAIL_SUMMED_CANCELLED_ADMIN: _ClassVar[EmailStatus]
    EMAIL_PAUSED: _ClassVar[EmailStatus]

class EmailIBGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IB_EMAIL_GROUP_UNKNOWN: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_PREPARING: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_SCHEDULED: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_RUNNING: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_PAUSED: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_RESUME: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_RUNNING_WITH_ERROR: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_ERROR_STANDBY: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_COMPLETED: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_CANCELLED_USER: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_CANCELLED_ADMIN: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_SUMMED_COMPLETED: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_SUMMED_CANCELLED_USER: _ClassVar[EmailIBGroupStatus]
    IB_EMAIL_GROUP_SUMMED_CANCELLED_ADMIN: _ClassVar[EmailIBGroupStatus]

class EmailIBReplyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IB_EMAIL_REPLY_UNKNOWN: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_REPLY_RECEIVED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_SENDING: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_SENDING_FAILED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_INVALID: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_SENT: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_DELIVERED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_DROPPED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_DEFERRED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_BOUNCED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_OPENED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_CLICKED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_UNSUBSCRIBED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_MARKED_AS_SPAM: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_AGENT_REPLY_BLOCKED: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_REPLY_DNC: _ClassVar[EmailIBReplyStatus]
    IB_EMAIL_REPLY_CANCELLED: _ClassVar[EmailIBReplyStatus]

class EmailIBGroupEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IB_EMAIL_GROUP_EVENT_PREPARED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_SCHEDULED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_STARTED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_RUNNING: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_STOPPED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_PAUSED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_RESUME: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_CANCELLED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_MESSAGE_RECEIVED: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_LOGIN_ERROR: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_FETCH_ERROR: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_STANDBY_ERROR: _ClassVar[EmailIBGroupEvent]
    IB_EMAIL_GROUP_EVENT_COMPLETED: _ClassVar[EmailIBGroupEvent]

class EmailIBReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REPLY_UNKNOWN: _ClassVar[EmailIBReplyType]
    EXISTING_CONV: _ClassVar[EmailIBReplyType]
    OUTBOUND_REPLY: _ClassVar[EmailIBReplyType]
    AGENT_REPLY: _ClassVar[EmailIBReplyType]
    INBOUND_PURE: _ClassVar[EmailIBReplyType]
    OUTBOUND_TASK: _ClassVar[EmailIBReplyType]
    OUTBOUND_PURE: _ClassVar[EmailIBReplyType]
EMAIL_RESULT_UNKNOWN: EmailResult
EMAIL_TASK_WAITING: EmailResult
EMAIL_TASK_PROCESSING: EmailResult
EMAIL_TASK_DNC: EmailResult
EMAIL_TASK_INVALID: EmailResult
EMAIL_TASK_ATTACHMENT_ERROR: EmailResult
EMAIL_TASK_CANCELLED: EmailResult
EMAIL_TASK_QUEUED: EmailResult
EMAIL_TASK_DELIVERED: EmailResult
EMAIL_TASK_DROPPED: EmailResult
EMAIL_TASK_DEFERRED: EmailResult
EMAIL_TASK_BOUNCED: EmailResult
EMAIL_TASK_OPENED: EmailResult
EMAIL_TASK_CLICKED: EmailResult
EMAIL_TASK_UNSUBSCRIBED: EmailResult
EMAIL_TASK_MARKED_AS_SPAM: EmailResult
EMAIL_TASK_BLOCKED: EmailResult
EMAIL_STATUS_UNKKNOWN: EmailStatus
EMAIL_PREPARING: EmailStatus
EMAIL_SCHEDULED: EmailStatus
EMAIL_RESUME: EmailStatus
EMAIL_RUNNING: EmailStatus
EMAIL_COMPLETED: EmailStatus
EMAIL_CANCELLED: EmailStatus
EMAIL_CANCELLED_ADMIN: EmailStatus
EMAIL_SUMMED_COMPLETED: EmailStatus
EMAIL_SUMMED_CANCELLED: EmailStatus
EMAIL_SUMMED_CANCELLED_ADMIN: EmailStatus
EMAIL_PAUSED: EmailStatus
IB_EMAIL_GROUP_UNKNOWN: EmailIBGroupStatus
IB_EMAIL_GROUP_PREPARING: EmailIBGroupStatus
IB_EMAIL_GROUP_SCHEDULED: EmailIBGroupStatus
IB_EMAIL_GROUP_RUNNING: EmailIBGroupStatus
IB_EMAIL_GROUP_PAUSED: EmailIBGroupStatus
IB_EMAIL_GROUP_RESUME: EmailIBGroupStatus
IB_EMAIL_GROUP_RUNNING_WITH_ERROR: EmailIBGroupStatus
IB_EMAIL_GROUP_ERROR_STANDBY: EmailIBGroupStatus
IB_EMAIL_GROUP_COMPLETED: EmailIBGroupStatus
IB_EMAIL_GROUP_CANCELLED_USER: EmailIBGroupStatus
IB_EMAIL_GROUP_CANCELLED_ADMIN: EmailIBGroupStatus
IB_EMAIL_GROUP_SUMMED_COMPLETED: EmailIBGroupStatus
IB_EMAIL_GROUP_SUMMED_CANCELLED_USER: EmailIBGroupStatus
IB_EMAIL_GROUP_SUMMED_CANCELLED_ADMIN: EmailIBGroupStatus
IB_EMAIL_REPLY_UNKNOWN: EmailIBReplyStatus
IB_EMAIL_REPLY_RECEIVED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_SENDING: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_SENDING_FAILED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_INVALID: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_SENT: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_DELIVERED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_DROPPED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_DEFERRED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_BOUNCED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_OPENED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_CLICKED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_UNSUBSCRIBED: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_MARKED_AS_SPAM: EmailIBReplyStatus
IB_EMAIL_AGENT_REPLY_BLOCKED: EmailIBReplyStatus
IB_EMAIL_REPLY_DNC: EmailIBReplyStatus
IB_EMAIL_REPLY_CANCELLED: EmailIBReplyStatus
IB_EMAIL_GROUP_EVENT_PREPARED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_SCHEDULED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_STARTED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_RUNNING: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_STOPPED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_PAUSED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_RESUME: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_CANCELLED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_MESSAGE_RECEIVED: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_LOGIN_ERROR: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_FETCH_ERROR: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_STANDBY_ERROR: EmailIBGroupEvent
IB_EMAIL_GROUP_EVENT_COMPLETED: EmailIBGroupEvent
REPLY_UNKNOWN: EmailIBReplyType
EXISTING_CONV: EmailIBReplyType
OUTBOUND_REPLY: EmailIBReplyType
AGENT_REPLY: EmailIBReplyType
INBOUND_PURE: EmailIBReplyType
OUTBOUND_TASK: EmailIBReplyType
OUTBOUND_PURE: EmailIBReplyType
