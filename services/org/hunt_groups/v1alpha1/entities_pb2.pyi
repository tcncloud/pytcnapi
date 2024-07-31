from api.commons.org import huntgroup_pb2 as _huntgroup_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExileLink(_message.Message):
    __slots__ = ("parameter_sid", "hunt_group_sid", "name", "description", "order", "inbound_data", "outbound_data")
    PARAMETER_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    INBOUND_DATA_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_DATA_FIELD_NUMBER: _ClassVar[int]
    parameter_sid: int
    hunt_group_sid: int
    name: str
    description: str
    order: int
    inbound_data: ExileLinkData
    outbound_data: ExileLinkData
    def __init__(self, parameter_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., order: _Optional[int] = ..., inbound_data: _Optional[_Union[ExileLinkData, _Mapping]] = ..., outbound_data: _Optional[_Union[ExileLinkData, _Mapping]] = ...) -> None: ...

class ExileLinkData(_message.Message):
    __slots__ = ("record_id", "alternate_id")
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_ID_FIELD_NUMBER: _ClassVar[int]
    record_id: ExileLinkParameter
    alternate_id: ExileLinkParameter
    def __init__(self, record_id: _Optional[_Union[ExileLinkParameter, _Mapping]] = ..., alternate_id: _Optional[_Union[ExileLinkParameter, _Mapping]] = ...) -> None: ...

class ExileLinkParameter(_message.Message):
    __slots__ = ("contact_field_sid", "helper_value", "parameter_source_type")
    CONTACT_FIELD_SID_FIELD_NUMBER: _ClassVar[int]
    HELPER_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contact_field_sid: int
    helper_value: str
    parameter_source_type: _huntgroup_pb2.ParameterSourceType
    def __init__(self, contact_field_sid: _Optional[int] = ..., helper_value: _Optional[str] = ..., parameter_source_type: _Optional[_Union[_huntgroup_pb2.ParameterSourceType, str]] = ...) -> None: ...

class ListHuntGroupExileLinksRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupExileLinksResponse(_message.Message):
    __slots__ = ("exile_links",)
    EXILE_LINKS_FIELD_NUMBER: _ClassVar[int]
    exile_links: _containers.RepeatedCompositeFieldContainer[ExileLink]
    def __init__(self, exile_links: _Optional[_Iterable[_Union[ExileLink, _Mapping]]] = ...) -> None: ...
