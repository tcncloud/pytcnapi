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
    __slots__ = ("org_id", "event_types", "config_types", "matching_rules", "matching_shas")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPES_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULES_FIELD_NUMBER: _ClassVar[int]
    MATCHING_SHAS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    event_types: _containers.RepeatedScalarFieldContainer[_event_types_pb2.EventType]
    config_types: _containers.RepeatedScalarFieldContainer[_rates_pb2.RateDefinitionConfigType]
    matching_rules: _containers.RepeatedScalarFieldContainer[_matching_pb2.MatchingRule]
    matching_shas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., event_types: _Optional[_Iterable[_Union[_event_types_pb2.EventType, str]]] = ..., config_types: _Optional[_Iterable[_Union[_rates_pb2.RateDefinitionConfigType, str]]] = ..., matching_rules: _Optional[_Iterable[_Union[_matching_pb2.MatchingRule, str]]] = ..., matching_shas: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRateHistoryResponse(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_history_pb2.RateHistoryItem]
    def __init__(self, history: _Optional[_Iterable[_Union[_history_pb2.RateHistoryItem, _Mapping]]] = ...) -> None: ...
