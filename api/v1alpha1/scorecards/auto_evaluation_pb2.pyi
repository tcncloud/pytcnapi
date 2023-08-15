from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAutoEvaluationRequest(_message.Message):
    __slots__ = ["auto_evaluation_id"]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    def __init__(self, auto_evaluation_id: _Optional[int] = ...) -> None: ...

class GetAutoEvaluationResponse(_message.Message):
    __slots__ = ["auto_evaluation"]
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...

class ListAutoEvaluationsRequest(_message.Message):
    __slots__ = ["scorecard_ids", "completed_at"]
    SCORECARD_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    scorecard_ids: _containers.RepeatedScalarFieldContainer[int]
    completed_at: _scorecards_pb2.TimeFilter
    def __init__(self, scorecard_ids: _Optional[_Iterable[int]] = ..., completed_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ...) -> None: ...

class ListAutoEvaluationsResponse(_message.Message):
    __slots__ = ["auto_evaluations"]
    AUTO_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    auto_evaluations: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.AutoEvaluation]
    def __init__(self, auto_evaluations: _Optional[_Iterable[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]]] = ...) -> None: ...

class DeleteAutoEvaluationRequest(_message.Message):
    __slots__ = ["auto_evaluation_id"]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation_id: int
    def __init__(self, auto_evaluation_id: _Optional[int] = ...) -> None: ...

class DeleteAutoEvaluationResponse(_message.Message):
    __slots__ = ["auto_evaluation"]
    AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    auto_evaluation: _scorecards_pb2.AutoEvaluation
    def __init__(self, auto_evaluation: _Optional[_Union[_scorecards_pb2.AutoEvaluation, _Mapping]] = ...) -> None: ...
