from api.commons import bireportgenerator_pb2 as _bireportgenerator_pb2
from api.commons import enums_pb2 as _enums_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import types_pb2 as _types_pb2
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
