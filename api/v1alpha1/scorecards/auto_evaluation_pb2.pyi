from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAutoEvaluationRequest(_message.Message):
    __slots__ = ("auto_evaluation_id",)
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    def __init__(self, auto_evaluation_id: _Optional[int] = ...) -> None: ...

class GetAutoEvaluationResponse(_message.Message):
    __slots__ = ("auto_evaluation",)
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...

class ListAutoEvaluationsRequest(_message.Message):
    __slots__ = ("scorecard_ids", "completed_at", "category_ids", "call_sid", "agent_user_ids", "page_size", "order_by", "page_token", "risk_levels")
    class CallSidFilter(_message.Message):
        __slots__ = ("any_of", "eq", "gte", "lte", "gt", "lt")
        ANY_OF_FIELD_NUMBER: _ClassVar[int]
        EQ_FIELD_NUMBER: _ClassVar[int]
        GTE_FIELD_NUMBER: _ClassVar[int]
        LTE_FIELD_NUMBER: _ClassVar[int]
        GT_FIELD_NUMBER: _ClassVar[int]
        LT_FIELD_NUMBER: _ClassVar[int]
        any_of: _containers.RepeatedScalarFieldContainer[int]
        eq: int
        gte: int
        lte: int
        gt: int
        lt: int
        def __init__(self, any_of: _Optional[_Iterable[int]] = ..., eq: _Optional[int] = ..., gte: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., lt: _Optional[int] = ...) -> None: ...
    SCORECARD_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVELS_FIELD_NUMBER: _ClassVar[int]
    scorecard_ids: _containers.RepeatedScalarFieldContainer[int]
    completed_at: _scorecards_pb2.TimeFilter
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    call_sid: ListAutoEvaluationsRequest.CallSidFilter
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    order_by: str
    page_token: str
    risk_levels: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.RiskLevel]
    def __init__(self, scorecard_ids: _Optional[_Iterable[int]] = ..., completed_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ..., category_ids: _Optional[_Iterable[int]] = ..., call_sid: _Optional[_Union[ListAutoEvaluationsRequest.CallSidFilter, _Mapping]] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., risk_levels: _Optional[_Iterable[_Union[_scorecards_pb2.RiskLevel, str]]] = ...) -> None: ...

class ListAutoEvaluationsResponse(_message.Message):
    __slots__ = ("auto_evaluations", "next_page_token")
    AUTO_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    auto_evaluations: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.AutoEvaluation]
    next_page_token: str
    def __init__(self, auto_evaluations: _Optional[_Iterable[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAutoEvaluationRequest(_message.Message):
    __slots__ = ("auto_evaluation_id",)
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    def __init__(self, auto_evaluation_id: _Optional[int] = ...) -> None: ...

class DeleteAutoEvaluationResponse(_message.Message):
    __slots__ = ("auto_evaluation",)
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...

class StreamAutoEvaluationsRequest(_message.Message):
    __slots__ = ("scorecard_ids", "completed_at")
    SCORECARD_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    scorecard_ids: _containers.RepeatedScalarFieldContainer[int]
    completed_at: _scorecards_pb2.TimeFilter
    def __init__(self, scorecard_ids: _Optional[_Iterable[int]] = ..., completed_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ...) -> None: ...

class StreamAutoEvaluationsResponse(_message.Message):
    __slots__ = ("auto_evaluation",)
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...

class ListAutoEvaluationsByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "scorecard_ids", "completed_at", "category_ids", "call_sid", "agent_user_ids", "page_size", "order_by", "page_token", "risk_levels")
    class CallSidFilter(_message.Message):
        __slots__ = ("any_of", "eq", "gte", "lte", "gt", "lt")
        ANY_OF_FIELD_NUMBER: _ClassVar[int]
        EQ_FIELD_NUMBER: _ClassVar[int]
        GTE_FIELD_NUMBER: _ClassVar[int]
        LTE_FIELD_NUMBER: _ClassVar[int]
        GT_FIELD_NUMBER: _ClassVar[int]
        LT_FIELD_NUMBER: _ClassVar[int]
        any_of: _containers.RepeatedScalarFieldContainer[int]
        eq: int
        gte: int
        lte: int
        gt: int
        lt: int
        def __init__(self, any_of: _Optional[_Iterable[int]] = ..., eq: _Optional[int] = ..., gte: _Optional[int] = ..., lte: _Optional[int] = ..., gt: _Optional[int] = ..., lt: _Optional[int] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVELS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    scorecard_ids: _containers.RepeatedScalarFieldContainer[int]
    completed_at: _scorecards_pb2.TimeFilter
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    call_sid: ListAutoEvaluationsByOrgIdRequest.CallSidFilter
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    order_by: str
    page_token: str
    risk_levels: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.RiskLevel]
    def __init__(self, org_id: _Optional[str] = ..., scorecard_ids: _Optional[_Iterable[int]] = ..., completed_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ..., category_ids: _Optional[_Iterable[int]] = ..., call_sid: _Optional[_Union[ListAutoEvaluationsByOrgIdRequest.CallSidFilter, _Mapping]] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., risk_levels: _Optional[_Iterable[_Union[_scorecards_pb2.RiskLevel, str]]] = ...) -> None: ...

class DeleteAutoEvaluationByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "auto_evaluation_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    auto_evaluation_id: int
    def __init__(self, org_id: _Optional[str] = ..., auto_evaluation_id: _Optional[int] = ...) -> None: ...
