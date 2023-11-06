from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetScorecardQuestionRequest(_message.Message):
    __slots__ = ("scorecard_question_id",)
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    scorecard_question_id: int
    def __init__(self, scorecard_question_id: _Optional[int] = ...) -> None: ...

class GetScorecardQuestionResponse(_message.Message):
    __slots__ = ("scorecard_question",)
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class CreateScorecardQuestionRequest(_message.Message):
    __slots__ = ("scorecard_question",)
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class CreateScorecardQuestionResponse(_message.Message):
    __slots__ = ("scorecard_question",)
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class UpdateScorecardQuestionRequest(_message.Message):
    __slots__ = ("scorecard_question", "update_mask")
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateScorecardQuestionResponse(_message.Message):
    __slots__ = ("scorecard_question",)
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class DeleteScorecardQuestionRequest(_message.Message):
    __slots__ = ("scorecard_question_id",)
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    scorecard_question_id: int
    def __init__(self, scorecard_question_id: _Optional[int] = ...) -> None: ...

class DeleteScorecardQuestionResponse(_message.Message):
    __slots__ = ("scorecard_question",)
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...
