from api.commons import agent_training_pb2 as _agent_training_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateLearningOpportunityRequest(_message.Message):
    __slots__ = ["learning_opportunity"]
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class CreateLearningOpportunityResponse(_message.Message):
    __slots__ = ["learning_opportunity"]
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...

class ListLearningOpportunitiesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListLearningOpportunitiesResponse(_message.Message):
    __slots__ = ["learning_opportunities"]
    LEARNING_OPPORTUNITIES_FIELD_NUMBER: _ClassVar[int]
    learning_opportunities: _containers.RepeatedCompositeFieldContainer[_agent_training_pb2.LearningOpportunity]
    def __init__(self, learning_opportunities: _Optional[_Iterable[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]]] = ...) -> None: ...
