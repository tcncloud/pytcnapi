from api.commons.audit import event_types_pb2 as _event_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import config_pb2 as _config_pb2
from services.billing.entities.v1alpha1 import matching_pb2 as _matching_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateDefinitionGroup(_message.Message):
    __slots__ = ["rate_definition_group_id", "event_type", "config_type", "matching_rule", "matching_config", "create_time", "update_time", "delete_time"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    event_type: _event_types_pb2.EventType
    config_type: _config_pb2.RateDefinitionConfigType
    matching_rule: _matching_pb2.MatchingRule
    matching_config: _matching_pb2.MatchingConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    def __init__(self, rate_definition_group_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., config_type: _Optional[_Union[_config_pb2.RateDefinitionConfigType, str]] = ..., matching_rule: _Optional[_Union[_matching_pb2.MatchingRule, str]] = ..., matching_config: _Optional[_Union[_matching_pb2.MatchingConfig, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
