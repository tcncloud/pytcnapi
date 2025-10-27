from annotations.perms import license_pb2 as _license_pb2
from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons import perms_pb2 as _perms_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionGroup(_message.Message):
    __slots__ = ()
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    org_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    read_only: bool
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission_group_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., read_only: _Optional[bool] = ..., label_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class P3PermissionGroup(_message.Message):
    __slots__ = ()
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group_id: str
    org_id: str
    region_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    def __init__(self, p3_permission_group_id: _Optional[str] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ...) -> None: ...

class License(_message.Message):
    __slots__ = ()
    class Card(_message.Message):
        __slots__ = ()
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        type: _license_pb2.Card
        permissions: _containers.RepeatedCompositeFieldContainer[License.Permission]
        name: str
        def __init__(self, type: _Optional[_Union[_license_pb2.Card, str]] = ..., permissions: _Optional[_Iterable[_Union[License.Permission, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...
    class Permission(_message.Message):
        __slots__ = ()
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        permission: _perms_pb2.Permission
        enabled: bool
        features: _containers.RepeatedScalarFieldContainer[str]
        name: str
        def __init__(self, permission: _Optional[_Union[_perms_pb2.Permission, str]] = ..., enabled: _Optional[bool] = ..., features: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ...) -> None: ...
    APP_FIELD_NUMBER: _ClassVar[int]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    app: _license_pb2.Application
    cards: _containers.RepeatedCompositeFieldContainer[License.Card]
    name: str
    def __init__(self, app: _Optional[_Union[_license_pb2.Application, str]] = ..., cards: _Optional[_Iterable[_Union[License.Card, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...
