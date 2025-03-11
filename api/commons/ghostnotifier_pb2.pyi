from api.commons import acd_pb2 as _acd_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GhostNotification(_message.Message):
    __slots__ = ("reference_id", "any", "status", "omni_conversation", "backoffice_message", "directed_call_ringing", "directed_call_hangup", "agent_queued_calls_notification", "auth_token_expiration_notification", "omni_message_received", "omni_conversation_assigned")
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OMNI_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    BACKOFFICE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_CALL_RINGING_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_CALL_HANGUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_QUEUED_CALLS_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_EXPIRATION_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    OMNI_MESSAGE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    OMNI_CONVERSATION_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    any: _any_pb2.Any
    status: Status
    omni_conversation: _omnichannel_pb2.OmniConversation
    backoffice_message: _acd_pb2.AgentBackofficeMessageAlert
    directed_call_ringing: _acd_pb2.AgentDirectedCallRingingAlert
    directed_call_hangup: _acd_pb2.AgentDirectedCallHangupAlert
    agent_queued_calls_notification: AgentQueuedCallsNotification
    auth_token_expiration_notification: AuthTokenExpiration
    omni_message_received: OmniMessageReceieved
    omni_conversation_assigned: OmniConversationAssigned
    def __init__(self, reference_id: _Optional[str] = ..., any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., omni_conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., backoffice_message: _Optional[_Union[_acd_pb2.AgentBackofficeMessageAlert, _Mapping]] = ..., directed_call_ringing: _Optional[_Union[_acd_pb2.AgentDirectedCallRingingAlert, _Mapping]] = ..., directed_call_hangup: _Optional[_Union[_acd_pb2.AgentDirectedCallHangupAlert, _Mapping]] = ..., agent_queued_calls_notification: _Optional[_Union[AgentQueuedCallsNotification, _Mapping]] = ..., auth_token_expiration_notification: _Optional[_Union[AuthTokenExpiration, _Mapping]] = ..., omni_message_received: _Optional[_Union[OmniMessageReceieved, _Mapping]] = ..., omni_conversation_assigned: _Optional[_Union[OmniConversationAssigned, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class AgentQueuedCallsNotification(_message.Message):
    __slots__ = ("agent_queue_calls", "on_hold_calls", "hqm_calls")
    class QueuedCallData(_message.Message):
        __slots__ = ("call_sid", "phone_number", "caller_id", "call_type", "start_date", "hold_date", "skills", "agent_specific", "queued_notification_type")
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        START_DATE_FIELD_NUMBER: _ClassVar[int]
        HOLD_DATE_FIELD_NUMBER: _ClassVar[int]
        SKILLS_FIELD_NUMBER: _ClassVar[int]
        AGENT_SPECIFIC_FIELD_NUMBER: _ClassVar[int]
        QUEUED_NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        phone_number: str
        caller_id: str
        call_type: _acd_pb2.CallType.Enum
        start_date: _timestamp_pb2.Timestamp
        hold_date: _timestamp_pb2.Timestamp
        skills: _containers.RepeatedScalarFieldContainer[str]
        agent_specific: bool
        queued_notification_type: _acd_pb2.QueuedNotificationType
        def __init__(self, call_sid: _Optional[int] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hold_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Iterable[str]] = ..., agent_specific: bool = ..., queued_notification_type: _Optional[_Union[_acd_pb2.QueuedNotificationType, str]] = ...) -> None: ...
    AGENT_QUEUE_CALLS_FIELD_NUMBER: _ClassVar[int]
    ON_HOLD_CALLS_FIELD_NUMBER: _ClassVar[int]
    HQM_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_queue_calls: _containers.RepeatedCompositeFieldContainer[AgentQueuedCallsNotification.QueuedCallData]
    on_hold_calls: _containers.RepeatedCompositeFieldContainer[AgentQueuedCallsNotification.QueuedCallData]
    hqm_calls: _containers.RepeatedCompositeFieldContainer[AgentQueuedCallsNotification.QueuedCallData]
    def __init__(self, agent_queue_calls: _Optional[_Iterable[_Union[AgentQueuedCallsNotification.QueuedCallData, _Mapping]]] = ..., on_hold_calls: _Optional[_Iterable[_Union[AgentQueuedCallsNotification.QueuedCallData, _Mapping]]] = ..., hqm_calls: _Optional[_Iterable[_Union[AgentQueuedCallsNotification.QueuedCallData, _Mapping]]] = ...) -> None: ...

class AuthTokenExpiration(_message.Message):
    __slots__ = ("token", "expiration")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OmniConversationAssigned(_message.Message):
    __slots__ = ("conversation_sid",)
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...

class OmniMessageReceieved(_message.Message):
    __slots__ = ("conversation_sid", "message")
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    message: str
    def __init__(self, conversation_sid: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
