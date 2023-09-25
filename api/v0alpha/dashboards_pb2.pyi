from annotations import authz_pb2 as _authz_pb2
from api.commons import org_pb2 as _org_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublishDashboardRequest(_message.Message):
    __slots__ = ["resource_id", "destination_resource_id"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    destination_resource_id: str
    def __init__(self, resource_id: _Optional[str] = ..., destination_resource_id: _Optional[str] = ...) -> None: ...

class PublishDashboardResponse(_message.Message):
    __slots__ = ["resource_id"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class ListDashboardsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListDashboardsResponse(_message.Message):
    __slots__ = ["dashboard_summaries"]
    DASHBOARD_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    dashboard_summaries: _containers.RepeatedCompositeFieldContainer[DashboardSummary]
    def __init__(self, dashboard_summaries: _Optional[_Iterable[_Union[DashboardSummary, _Mapping]]] = ...) -> None: ...

class DashboardSummary(_message.Message):
    __slots__ = ["dashboard_id", "title", "description", "panel_count", "resource_id", "standard_dashboard"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PANEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    description: str
    panel_count: int
    resource_id: str
    standard_dashboard: bool
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., panel_count: _Optional[int] = ..., resource_id: _Optional[str] = ..., standard_dashboard: bool = ...) -> None: ...

class GetDefaultDashboardRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetDefaultDashboardRequest(_message.Message):
    __slots__ = ["dashboard_id", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class ListProductTypesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListProductTypesResult(_message.Message):
    __slots__ = ["types"]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedCompositeFieldContainer[ProductType]
    def __init__(self, types: _Optional[_Iterable[_Union[ProductType, _Mapping]]] = ...) -> None: ...

class ProductType(_message.Message):
    __slots__ = ["name", "id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteDashboardRequest(_message.Message):
    __slots__ = ["dashboard_id", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class GetDashboardRequest(_message.Message):
    __slots__ = ["dashboard_id", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class CreateDashboardRequest(_message.Message):
    __slots__ = ["title", "description", "layout", "view", "type"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    layout: DashboardLayout
    view: DashboardView
    type: DashboardType
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., layout: _Optional[_Union[DashboardLayout, _Mapping]] = ..., view: _Optional[_Union[DashboardView, _Mapping]] = ..., type: _Optional[_Union[DashboardType, _Mapping]] = ...) -> None: ...

class CreateDashboardResponse(_message.Message):
    __slots__ = ["dashboard_id", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class DashboardLayout(_message.Message):
    __slots__ = ["panels"]
    PANELS_FIELD_NUMBER: _ClassVar[int]
    panels: _containers.RepeatedCompositeFieldContainer[DashboardPanel]
    def __init__(self, panels: _Optional[_Iterable[_Union[DashboardPanel, _Mapping]]] = ...) -> None: ...

class DashboardPanel(_message.Message):
    __slots__ = ["panel_source", "row_length", "column_length", "row_start", "column_start"]
    PANEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ROW_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ROW_START_FIELD_NUMBER: _ClassVar[int]
    COLUMN_START_FIELD_NUMBER: _ClassVar[int]
    panel_source: PanelSource
    row_length: int
    column_length: int
    row_start: int
    column_start: int
    def __init__(self, panel_source: _Optional[_Union[PanelSource, _Mapping]] = ..., row_length: _Optional[int] = ..., column_length: _Optional[int] = ..., row_start: _Optional[int] = ..., column_start: _Optional[int] = ...) -> None: ...

class PanelSource(_message.Message):
    __slots__ = ["insight_id", "legacy_insight_id"]
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: str
    legacy_insight_id: str
    def __init__(self, insight_id: _Optional[str] = ..., legacy_insight_id: _Optional[str] = ...) -> None: ...

class Dashboard(_message.Message):
    __slots__ = ["dashboard_id", "title", "description", "layout", "view", "type", "resource_id", "standard_dashboard"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    description: str
    layout: DashboardLayout
    view: DashboardView
    type: DashboardType
    resource_id: str
    standard_dashboard: bool
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., layout: _Optional[_Union[DashboardLayout, _Mapping]] = ..., view: _Optional[_Union[DashboardView, _Mapping]] = ..., type: _Optional[_Union[DashboardType, _Mapping]] = ..., resource_id: _Optional[str] = ..., standard_dashboard: bool = ...) -> None: ...

class DashboardType(_message.Message):
    __slots__ = ["historic", "real_time"]
    HISTORIC_FIELD_NUMBER: _ClassVar[int]
    REAL_TIME_FIELD_NUMBER: _ClassVar[int]
    historic: HistoricConfig
    real_time: RealTimeConfig
    def __init__(self, historic: _Optional[_Union[HistoricConfig, _Mapping]] = ..., real_time: _Optional[_Union[RealTimeConfig, _Mapping]] = ...) -> None: ...

class HistoricConfig(_message.Message):
    __slots__ = ["time_span_simple", "time_span_range", "time_zone"]
    TIME_SPAN_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    TIME_SPAN_RANGE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    time_span_simple: TimeSpan.Interval
    time_span_range: TimeSpan.Range
    time_zone: _org_pb2.TimeZone
    def __init__(self, time_span_simple: _Optional[_Union[TimeSpan.Interval, str]] = ..., time_span_range: _Optional[_Union[TimeSpan.Range, _Mapping]] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class RealTimeConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateDashboardRequest(_message.Message):
    __slots__ = ["dashboard_id", "title", "description", "layout", "view", "type", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    description: str
    layout: DashboardLayout
    view: DashboardView
    type: DashboardType
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., layout: _Optional[_Union[DashboardLayout, _Mapping]] = ..., view: _Optional[_Union[DashboardView, _Mapping]] = ..., type: _Optional[_Union[DashboardType, _Mapping]] = ..., resource_id: _Optional[str] = ...) -> None: ...

class UpdateDashboardTitleAndDescriptionRequest(_message.Message):
    __slots__ = ["dashboard_id", "title", "description", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    description: str
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., resource_id: _Optional[str] = ...) -> None: ...

class UpdateDashboardLayoutRequest(_message.Message):
    __slots__ = ["dashboard_id", "layout", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    layout: DashboardLayout
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., layout: _Optional[_Union[DashboardLayout, _Mapping]] = ..., resource_id: _Optional[str] = ...) -> None: ...

class UpdateDashboardViewRequest(_message.Message):
    __slots__ = ["dashboard_id", "view", "resource_id"]
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    view: DashboardView
    resource_id: str
    def __init__(self, dashboard_id: _Optional[str] = ..., view: _Optional[_Union[DashboardView, _Mapping]] = ..., resource_id: _Optional[str] = ...) -> None: ...

class DashboardView(_message.Message):
    __slots__ = ["org_ids"]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeSpan(_message.Message):
    __slots__ = []
    class Interval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        TODAY: _ClassVar[TimeSpan.Interval]
        YESTERDAY: _ClassVar[TimeSpan.Interval]
        LAST_30_DAYS: _ClassVar[TimeSpan.Interval]
        MONTH_TO_DATE: _ClassVar[TimeSpan.Interval]
        LAST_2_WEEKS: _ClassVar[TimeSpan.Interval]
        THIS_WEEK: _ClassVar[TimeSpan.Interval]
        THIS_MONTH: _ClassVar[TimeSpan.Interval]
        THIS_DAY_LAST_WEEK: _ClassVar[TimeSpan.Interval]
        PREVIOUS_MONTH: _ClassVar[TimeSpan.Interval]
    TODAY: TimeSpan.Interval
    YESTERDAY: TimeSpan.Interval
    LAST_30_DAYS: TimeSpan.Interval
    MONTH_TO_DATE: TimeSpan.Interval
    LAST_2_WEEKS: TimeSpan.Interval
    THIS_WEEK: TimeSpan.Interval
    THIS_MONTH: TimeSpan.Interval
    THIS_DAY_LAST_WEEK: TimeSpan.Interval
    PREVIOUS_MONTH: TimeSpan.Interval
    class Range(_message.Message):
        __slots__ = ["start", "end"]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: _timestamp_pb2.Timestamp
        end: _timestamp_pb2.Timestamp
        def __init__(self, start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
