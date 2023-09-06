from data.billing.v1alpha1 import plans_pb2 as _plans_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBillingPlanRequest(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class CreateBillingPlanResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class DeleteBillingPlanRequest(_message.Message):
    __slots__ = ["billing_plan_id"]
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DeleteBillingPlanResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBillingPlanRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetBillingPlanResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class GetDefaultBillingPlanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDefaultBillingPlanResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class ListBillingPlansRequest(_message.Message):
    __slots__ = ["billing_plan", "selector_fields", "return_fields", "order_by", "time_selectors"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELDS_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    TIME_SELECTORS_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    selector_fields: _field_mask_pb2.FieldMask
    return_fields: _field_mask_pb2.FieldMask
    order_by: _core_pb2.OrderBy
    time_selectors: _containers.RepeatedCompositeFieldContainer[_core_pb2.TimeSelector]
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ..., selector_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., return_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order_by: _Optional[_Union[_core_pb2.OrderBy, _Mapping]] = ..., time_selectors: _Optional[_Iterable[_Union[_core_pb2.TimeSelector, _Mapping]]] = ...) -> None: ...

class ListBillingPlansResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class UpdateBillingPlanRequest(_message.Message):
    __slots__ = ["billing_plan", "update_fields"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBillingPlanResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...

class UpdateDefaultBillingPlanRequest(_message.Message):
    __slots__ = ["billing_plan", "update_fields"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDefaultBillingPlanResponse(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plans_pb2.BillingPlan
    def __init__(self, billing_plan: _Optional[_Union[_plans_pb2.BillingPlan, _Mapping]] = ...) -> None: ...
