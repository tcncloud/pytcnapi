from api.commons import insights_pb2 as _insights_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OutputConfigurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_CONFIGURATION_TYPE_UNSPECIFIED: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_TABLE: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_MULTI_SERIES: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_PIE_CHART: _ClassVar[OutputConfigurationType]

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_TYPE_UNSPECIFIED: _ClassVar[OperationType]
    OPERATION_TYPE_DATE: _ClassVar[OperationType]
    OPERATION_TYPE_PREFIX: _ClassVar[OperationType]
    OPERATION_TYPE_SUFFIX: _ClassVar[OperationType]
    OPERATION_TYPE_DURATION: _ClassVar[OperationType]
    OPERATION_TYPE_ADD: _ClassVar[OperationType]
    OPERATION_TYPE_SUBTRACT: _ClassVar[OperationType]
    OPERATION_TYPE_MULTIPLY: _ClassVar[OperationType]
    OPERATION_TYPE_DIVIDE: _ClassVar[OperationType]
    OPERATION_TYPE_FORMAT_NUMBER: _ClassVar[OperationType]
    OPERATION_TYPE_PRECISION: _ClassVar[OperationType]

class ColumnSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLUMN_SORT_UNSPECIFIED: _ClassVar[ColumnSort]
    COLUMN_SORT_ASCENDING: _ClassVar[ColumnSort]
    COLUMN_SORT_DESCENDING: _ClassVar[ColumnSort]

class OutputConfigurationColumnSummaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_UNSPECIFIED: _ClassVar[OutputConfigurationColumnSummaryType]
    OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_AVG: _ClassVar[OutputConfigurationColumnSummaryType]
    OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_SUM: _ClassVar[OutputConfigurationColumnSummaryType]
    OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MIN: _ClassVar[OutputConfigurationColumnSummaryType]
    OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MAX: _ClassVar[OutputConfigurationColumnSummaryType]
OUTPUT_CONFIGURATION_TYPE_UNSPECIFIED: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_TABLE: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_MULTI_SERIES: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_PIE_CHART: OutputConfigurationType
OPERATION_TYPE_UNSPECIFIED: OperationType
OPERATION_TYPE_DATE: OperationType
OPERATION_TYPE_PREFIX: OperationType
OPERATION_TYPE_SUFFIX: OperationType
OPERATION_TYPE_DURATION: OperationType
OPERATION_TYPE_ADD: OperationType
OPERATION_TYPE_SUBTRACT: OperationType
OPERATION_TYPE_MULTIPLY: OperationType
OPERATION_TYPE_DIVIDE: OperationType
OPERATION_TYPE_FORMAT_NUMBER: OperationType
OPERATION_TYPE_PRECISION: OperationType
COLUMN_SORT_UNSPECIFIED: ColumnSort
COLUMN_SORT_ASCENDING: ColumnSort
COLUMN_SORT_DESCENDING: ColumnSort
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_UNSPECIFIED: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_AVG: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_SUM: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MIN: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MAX: OutputConfigurationColumnSummaryType

class Insight(_message.Message):
    __slots__ = ("insight_id", "name", "description", "insight_type", "insight_version", "body", "insight_permission_type", "resource_id", "standard_insight")
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_VERSION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STANDARD_INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    name: str
    description: str
    insight_type: _insights_pb2.InsightType
    insight_version: int
    body: str
    insight_permission_type: _insights_pb2.InsightPermissionType
    resource_id: str
    standard_insight: bool
    def __init__(self, insight_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., insight_type: _Optional[_Union[_insights_pb2.InsightType, str]] = ..., insight_version: _Optional[int] = ..., body: _Optional[str] = ..., insight_permission_type: _Optional[_Union[_insights_pb2.InsightPermissionType, str]] = ..., resource_id: _Optional[str] = ..., standard_insight: bool = ...) -> None: ...

