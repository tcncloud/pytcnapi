from api.v1alpha1.vanalytics import transcript_pb2 as _transcript_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilterSnapshot(_message.Message):
    __slots__ = ("filter_snapshot_sid", "filter_sid", "name", "search_request", "create_time", "version")
    FILTER_SNAPSHOT_SID_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_snapshot_sid: int
    filter_sid: int
    name: str
    search_request: _transcript_pb2.SearchRequest
    create_time: _timestamp_pb2.Timestamp
    version: int
    def __init__(self, filter_snapshot_sid: _Optional[int] = ..., filter_sid: _Optional[int] = ..., name: _Optional[str] = ..., search_request: _Optional[_Union[_transcript_pb2.SearchRequest, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...
