from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

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
