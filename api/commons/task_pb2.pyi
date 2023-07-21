from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TASK_UNKNOWN: _ClassVar[TaskStatus]
    TASK_SCHEDULED: _ClassVar[TaskStatus]
    TASK_WAITING: _ClassVar[TaskStatus]
    TASK_PREPARING: _ClassVar[TaskStatus]
    TASK_RUNNING: _ClassVar[TaskStatus]
    TASK_COMPLETED: _ClassVar[TaskStatus]
    TASK_CANCELLED_TIMEOUT: _ClassVar[TaskStatus]
    TASK_CANCELLED_USER: _ClassVar[TaskStatus]
    TASK_CANCELLED_ADMIN: _ClassVar[TaskStatus]
TASK_UNKNOWN: TaskStatus
TASK_SCHEDULED: TaskStatus
TASK_WAITING: TaskStatus
TASK_PREPARING: TaskStatus
TASK_RUNNING: TaskStatus
TASK_COMPLETED: TaskStatus
TASK_CANCELLED_TIMEOUT: TaskStatus
TASK_CANCELLED_USER: TaskStatus
TASK_CANCELLED_ADMIN: TaskStatus
