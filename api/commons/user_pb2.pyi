from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UserArchivedStateFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    USER_ARCHIVED_STATE_FILTER_ALL: _ClassVar[UserArchivedStateFilter]
    USER_ARCHIVED_STATE_FILTER_ARCHIVED: _ClassVar[UserArchivedStateFilter]
    USER_ARCHIVED_STATE_FILTER_UNARCHIVED: _ClassVar[UserArchivedStateFilter]
USER_ARCHIVED_STATE_FILTER_ALL: UserArchivedStateFilter
USER_ARCHIVED_STATE_FILTER_ARCHIVED: UserArchivedStateFilter
USER_ARCHIVED_STATE_FILTER_UNARCHIVED: UserArchivedStateFilter
