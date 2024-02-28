from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloWorldWFMAdherenceRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HelloWorldWFMAdherenceResponse(_message.Message):
    __slots__ = ("hello_message",)
    HELLO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    hello_message: str
    def __init__(self, hello_message: _Optional[str] = ...) -> None: ...
