import datetime

from api.commons import insights_pb2 as _insights_pb2
from api.v1alpha1.explorer import entities_pb2 as _entities_pb2
from api.v1alpha1.explorer import pipeline_pb2 as _pipeline_pb2
from api.v1alpha1.insights import insight_content_pb2 as _insight_content_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OutputConfigurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_CONFIGURATION_TYPE_UNSPECIFIED: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_TABLE: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_MULTI_SERIES: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_PIE_CHART: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_FIXED_WIDTH: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_TIMELINE: _ClassVar[OutputConfigurationType]
    OUTPUT_CONFIGURATION_TYPE_TEXT_VALUES: _ClassVar[OutputConfigurationType]

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
    OPERATION_TYPE_PAD: _ClassVar[OperationType]

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

class InsightContextualActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSIGHT_CONTEXTUAL_ACTION_TYPE_UNSPECIFIED: _ClassVar[InsightContextualActionType]
    INSIGHT_CONTEXTUAL_ACTION_TYPE_LINK: _ClassVar[InsightContextualActionType]
    INSIGHT_CONTEXTUAL_ACTION_TYPE_COMPONENT: _ClassVar[InsightContextualActionType]
    INSIGHT_CONTEXTUAL_ACTION_TYPE_DRILL_THROUGH: _ClassVar[InsightContextualActionType]

class QuoteCharacter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUOTE_CHARACTER_UNSPECIFIED: _ClassVar[QuoteCharacter]
    QUOTE_CHARACTER_DOUBLE_QUOTE: _ClassVar[QuoteCharacter]
    QUOTE_CHARACTER_SINGLE_QUOTE: _ClassVar[QuoteCharacter]
OUTPUT_CONFIGURATION_TYPE_UNSPECIFIED: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_TABLE: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_MULTI_SERIES: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_PIE_CHART: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_FIXED_WIDTH: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_TIMELINE: OutputConfigurationType
OUTPUT_CONFIGURATION_TYPE_TEXT_VALUES: OutputConfigurationType
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
OPERATION_TYPE_PAD: OperationType
COLUMN_SORT_UNSPECIFIED: ColumnSort
COLUMN_SORT_ASCENDING: ColumnSort
COLUMN_SORT_DESCENDING: ColumnSort
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_UNSPECIFIED: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_AVG: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_SUM: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MIN: OutputConfigurationColumnSummaryType
OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MAX: OutputConfigurationColumnSummaryType
INSIGHT_CONTEXTUAL_ACTION_TYPE_UNSPECIFIED: InsightContextualActionType
INSIGHT_CONTEXTUAL_ACTION_TYPE_LINK: InsightContextualActionType
INSIGHT_CONTEXTUAL_ACTION_TYPE_COMPONENT: InsightContextualActionType
INSIGHT_CONTEXTUAL_ACTION_TYPE_DRILL_THROUGH: InsightContextualActionType
QUOTE_CHARACTER_UNSPECIFIED: QuoteCharacter
QUOTE_CHARACTER_DOUBLE_QUOTE: QuoteCharacter
QUOTE_CHARACTER_SINGLE_QUOTE: QuoteCharacter

class Insight(_message.Message):
    __slots__ = ()
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_VERSION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STANDARD_INSIGHT_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_BODY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    name: str
    description: str
    insight_type: _insights_pb2.InsightType
    insight_version: int
    body: str
    insight_permission_type: _insights_pb2.InsightPermissionType
    resource_id: str
    standard_insight: bool
    datasource_type: _entities_pb2.DatasourceType
    datasource_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    pipeline: _insight_content_pb2.Pipeline
    insight_body: _pipeline_pb2.Pipeline
    export_options: ExportOptions
    data_export_options: _entities_pb2.ExportOptions
    def __init__(self, insight_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., insight_type: _Optional[_Union[_insights_pb2.InsightType, str]] = ..., insight_version: _Optional[int] = ..., body: _Optional[str] = ..., insight_permission_type: _Optional[_Union[_insights_pb2.InsightPermissionType, str]] = ..., resource_id: _Optional[str] = ..., standard_insight: _Optional[bool] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ..., datasource_name: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pipeline: _Optional[_Union[_insight_content_pb2.Pipeline, _Mapping]] = ..., insight_body: _Optional[_Union[_pipeline_pb2.Pipeline, _Mapping]] = ..., export_options: _Optional[_Union[ExportOptions, _Mapping]] = ..., data_export_options: _Optional[_Union[_entities_pb2.ExportOptions, _Mapping]] = ...) -> None: ...

