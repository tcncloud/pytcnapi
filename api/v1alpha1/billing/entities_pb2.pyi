from annotations import authz_pb2 as _authz_pb2
from api.commons.billing import detail_pb2 as _detail_pb2
from api.commons.billing import invoice_pb2 as _invoice_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvoiceFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INVOICE_FORMAT_UNSPECIFIED: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_PROTO: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_CSV: _ClassVar[InvoiceFormat]
INVOICE_FORMAT_UNSPECIFIED: InvoiceFormat
INVOICE_FORMAT_PROTO: InvoiceFormat
INVOICE_FORMAT_CSV: InvoiceFormat

class GetBillingPlanReq(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetBillingPlanRes(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _detail_pb2.Plan
    def __init__(self, billing_plan: _Optional[_Union[_detail_pb2.Plan, _Mapping]] = ...) -> None: ...

class UpdateBillingPlanReq(_message.Message):
    __slots__ = ["billing_details", "org_id"]
    BILLING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    billing_details: _containers.RepeatedCompositeFieldContainer[_detail_pb2.Detail]
    org_id: str
    def __init__(self, billing_details: _Optional[_Iterable[_Union[_detail_pb2.Detail, _Mapping]]] = ..., org_id: _Optional[str] = ...) -> None: ...

class UpdateBillingPlanRes(_message.Message):
    __slots__ = ["billing_plan"]
    BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    billing_plan: _detail_pb2.Plan
    def __init__(self, billing_plan: _Optional[_Union[_detail_pb2.Plan, _Mapping]] = ...) -> None: ...

class GetInvoiceReq(_message.Message):
    __slots__ = ["invoice_date", "org_id", "format"]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    invoice_date: _timestamp_pb2.Timestamp
    org_id: str
    format: InvoiceFormat
    def __init__(self, invoice_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., org_id: _Optional[str] = ..., format: _Optional[_Union[InvoiceFormat, str]] = ...) -> None: ...

class GetInvoiceRes(_message.Message):
    __slots__ = ["invoice", "proto", "csv_url"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PROTO_FIELD_NUMBER: _ClassVar[int]
    CSV_URL_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    proto: _invoice_pb2.Invoice
    csv_url: str
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., proto: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., csv_url: _Optional[str] = ...) -> None: ...

class ExportGeneratedInvoiceReq(_message.Message):
    __slots__ = ["invoice_date", "org_id", "format"]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    invoice_date: _timestamp_pb2.Timestamp
    org_id: str
    format: InvoiceFormat
    def __init__(self, invoice_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., org_id: _Optional[str] = ..., format: _Optional[_Union[InvoiceFormat, str]] = ...) -> None: ...

class ExportGeneratedInvoiceRes(_message.Message):
    __slots__ = ["proto", "csv_url"]
    PROTO_FIELD_NUMBER: _ClassVar[int]
    CSV_URL_FIELD_NUMBER: _ClassVar[int]
    proto: _invoice_pb2.Invoice
    csv_url: str
    def __init__(self, proto: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., csv_url: _Optional[str] = ...) -> None: ...
