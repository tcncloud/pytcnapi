from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListScreenRecordingsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListScreenRecordingsResponse(_message.Message):
    __slots__ = ("next_page_token", "recordings")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    recordings: _containers.RepeatedCompositeFieldContainer[ScreenRecording]
    def __init__(self, next_page_token: _Optional[str] = ..., recordings: _Optional[_Iterable[_Union[ScreenRecording, _Mapping]]] = ...) -> None: ...

class ScreenRecording(_message.Message):
    __slots__ = ("session_id", "agent_first_name", "agent_last_name", "start_time", "audio_time", "audio_bytes")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BYTES_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    agent_first_name: str
    agent_last_name: str
    start_time: _timestamp_pb2.Timestamp
    audio_time: int
    audio_bytes: int
    def __init__(self, session_id: _Optional[int] = ..., agent_first_name: _Optional[str] = ..., agent_last_name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., audio_time: _Optional[int] = ..., audio_bytes: _Optional[int] = ...) -> None: ...

class GetScreenRecordingURLRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class GetScreenRecordingURLResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DeleteScreenRecordingRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class DeleteScreenRecordingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
