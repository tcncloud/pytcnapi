from api.commons import agent_training_pb2 as _agent_training_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentTrainingCreateLearningOpportunityEvent(_message.Message):
    __slots__ = ["agent_user_id", "description", "learning_opportunity"]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEARNING_OPPORTUNITY_FIELD_NUMBER: _ClassVar[int]
    agent_user_id: str
    description: str
    learning_opportunity: _agent_training_pb2.LearningOpportunity
    def __init__(self, agent_user_id: _Optional[str] = ..., description: _Optional[str] = ..., learning_opportunity: _Optional[_Union[_agent_training_pb2.LearningOpportunity, _Mapping]] = ...) -> None: ...
