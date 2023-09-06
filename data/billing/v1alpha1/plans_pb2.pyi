from data.billing.v1alpha1 import rates_pb2 as _rates_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingPlan(_message.Message):
    __slots__ = ["billing_plan_id", "org_id", "create_time", "update_time", "start_time", "end_time", "rate_definitions"]
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    org_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    rate_definitions: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    def __init__(self, billing_plan_id: _Optional[str] = ..., org_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rate_definitions: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ...) -> None: ...
