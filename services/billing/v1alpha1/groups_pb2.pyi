from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.entities.v1alpha1 import groups_pb2 as _groups_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRateDefinitionGroupRequest(_message.Message):
    __slots__ = ["rate_definition_group_id", "rate_definition_group"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_GROUP_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    rate_definition_group: _groups_pb2.RateDefinitionGroup
    def __init__(self, rate_definition_group_id: _Optional[str] = ..., rate_definition_group: _Optional[_Union[_groups_pb2.RateDefinitionGroup, _Mapping]] = ...) -> None: ...

class CreateRateDefinitionGroupResponse(_message.Message):
    __slots__ = ["rate_definition_group_id"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    def __init__(self, rate_definition_group_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionGroupRequest(_message.Message):
    __slots__ = ["rate_definition_group_id"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    def __init__(self, rate_definition_group_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRateDefinitionGroupRequest(_message.Message):
    __slots__ = ["rate_definition_group_id"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    def __init__(self, rate_definition_group_id: _Optional[str] = ...) -> None: ...

class GetRateDefinitionGroupResponse(_message.Message):
    __slots__ = ["rate_definition_group"]
    RATE_DEFINITION_GROUP_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group: _groups_pb2.RateDefinitionGroup
    def __init__(self, rate_definition_group: _Optional[_Union[_groups_pb2.RateDefinitionGroup, _Mapping]] = ...) -> None: ...

class ListRateDefinitionGroupsRequest(_message.Message):
    __slots__ = ["rate_definition_group_id", "filter", "fields", "sort", "page"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, rate_definition_group_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListRateDefinitionGroupsResponse(_message.Message):
    __slots__ = ["rate_definition_groups", "token"]
    RATE_DEFINITION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    rate_definition_groups: _containers.RepeatedCompositeFieldContainer[_groups_pb2.RateDefinitionGroup]
    token: str
    def __init__(self, rate_definition_groups: _Optional[_Iterable[_Union[_groups_pb2.RateDefinitionGroup, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateRateDefinitionGroupRequest(_message.Message):
    __slots__ = ["rate_definition_group_id", "rate_definition_group", "update_fields"]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    rate_definition_group_id: str
    rate_definition_group: _groups_pb2.RateDefinitionGroup
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, rate_definition_group_id: _Optional[str] = ..., rate_definition_group: _Optional[_Union[_groups_pb2.RateDefinitionGroup, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRateDefinitionGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
