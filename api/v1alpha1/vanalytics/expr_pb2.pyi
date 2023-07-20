from api.commons import vanalytics_pb2 as _vanalytics_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Uint32Expr(_message.Message):
    __slots__ = ["gt", "gte", "lt", "lte", "eq", "not_eq", "range"]
    GT_FIELD_NUMBER: _ClassVar[int]
    GTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    EQ_FIELD_NUMBER: _ClassVar[int]
    NOT_EQ_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    gt: int
    gte: int
    lt: int
    lte: int
    eq: int
    not_eq: int
    range: Uint32Range
    def __init__(self, gt: _Optional[int] = ..., gte: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., eq: _Optional[int] = ..., not_eq: _Optional[int] = ..., range: _Optional[_Union[Uint32Range, _Mapping]] = ...) -> None: ...

class Uint32Range(_message.Message):
    __slots__ = ["to", "include_from", "include_to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FROM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TO_FIELD_NUMBER: _ClassVar[int]
    to: int
    include_from: bool
    include_to: bool
    def __init__(self, to: _Optional[int] = ..., include_from: bool = ..., include_to: bool = ..., **kwargs) -> None: ...

class TimestampExpr(_message.Message):
    __slots__ = ["range", "moment"]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    MOMENT_FIELD_NUMBER: _ClassVar[int]
    range: TimestampRange
    moment: Moment
    def __init__(self, range: _Optional[_Union[TimestampRange, _Mapping]] = ..., moment: _Optional[_Union[Moment, _Mapping]] = ...) -> None: ...

class Moment(_message.Message):
    __slots__ = ["time_zone", "interval"]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    interval: _vanalytics_pb2.Interval
    def __init__(self, time_zone: _Optional[str] = ..., interval: _Optional[_Union[_vanalytics_pb2.Interval, str]] = ...) -> None: ...

class TimestampRange(_message.Message):
    __slots__ = ["to", "include_from", "include_to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FROM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TO_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    include_from: bool
    include_to: bool
    def __init__(self, to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., include_from: bool = ..., include_to: bool = ..., **kwargs) -> None: ...
