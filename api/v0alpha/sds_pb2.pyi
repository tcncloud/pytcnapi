from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAgentResponseDataReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class GetAgentResponseDataRes(_message.Message):
    __slots__ = ["call_sid", "call_type", "responses"]
    class ResponsesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    responses: _containers.ScalarMap[str, str]
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., responses: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetCallReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class UpdateVoicemailBoxReq(_message.Message):
    __slots__ = ["call_sid", "call_type", "pbx_extension"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    pbx_extension: str
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., pbx_extension: _Optional[str] = ...) -> None: ...

class UpdateVoicemailBoxRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CallObject(_message.Message):
    __slots__ = ["oid", "call_sid", "call_type", "updated", "skills", "recording_file", "updated_date", "src_number", "dst_number", "caller_id_name", "agent_worker", "events", "call_data", "agent_response_data", "recorded", "connected", "suspended", "disconnect_reason", "voicemailed", "voicemail_box", "originated", "folder", "rtp_info"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class AgentResponseDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_DATE_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_WORKER_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    RECORDED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_REASON_FIELD_NUMBER: _ClassVar[int]
    VOICEMAILED_FIELD_NUMBER: _ClassVar[int]
    VOICEMAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    ORIGINATED_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    RTP_INFO_FIELD_NUMBER: _ClassVar[int]
    oid: str
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    updated: int
    skills: _containers.ScalarMap[str, bool]
    recording_file: str
    updated_date: _timestamp_pb2.Timestamp
    src_number: str
    dst_number: str
    caller_id_name: str
    agent_worker: str
    events: _containers.RepeatedScalarFieldContainer[str]
    call_data: str
    agent_response_data: _containers.ScalarMap[str, str]
    recorded: bool
    connected: bool
    suspended: bool
    disconnect_reason: str
    voicemailed: bool
    voicemail_box: str
    originated: str
    folder: str
    rtp_info: str
    def __init__(self, oid: _Optional[str] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., updated: _Optional[int] = ..., skills: _Optional[_Mapping[str, bool]] = ..., recording_file: _Optional[str] = ..., updated_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., src_number: _Optional[str] = ..., dst_number: _Optional[str] = ..., caller_id_name: _Optional[str] = ..., agent_worker: _Optional[str] = ..., events: _Optional[_Iterable[str]] = ..., call_data: _Optional[str] = ..., agent_response_data: _Optional[_Mapping[str, str]] = ..., recorded: bool = ..., connected: bool = ..., suspended: bool = ..., disconnect_reason: _Optional[str] = ..., voicemailed: bool = ..., voicemail_box: _Optional[str] = ..., originated: _Optional[str] = ..., folder: _Optional[str] = ..., rtp_info: _Optional[str] = ...) -> None: ...

class UpdateAgentResponseDataReq(_message.Message):
    __slots__ = ["call_sid", "call_type", "responses"]
    class ResponsesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    responses: _containers.ScalarMap[str, str]
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., responses: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdateAgentResponseDataRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
