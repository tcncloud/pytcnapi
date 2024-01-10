from google.protobuf import timestamp_pb2 as _timestamp_pb2
from wfo.vanalytics.v2 import transcript_pb2 as _transcript_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFilterRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    def __init__(self, filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class CreateFilterResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    def __init__(self, filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("filter_sid", "name", "transcript_query", "create_time", "version")
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_QUERY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_sid: int
    name: str
    transcript_query: _transcript_pb2.TranscriptQuery
    create_time: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, filter_sid: _Optional[int] = ..., name: _Optional[str] = ..., transcript_query: _Optional[_Union[_transcript_pb2.TranscriptQuery, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...
