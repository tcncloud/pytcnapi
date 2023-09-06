from data.billing.v1alpha1 import products_pb2 as _products_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ["invoice_id", "org_id", "billing_cycle", "create_time", "update_time", "items", "url"]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    org_id: str
    billing_cycle: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    items: _containers.RepeatedCompositeFieldContainer[InvoiceItem]
    url: str
    def __init__(self, invoice_id: _Optional[str] = ..., org_id: _Optional[str] = ..., billing_cycle: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., items: _Optional[_Iterable[_Union[InvoiceItem, _Mapping]]] = ..., url: _Optional[str] = ...) -> None: ...

class InvoiceItem(_message.Message):
    __slots__ = ["invoice_item_id", "invoice_id", "product", "price", "create_time", "update_time"]
    INVOICE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    invoice_item_id: str
    invoice_id: str
    product: _products_pb2.Product
    price: float
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, invoice_item_id: _Optional[str] = ..., invoice_id: _Optional[str] = ..., product: _Optional[_Union[_products_pb2.Product, str]] = ..., price: _Optional[float] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
