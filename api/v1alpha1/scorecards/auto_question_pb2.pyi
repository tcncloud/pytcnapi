from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAutoQuestionRequest(_message.Message):
    __slots__ = ["auto_question_id"]
    AUTO_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_question_id: int
    def __init__(self, auto_question_id: _Optional[int] = ...) -> None: ...

class GetAutoQuestionResponse(_message.Message):
    __slots__ = ["auto_question"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ...) -> None: ...

class CreateAutoQuestionRequest(_message.Message):
    __slots__ = ["auto_question"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ...) -> None: ...

class CreateAutoQuestionResponse(_message.Message):
    __slots__ = ["auto_question"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ...) -> None: ...

class UpdateAutoQuestionRequest(_message.Message):
    __slots__ = ["auto_question", "update_mask"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAutoQuestionResponse(_message.Message):
    __slots__ = ["auto_question"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ...) -> None: ...

class DeleteAutoQuestionRequest(_message.Message):
    __slots__ = ["auto_question_id"]
    AUTO_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_question_id: int
    def __init__(self, auto_question_id: _Optional[int] = ...) -> None: ...

class DeleteAutoQuestionResponse(_message.Message):
    __slots__ = ["auto_question"]
    AUTO_QUESTION_FIELD_NUMBER: _ClassVar[int]
    auto_question: _scorecards_pb2.AutoQuestion
    def __init__(self, auto_question: _Optional[_Union[_scorecards_pb2.AutoQuestion, _Mapping]] = ...) -> None: ...
