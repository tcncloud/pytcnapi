from annotations import authz_pb2 as _authz_pb2
from api.commons import call_pb2 as _call_pb2
from api.commons import sms_pb2 as _sms_pb2
from api.v0alpha import p3api_pb2 as _p3api_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DequeuePreviewRecordOrCallReq(_message.Message):
    __slots__ = ("timeout_minutes", "agent_session_sid")
    TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    timeout_minutes: int
    agent_session_sid: int
    def __init__(self, timeout_minutes: _Optional[int] = ..., agent_session_sid: _Optional[int] = ...) -> None: ...

class DequeuePreviewRecordOrCallRes(_message.Message):
    __slots__ = ("queue_name", "call", "record")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    call: _call_pb2.SimpleCallData
    record: _call_pb2.SimpleRecordData
    def __init__(self, queue_name: _Optional[str] = ..., call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., record: _Optional[_Union[_call_pb2.SimpleRecordData, _Mapping]] = ...) -> None: ...

class EnqueuePreviewRecordReq(_message.Message):
    __slots__ = ("record", "queue_name")
    RECORD_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    record: _call_pb2.SimpleRecordData
    queue_name: str
    def __init__(self, record: _Optional[_Union[_call_pb2.SimpleRecordData, _Mapping]] = ..., queue_name: _Optional[str] = ...) -> None: ...

class EnqueuePreviewRecordRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DequeueScrubbedCallForPreviewRecordReq(_message.Message):
    __slots__ = ("hunt_group_sid", "phone_number", "phone_num_index", "task_group_sid", "task_sid")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUM_INDEX_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    phone_number: str
    phone_num_index: int
    task_group_sid: int
    task_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., phone_number: _Optional[str] = ..., phone_num_index: _Optional[int] = ..., task_group_sid: _Optional[int] = ..., task_sid: _Optional[int] = ...) -> None: ...

class DequeueScrubbedCallForPreviewRecordRes(_message.Message):
    __slots__ = ("call",)
    CALL_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ...) -> None: ...

class ClearPreviewRecordReturnQueueReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearPreviewRecordReturnQueueRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnqueuePreviewDialCallReq(_message.Message):
    __slots__ = ("call", "queue_name")
    CALL_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    queue_name: str
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., queue_name: _Optional[str] = ...) -> None: ...

class EnqueuePreviewDialCallRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearManualDialQueueReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearManualDialQueueRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessManualDialCallReq(_message.Message):
    __slots__ = ("call",)
    CALL_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ...) -> None: ...

class ProcessManualDialCallRes(_message.Message):
    __slots__ = ("scrubbed_call",)
    SCRUBBED_CALL_FIELD_NUMBER: _ClassVar[int]
    scrubbed_call: _call_pb2.SimpleCallData
    def __init__(self, scrubbed_call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ...) -> None: ...

class DequeueCallForManualApprovalReq(_message.Message):
    __slots__ = ("hunt_group_sid", "agent_session_sid", "timeout_minutes")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    agent_session_sid: int
    timeout_minutes: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., agent_session_sid: _Optional[int] = ..., timeout_minutes: _Optional[int] = ...) -> None: ...

class DequeueCallForManualApprovalRes(_message.Message):
    __slots__ = ("call", "queue", "client_info", "client_info_template")
    CALL_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    queue: str
    client_info: _p3api_pb2.GetClientInfoDataRes
    client_info_template: _p3api_pb2.GetClientInfoDisplayTemplateRes
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., queue: _Optional[str] = ..., client_info: _Optional[_Union[_p3api_pb2.GetClientInfoDataRes, _Mapping]] = ..., client_info_template: _Optional[_Union[_p3api_pb2.GetClientInfoDisplayTemplateRes, _Mapping]] = ...) -> None: ...

class EnqueueManuallyApprovedCallReq(_message.Message):
    __slots__ = ("call",)
    CALL_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ...) -> None: ...

class EnqueueManuallyApprovedCallRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnqueueManuallyRejectedCallReq(_message.Message):
    __slots__ = ("call",)
    CALL_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ...) -> None: ...

class EnqueueManuallyRejectedCallRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequeueManuallyApprovedCallReq(_message.Message):
    __slots__ = ("call", "queue_name")
    CALL_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    queue_name: str
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., queue_name: _Optional[str] = ...) -> None: ...

class RequeueManuallyApprovedCallRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnqueueManuallyApprovedSmsReq(_message.Message):
    __slots__ = ("sms",)
    SMS_FIELD_NUMBER: _ClassVar[int]
    sms: _sms_pb2.SimpleSmsMamData
    def __init__(self, sms: _Optional[_Union[_sms_pb2.SimpleSmsMamData, _Mapping]] = ...) -> None: ...

class EnqueueManuallyApprovedSmsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnqueueManuallyRejectedSmsReq(_message.Message):
    __slots__ = ("sms",)
    SMS_FIELD_NUMBER: _ClassVar[int]
    sms: _sms_pb2.SimpleSmsMamData
    def __init__(self, sms: _Optional[_Union[_sms_pb2.SimpleSmsMamData, _Mapping]] = ...) -> None: ...

class EnqueueManuallyRejectedSmsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequeueManuallyApprovedSmsReq(_message.Message):
    __slots__ = ("sms", "queue_name")
    SMS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    sms: _sms_pb2.SimpleSmsMamData
    queue_name: str
    def __init__(self, sms: _Optional[_Union[_sms_pb2.SimpleSmsMamData, _Mapping]] = ..., queue_name: _Optional[str] = ...) -> None: ...

class RequeueManuallyApprovedSmsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DequeueSmsMamForManualApprovalReq(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class DequeueSmsMamForManualApprovalRes(_message.Message):
    __slots__ = ("sms", "queue")
    SMS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    sms: _sms_pb2.SimpleSmsMamData
    queue: str
    def __init__(self, sms: _Optional[_Union[_sms_pb2.SimpleSmsMamData, _Mapping]] = ..., queue: _Optional[str] = ...) -> None: ...
