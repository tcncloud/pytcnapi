from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicConfig(_message.Message):
    __slots__ = ()
    RATE_FIELD_NUMBER: _ClassVar[int]
    RATE_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    rate: float
    rate_decimal: _decimal_pb2.Decimal
    def __init__(self, rate: _Optional[float] = ..., rate_decimal: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...

class BasicUnitConfig(_message.Message):
    __slots__ = ()
    UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    MIN_UNITS_FIELD_NUMBER: _ClassVar[int]
    MAX_UNITS_FIELD_NUMBER: _ClassVar[int]
    MIN_UNITS_PER_CYCLE_FIELD_NUMBER: _ClassVar[int]
    MAX_UNITS_PER_CYCLE_FIELD_NUMBER: _ClassVar[int]
    RATE_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    unit_size: int
    rate: float
    min_units: _wrappers_pb2.Int64Value
    max_units: _wrappers_pb2.Int64Value
    min_units_per_cycle: _wrappers_pb2.Int64Value
    max_units_per_cycle: _wrappers_pb2.Int64Value
    rate_decimal: _decimal_pb2.Decimal
    def __init__(self, unit_size: _Optional[int] = ..., rate: _Optional[float] = ..., min_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_units: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_units_per_cycle: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_units_per_cycle: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., rate_decimal: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...
