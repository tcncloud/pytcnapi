from api.commons.auth import perms_pb2 as _perms_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
AUTHZ_FIELD_NUMBER: _ClassVar[int]
authz: _descriptor.FieldDescriptor

class Permissions(_message.Message):
    __slots__ = ("sets", "wip", "no_permissions")
    SETS_FIELD_NUMBER: _ClassVar[int]
    WIP_FIELD_NUMBER: _ClassVar[int]
    NO_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    sets: _containers.RepeatedCompositeFieldContainer[PermissionSet]
    wip: bool
    no_permissions: bool
    def __init__(self, sets: _Optional[_Iterable[_Union[PermissionSet, _Mapping]]] = ..., wip: bool = ..., no_permissions: bool = ...) -> None: ...

class PermissionSet(_message.Message):
    __slots__ = ("permissions", "taint")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TAINT_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    taint: Taint
    def __init__(self, permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., taint: _Optional[_Union[Taint, _Mapping]] = ...) -> None: ...

class Taint(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: int
    def __init__(self, id: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
