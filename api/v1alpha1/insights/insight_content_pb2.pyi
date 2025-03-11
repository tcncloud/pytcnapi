from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pipeline(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("node_id", "type", "title", "input_ids", "output_ids", "from_node", "filter_node", "derive_node", "group_node", "join_node", "select_node", "aggregate_node", "take_node", "json_node", "map_node", "replace_node", "sort_node", "string_manipulation_node")
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
    def __init__(self, node_id: _Optional[str] = ..., type: _Optional[str] = ..., title: _Optional[str] = ..., input_ids: _Optional[_Iterable[str]] = ..., output_ids: _Optional[_Iterable[str]] = ..., from_node: _Optional[_Union[FromNode, _Mapping]] = ..., filter_node: _Optional[_Union[FilterNode, _Mapping]] = ..., derive_node: _Optional[_Union[DeriveNode, _Mapping]] = ..., group_node: _Optional[_Union[GroupNode, _Mapping]] = ..., join_node: _Optional[_Union[JoinNode, _Mapping]] = ..., select_node: _Optional[_Union[SelectNode, _Mapping]] = ..., aggregate_node: _Optional[_Union[AggregateNode, _Mapping]] = ..., take_node: _Optional[_Union[TakeNode, _Mapping]] = ..., json_node: _Optional[_Union[JsonNode, _Mapping]] = ..., map_node: _Optional[_Union[MapNode, _Mapping]] = ..., replace_node: _Optional[_Union[ReplaceNode, _Mapping]] = ..., sort_node: _Optional[_Union[SortNode, _Mapping]] = ..., string_manipulation_node: _Optional[_Union[StringManipulationNode, _Mapping]] = ...) -> None: ...

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

class Parameters(_message.Message):
    __slots__ = ("parameters",)
    class Parameter(_message.Message):
        __slots__ = ("value", "data_type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        data_type: str
        def __init__(self, value: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Parameters.Parameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Parameters.Parameter, _Mapping]] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.MessageMap[str, Parameters.Parameter]
    def __init__(self, parameters: _Optional[_Mapping[str, Parameters.Parameter]] = ...) -> None: ...

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