class PublishInsightRequest(_message.Message):
    __slots__ = ()
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    destination_resource_id: str
    def __init__(self, resource_id: _Optional[str] = ..., destination_resource_id: _Optional[str] = ...) -> None: ...

class PublishInsightResponse(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class CreateInsightRequest(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class CreateInsightResponse(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class ListInsightsRequest(_message.Message):
    __slots__ = ()
    INSIGHT_PERMISSION_TYPES_FIELD_NUMBER: _ClassVar[int]
    insight_permission_types: _containers.RepeatedScalarFieldContainer[_insights_pb2.InsightPermissionType]
    def __init__(self, insight_permission_types: _Optional[_Iterable[_Union[_insights_pb2.InsightPermissionType, str]]] = ...) -> None: ...

class ListInsightsStreamResponse(_message.Message):
    __slots__ = ()
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: Insight
    def __init__(self, insights: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class ListInsightsResponse(_message.Message):
    __slots__ = ()
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]] = ...) -> None: ...

class ListOrgInsightsRequest(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListOrgInsightsResponse(_message.Message):
    __slots__ = ()
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]] = ...) -> None: ...

class UpdateInsightRequest(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInsightResponse(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class DeleteInsightRequest(_message.Message):
    __slots__ = ()
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    resource_id: str
    def __init__(self, insight_id: _Optional[int] = ..., resource_id: _Optional[str] = ...) -> None: ...

class DeleteInsightResponse(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetInsightRequest(_message.Message):
    __slots__ = ()
    INSIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_id: int
    resource_id: str
    def __init__(self, insight_id: _Optional[int] = ..., resource_id: _Optional[str] = ...) -> None: ...

class GetInsightResponse(_message.Message):
    __slots__ = ()
    INSIGHT_FIELD_NUMBER: _ClassVar[int]
    insight: Insight
    def __init__(self, insight: _Optional[_Union[Insight, _Mapping]] = ...) -> None: ...

class GetVfsSchemaRequest(_message.Message):
    __slots__ = ()
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    def __init__(self, alias_name: _Optional[str] = ...) -> None: ...

class GetVfsSchemaResponse(_message.Message):
    __slots__ = ()
    class Field(_message.Message):
        __slots__ = ()
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
    __slots__ = ()
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class ListVfsSchemasRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVfsSchemasResponse(_message.Message):
    __slots__ = ()
    VFS_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    vfs_schemas: _containers.RepeatedCompositeFieldContainer[GetVfsSchemaResponse]
    def __init__(self, vfs_schemas: _Optional[_Iterable[_Union[GetVfsSchemaResponse, _Mapping]]] = ...) -> None: ...

class ExportOptions(_message.Message):
    __slots__ = ()
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    NO_HEADER_FIELD_NUMBER: _ClassVar[int]
    delimiter: str
    quote_character: QuoteCharacter
    no_header: bool
    def __init__(self, delimiter: _Optional[str] = ..., quote_character: _Optional[_Union[QuoteCharacter, str]] = ..., no_header: _Optional[bool] = ...) -> None: ...

class TableVisualization(_message.Message):
    __slots__ = ()
    TABLE_COLUMN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    NO_HEADER_FIELD_NUMBER: _ClassVar[int]
    HEADER_BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    table_column_details: _containers.RepeatedCompositeFieldContainer[TableColumnConfig]
    delimiter: str
    quote_character: QuoteCharacter
    no_header: bool
    header_background_color: str
    header_text_color: str
    def __init__(self, table_column_details: _Optional[_Iterable[_Union[TableColumnConfig, _Mapping]]] = ..., delimiter: _Optional[str] = ..., quote_character: _Optional[_Union[QuoteCharacter, str]] = ..., no_header: _Optional[bool] = ..., header_background_color: _Optional[str] = ..., header_text_color: _Optional[str] = ...) -> None: ...

class CardVisualization(_message.Message):
    __slots__ = ()
    TEXT_VALUES_FIELD_NUMBER: _ClassVar[int]
    text_values: _containers.RepeatedCompositeFieldContainer[TextValue]
    def __init__(self, text_values: _Optional[_Iterable[_Union[TextValue, _Mapping]]] = ...) -> None: ...

class TextValue(_message.Message):
    __slots__ = ()
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.RepeatedCompositeFieldContainer[TextValueCondition]
    def __init__(self, conditions: _Optional[_Iterable[_Union[TextValueCondition, _Mapping]]] = ...) -> None: ...

class TextValueCondition(_message.Message):
    __slots__ = ()
    class Color(_message.Message):
        __slots__ = ()
        RED_FIELD_NUMBER: _ClassVar[int]
        GREEN_FIELD_NUMBER: _ClassVar[int]
        BLUE_FIELD_NUMBER: _ClassVar[int]
        red: int
        green: int
        blue: int
        def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    ICON_NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_COLOR_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    expression: _insight_content_pb2.ExpressionNode
    size: int
    operations: _containers.RepeatedCompositeFieldContainer[ColumnOperation]
    icon_name: str
    icon_color: TextValueCondition.Color
    expression_node: _pipeline_pb2.ExpressionNode
    condition_expression: _pipeline_pb2.ExpressionNode
    result_expression: _pipeline_pb2.ExpressionNode
    def __init__(self, expression: _Optional[_Union[_insight_content_pb2.ExpressionNode, _Mapping]] = ..., size: _Optional[int] = ..., operations: _Optional[_Iterable[_Union[ColumnOperation, _Mapping]]] = ..., icon_name: _Optional[str] = ..., icon_color: _Optional[_Union[TextValueCondition.Color, _Mapping]] = ..., expression_node: _Optional[_Union[_pipeline_pb2.ExpressionNode, _Mapping]] = ..., condition_expression: _Optional[_Union[_pipeline_pb2.ExpressionNode, _Mapping]] = ..., result_expression: _Optional[_Union[_pipeline_pb2.ExpressionNode, _Mapping]] = ...) -> None: ...

class TableColumnConfig(_message.Message):
    __slots__ = ()
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    HIDE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    RENAMED_AS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_CONTEXTUAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    column_width: int
    hide_column: bool
    renamed_as: str
    operations: _containers.RepeatedCompositeFieldContainer[ColumnOperation]
    column_summary: OutputConfigurationColumnSummaryType
    description: str
    sort_direction: ColumnSort
    insight_contextual_action: InsightContextualAction
    def __init__(self, column_name: _Optional[str] = ..., column_width: _Optional[int] = ..., hide_column: _Optional[bool] = ..., renamed_as: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[ColumnOperation, _Mapping]]] = ..., column_summary: _Optional[_Union[OutputConfigurationColumnSummaryType, str]] = ..., description: _Optional[str] = ..., sort_direction: _Optional[_Union[ColumnSort, str]] = ..., insight_contextual_action: _Optional[_Union[InsightContextualAction, _Mapping]] = ...) -> None: ...

class FormatSeries(_message.Message):
    __slots__ = ()
    FORMAT_PARTS_FIELD_NUMBER: _ClassVar[int]
    format_parts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, format_parts: _Optional[_Iterable[str]] = ...) -> None: ...

