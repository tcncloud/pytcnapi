from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateQuestionRequest(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class CreateQuestionResponse(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class ListQuestionsRequest(_message.Message):
    __slots__ = ()
    AUTHOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    author_ids: _containers.RepeatedScalarFieldContainer[str]
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, author_ids: _Optional[_Iterable[str]] = ..., category_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListQuestionsResponse(_message.Message):
    __slots__ = ()
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    questions: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Question]
    def __init__(self, questions: _Optional[_Iterable[_Union[_scorecards_pb2.Question, _Mapping]]] = ...) -> None: ...

class UpdateQuestionRequest(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateQuestionResponse(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class DeleteQuestionRequest(_message.Message):
    __slots__ = ()
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    def __init__(self, question_id: _Optional[int] = ...) -> None: ...

class DeleteQuestionResponse(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class GetQuestionRequest(_message.Message):
    __slots__ = ()
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    question: str
    def __init__(self, question_id: _Optional[int] = ..., question: _Optional[str] = ...) -> None: ...

class GetQuestionResponse(_message.Message):
    __slots__ = ()
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _scorecards_pb2.Question
    def __init__(self, question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class CreateQuestionCategoryRequest(_message.Message):
    __slots__ = ()
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    category_id: int
    def __init__(self, question_id: _Optional[int] = ..., category_id: _Optional[int] = ...) -> None: ...

class CreateQuestionCategoryResponse(_message.Message):
    __slots__ = ()
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    category_id: int
    question_category_id: int
    def __init__(self, question_id: _Optional[int] = ..., category_id: _Optional[int] = ..., question_category_id: _Optional[int] = ...) -> None: ...

class DeleteQuestionCategoryRequest(_message.Message):
    __slots__ = ()
    class BothIds(_message.Message):
        __slots__ = ()
        QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        question_id: int
        category_id: int
        def __init__(self, question_id: _Optional[int] = ..., category_id: _Optional[int] = ...) -> None: ...
    QUESTION_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    BOTH_IDS_FIELD_NUMBER: _ClassVar[int]
    question_category_id: int
    both_ids: DeleteQuestionCategoryRequest.BothIds
    def __init__(self, question_category_id: _Optional[int] = ..., both_ids: _Optional[_Union[DeleteQuestionCategoryRequest.BothIds, _Mapping]] = ...) -> None: ...

class DeleteQuestionCategoryResponse(_message.Message):
    __slots__ = ()
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    category_id: int
    question_category_id: int
    def __init__(self, question_id: _Optional[int] = ..., category_id: _Optional[int] = ..., question_category_id: _Optional[int] = ...) -> None: ...

class BulkCreateQuestionsRequest(_message.Message):
    __slots__ = ()
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    scorecard_id: int
    use_default: bool
    def __init__(self, scorecard_id: _Optional[int] = ..., use_default: _Optional[bool] = ...) -> None: ...

class BulkCreateQuestionsResponse(_message.Message):
    __slots__ = ()
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    questions: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Question]
    def __init__(self, questions: _Optional[_Iterable[_Union[_scorecards_pb2.Question, _Mapping]]] = ...) -> None: ...
