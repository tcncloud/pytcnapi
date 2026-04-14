from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WFMPublishScheduleEvent(_message.Message):
    __slots__ = ("published_schedule_sid", "user_ids")
    PUBLISHED_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    published_schedule_sid: int
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, published_schedule_sid: _Optional[int] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...
