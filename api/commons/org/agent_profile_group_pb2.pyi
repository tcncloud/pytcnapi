from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentProfileGroup(_message.Message):
    __slots__ = ("id", "org_id", "name", "priority_groups", "last_updated", "default_group")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GROUP_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    name: str
    priority_groups: _containers.RepeatedCompositeFieldContainer[PriorityGroup]
    last_updated: _timestamp_pb2.Timestamp
    default_group: bool
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., priority_groups: _Optional[_Iterable[_Union[PriorityGroup, _Mapping]]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., default_group: bool = ...) -> None: ...

class PriorityGroup(_message.Message):
    __slots__ = ("threshold", "channel_type")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    channel_type: _omnichannel_pb2.ChannelType
    def __init__(self, threshold: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ...) -> None: ...
