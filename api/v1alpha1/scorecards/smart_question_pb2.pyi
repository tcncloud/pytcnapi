from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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

class UpdateSmartQuestionRequest(_message.Message):
    __slots__ = ("smart_question", "update_mask")
    SMART_QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    smart_question: _scorecards_pb2.SmartQuestion
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, smart_question: _Optional[_Union[_scorecards_pb2.SmartQuestion, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSmartQuestionResponse(_message.Message):
    __slots__ = ("smart_question",)
    SMART_QUESTION_FIELD_NUMBER: _ClassVar[int]
    smart_question: _scorecards_pb2.SmartQuestion
    def __init__(self, smart_question: _Optional[_Union[_scorecards_pb2.SmartQuestion, _Mapping]] = ...) -> None: ...

class DeleteSmartQuestionRequest(_message.Message):
    __slots__ = ("smart_question_id",)
    SMART_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    smart_question_id: int
    def __init__(self, smart_question_id: _Optional[int] = ...) -> None: ...

class DeleteSmartQuestionResponse(_message.Message):
    __slots__ = ("smart_question",)
    SMART_QUESTION_FIELD_NUMBER: _ClassVar[int]
    smart_question: _scorecards_pb2.SmartQuestion
    def __init__(self, smart_question: _Optional[_Union[_scorecards_pb2.SmartQuestion, _Mapping]] = ...) -> None: ...
