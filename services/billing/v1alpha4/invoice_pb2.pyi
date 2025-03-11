from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha4 import invoice_pb2 as _invoice_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_FORMAT_UNSPECIFIED: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_CSV: _ClassVar[InvoiceFormat]
INVOICE_FORMAT_UNSPECIFIED: InvoiceFormat
INVOICE_FORMAT_CSV: InvoiceFormat

class ExportInvoiceRequest(_message.Message):
    __slots__ = ("format", "invoice_date")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    format: InvoiceFormat
    invoice_date: _timestamp_pb2.Timestamp
    def __init__(self, format: _Optional[_Union[InvoiceFormat, str]] = ..., invoice_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportInvoiceResponse(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...
