from api.commons.audit import event_types_pb2 as _event_types_pb2
from services.billing.entities.v1alpha1 import history_pb2 as _history_pb2
from services.billing.entities.v1alpha1 import matching_pb2 as _matching_pb2
from services.billing.entities.v1alpha1 import rates_pb2 as _rates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRateHistoryRequest(_message.Message):
    __slots__ = ("org_id", "group_ids")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRateHistoryResponse(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_history_pb2.RateHistoryItem]
    def __init__(self, history: _Optional[_Iterable[_Union[_history_pb2.RateHistoryItem, _Mapping]]] = ...) -> None: ...
