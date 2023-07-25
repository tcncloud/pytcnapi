from api.commons.org import auth_connections_pb2 as _auth_connections_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAuthConnectionRequest(_message.Message):
    __slots__ = ["settings", "client_secret"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    settings: _auth_connections_pb2.AuthConnectionSettings
    client_secret: str
    def __init__(self, settings: _Optional[_Union[_auth_connections_pb2.AuthConnectionSettings, _Mapping]] = ..., client_secret: _Optional[str] = ...) -> None: ...

class CreateAuthConnectionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAuthConnectionSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAuthConnectionSettingsResponse(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _auth_connections_pb2.AuthConnectionSettings
    def __init__(self, settings: _Optional[_Union[_auth_connections_pb2.AuthConnectionSettings, _Mapping]] = ...) -> None: ...

class DeleteAuthConnectionRequest(_message.Message):
    __slots__ = ["connection_id"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class DeleteAuthConnectionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAuthConnectionSecretRequest(_message.Message):
    __slots__ = ["connection_id", "client_secret"]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    client_secret: str
    def __init__(self, connection_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class UpdateAuthConnectionSecretResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAuthConnectionGroupsRequest(_message.Message):
    __slots__ = ["default_group", "custom_groups"]
    DEFAULT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GROUPS_FIELD_NUMBER: _ClassVar[int]
    default_group: _auth_connections_pb2.GroupItem
    custom_groups: _containers.RepeatedCompositeFieldContainer[_auth_connections_pb2.GroupItem]
    def __init__(self, default_group: _Optional[_Union[_auth_connections_pb2.GroupItem, _Mapping]] = ..., custom_groups: _Optional[_Iterable[_Union[_auth_connections_pb2.GroupItem, _Mapping]]] = ...) -> None: ...

class UpdateAuthConnectionGroupsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
