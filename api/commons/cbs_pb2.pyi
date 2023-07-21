from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduledCallbackStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SCS_INVALID: _ClassVar[ScheduledCallbackStatus]
    SCS_OPENED: _ClassVar[ScheduledCallbackStatus]
    SCS_CANCELED: _ClassVar[ScheduledCallbackStatus]
    SCS_CLOSED: _ClassVar[ScheduledCallbackStatus]
    SCS_READY: _ClassVar[ScheduledCallbackStatus]
SCS_INVALID: ScheduledCallbackStatus
SCS_OPENED: ScheduledCallbackStatus
SCS_CANCELED: ScheduledCallbackStatus
SCS_CLOSED: ScheduledCallbackStatus
SCS_READY: ScheduledCallbackStatus
