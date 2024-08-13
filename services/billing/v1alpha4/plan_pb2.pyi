from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha4 import plan_pb2 as _plan_pb2
from services.billing.entities.v1alpha4 import rates_pb2 as _rates_pb2
from services.billing.v1alpha4 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyBillingPlanDraftRequest(_message.Message):
    __slots__ = ("billing_plan_id", "start_time", "org_ids")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    start_time: _timestamp_pb2.Timestamp
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, billing_plan_id: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., org_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyBillingPlanDraftResponse(_message.Message):
    __slots__ = ("billing_plan_ids",)
    BILLING_PLAN_IDS_FIELD_NUMBER: _ClassVar[int]
    billing_plan_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, billing_plan_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CloneBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class CloneBillingPlanResponse(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

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

class DeleteBillingPlanRequest(_message.Message):
    __slots__ = ("billing_plan_id",)
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ...) -> None: ...

class DeleteBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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
    __slots__ = ("billing_plan_id", "billing_plan", "update_mask")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    billing_plan: _plan_pb2.BillingPlan
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, billing_plan_id: _Optional[str] = ..., billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBillingPlanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id", "rate_definition")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class CreateRateDefinitionResponse(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class GetRateDefinitionResponse(_message.Message):
    __slots__ = ("rate_definition",)
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class ListRateDefinitionsRequest(_message.Message):
    __slots__ = ("rate_definition_id", "filter", "fields", "sort", "page")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, rate_definition_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListRateDefinitionsResponse(_message.Message):
    __slots__ = ("rate_definitions", "token")
    RATE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    rate_definitions: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    token: str
    def __init__(self, rate_definitions: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id", "rate_definition", "update_mask")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
