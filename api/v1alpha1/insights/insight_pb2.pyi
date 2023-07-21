from api.commons import insights_pb2 as _insights_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Insight(_message.Message):
    __slots__ = ["insight_id", "name", "description", "insight_type", "insight_version", "body", "insight_permission_type"]
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_VERSION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    name: str
    description: str
    insight_type: _insights_pb2.InsightType
    insight_version: int
    body: str
    insight_permission_type: _insights_pb2.InsightPermissionType
    def __init__(self, insight_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., insight_type: _Optional[_Union[_insights_pb2.InsightType, str]] = ..., insight_version: _Optional[int] = ..., body: _Optional[str] = ..., insight_permission_type: _Optional[_Union[_insights_pb2.InsightPermissionType, str]] = ...) -> None: ...

class CreateInsightRequest(_message.Message):
    __slots__ = ["insight"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class CreateInsightResponse(_message.Message):
    __slots__ = ["insight"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class ListInsightsRequest(_message.Message):
    __slots__ = ["insight_permission_types"]
    INSIGHT_PERMISSION_TYPES_FIELD_NUMBER: _ClassVar[int]
    insight_permission_types: _containers.RepeatedScalarFieldContainer[_insights_pb2.InsightPermissionType]
    def __init__(self, insight_permission_types: _Optional[_Iterable[_Union[_insights_pb2.InsightPermissionType, str]]] = ...) -> None: ...

class ListInsightsResponse(_message.Message):
    __slots__ = ["insights"]
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]] = ...) -> None: ...

class UpdateInsightRequest(_message.Message):
    __slots__ = ["insight", "update_mask"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInsightResponse(_message.Message):
    __slots__ = ["insight"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class DeleteInsightRequest(_message.Message):
    __slots__ = ["insight_id"]
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    def __init__(self, insight_id: _Optional[int] = ...) -> None: ...

class DeleteInsightResponse(_message.Message):
    __slots__ = ["insight"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetInsightRequest(_message.Message):
    __slots__ = ["insight_id"]
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    def __init__(self, insight_id: _Optional[int] = ...) -> None: ...

class GetInsightResponse(_message.Message):
    __slots__ = ["insight"]
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetVfsSchemaRequest(_message.Message):
    __slots__ = ["alias_name"]
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    def __init__(self, alias_name: _Optional[str] = ...) -> None: ...

class GetVfsSchemaResponse(_message.Message):
    __slots__ = ["fields", "vfs_description"]
    class Field(_message.Message):
        __slots__ = ["column_name", "column_type", "column_description"]
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        column_type: _insights_pb2.InsightVfsSchemaType
        column_description: str
        def __init__(self, column_name: _Optional[str] = ..., column_type: _Optional[_Union[_insights_pb2.InsightVfsSchemaType, str]] = ..., column_description: _Optional[str] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    VFS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[GetVfsSchemaResponse.Field]
    vfs_description: str
    def __init__(self, fields: _Optional[_Iterable[_Union[GetVfsSchemaResponse.Field, _Mapping]]] = ..., vfs_description: _Optional[str] = ...) -> None: ...

class ListVfsesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListVfsesResponse(_message.Message):
    __slots__ = ["aliases"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, aliases: _Optional[_Iterable[str]] = ...) -> None: ...
