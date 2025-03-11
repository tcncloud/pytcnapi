from google.protobuf import timestamp_pb2 as _timestamp_pb2
from wfo.vanalytics.v2 import transcript_pb2 as _transcript_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilterSnapshot(_message.Message):
    __slots__ = ("filter_snapshot_sid", "filter_sid", "name", "create_time", "version", "transcript_query")
    FILTER_SNAPSHOT_SID_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_QUERY_FIELD_NUMBER: _ClassVar[int]
    filter_snapshot_sid: int
    filter_sid: int
    name: str
    create_time: _timestamp_pb2.Timestamp
    version: int
    transcript_query: _transcript_pb2.TranscriptQuery
    def __init__(self, filter_snapshot_sid: _Optional[int] = ..., filter_sid: _Optional[int] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., transcript_query: _Optional[_Union[_transcript_pb2.TranscriptQuery, _Mapping]] = ...) -> None: ...
