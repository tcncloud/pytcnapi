from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[CategoryType]
    SKILL_CALLS: _ClassVar[CategoryType]
    MANUAL_DIAL: _ClassVar[CategoryType]

class EvaluationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATE_MANUAL: _ClassVar[EvaluationType]
    EVALUATE_AUTO: _ClassVar[EvaluationType]
    EVALUATE_SMART: _ClassVar[EvaluationType]

class ScoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORE_SIMPLE_SUM: _ClassVar[ScoreType]
    SCORE_WEIGHTED_SUM: _ClassVar[ScoreType]
    SCORE_EVEN_WEIGHTED_SUM: _ClassVar[ScoreType]

class FailType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAIL_QUESTION: _ClassVar[FailType]
    FAIL_SECTION: _ClassVar[FailType]
    FAIL_SCORECARD: _ClassVar[FailType]

class QuestionFocus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUESTION_FOCUS_UNSPECIFIED: _ClassVar[QuestionFocus]
    QUESTION_FOCUS_AGENT: _ClassVar[QuestionFocus]
    QUESTION_FOCUS_CUSTOMER: _ClassVar[QuestionFocus]

class ScorecardState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCORECARD_IS_DRAFT: _ClassVar[ScorecardState]
    SCORECARD_IS_READY: _ClassVar[ScorecardState]
    SCORECARD_IS_IN_USE: _ClassVar[ScorecardState]
    SCORECARD_IS_TEMPLATE: _ClassVar[ScorecardState]
    SCORECARD_IS_READY_DISABLED: _ClassVar[ScorecardState]
    SCORECARD_IS_IN_USE_DISABLED: _ClassVar[ScorecardState]

class EvaluationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_IN_PROGRESS: _ClassVar[EvaluationState]
    EVALUATION_PASSED: _ClassVar[EvaluationState]
    EVALUATION_FAILED: _ClassVar[EvaluationState]

class RiskLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RISK_LEVEL_NONE: _ClassVar[RiskLevel]
    RISK_LEVEL_LOW: _ClassVar[RiskLevel]
    RISK_LEVEL_MEDIUM: _ClassVar[RiskLevel]
    RISK_LEVEL_HIGH: _ClassVar[RiskLevel]
    RISK_LEVEL_RISK_FREE: _ClassVar[RiskLevel]
INVALID: CategoryType
SKILL_CALLS: CategoryType
MANUAL_DIAL: CategoryType
EVALUATE_MANUAL: EvaluationType
EVALUATE_AUTO: EvaluationType
EVALUATE_SMART: EvaluationType
SCORE_SIMPLE_SUM: ScoreType
SCORE_WEIGHTED_SUM: ScoreType
SCORE_EVEN_WEIGHTED_SUM: ScoreType
FAIL_QUESTION: FailType
FAIL_SECTION: FailType
FAIL_SCORECARD: FailType
QUESTION_FOCUS_UNSPECIFIED: QuestionFocus
QUESTION_FOCUS_AGENT: QuestionFocus
QUESTION_FOCUS_CUSTOMER: QuestionFocus
SCORECARD_IS_DRAFT: ScorecardState
SCORECARD_IS_READY: ScorecardState
SCORECARD_IS_IN_USE: ScorecardState
SCORECARD_IS_TEMPLATE: ScorecardState
SCORECARD_IS_READY_DISABLED: ScorecardState
SCORECARD_IS_IN_USE_DISABLED: ScorecardState
EVALUATION_IN_PROGRESS: EvaluationState
EVALUATION_PASSED: EvaluationState
EVALUATION_FAILED: EvaluationState
RISK_LEVEL_NONE: RiskLevel
RISK_LEVEL_LOW: RiskLevel
RISK_LEVEL_MEDIUM: RiskLevel
RISK_LEVEL_HIGH: RiskLevel
RISK_LEVEL_RISK_FREE: RiskLevel

