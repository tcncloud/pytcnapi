from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TaskGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TG_UNKNOWN: _ClassVar[TaskGroupStatus]
    TG_PREPARE: _ClassVar[TaskGroupStatus]
    TG_SCHEDULED: _ClassVar[TaskGroupStatus]
    TG_SCHEDULED_LINKING: _ClassVar[TaskGroupStatus]
    TG_SCHEDULED_PAUSED: _ClassVar[TaskGroupStatus]
    TG_RUNNING: _ClassVar[TaskGroupStatus]
    TG_PAUSED: _ClassVar[TaskGroupStatus]
    TG_WAITING: _ClassVar[TaskGroupStatus]
    TG_COMPLETED: _ClassVar[TaskGroupStatus]
    TG_CANCELLED_TIMEOUT: _ClassVar[TaskGroupStatus]
    TG_CANCELLED_USER: _ClassVar[TaskGroupStatus]
    TG_CANCELLED_ADMIN: _ClassVar[TaskGroupStatus]
    TG_SUMMED_COMPLETED: _ClassVar[TaskGroupStatus]
    TG_SUMMED_CANCELLED_TIMEOUT: _ClassVar[TaskGroupStatus]
    TG_SUMMED_CANCELLED_USER: _ClassVar[TaskGroupStatus]
    TG_SUMMED_CANCELLED_ADMIN: _ClassVar[TaskGroupStatus]
    TG_ACCOUNTINGEXPORT_COMPLETED: _ClassVar[TaskGroupStatus]
    TG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: _ClassVar[TaskGroupStatus]
    TG_ACCOUNTINGEXPORT_CANCELLED_USER: _ClassVar[TaskGroupStatus]
    TG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: _ClassVar[TaskGroupStatus]
TG_UNKNOWN: TaskGroupStatus
TG_PREPARE: TaskGroupStatus
TG_SCHEDULED: TaskGroupStatus
TG_SCHEDULED_LINKING: TaskGroupStatus
TG_SCHEDULED_PAUSED: TaskGroupStatus
TG_RUNNING: TaskGroupStatus
TG_PAUSED: TaskGroupStatus
TG_WAITING: TaskGroupStatus
TG_COMPLETED: TaskGroupStatus
TG_CANCELLED_TIMEOUT: TaskGroupStatus
TG_CANCELLED_USER: TaskGroupStatus
TG_CANCELLED_ADMIN: TaskGroupStatus
TG_SUMMED_COMPLETED: TaskGroupStatus
TG_SUMMED_CANCELLED_TIMEOUT: TaskGroupStatus
TG_SUMMED_CANCELLED_USER: TaskGroupStatus
TG_SUMMED_CANCELLED_ADMIN: TaskGroupStatus
TG_ACCOUNTINGEXPORT_COMPLETED: TaskGroupStatus
TG_ACCOUNTINGEXPORT_CANCELLED_TIMEOUT: TaskGroupStatus
TG_ACCOUNTINGEXPORT_CANCELLED_USER: TaskGroupStatus
TG_ACCOUNTINGEXPORT_CANCELLED_ADMIN: TaskGroupStatus
