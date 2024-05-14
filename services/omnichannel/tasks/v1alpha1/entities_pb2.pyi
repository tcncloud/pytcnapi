from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelTasksRequest(_message.Message):
    __slots__ = ("task_sid",)
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    task_sid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, task_sid: _Optional[_Iterable[int]] = ...) -> None: ...

class CancelTasksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
