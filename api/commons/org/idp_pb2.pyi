from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdpClient(_message.Message):
    __slots__ = ("idp_client_id", "secret", "redirect_uris", "trusted_peers", "public", "name", "logo_url")
    IDP_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_PEERS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    idp_client_id: str
    secret: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    trusted_peers: _containers.RepeatedScalarFieldContainer[str]
    public: bool
    name: str
    logo_url: str
    def __init__(self, idp_client_id: _Optional[str] = ..., secret: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., trusted_peers: _Optional[_Iterable[str]] = ..., public: bool = ..., name: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...
