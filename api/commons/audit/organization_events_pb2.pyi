from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AccessTokensExpiringEvent(_message.Message):
    __slots__ = ("org_id", "report")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    report: str
    def __init__(self, org_id: _Optional[str] = ..., report: _Optional[str] = ...) -> None: ...
