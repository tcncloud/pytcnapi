from api.commons import bireportgenerator_pb2 as _bireportgenerator_pb2
from api.commons import enums_pb2 as _enums_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportJob(_message.Message):
    __slots__ = ("report_job_id", "name", "description", "dashboard_id", "time_zone", "time_period", "delivery_times", "day_filter", "months", "format_options", "delivery_options", "is_active", "send_empty_report", "dashboard_resource_id", "time_zone_wrapper", "hide_csv_footer", "transfer_config_sid", "cron_expression", "transfer_options")
    REPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIMES_FIELD_NUMBER: _ClassVar[int]
    DAY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SEND_EMPTY_REPORT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    HIDE_CSV_FOOTER_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    report_job_id: str
    name: str
    description: str
    dashboard_id: str
    time_zone: str
    time_period: _bireportgenerator_pb2.TimePeriod
    delivery_times: _bireportgenerator_pb2.DeliveryTimes
    day_filter: _bireportgenerator_pb2.DayFilter
    months: _containers.RepeatedScalarFieldContainer[_enums_pb2.Month]
    format_options: _bireportgenerator_pb2.FormatOptions
    delivery_options: _bireportgenerator_pb2.DeliveryOptions
    is_active: bool
    send_empty_report: bool
    dashboard_resource_id: str
    time_zone_wrapper: _org_pb2.TimeZoneWrapper
    hide_csv_footer: bool
    transfer_config_sid: int
    cron_expression: _types_pb2.CronExpression
    transfer_options: _bireportgenerator_pb2.TransferOptions
    def __init__(self, report_job_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., dashboard_id: _Optional[str] = ..., time_zone: _Optional[str] = ..., time_period: _Optional[_Union[_bireportgenerator_pb2.TimePeriod, str]] = ..., delivery_times: _Optional[_Union[_bireportgenerator_pb2.DeliveryTimes, _Mapping]] = ..., day_filter: _Optional[_Union[_bireportgenerator_pb2.DayFilter, _Mapping]] = ..., months: _Optional[_Iterable[_Union[_enums_pb2.Month, str]]] = ..., format_options: _Optional[_Union[_bireportgenerator_pb2.FormatOptions, _Mapping]] = ..., delivery_options: _Optional[_Union[_bireportgenerator_pb2.DeliveryOptions, _Mapping]] = ..., is_active: bool = ..., send_empty_report: bool = ..., dashboard_resource_id: _Optional[str] = ..., time_zone_wrapper: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., hide_csv_footer: bool = ..., transfer_config_sid: _Optional[int] = ..., cron_expression: _Optional[_Union[_types_pb2.CronExpression, _Mapping]] = ..., transfer_options: _Optional[_Union[_bireportgenerator_pb2.TransferOptions, _Mapping]] = ...) -> None: ...

class ReportLog(_message.Message):
    __slots__ = ("org_id", "report_log_id", "report_job_id", "execution_id", "report_name", "job_requested_time", "job_completed_time", "success", "failure_reason", "attempt_number", "max_attempts", "create_time", "update_time", "dashboard_title", "scheduled_time", "execution_start_time", "execution_end_time", "report_start_date", "report_end_date", "comments", "timezone", "filenames", "insight_count", "delivery_definition_title")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOG_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_REQUESTED_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_COMPLETED_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_TITLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    REPORT_START_DATE_FIELD_NUMBER: _ClassVar[int]
    REPORT_END_DATE_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DEFINITION_TITLE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    report_log_id: int
    report_job_id: int
    execution_id: str
    report_name: str
    job_requested_time: _timestamp_pb2.Timestamp
    job_completed_time: _timestamp_pb2.Timestamp
    success: bool
    failure_reason: str
    attempt_number: int
    max_attempts: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    dashboard_title: str
    scheduled_time: _timestamp_pb2.Timestamp
    execution_start_time: _timestamp_pb2.Timestamp
    execution_end_time: _timestamp_pb2.Timestamp
    report_start_date: _timestamp_pb2.Timestamp
    report_end_date: _timestamp_pb2.Timestamp
    comments: _containers.RepeatedScalarFieldContainer[str]
    timezone: str
    filenames: _containers.RepeatedScalarFieldContainer[str]
    insight_count: int
    delivery_definition_title: str
    def __init__(self, org_id: _Optional[str] = ..., report_log_id: _Optional[int] = ..., report_job_id: _Optional[int] = ..., execution_id: _Optional[str] = ..., report_name: _Optional[str] = ..., job_requested_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., job_completed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success: bool = ..., failure_reason: _Optional[str] = ..., attempt_number: _Optional[int] = ..., max_attempts: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dashboard_title: _Optional[str] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., report_start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., report_end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comments: _Optional[_Iterable[str]] = ..., timezone: _Optional[str] = ..., filenames: _Optional[_Iterable[str]] = ..., insight_count: _Optional[int] = ..., delivery_definition_title: _Optional[str] = ...) -> None: ...
