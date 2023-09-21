from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LMSPipelineFailureEvent(_message.Message):
    __slots__ = ["element_id", "element_name", "file_names", "failure_message"]
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    element_name: str
    file_names: _containers.RepeatedScalarFieldContainer[str]
    failure_message: str
    def __init__(self, element_id: _Optional[str] = ..., element_name: _Optional[str] = ..., file_names: _Optional[_Iterable[str]] = ..., failure_message: _Optional[str] = ...) -> None: ...
