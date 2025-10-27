import datetime

from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons import asm_pb2 as _asm_pb2
from api.commons.auth import user_pb2 as _user_pb2
from api.commons import event_pb2 as _event_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SUBSESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    subsession_type: _asm_pb2.AsmSubsessionType
    def __init__(self, hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ..., subsession_type: _Optional[_Union[_asm_pb2.AsmSubsessionType, str]] = ...) -> None: ...

class CreateSessionRes(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    voice_session_sid: int
    voice_registration: VoiceRegistration
    def __init__(self, asm_session_sid: _Optional[int] = ..., voice_session_sid: _Optional[int] = ..., voice_registration: _Optional[_Union[VoiceRegistration, _Mapping]] = ...) -> None: ...

class VoiceRegistration(_message.Message):
    __slots__ = ()
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DIAL_URL_FIELD_NUMBER: _ClassVar[int]
    PSTN_PHONE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    dial_url: str
    pstn_phone: str
    default_time_zone: str
    expiration_timestamp: int
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., dial_url: _Optional[str] = ..., pstn_phone: _Optional[str] = ..., default_time_zone: _Optional[str] = ..., expiration_timestamp: _Optional[int] = ...) -> None: ...

class StreamAgentStateReq(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    keep_alive: bool
    def __init__(self, asm_session_sid: _Optional[int] = ..., keep_alive: _Optional[bool] = ...) -> None: ...

class ManagerStreamAgentStateReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStatusReq(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_GET_QUEUED_CALLS_FIELD_NUMBER: _ClassVar[int]
    PERFORM_GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_MESSAGE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    perform_keep_alive: bool
    perform_get_queued_calls: bool
    perform_get_message: bool
    minimum_message_timestamp: int
    skills: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    agent_pbx_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, asm_session_sid: _Optional[int] = ..., perform_keep_alive: _Optional[bool] = ..., perform_get_queued_calls: _Optional[bool] = ..., perform_get_message: _Optional[bool] = ..., minimum_message_timestamp: _Optional[int] = ..., skills: _Optional[_Iterable[str]] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., agent_pbx_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetStatusRes(_message.Message):
    __slots__ = ()
    VOICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    voice_status: VoiceStatus
    def __init__(self, voice_status: _Optional[_Union[VoiceStatus, _Mapping]] = ...) -> None: ...

class VoiceStatus(_message.Message):
    __slots__ = ()
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DESC_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    CALLS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_SIP_CODE_FIELD_NUMBER: _ClassVar[int]
    AGENT_PEER_IS_LOST_CALL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    QUEUED_CALLS_FIELD_NUMBER: _ClassVar[int]
    CALLER_WAS_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    AGENT_PEER_IS_DIRECT_TO_AGENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    status: int
    status_desc: _acd_pb2.AgentStatus.Enum
    paused: bool
    queue: str
    current_session_id: int
    last_status_change: int
    monitoring: bool
    calls_count: int
    last_sip_code: int
    agent_peer_is_lost_call: bool
    disabled: bool
    keep_alive_succeeded: bool
    message: str
    message_timestamp: int
    queued_calls: QueuedCalls
    caller_was_suspended: bool
    transfer_members: _containers.RepeatedCompositeFieldContainer[_acd_pb2.TransferMember]
    alert: _acd_pb2.AgentAlert
    agent_peer_is_direct_to_agent: bool
    agent_is_muted: bool
    def __init__(self, status: _Optional[int] = ..., status_desc: _Optional[_Union[_acd_pb2.AgentStatus.Enum, str]] = ..., paused: _Optional[bool] = ..., queue: _Optional[str] = ..., current_session_id: _Optional[int] = ..., last_status_change: _Optional[int] = ..., monitoring: _Optional[bool] = ..., calls_count: _Optional[int] = ..., last_sip_code: _Optional[int] = ..., agent_peer_is_lost_call: _Optional[bool] = ..., disabled: _Optional[bool] = ..., keep_alive_succeeded: _Optional[bool] = ..., message: _Optional[str] = ..., message_timestamp: _Optional[int] = ..., queued_calls: _Optional[_Union[QueuedCalls, _Mapping]] = ..., caller_was_suspended: _Optional[bool] = ..., transfer_members: _Optional[_Iterable[_Union[_acd_pb2.TransferMember, _Mapping]]] = ..., alert: _Optional[_Union[_acd_pb2.AgentAlert, _Mapping]] = ..., agent_peer_is_direct_to_agent: _Optional[bool] = ..., agent_is_muted: _Optional[bool] = ...) -> None: ...

class QueuedCalls(_message.Message):
    __slots__ = ()
    class QueuedCallData(_message.Message):
        __slots__ = ()
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
        def __init__(self, call_sid: _Optional[int] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., hold_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Iterable[str]] = ..., agent_specific: _Optional[bool] = ..., queued_notification_type: _Optional[_Union[_acd_pb2.QueuedNotificationType, str]] = ...) -> None: ...
    AGENT_QUEUE_CALLS_FIELD_NUMBER: _ClassVar[int]
    ON_HOLD_CALLS_FIELD_NUMBER: _ClassVar[int]
    HQM_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_queue_calls: _containers.RepeatedCompositeFieldContainer[QueuedCalls.QueuedCallData]
    on_hold_calls: _containers.RepeatedCompositeFieldContainer[QueuedCalls.QueuedCallData]
    hqm_calls: _containers.RepeatedCompositeFieldContainer[QueuedCalls.QueuedCallData]
    def __init__(self, agent_queue_calls: _Optional[_Iterable[_Union[QueuedCalls.QueuedCallData, _Mapping]]] = ..., on_hold_calls: _Optional[_Iterable[_Union[QueuedCalls.QueuedCallData, _Mapping]]] = ..., hqm_calls: _Optional[_Iterable[_Union[QueuedCalls.QueuedCallData, _Mapping]]] = ...) -> None: ...

class EndSessionReq(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    reason: str
    def __init__(self, asm_session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class EndSessionRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AsmSession(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_START_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_END_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    asm_session_start: _timestamp_pb2.Timestamp
    asm_session_end: _timestamp_pb2.Timestamp
    voice_session: VoiceSession
    def __init__(self, asm_session_sid: _Optional[int] = ..., asm_session_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., asm_session_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., voice_session: _Optional[_Union[VoiceSession, _Mapping]] = ...) -> None: ...

class VoiceSession(_message.Message):
    __slots__ = ()
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_START_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_END_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    voice_session_start: _timestamp_pb2.Timestamp
    voice_session_end: _timestamp_pb2.Timestamp
    def __init__(self, voice_session_sid: _Optional[int] = ..., voice_session_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., voice_session_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SwitchSubsessionReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    channel_type: _asm_pb2.AsmSubsessionType
    def __init__(self, asm_session_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ..., channel_type: _Optional[_Union[_asm_pb2.AsmSubsessionType, str]] = ...) -> None: ...

class SwitchSubsessionRes(_message.Message):
    __slots__ = ()
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    voice_registration: VoiceRegistration
    def __init__(self, voice_session_sid: _Optional[int] = ..., voice_registration: _Optional[_Union[VoiceRegistration, _Mapping]] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_LAST_UPDATED_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLA_TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COLLECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_GROUP_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    conversation_created_time: _timestamp_pb2.Timestamp
    assigned_last_updated_time: _timestamp_pb2.Timestamp
    conversation_status: _omnichannel_pb2.ConversationStatus
    channel_type: _omnichannel_pb2.ChannelType
    customer_info: _omnichannel_pb2.ConversationCustomerInformation
    last_message_time: _timestamp_pb2.Timestamp
    skills: ConversationSkills
    assignment_status: _omnichannel_pb2.AgentConversationAssignmentStatus
    assignment_type: _omnichannel_pb2.AgentConversationAssignmentType
    sla_timeouts: _omnichannel_pb2.SLATimeouts
    conversation_collected_data: _omnichannel_pb2.ConversationCollectedData
    last_message_group_time: _timestamp_pb2.Timestamp
    last_message_group_type: _omnichannel_pb2.OmniSenderType
    task_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., conversation_created_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., assigned_last_updated_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., conversation_status: _Optional[_Union[_omnichannel_pb2.ConversationStatus, str]] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., customer_info: _Optional[_Union[_omnichannel_pb2.ConversationCustomerInformation, _Mapping]] = ..., last_message_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Union[ConversationSkills, _Mapping]] = ..., assignment_status: _Optional[_Union[_omnichannel_pb2.AgentConversationAssignmentStatus, str]] = ..., assignment_type: _Optional[_Union[_omnichannel_pb2.AgentConversationAssignmentType, str]] = ..., sla_timeouts: _Optional[_Union[_omnichannel_pb2.SLATimeouts, _Mapping]] = ..., conversation_collected_data: _Optional[_Union[_omnichannel_pb2.ConversationCollectedData, _Mapping]] = ..., last_message_group_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_message_group_type: _Optional[_Union[_omnichannel_pb2.OmniSenderType, str]] = ..., task_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class ConversationSkills(_message.Message):
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

class AssignNewConversationReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    skills: _containers.ScalarMap[str, int]
    channel_types: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ChannelType]
    def __init__(self, asm_session_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ..., channel_types: _Optional[_Iterable[_Union[_omnichannel_pb2.ChannelType, str]]] = ...) -> None: ...

class AssignNewConversationRes(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    reference_id: str
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class ListAgentsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentsRes(_message.Message):
    __slots__ = ()
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[_asm_pb2.DashboardAgentInfo]
    def __init__(self, agents: _Optional[_Iterable[_Union[_asm_pb2.DashboardAgentInfo, _Mapping]]] = ...) -> None: ...

class SetConversationCollectedDataReq(_message.Message):
    __slots__ = ()
    class CollectedDataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    collected_data: _containers.ScalarMap[str, str]
    asm_session_sid: int
    def __init__(self, conversation_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., collected_data: _Optional[_Mapping[str, str]] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class SetConversationCollectedDataRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConversationsReq(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_USER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    authenticated_user: _user_pb2.AuthenticatedUser
    user_id: str
    statuses: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ConversationStatus]
    field_mask: _field_mask_pb2.FieldMask
    channel_types: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ChannelType]
    def __init__(self, asm_session_sid: _Optional[int] = ..., authenticated_user: _Optional[_Union[_user_pb2.AuthenticatedUser, _Mapping]] = ..., user_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[_omnichannel_pb2.ConversationStatus, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., channel_types: _Optional[_Iterable[_Union[_omnichannel_pb2.ChannelType, str]]] = ...) -> None: ...

class ListConversationsRes(_message.Message):
    __slots__ = ()
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniConversation]
    next_page_token: str
    def __init__(self, conversations: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniConversation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetQueuesDetailsReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    channel_types: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ChannelType]
    skills: _containers.ScalarMap[str, int]
    def __init__(self, asm_session_sid: _Optional[int] = ..., channel_types: _Optional[_Iterable[_Union[_omnichannel_pb2.ChannelType, str]]] = ..., skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class PushEventsReq(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.AsmEvent]
    def __init__(self, asm_session_sid: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_event_pb2.AsmEvent, _Mapping]]] = ...) -> None: ...

class PushEventsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableVoiceReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    def __init__(self, asm_session_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EnableVoiceRes(_message.Message):
    __slots__ = ()
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    voice_registration: VoiceRegistration
    def __init__(self, voice_session_sid: _Optional[int] = ..., voice_registration: _Optional[_Union[VoiceRegistration, _Mapping]] = ...) -> None: ...

class DisableVoiceReq(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    def __init__(self, asm_session_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class DisableVoiceRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
