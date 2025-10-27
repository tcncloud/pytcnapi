import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HoldQueueMonitorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HOLD_QUEUE_MONITOR_STATUS_UNSPECIFIED: _ClassVar[HoldQueueMonitorStatus]
    HOLD_QUEUE_MONITOR_STATUS_MONITORING: _ClassVar[HoldQueueMonitorStatus]
    HOLD_QUEUE_MONITOR_STATUS_SUCCESS: _ClassVar[HoldQueueMonitorStatus]
    HOLD_QUEUE_MONITOR_STATUS_FAILED: _ClassVar[HoldQueueMonitorStatus]
    HOLD_QUEUE_MONITOR_STATUS_ENDED: _ClassVar[HoldQueueMonitorStatus]
HOLD_QUEUE_MONITOR_STATUS_UNSPECIFIED: HoldQueueMonitorStatus
HOLD_QUEUE_MONITOR_STATUS_MONITORING: HoldQueueMonitorStatus
HOLD_QUEUE_MONITOR_STATUS_SUCCESS: HoldQueueMonitorStatus
HOLD_QUEUE_MONITOR_STATUS_FAILED: HoldQueueMonitorStatus
HOLD_QUEUE_MONITOR_STATUS_ENDED: HoldQueueMonitorStatus

class HoldQueueCallStats(_message.Message):
    __slots__ = ()
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MONITOR_DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    MONITOR_START_TIME_FIELD_NUMBER: _ClassVar[int]
    MONITOR_END_TIME_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    org_id: str
    campaign_id: str
    phone_number: str
    status: HoldQueueMonitorStatus
    monitor_duration_millis: int
    monitor_start_time: _timestamp_pb2.Timestamp
    monitor_end_time: _timestamp_pb2.Timestamp
    def __init__(self, call_id: _Optional[str] = ..., org_id: _Optional[str] = ..., campaign_id: _Optional[str] = ..., phone_number: _Optional[str] = ..., status: _Optional[_Union[HoldQueueMonitorStatus, str]] = ..., monitor_duration_millis: _Optional[int] = ..., monitor_start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., monitor_end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
