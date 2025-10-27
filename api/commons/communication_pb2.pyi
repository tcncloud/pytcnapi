from api.commons import acd_pb2 as _acd_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommType(_message.Message):
    __slots__ = ()
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SMS_TYPE_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_type: _acd_pb2.CallType.Enum
    email_type: EmailType.Enum
    sms_type: SmsType.Enum
    whatsapp_type: WhatsAppType.Enum
    def __init__(self, call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., email_type: _Optional[_Union[EmailType.Enum, str]] = ..., sms_type: _Optional[_Union[SmsType.Enum, str]] = ..., whatsapp_type: _Optional[_Union[WhatsAppType.Enum, str]] = ...) -> None: ...

class EmailType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTBOUND: _ClassVar[EmailType.Enum]
    OUTBOUND: EmailType.Enum
    def __init__(self) -> None: ...

class SmsType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTBOUND: _ClassVar[SmsType.Enum]
    OUTBOUND: SmsType.Enum
    def __init__(self) -> None: ...

class WhatsAppType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTBOUND: _ClassVar[WhatsAppType.Enum]
    OUTBOUND: WhatsAppType.Enum
    def __init__(self) -> None: ...
