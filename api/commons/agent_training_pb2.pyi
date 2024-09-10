from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LearningOpportunityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_OPEN: _ClassVar[LearningOpportunityStatus]
    STATUS_COMPLETED: _ClassVar[LearningOpportunityStatus]

class LearningOpportunityOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[LearningOpportunityOrigin]
    QUALITY_EVALUATION: _ClassVar[LearningOpportunityOrigin]
    AUTO_EVALUATION: _ClassVar[LearningOpportunityOrigin]
    FLAG_EVALUATION: _ClassVar[LearningOpportunityOrigin]
    CONVERSATION: _ClassVar[LearningOpportunityOrigin]
    FLAGGED_CONVERSATION: _ClassVar[LearningOpportunityOrigin]
    SMART_EVALUATION: _ClassVar[LearningOpportunityOrigin]
STATUS_OPEN: LearningOpportunityStatus
STATUS_COMPLETED: LearningOpportunityStatus
UNDEFINED: LearningOpportunityOrigin
QUALITY_EVALUATION: LearningOpportunityOrigin
AUTO_EVALUATION: LearningOpportunityOrigin
FLAG_EVALUATION: LearningOpportunityOrigin
CONVERSATION: LearningOpportunityOrigin
FLAGGED_CONVERSATION: LearningOpportunityOrigin
SMART_EVALUATION: LearningOpportunityOrigin

class LearningOpportunity(_message.Message):
    __slots__ = ("learning_opportunity_id", "call_sid", "call_type", "transcript_sid", "agent_user_id", "start_offset", "end_offset", "description", "created_at", "title", "status", "origin", "creator_user_id", "evaluation_id", "auto_evaluation_id", "smart_evaluation_id")
    LEARNING_OPPORTUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    CREATOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    learning_opportunity_id: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    transcript_sid: int
    agent_user_id: str
    start_offset: int
    end_offset: int
    description: str
    created_at: _timestamp_pb2.Timestamp
    title: str
    status: LearningOpportunityStatus
    origin: LearningOpportunityOrigin
    creator_user_id: str
    evaluation_id: int
    auto_evaluation_id: int
    smart_evaluation_id: int
    def __init__(self, learning_opportunity_id: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., transcript_sid: _Optional[int] = ..., agent_user_id: _Optional[str] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., status: _Optional[_Union[LearningOpportunityStatus, str]] = ..., origin: _Optional[_Union[LearningOpportunityOrigin, str]] = ..., creator_user_id: _Optional[str] = ..., evaluation_id: _Optional[int] = ..., auto_evaluation_id: _Optional[int] = ..., smart_evaluation_id: _Optional[int] = ...) -> None: ...

class CallIdentifier(_message.Message):
    __slots__ = ("sid", "type")
    SID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    sid: int
    type: _acd_pb2.CallType.Enum
    def __init__(self, sid: _Optional[int] = ..., type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...
