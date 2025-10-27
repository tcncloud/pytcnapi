from api.commons import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RepeatFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPEAT_FREQUENCY_UNSPECIFIED: _ClassVar[RepeatFrequency]
    REPEAT_FREQUENCY_ON_HOUR: _ClassVar[RepeatFrequency]
    REPEAT_FREQUENCY_15_MINUTES: _ClassVar[RepeatFrequency]
    REPEAT_FREQUENCY_30_MINUTES: _ClassVar[RepeatFrequency]

class DayFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DAY_FILTER_TYPE_UNSPECIFIED: _ClassVar[DayFilterType]
    DAY_FILTER_TYPE_EVERY_DAY: _ClassVar[DayFilterType]
    DAY_FILTER_TYPE_DAY_OF_WEEK: _ClassVar[DayFilterType]
    DAY_FILTER_TYPE_DAY_OF_MONTH: _ClassVar[DayFilterType]

class ReportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_FORMAT_UNSPECIFIED: _ClassVar[ReportFormat]
    REPORT_FORMAT_CSV: _ClassVar[ReportFormat]

class TimePeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_PERIOD_UNSPECIFIED: _ClassVar[TimePeriod]
    TIME_PERIOD_TODAY: _ClassVar[TimePeriod]
    TIME_PERIOD_THIS_WEEK: _ClassVar[TimePeriod]
    TIME_PERIOD_THIS_MONTH: _ClassVar[TimePeriod]
    TIME_PERIOD_THIS_YEAR: _ClassVar[TimePeriod]
    TIME_PERIOD_THE_DAY_SO_FAR: _ClassVar[TimePeriod]
    TIME_PERIOD_WEEK_TO_DATE: _ClassVar[TimePeriod]
    TIME_PERIOD_MONTH_TO_DATE: _ClassVar[TimePeriod]
    TIME_PERIOD_YEAR_TO_DATE: _ClassVar[TimePeriod]
    TIME_PERIOD_YESTERDAY: _ClassVar[TimePeriod]
    TIME_PERIOD_DAY_BEFORE_YESTERDAY: _ClassVar[TimePeriod]
    TIME_PERIOD_THIS_DAY_LAST_WEEK: _ClassVar[TimePeriod]
    TIME_PERIOD_PREVIOUS_WEEK: _ClassVar[TimePeriod]
    TIME_PERIOD_PREVIOUS_MONTH: _ClassVar[TimePeriod]
    TIME_PERIOD_PREVIOUS_YEAR: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_15_MINUTES: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_30_MINUTES: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_1_HOUR: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_2_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_3_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_4_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_6_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_12_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_24_HOURS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_2_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_3_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_7_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_2_WEEKS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_30_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_60_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_90_DAYS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_6_MONTHS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_1_YEAR: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_2_YEARS: _ClassVar[TimePeriod]
    TIME_PERIOD_LAST_5_YEARS: _ClassVar[TimePeriod]

class FilenamePartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILENAME_PART_TYPE_UNSPECIFIED: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_DASHBOARD_NAME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_JOB_NAME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_INSIGHT_NAME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_DATE_TIME_FILTER_TEXT: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_START_DATE_TIME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_END_DATE_TIME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_REPORT_DATE_TIME: _ClassVar[FilenamePartType]
    FILENAME_PART_TYPE_STATIC_TEXT: _ClassVar[FilenamePartType]
REPEAT_FREQUENCY_UNSPECIFIED: RepeatFrequency
REPEAT_FREQUENCY_ON_HOUR: RepeatFrequency
REPEAT_FREQUENCY_15_MINUTES: RepeatFrequency
REPEAT_FREQUENCY_30_MINUTES: RepeatFrequency
DAY_FILTER_TYPE_UNSPECIFIED: DayFilterType
DAY_FILTER_TYPE_EVERY_DAY: DayFilterType
DAY_FILTER_TYPE_DAY_OF_WEEK: DayFilterType
DAY_FILTER_TYPE_DAY_OF_MONTH: DayFilterType
REPORT_FORMAT_UNSPECIFIED: ReportFormat
REPORT_FORMAT_CSV: ReportFormat
TIME_PERIOD_UNSPECIFIED: TimePeriod
TIME_PERIOD_TODAY: TimePeriod
TIME_PERIOD_THIS_WEEK: TimePeriod
TIME_PERIOD_THIS_MONTH: TimePeriod
TIME_PERIOD_THIS_YEAR: TimePeriod
TIME_PERIOD_THE_DAY_SO_FAR: TimePeriod
TIME_PERIOD_WEEK_TO_DATE: TimePeriod
TIME_PERIOD_MONTH_TO_DATE: TimePeriod
TIME_PERIOD_YEAR_TO_DATE: TimePeriod
TIME_PERIOD_YESTERDAY: TimePeriod
TIME_PERIOD_DAY_BEFORE_YESTERDAY: TimePeriod
TIME_PERIOD_THIS_DAY_LAST_WEEK: TimePeriod
TIME_PERIOD_PREVIOUS_WEEK: TimePeriod
TIME_PERIOD_PREVIOUS_MONTH: TimePeriod
TIME_PERIOD_PREVIOUS_YEAR: TimePeriod
TIME_PERIOD_LAST_15_MINUTES: TimePeriod
TIME_PERIOD_LAST_30_MINUTES: TimePeriod
TIME_PERIOD_LAST_1_HOUR: TimePeriod
TIME_PERIOD_LAST_2_HOURS: TimePeriod
TIME_PERIOD_LAST_3_HOURS: TimePeriod
TIME_PERIOD_LAST_4_HOURS: TimePeriod
TIME_PERIOD_LAST_6_HOURS: TimePeriod
TIME_PERIOD_LAST_12_HOURS: TimePeriod
TIME_PERIOD_LAST_24_HOURS: TimePeriod
TIME_PERIOD_LAST_2_DAYS: TimePeriod
TIME_PERIOD_LAST_3_DAYS: TimePeriod
TIME_PERIOD_LAST_7_DAYS: TimePeriod
TIME_PERIOD_LAST_2_WEEKS: TimePeriod
TIME_PERIOD_LAST_30_DAYS: TimePeriod
TIME_PERIOD_LAST_60_DAYS: TimePeriod
TIME_PERIOD_LAST_90_DAYS: TimePeriod
TIME_PERIOD_LAST_6_MONTHS: TimePeriod
TIME_PERIOD_LAST_1_YEAR: TimePeriod
TIME_PERIOD_LAST_2_YEARS: TimePeriod
TIME_PERIOD_LAST_5_YEARS: TimePeriod
FILENAME_PART_TYPE_UNSPECIFIED: FilenamePartType
FILENAME_PART_TYPE_DASHBOARD_NAME: FilenamePartType
FILENAME_PART_TYPE_JOB_NAME: FilenamePartType
FILENAME_PART_TYPE_INSIGHT_NAME: FilenamePartType
FILENAME_PART_TYPE_DATE_TIME_FILTER_TEXT: FilenamePartType
FILENAME_PART_TYPE_START_DATE_TIME: FilenamePartType
FILENAME_PART_TYPE_END_DATE_TIME: FilenamePartType
FILENAME_PART_TYPE_REPORT_DATE_TIME: FilenamePartType
FILENAME_PART_TYPE_STATIC_TEXT: FilenamePartType

