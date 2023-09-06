from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderByDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ORDER_BY_DIRECTION_UNSPECIFIED: _ClassVar[OrderByDirection]
    ORDER_BY_DIRECTION_ASC: _ClassVar[OrderByDirection]
    ORDER_BY_DIRECTION_DESC: _ClassVar[OrderByDirection]

class TimeSelectorOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TIME_SELECTOR_OP_UNSPECIFIED: _ClassVar[TimeSelectorOp]
    TIME_SELECTOR_OP_EQ: _ClassVar[TimeSelectorOp]
    TIME_SELECTOR_OP_GT: _ClassVar[TimeSelectorOp]
    TIME_SELECTOR_OP_GE: _ClassVar[TimeSelectorOp]
    TIME_SELECTOR_OP_LT: _ClassVar[TimeSelectorOp]
    TIME_SELECTOR_OP_LE: _ClassVar[TimeSelectorOp]
ORDER_BY_DIRECTION_UNSPECIFIED: OrderByDirection
ORDER_BY_DIRECTION_ASC: OrderByDirection
ORDER_BY_DIRECTION_DESC: OrderByDirection
TIME_SELECTOR_OP_UNSPECIFIED: TimeSelectorOp
TIME_SELECTOR_OP_EQ: TimeSelectorOp
TIME_SELECTOR_OP_GT: TimeSelectorOp
TIME_SELECTOR_OP_GE: TimeSelectorOp
TIME_SELECTOR_OP_LT: TimeSelectorOp
TIME_SELECTOR_OP_LE: TimeSelectorOp

class OrderBy(_message.Message):
    __slots__ = ["fields", "direction"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    direction: OrderByDirection
    def __init__(self, fields: _Optional[_Iterable[str]] = ..., direction: _Optional[_Union[OrderByDirection, str]] = ...) -> None: ...

class TimeSelector(_message.Message):
    __slots__ = ["field_name", "op", "value"]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    op: TimeSelectorOp
    value: _timestamp_pb2.Timestamp
    def __init__(self, field_name: _Optional[str] = ..., op: _Optional[_Union[TimeSelectorOp, str]] = ..., value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
