from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFF: _ClassVar[Level]
    FATAL: _ClassVar[Level]
    PANIC: _ClassVar[Level]
    DPANIC: _ClassVar[Level]
    ERROR: _ClassVar[Level]
    WARN: _ClassVar[Level]
    INFO: _ClassVar[Level]
    DEBUG: _ClassVar[Level]
    TRACE: _ClassVar[Level]
OFF: Level
FATAL: Level
PANIC: Level
DPANIC: Level
ERROR: Level
WARN: Level
INFO: Level
DEBUG: Level
TRACE: Level
