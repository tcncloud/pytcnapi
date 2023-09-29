from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SORT_DIRECTION_UNSPECIFIED: _ClassVar[SortDirection]
    SORT_DIRECTION_DESC: _ClassVar[SortDirection]
SORT_DIRECTION_UNSPECIFIED: SortDirection
SORT_DIRECTION_DESC: SortDirection

class Page(_message.Message):
    __slots__ = ["limit", "token"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    limit: int
    token: str
    def __init__(self, limit: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class Sort(_message.Message):
    __slots__ = ["field", "direction"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    field: str
    direction: SortDirection
    def __init__(self, field: _Optional[str] = ..., direction: _Optional[_Union[SortDirection, str]] = ...) -> None: ...
