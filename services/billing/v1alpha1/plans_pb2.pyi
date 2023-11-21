from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import plan_pb2 as _plan_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommitBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class CommitBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommitDefaultBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class CommitDefaultBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class CreateBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class CreateDefaultBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class CreateDefaultBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DeleteBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DeleteBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDefaultBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DeleteDefaultBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuplicateBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class DuplicateBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DuplicateDefaultBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class DuplicateDefaultBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class GetActiveBillingPlanRequest(_message.Message):
    __slots__ = ("org_id", "effective_time")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    effective_time: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetActiveBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan",)
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class GetBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class GetBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan",)
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plan_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class ListBillingPlansRequest(_message.Message):
    __slots__ = ("billing_plan_id", "filter", "fields", "sort", "page")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, billing_plan_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListBillingPlansResponse(_message.Message):
    __slots__ = ("billing_plans", "token")
    BILLING_PLANS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    billing_plans: _containers.RepeatedCompositeFieldContainer[_plan_pb2.BillingPlan]
    token: str
    def __init__(self, billing_plans: _Optional[_Iterable[_Union[_plan_pb2.BillingPlan, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan", "update_fields")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateDefaultBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id", "billing_plan", "update_fields")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDefaultBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
