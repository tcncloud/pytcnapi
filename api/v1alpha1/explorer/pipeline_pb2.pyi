from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class ColumnSummaryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLUMN_SUMMARY_TYPE_UNSPECIFIED: _ClassVar[ColumnSummaryType]
    COLUMN_SUMMARY_TYPE_AVG: _ClassVar[ColumnSummaryType]
    COLUMN_SUMMARY_TYPE_SUM: _ClassVar[ColumnSummaryType]
    COLUMN_SUMMARY_TYPE_MIN: _ClassVar[ColumnSummaryType]
    COLUMN_SUMMARY_TYPE_MAX: _ClassVar[ColumnSummaryType]
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
COLUMN_SUMMARY_TYPE_UNSPECIFIED: ColumnSummaryType
COLUMN_SUMMARY_TYPE_AVG: ColumnSummaryType
COLUMN_SUMMARY_TYPE_SUM: ColumnSummaryType
COLUMN_SUMMARY_TYPE_MIN: ColumnSummaryType
COLUMN_SUMMARY_TYPE_MAX: ColumnSummaryType

class Pipeline(_message.Message):
    __slots__ = ("nodes", "format_query")
    NODES_FIELD_NUMBER: _ClassVar[int]
    FORMAT_QUERY_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    format_query: FormatQuery
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., format_query: _Optional[_Union[FormatQuery, _Mapping]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("node_id", "type", "title", "input_ids", "output_ids", "from_node", "filter_node", "derive_node", "group_node", "join_node", "select_node", "aggregate_node", "take_node", "json_node", "map_node", "replace_node", "sort_node", "string_manipulation_node", "transpose_node")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    INPUT_IDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_IDS_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_FIELD_NUMBER: _ClassVar[int]
    FILTER_NODE_FIELD_NUMBER: _ClassVar[int]
    DERIVE_NODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_NODE_FIELD_NUMBER: _ClassVar[int]
    JOIN_NODE_FIELD_NUMBER: _ClassVar[int]
    SELECT_NODE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_NODE_FIELD_NUMBER: _ClassVar[int]
    TAKE_NODE_FIELD_NUMBER: _ClassVar[int]
    JSON_NODE_FIELD_NUMBER: _ClassVar[int]
    MAP_NODE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_NODE_FIELD_NUMBER: _ClassVar[int]
    SORT_NODE_FIELD_NUMBER: _ClassVar[int]
    STRING_MANIPULATION_NODE_FIELD_NUMBER: _ClassVar[int]
    TRANSPOSE_NODE_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    type: str
    title: str
    input_ids: _containers.RepeatedScalarFieldContainer[str]
    output_ids: _containers.RepeatedScalarFieldContainer[str]
    from_node: FromNode
    filter_node: FilterNode
    derive_node: DeriveNode
    group_node: GroupNode
    join_node: JoinNode
    select_node: SelectNode
    aggregate_node: AggregateNode
    take_node: TakeNode
    json_node: JsonNode
    map_node: MapNode
    replace_node: ReplaceNode
    sort_node: SortNode
    string_manipulation_node: StringManipulationNode
    transpose_node: TransposeNode
    def __init__(self, node_id: _Optional[str] = ..., type: _Optional[str] = ..., title: _Optional[str] = ..., input_ids: _Optional[_Iterable[str]] = ..., output_ids: _Optional[_Iterable[str]] = ..., from_node: _Optional[_Union[FromNode, _Mapping]] = ..., filter_node: _Optional[_Union[FilterNode, _Mapping]] = ..., derive_node: _Optional[_Union[DeriveNode, _Mapping]] = ..., group_node: _Optional[_Union[GroupNode, _Mapping]] = ..., join_node: _Optional[_Union[JoinNode, _Mapping]] = ..., select_node: _Optional[_Union[SelectNode, _Mapping]] = ..., aggregate_node: _Optional[_Union[AggregateNode, _Mapping]] = ..., take_node: _Optional[_Union[TakeNode, _Mapping]] = ..., json_node: _Optional[_Union[JsonNode, _Mapping]] = ..., map_node: _Optional[_Union[MapNode, _Mapping]] = ..., replace_node: _Optional[_Union[ReplaceNode, _Mapping]] = ..., sort_node: _Optional[_Union[SortNode, _Mapping]] = ..., string_manipulation_node: _Optional[_Union[StringManipulationNode, _Mapping]] = ..., transpose_node: _Optional[_Union[TransposeNode, _Mapping]] = ...) -> None: ...

class FromNode(_message.Message):
    __slots__ = ("dataset",)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    def __init__(self, dataset: _Optional[str] = ...) -> None: ...

class FilterNode(_message.Message):
    __slots__ = ("expression",)
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    expression: ExpressionNode
    def __init__(self, expression: _Optional[_Union[ExpressionNode, _Mapping]] = ...) -> None: ...

class DeriveNode(_message.Message):
    __slots__ = ("column_name", "expression")
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    expression: ExpressionNode
    def __init__(self, column_name: _Optional[str] = ..., expression: _Optional[_Union[ExpressionNode, _Mapping]] = ...) -> None: ...

class GroupNode(_message.Message):
    __slots__ = ("group_by_columns", "aggregation_columns")
    GROUP_BY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    group_by_columns: _containers.RepeatedScalarFieldContainer[str]
    aggregation_columns: _containers.RepeatedCompositeFieldContainer[AggregationColumn]
    def __init__(self, group_by_columns: _Optional[_Iterable[str]] = ..., aggregation_columns: _Optional[_Iterable[_Union[AggregationColumn, _Mapping]]] = ...) -> None: ...

class TakeNode(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class AggregateNode(_message.Message):
    __slots__ = ("aggregation_columns",)
    AGGREGATION_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    aggregation_columns: _containers.RepeatedCompositeFieldContainer[AggregationColumn]
    def __init__(self, aggregation_columns: _Optional[_Iterable[_Union[AggregationColumn, _Mapping]]] = ...) -> None: ...

class AggregationColumn(_message.Message):
    __slots__ = ("name", "group_by_columns", "column_to_aggregate", "aggregation_function")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TO_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    group_by_columns: _containers.RepeatedScalarFieldContainer[str]
    column_to_aggregate: str
    aggregation_function: str
    def __init__(self, name: _Optional[str] = ..., group_by_columns: _Optional[_Iterable[str]] = ..., column_to_aggregate: _Optional[str] = ..., aggregation_function: _Optional[str] = ...) -> None: ...

class Column(_message.Message):
    __slots__ = ("key", "data_type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    data_type: str
    def __init__(self, key: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...

class ExpressionNode(_message.Message):
    __slots__ = ("type", "value", "children")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    children: _containers.RepeatedCompositeFieldContainer[ExpressionNode]
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ..., children: _Optional[_Iterable[_Union[ExpressionNode, _Mapping]]] = ...) -> None: ...

class MapNode(_message.Message):
    __slots__ = ("new_column", "column_to_map", "mappings", "default_value", "is_complex")
    class Mapping(_message.Message):
        __slots__ = ("condition", "result")
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        condition: ExpressionNode
        result: ExpressionNode
        def __init__(self, condition: _Optional[_Union[ExpressionNode, _Mapping]] = ..., result: _Optional[_Union[ExpressionNode, _Mapping]] = ...) -> None: ...
    NEW_COLUMN_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TO_MAP_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLEX_FIELD_NUMBER: _ClassVar[int]
    new_column: Column
    column_to_map: Column
    mappings: _containers.RepeatedCompositeFieldContainer[MapNode.Mapping]
    default_value: ExpressionNode
    is_complex: bool
    def __init__(self, new_column: _Optional[_Union[Column, _Mapping]] = ..., column_to_map: _Optional[_Union[Column, _Mapping]] = ..., mappings: _Optional[_Iterable[_Union[MapNode.Mapping, _Mapping]]] = ..., default_value: _Optional[_Union[ExpressionNode, _Mapping]] = ..., is_complex: bool = ...) -> None: ...

class JoinNode(_message.Message):
    __slots__ = ("side", "join_columns", "first_parent", "second_parent")
    SIDE_FIELD_NUMBER: _ClassVar[int]
    JOIN_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    FIRST_PARENT_FIELD_NUMBER: _ClassVar[int]
    SECOND_PARENT_FIELD_NUMBER: _ClassVar[int]
    side: str
    join_columns: _containers.RepeatedCompositeFieldContainer[JoinColumn]
    first_parent: Parent
    second_parent: Parent
    def __init__(self, side: _Optional[str] = ..., join_columns: _Optional[_Iterable[_Union[JoinColumn, _Mapping]]] = ..., first_parent: _Optional[_Union[Parent, _Mapping]] = ..., second_parent: _Optional[_Union[Parent, _Mapping]] = ...) -> None: ...

class JoinColumn(_message.Message):
    __slots__ = ("first_parent_column", "second_parent_column")
    FIRST_PARENT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    SECOND_PARENT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    first_parent_column: str
    second_parent_column: str
    def __init__(self, first_parent_column: _Optional[str] = ..., second_parent_column: _Optional[str] = ...) -> None: ...

class Parent(_message.Message):
    __slots__ = ("parent_id", "title", "renamed_columns")
    class RenamedColumnsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RENAMED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent_id: str
    title: str
    renamed_columns: _containers.ScalarMap[str, str]
    def __init__(self, parent_id: _Optional[str] = ..., title: _Optional[str] = ..., renamed_columns: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SelectNode(_message.Message):
    __slots__ = ("columns", "renamed_columns")
    class RenamedColumnsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    RENAMED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    renamed_columns: _containers.ScalarMap[str, str]
    def __init__(self, columns: _Optional[_Iterable[str]] = ..., renamed_columns: _Optional[_Mapping[str, str]] = ...) -> None: ...

class JsonTarget(_message.Message):
    __slots__ = ("path_parts", "column_name", "result_type")
    PATH_PARTS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    path_parts: _containers.RepeatedScalarFieldContainer[str]
    column_name: str
    result_type: str
    def __init__(self, path_parts: _Optional[_Iterable[str]] = ..., column_name: _Optional[str] = ..., result_type: _Optional[str] = ...) -> None: ...

class JsonNode(_message.Message):
    __slots__ = ("type", "json_column", "targets", "unnest_to_columns_node")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JSON_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    UNNEST_TO_COLUMNS_NODE_FIELD_NUMBER: _ClassVar[int]
    type: str
    json_column: str
    targets: _containers.RepeatedCompositeFieldContainer[JsonTarget]
    unnest_to_columns_node: UnnestToColumnsNode
    def __init__(self, type: _Optional[str] = ..., json_column: _Optional[str] = ..., targets: _Optional[_Iterable[_Union[JsonTarget, _Mapping]]] = ..., unnest_to_columns_node: _Optional[_Union[UnnestToColumnsNode, _Mapping]] = ...) -> None: ...

class UnnestToColumnsNode(_message.Message):
    __slots__ = ("unnest_target", "key_target", "value_target", "columns", "primary_keys", "json_columns")
    UNNEST_TARGET_FIELD_NUMBER: _ClassVar[int]
    KEY_TARGET_FIELD_NUMBER: _ClassVar[int]
    VALUE_TARGET_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    JSON_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    unnest_target: JsonTarget
    key_target: JsonTarget
    value_target: JsonTarget
    columns: _containers.RepeatedScalarFieldContainer[str]
    primary_keys: _containers.RepeatedScalarFieldContainer[str]
    json_columns: _containers.RepeatedCompositeFieldContainer[Column]
    def __init__(self, unnest_target: _Optional[_Union[JsonTarget, _Mapping]] = ..., key_target: _Optional[_Union[JsonTarget, _Mapping]] = ..., value_target: _Optional[_Union[JsonTarget, _Mapping]] = ..., columns: _Optional[_Iterable[str]] = ..., primary_keys: _Optional[_Iterable[str]] = ..., json_columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ...) -> None: ...

class ValuesReplacement(_message.Message):
    __slots__ = ("target_value", "target_data_type", "replacement_value")
    TARGET_VALUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    target_value: str
    target_data_type: str
    replacement_value: ExpressionNode
    def __init__(self, target_value: _Optional[str] = ..., target_data_type: _Optional[str] = ..., replacement_value: _Optional[_Union[ExpressionNode, _Mapping]] = ...) -> None: ...

class ColumnReplacement(_message.Message):
    __slots__ = ("column_names", "values_replacements")
    COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    VALUES_REPLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    column_names: _containers.RepeatedScalarFieldContainer[str]
    values_replacements: _containers.RepeatedCompositeFieldContainer[ValuesReplacement]
    def __init__(self, column_names: _Optional[_Iterable[str]] = ..., values_replacements: _Optional[_Iterable[_Union[ValuesReplacement, _Mapping]]] = ...) -> None: ...

class ReplaceNode(_message.Message):
    __slots__ = ("column_replacements", "is_complex")
    COLUMN_REPLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLEX_FIELD_NUMBER: _ClassVar[int]
    column_replacements: _containers.RepeatedCompositeFieldContainer[ColumnReplacement]
    is_complex: bool
    def __init__(self, column_replacements: _Optional[_Iterable[_Union[ColumnReplacement, _Mapping]]] = ..., is_complex: bool = ...) -> None: ...

class SortColumn(_message.Message):
    __slots__ = ("column_name", "ascending")
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    ASCENDING_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    ascending: bool
    def __init__(self, column_name: _Optional[str] = ..., ascending: bool = ...) -> None: ...

class SortNode(_message.Message):
    __slots__ = ("sort_columns",)
    SORT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    sort_columns: _containers.RepeatedCompositeFieldContainer[SortColumn]
    def __init__(self, sort_columns: _Optional[_Iterable[_Union[SortColumn, _Mapping]]] = ...) -> None: ...

class StringManipulationSplit(_message.Message):
    __slots__ = ("split_by", "is_index_extraction", "index_extraction")
    SPLIT_BY_FIELD_NUMBER: _ClassVar[int]
    IS_INDEX_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    INDEX_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    split_by: str
    is_index_extraction: bool
    index_extraction: int
    def __init__(self, split_by: _Optional[str] = ..., is_index_extraction: bool = ..., index_extraction: _Optional[int] = ...) -> None: ...

class StringManipulationReplace(_message.Message):
    __slots__ = ("target", "value")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    target: str
    value: str
    def __init__(self, target: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class StringManipulationNode(_message.Message):
    __slots__ = ("type", "source_column_name", "target_column_name", "string_manipulation_split", "string_manipulation_replace")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_MANIPULATION_SPLIT_FIELD_NUMBER: _ClassVar[int]
    STRING_MANIPULATION_REPLACE_FIELD_NUMBER: _ClassVar[int]
    type: str
    source_column_name: str
    target_column_name: str
    string_manipulation_split: StringManipulationSplit
    string_manipulation_replace: StringManipulationReplace
    def __init__(self, type: _Optional[str] = ..., source_column_name: _Optional[str] = ..., target_column_name: _Optional[str] = ..., string_manipulation_split: _Optional[_Union[StringManipulationSplit, _Mapping]] = ..., string_manipulation_replace: _Optional[_Union[StringManipulationReplace, _Mapping]] = ...) -> None: ...

class TransposeNode(_message.Message):
    __slots__ = ("group_by_columns", "key_column", "options")
    class Option(_message.Message):
        __slots__ = ("key_name", "value_column", "value_type")
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_COLUMN_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        value_column: str
        value_type: str
        def __init__(self, key_name: _Optional[str] = ..., value_column: _Optional[str] = ..., value_type: _Optional[str] = ...) -> None: ...
    GROUP_BY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    KEY_COLUMN_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    group_by_columns: _containers.RepeatedScalarFieldContainer[str]
    key_column: str
    options: _containers.RepeatedCompositeFieldContainer[TransposeNode.Option]
    def __init__(self, group_by_columns: _Optional[_Iterable[str]] = ..., key_column: _Optional[str] = ..., options: _Optional[_Iterable[_Union[TransposeNode.Option, _Mapping]]] = ...) -> None: ...

class FormatQuery(_message.Message):
    __slots__ = ("table_column_configs",)
    TABLE_COLUMN_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    table_column_configs: _containers.RepeatedCompositeFieldContainer[TableColumnConfig]
    def __init__(self, table_column_configs: _Optional[_Iterable[_Union[TableColumnConfig, _Mapping]]] = ...) -> None: ...

class TableColumnConfig(_message.Message):
    __slots__ = ("column_name", "operations", "column_summary")
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    operations: _containers.RepeatedCompositeFieldContainer[ColumnOperation]
    column_summary: ColumnSummaryType
    def __init__(self, column_name: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[ColumnOperation, _Mapping]]] = ..., column_summary: _Optional[_Union[ColumnSummaryType, str]] = ...) -> None: ...

class FormatSeries(_message.Message):
    __slots__ = ("format_parts",)
    FORMAT_PARTS_FIELD_NUMBER: _ClassVar[int]
    format_parts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, format_parts: _Optional[_Iterable[str]] = ...) -> None: ...

class PadOperation(_message.Message):
    __slots__ = ("pad_character", "pad_left", "pad_size")
    PAD_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    PAD_LEFT_FIELD_NUMBER: _ClassVar[int]
    PAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    pad_character: str
    pad_left: bool
    pad_size: int
    def __init__(self, pad_character: _Optional[str] = ..., pad_left: bool = ..., pad_size: _Optional[int] = ...) -> None: ...

class ColumnOperation(_message.Message):
    __slots__ = ("operation_type", "float_value", "format_series", "pad_operation")
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_SERIES_FIELD_NUMBER: _ClassVar[int]
    PAD_OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation_type: OperationType
    float_value: float
    format_series: FormatSeries
    pad_operation: PadOperation
    def __init__(self, operation_type: _Optional[_Union[OperationType, str]] = ..., float_value: _Optional[float] = ..., format_series: _Optional[_Union[FormatSeries, _Mapping]] = ..., pad_operation: _Optional[_Union[PadOperation, _Mapping]] = ...) -> None: ...
