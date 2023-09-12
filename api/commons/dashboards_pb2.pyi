from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DashboardPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DASHBOARD_PERMISSION_TYPE_ORG_CUSTOM: _ClassVar[DashboardPermissionType]
    DASHBOARD_PERMISSION_TYPE_TCN_STANDARD: _ClassVar[DashboardPermissionType]
DASHBOARD_PERMISSION_TYPE_ORG_CUSTOM: DashboardPermissionType
DASHBOARD_PERMISSION_TYPE_TCN_STANDARD: DashboardPermissionType
