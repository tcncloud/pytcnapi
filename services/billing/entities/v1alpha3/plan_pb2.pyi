from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingPlanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BILLING_PLAN_TYPE_UNSPECIFIED: _ClassVar[BillingPlanType]
    BILLING_PLAN_TYPE_DEFAULT: _ClassVar[BillingPlanType]
    BILLING_PLAN_TYPE_ORG: _ClassVar[BillingPlanType]
BILLING_PLAN_TYPE_UNSPECIFIED: BillingPlanType
BILLING_PLAN_TYPE_DEFAULT: BillingPlanType
BILLING_PLAN_TYPE_ORG: BillingPlanType

class BillingPlan(_message.Message):
    __slots__ = ("billing_plan_id", "title", "type", "is_draft", "start_time", "create_time", "update_time", "delete_time", "user_id")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DRAFT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    title: str
    type: BillingPlanType
    is_draft: bool
    start_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    user_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ..., title: _Optional[str] = ..., type: _Optional[_Union[BillingPlanType, str]] = ..., is_draft: bool = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...
