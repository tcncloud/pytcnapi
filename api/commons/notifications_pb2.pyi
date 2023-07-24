from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FieldValueFilter(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class NotificationType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INVALID: _ClassVar[NotificationType.Enum]
        EMAIL: _ClassVar[NotificationType.Enum]
        SERVER_PUSH: _ClassVar[NotificationType.Enum]
        IOS: _ClassVar[NotificationType.Enum]
        ANDROID: _ClassVar[NotificationType.Enum]
        SMS: _ClassVar[NotificationType.Enum]
    INVALID: NotificationType.Enum
    EMAIL: NotificationType.Enum
    SERVER_PUSH: NotificationType.Enum
    IOS: NotificationType.Enum
    ANDROID: NotificationType.Enum
    SMS: NotificationType.Enum
    def __init__(self) -> None: ...
