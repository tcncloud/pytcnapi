from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEvaluationRequest(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class CreateEvaluationResponse(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class UpdateEvaluationRequest(_message.Message):
    __slots__ = ["evaluation", "update_mask"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEvaluationResponse(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class DeleteEvaluationRequest(_message.Message):
    __slots__ = ["evaluation_id"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    def __init__(self, evaluation_id: _Optional[int] = ...) -> None: ...

class DeleteEvaluationResponse(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class GetEvaluationRequest(_message.Message):
    __slots__ = ["evaluation_id"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    def __init__(self, evaluation_id: _Optional[int] = ...) -> None: ...

class GetEvaluationResponse(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class ScoreEvaluationRequest(_message.Message):
    __slots__ = ["evaluation_id"]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: int
    def __init__(self, evaluation_id: _Optional[int] = ...) -> None: ...

class ScoreEvaluationResponse(_message.Message):
    __slots__ = ["evaluation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _scorecards_pb2.Evaluation
    def __init__(self, evaluation: _Optional[_Union[_scorecards_pb2.Evaluation, _Mapping]] = ...) -> None: ...

class ListEvaluationsRequest(_message.Message):
    __slots__ = ["scorer_id", "completed_at", "category_ids", "agent_user_ids", "scorecard_ids"]
    SCORER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_IDS_FIELD_NUMBER: _ClassVar[int]
    scorer_id: _containers.RepeatedScalarFieldContainer[str]
    completed_at: _scorecards_pb2.TimeFilter
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    scorecard_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, scorer_id: _Optional[_Iterable[str]] = ..., completed_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ..., category_ids: _Optional[_Iterable[int]] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., scorecard_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListEvaluationsResponse(_message.Message):
    __slots__ = ["evaluations"]
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Evaluation]
    def __init__(self, evaluations: _Optional[_Iterable[_Union[_scorecards_pb2.Evaluation, _Mapping]]] = ...) -> None: ...
