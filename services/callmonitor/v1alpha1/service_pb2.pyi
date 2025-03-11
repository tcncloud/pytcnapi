from annotations import authz_pb2 as _authz_pb2
from api.commons import callmonitor_pb2 as _callmonitor_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHoldQueueStatsRequest(_message.Message):
    __slots__ = ("org_id", "start_time", "end_time", "filter")
    class Filter(_message.Message):
        __slots__ = ("status", "campaign_id")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
        status: _callmonitor_pb2.HoldQueueMonitorStatus
        campaign_id: str
        def __init__(self, status: _Optional[_Union[_callmonitor_pb2.HoldQueueMonitorStatus, str]] = ..., campaign_id: _Optional[str] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    filter: GetHoldQueueStatsRequest.Filter
    def __init__(self, org_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[GetHoldQueueStatsRequest.Filter, _Mapping]] = ...) -> None: ...

class GetHoldQueueStatsResponse(_message.Message):
    __slots__ = ("stats", "total_num_calls", "total_num_successful", "total_num_failed", "avg_monitor_duration_ms", "total_num_monitoring")
    STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_FAILED_FIELD_NUMBER: _ClassVar[int]
    AVG_MONITOR_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_MONITORING_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_callmonitor_pb2.HoldQueueCallStats]
    total_num_calls: int
    total_num_successful: int
    total_num_failed: int
    avg_monitor_duration_ms: int
    total_num_monitoring: int
    def __init__(self, stats: _Optional[_Iterable[_Union[_callmonitor_pb2.HoldQueueCallStats, _Mapping]]] = ..., total_num_calls: _Optional[int] = ..., total_num_successful: _Optional[int] = ..., total_num_failed: _Optional[int] = ..., avg_monitor_duration_ms: _Optional[int] = ..., total_num_monitoring: _Optional[int] = ...) -> None: ...
