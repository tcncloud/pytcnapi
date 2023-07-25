from api.commons.integrations import integrations_pb2 as _integrations_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Values(_message.Message):
    __slots__ = ["values"]
    class ValuesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, Value]
    def __init__(self, values: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ["str_val", "num_val", "bool_val", "time_val", "comp_val", "int_val", "sensitive", "validation"]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    NUM_VAL_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    TIME_VAL_FIELD_NUMBER: _ClassVar[int]
    COMP_VAL_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    str_val: str
    num_val: float
    bool_val: bool
    time_val: _timestamp_pb2.Timestamp
    comp_val: CompositeVal
    int_val: int
    sensitive: bool
    validation: _integrations_pb2.Validation
    def __init__(self, str_val: _Optional[str] = ..., num_val: _Optional[float] = ..., bool_val: bool = ..., time_val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comp_val: _Optional[_Union[CompositeVal, _Mapping]] = ..., int_val: _Optional[int] = ..., sensitive: bool = ..., validation: _Optional[_Union[_integrations_pb2.Validation, str]] = ...) -> None: ...

class CompositeVal(_message.Message):
    __slots__ = ["parts"]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[FieldOrStr]
    def __init__(self, parts: _Optional[_Iterable[_Union[FieldOrStr, _Mapping]]] = ...) -> None: ...

class FieldOrStr(_message.Message):
    __slots__ = ["field", "str_val"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    field: str
    str_val: str
    def __init__(self, field: _Optional[str] = ..., str_val: _Optional[str] = ...) -> None: ...

class PortalConfigId(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PortalConfig(_message.Message):
    __slots__ = ["id", "name", "description", "chat_client_link", "contact_email", "contact_phone", "postal_code", "city", "state", "company_name", "logo", "primary_color", "secondary_color", "street_address"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAT_CLIENT_LINK_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONTACT_PHONE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    chat_client_link: str
    contact_email: str
    contact_phone: str
    postal_code: str
    city: str
    state: str
    company_name: str
    logo: bytes
    primary_color: str
    secondary_color: str
    street_address: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., chat_client_link: _Optional[str] = ..., contact_email: _Optional[str] = ..., contact_phone: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., company_name: _Optional[str] = ..., logo: _Optional[bytes] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., street_address: _Optional[str] = ...) -> None: ...

class PortalLinkId(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetLinkDataReq(_message.Message):
    __slots__ = ["entity"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ...) -> None: ...

class GetLinkDataRes(_message.Message):
    __slots__ = ["complete", "expired", "portal_config", "verification", "invoice", "payments", "flow_forms", "portal_text"]
    class FieldNames(_message.Message):
        __slots__ = ["flow", "field_names", "fields"]
        FLOW_FIELD_NUMBER: _ClassVar[int]
        FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        flow: _integrations_pb2.Flow
        field_names: _containers.RepeatedScalarFieldContainer[str]
        fields: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.FieldDefinition]
        def __init__(self, flow: _Optional[_Union[_integrations_pb2.Flow, _Mapping]] = ..., field_names: _Optional[_Iterable[str]] = ..., fields: _Optional[_Iterable[_Union[_integrations_pb2.FieldDefinition, _Mapping]]] = ...) -> None: ...
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    FLOW_FORMS_FIELD_NUMBER: _ClassVar[int]
    PORTAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    complete: bool
    expired: bool
    portal_config: PortalConfig
    verification: _integrations_pb2.VerificationFlow
    invoice: _integrations_pb2.InvoiceFlow
    payments: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.PaymentFlow]
    flow_forms: _containers.RepeatedCompositeFieldContainer[GetLinkDataRes.FieldNames]
    portal_text: PortalText
    def __init__(self, complete: bool = ..., expired: bool = ..., portal_config: _Optional[_Union[PortalConfig, _Mapping]] = ..., verification: _Optional[_Union[_integrations_pb2.VerificationFlow, _Mapping]] = ..., invoice: _Optional[_Union[_integrations_pb2.InvoiceFlow, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[_integrations_pb2.PaymentFlow, _Mapping]]] = ..., flow_forms: _Optional[_Iterable[_Union[GetLinkDataRes.FieldNames, _Mapping]]] = ..., portal_text: _Optional[_Union[PortalText, _Mapping]] = ...) -> None: ...

class PortalText(_message.Message):
    __slots__ = ["verification_header", "verification_footer", "payment_header", "payment_footer", "receipt_header", "receipt_footer", "invoice_header", "invoice_footer"]
    VERIFICATION_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FOOTER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FOOTER_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HEADER_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FOOTER_FIELD_NUMBER: _ClassVar[int]
    INVOICE_HEADER_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FOOTER_FIELD_NUMBER: _ClassVar[int]
    verification_header: str
    verification_footer: str
    payment_header: str
    payment_footer: str
    receipt_header: str
    receipt_footer: str
    invoice_header: str
    invoice_footer: str
    def __init__(self, verification_header: _Optional[str] = ..., verification_footer: _Optional[str] = ..., payment_header: _Optional[str] = ..., payment_footer: _Optional[str] = ..., receipt_header: _Optional[str] = ..., receipt_footer: _Optional[str] = ..., invoice_header: _Optional[str] = ..., invoice_footer: _Optional[str] = ...) -> None: ...

class SubmitVerificationReq(_message.Message):
    __slots__ = ["entity", "verification_fields"]
    class VerificationFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    verification_fields: _containers.MessageMap[str, Value]
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., verification_fields: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class SubmitVerificationRes(_message.Message):
    __slots__ = ["verified", "session_id"]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    session_id: str
    def __init__(self, verified: bool = ..., session_id: _Optional[str] = ...) -> None: ...

class SessionKeepAliveReq(_message.Message):
    __slots__ = ["entity", "session_id"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class SessionKeepAliveRes(_message.Message):
    __slots__ = ["ok", "session_id"]
    OK_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    session_id: str
    def __init__(self, ok: bool = ..., session_id: _Optional[str] = ...) -> None: ...

class GetInvoiceReq(_message.Message):
    __slots__ = ["entity", "session_id"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetInvoiceRes(_message.Message):
    __slots__ = ["fields", "amount_due", "amount_due_key", "invoices"]
    class FieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_DUE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_DUE_KEY_FIELD_NUMBER: _ClassVar[int]
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Value]
    amount_due: float
    amount_due_key: str
    invoices: _integrations_pb2.Invoices
    def __init__(self, fields: _Optional[_Mapping[str, Value]] = ..., amount_due: _Optional[float] = ..., amount_due_key: _Optional[str] = ..., invoices: _Optional[_Union[_integrations_pb2.Invoices, _Mapping]] = ...) -> None: ...

class SubmitPaymentReq(_message.Message):
    __slots__ = ["entity", "session_id", "payment_fields", "payment_flow"]
    class PaymentFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FLOW_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    payment_fields: _containers.MessageMap[str, Value]
    payment_flow: _integrations_pb2.PaymentFlow
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ..., payment_fields: _Optional[_Mapping[str, Value]] = ..., payment_flow: _Optional[_Union[_integrations_pb2.PaymentFlow, _Mapping]] = ...) -> None: ...

class SubmitPaymentRes(_message.Message):
    __slots__ = ["fields", "amount_paid", "amount_paid_key"]
    class FieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_KEY_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Value]
    amount_paid: float
    amount_paid_key: str
    def __init__(self, fields: _Optional[_Mapping[str, Value]] = ..., amount_paid: _Optional[float] = ..., amount_paid_key: _Optional[str] = ...) -> None: ...

class GetReceiptReq(_message.Message):
    __slots__ = ["entity", "session_id"]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetReceiptRes(_message.Message):
    __slots__ = ["receipt_id", "request", "response", "amount_paid", "amount_paid_key", "payment_flow"]
    class RequestEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class ResponseEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    RECEIPT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_KEY_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FLOW_FIELD_NUMBER: _ClassVar[int]
    receipt_id: str
    request: _containers.MessageMap[str, Value]
    response: _containers.MessageMap[str, Value]
    amount_paid: float
    amount_paid_key: str
    payment_flow: _integrations_pb2.PaymentFlow
    def __init__(self, receipt_id: _Optional[str] = ..., request: _Optional[_Mapping[str, Value]] = ..., response: _Optional[_Mapping[str, Value]] = ..., amount_paid: _Optional[float] = ..., amount_paid_key: _Optional[str] = ..., payment_flow: _Optional[_Union[_integrations_pb2.PaymentFlow, _Mapping]] = ...) -> None: ...
