from annotations import authz_pb2 as _authz_pb2
from api.commons import logging_pb2 as _logging_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SentinelEvent(_message.Message):
    __slots__ = ["log_event"]
    LOG_EVENT_FIELD_NUMBER: _ClassVar[int]
    log_event: LogEvent
    def __init__(self, log_event: _Optional[_Union[LogEvent, _Mapping]] = ...) -> None: ...

class LogEvent(_message.Message):
    __slots__ = ["trace_id", "session_id", "message", "location", "stack_trace", "timestamp", "metadata", "severity"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    session_id: str
    message: str
    location: str
    stack_trace: str
    timestamp: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    severity: _logging_pb2.Level
    def __init__(self, trace_id: _Optional[str] = ..., session_id: _Optional[str] = ..., message: _Optional[str] = ..., location: _Optional[str] = ..., stack_trace: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., severity: _Optional[_Union[_logging_pb2.Level, str]] = ...) -> None: ...

class SendEventsReq(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[SentinelEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[SentinelEvent, _Mapping]]] = ...) -> None: ...

class SendEventsRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
