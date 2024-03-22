from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import rates_pb2 as _rates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateHistoryItem(_message.Message):
    __slots__ = ("start_date", "end_date", "rates")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    rates: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    def __init__(self, start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rates: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ...) -> None: ...
