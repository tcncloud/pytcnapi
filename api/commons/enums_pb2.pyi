from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Month(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONTH_JANUARY: _ClassVar[Month]
    MONTH_FEBRUARY: _ClassVar[Month]
    MONTH_MARCH: _ClassVar[Month]
    MONTH_APRIL: _ClassVar[Month]
    MONTH_MAY: _ClassVar[Month]
    MONTH_JUNE: _ClassVar[Month]
    MONTH_JULY: _ClassVar[Month]
    MONTH_AUGUST: _ClassVar[Month]
    MONTH_SEPTEMBER: _ClassVar[Month]
    MONTH_OCTOBER: _ClassVar[Month]
    MONTH_NOVEMBER: _ClassVar[Month]
    MONTH_DECEMBER: _ClassVar[Month]
MONTH_JANUARY: Month
MONTH_FEBRUARY: Month
MONTH_MARCH: Month
MONTH_APRIL: Month
MONTH_MAY: Month
MONTH_JUNE: Month
MONTH_JULY: Month
MONTH_AUGUST: Month
MONTH_SEPTEMBER: Month
MONTH_OCTOBER: Month
MONTH_NOVEMBER: Month
MONTH_DECEMBER: Month

class Weekday(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUNDAY: _ClassVar[Weekday.Enum]
        MONDAY: _ClassVar[Weekday.Enum]
        TUESDAY: _ClassVar[Weekday.Enum]
        WEDNESDAY: _ClassVar[Weekday.Enum]
        THURSDAY: _ClassVar[Weekday.Enum]
        FRIDAY: _ClassVar[Weekday.Enum]
        SATURDAY: _ClassVar[Weekday.Enum]
    SUNDAY: Weekday.Enum
    MONDAY: Weekday.Enum
    TUESDAY: Weekday.Enum
    WEDNESDAY: Weekday.Enum
    THURSDAY: Weekday.Enum
    FRIDAY: Weekday.Enum
    SATURDAY: Weekday.Enum
    def __init__(self) -> None: ...

class CronRequestType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVALID: _ClassVar[CronRequestType.Enum]
        SFTP: _ClassVar[CronRequestType.Enum]
    INVALID: CronRequestType.Enum
    SFTP: CronRequestType.Enum
    def __init__(self) -> None: ...
