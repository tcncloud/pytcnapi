from api.commons import acd_pb2 as _acd_pb2
from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScorecardRequest(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class CreateScorecardResponse(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ListScorecardsRequest(_message.Message):
    __slots__ = ()
    AUTHOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    author_ids: _containers.RepeatedScalarFieldContainer[str]
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    states: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.ScorecardState]
    evaluation_types: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.EvaluationType]
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    def __init__(self, author_ids: _Optional[_Iterable[str]] = ..., category_ids: _Optional[_Iterable[int]] = ..., states: _Optional[_Iterable[_Union[_scorecards_pb2.ScorecardState, str]]] = ..., evaluation_types: _Optional[_Iterable[_Union[_scorecards_pb2.EvaluationType, str]]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ...) -> None: ...

class ListScorecardsResponse(_message.Message):
    __slots__ = ()
    SCORECARDS_FIELD_NUMBER: _ClassVar[int]
    scorecards: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Scorecard]
    def __init__(self, scorecards: _Optional[_Iterable[_Union[_scorecards_pb2.Scorecard, _Mapping]]] = ...) -> None: ...

class UpdateScorecardRequest(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateScorecardResponse(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class DeleteScorecardRequest(_message.Message):
    __slots__ = ()
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    scorecard_id: int
    def __init__(self, scorecard_id: _Optional[int] = ...) -> None: ...

class DeleteScorecardResponse(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class GetScorecardRequest(_message.Message):
    __slots__ = ()
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    scorecard_id: int
    use_default: bool
    def __init__(self, scorecard_id: _Optional[int] = ..., use_default: _Optional[bool] = ...) -> None: ...

class GetScorecardResponse(_message.Message):
    __slots__ = ()
    SCORECARD_FIELD_NUMBER: _ClassVar[int]
    scorecard: _scorecards_pb2.Scorecard
    def __init__(self, scorecard: _Optional[_Union[_scorecards_pb2.Scorecard, _Mapping]] = ...) -> None: ...

class ListScorecardsByOrgIdRequest(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_IDS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    author_ids: _containers.RepeatedScalarFieldContainer[str]
    category_ids: _containers.RepeatedScalarFieldContainer[int]
    states: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.ScorecardState]
    evaluation_types: _containers.RepeatedScalarFieldContainer[_scorecards_pb2.EvaluationType]
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    def __init__(self, org_id: _Optional[str] = ..., author_ids: _Optional[_Iterable[str]] = ..., category_ids: _Optional[_Iterable[int]] = ..., states: _Optional[_Iterable[_Union[_scorecards_pb2.ScorecardState, str]]] = ..., evaluation_types: _Optional[_Iterable[_Union[_scorecards_pb2.EvaluationType, str]]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ...) -> None: ...