class PadOperation(_message.Message):
    __slots__ = ()
    PAD_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    PAD_LEFT_FIELD_NUMBER: _ClassVar[int]
    PAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    pad_character: str
    pad_left: bool
    pad_size: int
    def __init__(self, pad_character: _Optional[str] = ..., pad_left: _Optional[bool] = ..., pad_size: _Optional[int] = ...) -> None: ...

class ColumnOperation(_message.Message):
    __slots__ = ()
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_SERIES_FIELD_NUMBER: _ClassVar[int]
    PAD_OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation_type: OperationType
    float_value: float
    format_series: FormatSeries
    pad_operation: PadOperation
    def __init__(self, operation_type: _Optional[_Union[OperationType, str]] = ..., float_value: _Optional[float] = ..., format_series: _Optional[_Union[FormatSeries, _Mapping]] = ..., pad_operation: _Optional[_Union[PadOperation, _Mapping]] = ...) -> None: ...

class InsightContextualAction(_message.Message):
    __slots__ = ()
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DRILL_THROUGH_FIELD_NUMBER: _ClassVar[int]
    type: InsightContextualActionType
    link: LinkAction
    component: ComponentAction
    drill_through: DrillThroughAction
    def __init__(self, type: _Optional[_Union[InsightContextualActionType, str]] = ..., link: _Optional[_Union[LinkAction, _Mapping]] = ..., component: _Optional[_Union[ComponentAction, _Mapping]] = ..., drill_through: _Optional[_Union[DrillThroughAction, _Mapping]] = ...) -> None: ...

