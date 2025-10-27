import datetime

from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNotifyRequest(_message.Message):
    __slots__ = ()
    NOTIFY_ID_FIELD_NUMBER: _ClassVar[int]
    notify_id: str
    def __init__(self, notify_id: _Optional[str] = ...) -> None: ...

class Notify(_message.Message):
    __slots__ = ()
    NOTIFY_ID_FIELD_NUMBER: _ClassVar[int]
    START_TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    END_TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    notify_id: str
    start_transcript_sid: int
    end_transcript_sid: int
    flag_sid: int
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, notify_id: _Optional[str] = ..., start_transcript_sid: _Optional[int] = ..., end_transcript_sid: _Optional[int] = ..., flag_sid: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
