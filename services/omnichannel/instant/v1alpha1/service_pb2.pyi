from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamAgentEventsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class StreamAgentEventsResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _containers.RepeatedCompositeFieldContainer[AgentEvent]
    def __init__(self, event: _Optional[_Iterable[_Union[AgentEvent, _Mapping]]] = ...) -> None: ...

class StreamCallerEventsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class StreamCallerEventsResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _containers.RepeatedCompositeFieldContainer[CallerEvent]
    def __init__(self, event: _Optional[_Iterable[_Union[CallerEvent, _Mapping]]] = ...) -> None: ...

class AgentEvent(_message.Message):
    __slots__ = ("org_id", "client_sid", "agent_sid", "user_id", "event_time", "event_data")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    client_sid: int
    agent_sid: int
    user_id: str
    event_time: _timestamp_pb2.Timestamp
    event_data: str
    def __init__(self, org_id: _Optional[str] = ..., client_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., user_id: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_data: _Optional[str] = ...) -> None: ...

class CallerEvent(_message.Message):
    __slots__ = ("org_id", "client_sid", "caller_sid", "caller_type", "event_time", "event_data")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    client_sid: int
    caller_sid: int
    caller_type: _acd_pb2.CallType.Enum
    event_time: _timestamp_pb2.Timestamp
    event_data: str
    def __init__(self, org_id: _Optional[str] = ..., client_sid: _Optional[int] = ..., caller_sid: _Optional[int] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_data: _Optional[str] = ...) -> None: ...