class LinkAction(_message.Message):
    __slots__ = ()
    class ComponentValueEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LINK_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    link_elements: _containers.RepeatedScalarFieldContainer[str]
    component_value: _containers.ScalarMap[str, str]
    def __init__(self, link_elements: _Optional[_Iterable[str]] = ..., component_value: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ComponentAction(_message.Message):
    __slots__ = ()
    class ComponentValueEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    component_name: str
    component_value: _containers.ScalarMap[str, str]
    def __init__(self, component_name: _Optional[str] = ..., component_value: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DrillThroughAction(_message.Message):
    __slots__ = ()
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DRILL_THROUGH_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    insight_resource_id: str
    drill_through_parameters: _containers.RepeatedCompositeFieldContainer[DrillThroughParameter]
    def __init__(self, insight_resource_id: _Optional[str] = ..., drill_through_parameters: _Optional[_Iterable[_Union[DrillThroughParameter, _Mapping]]] = ...) -> None: ...

class DrillThroughParameter(_message.Message):
    __slots__ = ()
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    parameter_name: str
    column_name: str
    def __init__(self, parameter_name: _Optional[str] = ..., column_name: _Optional[str] = ...) -> None: ...

class OutputConfiguration(_message.Message):
    __slots__ = ()
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_TITLE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    TABLE_VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    CARD_VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    output_configuration_title: str
    output_configuration_type: OutputConfigurationType
    insight_resource_id: str
    is_default: bool
    blob: str
    table_visualization: TableVisualization
    card_visualization: CardVisualization
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, resource_id: _Optional[str] = ..., output_configuration_title: _Optional[str] = ..., output_configuration_type: _Optional[_Union[OutputConfigurationType, str]] = ..., insight_resource_id: _Optional[str] = ..., is_default: _Optional[bool] = ..., blob: _Optional[str] = ..., table_visualization: _Optional[_Union[TableVisualization, _Mapping]] = ..., card_visualization: _Optional[_Union[CardVisualization, _Mapping]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class CreateOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class ListOutputConfigurationsRequest(_message.Message):
    __slots__ = ()
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_resource_id: str
    def __init__(self, insight_resource_id: _Optional[str] = ...) -> None: ...

class ListOutputConfigurationsResponse(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    output_configurations: _containers.RepeatedCompositeFieldContainer[OutputConfiguration]
    def __init__(self, output_configurations: _Optional[_Iterable[_Union[OutputConfiguration, _Mapping]]] = ...) -> None: ...

class UpdateOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    output_configuration: OutputConfiguration
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class UpdateOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class DeleteOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class DeleteOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class GetOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...

class SetDefaultOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    insight_resource_id: str
    def __init__(self, resource_id: _Optional[str] = ..., insight_resource_id: _Optional[str] = ...) -> None: ...

class SetDefaultOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultOutputConfigurationRequest(_message.Message):
    __slots__ = ()
    INSIGHT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    insight_resource_id: str
    def __init__(self, insight_resource_id: _Optional[str] = ...) -> None: ...

class GetDefaultOutputConfigurationResponse(_message.Message):
    __slots__ = ()
    OUTPUT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    output_configuration: OutputConfiguration
    def __init__(self, output_configuration: _Optional[_Union[OutputConfiguration, _Mapping]] = ...) -> None: ...