class PublishInsightRequest(_message.Message):
    __slots__ = ("resource_id", "destination_resource_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    destination_resource_id: str
    def __init__(self, resource_id: _Optional[str] = ..., destination_resource_id: _Optional[str] = ...) -> None: ...

class PublishInsightResponse(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class CreateInsightRequest(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class CreateInsightResponse(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class ListInsightsRequest(_message.Message):
    __slots__ = ("insight_permission_types",)
    INSIGHT_PERMISSION_TYPES_FIELD_NUMBER: _ClassVar[int]
    insight_permission_types: _containers.RepeatedScalarFieldContainer[_insights_pb2.InsightPermissionType]
    def __init__(self, insight_permission_types: _Optional[_Iterable[_Union[_insights_pb2.InsightPermissionType, str]]] = ...) -> None: ...

class ListInsightsResponse(_message.Message):
    __slots__ = ("insights",)
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]] = ...) -> None: ...

class ListOrgInsightsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListOrgInsightsResponse(_message.Message):
    __slots__ = ("insights",)
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]] = ...) -> None: ...

class UpdateInsightRequest(_message.Message):
    __slots__ = ("insight", "update_mask")
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInsightResponse(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class DeleteInsightRequest(_message.Message):
    __slots__ = ("insight_id", "resource_id")
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    resource_id: str
    def __init__(self, insight_id: _Optional[int] = ..., resource_id: _Optional[str] = ...) -> None: ...

class DeleteInsightResponse(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetInsightRequest(_message.Message):
    __slots__ = ("insight_id", "resource_id")
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    resource_id: str
    def __init__(self, insight_id: _Optional[int] = ..., resource_id: _Optional[str] = ...) -> None: ...

class GetInsightResponse(_message.Message):
    __slots__ = ("insight",)
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetVfsSchemaRequest(_message.Message):
    __slots__ = ("alias_name",)
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    def __init__(self, alias_name: _Optional[str] = ...) -> None: ...

class GetVfsSchemaResponse(_message.Message):
    __slots__ = ("fields", "vfs_description", "alias_name")
    class Field(_message.Message):
        __slots__ = ("column_name", "column_type", "column_description")
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        column_type: _insights_pb2.InsightVfsSchemaType
        column_description: str
        def __init__(self, column_name: _Optional[str] = ..., column_type: _Optional[_Union[_insights_pb2.InsightVfsSchemaType, str]] = ..., column_description: _Optional[str] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    VFS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[GetVfsSchemaResponse.Field]
    vfs_description: str
    alias_name: str
    def __init__(self, fields: _Optional[_Iterable[_Union[GetVfsSchemaResponse.Field, _Mapping]]] = ..., vfs_description: _Optional[str] = ..., alias_name: _Optional[str] = ...) -> None: ...

class ListVfsesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVfsesResponse(_message.Message):
    __slots__ = ("aliases",)
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class ListVfsSchemasRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVfsSchemasResponse(_message.Message):
    __slots__ = ("vfs_schemas",)
    VFS_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    vfs_schemas: _containers.RepeatedCompositeFieldContainer[GetVfsSchemaResponse]
    def __init__(self, vfs_schemas: _Optional[_Iterable[_Union[GetVfsSchemaResponse, _Mapping]]] = ...) -> None: ...

class TableVisualization(_message.Message):
    __slots__ = ("table_column_details",)
    TABLE_COLUMN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    table_column_details: _containers.RepeatedCompositeFieldContainer[TableColumnConfig]
    def __init__(self, table_column_details: _Optional[_Iterable[_Union[TableColumnConfig, _Mapping]]] = ...) -> None: ...

class TableColumnConfig(_message.Message):
    __slots__ = ("column_name", "column_width", "hide_column", "renamed_as", "operations", "column_summary", "description", "sort_direction")
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    HIDE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    RENAMED_AS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    column_width: int
    hide_column: bool
    renamed_as: str
    operations: _containers.RepeatedCompositeFieldContainer[ColumnOperation]
    column_summary: OutputConfigurationColumnSummaryType
    description: str
    sort_direction: ColumnSort
    def __init__(self, column_name: _Optional[str] = ..., column_width: _Optional[int] = ..., hide_column: bool = ..., renamed_as: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[ColumnOperation, _Mapping]]] = ..., column_summary: _Optional[_Union[OutputConfigurationColumnSummaryType, str]] = ..., description: _Optional[str] = ..., sort_direction: _Optional[_Union[ColumnSort, str]] = ...) -> None: ...

class FormatSeries(_message.Message):
    __slots__ = ("format_parts",)
    FORMAT_PARTS_FIELD_NUMBER: _ClassVar[int]
    format_parts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, format_parts: _Optional[_Iterable[str]] = ...) -> None: ...

