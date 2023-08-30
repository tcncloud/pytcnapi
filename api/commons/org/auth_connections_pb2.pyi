from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONNECTION_TYPE_NONE: _ClassVar[ConnectionType]
    CONNECTION_TYPE_OIDC: _ClassVar[ConnectionType]
CONNECTION_TYPE_NONE: ConnectionType
CONNECTION_TYPE_OIDC: ConnectionType

class AuthConnectionSettings(_message.Message):
    __slots__ = ["issuer_url", "tenant_url", "client_id", "connection_id", "secret_expiration", "default_group", "custom_groups", "org_id", "name", "type"]
    class SecretExpiration(_message.Message):
        __slots__ = ["date"]
        DATE_FIELD_NUMBER: _ClassVar[int]
        date: _timestamp_pb2.Timestamp
        def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    TENANT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    issuer_url: str
    tenant_url: str
    client_id: str
    connection_id: str
    secret_expiration: AuthConnectionSettings.SecretExpiration
    default_group: GroupItem
    custom_groups: _containers.RepeatedCompositeFieldContainer[GroupItem]
    org_id: str
    name: str
    type: ConnectionType
    def __init__(self, issuer_url: _Optional[str] = ..., tenant_url: _Optional[str] = ..., client_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., secret_expiration: _Optional[_Union[AuthConnectionSettings.SecretExpiration, _Mapping]] = ..., default_group: _Optional[_Union[GroupItem, _Mapping]] = ..., custom_groups: _Optional[_Iterable[_Union[GroupItem, _Mapping]]] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[ConnectionType, str]] = ...) -> None: ...

class GroupItem(_message.Message):
    __slots__ = ["group_name", "hunt_group_sid", "agent_profile_group_id", "p3_permission_group_id", "permission_group_ids"]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    group_name: str
    hunt_group_sid: int
    agent_profile_group_id: str
    p3_permission_group_id: str
    permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_name: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., agent_profile_group_id: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., permission_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...