class DeliveryTimes(_message.Message):
    __slots__ = ()
    DELIVERY_TIMES_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    delivery_times: _containers.RepeatedScalarFieldContainer[int]
    repeat_frequency: RepeatFrequency
    def __init__(self, delivery_times: _Optional[_Iterable[int]] = ..., repeat_frequency: _Optional[_Union[RepeatFrequency, str]] = ...) -> None: ...

class DayOfWeekFilter(_message.Message):
    __slots__ = ()
    DAYS_OF_WEEKS_FIELD_NUMBER: _ClassVar[int]
    WEEKS_OF_MONTHS_FIELD_NUMBER: _ClassVar[int]
    days_of_weeks: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    weeks_of_months: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, days_of_weeks: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., weeks_of_months: _Optional[_Iterable[int]] = ...) -> None: ...

class DayOfMonthFilter(_message.Message):
    __slots__ = ()
    DAY_OF_MONTHS_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    day_of_months: _containers.RepeatedScalarFieldContainer[int]
    is_last_day_of_month: bool
    def __init__(self, day_of_months: _Optional[_Iterable[int]] = ..., is_last_day_of_month: _Optional[bool] = ...) -> None: ...

class DayFilter(_message.Message):
    __slots__ = ()
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FILTER_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FILTER_FIELD_NUMBER: _ClassVar[int]
    type: DayFilterType
    day_of_week_filter: DayOfWeekFilter
    day_of_month_filter: DayOfMonthFilter
    def __init__(self, type: _Optional[_Union[DayFilterType, str]] = ..., day_of_week_filter: _Optional[_Union[DayOfWeekFilter, _Mapping]] = ..., day_of_month_filter: _Optional[_Union[DayOfMonthFilter, _Mapping]] = ...) -> None: ...

class FormatOptions(_message.Message):
    __slots__ = ()
    REPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_PARTS_FIELD_NUMBER: _ClassVar[int]
    report_format: ReportFormat
    filename_parts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, report_format: _Optional[_Union[ReportFormat, str]] = ..., filename_parts: _Optional[_Iterable[str]] = ...) -> None: ...

class DeliveryOptions(_message.Message):
    __slots__ = ()
    TRANSFER_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_NOTIFICATION_EMAILS_FIELD_NUMBER: _ClassVar[int]
    transfer_config_sid: int
    failure_notification_emails: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transfer_config_sid: _Optional[int] = ..., failure_notification_emails: _Optional[_Iterable[str]] = ...) -> None: ...

class FilenamePart(_message.Message):
    __slots__ = ()
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATIC_TEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_PARTS_FIELD_NUMBER: _ClassVar[int]
    type: FilenamePartType
    static_text: str
    date_parts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[FilenamePartType, str]] = ..., static_text: _Optional[str] = ..., date_parts: _Optional[_Iterable[str]] = ...) -> None: ...

class TransferOptions(_message.Message):
    __slots__ = ()
    TRANSFER_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_PARTS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DEFINITION_TITLE_FIELD_NUMBER: _ClassVar[int]
    transfer_config_sid: str
    filename_parts: _containers.RepeatedCompositeFieldContainer[FilenamePart]
    delivery_definition_title: str
    def __init__(self, transfer_config_sid: _Optional[str] = ..., filename_parts: _Optional[_Iterable[_Union[FilenamePart, _Mapping]]] = ..., delivery_definition_title: _Optional[str] = ...) -> None: ...
