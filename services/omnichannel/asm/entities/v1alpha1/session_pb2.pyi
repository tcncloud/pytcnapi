import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_STATE_UNKNOWN: _ClassVar[StatusState]
    WAITING: _ClassVar[StatusState]
    IDLE: _ClassVar[StatusState]
    CONVERSATION_OPEN: _ClassVar[StatusState]
STATUS_STATE_UNKNOWN: StatusState
WAITING: StatusState
IDLE: StatusState
CONVERSATION_OPEN: StatusState

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

class AsmUserDetails(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CUSTOMER_WAIT_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_RESPOND_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    agent_sid: int
    agent_status: StatusState
    agent_profile_group_name: str
    current_conversation_sid: int
    average_customer_wait_time_seconds: int
    average_time_to_respond_seconds: int
    last_event_time: _timestamp_pb2.Timestamp
    skills: _containers.ScalarMap[str, int]
    asm_session_sid: _wrappers_pb2.Int64Value
    events: _containers.RepeatedCompositeFieldContainer[DashboardAgentResponseEvent]
    login_time: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., agent_sid: _Optional[int] = ..., agent_status: _Optional[_Union[StatusState, str]] = ..., agent_profile_group_name: _Optional[str] = ..., current_conversation_sid: _Optional[int] = ..., average_customer_wait_time_seconds: _Optional[int] = ..., average_time_to_respond_seconds: _Optional[int] = ..., last_event_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Mapping[str, int]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., events: _Optional[_Iterable[_Union[DashboardAgentResponseEvent, _Mapping]]] = ..., login_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DashboardAgentResponseEvent(_message.Message):
    __slots__ = ()
    RESPONSE_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    IS_INITIAL_AGENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    response_time_seconds: int
    time: _timestamp_pb2.Timestamp
    is_initial_agent_message: bool
    def __init__(self, response_time_seconds: _Optional[int] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_initial_agent_message: _Optional[bool] = ...) -> None: ...
