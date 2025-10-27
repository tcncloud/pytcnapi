import datetime

from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import invoice_pb2 as _invoice_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_FORMAT_UNSPECIFIED: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_CSV: _ClassVar[InvoiceFormat]
INVOICE_FORMAT_UNSPECIFIED: InvoiceFormat
INVOICE_FORMAT_CSV: InvoiceFormat

class CreateInvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice_id: _Optional[str] = ..., invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CreateInvoiceResponse(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DeleteInvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DeleteInvoiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportInvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    format: InvoiceFormat
    invoice_date: _timestamp_pb2.Timestamp
    def __init__(self, invoice_id: _Optional[str] = ..., format: _Optional[_Union[InvoiceFormat, str]] = ..., invoice_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportInvoiceResponse(_message.Message):
    __slots__ = ()
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class GetInvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class GetInvoiceResponse(_message.Message):
    __slots__ = ()
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, invoice_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ()
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[_invoice_pb2.Invoice]
    token: str
    def __init__(self, invoices: _Optional[_Iterable[_Union[_invoice_pb2.Invoice, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateInvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    invoice: _invoice_pb2.Invoice
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, invoice_id: _Optional[str] = ..., invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInvoiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
