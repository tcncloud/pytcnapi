from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class InsightPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSIGHT_PERMISSION_TYPE_COMMON_LIBRARY: _ClassVar[InsightPermissionType]
    INSIGHT_PERMISSION_TYPE_ORG: _ClassVar[InsightPermissionType]

class InsightType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSIGHT_TYPE_TABLE_VIEW: _ClassVar[InsightType]

class InsightVfsSchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSIGHT_VFS_SCHEMA_TYPE_STRING: _ClassVar[InsightVfsSchemaType]
    INSIGHT_VFS_SCHEMA_TYPE_INT64: _ClassVar[InsightVfsSchemaType]
    INSIGHT_VFS_SCHEMA_TYPE_FLOAT64: _ClassVar[InsightVfsSchemaType]
    INSIGHT_VFS_SCHEMA_TYPE_BOOLEAN: _ClassVar[InsightVfsSchemaType]
    INSIGHT_VFS_SCHEMA_TYPE_DATETIME: _ClassVar[InsightVfsSchemaType]
INSIGHT_PERMISSION_TYPE_COMMON_LIBRARY: InsightPermissionType
INSIGHT_PERMISSION_TYPE_ORG: InsightPermissionType
INSIGHT_TYPE_TABLE_VIEW: InsightType
INSIGHT_VFS_SCHEMA_TYPE_STRING: InsightVfsSchemaType
INSIGHT_VFS_SCHEMA_TYPE_INT64: InsightVfsSchemaType
INSIGHT_VFS_SCHEMA_TYPE_FLOAT64: InsightVfsSchemaType
INSIGHT_VFS_SCHEMA_TYPE_BOOLEAN: InsightVfsSchemaType
INSIGHT_VFS_SCHEMA_TYPE_DATETIME: InsightVfsSchemaType
