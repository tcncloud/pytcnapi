from api.commons import agent_training_pb2 as _agent_training_pb2
from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateLearningOpportunityRequest(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class CreateLearningOpportunityResponse(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class ListLearningOpportunitiesRequest(_message.Message):
    __slots__ = ("call_identifiers", "transcript_sids", "agent_user_ids", "created_at")
    CALL_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    call_identifiers: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.CallIdentifier]
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _scorecards_pb2.TimeFilter
    def __init__(self, call_identifiers: _Optional[_Iterable[_Union[_agent_training_pb2.CallIdentifier, _Mapping]]] = ..., transcript_sids: _Optional[_Iterable[int]] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ...) -> None: ...

class ListLearningOpportunitiesResponse(_message.Message):
    __slots__ = ("learning_opportunities",)
    LEARNING_OPPORTUNITIES_FIELD_NUMBER: _ClassVar[int]
    learning_opportunities: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.LearningOpportunity]
    def __init__(self, learning_opportunities: _Optional[_Iterable[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]]] = ...) -> None: ...

class ListAgentLearningOpportunitiesRequest(_message.Message):
    __slots__ = ("call_identifiers", "transcript_sids", "created_at")
    CALL_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    call_identifiers: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.CallIdentifier]
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    created_at: _scorecards_pb2.TimeFilter
    def __init__(self, call_identifiers: _Optional[_Iterable[_Union[_agent_training_pb2.CallIdentifier, _Mapping]]] = ..., transcript_sids: _Optional[_Iterable[int]] = ..., created_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ...) -> None: ...

class ListAgentLearningOpportunitiesResponse(_message.Message):
    __slots__ = ("learning_opportunities",)
    LEARNING_OPPORTUNITIES_FIELD_NUMBER: _ClassVar[int]
    learning_opportunities: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.LearningOpportunity]
    def __init__(self, learning_opportunities: _Optional[_Iterable[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]]] = ...) -> None: ...

class UpdateLearningOpportunityRequest(_message.Message):
    __slots__ = ("learning_opportunity", "update_mask")
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateLearningOpportunityResponse(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class CompleteAgentLearningOpportunityRequest(_message.Message):
    __slots__ = ("learning_opportunity_id",)
    LEARNING_OPPORTUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity_id: int
    def __init__(self, learning_opportunity_id: _Optional[int] = ...) -> None: ...

class CompleteAgentLearningOpportunityResponse(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class DeleteLearningOpportunityRequest(_message.Message):
    __slots__ = ("learning_opportunity_id",)
    LEARNING_OPPORTUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity_id: int
    def __init__(self, learning_opportunity_id: _Optional[int] = ...) -> None: ...

class DeleteLearningOpportunityResponse(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class GetLearningOpportunityRequest(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: int
    def __init__(self, learning_opportunity: _Optional[int] = ...) -> None: ...

class GetLearningOpportunityResponse(_message.Message):
    __slots__ = ("learning_opportunity",)
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class ListDashboardsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDashboardsResponse(_message.Message):
    __slots__ = ("dashboards",)
    class Dashboard(_message.Message):
        __slots__ = ("resource_id", "title")
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        resource_id: str
        title: str
        def __init__(self, resource_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    dashboards: _containers.RepeatedCompositeFieldContainer[ListDashboardsResponse.Dashboard]
    def __init__(self, dashboards: _Optional[_Iterable[_Union[ListDashboardsResponse.Dashboard, _Mapping]]] = ...) -> None: ...

class ListLearningOpportunitiesByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "call_identifiers", "transcript_sids", "agent_user_ids", "created_at")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    call_identifiers: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.CallIdentifier]
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _scorecards_pb2.TimeFilter
    def __init__(self, org_id: _Optional[str] = ..., call_identifiers: _Optional[_Iterable[_Union[_agent_training_pb2.CallIdentifier, _Mapping]]] = ..., transcript_sids: _Optional[_Iterable[int]] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_scorecards_pb2.TimeFilter, _Mapping]] = ...) -> None: ...

class DeleteLearningOpportunityByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "learning_opportunity_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LEARNING_OPPORTUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    learning_opportunity_id: int
    def __init__(self, org_id: _Optional[str] = ..., learning_opportunity_id: _Optional[int] = ...) -> None: ...
