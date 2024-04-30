from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons.org import labels_pb2 as _labels_pb2
from api.commons.org import permissions_pb2 as _permissions_pb2
from api.commons.org import user_pb2 as _user_pb2
from api.commons import perms_pb2 as _perms_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPermissionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPermissionsResponse(_message.Message):
    __slots__ = ("permissions", "p3_permissions", "user", "default_app")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    p3_permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    user: _user_pb2.User
    default_app: _org_pb2.OperatorApplications
    def __init__(self, permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., p3_permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ...) -> None: ...

class GetUserPermissionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserPermissionsResponse(_message.Message):
    __slots__ = ("permissions", "labels")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    def __init__(self, permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ...) -> None: ...

class CreatePermissionGroupRequest(_message.Message):
    __slots__ = ("name", "description", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class CreatePermissionGroupResponse(_message.Message):
    __slots__ = ("permission_group_id",)
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    def __init__(self, permission_group_id: _Optional[str] = ...) -> None: ...

class UpdatePermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "name", "description", "permissions")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, permission_group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class UpdatePermissionGroupResponse(_message.Message):
    __slots__ = ("permission_group",)
    PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    permission_group: _permissions_pb2.PermissionGroup
    def __init__(self, permission_group: _Optional[_Union[_permissions_pb2.PermissionGroup, _Mapping]] = ...) -> None: ...

class DeletePermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id",)
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    def __init__(self, permission_group_id: _Optional[str] = ...) -> None: ...

class DeletePermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionGroupsResponse(_message.Message):
    __slots__ = ("permission_groups",)
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    def __init__(self, permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ...) -> None: ...

class ListPermissionGroupsByOrgIdRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListPermissionGroupsByOrgIdResponse(_message.Message):
    __slots__ = ("permission_groups",)
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    def __init__(self, permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ...) -> None: ...

class AssignUsersPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "assign_user_ids")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    assign_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission_group_id: _Optional[str] = ..., assign_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignUsersPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeUsersPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "revoke_user_ids")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    revoke_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission_group_id: _Optional[str] = ..., revoke_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeUsersPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignAccountOwnerPermissionToUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AssignAccountOwnerPermissionToUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeAccountOwnerPermissionFromUserRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class RevokeAccountOwnerPermissionFromUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitDefaultPermissionGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitDefaultPermissionGroupsResponse(_message.Message):
    __slots__ = ("default_permission_groups",)
    DEFAULT_PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    default_permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    def __init__(self, default_permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ...) -> None: ...

class GetAccountOwnerGroupRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetAccountOwnerGroupResponse(_message.Message):
    __slots__ = ("permission_group",)
    PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    permission_group: _permissions_pb2.PermissionGroup
    def __init__(self, permission_group: _Optional[_Union[_permissions_pb2.PermissionGroup, _Mapping]] = ...) -> None: ...

class GetLicensesRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetLicensesResponse(_message.Message):
    __slots__ = ("licenses",)
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    licenses: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.License]
    def __init__(self, licenses: _Optional[_Iterable[_Union[_permissions_pb2.License, _Mapping]]] = ...) -> None: ...

class GetOrgLicensesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrgLicensesResponse(_message.Message):
    __slots__ = ("licenses",)
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    licenses: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.License]
    def __init__(self, licenses: _Optional[_Iterable[_Union[_permissions_pb2.License, _Mapping]]] = ...) -> None: ...

class UpdateLicensesRequest(_message.Message):
    __slots__ = ("org_id", "added_licenses", "revoked_licenses")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ADDED_LICENSES_FIELD_NUMBER: _ClassVar[int]
    REVOKED_LICENSES_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    added_licenses: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    revoked_licenses: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, org_id: _Optional[str] = ..., added_licenses: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., revoked_licenses: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class UpdateLicensesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemovePermissionFromAllPermissionGroupsRequest(_message.Message):
    __slots__ = ("org_id", "permission")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permission: _perms_pb2.Permission
    def __init__(self, org_id: _Optional[str] = ..., permission: _Optional[_Union[_perms_pb2.Permission, str]] = ...) -> None: ...

class RemovePermissionFromAllPermissionGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignLabelsRequest(_message.Message):
    __slots__ = ("label_ids", "permission_group_id")
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, label_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class AssignLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeLabelsRequest(_message.Message):
    __slots__ = ("label_ids", "permission_group_id")
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, label_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class RevokeLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
