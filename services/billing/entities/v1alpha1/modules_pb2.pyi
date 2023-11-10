from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicConfig(_message.Message):
    __slots__ = ("rate",)
    RATE_FIELD_NUMBER: _ClassVar[int]
    rate: float
    def __init__(self, rate: _Optional[float] = ...) -> None: ...

class BasicUnitConfig(_message.Message):
    __slots__ = ("unit_size", "rate", "min_units", "max_units")
    UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_UNITS_FIELD_NUMBER: _ClassVar[int]
    MAX_UNITS_FIELD_NUMBER: _ClassVar[int]
    unit_size: int
    rate: float
    min_units: _wrappers_pb2.Int64Value
    max_units: _wrappers_pb2.Int64Value
    def __init__(self, unit_size: _Optional[int] = ..., rate: _Optional[float] = ..., min_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
