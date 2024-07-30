from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PopAccountReq(_message.Message):
    __slots__ = ("record_id", "user_id", "alternate_id", "call_sid", "call_type")
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    record_id: str
    user_id: str
    alternate_id: str
    call_sid: int
    call_type: str
    def __init__(self, record_id: _Optional[str] = ..., user_id: _Optional[str] = ..., alternate_id: _Optional[str] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[str] = ...) -> None: ...

class PopAccountRes(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ASYNC_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    def __init__(self, job_id: _Optional[int] = ..., **kwargs) -> None: ...
