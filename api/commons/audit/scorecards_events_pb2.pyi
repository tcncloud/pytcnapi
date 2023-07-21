from api.commons import acd_pb2 as _acd_pb2
from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScorecardsCreateQuestionEvent(_message.Message):
    __slots__ = ["author_id", "question_text", "description", "question"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    question_text: str
    description: str
    question: _scorecards_pb2.Question
    def __init__(self, author_id: _Optional[str] = ..., question_text: _Optional[str] = ..., description: _Optional[str] = ..., question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateQuestionEvent(_message.Message):
    __slots__ = ["user_id", "question_text", "description", "update_mask", "question"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    question_text: str
    description: str
    update_mask: _field_mask_pb2.FieldMask
    question: _scorecards_pb2.Question
    def __init__(self, user_id: _Optional[str] = ..., question_text: _Optional[str] = ..., description: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteQuestionEvent(_message.Message):
    __slots__ = ["user_id", "question_text", "description", "category_ids", "question"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    question_text: str
    description: str
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    question: _scorecards_pb2.Question
    def __init__(self, user_id: _Optional[str] = ..., question_text: _Optional[str] = ..., description: _Optional[str] = ..., category_ids: _Optional[_Iterable[int]] = ..., question: _Optional[_Union[_scorecards_pb2.Question, _Mapping]] = ...) -> None: ...

class ScorecardsCreateScorecardEvent(_message.Message):
    __slots__ = ["author_id", "title", "description", "pass_score", "score_type", "evaluation_type", "scorecard"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASS_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    title: str
    description: str
    pass_score: float
    score_type: _scorecards_pb2.ScoreType
    evaluation_type: _scorecards_pb2.EvaluationType
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, author_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., pass_score: _Optional[float] = ..., score_type: _Optional[_Union[_scorecards_pb2.ScoreType, str]] = ..., evaluation_type: _Optional[_Union[_scorecards_pb2.EvaluationType, str]] = ..., scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateScorecardEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "pass_score", "score_type", "evaluation_type", "allow_feedback", "state", "update_mask", "scorecard"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASS_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    pass_score: float
    score_type: _scorecards_pb2.ScoreType
    evaluation_type: _scorecards_pb2.EvaluationType
    allow_feedback: bool
    state: _scorecards_pb2.ScorecardState
    update_mask: _field_mask_pb2.FieldMask
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., pass_score: _Optional[float] = ..., score_type: _Optional[_Union[_scorecards_pb2.ScoreType, str]] = ..., evaluation_type: _Optional[_Union[_scorecards_pb2.EvaluationType, str]] = ..., allow_feedback: bool = ..., state: _Optional[_Union[_scorecards_pb2.ScorecardState, str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteScorecardEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "pass_score", "score_type", "evaluation_type", "state", "scorecard"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASS_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    pass_score: float
    score_type: _scorecards_pb2.ScoreType
    evaluation_type: _scorecards_pb2.EvaluationType
    state: _scorecards_pb2.ScorecardState
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., pass_score: _Optional[float] = ..., score_type: _Optional[_Union[_scorecards_pb2.ScoreType, str]] = ..., evaluation_type: _Optional[_Union[_scorecards_pb2.EvaluationType, str]] = ..., state: _Optional[_Union[_scorecards_pb2.ScorecardState, str]] = ..., scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ScorecardsCloneScorecardEvent(_message.Message):
    __slots__ = ["author_id", "title", "description", "pass_score", "score_type", "evaluation_type", "scorecard"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASS_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    title: str
    description: str
    pass_score: float
    score_type: _scorecards_pb2.ScoreType
    evaluation_type: _scorecards_pb2.EvaluationType
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, author_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., pass_score: _Optional[float] = ..., score_type: _Optional[_Union[_scorecards_pb2.ScoreType, str]] = ..., evaluation_type: _Optional[_Union[_scorecards_pb2.EvaluationType, str]] = ..., scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ScorecardsCreateEvaluationEvent(_message.Message):
    __slots__ = ["evaluation_id", "scorecard_id", "scorer_id", "agent_user_id", "call_sid", "evaluation"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    scorecard_id: int
    scorer_id: str
    agent_user_id: str
    call_sid: int
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., scorer_id: _Optional[str] = ..., agent_user_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateEvaluationEvent(_message.Message):
    __slots__ = ["evaluation_id", "scorecard_id", "scorer_id", "agent_user_id", "call_sid", "evaluation"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    scorecard_id: int
    scorer_id: str
    agent_user_id: str
    call_sid: int
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., scorer_id: _Optional[str] = ..., agent_user_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteEvaluationEvent(_message.Message):
    __slots__ = ["evaluation_id", "scorecard_id", "user_id", "agent_user_id", "call_sid", "evaluation"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    scorecard_id: int
    user_id: str
    agent_user_id: str
    call_sid: int
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., user_id: _Optional[str] = ..., agent_user_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class ScorecardsCreateSectionEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "weight", "section"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    weight: int
    section: _scorecards_pb2.Section
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., weight: _Optional[int] = ..., section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateSectionEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "weight", "sort_order", "update_mask", "section"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    weight: int
    sort_order: int
    update_mask: _field_mask_pb2.FieldMask
    section: _scorecards_pb2.Section
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., weight: _Optional[int] = ..., sort_order: _Optional[int] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteSectionEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "weight", "section"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    weight: int
    section: _scorecards_pb2.Section
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., weight: _Optional[int] = ..., section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class ScorecardsCreateCategoryEvent(_message.Message):
    __slots__ = ["author_id", "title", "description", "created_at", "category"]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    title: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    category: _scorecards_pb2.Category
    def __init__(self, author_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateCategoryEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "update_mask", "category"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    update_mask: _field_mask_pb2.FieldMask
    category: _scorecards_pb2.Category
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteCategoryEvent(_message.Message):
    __slots__ = ["user_id", "title", "description", "deleted_at", "category"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    title: str
    description: str
    deleted_at: _timestamp_pb2.Timestamp
    category: _scorecards_pb2.Category
    def __init__(self, user_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class ScorecardsCreateEvaluationQuestionEvent(_message.Message):
    __slots__ = ["evaluation_question_id", "evaluation_id", "scorecard_question_id", "user_id", "evaluation_question"]
    EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question_id: int
    evaluation_id: int
    scorecard_question_id: int
    user_id: str
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question_id: _Optional[int] = ..., evaluation_id: _Optional[int] = ..., scorecard_question_id: _Optional[int] = ..., user_id: _Optional[str] = ..., evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateEvaluationQuestionEvent(_message.Message):
    __slots__ = ["evaluation_question_id", "evaluation_id", "scorecard_question_id", "user_id", "skipped", "points", "update_mask", "evaluation_question"]
    EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_QUESTION_FIELD_NUMBER: _ClassVar[int]
    evaluation_question_id: int
    evaluation_id: int
    scorecard_question_id: int
    user_id: str
    skipped: bool
    points: int
    update_mask: _field_mask_pb2.FieldMask
    evaluation_question: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question_id: _Optional[int] = ..., evaluation_id: _Optional[int] = ..., scorecard_question_id: _Optional[int] = ..., user_id: _Optional[str] = ..., skipped: bool = ..., points: _Optional[int] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., evaluation_question: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteEvaluationQuestionEvent(_message.Message):
    __slots__ = ["evaluation_question_id", "evaluation_id", "scorecard_question_id", "user_id", "evaluation_questions"]
    EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    evaluation_question_id: int
    evaluation_id: int
    scorecard_question_id: int
    user_id: str
    evaluation_questions: _scorecards_pb2.EvaluationQuestion
    def __init__(self, evaluation_question_id: _Optional[int] = ..., evaluation_id: _Optional[int] = ..., scorecard_question_id: _Optional[int] = ..., user_id: _Optional[str] = ..., evaluation_questions: _Optional[_Union[_scorecards_pb2.EvaluationQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsCreateScorecardQuestionEvent(_message.Message):
    __slots__ = ["user_id", "question", "description", "allow_skip", "max_points", "allow_multi_select", "scorecard_question"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SKIP_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTI_SELECT_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    question: str
    description: str
    allow_skip: bool
    max_points: int
    allow_multi_select: bool
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, user_id: _Optional[str] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., allow_skip: bool = ..., max_points: _Optional[int] = ..., allow_multi_select: bool = ..., scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsUpdateScorecardQuestionEvent(_message.Message):
    __slots__ = ["user_id", "question", "description", "allow_skip", "max_points", "allow_multi_select", "sort_order", "update_mask", "scorecard_question"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SKIP_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTI_SELECT_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    question: str
    description: str
    allow_skip: bool
    max_points: int
    allow_multi_select: bool
    sort_order: int
    update_mask: _field_mask_pb2.FieldMask
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, user_id: _Optional[str] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., allow_skip: bool = ..., max_points: _Optional[int] = ..., allow_multi_select: bool = ..., sort_order: _Optional[int] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsDeleteScorecardQuestionEvent(_message.Message):
    __slots__ = ["user_id", "question", "description", "allow_skip", "max_points", "allow_multi_select", "scorecard_question"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SKIP_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTI_SELECT_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    question: str
    description: str
    allow_skip: bool
    max_points: int
    allow_multi_select: bool
    scorecard_question: _scorecards_pb2.ScorecardQuestion
    def __init__(self, user_id: _Optional[str] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., allow_skip: bool = ..., max_points: _Optional[int] = ..., allow_multi_select: bool = ..., scorecard_question: _Optional[_Union[_scorecards_pb2.ScorecardQuestion, _Mapping]] = ...) -> None: ...

class ScorecardsCreateAutoEvaluationEvent(_message.Message):
    __slots__ = ["auto_evaluation_id", "scorecard_id", "agent_user_id", "call_sid", "call_type", "transcript_sid", "risk_level", "auto_evaluation"]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    scorecard_id: int
    agent_user_id: str
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    transcript_sid: int
    risk_level: _scorecards_pb2.RiskLevel
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., agent_user_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., transcript_sid: _Optional[int] = ..., risk_level: _Optional[_Union[_scorecards_pb2.RiskLevel, str]] = ..., auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...
