from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNSPECIFIED: _ClassVar[Product]
    PRODUCT_OMNI: _ClassVar[Product]
    PRODUCT_OMNI_SEATS: _ClassVar[Product]
    PRODUCT_OMNI_CHAT_SENT: _ClassVar[Product]
    PRODUCT_OMNI_CHAT_RECEIVED: _ClassVar[Product]
    PRODUCT_OMNI_EMAILS_SENT: _ClassVar[Product]
    PRODUCT_OMNI_EMAILS_RECEIVED: _ClassVar[Product]
    PRODUCT_OMNI_SMS_SENT: _ClassVar[Product]
    PRODUCT_OMNI_SMS_RECEIVED: _ClassVar[Product]
    PRODUCT_COMPLIANCE: _ClassVar[Product]
PRODUCT_UNSPECIFIED: Product
PRODUCT_OMNI: Product
PRODUCT_OMNI_SEATS: Product
PRODUCT_OMNI_CHAT_SENT: Product
PRODUCT_OMNI_CHAT_RECEIVED: Product
PRODUCT_OMNI_EMAILS_SENT: Product
PRODUCT_OMNI_EMAILS_RECEIVED: Product
PRODUCT_OMNI_SMS_SENT: Product
PRODUCT_OMNI_SMS_RECEIVED: Product
PRODUCT_COMPLIANCE: Product

class Invoice(_message.Message):
    __slots__ = ("billing_cycle", "create_time", "items", "download_url")
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    billing_cycle: str
    create_time: _timestamp_pb2.Timestamp
    items: _containers.RepeatedCompositeFieldContainer[InvoiceItem]
    download_url: _wrappers_pb2.StringValue
    def __init__(self, billing_cycle: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., items: _Optional[_Iterable[_Union[InvoiceItem, _Mapping]]] = ..., download_url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class InvoiceItem(_message.Message):
    __slots__ = ("client_id", "product", "description", "date", "price", "columns")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    product: Product
    description: str
    date: _timestamp_pb2.Timestamp
    price: float
    columns: _containers.RepeatedCompositeFieldContainer[InvoiceItemColumn]
    def __init__(self, client_id: _Optional[str] = ..., product: _Optional[_Union[Product, str]] = ..., description: _Optional[str] = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price: _Optional[float] = ..., columns: _Optional[_Iterable[_Union[InvoiceItemColumn, _Mapping]]] = ...) -> None: ...

class InvoiceItemColumn(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
