from annotations import authz_pb2 as _authz_pb2
from api.commons import ana_pb2 as _ana_pb2
from api.commons import ana_charts_pb2 as _ana_charts_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetWeeksReq(_message.Message):
    __slots__ = ("weeks", "org_id")
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    weeks: int
    org_id: str
    def __init__(self, weeks: _Optional[int] = ..., org_id: _Optional[str] = ...) -> None: ...

class SetWeeksRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetHomeDashboardReq(_message.Message):
    __slots__ = ("home_dashboard",)
    HOME_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    home_dashboard: str
    def __init__(self, home_dashboard: _Optional[str] = ...) -> None: ...

class SetHomeDashboardRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetDefaultTimeFilterReq(_message.Message):
    __slots__ = ("default_time_filter",)
    DEFAULT_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    default_time_filter: str
    def __init__(self, default_time_filter: _Optional[str] = ...) -> None: ...

class SetDefaultTimeFilterRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetDefaultDashboardReq(_message.Message):
    __slots__ = ("dashboard_id",)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    def __init__(self, dashboard_id: _Optional[str] = ...) -> None: ...

class SetDefaultDashboardRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAccountReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpecifiedAccountReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GenerateMonthlyBillingReq(_message.Message):
    __slots__ = ("month", "year")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    month: int
    year: int
    def __init__(self, month: _Optional[int] = ..., year: _Optional[int] = ...) -> None: ...

class GenerateMonthlyBillingRes(_message.Message):
    __slots__ = ("month", "year", "url")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    month: int
    year: int
    url: str
    def __init__(self, month: _Optional[int] = ..., year: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class AnaAccount(_message.Message):
    __slots__ = ("uuid", "p3_client_sid", "registration_date", "price_per_doc", "ana_time_zone", "home_dashboard", "adoptable", "default_time_filter", "neo_home_dashboard", "current_month_max_doc_count", "current_weeks")
    UUID_FIELD_NUMBER: _ClassVar[int]
    P3_CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_DOC_FIELD_NUMBER: _ClassVar[int]
    ANA_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    HOME_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    ADOPTABLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    NEO_HOME_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MONTH_MAX_DOC_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_WEEKS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    p3_client_sid: int
    registration_date: _timestamp_pb2.Timestamp
    price_per_doc: float
    ana_time_zone: _ana_pb2.AnaTimeZone
    home_dashboard: str
    adoptable: bool
    default_time_filter: str
    neo_home_dashboard: str
    current_month_max_doc_count: int
    current_weeks: int
    def __init__(self, uuid: _Optional[str] = ..., p3_client_sid: _Optional[int] = ..., registration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price_per_doc: _Optional[float] = ..., ana_time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ..., home_dashboard: _Optional[str] = ..., adoptable: bool = ..., default_time_filter: _Optional[str] = ..., neo_home_dashboard: _Optional[str] = ..., current_month_max_doc_count: _Optional[int] = ..., current_weeks: _Optional[int] = ...) -> None: ...

class SetCustomReportsEnabledReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCustomReportsEnabledRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterAccountReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class View(_message.Message):
    __slots__ = ("client_sid", "weeks")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    weeks: int
    def __init__(self, client_sid: _Optional[int] = ..., weeks: _Optional[int] = ...) -> None: ...

class AccountDataVisibility(_message.Message):
    __slots__ = ("viewer", "views")
    VIEWER_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    viewer: int
    views: _containers.RepeatedCompositeFieldContainer[View]
    def __init__(self, viewer: _Optional[int] = ..., views: _Optional[_Iterable[_Union[View, _Mapping]]] = ...) -> None: ...

class DataVisibility(_message.Message):
    __slots__ = ("visibilities",)
    VISIBILITIES_FIELD_NUMBER: _ClassVar[int]
    visibilities: _containers.RepeatedCompositeFieldContainer[AccountDataVisibility]
    def __init__(self, visibilities: _Optional[_Iterable[_Union[AccountDataVisibility, _Mapping]]] = ...) -> None: ...

class IndexVisibility(_message.Message):
    __slots__ = ("client_sid", "year", "week", "viewers")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    year: int
    week: int
    viewers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, client_sid: _Optional[int] = ..., year: _Optional[int] = ..., week: _Optional[int] = ..., viewers: _Optional[_Iterable[int]] = ...) -> None: ...

class IndicesVisibility(_message.Message):
    __slots__ = ("visibilities",)
    VISIBILITIES_FIELD_NUMBER: _ClassVar[int]
    visibilities: _containers.RepeatedCompositeFieldContainer[IndexVisibility]
    def __init__(self, visibilities: _Optional[_Iterable[_Union[IndexVisibility, _Mapping]]] = ...) -> None: ...

class GetVisualizationsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateVizDataByIdReq(_message.Message):
    __slots__ = ("visualization_id", "time_from", "time_to", "time_zone", "included_org_ids")
    VISUALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    visualization_id: str
    time_from: str
    time_to: str
    time_zone: str
    included_org_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, visualization_id: _Optional[str] = ..., time_from: _Optional[str] = ..., time_to: _Optional[str] = ..., time_zone: _Optional[str] = ..., included_org_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateVizDataByIdRes(_message.Message):
    __slots__ = ("json_string",)
    JSON_STRING_FIELD_NUMBER: _ClassVar[int]
    json_string: str
    def __init__(self, json_string: _Optional[str] = ...) -> None: ...

class GetDashboardsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpecifiedVisualizationsReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class Visualizations(_message.Message):
    __slots__ = ("visualizations",)
    VISUALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    visualizations: _containers.RepeatedCompositeFieldContainer[Visualization]
    def __init__(self, visualizations: _Optional[_Iterable[_Union[Visualization, _Mapping]]] = ...) -> None: ...

