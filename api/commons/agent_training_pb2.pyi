from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LearningOpportunity(_message.Message):
    __slots__ = ["learning_opportunity_id", "call_sid", "call_type", "transcript_sid", "agent_user_id", "start_offset", "end_offset", "description"]
    LEARNING_OPPORTUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity_id: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    transcript_sid: int
    agent_user_id: str
    start_offset: int
    end_offset: int
    description: str
    def __init__(self, learning_opportunity_id: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., transcript_sid: _Optional[int] = ..., agent_user_id: _Optional[str] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
