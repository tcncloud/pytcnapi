from services.billing.entities.v1alpha3 import matching_pb2 as _matching_pb2
from services.billing.entities.v1alpha3 import modules_pb2 as _modules_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OmniSmsConfig(_message.Message):
    __slots__ = ()
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    prefixes: _matching_pb2.CountryCodePrefix
    config: _modules_pb2.BasicConfig
    def __init__(self, prefixes: _Optional[_Union[_matching_pb2.CountryCodePrefix, _Mapping]] = ..., config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...

class OmniSmsUnitConfig(_message.Message):
    __slots__ = ()
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    prefixes: _matching_pb2.CountryCodePrefix
    config: _modules_pb2.BasicUnitConfig
    def __init__(self, prefixes: _Optional[_Union[_matching_pb2.CountryCodePrefix, _Mapping]] = ..., config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ...) -> None: ...
