from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CountryCodePrefix(_message.Message):
    __slots__ = ("country_code", "prefixes", "matching_rule_id", "name")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    country_code: int
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    matching_rule_id: str
    name: str
    def __init__(self, country_code: _Optional[int] = ..., prefixes: _Optional[_Iterable[str]] = ..., matching_rule_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
