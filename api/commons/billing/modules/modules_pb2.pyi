from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicConfig(_message.Message):
    __slots__ = ()
    RATE_FIELD_NUMBER: _ClassVar[int]
    rate: float
    def __init__(self, rate: _Optional[float] = ...) -> None: ...

class BasicAmountConfig(_message.Message):
    __slots__ = ()
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    rate: float
    min_increment: _wrappers_pb2.Int64Value
    max_increment: _wrappers_pb2.Int64Value
    def __init__(self, amount: _Optional[int] = ..., rate: _Optional[float] = ..., min_increment: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_increment: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
