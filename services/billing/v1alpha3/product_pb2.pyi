from services.billing.entities.v1alpha3 import rates_pb2 as _rates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProductsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProductsResponse(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[_rates_pb2.Product]
    def __init__(self, products: _Optional[_Iterable[_Union[_rates_pb2.Product, _Mapping]]] = ...) -> None: ...
