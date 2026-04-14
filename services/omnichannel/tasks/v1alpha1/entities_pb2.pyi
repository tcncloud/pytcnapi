from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelTasksRequest(_message.Message):
    __slots__ = ("task_sid",)
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    task_sid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, task_sid: _Optional[_Iterable[int]] = ...) -> None: ...

class CancelTasksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkCancelTasksRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    def __init__(self, filter: _Optional[str] = ...) -> None: ...

class BulkCancelTasksResponse(_message.Message):
    __slots__ = ("ghost_reference_id",)
    GHOST_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    ghost_reference_id: str
    def __init__(self, ghost_reference_id: _Optional[str] = ...) -> None: ...
