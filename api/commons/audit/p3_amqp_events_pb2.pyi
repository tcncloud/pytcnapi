import datetime

from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class P3AMQPCallResultEvent(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_CALL_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OF_CALL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DTMF_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    result: int
    campaign_sid: int
    time_of_call: _timestamp_pb2.Timestamp
    call_type: _acd_pb2.CallType.Enum
    client_sid: int
    duration: _duration_pb2.Duration
    group_description: str
    end_time_of_call: _timestamp_pb2.Timestamp
    phone_number: str
    task_sid: int
    call_sid: int
    caller_id: str
    dtmf_responses: str
    def __init__(self, result: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., time_of_call: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., client_sid: _Optional[int] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., group_description: _Optional[str] = ..., end_time_of_call: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., phone_number: _Optional[str] = ..., task_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., caller_id: _Optional[str] = ..., dtmf_responses: _Optional[str] = ...) -> None: ...

class P3AMQPAgentResponseEvent(_message.Message):
    __slots__ = ()
    class ResponsesMapEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHODS_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_MAP_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    agent_sid: int
    hunt_group_sid: int
    call_type: _acd_pb2.CallType.Enum
    campaign_sid: int
    call_sid: int
    aggregation_methods: _containers.RepeatedScalarFieldContainer[str]
    agent_name: str
    hunt_group_name: str
    responses_map: _containers.ScalarMap[str, str]
    def __init__(self, client_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., campaign_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., aggregation_methods: _Optional[_Iterable[str]] = ..., agent_name: _Optional[str] = ..., hunt_group_name: _Optional[str] = ..., responses_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
