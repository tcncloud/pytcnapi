from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicConfig(_message.Message):
    __slots__ = ("rate", "precision")
    RATE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    rate: _decimal_pb2.Decimal
    precision: int
    def __init__(self, rate: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., precision: _Optional[int] = ...) -> None: ...

class BasicUnitConfig(_message.Message):
    __slots__ = ("unit_size", "min_units", "max_units", "rate", "precision")
    UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    MIN_UNITS_FIELD_NUMBER: _ClassVar[int]
    MAX_UNITS_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    unit_size: int
    min_units: _wrappers_pb2.Int64Value
    max_units: _wrappers_pb2.Int64Value
    rate: _decimal_pb2.Decimal
    precision: int
    def __init__(self, unit_size: _Optional[int] = ..., min_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., rate: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ..., precision: _Optional[int] = ...) -> None: ...
