from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdpClient(_message.Message):
    __slots__ = ("idp_client_id", "secret", "redirect_uris", "trusted_peers", "name", "billing_id")
    IDP_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_PEERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    idp_client_id: str
    secret: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    trusted_peers: _containers.RepeatedScalarFieldContainer[str]
    name: str
    billing_id: str
    def __init__(self, idp_client_id: _Optional[str] = ..., secret: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., trusted_peers: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., billing_id: _Optional[str] = ...) -> None: ...