class Visualization(_message.Message):
    __slots__ = ("id", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class TimeFilter(_message.Message):
    __slots__ = ("relative", "absolute", "quick")
    RELATIVE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    QUICK_FIELD_NUMBER: _ClassVar[int]
    relative: Relative
    absolute: Absolute
    quick: Quick
    def __init__(self, relative: _Optional[_Union[Relative, _Mapping]] = ..., absolute: _Optional[_Union[Absolute, _Mapping]] = ..., quick: _Optional[_Union[Quick, _Mapping]] = ...) -> None: ...

class Quick(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: str
    def __init__(self, label: _Optional[str] = ...) -> None: ...

class Relative(_message.Message):
    __slots__ = ("to_quantity_time", "to_filter_by", "to_round", "from_quantity_time", "from_filter_by", "from_round")
    TO_QUANTITY_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_FILTER_BY_FIELD_NUMBER: _ClassVar[int]
    TO_ROUND_FIELD_NUMBER: _ClassVar[int]
    FROM_QUANTITY_TIME_FIELD_NUMBER: _ClassVar[int]
    FROM_FILTER_BY_FIELD_NUMBER: _ClassVar[int]
    FROM_ROUND_FIELD_NUMBER: _ClassVar[int]
    to_quantity_time: int
    to_filter_by: _ana_pb2.FilterBy
    to_round: bool
    from_quantity_time: int
    from_filter_by: _ana_pb2.FilterBy
    from_round: bool
    def __init__(self, to_quantity_time: _Optional[int] = ..., to_filter_by: _Optional[_Union[_ana_pb2.FilterBy, str]] = ..., to_round: bool = ..., from_quantity_time: _Optional[int] = ..., from_filter_by: _Optional[_Union[_ana_pb2.FilterBy, str]] = ..., from_round: bool = ...) -> None: ...

class Absolute(_message.Message):
    __slots__ = ("to",)
    TO_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    def __init__(self, to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class DeleteDashboardReq(_message.Message):
    __slots__ = ("dashboard_id",)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    def __init__(self, dashboard_id: _Optional[str] = ...) -> None: ...

class DeleteDashboardRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashboardHistoryEntry(_message.Message):
    __slots__ = ("dashboard_id", "title", "editing_user_id", "user_name", "create_time")
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EDITING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    editing_user_id: str
    user_name: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., editing_user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDashboardHistoryReq(_message.Message):
    __slots__ = ("dashboard_id",)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    def __init__(self, dashboard_id: _Optional[str] = ...) -> None: ...

class GetDashboardHistoryRes(_message.Message):
    __slots__ = ("dashboard_history_entries",)
    DASHBOARD_HISTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    dashboard_history_entries: _containers.RepeatedCompositeFieldContainer[DashboardHistoryEntry]
    def __init__(self, dashboard_history_entries: _Optional[_Iterable[_Union[DashboardHistoryEntry, _Mapping]]] = ...) -> None: ...

class GetVisibilityReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTimeZoneReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetTimeZoneReq(_message.Message):
    __slots__ = ("ana_time_zone",)
    ANA_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ana_time_zone: _ana_pb2.AnaTimeZone
    def __init__(self, ana_time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ...) -> None: ...

class SetTimeZoneRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimeZone(_message.Message):
    __slots__ = ("ana_time_zone",)
    ANA_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ana_time_zone: _ana_pb2.AnaTimeZone
    def __init__(self, ana_time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ...) -> None: ...

class CopyChartsAndDashboardsRes(_message.Message):
    __slots__ = ("conflicts",)
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    conflicts: _containers.RepeatedCompositeFieldContainer[CopyChartsAndDashboardsConflict]
    def __init__(self, conflicts: _Optional[_Iterable[_Union[CopyChartsAndDashboardsConflict, _Mapping]]] = ...) -> None: ...

class CopyChartsAndDashboardsConflict(_message.Message):
    __slots__ = ("type", "title")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    type: str
    title: str
    def __init__(self, type: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class CopyDashVizReq(_message.Message):
    __slots__ = ("dashboard_ids", "visualization_ids", "org_id")
    DASHBOARD_IDS_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_ids: _containers.RepeatedScalarFieldContainer[str]
    visualization_ids: _containers.RepeatedScalarFieldContainer[str]
    org_id: str
    def __init__(self, dashboard_ids: _Optional[_Iterable[str]] = ..., visualization_ids: _Optional[_Iterable[str]] = ..., org_id: _Optional[str] = ...) -> None: ...

class CopyDashVizConflict(_message.Message):
    __slots__ = ("type", "title")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    type: str
    title: str
    def __init__(self, type: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class CopyDashVizRes(_message.Message):
    __slots__ = ("conflicts",)
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    conflicts: _containers.RepeatedCompositeFieldContainer[CopyDashVizConflict]
    def __init__(self, conflicts: _Optional[_Iterable[_Union[CopyDashVizConflict, _Mapping]]] = ...) -> None: ...

class GetSpecifiedBillingSummaryReq(_message.Message):
    __slots__ = ("ts", "org_id")
    TS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    org_id: str
    def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetBillingSummaryReq(_message.Message):
    __slots__ = ("ts",)
    TS_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BillingSummary(_message.Message):
    __slots__ = ("client_sid", "client_name", "pro_status", "weeks", "custom_reports", "report_jobs", "watchers", "multi_client")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REPORTS_FIELD_NUMBER: _ClassVar[int]
    REPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    WATCHERS_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLIENT_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    client_name: str
    pro_status: bool
    weeks: WeeksSummary
    custom_reports: CustomReportsSummary
    report_jobs: ActiveReportJobsSummary
    watchers: ActiveWatchersSummary
    multi_client: MultiClientSummary
    def __init__(self, client_sid: _Optional[int] = ..., client_name: _Optional[str] = ..., pro_status: bool = ..., weeks: _Optional[_Union[WeeksSummary, _Mapping]] = ..., custom_reports: _Optional[_Union[CustomReportsSummary, _Mapping]] = ..., report_jobs: _Optional[_Union[ActiveReportJobsSummary, _Mapping]] = ..., watchers: _Optional[_Union[ActiveWatchersSummary, _Mapping]] = ..., multi_client: _Optional[_Union[MultiClientSummary, _Mapping]] = ...) -> None: ...

class WeeksSummary(_message.Message):
    __slots__ = ("weeks_current", "weeks_peak", "weeks_editor", "pro_status")
    WEEKS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    WEEKS_PEAK_FIELD_NUMBER: _ClassVar[int]
    WEEKS_EDITOR_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    weeks_current: int
    weeks_peak: int
    weeks_editor: str
    pro_status: bool
    def __init__(self, weeks_current: _Optional[int] = ..., weeks_peak: _Optional[int] = ..., weeks_editor: _Optional[str] = ..., pro_status: bool = ...) -> None: ...

class CustomReportsSummary(_message.Message):
    __slots__ = ("enabled", "visualizations", "dashboards", "pro_status")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    enabled: CustomReportsEnabledSummary
    visualizations: CustomVisualizationsSummary
    dashboards: CustomDashboardsSummary
    pro_status: bool
    def __init__(self, enabled: _Optional[_Union[CustomReportsEnabledSummary, _Mapping]] = ..., visualizations: _Optional[_Union[CustomVisualizationsSummary, _Mapping]] = ..., dashboards: _Optional[_Union[CustomDashboardsSummary, _Mapping]] = ..., pro_status: bool = ...) -> None: ...

class CustomVisualizationsSummary(_message.Message):
    __slots__ = ("visualizations_current", "visualizations_peak", "custom_visualizations_editor")
    VISUALIZATIONS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATIONS_PEAK_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VISUALIZATIONS_EDITOR_FIELD_NUMBER: _ClassVar[int]
    visualizations_current: int
    visualizations_peak: int
    custom_visualizations_editor: str
    def __init__(self, visualizations_current: _Optional[int] = ..., visualizations_peak: _Optional[int] = ..., custom_visualizations_editor: _Optional[str] = ...) -> None: ...

class CustomDashboardsSummary(_message.Message):
    __slots__ = ("dashboards_current", "dashboards_peak", "custom_dashboards_editor")
    DASHBOARDS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_PEAK_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DASHBOARDS_EDITOR_FIELD_NUMBER: _ClassVar[int]
    dashboards_current: int
    dashboards_peak: int
    custom_dashboards_editor: str
    def __init__(self, dashboards_current: _Optional[int] = ..., dashboards_peak: _Optional[int] = ..., custom_dashboards_editor: _Optional[str] = ...) -> None: ...

class CustomReportsEnabledSummary(_message.Message):
    __slots__ = ("custom_reports_enabled_current", "custom_reports_enabled_peak", "custom_reports_enabled_editor", "pro_status")
    CUSTOM_REPORTS_ENABLED_CURRENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REPORTS_ENABLED_PEAK_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REPORTS_ENABLED_EDITOR_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    custom_reports_enabled_current: bool
    custom_reports_enabled_peak: bool
    custom_reports_enabled_editor: str
    pro_status: bool
    def __init__(self, custom_reports_enabled_current: bool = ..., custom_reports_enabled_peak: bool = ..., custom_reports_enabled_editor: _Optional[str] = ..., pro_status: bool = ...) -> None: ...

class MultiClientSummary(_message.Message):
    __slots__ = ("adoptable", "parents", "children", "pro_status")
    ADOPTABLE_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    adoptable: bool
    parents: Relations
    children: Relations
    pro_status: bool
    def __init__(self, adoptable: bool = ..., parents: _Optional[_Union[Relations, _Mapping]] = ..., children: _Optional[_Union[Relations, _Mapping]] = ..., pro_status: bool = ...) -> None: ...

class Relations(_message.Message):
    __slots__ = ("relations",)
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    def __init__(self, relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ...) -> None: ...

class Relation(_message.Message):
    __slots__ = ("client_sid", "client_name", "relation_initiation", "relation_initiator", "relation_termination", "relation_terminator", "is_current", "org_id")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_INITIATION_FIELD_NUMBER: _ClassVar[int]
    RELATION_INITIATOR_FIELD_NUMBER: _ClassVar[int]
    RELATION_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    RELATION_TERMINATOR_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    client_name: str
    relation_initiation: _timestamp_pb2.Timestamp
    relation_initiator: str
    relation_termination: _timestamp_pb2.Timestamp
    relation_terminator: str
    is_current: bool
    org_id: str
    def __init__(self, client_sid: _Optional[int] = ..., client_name: _Optional[str] = ..., relation_initiation: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., relation_initiator: _Optional[str] = ..., relation_termination: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., relation_terminator: _Optional[str] = ..., is_current: bool = ..., org_id: _Optional[str] = ...) -> None: ...

class Family(_message.Message):
    __slots__ = ("client_sid", "client_name", "parents", "children")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENTS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    client_name: str
    parents: Relations
    children: Relations
    def __init__(self, client_sid: _Optional[int] = ..., client_name: _Optional[str] = ..., parents: _Optional[_Union[Relations, _Mapping]] = ..., children: _Optional[_Union[Relations, _Mapping]] = ...) -> None: ...

class GetAccessibleClientsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFamilyReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class MakeAdoptableReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MakeAdoptableRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpecifiedMakeAdoptableRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAnaAccountRelationReq(_message.Message):
    __slots__ = ("parent_org_id", "child_org_id")
    PARENT_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    parent_org_id: str
    child_org_id: str
    def __init__(self, parent_org_id: _Optional[str] = ..., child_org_id: _Optional[str] = ...) -> None: ...

class SetAnaAccountRelationRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActiveReportJobsSummary(_message.Message):
    __slots__ = ("active_report_jobs_current", "processed_report_jobs", "report_jobs_activator", "pro_status")
    ACTIVE_REPORT_JOBS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_REPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    REPORT_JOBS_ACTIVATOR_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    active_report_jobs_current: int
    processed_report_jobs: int
    report_jobs_activator: str
    pro_status: bool
    def __init__(self, active_report_jobs_current: _Optional[int] = ..., processed_report_jobs: _Optional[int] = ..., report_jobs_activator: _Optional[str] = ..., pro_status: bool = ...) -> None: ...

class ActiveWatchersSummary(_message.Message):
    __slots__ = ("active_watchers_current", "processed_watchers", "watchers_activator", "pro_status")
    ACTIVE_WATCHERS_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_WATCHERS_FIELD_NUMBER: _ClassVar[int]
    WATCHERS_ACTIVATOR_FIELD_NUMBER: _ClassVar[int]
    PRO_STATUS_FIELD_NUMBER: _ClassVar[int]
    active_watchers_current: int
    processed_watchers: int
    watchers_activator: str
    pro_status: bool
    def __init__(self, active_watchers_current: _Optional[int] = ..., processed_watchers: _Optional[int] = ..., watchers_activator: _Optional[str] = ..., pro_status: bool = ...) -> None: ...

class SimpleRelations(_message.Message):
    __slots__ = ("simple_relations",)
    SIMPLE_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    simple_relations: _containers.RepeatedCompositeFieldContainer[SimpleRelation]
    def __init__(self, simple_relations: _Optional[_Iterable[_Union[SimpleRelation, _Mapping]]] = ...) -> None: ...

class SimpleRelation(_message.Message):
    __slots__ = ("client_name", "org_id")
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    org_id: str
    def __init__(self, client_name: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetOrganizationNamesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrganizationNamesRes(_message.Message):
    __slots__ = ("names",)
    class NamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.ScalarMap[int, str]
    def __init__(self, names: _Optional[_Mapping[int, str]] = ...) -> None: ...

class Datapoint(_message.Message):
    __slots__ = ("id", "labels", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    type: str
    def __init__(self, id: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., type: _Optional[str] = ...) -> None: ...

class GetDatapointsReq(_message.Message):
    __slots__ = ("type", "group_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    type: _ana_pb2.Tag
    group_id: str
    def __init__(self, type: _Optional[_Union[_ana_pb2.Tag, str]] = ..., group_id: _Optional[str] = ...) -> None: ...

class GetDatapointsRes(_message.Message):
    __slots__ = ("datapoints",)
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    datapoints: _containers.RepeatedCompositeFieldContainer[Datapoint]
    def __init__(self, datapoints: _Optional[_Iterable[_Union[Datapoint, _Mapping]]] = ...) -> None: ...

class NewDatapoint(_message.Message):
    __slots__ = ("uuid", "label", "filter_id", "float", "string", "bool", "date", "datapoint_id", "tags")
    class Float(_message.Message):
        __slots__ = ("aggregation", "datapoint", "constant", "operation", "percentile")
        AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        DATAPOINT_FIELD_NUMBER: _ClassVar[int]
        CONSTANT_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        PERCENTILE_FIELD_NUMBER: _ClassVar[int]
        aggregation: _ana_pb2.NumericAggregation
        datapoint: str
        constant: float
        operation: _ana_pb2.Operation
        percentile: float
        def __init__(self, aggregation: _Optional[_Union[_ana_pb2.NumericAggregation, str]] = ..., datapoint: _Optional[str] = ..., constant: _Optional[float] = ..., operation: _Optional[_Union[_ana_pb2.Operation, str]] = ..., percentile: _Optional[float] = ...) -> None: ...
    class String(_message.Message):
        __slots__ = ("aggregation", "prepend", "append")
        AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        PREPEND_FIELD_NUMBER: _ClassVar[int]
        APPEND_FIELD_NUMBER: _ClassVar[int]
        aggregation: _ana_pb2.NonNumericAggregation
        prepend: str
        append: str
        def __init__(self, aggregation: _Optional[_Union[_ana_pb2.NonNumericAggregation, str]] = ..., prepend: _Optional[str] = ..., append: _Optional[str] = ...) -> None: ...
    class Bool(_message.Message):
        __slots__ = ("aggregation",)
        AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        aggregation: _ana_pb2.NonNumericAggregation
        def __init__(self, aggregation: _Optional[_Union[_ana_pb2.NonNumericAggregation, str]] = ...) -> None: ...
    class Date(_message.Message):
        __slots__ = ("aggregation", "format", "percentile")
        AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        PERCENTILE_FIELD_NUMBER: _ClassVar[int]
        aggregation: _ana_pb2.NumericAggregation
        format: str
        percentile: float
        def __init__(self, aggregation: _Optional[_Union[_ana_pb2.NumericAggregation, str]] = ..., format: _Optional[str] = ..., percentile: _Optional[float] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    label: str
    filter_id: str
    float: NewDatapoint.Float
    string: NewDatapoint.String
    bool: NewDatapoint.Bool
    date: NewDatapoint.Date
    datapoint_id: str
    tags: _containers.RepeatedScalarFieldContainer[_ana_pb2.Tag]
    def __init__(self, uuid: _Optional[str] = ..., label: _Optional[str] = ..., filter_id: _Optional[str] = ..., float: _Optional[_Union[NewDatapoint.Float, _Mapping]] = ..., string: _Optional[_Union[NewDatapoint.String, _Mapping]] = ..., bool: _Optional[_Union[NewDatapoint.Bool, _Mapping]] = ..., date: _Optional[_Union[NewDatapoint.Date, _Mapping]] = ..., datapoint_id: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_ana_pb2.Tag, str]]] = ...) -> None: ...

class GetDatapointReq(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class GetDatapointResp(_message.Message):
    __slots__ = ("datapoint",)
    DATAPOINT_FIELD_NUMBER: _ClassVar[int]
    datapoint: NewDatapoint
    def __init__(self, datapoint: _Optional[_Union[NewDatapoint, _Mapping]] = ...) -> None: ...

class CreateDatapointReq(_message.Message):
    __slots__ = ("datapoint",)
    DATAPOINT_FIELD_NUMBER: _ClassVar[int]
    datapoint: NewDatapoint
    def __init__(self, datapoint: _Optional[_Union[NewDatapoint, _Mapping]] = ...) -> None: ...

class CreateDatapointResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDatapointReq(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class DeleteDatapointResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CategoryData(_message.Message):
    __slots__ = ("category", "value")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    category: str
    value: float
    def __init__(self, category: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("time_from", "time_to", "time_zone", "filter_id", "org_ids")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    time_zone: _ana_pb2.AnaTimeZone
    filter_id: str
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ..., filter_id: _Optional[str] = ..., org_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFiltersReq(_message.Message):
    __slots__ = ("tag",)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: _ana_pb2.Tag
    def __init__(self, tag: _Optional[_Union[_ana_pb2.Tag, str]] = ...) -> None: ...

class NewFilter(_message.Message):
    __slots__ = ("uuid", "label")
    UUID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    label: str
    def __init__(self, uuid: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class GetFiltersResp(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[NewFilter]
    def __init__(self, filters: _Optional[_Iterable[_Union[NewFilter, _Mapping]]] = ...) -> None: ...

class CreateFilterReq(_message.Message):
    __slots__ = ("compound", "simple", "label", "tags")
    class Compound(_message.Message):
        __slots__ = ("join", "left_filter_id", "right_filter_id")
        JOIN_FIELD_NUMBER: _ClassVar[int]
        LEFT_FILTER_ID_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FILTER_ID_FIELD_NUMBER: _ClassVar[int]
        join: _ana_pb2.CompoundFilterJoin
        left_filter_id: str
        right_filter_id: str
        def __init__(self, join: _Optional[_Union[_ana_pb2.CompoundFilterJoin, str]] = ..., left_filter_id: _Optional[str] = ..., right_filter_id: _Optional[str] = ...) -> None: ...
    class Simple(_message.Message):
        __slots__ = ("datapoint_id", "comparison")
        DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        datapoint_id: str
        comparison: Comparison
        def __init__(self, datapoint_id: _Optional[str] = ..., comparison: _Optional[_Union[Comparison, _Mapping]] = ...) -> None: ...
    COMPOUND_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    compound: CreateFilterReq.Compound
    simple: CreateFilterReq.Simple
    label: str
    tags: _containers.RepeatedScalarFieldContainer[_ana_pb2.Tag]
    def __init__(self, compound: _Optional[_Union[CreateFilterReq.Compound, _Mapping]] = ..., simple: _Optional[_Union[CreateFilterReq.Simple, _Mapping]] = ..., label: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_ana_pb2.Tag, str]]] = ...) -> None: ...

class Comparison(_message.Message):
    __slots__ = ("string", "float", "bool", "date")
    class String(_message.Message):
        __slots__ = ("value", "comparison")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        value: str
        comparison: _ana_pb2.StringComparison
        def __init__(self, value: _Optional[str] = ..., comparison: _Optional[_Union[_ana_pb2.StringComparison, str]] = ...) -> None: ...
    class Float(_message.Message):
        __slots__ = ("value", "comparison")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        value: float
        comparison: _ana_pb2.FloatComparison
        def __init__(self, value: _Optional[float] = ..., comparison: _Optional[_Union[_ana_pb2.FloatComparison, str]] = ...) -> None: ...
    class Bool(_message.Message):
        __slots__ = ("value", "comparison")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        value: bool
        comparison: _ana_pb2.BoolComparison
        def __init__(self, value: bool = ..., comparison: _Optional[_Union[_ana_pb2.BoolComparison, str]] = ...) -> None: ...
    class Date(_message.Message):
        __slots__ = ("value", "comparison")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        value: _timestamp_pb2.Timestamp
        comparison: _ana_pb2.DateComparison
        def __init__(self, value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., comparison: _Optional[_Union[_ana_pb2.DateComparison, str]] = ...) -> None: ...
    STRING_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    string: Comparison.String
    float: Comparison.Float
    bool: Comparison.Bool
    date: Comparison.Date
    def __init__(self, string: _Optional[_Union[Comparison.String, _Mapping]] = ..., float: _Optional[_Union[Comparison.Float, _Mapping]] = ..., bool: _Optional[_Union[Comparison.Bool, _Mapping]] = ..., date: _Optional[_Union[Comparison.Date, _Mapping]] = ...) -> None: ...

class CreateFilterResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MultiValueCategoryData(_message.Message):
    __slots__ = ("category", "values")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    category: str
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, category: _Optional[str] = ..., values: _Optional[_Iterable[float]] = ...) -> None: ...

class GetDataReq(_message.Message):
    __slots__ = ("groupings", "field_datapoint_ids", "filter", "results_on_every_level", "orders", "limit")
    GROUPINGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_DATAPOINT_IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RESULTS_ON_EVERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    groupings: _containers.RepeatedCompositeFieldContainer[Grouping]
    field_datapoint_ids: _containers.RepeatedScalarFieldContainer[str]
    filter: Filter
    results_on_every_level: bool
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    limit: int
    def __init__(self, groupings: _Optional[_Iterable[_Union[Grouping, _Mapping]]] = ..., field_datapoint_ids: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., results_on_every_level: bool = ..., orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., limit: _Optional[int] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("datapoint_id", "desc")
    DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    datapoint_id: str
    desc: bool
    def __init__(self, datapoint_id: _Optional[str] = ..., desc: bool = ...) -> None: ...

class Grouping(_message.Message):
    __slots__ = ("datapoint_id", "time_scope")
    DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    datapoint_id: str
    time_scope: _ana_pb2.TimeScope
    def __init__(self, datapoint_id: _Optional[str] = ..., time_scope: _Optional[_Union[_ana_pb2.TimeScope, str]] = ...) -> None: ...

class GetDataResp(_message.Message):
    __slots__ = ("data", "warnings")
    DATA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[MultiCategoryMultiValueData]
    warnings: _containers.RepeatedCompositeFieldContainer[Warning]
    def __init__(self, data: _Optional[_Iterable[_Union[MultiCategoryMultiValueData, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[Warning, _Mapping]]] = ...) -> None: ...

class Warning(_message.Message):
    __slots__ = ("missing_fields", "missing_locations")
    MISSING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    MISSING_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    missing_fields: MissingFields
    missing_locations: MissingLocations
    def __init__(self, missing_fields: _Optional[_Union[MissingFields, _Mapping]] = ..., missing_locations: _Optional[_Union[MissingLocations, _Mapping]] = ...) -> None: ...

class MissingFields(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fields: _Optional[_Iterable[str]] = ...) -> None: ...

class MissingLocations(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[MissingLocation]
    def __init__(self, fields: _Optional[_Iterable[_Union[MissingLocation, _Mapping]]] = ...) -> None: ...

class MissingLocation(_message.Message):
    __slots__ = ("datapoint_id", "message", "label")
    DATAPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    datapoint_id: str
    message: str
    label: str
    def __init__(self, datapoint_id: _Optional[str] = ..., message: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class MultiCategoryMultiValueData(_message.Message):
    __slots__ = ("categories", "values")
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[Category]
    values: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, categories: _Optional[_Iterable[_Union[Category, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ("string_value", "timestamp_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    timestamp_value: _timestamp_pb2.Timestamp
    def __init__(self, string_value: _Optional[str] = ..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("string_value", "float_value", "timestamp_value", "empty", "bool_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    float_value: float
    timestamp_value: _timestamp_pb2.Timestamp
    empty: _empty_pb2.Empty
    bool_value: bool
    def __init__(self, string_value: _Optional[str] = ..., float_value: _Optional[float] = ..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., bool_value: bool = ...) -> None: ...

class GetDataTimeIncrementResp(_message.Message):
    __slots__ = ("time_increments",)
    TIME_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    time_increments: _containers.RepeatedCompositeFieldContainer[TimeIncrement]
    def __init__(self, time_increments: _Optional[_Iterable[_Union[TimeIncrement, _Mapping]]] = ...) -> None: ...

class TimeIncrement(_message.Message):
    __slots__ = ("time", "value")
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    value: Value
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class Charts(_message.Message):
    __slots__ = ("charts",)
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    charts: _containers.RepeatedCompositeFieldContainer[Chart]
    def __init__(self, charts: _Optional[_Iterable[_Union[Chart, _Mapping]]] = ...) -> None: ...

class Chart(_message.Message):
    __slots__ = ("chart_id", "title", "chart_details", "root_id", "display_labels")
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CHART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABELS_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    title: str
    chart_details: ChartDetails
    root_id: str
    display_labels: _ana_charts_pb2.ChartDisplayLabels
    def __init__(self, chart_id: _Optional[str] = ..., title: _Optional[str] = ..., chart_details: _Optional[_Union[ChartDetails, _Mapping]] = ..., root_id: _Optional[str] = ..., display_labels: _Optional[_Union[_ana_charts_pb2.ChartDisplayLabels, str]] = ...) -> None: ...

class ChartDetails(_message.Message):
    __slots__ = ("single_value_chart", "pie_chart", "radar_fixed_chart", "bar_chart", "bullet_chart", "multi_value_chart", "tree_map_chart", "activity_gauge_chart", "arc_chart", "scatter_chart", "time_histogram_chart", "tree_table_chart", "info_panel_chart", "ranked_list_chart", "speedometer_chart", "line_chart", "spline_chart", "area_chart", "table_chart", "bubble_chart", "packed_bubble_chart", "sunburst_chart")
    SINGLE_VALUE_CHART_FIELD_NUMBER: _ClassVar[int]
    PIE_CHART_FIELD_NUMBER: _ClassVar[int]
    RADAR_FIXED_CHART_FIELD_NUMBER: _ClassVar[int]
    BAR_CHART_FIELD_NUMBER: _ClassVar[int]
    BULLET_CHART_FIELD_NUMBER: _ClassVar[int]
    MULTI_VALUE_CHART_FIELD_NUMBER: _ClassVar[int]
    TREE_MAP_CHART_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_GAUGE_CHART_FIELD_NUMBER: _ClassVar[int]
    ARC_CHART_FIELD_NUMBER: _ClassVar[int]
    SCATTER_CHART_FIELD_NUMBER: _ClassVar[int]
    TIME_HISTOGRAM_CHART_FIELD_NUMBER: _ClassVar[int]
    TREE_TABLE_CHART_FIELD_NUMBER: _ClassVar[int]
    INFO_PANEL_CHART_FIELD_NUMBER: _ClassVar[int]
    RANKED_LIST_CHART_FIELD_NUMBER: _ClassVar[int]
    SPEEDOMETER_CHART_FIELD_NUMBER: _ClassVar[int]
    LINE_CHART_FIELD_NUMBER: _ClassVar[int]
    SPLINE_CHART_FIELD_NUMBER: _ClassVar[int]
    AREA_CHART_FIELD_NUMBER: _ClassVar[int]
    TABLE_CHART_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_CHART_FIELD_NUMBER: _ClassVar[int]
    PACKED_BUBBLE_CHART_FIELD_NUMBER: _ClassVar[int]
    SUNBURST_CHART_FIELD_NUMBER: _ClassVar[int]
    single_value_chart: SingleValueChart
    pie_chart: PieChart
    radar_fixed_chart: RadarFixedChart
    bar_chart: BarChart
    bullet_chart: BulletChart
    multi_value_chart: MultiValueChart
    tree_map_chart: TreeMapChart
    activity_gauge_chart: ActivityGaugeChart
    arc_chart: ArcChart
    scatter_chart: ScatterChart
    time_histogram_chart: TimeHistogramChart
    tree_table_chart: TreeTableChart
    info_panel_chart: InfoPanelChart
    ranked_list_chart: RankedListChart
    speedometer_chart: SpeedometerChart
    line_chart: LineChart
    spline_chart: SplineChart
    area_chart: AreaChart
    table_chart: TableChart
    bubble_chart: BubbleChart
    packed_bubble_chart: PackedBubbleChart
    sunburst_chart: SunburstChart
    def __init__(self, single_value_chart: _Optional[_Union[SingleValueChart, _Mapping]] = ..., pie_chart: _Optional[_Union[PieChart, _Mapping]] = ..., radar_fixed_chart: _Optional[_Union[RadarFixedChart, _Mapping]] = ..., bar_chart: _Optional[_Union[BarChart, _Mapping]] = ..., bullet_chart: _Optional[_Union[BulletChart, _Mapping]] = ..., multi_value_chart: _Optional[_Union[MultiValueChart, _Mapping]] = ..., tree_map_chart: _Optional[_Union[TreeMapChart, _Mapping]] = ..., activity_gauge_chart: _Optional[_Union[ActivityGaugeChart, _Mapping]] = ..., arc_chart: _Optional[_Union[ArcChart, _Mapping]] = ..., scatter_chart: _Optional[_Union[ScatterChart, _Mapping]] = ..., time_histogram_chart: _Optional[_Union[TimeHistogramChart, _Mapping]] = ..., tree_table_chart: _Optional[_Union[TreeTableChart, _Mapping]] = ..., info_panel_chart: _Optional[_Union[InfoPanelChart, _Mapping]] = ..., ranked_list_chart: _Optional[_Union[RankedListChart, _Mapping]] = ..., speedometer_chart: _Optional[_Union[SpeedometerChart, _Mapping]] = ..., line_chart: _Optional[_Union[LineChart, _Mapping]] = ..., spline_chart: _Optional[_Union[SplineChart, _Mapping]] = ..., area_chart: _Optional[_Union[AreaChart, _Mapping]] = ..., table_chart: _Optional[_Union[TableChart, _Mapping]] = ..., bubble_chart: _Optional[_Union[BubbleChart, _Mapping]] = ..., packed_bubble_chart: _Optional[_Union[PackedBubbleChart, _Mapping]] = ..., sunburst_chart: _Optional[_Union[SunburstChart, _Mapping]] = ...) -> None: ...

class SingleValueChart(_message.Message):
    __slots__ = ("data_point_id", "label", "suffix", "show_label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    SHOW_LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    suffix: _ana_charts_pb2.SuffixChoices
    show_label: bool
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ..., suffix: _Optional[_Union[_ana_charts_pb2.SuffixChoices, str]] = ..., show_label: bool = ...) -> None: ...

class PieChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "hole_radius")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    HOLE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    hole_radius: int
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., hole_radius: _Optional[int] = ...) -> None: ...

class RadarFixedChart(_message.Message):
    __slots__ = ("grouping_data_point_id", "radar_fixed_inner_charts", "data_labels")
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    RADAR_FIXED_INNER_CHARTS_FIELD_NUMBER: _ClassVar[int]
    DATA_LABELS_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    radar_fixed_inner_charts: _containers.RepeatedCompositeFieldContainer[RadarFixedInnerChart]
    data_labels: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ..., radar_fixed_inner_charts: _Optional[_Iterable[_Union[RadarFixedInnerChart, _Mapping]]] = ..., data_labels: _Optional[str] = ...) -> None: ...

class RadarFixedInnerChart(_message.Message):
    __slots__ = ("data_point_id", "category_name", "area", "bar", "line", "spline")
    class Area(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Bar(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Line(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Spline(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    SPLINE_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    category_name: str
    area: RadarFixedInnerChart.Area
    bar: RadarFixedInnerChart.Bar
    line: RadarFixedInnerChart.Line
    spline: RadarFixedInnerChart.Spline
    def __init__(self, data_point_id: _Optional[str] = ..., category_name: _Optional[str] = ..., area: _Optional[_Union[RadarFixedInnerChart.Area, _Mapping]] = ..., bar: _Optional[_Union[RadarFixedInnerChart.Bar, _Mapping]] = ..., line: _Optional[_Union[RadarFixedInnerChart.Line, _Mapping]] = ..., spline: _Optional[_Union[RadarFixedInnerChart.Spline, _Mapping]] = ...) -> None: ...

class BarChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "orientation", "threshold", "x_label", "y_label", "legend")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    X_LABEL_FIELD_NUMBER: _ClassVar[int]
    Y_LABEL_FIELD_NUMBER: _ClassVar[int]
    LEGEND_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    orientation: _ana_charts_pb2.BarChartOrientation
    threshold: Threshold
    x_label: str
    y_label: str
    legend: str
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., orientation: _Optional[_Union[_ana_charts_pb2.BarChartOrientation, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ..., x_label: _Optional[str] = ..., y_label: _Optional[str] = ..., legend: _Optional[str] = ...) -> None: ...

class BulletChart(_message.Message):
    __slots__ = ("field_data_point_id", "orientation", "threshold", "legend")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    LEGEND_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    orientation: _ana_charts_pb2.ChartOrientation
    threshold: Threshold
    legend: str
    def __init__(self, field_data_point_id: _Optional[str] = ..., orientation: _Optional[_Union[_ana_charts_pb2.ChartOrientation, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ..., legend: _Optional[str] = ...) -> None: ...

class MultiValueChart(_message.Message):
    __slots__ = ("data_values", "columns")
    DATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    data_values: _containers.RepeatedCompositeFieldContainer[DataValue]
    columns: int
    def __init__(self, data_values: _Optional[_Iterable[_Union[DataValue, _Mapping]]] = ..., columns: _Optional[int] = ...) -> None: ...

class DataValue(_message.Message):
    __slots__ = ("data_point_id", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class TreeMapChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "min_color", "max_color")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_COLOR_FIELD_NUMBER: _ClassVar[int]
    MAX_COLOR_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    min_color: str
    max_color: str
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., min_color: _Optional[str] = ..., max_color: _Optional[str] = ...) -> None: ...

class ActivityGaugeChart(_message.Message):
    __slots__ = ("activity_gauge_rings",)
    ACTIVITY_GAUGE_RINGS_FIELD_NUMBER: _ClassVar[int]
    activity_gauge_rings: _containers.RepeatedCompositeFieldContainer[ActivityGaugeRing]
    def __init__(self, activity_gauge_rings: _Optional[_Iterable[_Union[ActivityGaugeRing, _Mapping]]] = ...) -> None: ...

class ActivityGaugeRing(_message.Message):
    __slots__ = ("data_point_id", "threshold", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    threshold: Threshold
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ..., label: _Optional[str] = ...) -> None: ...

class ArcChart(_message.Message):
    __slots__ = ("data_point_id", "label", "threshold")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    threshold: Threshold
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ...) -> None: ...

class Threshold(_message.Message):
    __slots__ = ("static_threshold", "data_point_threshold")
    STATIC_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DATA_POINT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    static_threshold: int
    data_point_threshold: str
    def __init__(self, static_threshold: _Optional[int] = ..., data_point_threshold: _Optional[str] = ...) -> None: ...

class ScatterChart(_message.Message):
    __slots__ = ("grouping_data_point_id", "x_data_point_id", "y_data_point_id", "x_label", "y_label", "legend")
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    X_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    Y_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    X_LABEL_FIELD_NUMBER: _ClassVar[int]
    Y_LABEL_FIELD_NUMBER: _ClassVar[int]
    LEGEND_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    x_data_point_id: str
    y_data_point_id: str
    x_label: str
    y_label: str
    legend: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ..., x_data_point_id: _Optional[str] = ..., y_data_point_id: _Optional[str] = ..., x_label: _Optional[str] = ..., y_label: _Optional[str] = ..., legend: _Optional[str] = ...) -> None: ...

class TimeHistogramChart(_message.Message):
    __slots__ = ("data_point_id", "time_scope", "threshold")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    time_scope: _ana_pb2.TimeScope
    threshold: Threshold
    def __init__(self, data_point_id: _Optional[str] = ..., time_scope: _Optional[_Union[_ana_pb2.TimeScope, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ...) -> None: ...

class InfoPanelChart(_message.Message):
    __slots__ = ("data_values",)
    DATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    data_values: _containers.RepeatedCompositeFieldContainer[InfoPanelDataValue]
    def __init__(self, data_values: _Optional[_Iterable[_Union[InfoPanelDataValue, _Mapping]]] = ...) -> None: ...

class InfoPanelDataValue(_message.Message):
    __slots__ = ("data_point_id", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class TreeTableChart(_message.Message):
    __slots__ = ("data_values", "grouping_values")
    DATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    GROUPING_VALUES_FIELD_NUMBER: _ClassVar[int]
    data_values: _containers.RepeatedCompositeFieldContainer[TreeTableDataValue]
    grouping_values: _containers.RepeatedCompositeFieldContainer[TreeTableGroupingValue]
    def __init__(self, data_values: _Optional[_Iterable[_Union[TreeTableDataValue, _Mapping]]] = ..., grouping_values: _Optional[_Iterable[_Union[TreeTableGroupingValue, _Mapping]]] = ...) -> None: ...

class TreeTableDataValue(_message.Message):
    __slots__ = ("data_point_id", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class TreeTableGroupingValue(_message.Message):
    __slots__ = ("grouping_data_point_id",)
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ...) -> None: ...

class RankedListChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "threshold")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    threshold: Threshold
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ...) -> None: ...

class SpeedometerChart(_message.Message):
    __slots__ = ("data_point_id", "label", "warning_threshold", "danger_threshold", "max_threshold", "suffix_label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    WARNING_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DANGER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    warning_threshold: Threshold
    danger_threshold: Threshold
    max_threshold: Threshold
    suffix_label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ..., warning_threshold: _Optional[_Union[Threshold, _Mapping]] = ..., danger_threshold: _Optional[_Union[Threshold, _Mapping]] = ..., max_threshold: _Optional[_Union[Threshold, _Mapping]] = ..., suffix_label: _Optional[str] = ...) -> None: ...

class LineChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "orientation", "threshold", "step")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    orientation: _ana_charts_pb2.ChartOrientation
    threshold: Threshold
    step: _ana_charts_pb2.LineChartStep
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., orientation: _Optional[_Union[_ana_charts_pb2.ChartOrientation, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ..., step: _Optional[_Union[_ana_charts_pb2.LineChartStep, str]] = ...) -> None: ...

class SplineChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "orientation", "threshold")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    orientation: _ana_charts_pb2.ChartOrientation
    threshold: Threshold
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., orientation: _Optional[_Union[_ana_charts_pb2.ChartOrientation, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ...) -> None: ...

class AreaChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_data_point_id", "orientation", "threshold", "area_type")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    AREA_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_data_point_id: str
    orientation: _ana_charts_pb2.ChartOrientation
    threshold: Threshold
    area_type: _ana_charts_pb2.AreaChartChoice
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_data_point_id: _Optional[str] = ..., orientation: _Optional[_Union[_ana_charts_pb2.ChartOrientation, str]] = ..., threshold: _Optional[_Union[Threshold, _Mapping]] = ..., area_type: _Optional[_Union[_ana_charts_pb2.AreaChartChoice, str]] = ...) -> None: ...

class TableChart(_message.Message):
    __slots__ = ("data_values", "grouping_values", "order_by_values")
    DATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    GROUPING_VALUES_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_VALUES_FIELD_NUMBER: _ClassVar[int]
    data_values: _containers.RepeatedCompositeFieldContainer[TableDataValue]
    grouping_values: _containers.RepeatedCompositeFieldContainer[TableGroupingValue]
    order_by_values: _containers.RepeatedCompositeFieldContainer[TableOrderByValue]
    def __init__(self, data_values: _Optional[_Iterable[_Union[TableDataValue, _Mapping]]] = ..., grouping_values: _Optional[_Iterable[_Union[TableGroupingValue, _Mapping]]] = ..., order_by_values: _Optional[_Iterable[_Union[TableOrderByValue, _Mapping]]] = ...) -> None: ...

class TableDataValue(_message.Message):
    __slots__ = ("data_point_id", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class TableGroupingValue(_message.Message):
    __slots__ = ("grouping_data_point_id",)
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ...) -> None: ...

class TableOrderByValue(_message.Message):
    __slots__ = ("order_by",)
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    order_by: str
    def __init__(self, order_by: _Optional[str] = ...) -> None: ...

class BubbleChart(_message.Message):
    __slots__ = ("grouping_data_point_id", "grouping_label", "x_data_point_id", "x_label", "y_data_point_id", "y_label", "z_data_point_id", "z_label")
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_LABEL_FIELD_NUMBER: _ClassVar[int]
    X_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    X_LABEL_FIELD_NUMBER: _ClassVar[int]
    Y_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    Y_LABEL_FIELD_NUMBER: _ClassVar[int]
    Z_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    Z_LABEL_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    grouping_label: str
    x_data_point_id: str
    x_label: str
    y_data_point_id: str
    y_label: str
    z_data_point_id: str
    z_label: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ..., grouping_label: _Optional[str] = ..., x_data_point_id: _Optional[str] = ..., x_label: _Optional[str] = ..., y_data_point_id: _Optional[str] = ..., y_label: _Optional[str] = ..., z_data_point_id: _Optional[str] = ..., z_label: _Optional[str] = ...) -> None: ...

class PackedBubbleChart(_message.Message):
    __slots__ = ("field_data_point_id", "field_label", "grouping_values", "packed_choice")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_LABEL_FIELD_NUMBER: _ClassVar[int]
    GROUPING_VALUES_FIELD_NUMBER: _ClassVar[int]
    PACKED_CHOICE_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    field_label: str
    grouping_values: _containers.RepeatedCompositeFieldContainer[PackedBubbleGroupingValue]
    packed_choice: _ana_charts_pb2.PackedBubbleChoice
    def __init__(self, field_data_point_id: _Optional[str] = ..., field_label: _Optional[str] = ..., grouping_values: _Optional[_Iterable[_Union[PackedBubbleGroupingValue, _Mapping]]] = ..., packed_choice: _Optional[_Union[_ana_charts_pb2.PackedBubbleChoice, str]] = ...) -> None: ...

class PackedBubbleGroupingValue(_message.Message):
    __slots__ = ("grouping_data_point_id",)
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ...) -> None: ...

class SunburstChart(_message.Message):
    __slots__ = ("field_data_point_id", "grouping_values", "center_label")
    FIELD_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUPING_VALUES_FIELD_NUMBER: _ClassVar[int]
    CENTER_LABEL_FIELD_NUMBER: _ClassVar[int]
    field_data_point_id: str
    grouping_values: _containers.RepeatedCompositeFieldContainer[SunburstGroupingValue]
    center_label: str
    def __init__(self, field_data_point_id: _Optional[str] = ..., grouping_values: _Optional[_Iterable[_Union[SunburstGroupingValue, _Mapping]]] = ..., center_label: _Optional[str] = ...) -> None: ...

class SunburstGroupingValue(_message.Message):
    __slots__ = ("grouping_data_point_id",)
    GROUPING_DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    grouping_data_point_id: str
    def __init__(self, grouping_data_point_id: _Optional[str] = ...) -> None: ...

class CreateChartReq(_message.Message):
    __slots__ = ("title", "chart_details", "display_labels")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CHART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABELS_FIELD_NUMBER: _ClassVar[int]
    title: str
    chart_details: ChartDetails
    display_labels: _ana_charts_pb2.ChartDisplayLabels
    def __init__(self, title: _Optional[str] = ..., chart_details: _Optional[_Union[ChartDetails, _Mapping]] = ..., display_labels: _Optional[_Union[_ana_charts_pb2.ChartDisplayLabels, str]] = ...) -> None: ...

class CreateChartRes(_message.Message):
    __slots__ = ("chart_id",)
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    def __init__(self, chart_id: _Optional[str] = ...) -> None: ...

class GetChartReq(_message.Message):
    __slots__ = ("chart_id",)
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    def __init__(self, chart_id: _Optional[str] = ...) -> None: ...

class DeleteChartReq(_message.Message):
    __slots__ = ("chart_id",)
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    def __init__(self, chart_id: _Optional[str] = ...) -> None: ...

class DeleteChartRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashPage(_message.Message):
    __slots__ = ("dashboard", "visualization_legacy", "chart")
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATION_LEGACY_FIELD_NUMBER: _ClassVar[int]
    CHART_FIELD_NUMBER: _ClassVar[int]
    dashboard: DashPageDashboard
    visualization_legacy: DashPageVisualizationLegacy
    chart: DashPageChart
    def __init__(self, dashboard: _Optional[_Union[DashPageDashboard, _Mapping]] = ..., visualization_legacy: _Optional[_Union[DashPageVisualizationLegacy, _Mapping]] = ..., chart: _Optional[_Union[DashPageChart, _Mapping]] = ...) -> None: ...

class DashPageDashboard(_message.Message):
    __slots__ = ("dashboard_id", "title", "root_id", "tcn_standard")
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TCN_STANDARD_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    root_id: str
    tcn_standard: bool
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ..., tcn_standard: bool = ...) -> None: ...

class DashPageVisualizationLegacy(_message.Message):
    __slots__ = ("visualization_id", "title", "root_id")
    VISUALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    visualization_id: str
    title: str
    root_id: str
    def __init__(self, visualization_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ...) -> None: ...

class DashPageChart(_message.Message):
    __slots__ = ("chart_id", "title", "root_id", "tcn_standard")
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TCN_STANDARD_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    title: str
    root_id: str
    tcn_standard: bool
    def __init__(self, chart_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ..., tcn_standard: bool = ...) -> None: ...

class GetAccessibleDashPagesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAccessibleDashPagesRes(_message.Message):
    __slots__ = ("dash_pages",)
    DASH_PAGES_FIELD_NUMBER: _ClassVar[int]
    dash_pages: _containers.RepeatedCompositeFieldContainer[DashPage]
    def __init__(self, dash_pages: _Optional[_Iterable[_Union[DashPage, _Mapping]]] = ...) -> None: ...

class RecommendedDashPage(_message.Message):
    __slots__ = ("dashboard", "visualization_legacy", "chart")
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATION_LEGACY_FIELD_NUMBER: _ClassVar[int]
    CHART_FIELD_NUMBER: _ClassVar[int]
    dashboard: RecommendedDashboard
    visualization_legacy: RecommendedVisualizationLegacy
    chart: RecommendedChart
    def __init__(self, dashboard: _Optional[_Union[RecommendedDashboard, _Mapping]] = ..., visualization_legacy: _Optional[_Union[RecommendedVisualizationLegacy, _Mapping]] = ..., chart: _Optional[_Union[RecommendedChart, _Mapping]] = ...) -> None: ...

class RecommendedDashboard(_message.Message):
    __slots__ = ("dashboard_id", "title", "root_id", "tcn_standard")
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TCN_STANDARD_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    title: str
    root_id: str
    tcn_standard: bool
    def __init__(self, dashboard_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ..., tcn_standard: bool = ...) -> None: ...

class RecommendedVisualizationLegacy(_message.Message):
    __slots__ = ("visualization_id", "title", "root_id")
    VISUALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    visualization_id: str
    title: str
    root_id: str
    def __init__(self, visualization_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ...) -> None: ...

class RecommendedChart(_message.Message):
    __slots__ = ("chart_id", "title", "root_id", "tcn_standard")
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    TCN_STANDARD_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    title: str
    root_id: str
    tcn_standard: bool
    def __init__(self, chart_id: _Optional[str] = ..., title: _Optional[str] = ..., root_id: _Optional[str] = ..., tcn_standard: bool = ...) -> None: ...

class RecommendedDashPageReq(_message.Message):
    __slots__ = ("dashboard", "visualization_legacy", "chart")
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    VISUALIZATION_LEGACY_FIELD_NUMBER: _ClassVar[int]
    CHART_FIELD_NUMBER: _ClassVar[int]
    dashboard: RecommendedDashboardReq
    visualization_legacy: RecommendedVisualizationLegacyReq
    chart: RecommendedChartReq
    def __init__(self, dashboard: _Optional[_Union[RecommendedDashboardReq, _Mapping]] = ..., visualization_legacy: _Optional[_Union[RecommendedVisualizationLegacyReq, _Mapping]] = ..., chart: _Optional[_Union[RecommendedChartReq, _Mapping]] = ...) -> None: ...

class RecommendedDashboardReq(_message.Message):
    __slots__ = ("dashboard_id",)
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    def __init__(self, dashboard_id: _Optional[str] = ...) -> None: ...

class RecommendedVisualizationLegacyReq(_message.Message):
    __slots__ = ("visualization_id",)
    VISUALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    visualization_id: str
    def __init__(self, visualization_id: _Optional[str] = ...) -> None: ...

class RecommendedChartReq(_message.Message):
    __slots__ = ("chart_id",)
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    def __init__(self, chart_id: _Optional[str] = ...) -> None: ...

class GetRecommendedDashPagesHomeReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRecommendedDashPagesReq(_message.Message):
    __slots__ = ("source_dash_page",)
    SOURCE_DASH_PAGE_FIELD_NUMBER: _ClassVar[int]
    source_dash_page: RecommendedDashPageReq
    def __init__(self, source_dash_page: _Optional[_Union[RecommendedDashPageReq, _Mapping]] = ...) -> None: ...

class GetRecommendedDashPagesRes(_message.Message):
    __slots__ = ("recommended_dash_pages",)
    RECOMMENDED_DASH_PAGES_FIELD_NUMBER: _ClassVar[int]
    recommended_dash_pages: _containers.RepeatedCompositeFieldContainer[RecommendedDashPage]
    def __init__(self, recommended_dash_pages: _Optional[_Iterable[_Union[RecommendedDashPage, _Mapping]]] = ...) -> None: ...

class DashPageSelectEventReq(_message.Message):
    __slots__ = ("selection_dash_page", "source_dash_page", "from_home")
    SELECTION_DASH_PAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DASH_PAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_HOME_FIELD_NUMBER: _ClassVar[int]
    selection_dash_page: RecommendedDashPageReq
    source_dash_page: RecommendedDashPageReq
    from_home: bool
    def __init__(self, selection_dash_page: _Optional[_Union[RecommendedDashPageReq, _Mapping]] = ..., source_dash_page: _Optional[_Union[RecommendedDashPageReq, _Mapping]] = ..., from_home: bool = ...) -> None: ...

class DashPageSelectEventRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VisualizationEventRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRecommendedTimeFiltersReq(_message.Message):
    __slots__ = ("dash_page_id", "dash_page_type", "current_filter")
    DASH_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DASH_PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    dash_page_id: str
    dash_page_type: RecommendedDashPageReq
    current_filter: str
    def __init__(self, dash_page_id: _Optional[str] = ..., dash_page_type: _Optional[_Union[RecommendedDashPageReq, _Mapping]] = ..., current_filter: _Optional[str] = ...) -> None: ...

class GetRecommendedTimeFiltersRes(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filters: _Optional[_Iterable[str]] = ...) -> None: ...

class TimeFilterEventReq(_message.Message):
    __slots__ = ("time_filter_type", "time_filter_name", "dash_page_type")
    TIME_FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DASH_PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    time_filter_type: _ana_pb2.TimeFilterType
    time_filter_name: str
    dash_page_type: RecommendedDashPageReq
    def __init__(self, time_filter_type: _Optional[_Union[_ana_pb2.TimeFilterType, str]] = ..., time_filter_name: _Optional[str] = ..., dash_page_type: _Optional[_Union[RecommendedDashPageReq, _Mapping]] = ...) -> None: ...

class TimeFilterEventRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportJob(_message.Message):
    __slots__ = ("export_job_id", "title", "export_delivery", "export_options", "export_schedule")
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    title: str
    export_delivery: ExportDelivery
    export_options: ExportOptions
    export_schedule: ExportSchedule
    def __init__(self, export_job_id: _Optional[str] = ..., title: _Optional[str] = ..., export_delivery: _Optional[_Union[ExportDelivery, _Mapping]] = ..., export_options: _Optional[_Union[ExportOptions, _Mapping]] = ..., export_schedule: _Optional[_Union[ExportSchedule, _Mapping]] = ...) -> None: ...

class ExportSchedule(_message.Message):
    __slots__ = ("enabled", "campaign_complete", "end_of_day")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    END_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    campaign_complete: CampaignCompleteSchedule
    end_of_day: EndOfDaySchedule
    def __init__(self, enabled: bool = ..., campaign_complete: _Optional[_Union[CampaignCompleteSchedule, _Mapping]] = ..., end_of_day: _Optional[_Union[EndOfDaySchedule, _Mapping]] = ...) -> None: ...

class CampaignCompleteSchedule(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndOfDaySchedule(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportOptions(_message.Message):
    __slots__ = ("zip", "csv_options")
    ZIP_FIELD_NUMBER: _ClassVar[int]
    CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    zip: bool
    csv_options: CsvOptions
    def __init__(self, zip: bool = ..., csv_options: _Optional[_Union[CsvOptions, _Mapping]] = ...) -> None: ...

class CsvOptions(_message.Message):
    __slots__ = ("fixed_width", "csv_quote_type", "include_headers")
    FIXED_WIDTH_FIELD_NUMBER: _ClassVar[int]
    CSV_QUOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    fixed_width: bool
    csv_quote_type: _ana_pb2.CsvQuoteType
    include_headers: bool
    def __init__(self, fixed_width: bool = ..., csv_quote_type: _Optional[_Union[_ana_pb2.CsvQuoteType, str]] = ..., include_headers: bool = ...) -> None: ...

class ExportDelivery(_message.Message):
    __slots__ = ("email", "sftp", "https", "failure_email_addreses")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SFTP_FIELD_NUMBER: _ClassVar[int]
    HTTPS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_EMAIL_ADDRESES_FIELD_NUMBER: _ClassVar[int]
    email: EmailDelivery
    sftp: SftpDelivery
    https: HttpsDelivery
    failure_email_addreses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email: _Optional[_Union[EmailDelivery, _Mapping]] = ..., sftp: _Optional[_Union[SftpDelivery, _Mapping]] = ..., https: _Optional[_Union[HttpsDelivery, _Mapping]] = ..., failure_email_addreses: _Optional[_Iterable[str]] = ...) -> None: ...

class HttpsDelivery(_message.Message):
    __slots__ = ("url", "post_parameter")
    URL_FIELD_NUMBER: _ClassVar[int]
    POST_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    url: str
    post_parameter: str
    def __init__(self, url: _Optional[str] = ..., post_parameter: _Optional[str] = ...) -> None: ...

class SftpDelivery(_message.Message):
    __slots__ = ("password", "private_key", "user_name", "url", "path")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    password: str
    private_key: str
    user_name: str
    url: str
    path: str
    def __init__(self, password: _Optional[str] = ..., private_key: _Optional[str] = ..., user_name: _Optional[str] = ..., url: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class EmailDelivery(_message.Message):
    __slots__ = ("addresses",)
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class DataSelection(_message.Message):
    __slots__ = ("chart_id", "custom", "table_data_points", "filter_ids")
    CHART_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    TABLE_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_IDS_FIELD_NUMBER: _ClassVar[int]
    chart_id: str
    custom: _ana_pb2.CustomDataSeleciton
    table_data_points: TableDataPoints
    filter_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chart_id: _Optional[str] = ..., custom: _Optional[_Union[_ana_pb2.CustomDataSeleciton, str]] = ..., table_data_points: _Optional[_Union[TableDataPoints, _Mapping]] = ..., filter_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TableDataPoints(_message.Message):
    __slots__ = ("title", "data_values", "grouping_data_point_ids", "order_by")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DATA_VALUES_FIELD_NUMBER: _ClassVar[int]
    GROUPING_DATA_POINT_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    title: str
    data_values: _containers.RepeatedCompositeFieldContainer[ExporterTableDataValue]
    grouping_data_point_ids: _containers.RepeatedScalarFieldContainer[str]
    order_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., data_values: _Optional[_Iterable[_Union[ExporterTableDataValue, _Mapping]]] = ..., grouping_data_point_ids: _Optional[_Iterable[str]] = ..., order_by: _Optional[_Iterable[str]] = ...) -> None: ...

class ExporterTableDataValue(_message.Message):
    __slots__ = ("data_point_id", "label")
    DATA_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    data_point_id: str
    label: str
    def __init__(self, data_point_id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class CreateExportJobReq(_message.Message):
    __slots__ = ("title", "data_selection", "export_delivery", "export_options", "export_schedule")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DATA_SELECTION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    title: str
    data_selection: DataSelection
    export_delivery: ExportDelivery
    export_options: ExportOptions
    export_schedule: ExportSchedule
    def __init__(self, title: _Optional[str] = ..., data_selection: _Optional[_Union[DataSelection, _Mapping]] = ..., export_delivery: _Optional[_Union[ExportDelivery, _Mapping]] = ..., export_options: _Optional[_Union[ExportOptions, _Mapping]] = ..., export_schedule: _Optional[_Union[ExportSchedule, _Mapping]] = ...) -> None: ...

class CreateExportJobRes(_message.Message):
    __slots__ = ("export_job_id",)
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    def __init__(self, export_job_id: _Optional[str] = ...) -> None: ...

class GetExportJobsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetExportJobsRes(_message.Message):
    __slots__ = ("export_jobs",)
    EXPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    export_jobs: _containers.RepeatedCompositeFieldContainer[ExportJob]
    def __init__(self, export_jobs: _Optional[_Iterable[_Union[ExportJob, _Mapping]]] = ...) -> None: ...

class SendExportReq(_message.Message):
    __slots__ = ("export_job_id",)
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    def __init__(self, export_job_id: _Optional[str] = ...) -> None: ...

class SendExportRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteExportJobReq(_message.Message):
    __slots__ = ("export_job_id",)
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    def __init__(self, export_job_id: _Optional[str] = ...) -> None: ...

class DeleteExportJobRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetExportJobActiveReq(_message.Message):
    __slots__ = ("export_job_id", "set_active")
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SET_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    set_active: bool
    def __init__(self, export_job_id: _Optional[str] = ..., set_active: bool = ...) -> None: ...

class SetExportJobActiveRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetExportHistoryDetailsReq(_message.Message):
    __slots__ = ("org_id", "time_from", "time_to")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    time_from: _timestamp_pb2.Timestamp
    time_to: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., time_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetExportHistoryDetailsRes(_message.Message):
    __slots__ = ("result_count", "exports")
    RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPORTS_FIELD_NUMBER: _ClassVar[int]
    result_count: int
    exports: _containers.RepeatedCompositeFieldContainer[Export]
    def __init__(self, result_count: _Optional[int] = ..., exports: _Optional[_Iterable[_Union[Export, _Mapping]]] = ...) -> None: ...

class Export(_message.Message):
    __slots__ = ("export_job_id", "title", "run_time", "status")
    EXPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    export_job_id: str
    title: str
    run_time: _timestamp_pb2.Timestamp
    status: _ana_pb2.ExportStatus
    def __init__(self, export_job_id: _Optional[str] = ..., title: _Optional[str] = ..., run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_ana_pb2.ExportStatus, str]] = ...) -> None: ...

class DownloadExportReq(_message.Message):
    __slots__ = ("export_id",)
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    export_id: str
    def __init__(self, export_id: _Optional[str] = ...) -> None: ...

class DownloadExportRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBillingReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBillingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthorizedAnalyticsLinkReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthorizedAnalyticsLinkRes(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class ClientGroup(_message.Message):
    __slots__ = ("campaign_type", "processed_call_count", "baseline_call_count")
    CAMPAIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    BASELINE_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    campaign_type: str
    processed_call_count: int
    baseline_call_count: int
    def __init__(self, campaign_type: _Optional[str] = ..., processed_call_count: _Optional[int] = ..., baseline_call_count: _Optional[int] = ...) -> None: ...

class GetClientStatusReq(_message.Message):
    __slots__ = ("start_time", "org_id")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    org_id: str
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetClientStatusResp(_message.Message):
    __slots__ = ("client_groups",)
    CLIENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    client_groups: _containers.RepeatedCompositeFieldContainer[ClientGroup]
    def __init__(self, client_groups: _Optional[_Iterable[_Union[ClientGroup, _Mapping]]] = ...) -> None: ...

class ReloadClientDataReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ReloadClientDataResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVisualizationsLegacyReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVisualizationsLegacyRes(_message.Message):
    __slots__ = ("descriptions",)
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    descriptions: _containers.RepeatedCompositeFieldContainer[VizDescription]
    def __init__(self, descriptions: _Optional[_Iterable[_Union[VizDescription, _Mapping]]] = ...) -> None: ...

class VizDescription(_message.Message):
    __slots__ = ("id", "title", "show_the", "watcher", "tcn_modified_date", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SHOW_THE_FIELD_NUMBER: _ClassVar[int]
    WATCHER_FIELD_NUMBER: _ClassVar[int]
    TCN_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    show_the: str
    watcher: bool
    tcn_modified_date: int
    description: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., show_the: _Optional[str] = ..., watcher: bool = ..., tcn_modified_date: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
