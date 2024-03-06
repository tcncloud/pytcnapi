from annotations.perms import license_pb2 as _license_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultPermissionGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCOUNT_OWNER_GROUP: _ClassVar[DefaultPermissionGroup]
    SUPER_USER_GROUP: _ClassVar[DefaultPermissionGroup]
    USER_GROUP: _ClassVar[DefaultPermissionGroup]
    MONITOR_GROUP: _ClassVar[DefaultPermissionGroup]
    AGENT_GROUP: _ClassVar[DefaultPermissionGroup]
ACCOUNT_OWNER_GROUP: DefaultPermissionGroup
SUPER_USER_GROUP: DefaultPermissionGroup
USER_GROUP: DefaultPermissionGroup
MONITOR_GROUP: DefaultPermissionGroup
AGENT_GROUP: DefaultPermissionGroup
OPTIONS_FIELD_NUMBER: _ClassVar[int]
options: _descriptor.FieldDescriptor

class Tcn(_message.Message):
    __slots__ = ("wip", "app", "card", "features", "default_permission_groups", "blacklisted")
    WIP_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    wip: bool
    app: _license_pb2.Application
    card: _license_pb2.Card
    features: _containers.RepeatedScalarFieldContainer[str]
    default_permission_groups: _containers.RepeatedScalarFieldContainer[DefaultPermissionGroup]
    blacklisted: bool
    def __init__(self, wip: bool = ..., app: _Optional[_Union[_license_pb2.Application, str]] = ..., card: _Optional[_Union[_license_pb2.Card, str]] = ..., features: _Optional[_Iterable[str]] = ..., default_permission_groups: _Optional[_Iterable[_Union[DefaultPermissionGroup, str]]] = ..., blacklisted: bool = ...) -> None: ...
