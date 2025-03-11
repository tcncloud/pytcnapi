from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchingRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCHING_RULE_UNSPECIFIED: _ClassVar[MatchingRule]
    MATCHING_RULE_AREA_CODE: _ClassVar[MatchingRule]
    MATCHING_RULE_COUNTRY_PREFIX: _ClassVar[MatchingRule]
MATCHING_RULE_UNSPECIFIED: MatchingRule
MATCHING_RULE_AREA_CODE: MatchingRule
MATCHING_RULE_COUNTRY_PREFIX: MatchingRule

class MatchingConfig(_message.Message):
    __slots__ = ("name", "area_code", "country_prefix")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    name: str
    area_code: MatchingConfigAreaCode
    country_prefix: MatchingConfigCountryPrefix
    def __init__(self, name: _Optional[str] = ..., area_code: _Optional[_Union[MatchingConfigAreaCode, _Mapping]] = ..., country_prefix: _Optional[_Union[MatchingConfigCountryPrefix, _Mapping]] = ...) -> None: ...

class MatchingConfigAreaCode(_message.Message):
    __slots__ = ("name", "area_codes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AREA_CODES_FIELD_NUMBER: _ClassVar[int]
    name: str
    area_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., area_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class MatchingConfigCountryPrefix(_message.Message):
    __slots__ = ("country_code", "prefixes")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    country_code: int
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, country_code: _Optional[int] = ..., prefixes: _Optional[_Iterable[str]] = ...) -> None: ...
