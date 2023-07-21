from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class InboundGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IBG_UNKNOWN: _ClassVar[InboundGroupStatus]
    IBG_PREPARE: _ClassVar[InboundGroupStatus]
    IBG_SCHEDULED: _ClassVar[InboundGroupStatus]
    IBG_RUNNING: _ClassVar[InboundGroupStatus]
    IBG_PAUSED: _ClassVar[InboundGroupStatus]
    IBG_COMPLETED: _ClassVar[InboundGroupStatus]
    IBG_CANCELLED_TIMEOUT: _ClassVar[InboundGroupStatus]
    IBG_CANCELLED_USER: _ClassVar[InboundGroupStatus]
    IBG_CANCELLED_ADMIN: _ClassVar[InboundGroupStatus]
    IBG_SUMMED_COMPLETED: _ClassVar[InboundGroupStatus]
    IBG_SUMMED_CANCELLED_TIMEOUT: _ClassVar[InboundGroupStatus]
    IBG_SUMMED_CANCELLED_USER: _ClassVar[InboundGroupStatus]
    IBG_SUMMED_CANCELLED_ADMIN: _ClassVar[InboundGroupStatus]
    IBG_ACCOUNTINGEXPORT_COMPLETED: _ClassVar[InboundGroupStatus]
    IBG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: _ClassVar[InboundGroupStatus]
    IBG_ACCOUNTINGEXPORT_CANCELLED_USER: _ClassVar[InboundGroupStatus]
    IBG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: _ClassVar[InboundGroupStatus]
IBG_UNKNOWN: InboundGroupStatus
IBG_PREPARE: InboundGroupStatus
IBG_SCHEDULED: InboundGroupStatus
IBG_RUNNING: InboundGroupStatus
IBG_PAUSED: InboundGroupStatus
IBG_COMPLETED: InboundGroupStatus
IBG_CANCELLED_TIMEOUT: InboundGroupStatus
IBG_CANCELLED_USER: InboundGroupStatus
IBG_CANCELLED_ADMIN: InboundGroupStatus
IBG_SUMMED_COMPLETED: InboundGroupStatus
IBG_SUMMED_CANCELLED_TIMEOUT: InboundGroupStatus
IBG_SUMMED_CANCELLED_USER: InboundGroupStatus
IBG_SUMMED_CANCELLED_ADMIN: InboundGroupStatus
IBG_ACCOUNTINGEXPORT_COMPLETED: InboundGroupStatus
IBG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: InboundGroupStatus
IBG_ACCOUNTINGEXPORT_CANCELLED_USER: InboundGroupStatus
IBG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: InboundGroupStatus
