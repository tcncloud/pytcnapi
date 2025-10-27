from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadSpecifiedMessagesRequest(_message.Message):
    __slots__ = ()
    class MessageRequest(_message.Message):
        __slots__ = ()
        MAIL_BOX_FIELD_NUMBER: _ClassVar[int]
        CALLER_SID_FIELD_NUMBER: _ClassVar[int]
        CALLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        mail_box: str
        caller_sid: str
        caller_type: _acd_pb2.CallType.Enum
        def __init__(self, mail_box: _Optional[str] = ..., caller_sid: _Optional[str] = ..., caller_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[DownloadSpecifiedMessagesRequest.MessageRequest]
    def __init__(self, messages: _Optional[_Iterable[_Union[DownloadSpecifiedMessagesRequest.MessageRequest, _Mapping]]] = ...) -> None: ...

class DownloadSpecifiedMessagesResponse(_message.Message):
    __slots__ = ()
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...
