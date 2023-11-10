from google.protobuf import wrappers_pb2 as _wrappers_pb2
from services.billing.entities.v1alpha1 import invoice_pb2 as _invoice_pb2
from services.billing.entities.v1alpha1 import plan_pb2 as _plan_pb2
from services.billing.entities.v1alpha1 import rates_pb2 as _rates_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingCreateBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan", "user_id")
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plan_pb2.BillingPlan
    user_id: str
    def __init__(self, billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingCreateInvoiceEvent(_message.Message):
    __slots__ = ("invoice", "user_id")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    user_id: str
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingCreateRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition", "user_id")
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition: _rates_pb2.RateDefinition
    user_id: str
    def __init__(self, rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan_id", "user_id")
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan_id: _wrappers_pb2.StringValue
    user_id: str
    def __init__(self, billing_plan_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteInvoiceEvent(_message.Message):
    __slots__ = ("invoice_id", "user_id")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: _wrappers_pb2.StringValue
    user_id: str
    def __init__(self, invoice_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingDeleteRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition_id", "user_id")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: _wrappers_pb2.StringValue
    user_id: str
    def __init__(self, rate_definition_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingExportInvoiceEvent(_message.Message):
    __slots__ = ("invoice", "user_id")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    user_id: str
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateBillingPlanEvent(_message.Message):
    __slots__ = ("billing_plan", "user_id")
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _plan_pb2.BillingPlan
    user_id: str
    def __init__(self, billing_plan: _Optional[_Union[_plan_pb2.BillingPlan, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateInvoiceEvent(_message.Message):
    __slots__ = ("invoice", "user_id")
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    user_id: str
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class BillingUpdateRateDefinitionEvent(_message.Message):
    __slots__ = ("rate_definition", "user_id")
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition: _rates_pb2.RateDefinition
    user_id: str
    def __init__(self, rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...
