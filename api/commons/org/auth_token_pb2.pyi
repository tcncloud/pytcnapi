from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthToken(_message.Message):
    __slots__ = ("token", "user_id", "org_id", "expiration")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    token: str
    user_id: str
    org_id: str
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[str] = ..., user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
