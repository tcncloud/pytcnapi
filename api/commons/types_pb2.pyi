import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CronExpression(_message.Message):
    __slots__ = ()
    REPEAT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    HOURS_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTHS_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    repeat_minutes: str
    hours_of_day: str
    days_of_month: str
    months_of_year: str
    day_of_week: str
    def __init__(self, repeat_minutes: _Optional[str] = ..., hours_of_day: _Optional[str] = ..., days_of_month: _Optional[str] = ..., months_of_year: _Optional[str] = ..., day_of_week: _Optional[str] = ...) -> None: ...

class Int32Nullable(_message.Message):
    __slots__ = ()
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    value: int
    def __init__(self, is_null: _Optional[bool] = ..., value: _Optional[int] = ...) -> None: ...

class Int64Nullable(_message.Message):
    __slots__ = ()
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    value: int
    def __init__(self, is_null: _Optional[bool] = ..., value: _Optional[int] = ...) -> None: ...

class SomeSidAndDateCompare(_message.Message):
    __slots__ = ()
    SOME_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_GREATER_FIELD_NUMBER: _ClassVar[int]
    DATE_LESS_FIELD_NUMBER: _ClassVar[int]
    some_sid: int
    date_greater: _timestamp_pb2.Timestamp
    date_less: _timestamp_pb2.Timestamp
    def __init__(self, some_sid: _Optional[int] = ..., date_greater: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_less: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Int64ArraySql(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class Int32ArraySql(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class StringArraySql(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class BoolArraySql(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, values: _Optional[_Iterable[bool]] = ...) -> None: ...

class Int32ValueArraySql(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    def __init__(self, values: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ...) -> None: ...

class Int64Id(_message.Message):
    __slots__ = ()
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
