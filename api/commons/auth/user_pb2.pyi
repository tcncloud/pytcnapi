from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthClaims(_message.Message):
    __slots__ = ("auth0_user_id", "org_user_id", "org_id", "api_key", "region_id", "name", "impersonate", "client_sid", "agent_sid", "login_sid", "active_org_id")
    AUTH0_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    auth0_user_id: str
    org_user_id: str
    org_id: str
    api_key: str
    region_id: str
    name: str
    impersonate: str
    client_sid: int
    agent_sid: int
    login_sid: int
    active_org_id: str
    def __init__(self, auth0_user_id: _Optional[str] = ..., org_user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., api_key: _Optional[str] = ..., region_id: _Optional[str] = ..., name: _Optional[str] = ..., impersonate: _Optional[str] = ..., client_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., login_sid: _Optional[int] = ..., active_org_id: _Optional[str] = ...) -> None: ...

class AuthenticatedUser(_message.Message):
    __slots__ = ("claims",)
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    claims: AuthClaims
    def __init__(self, claims: _Optional[_Union[AuthClaims, _Mapping]] = ...) -> None: ...
