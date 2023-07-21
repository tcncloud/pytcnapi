from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DLFSDef(_message.Message):
    __slots__ = ["vfs_id", "incremental"]
    VFS_ID_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    vfs_id: int
    incremental: bool
    def __init__(self, vfs_id: _Optional[int] = ..., incremental: bool = ...) -> None: ...

class DLFSDefs(_message.Message):
    __slots__ = ["defs"]
    DEFS_FIELD_NUMBER: _ClassVar[int]
    defs: _containers.RepeatedCompositeFieldContainer[DLFSDef]
    def __init__(self, defs: _Optional[_Iterable[_Union[DLFSDef, _Mapping]]] = ...) -> None: ...
