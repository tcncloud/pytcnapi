from api.commons.org import permissions_pb2 as _permissions_pb2
from api.commons import perms_pb2 as _perms_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateP3PermissionGroupRequest(_message.Message):
    __slots__ = ("name", "description", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class CreateP3PermissionGroupResponse(_message.Message):
    __slots__ = ("p3_permission_group_id",)
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    def __init__(self, p3_permission_group_id: _Optional[str] = ...) -> None: ...

class UpdateP3PermissionGroupRequest(_message.Message):
    __slots__ = ("p3_permission_group_id", "p3_permission_group", "field_mask")
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, p3_permission_group_id: _Optional[str] = ..., p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateP3PermissionGroupResponse(_message.Message):
    __slots__ = ("p3_permission_group",)
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    def __init__(self, p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ...) -> None: ...

class UpdateP3PermissionGroupByOrgIdRequest(_message.Message):
    __slots__ = ("p3_permission_group_id", "org_id", "p3_permission_group", "field_mask")
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    org_id: str
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, p3_permission_group_id: _Optional[str] = ..., org_id: _Optional[str] = ..., p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateP3PermissionGroupByOrgIdResponse(_message.Message):
    __slots__ = ("p3_permission_group",)
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    def __init__(self, p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ...) -> None: ...

class DeleteP3PermissionGroupRequest(_message.Message):
    __slots__ = ("p3_permission_group_id",)
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    def __init__(self, p3_permission_group_id: _Optional[str] = ...) -> None: ...

class DeleteP3PermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignUsersP3PermissionGroupRequest(_message.Message):
    __slots__ = ("p3_permission_group_id", "user_ids")
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, p3_permission_group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignUsersP3PermissionGroupResponse(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeUsersP3PermissionGroupRequest(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeUsersP3PermissionGroupResponse(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListP3PermissionGroupsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListP3PermissionGroupsResponse(_message.Message):
    __slots__ = ("p3_permission_groups",)
    P3_PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    p3_permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.P3PermissionGroup]
    def __init__(self, p3_permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]]] = ...) -> None: ...
