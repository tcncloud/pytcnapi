import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import decimal_pb2 as _decimal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ()
    BILLING_CYCLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    billing_cycle: str
    create_time: _timestamp_pb2.Timestamp
    rows: _containers.RepeatedCompositeFieldContainer[InvoiceRow]
    download_url: _wrappers_pb2.StringValue
    def __init__(self, billing_cycle: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[InvoiceRow, _Mapping]]] = ..., download_url: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class InvoiceRow(_message.Message):
    __slots__ = ()
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    RATED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    product_id: str
    description: str
    date: _timestamp_pb2.Timestamp
    columns: _containers.RepeatedCompositeFieldContainer[InvoiceColumn]
    rated_amount: _decimal_pb2.Decimal
    def __init__(self, client_id: _Optional[str] = ..., product_id: _Optional[str] = ..., description: _Optional[str] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[InvoiceColumn, _Mapping]]] = ..., rated_amount: _Optional[_Union[_decimal_pb2.Decimal, _Mapping]] = ...) -> None: ...

class InvoiceColumn(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
