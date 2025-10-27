import datetime

from api.commons import acd_pb2 as _acd_pb2
from api.commons.integrations import integrations_pb2 as _integrations_pb2
from api.v1alpha1.integrations import portals_pb2 as _portals_pb2
from api.v1alpha1.integrations import service_pb2 as _service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Values(_message.Message):
    __slots__ = ()
    class ValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, Value]
    def __init__(self, values: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ()
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
    def __init__(self, str_val: _Optional[str] = ..., num_val: _Optional[float] = ..., bool_val: _Optional[bool] = ..., time_val: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comp_val: _Optional[_Union[CompositeVal, _Mapping]] = ..., int_val: _Optional[int] = ..., sensitive: _Optional[bool] = ..., validation: _Optional[_Union[_integrations_pb2.Validation, str]] = ...) -> None: ...

class CompositeVal(_message.Message):
    __slots__ = ()
    PARTS_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[FieldOrStr]
    def __init__(self, parts: _Optional[_Iterable[_Union[FieldOrStr, _Mapping]]] = ...) -> None: ...

class FieldOrStr(_message.Message):
    __slots__ = ()
    FIELD_FIELD_NUMBER: _ClassVar[int]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    field: str
    str_val: str
    def __init__(self, field: _Optional[str] = ..., str_val: _Optional[str] = ...) -> None: ...

class PortalConfigId(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PortalConfig(_message.Message):
    __slots__ = ()
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
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetLinkDataReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ...) -> None: ...

class GetLinkDataRes(_message.Message):
    __slots__ = ()
    class FieldNames(_message.Message):
        __slots__ = ()
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
    def __init__(self, complete: _Optional[bool] = ..., expired: _Optional[bool] = ..., portal_config: _Optional[_Union[PortalConfig, _Mapping]] = ..., verification: _Optional[_Union[_integrations_pb2.VerificationFlow, _Mapping]] = ..., invoice: _Optional[_Union[_integrations_pb2.InvoiceFlow, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[_integrations_pb2.PaymentFlow, _Mapping]]] = ..., flow_forms: _Optional[_Iterable[_Union[GetLinkDataRes.FieldNames, _Mapping]]] = ..., portal_text: _Optional[_Union[PortalText, _Mapping]] = ...) -> None: ...

class PortalText(_message.Message):
    __slots__ = ()
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
    __slots__ = ()
    class VerificationFieldsEntry(_message.Message):
        __slots__ = ()
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
    __slots__ = ()
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    session_id: str
    def __init__(self, verified: _Optional[bool] = ..., session_id: _Optional[str] = ...) -> None: ...

class SessionKeepAliveReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class SessionKeepAliveRes(_message.Message):
    __slots__ = ()
    OK_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    session_id: str
    def __init__(self, ok: _Optional[bool] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetInvoiceReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetInvoiceRes(_message.Message):
    __slots__ = ()
    class FieldsEntry(_message.Message):
        __slots__ = ()
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
    __slots__ = ()
    class PaymentFieldsEntry(_message.Message):
        __slots__ = ()
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
    __slots__ = ()
    class FieldsEntry(_message.Message):
        __slots__ = ()
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
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    session_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetReceiptRes(_message.Message):
    __slots__ = ()
    class RequestEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class ResponseEntry(_message.Message):
        __slots__ = ()
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

class ProcessWorkflowReq(_message.Message):
    __slots__ = ()
    class ParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    PORTAL_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    portal_link_id: str
    portal_id: str
    segment: int
    choice: int
    params: _containers.MessageMap[str, Value]
    request_origin: _integrations_pb2.RequestOrigin
    session_id: str
    def __init__(self, portal_link_id: _Optional[str] = ..., portal_id: _Optional[str] = ..., segment: _Optional[int] = ..., choice: _Optional[int] = ..., params: _Optional[_Mapping[str, Value]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ..., session_id: _Optional[str] = ...) -> None: ...

class ProcessWorkflowRes(_message.Message):
    __slots__ = ()
    class DataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: _containers.MessageMap[str, Value]
    session_id: str
    def __init__(self, success: _Optional[bool] = ..., data: _Optional[_Mapping[str, Value]] = ..., session_id: _Optional[str] = ...) -> None: ...

class GetLinkDetailsReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ...) -> None: ...

class GetLinkDetailsRes(_message.Message):
    __slots__ = ()
    PORTAL_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PORTAL_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    portal: _service_pb2.Portal
    portal_config: PortalConfig
    expired: bool
    completed: bool
    portal_definition: _portals_pb2.PortalDefinition
    def __init__(self, portal: _Optional[_Union[_service_pb2.Portal, _Mapping]] = ..., portal_config: _Optional[_Union[PortalConfig, _Mapping]] = ..., expired: _Optional[bool] = ..., completed: _Optional[bool] = ..., portal_definition: _Optional[_Union[_portals_pb2.PortalDefinition, _Mapping]] = ...) -> None: ...

class CalculateFeesReq(_message.Message):
    __slots__ = ()
    class ParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    FEES_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    fees: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.Fee]
    params: _containers.MessageMap[str, Value]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    request_origin: _integrations_pb2.RequestOrigin
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., fees: _Optional[_Iterable[_Union[_integrations_pb2.Fee, _Mapping]]] = ..., params: _Optional[_Mapping[str, Value]] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ...) -> None: ...

class CalculateFeesRes(_message.Message):
    __slots__ = ()
    class CalculatedFeesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _money_pb2.Money
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...
    CALCULATED_FEES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_DUE_FIELD_NUMBER: _ClassVar[int]
    calculated_fees: _containers.MessageMap[str, _money_pb2.Money]
    total_amount_due: _money_pb2.Money
    def __init__(self, calculated_fees: _Optional[_Mapping[str, _money_pb2.Money]] = ..., total_amount_due: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...

class DeliverReceiptReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalLinkId
    email_receipt: EmailReceipt
    receipt_id: str
    def __init__(self, entity: _Optional[_Union[PortalLinkId, _Mapping]] = ..., email_receipt: _Optional[_Union[EmailReceipt, _Mapping]] = ..., receipt_id: _Optional[str] = ...) -> None: ...

class EmailReceipt(_message.Message):
    __slots__ = ()
    TO_ADDR_FIELD_NUMBER: _ClassVar[int]
    to_addr: str
    def __init__(self, to_addr: _Optional[str] = ...) -> None: ...

class DeliverReceiptRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