class ColumnOperation(_message.Message):
    __slots__ = ("operation_type", "float_value", "format_series")
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_SERIES_FIELD_NUMBER: _ClassVar[int]
    operation_type: OperationType
    float_value: float
    format_series: FormatSeries
    def __init__(self, operation_type: _Optional[_Union[OperationType, str]] = ..., float_value: _Optional[float] = ..., format_series: _Optional[_Union[FormatSeries, _Mapping]] = ...) -> None: ...

class OutputConfiguration(_message.Message):
    __slots__ = ("resource_id", "output_configuration_title", "output_configuration_type", "insight_resource_id", "is_default", "blob", "table_visualization")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_TITLE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    TABLE_VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    output_configuration_title: str
    output_configuration_type: OutputConfigurationType
    insight_resource_id: str
    is_default: bool
    blob: str
    table_visualization: TableVisualization
    def __init__(self, resource_id: _Optional[str] = ..., output_configuration_title: _Optional[str] = ..., output_configuration_type: _Optional[_Union[OutputConfigurationType, str]] = ..., insight_resource_id: _Optional[str] = ..., is_default: bool = ..., blob: _Optional[str] = ..., table_visualization: _Optional[_Union[TableVisualization, _Mapping]] = ...) -> None: ...

class CreateOutputConfigurationRequest(_message.Message):
    __slots__ = ("output_configuration",)
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class CreateOutputConfigurationResponse(_message.Message):
    __slots__ = ("output_configuration",)
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class ListOutputConfigurationsRequest(_message.Message):
    __slots__ = ("insight_resource_id",)
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_resource_id: str
    def __init__(self, insight_resource_id: _Optional[str] = ...) -> None: ...

class ListOutputConfigurationsResponse(_message.Message):
    __slots__ = ("output_configurations",)
    OUTPUT_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    output_configurations: _containers.RepeatedCompositeFieldContainer[OutputConfiguration]
    def __init__(self, output_configurations: _Optional[_Iterable[_Union[OutputConfiguration, _Mapping]]] = ...) -> None: ...

class UpdateOutputConfigurationRequest(_message.Message):
    __slots__ = ("update_mask", "output_configuration")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    output_configuration: OutputConfiguration
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class UpdateOutputConfigurationResponse(_message.Message):
    __slots__ = ("output_configuration",)
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class DeleteOutputConfigurationRequest(_message.Message):
    __slots__ = ("resource_id",)
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class DeleteOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOutputConfigurationRequest(_message.Message):
    __slots__ = ("resource_id",)
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class GetOutputConfigurationResponse(_message.Message):
    __slots__ = ("output_configuration",)
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class SetDefaultOutputConfigurationRequest(_message.Message):
    __slots__ = ("resource_id", "insight_resource_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    insight_resource_id: str
    def __init__(self, resource_id: _Optional[str] = ..., insight_resource_id: _Optional[str] = ...) -> None: ...

class SetDefaultOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultOutputConfigurationRequest(_message.Message):
    __slots__ = ("insight_resource_id",)
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_resource_id: str
    def __init__(self, insight_resource_id: _Optional[str] = ...) -> None: ...

class GetDefaultOutputConfigurationResponse(_message.Message):
    __slots__ = ("output_configuration",)
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...
