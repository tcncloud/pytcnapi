from data.billing.v1alpha1 import invoices_pb2 as _invoices_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateInvoiceRequest(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CreateInvoiceResponse(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ...) -> None: ...

class DeleteInvoiceRequest(_message.Message):
    __slots__ = ["invoice_id"]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DeleteInvoiceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInvoiceRequest(_message.Message):
    __slots__ = ["invoice_id"]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class GetInvoiceResponse(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ["invoice", "selector_fields", "return_fields", "order_by"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELDS_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    selector_fields: _field_mask_pb2.FieldMask
    return_fields: _field_mask_pb2.FieldMask
    order_by: _core_pb2.OrderBy
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ..., selector_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., return_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order_by: _Optional[_Union[_core_pb2.OrderBy, _Mapping]] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ["invoices"]
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_invoices_pb2.Invoice]
    def __init__(self, invoices: _Optional[_Iterable[_Union[_invoices_pb2.Invoice, _Mapping]]] = ...) -> None: ...

class UpdateInvoiceRequest(_message.Message):
    __slots__ = ["invoice", "update_fields"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInvoiceResponse(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoices_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoices_pb2.Invoice, _Mapping]] = ...) -> None: ...
