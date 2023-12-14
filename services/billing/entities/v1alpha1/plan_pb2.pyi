from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import rates_pb2 as _rates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingPlanStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_PLAN_STATUS_UNSPECIFIED: _ClassVar[BillingPlanStatus]
    BILLING_PLAN_STATUS_CREATING: _ClassVar[BillingPlanStatus]
    BILLING_PLAN_STATUS_CREATED: _ClassVar[BillingPlanStatus]
BILLING_PLAN_STATUS_UNSPECIFIED: BillingPlanStatus
BILLING_PLAN_STATUS_CREATING: BillingPlanStatus
BILLING_PLAN_STATUS_CREATED: BillingPlanStatus

class BillingPlan(_message.Message):
    __slots__ = ("billing_plan_id", "create_time", "update_time", "start_time", "end_time", "delete_time", "rate_definition_ids", "status", "actual_start_time")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    rate_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    status: BillingPlanStatus
    actual_start_time: _timestamp_pb2.Timestamp
    def __init__(self, billing_plan_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rate_definition_ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[BillingPlanStatus, str]] = ..., actual_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
