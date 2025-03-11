from api.commons.org import idp_pb2 as _idp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateClientRequest(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _idp_pb2.IdpClient
    def __init__(self, client: _Optional[_Union[_idp_pb2.IdpClient, _Mapping]] = ...) -> None: ...

class CreateClientResponse(_message.Message):
    __slots__ = ("already_exists", "client")
    ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    already_exists: bool
    client: _idp_pb2.IdpClient
    def __init__(self, already_exists: bool = ..., client: _Optional[_Union[_idp_pb2.IdpClient, _Mapping]] = ...) -> None: ...

class DeleteClientRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteClientResponse(_message.Message):
    __slots__ = ("not_found",)
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    not_found: bool
    def __init__(self, not_found: bool = ...) -> None: ...

class UpdateClientRequest(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _idp_pb2.IdpClient
    def __init__(self, client: _Optional[_Union[_idp_pb2.IdpClient, _Mapping]] = ...) -> None: ...

class UpdateClientResponse(_message.Message):
    __slots__ = ("not_found",)
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    not_found: bool
    def __init__(self, not_found: bool = ...) -> None: ...

class ListClientsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClientsResponse(_message.Message):
    __slots__ = ("clients",)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[_idp_pb2.IdpClient]
    def __init__(self, clients: _Optional[_Iterable[_Union[_idp_pb2.IdpClient, _Mapping]]] = ...) -> None: ...
