from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AgentSessionStatus(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[AgentSessionStatus.Enum]
        LOGGING_IN: _ClassVar[AgentSessionStatus.Enum]
        LOGGED_IN: _ClassVar[AgentSessionStatus.Enum]
        COMPLETED: _ClassVar[AgentSessionStatus.Enum]
        SUMMED: _ClassVar[AgentSessionStatus.Enum]
        ACCOUNTING_EXPORT: _ClassVar[AgentSessionStatus.Enum]
    UNKNOWN: AgentSessionStatus.Enum
    LOGGING_IN: AgentSessionStatus.Enum
    LOGGED_IN: AgentSessionStatus.Enum
    COMPLETED: AgentSessionStatus.Enum
    SUMMED: AgentSessionStatus.Enum
    ACCOUNTING_EXPORT: AgentSessionStatus.Enum
    def __init__(self) -> None: ...
