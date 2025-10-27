from api.commons.org import auth_token_pb2 as _auth_token_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAuthTokenRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateAuthTokenResponse(_message.Message):
    __slots__ = ()
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_token: _auth_token_pb2.AuthToken
    def __init__(self, auth_token: _Optional[_Union[_auth_token_pb2.AuthToken, _Mapping]] = ...) -> None: ...

class CreateAuthTokenByUserIdRequest(_message.Message):
    __slots__ = ()
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CreateAuthTokenByUserIdResponse(_message.Message):
    __slots__ = ()
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auth_token: _auth_token_pb2.AuthToken
    def __init__(self, auth_token: _Optional[_Union[_auth_token_pb2.AuthToken, _Mapping]] = ...) -> None: ...

class ListAuthTokensRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAuthTokensResponse(_message.Message):
    __slots__ = ()
    AUTH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    auth_tokens: _containers.RepeatedCompositeFieldContainer[_auth_token_pb2.AuthToken]
    def __init__(self, auth_tokens: _Optional[_Iterable[_Union[_auth_token_pb2.AuthToken, _Mapping]]] = ...) -> None: ...

class ListAuthTokensByUserIdRequest(_message.Message):
    __slots__ = ()
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListAuthTokensByUserIdResponse(_message.Message):
    __slots__ = ()
    AUTH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    auth_tokens: _containers.RepeatedCompositeFieldContainer[_auth_token_pb2.AuthToken]
    def __init__(self, auth_tokens: _Optional[_Iterable[_Union[_auth_token_pb2.AuthToken, _Mapping]]] = ...) -> None: ...

class SetAuthTokenExpirationRequest(_message.Message):
    __slots__ = ()
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class SetAuthTokenExpirationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAuthTokenExpirationByUserIdRequest(_message.Message):
    __slots__ = ()
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    user_id: str
    def __init__(self, token: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SetAuthTokenExpirationByUserIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAuthTokenRequest(_message.Message):
    __slots__ = ()
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class DeleteAuthTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAuthTokenByUserIdRequest(_message.Message):
    __slots__ = ()
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    user_id: str
    def __init__(self, token: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteAuthTokenByUserIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
