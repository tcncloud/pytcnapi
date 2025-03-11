from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from services.billing.entities.v1alpha1 import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ("invoice_id", "billing_cycle", "create_time", "update_time", "delete_time", "items", "url", "client_id")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    billing_cycle: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    items: _containers.RepeatedCompositeFieldContainer[InvoiceItem]
    url: _wrappers_pb2.StringValue
    client_id: str
    def __init__(self, invoice_id: _Optional[str] = ..., billing_cycle: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., items: _Optional[_Iterable[_Union[InvoiceItem, _Mapping]]] = ..., url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., client_id: _Optional[str] = ...) -> None: ...

class InvoiceItem(_message.Message):
    __slots__ = ("invoice_item_id", "product", "price", "create_time", "update_time", "description", "date", "columns", "client_id")
    INVOICE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_item_id: str
    product: _product_pb2.Product
    price: float
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    date: _timestamp_pb2.Timestamp
    columns: _containers.RepeatedCompositeFieldContainer[InvoiceItemColumn]
    client_id: str
    def __init__(self, invoice_item_id: _Optional[str] = ..., product: _Optional[_Union[_product_pb2.Product, str]] = ..., price: _Optional[float] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[InvoiceItemColumn, _Mapping]]] = ..., client_id: _Optional[str] = ...) -> None: ...

class InvoiceItemColumn(_message.Message):
    __slots__ = ("name", "value", "column_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    column_value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ..., column_value: _Optional[str] = ...) -> None: ...
