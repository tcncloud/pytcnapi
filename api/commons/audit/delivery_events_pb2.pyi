import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryFailureEvent(_message.Message):
    __slots__ = ()
    DELIVERY_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_TIME_FIELD_NUMBER: _ClassVar[int]
    FAILURE_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    delivery_definition_name: int
    org_id: str
    transaction_sid: int
    attachment_names: _containers.RepeatedScalarFieldContainer[str]
    failure_time: _timestamp_pb2.Timestamp
    failure_error_message: str
    definition: str
    original_payload: str
    def __init__(self, delivery_definition_name: _Optional[int] = ..., org_id: _Optional[str] = ..., transaction_sid: _Optional[int] = ..., attachment_names: _Optional[_Iterable[str]] = ..., failure_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., failure_error_message: _Optional[str] = ..., definition: _Optional[str] = ..., original_payload: _Optional[str] = ...) -> None: ...

class DeliverySuccessEvent(_message.Message):
    __slots__ = ()
    DELIVERY_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    delivery_definition_name: str
    org_id: str
    transaction_sid: int
    attachment_names: _containers.RepeatedScalarFieldContainer[str]
    success_time: _timestamp_pb2.Timestamp
    success_message: str
    def __init__(self, delivery_definition_name: _Optional[str] = ..., org_id: _Optional[str] = ..., transaction_sid: _Optional[int] = ..., attachment_names: _Optional[_Iterable[str]] = ..., success_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., success_message: _Optional[str] = ...) -> None: ...
