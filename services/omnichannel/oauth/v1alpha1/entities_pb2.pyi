from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectedInboxOAuthURLRequest(_message.Message):
    __slots__ = ("authentication_type", "returning_redirect_uri")
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETURNING_REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    authentication_type: _omnichannel_pb2.ConnectedInboxAuthenticationType
    returning_redirect_uri: str
    def __init__(self, authentication_type: _Optional[_Union[_omnichannel_pb2.ConnectedInboxAuthenticationType, str]] = ..., returning_redirect_uri: _Optional[str] = ...) -> None: ...

class GetConnectedInboxOAuthURLResponse(_message.Message):
    __slots__ = ("oauth_url",)
    OAUTH_URL_FIELD_NUMBER: _ClassVar[int]
    oauth_url: str
    def __init__(self, oauth_url: _Optional[str] = ...) -> None: ...
