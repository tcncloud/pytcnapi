from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingAccumulateItemsEvent(_message.Message):
    __slots__ = ("org_id", "product_type", "event_log_ids", "billing_cycle", "event_data")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_LOG_IDS_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    product_type: int
    event_log_ids: _containers.RepeatedScalarFieldContainer[int]
    billing_cycle: str
    event_data: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, org_id: _Optional[str] = ..., product_type: _Optional[int] = ..., event_log_ids: _Optional[_Iterable[int]] = ..., billing_cycle: _Optional[str] = ..., event_data: _Optional[_Iterable[bytes]] = ...) -> None: ...

class BillingCommitBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan_id", "user_id")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    user_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingCreateBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan", "user_id")
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan: str
    user_id: str
    def __init__(self, billing_plan: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingCreateInvoiceEvent(_message.Message):
    __slots__ = ("invoice", "user_id")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice: str
    user_id: str
    def __init__(self, invoice: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingCreateRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition", "user_id")
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition: str
    user_id: str
    def __init__(self, rate_definition: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan_id", "user_id")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: str
    user_id: str
    def __init__(self, billing_plan_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteInvoiceEvent(_message.Message):
    __slots__ = ("invoice_id", "user_id")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    user_id: str
    def __init__(self, invoice_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition_id", "user_id")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    user_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingExportInvoiceEvent(_message.Message):
    __slots__ = ("invoice_id", "user_id")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    user_id: str
    def __init__(self, invoice_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan", "user_id")
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan: str
    user_id: str
    def __init__(self, billing_plan: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateInvoiceEvent(_message.Message):
    __slots__ = ("invoice", "user_id")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice: str
    user_id: str
    def __init__(self, invoice: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition", "user_id")
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition: str
    user_id: str
    def __init__(self, rate_definition: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingRatedItemsGeneratedEvent(_message.Message):
    __slots__ = ("rated_items",)
    class RatedItem(_message.Message):
        __slots__ = ("rated_item_id", "billing_cycle", "event_log_id", "module_name", "org_id", "rate_definition_id", "sku_id")
        RATED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
        EVENT_LOG_ID_FIELD_NUMBER: _ClassVar[int]
        MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
        SKU_ID_FIELD_NUMBER: _ClassVar[int]
        rated_item_id: str
        billing_cycle: str
        event_log_id: str
        module_name: str
        org_id: str
        rate_definition_id: str
        sku_id: str
        def __init__(self, rated_item_id: _Optional[str] = ..., billing_cycle: _Optional[str] = ..., event_log_id: _Optional[str] = ..., module_name: _Optional[str] = ..., org_id: _Optional[str] = ..., rate_definition_id: _Optional[str] = ..., sku_id: _Optional[str] = ...) -> None: ...
    RATED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    rated_items: _containers.RepeatedCompositeFieldContainer[BillingRatedItemsGeneratedEvent.RatedItem]
    def __init__(self, rated_items: _Optional[_Iterable[_Union[BillingRatedItemsGeneratedEvent.RatedItem, _Mapping]]] = ...) -> None: ...
