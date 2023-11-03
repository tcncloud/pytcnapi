from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Interval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TODAY: _ClassVar[Interval]
    YESTERDAY: _ClassVar[Interval]
    THIS_WEEK: _ClassVar[Interval]
    LAST_7_DAYS: _ClassVar[Interval]
    LAST_WEEK: _ClassVar[Interval]
    LAST_14_DAYS: _ClassVar[Interval]
    THIS_MONTH: _ClassVar[Interval]
    LAST_30_DAYS: _ClassVar[Interval]
    LAST_60_DAYS: _ClassVar[Interval]
    LAST_90_DAYS: _ClassVar[Interval]
    LAST_180_DAYS: _ClassVar[Interval]
TODAY: Interval
YESTERDAY: Interval
THIS_WEEK: Interval
LAST_7_DAYS: Interval
LAST_WEEK: Interval
LAST_14_DAYS: Interval
THIS_MONTH: Interval
LAST_30_DAYS: Interval
LAST_60_DAYS: Interval
LAST_90_DAYS: Interval
LAST_180_DAYS: Interval
