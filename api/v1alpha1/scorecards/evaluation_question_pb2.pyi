from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEvaluationQuestionRequest(_message.Message):
    __slots__ = ("evaluation_question",)
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class CreateEvaluationQuestionResponse(_message.Message):
    __slots__ = ("evaluation_question",)
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class UpdateEvaluationQuestionRequest(_message.Message):
    __slots__ = ("evaluation_question", "update_mask")
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEvaluationQuestionResponse(_message.Message):
    __slots__ = ("evaluation_question",)
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class DeleteEvaluationQuestionRequest(_message.Message):
    __slots__ = ("evaluation_question_id",)
    EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_question_id: int
    def __init__(self, evaluation_question_id: _Optional[int] = ...) -> None: ...

class DeleteEvaluationQuestionResponse(_message.Message):
    __slots__ = ("evaluation_question",)
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...
