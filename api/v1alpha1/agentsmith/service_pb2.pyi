from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[AgentState]
    UNAVAILABLE: _ClassVar[AgentState]
    IDLE: _ClassVar[AgentState]
    READY: _ClassVar[AgentState]
    HUNGUP: _ClassVar[AgentState]
    DESTROYED: _ClassVar[AgentState]
    PEERED: _ClassVar[AgentState]
    PAUSED: _ClassVar[AgentState]
    WRAPUP: _ClassVar[AgentState]
    PREPARING_AFTER_IDLE: _ClassVar[AgentState]
UNKNOWN: AgentState
UNAVAILABLE: AgentState
IDLE: AgentState
READY: AgentState
HUNGUP: AgentState
DESTROYED: AgentState
PEERED: AgentState
PAUSED: AgentState
WRAPUP: AgentState
PREPARING_AFTER_IDLE: AgentState

class FollowAgentReq(_message.Message):
    __slots__ = ("user_id", "asm_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class FollowAgentRes(_message.Message):
    __slots__ = ("ts", "agent_state_change", "agent_voice_start", "agent_voice_end", "agent_session_end")
    TS_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    AGENT_VOICE_START_FIELD_NUMBER: _ClassVar[int]
    AGENT_VOICE_END_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_END_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    agent_state_change: AgentStateChangeEvent
    agent_voice_start: AgentVoiceStartEvent
    agent_voice_end: AgentVoiceEndEvent
    agent_session_end: AgentSessionEndEvent
    def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_state_change: _Optional[_Union[AgentStateChangeEvent, _Mapping]] = ..., agent_voice_start: _Optional[_Union[AgentVoiceStartEvent, _Mapping]] = ..., agent_voice_end: _Optional[_Union[AgentVoiceEndEvent, _Mapping]] = ..., agent_session_end: _Optional[_Union[AgentSessionEndEvent, _Mapping]] = ...) -> None: ...

class AgentStateChangeEvent(_message.Message):
    __slots__ = ("old_state", "new_state", "empty")
    OLD_STATE_FIELD_NUMBER: _ClassVar[int]
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    old_state: AgentState
    new_state: AgentState
    empty: EmptyState
    def __init__(self, old_state: _Optional[_Union[AgentState, str]] = ..., new_state: _Optional[_Union[AgentState, str]] = ..., empty: _Optional[_Union[EmptyState, _Mapping]] = ...) -> None: ...

class EmptyState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentVoiceStartEvent(_message.Message):
    __slots__ = ("sip_dial_url",)
    SIP_DIAL_URL_FIELD_NUMBER: _ClassVar[int]
    sip_dial_url: str
    def __init__(self, sip_dial_url: _Optional[str] = ...) -> None: ...

class AgentVoiceEndEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentSessionEndEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
