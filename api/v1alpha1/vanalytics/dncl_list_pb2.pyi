from api.commons import compliance_pb2 as _compliance_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DnclExpirePeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DNCL_EXPIRE_PERIOD_HOUR: _ClassVar[DnclExpirePeriod]
    DNCL_EXPIRE_PERIOD_DAY: _ClassVar[DnclExpirePeriod]
    DNCL_EXPIRE_PERIOD_WEEK: _ClassVar[DnclExpirePeriod]
    DNCL_EXPIRE_PERIOD_MONTH: _ClassVar[DnclExpirePeriod]
DNCL_EXPIRE_PERIOD_HOUR: DnclExpirePeriod
DNCL_EXPIRE_PERIOD_DAY: DnclExpirePeriod
DNCL_EXPIRE_PERIOD_WEEK: DnclExpirePeriod
DNCL_EXPIRE_PERIOD_MONTH: DnclExpirePeriod

class DnclList(_message.Message):
    __slots__ = ("list_id", "content_type", "expire_period", "expire_offset", "agent_response_key")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_KEY_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    content_type: _compliance_pb2.ContentType
    expire_period: DnclExpirePeriod
    expire_offset: int
    agent_response_key: str
    def __init__(self, list_id: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., expire_period: _Optional[_Union[DnclExpirePeriod, str]] = ..., expire_offset: _Optional[int] = ..., agent_response_key: _Optional[str] = ...) -> None: ...
