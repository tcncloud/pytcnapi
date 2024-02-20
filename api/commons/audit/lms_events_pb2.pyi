from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LMSPipelineFailureEvent(_message.Message):
    __slots__ = ("element_id", "element_name", "file_name", "failure_message")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    element_name: str
    file_name: str
    failure_message: str
    def __init__(self, element_id: _Optional[str] = ..., element_name: _Optional[str] = ..., file_name: _Optional[str] = ..., failure_message: _Optional[str] = ...) -> None: ...

class LMSPipelineNoOutputEvent(_message.Message):
    __slots__ = ("element_id", "element_name", "file_name", "event_message")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    element_name: str
    file_name: str
    event_message: str
    def __init__(self, element_id: _Optional[str] = ..., element_name: _Optional[str] = ..., file_name: _Optional[str] = ..., event_message: _Optional[str] = ...) -> None: ...

class LMSPipelineSuccessfulEvent(_message.Message):
    __slots__ = ("element_id", "element_name", "file_name", "event_message")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    element_name: str
    file_name: str
    event_message: str
    def __init__(self, element_id: _Optional[str] = ..., element_name: _Optional[str] = ..., file_name: _Optional[str] = ..., event_message: _Optional[str] = ...) -> None: ...
