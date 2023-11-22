from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchingRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MATCHING_RULE_UNSPECIFIED: _ClassVar[MatchingRule]
    MATCHING_RULE_AREA_CODE: _ClassVar[MatchingRule]
MATCHING_RULE_UNSPECIFIED: MatchingRule
MATCHING_RULE_AREA_CODE: MatchingRule

class MatchingConfig(_message.Message):
    __slots__ = ("area_code",)
    AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    area_code: MatchingConfigAreaCode
    def __init__(self, area_code: _Optional[_Union[MatchingConfigAreaCode, _Mapping]] = ...) -> None: ...

class MatchingConfigAreaCode(_message.Message):
    __slots__ = ("name", "area_codes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AREA_CODES_FIELD_NUMBER: _ClassVar[int]
    name: str
    area_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., area_codes: _Optional[_Iterable[str]] = ...) -> None: ...
