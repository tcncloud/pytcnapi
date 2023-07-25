from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ManualDialGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MDG_UNKNOWN: _ClassVar[ManualDialGroupStatus]
    MDG_PREPARE: _ClassVar[ManualDialGroupStatus]
    MDG_SCHEDULED: _ClassVar[ManualDialGroupStatus]
    MDG_RUNNING: _ClassVar[ManualDialGroupStatus]
    MDG_COMPLETED: _ClassVar[ManualDialGroupStatus]
    MDG_CANCELLED_TIMEOUT: _ClassVar[ManualDialGroupStatus]
    MDG_CANCELLED_USER: _ClassVar[ManualDialGroupStatus]
    MDG_CANCELLED_ADMIN: _ClassVar[ManualDialGroupStatus]
    MDG_SUMMED_COMPLETED: _ClassVar[ManualDialGroupStatus]
    MDG_SUMMED_CANCELLED_TIMEOUT: _ClassVar[ManualDialGroupStatus]
    MDG_SUMMED_CANCELLED_USER: _ClassVar[ManualDialGroupStatus]
    MDG_SUMMED_CANCELLED_ADMIN: _ClassVar[ManualDialGroupStatus]
    MDG_ACCOUNTINGEXPORT_COMPLETED: _ClassVar[ManualDialGroupStatus]
    MDG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: _ClassVar[ManualDialGroupStatus]
    MDG_ACCOUNTINGEXPORT_CANCELLED_USER: _ClassVar[ManualDialGroupStatus]
    MDG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: _ClassVar[ManualDialGroupStatus]
MDG_UNKNOWN: ManualDialGroupStatus
MDG_PREPARE: ManualDialGroupStatus
MDG_SCHEDULED: ManualDialGroupStatus
MDG_RUNNING: ManualDialGroupStatus
MDG_COMPLETED: ManualDialGroupStatus
MDG_CANCELLED_TIMEOUT: ManualDialGroupStatus
MDG_CANCELLED_USER: ManualDialGroupStatus
MDG_CANCELLED_ADMIN: ManualDialGroupStatus
MDG_SUMMED_COMPLETED: ManualDialGroupStatus
MDG_SUMMED_CANCELLED_TIMEOUT: ManualDialGroupStatus
MDG_SUMMED_CANCELLED_USER: ManualDialGroupStatus
MDG_SUMMED_CANCELLED_ADMIN: ManualDialGroupStatus
MDG_ACCOUNTINGEXPORT_COMPLETED: ManualDialGroupStatus
MDG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: ManualDialGroupStatus
MDG_ACCOUNTINGEXPORT_CANCELLED_USER: ManualDialGroupStatus
MDG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: ManualDialGroupStatus