class TimeFilter(_message.Message):
    __slots__ = ("eq", "gte", "lte", "gt", "lt")
    EQ_FIELD_NUMBER: _ClassVar[int]
    GTE_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    GT_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    eq: _timestamp_pb2.Timestamp
    gte: _timestamp_pb2.Timestamp
    lte: _timestamp_pb2.Timestamp
    gt: _timestamp_pb2.Timestamp
    lt: _timestamp_pb2.Timestamp
    def __init__(self, eq: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ("category_id", "author_id", "title", "description", "skill_profiles", "version", "call_types", "is_system", "category_type", "skill_profile_group_sids")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    author_id: str
    title: str
    description: str
    skill_profiles: _containers.RepeatedScalarFieldContainer[int]
    version: int
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    is_system: bool
    category_type: CategoryType
    skill_profile_group_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, category_id: _Optional[int] = ..., author_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., skill_profiles: _Optional[_Iterable[int]] = ..., version: _Optional[int] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., is_system: bool = ..., category_type: _Optional[_Union[CategoryType, str]] = ..., skill_profile_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class Evaluation(_message.Message):
    __slots__ = ("evaluation_id", "scorecard_id", "scorer_id", "call_sid", "score", "evaluation_state", "evaluation_sections", "completed_at", "deleted_at", "agent_user_id", "call_type", "transcript_sid", "custom_fields", "deleted_by", "is_recoverable")
    class CustomField(_message.Message):
        __slots__ = ("key", "field")
        KEY_FIELD_NUMBER: _ClassVar[int]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        key: str
        field: str
        def __init__(self, key: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCORER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_STATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_RECOVERABLE_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    scorecard_id: int
    scorer_id: str
    call_sid: int
    score: float
    evaluation_state: EvaluationState
    evaluation_sections: _containers.RepeatedCompositeFieldContainer[EvaluationSection]
    completed_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    agent_user_id: str
    call_type: _acd_pb2.CallType.Enum
    transcript_sid: int
    custom_fields: _containers.RepeatedCompositeFieldContainer[Evaluation.CustomField]
    deleted_by: str
    is_recoverable: bool
    def __init__(self, evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., scorer_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., score: _Optional[float] = ..., evaluation_state: _Optional[_Union[EvaluationState, str]] = ..., evaluation_sections: _Optional[_Iterable[_Union[EvaluationSection, _Mapping]]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_user_id: _Optional[str] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., transcript_sid: _Optional[int] = ..., custom_fields: _Optional[_Iterable[_Union[Evaluation.CustomField, _Mapping]]] = ..., deleted_by: _Optional[str] = ..., is_recoverable: bool = ...) -> None: ...

class EvaluationSection(_message.Message):
    __slots__ = ("evaluation_section_id", "evaluation_id", "section_id", "points", "possible_points", "sort_order", "deleted_at", "created_at", "evaluation_questions", "auto_evaluation_questions", "skipped")
    EVALUATION_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_POINTS_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    evaluation_section_id: int
    evaluation_id: int
    section_id: int
    points: int
    possible_points: int
    sort_order: int
    deleted_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    evaluation_questions: _containers.RepeatedCompositeFieldContainer[EvaluationQuestion]
    auto_evaluation_questions: _containers.RepeatedCompositeFieldContainer[AutoEvaluationQuestion]
    skipped: bool
    def __init__(self, evaluation_section_id: _Optional[int] = ..., evaluation_id: _Optional[int] = ..., section_id: _Optional[int] = ..., points: _Optional[int] = ..., possible_points: _Optional[int] = ..., sort_order: _Optional[int] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., evaluation_questions: _Optional[_Iterable[_Union[EvaluationQuestion, _Mapping]]] = ..., auto_evaluation_questions: _Optional[_Iterable[_Union[AutoEvaluationQuestion, _Mapping]]] = ..., skipped: bool = ...) -> None: ...

class EvaluationQuestion(_message.Message):
    __slots__ = ("evaluation_question_id", "evaluation_id", "scorecard_question_id", "skipped", "points", "answers", "evaluation_section_id", "comment", "sort_order")
    class Answer(_message.Message):
        __slots__ = ("answer_option", "points", "fail_type")
        ANSWER_OPTION_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        FAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
        answer_option: str
        points: int
        fail_type: FailType
        def __init__(self, answer_option: _Optional[str] = ..., points: _Optional[int] = ..., fail_type: _Optional[_Union[FailType, str]] = ...) -> None: ...
    EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    evaluation_question_id: int
    evaluation_id: int
    scorecard_question_id: int
    skipped: bool
    points: int
    answers: _containers.RepeatedCompositeFieldContainer[EvaluationQuestion.Answer]
    evaluation_section_id: int
    comment: str
    sort_order: int
    def __init__(self, evaluation_question_id: _Optional[int] = ..., evaluation_id: _Optional[int] = ..., scorecard_question_id: _Optional[int] = ..., skipped: bool = ..., points: _Optional[int] = ..., answers: _Optional[_Iterable[_Union[EvaluationQuestion.Answer, _Mapping]]] = ..., evaluation_section_id: _Optional[int] = ..., comment: _Optional[str] = ..., sort_order: _Optional[int] = ...) -> None: ...

class AutoEvaluation(_message.Message):
    __slots__ = ("auto_evaluation_id", "scorecard_id", "call_sid", "agent_user_id", "auto_evaluation_sections", "completed_at", "deleted_at", "call_type", "transcript_sid", "expression_matched", "risk_level", "call_length", "scorecard_info", "category_info")
    class ScorecardInfo(_message.Message):
        __slots__ = ("title",)
        TITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        def __init__(self, title: _Optional[str] = ...) -> None: ...
    class CategoryInfo(_message.Message):
        __slots__ = ("title",)
        TITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        def __init__(self, title: _Optional[str] = ...) -> None: ...
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_MATCHED_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CALL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_INFO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_INFO_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    scorecard_id: int
    call_sid: int
    agent_user_id: str
    auto_evaluation_sections: _containers.RepeatedCompositeFieldContainer[AutoEvaluationSection]
    completed_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    call_type: _acd_pb2.CallType.Enum
    transcript_sid: int
    expression_matched: bool
    risk_level: RiskLevel
    call_length: int
    scorecard_info: AutoEvaluation.ScorecardInfo
    category_info: AutoEvaluation.CategoryInfo
    def __init__(self, auto_evaluation_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., call_sid: _Optional[int] = ..., agent_user_id: _Optional[str] = ..., auto_evaluation_sections: _Optional[_Iterable[_Union[AutoEvaluationSection, _Mapping]]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., transcript_sid: _Optional[int] = ..., expression_matched: bool = ..., risk_level: _Optional[_Union[RiskLevel, str]] = ..., call_length: _Optional[int] = ..., scorecard_info: _Optional[_Union[AutoEvaluation.ScorecardInfo, _Mapping]] = ..., category_info: _Optional[_Union[AutoEvaluation.CategoryInfo, _Mapping]] = ...) -> None: ...

class AutoEvaluationQuestion(_message.Message):
    __slots__ = ("auto_evaluation_question_id", "auto_evaluation_id", "auto_evaluation_section_id", "auto_question_id", "flagged", "passed", "sort_order", "risk_level", "expression_matched")
    AUTO_EVALUATION_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    FLAGGED_FIELD_NUMBER: _ClassVar[int]
    PASSED_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_MATCHED_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_question_id: int
    auto_evaluation_id: int
    auto_evaluation_section_id: int
    auto_question_id: int
    flagged: _containers.RepeatedScalarFieldContainer[int]
    passed: bool
    sort_order: int
    risk_level: RiskLevel
    expression_matched: bool
    def __init__(self, auto_evaluation_question_id: _Optional[int] = ..., auto_evaluation_id: _Optional[int] = ..., auto_evaluation_section_id: _Optional[int] = ..., auto_question_id: _Optional[int] = ..., flagged: _Optional[_Iterable[int]] = ..., passed: bool = ..., sort_order: _Optional[int] = ..., risk_level: _Optional[_Union[RiskLevel, str]] = ..., expression_matched: bool = ...) -> None: ...

class AutoEvaluationSection(_message.Message):
    __slots__ = ("auto_evaluation_section_id", "auto_evaluation_id", "section_id", "sort_order", "deleted_at", "created_at", "auto_evaluation_questions", "risk_level")
    AUTO_EVALUATION_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_section_id: int
    auto_evaluation_id: int
    section_id: int
    sort_order: int
    deleted_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    auto_evaluation_questions: _containers.RepeatedCompositeFieldContainer[AutoEvaluationQuestion]
    risk_level: RiskLevel
    def __init__(self, auto_evaluation_section_id: _Optional[int] = ..., auto_evaluation_id: _Optional[int] = ..., section_id: _Optional[int] = ..., sort_order: _Optional[int] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auto_evaluation_questions: _Optional[_Iterable[_Union[AutoEvaluationQuestion, _Mapping]]] = ..., risk_level: _Optional[_Union[RiskLevel, str]] = ...) -> None: ...

class Question(_message.Message):
    __slots__ = ("question_id", "author_id", "question", "description", "categories", "focus")
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    FOCUS_FIELD_NUMBER: _ClassVar[int]
    question_id: int
    author_id: str
    question: str
    description: str
    categories: _containers.RepeatedCompositeFieldContainer[Category]
    focus: QuestionFocus
    def __init__(self, question_id: _Optional[int] = ..., author_id: _Optional[str] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[Category, _Mapping]]] = ..., focus: _Optional[_Union[QuestionFocus, str]] = ...) -> None: ...

class ScorecardQuestion(_message.Message):
    __slots__ = ("scorecard_question_id", "question", "description", "question_id", "allow_skip", "answers", "multi_select", "scorecard_id", "section_id", "version", "sort_order")
    class Answer(_message.Message):
        __slots__ = ("answer_option", "points", "fail_type")
        ANSWER_OPTION_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        FAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
        answer_option: str
        points: int
        fail_type: FailType
        def __init__(self, answer_option: _Optional[str] = ..., points: _Optional[int] = ..., fail_type: _Optional[_Union[FailType, str]] = ...) -> None: ...
    class MultiSelect(_message.Message):
        __slots__ = ("max_points",)
        MAX_POINTS_FIELD_NUMBER: _ClassVar[int]
        max_points: int
        def __init__(self, max_points: _Optional[int] = ...) -> None: ...
    SCORECARD_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SKIP_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    MULTI_SELECT_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    scorecard_question_id: int
    question: str
    description: str
    question_id: int
    allow_skip: bool
    answers: _containers.RepeatedCompositeFieldContainer[ScorecardQuestion.Answer]
    multi_select: ScorecardQuestion.MultiSelect
    scorecard_id: int
    section_id: int
    version: int
    sort_order: int
    def __init__(self, scorecard_question_id: _Optional[int] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., question_id: _Optional[int] = ..., allow_skip: bool = ..., answers: _Optional[_Iterable[_Union[ScorecardQuestion.Answer, _Mapping]]] = ..., multi_select: _Optional[_Union[ScorecardQuestion.MultiSelect, _Mapping]] = ..., scorecard_id: _Optional[int] = ..., section_id: _Optional[int] = ..., version: _Optional[int] = ..., sort_order: _Optional[int] = ...) -> None: ...

class Section(_message.Message):
    __slots__ = ("section_id", "scorecard_id", "title", "description", "weight", "questions", "version", "sort_order", "auto_questions", "smart_questions")
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    AUTO_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    SMART_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    section_id: int
    scorecard_id: int
    title: str
    description: str
    weight: int
    questions: _containers.RepeatedCompositeFieldContainer[ScorecardQuestion]
    version: int
    sort_order: int
    auto_questions: _containers.RepeatedCompositeFieldContainer[AutoQuestion]
    smart_questions: _containers.RepeatedCompositeFieldContainer[SmartQuestion]
    def __init__(self, section_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., weight: _Optional[int] = ..., questions: _Optional[_Iterable[_Union[ScorecardQuestion, _Mapping]]] = ..., version: _Optional[int] = ..., sort_order: _Optional[int] = ..., auto_questions: _Optional[_Iterable[_Union[AutoQuestion, _Mapping]]] = ..., smart_questions: _Optional[_Iterable[_Union[SmartQuestion, _Mapping]]] = ...) -> None: ...

class Scorecard(_message.Message):
    __slots__ = ("scorecard_id", "author_id", "title", "description", "pass_score", "score_type", "evaluation_type", "allow_feedback", "distribute_weights", "category", "sections", "version", "state", "is_ad_hoc", "custom_field_keys", "call_types", "updated_at")
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PASS_SCORE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTE_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_AD_HOC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_KEYS_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    scorecard_id: int
    author_id: str
    title: str
    description: str
    pass_score: float
    score_type: ScoreType
    evaluation_type: EvaluationType
    allow_feedback: bool
    distribute_weights: bool
    category: Category
    sections: _containers.RepeatedCompositeFieldContainer[Section]
    version: int
    state: ScorecardState
    is_ad_hoc: bool
    custom_field_keys: _containers.RepeatedScalarFieldContainer[str]
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, scorecard_id: _Optional[int] = ..., author_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., pass_score: _Optional[float] = ..., score_type: _Optional[_Union[ScoreType, str]] = ..., evaluation_type: _Optional[_Union[EvaluationType, str]] = ..., allow_feedback: bool = ..., distribute_weights: bool = ..., category: _Optional[_Union[Category, _Mapping]] = ..., sections: _Optional[_Iterable[_Union[Section, _Mapping]]] = ..., version: _Optional[int] = ..., state: _Optional[_Union[ScorecardState, str]] = ..., is_ad_hoc: bool = ..., custom_field_keys: _Optional[_Iterable[str]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AutoQuestion(_message.Message):
    __slots__ = ("auto_question_id", "flag_sid", "scorecard_id", "auto_section_id", "sort_order", "flag_expression", "question", "description", "question_id", "risk_level")
    class FlagExpr(_message.Message):
        __slots__ = ("flag",)
        class Flag(_message.Message):
            __slots__ = ("flag_sid",)
            FLAG_SID_FIELD_NUMBER: _ClassVar[int]
            flag_sid: int
            def __init__(self, flag_sid: _Optional[int] = ...) -> None: ...
        AND_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        FLAG_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        flag: AutoQuestion.FlagExpr.Flag
        def __init__(self, flag: _Optional[_Union[AutoQuestion.FlagExpr.Flag, _Mapping]] = ..., **kwargs) -> None: ...
    AUTO_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    FLAG_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    auto_question_id: int
    flag_sid: int
    scorecard_id: int
    auto_section_id: int
    sort_order: int
    flag_expression: AutoQuestion.FlagExpr
    question: str
    description: str
    question_id: int
    risk_level: RiskLevel
    def __init__(self, auto_question_id: _Optional[int] = ..., flag_sid: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., auto_section_id: _Optional[int] = ..., sort_order: _Optional[int] = ..., flag_expression: _Optional[_Union[AutoQuestion.FlagExpr, _Mapping]] = ..., question: _Optional[str] = ..., description: _Optional[str] = ..., question_id: _Optional[int] = ..., risk_level: _Optional[_Union[RiskLevel, str]] = ...) -> None: ...

class SmartQuestion(_message.Message):
    __slots__ = ("smart_question_id", "scorecard_id", "section_id", "question_id", "description", "question", "answers", "focus", "sort_order")
    class Answer(_message.Message):
        __slots__ = ("answer", "points", "fail_type")
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        FAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
        answer: str
        points: int
        fail_type: FailType
        def __init__(self, answer: _Optional[str] = ..., points: _Optional[int] = ..., fail_type: _Optional[_Union[FailType, str]] = ...) -> None: ...
    SMART_QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    FOCUS_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    smart_question_id: int
    scorecard_id: int
    section_id: int
    question_id: int
    description: str
    question: str
    answers: _containers.RepeatedCompositeFieldContainer[SmartQuestion.Answer]
    focus: QuestionFocus
    sort_order: int
    def __init__(self, smart_question_id: _Optional[int] = ..., scorecard_id: _Optional[int] = ..., section_id: _Optional[int] = ..., question_id: _Optional[int] = ..., description: _Optional[str] = ..., question: _Optional[str] = ..., answers: _Optional[_Iterable[_Union[SmartQuestion.Answer, _Mapping]]] = ..., focus: _Optional[_Union[QuestionFocus, str]] = ..., sort_order: _Optional[int] = ...) -> None: ...
