from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNSPECIFIED: _ClassVar[Product]
    PRODUCT_OTHER: _ClassVar[Product]
    PRODUCT_AGENT_SEATS: _ClassVar[Product]
    PRODUCT_EMAILS_SENT: _ClassVar[Product]
    PRODUCT_EMAILS_RECEIVED: _ClassVar[Product]
    PRODUCT_SMS_SENT: _ClassVar[Product]
    PRODUCT_SMS_RECEIVED: _ClassVar[Product]
    PRODUCT_CHAT_SENT: _ClassVar[Product]
    PRODUCT_CHAT_RECEIVED: _ClassVar[Product]
    PRODUCT_OMNI: _ClassVar[Product]
    PRODUCT_VANA: _ClassVar[Product]
    PRODUCT_COMPLIANCE: _ClassVar[Product]

class InvoiceFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOICE_FORMAT_UNSPECIFIED: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_PROTO: _ClassVar[InvoiceFormat]
    INVOICE_FORMAT_CSV: _ClassVar[InvoiceFormat]
PRODUCT_UNSPECIFIED: Product
PRODUCT_OTHER: Product
PRODUCT_AGENT_SEATS: Product
PRODUCT_EMAILS_SENT: Product
PRODUCT_EMAILS_RECEIVED: Product
PRODUCT_SMS_SENT: Product
PRODUCT_SMS_RECEIVED: Product
PRODUCT_CHAT_SENT: Product
PRODUCT_CHAT_RECEIVED: Product
PRODUCT_OMNI: Product
PRODUCT_VANA: Product
PRODUCT_COMPLIANCE: Product
INVOICE_FORMAT_UNSPECIFIED: InvoiceFormat
INVOICE_FORMAT_PROTO: InvoiceFormat
INVOICE_FORMAT_CSV: InvoiceFormat

class Invoice(_message.Message):
    __slots__ = ("items", "invoice_id", "billing_cycle", "create_time", "update_time")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[InvoiceItem]
    invoice_id: int
    billing_cycle: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, items: _Optional[_Iterable[_Union[InvoiceItem, _Mapping]]] = ..., invoice_id: _Optional[int] = ..., billing_cycle: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class InvoiceItem(_message.Message):
    __slots__ = ("invoice_item_sid", "product", "amount", "date_created", "date_modified", "invoice_id")
    INVOICE_ITEM_SID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_item_sid: int
    product: Product
    amount: float
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    invoice_id: int
    def __init__(self, invoice_item_sid: _Optional[int] = ..., product: _Optional[_Union[Product, str]] = ..., amount: _Optional[float] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., invoice_id: _Optional[int] = ...) -> None: ...
