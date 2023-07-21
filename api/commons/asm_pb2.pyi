from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AsmSubsessionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VOICE: _ClassVar[AsmSubsessionType]
    OMNI: _ClassVar[AsmSubsessionType]

class StatusState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STATUS_STATE_UNKNOWN: _ClassVar[StatusState]
    WAITING: _ClassVar[StatusState]
    IDLE: _ClassVar[StatusState]
    CONVERSATION_OPEN: _ClassVar[StatusState]
VOICE: AsmSubsessionType
OMNI: AsmSubsessionType
STATUS_STATE_UNKNOWN: StatusState
WAITING: StatusState
IDLE: StatusState
CONVERSATION_OPEN: StatusState

class DashboardAgentInfo(_message.Message):
    __slots__ = ["user_id", "name", "user_name", "hunt_group_name", "partner_agent_id", "hunt_group_sid", "agent_sid", "user_caller_id", "first_name", "last_name", "created", "last_updated", "agent_profile_group_id", "agent_profile_group_name", "agent_status", "current_conversation_sid", "average_customer_wait_time_seconds", "average_time_to_respond_seconds", "average_conversation_duration_seconds", "login_time", "last_event_time", "events", "skills", "asm_session_sid"]
    class DashboardAgentResponseEvent(_message.Message):
        __slots__ = ["response_time_seconds", "time", "is_initial_agent_message"]
        RESPONSE_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        IS_INITIAL_AGENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        response_time_seconds: int
        time: _timestamp_pb2.Timestamp
        is_initial_agent_message: bool
        def __init__(self, response_time_seconds: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_initial_agent_message: bool = ...) -> None: ...
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CUSTOMER_WAIT_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_RESPOND_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CONVERSATION_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    user_name: str
    hunt_group_name: str
    partner_agent_id: str
    hunt_group_sid: int
    agent_sid: int
    user_caller_id: str
    first_name: str
    last_name: str
    created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    agent_profile_group_id: str
    agent_profile_group_name: str
    agent_status: StatusState
    current_conversation_sid: int
    average_customer_wait_time_seconds: int
    average_time_to_respond_seconds: int
    average_conversation_duration_seconds: int
    login_time: _timestamp_pb2.Timestamp
    last_event_time: _timestamp_pb2.Timestamp
    events: _containers.RepeatedCompositeFieldContainer[DashboardAgentInfo.DashboardAgentResponseEvent]
    skills: _containers.ScalarMap[str, int]
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., user_name: _Optional[str] = ..., hunt_group_name: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., user_caller_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ..., agent_status: _Optional[_Union[StatusState, str]] = ..., current_conversation_sid: _Optional[int] = ..., average_customer_wait_time_seconds: _Optional[int] = ..., average_time_to_respond_seconds: _Optional[int] = ..., average_conversation_duration_seconds: _Optional[int] = ..., login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., events: _Optional[_Iterable[_Union[DashboardAgentInfo.DashboardAgentResponseEvent, _Mapping]]] = ..., skills: _Optional[_Mapping[str, int]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class StreamAgentStateRes(_message.Message):
    __slots__ = ["state", "heart_beat", "call_queue_add", "call_queue_remove"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HEART_BEAT_FIELD_NUMBER: _ClassVar[int]
    CALL_QUEUE_ADD_FIELD_NUMBER: _ClassVar[int]
    CALL_QUEUE_REMOVE_FIELD_NUMBER: _ClassVar[int]
    state: _acd_pb2.AgentState
    heart_beat: KeepAlive
    call_queue_add: QueueCallAdd
    call_queue_remove: QueueCallRemove
    def __init__(self, state: _Optional[_Union[_acd_pb2.AgentState, _Mapping]] = ..., heart_beat: _Optional[_Union[KeepAlive, _Mapping]] = ..., call_queue_add: _Optional[_Union[QueueCallAdd, _Mapping]] = ..., call_queue_remove: _Optional[_Union[QueueCallRemove, _Mapping]] = ...) -> None: ...

class ManagerStreamAgentStateRes(_message.Message):
    __slots__ = ["state", "heart_beat"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HEART_BEAT_FIELD_NUMBER: _ClassVar[int]
    state: _acd_pb2.AgentState
    heart_beat: KeepAlive
    def __init__(self, state: _Optional[_Union[_acd_pb2.AgentState, _Mapping]] = ..., heart_beat: _Optional[_Union[KeepAlive, _Mapping]] = ...) -> None: ...

class KeepAlive(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueueCallAdd(_message.Message):
    __slots__ = ["phone_number", "caller_id", "start_date", "hold_date", "formatted_skills", "agent_specific", "queued_notification_type", "caller_sid", "skills"]
    class FormattedSkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    HOLD_DATE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SPECIFIC_FIELD_NUMBER: _ClassVar[int]
    QUEUED_NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    caller_id: str
    start_date: _timestamp_pb2.Timestamp
    hold_date: _timestamp_pb2.Timestamp
    formatted_skills: _containers.ScalarMap[str, str]
    agent_specific: bool
    queued_notification_type: _acd_pb2.QueuedNotificationType
    caller_sid: _acd_pb2.CallerSid
    skills: _containers.ScalarMap[str, bool]
    def __init__(self, phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hold_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., formatted_skills: _Optional[_Mapping[str, str]] = ..., agent_specific: bool = ..., queued_notification_type: _Optional[_Union[_acd_pb2.QueuedNotificationType, str]] = ..., caller_sid: _Optional[_Union[_acd_pb2.CallerSid, _Mapping]] = ..., skills: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class QueueCallRemove(_message.Message):
    __slots__ = ["caller_sid"]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    caller_sid: _acd_pb2.CallerSid
    def __init__(self, caller_sid: _Optional[_Union[_acd_pb2.CallerSid, _Mapping]] = ...) -> None: ...
