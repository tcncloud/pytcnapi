from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MatchingRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MATCHING_RULE_UNSPECIFIED: _ClassVar[MatchingRule]
MATCHING_RULE_UNSPECIFIED: MatchingRule

class MatchingConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
