from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BroadcastType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNKNOWN: _ClassVar[BroadcastType]
    TYPE_OUTBOUND: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_PREVIEW_ONLY: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_MAC_ONLY: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_RINGLESS_VOICEMAIL: _ClassVar[BroadcastType]
    TYPE_INBOUND: _ClassVar[BroadcastType]
    TYPE_MANUAL: _ClassVar[BroadcastType]
    TYPE_SMS: _ClassVar[BroadcastType]
    TYPE_EMAIL: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_INBOUND: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_MANUAL: _ClassVar[BroadcastType]
    TYPE_INBOUND_MANUAL: _ClassVar[BroadcastType]
    TYPE_OUTBOUND_INBOUND_MANUAL: _ClassVar[BroadcastType]
TYPE_UNKNOWN: BroadcastType
TYPE_OUTBOUND: BroadcastType
TYPE_OUTBOUND_PREVIEW_ONLY: BroadcastType
TYPE_OUTBOUND_MAC_ONLY: BroadcastType
TYPE_OUTBOUND_RINGLESS_VOICEMAIL: BroadcastType
TYPE_INBOUND: BroadcastType
TYPE_MANUAL: BroadcastType
TYPE_SMS: BroadcastType
TYPE_EMAIL: BroadcastType
TYPE_OUTBOUND_INBOUND: BroadcastType
TYPE_OUTBOUND_MANUAL: BroadcastType
TYPE_INBOUND_MANUAL: BroadcastType
TYPE_OUTBOUND_INBOUND_MANUAL: BroadcastType

class TemplateType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TemplateType.Enum]
        STANDARD: _ClassVar[TemplateType.Enum]
        LAYERED: _ClassVar[TemplateType.Enum]
        INBOUND: _ClassVar[TemplateType.Enum]
        MAC_ONLY: _ClassVar[TemplateType.Enum]
        PREVIEW_ONLY: _ClassVar[TemplateType.Enum]
        RINGLESS_VOICEMAIL: _ClassVar[TemplateType.Enum]
    UNKNOWN: TemplateType.Enum
    STANDARD: TemplateType.Enum
    LAYERED: TemplateType.Enum
    INBOUND: TemplateType.Enum
    MAC_ONLY: TemplateType.Enum
    PREVIEW_ONLY: TemplateType.Enum
    RINGLESS_VOICEMAIL: TemplateType.Enum
    def __init__(self) -> None: ...
