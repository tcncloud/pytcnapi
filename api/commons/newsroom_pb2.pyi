from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArticleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STATUS_DRAFT: _ClassVar[ArticleStatus]
    STATUS_PUBLISHED: _ClassVar[ArticleStatus]
    STATUS_ARCHIVED: _ClassVar[ArticleStatus]
STATUS_DRAFT: ArticleStatus
STATUS_PUBLISHED: ArticleStatus
STATUS_ARCHIVED: ArticleStatus
