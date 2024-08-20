from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSmartQuestionRequest(_message.Message):
    __slots__ = ("smart_question",)
    SMART_QUESTION_FIELD_NUMBER: _ClassVar[int]
    smart_question: _scorecards_pb2.SmartQuestion
    def __init__(self, smart_question: _Optional[_Union[_scorecards_pb2.SmartQuestion, _Mapping]] = ...) -> None: ...

class CreateSmartQuestionResponse(_message.Message):
    __slots__ = ("smart_question",)
    SMART_QUESTION_FIELD_NUMBER: _ClassVar[int]
    smart_question: _scorecards_pb2.SmartQuestion
    def __init__(self, smart_question: _Optional[_Union[_scorecards_pb2.SmartQuestion, _Mapping]] = ...) -> None: ...
