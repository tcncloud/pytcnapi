import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComplianceRndQueryEvent(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DATE_LAST_CONTACT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    phone_number: str
    result: str
    date_last_contact: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., phone_number: _Optional[str] = ..., result: _Optional[str] = ..., date_last_contact: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
