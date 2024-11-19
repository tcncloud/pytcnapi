from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_FORMAT_UNSPECIFIED: _ClassVar[ExportFormat]
    REPORT_FORMAT_CSV: _ClassVar[ExportFormat]
    REPORT_FORMAT_PARQUET: _ClassVar[ExportFormat]

class SchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEMA_TYPE_UNSPECIFIED: _ClassVar[SchemaType]
    SCHEMA_TYPE_INT: _ClassVar[SchemaType]
    SCHEMA_TYPE_FLOAT: _ClassVar[SchemaType]
    SCHEMA_TYPE_STRING: _ClassVar[SchemaType]
    SCHEMA_TYPE_BOOL: _ClassVar[SchemaType]
    SCHEMA_TYPE_TIMESTAMP: _ClassVar[SchemaType]
    SCHEMA_TYPE_INT_ARRAY: _ClassVar[SchemaType]
    SCHEMA_TYPE_FLOAT_ARRAY: _ClassVar[SchemaType]
    SCHEMA_TYPE_STRING_ARRAY: _ClassVar[SchemaType]
    SCHEMA_TYPE_BOOL_ARRAY: _ClassVar[SchemaType]
    SCHEMA_TYPE_MAP: _ClassVar[SchemaType]

class DatasourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASOURCE_TYPE_UNSPECIFIED: _ClassVar[DatasourceType]
    DATASOURCE_TYPE_VFS: _ClassVar[DatasourceType]
    DATASOURCE_TYPE_CLICKHOUSE: _ClassVar[DatasourceType]
REPORT_FORMAT_UNSPECIFIED: ExportFormat
REPORT_FORMAT_CSV: ExportFormat
REPORT_FORMAT_PARQUET: ExportFormat
SCHEMA_TYPE_UNSPECIFIED: SchemaType
SCHEMA_TYPE_INT: SchemaType
SCHEMA_TYPE_FLOAT: SchemaType
SCHEMA_TYPE_STRING: SchemaType
SCHEMA_TYPE_BOOL: SchemaType
SCHEMA_TYPE_TIMESTAMP: SchemaType
SCHEMA_TYPE_INT_ARRAY: SchemaType
SCHEMA_TYPE_FLOAT_ARRAY: SchemaType
SCHEMA_TYPE_STRING_ARRAY: SchemaType
SCHEMA_TYPE_BOOL_ARRAY: SchemaType
SCHEMA_TYPE_MAP: SchemaType
DATASOURCE_TYPE_UNSPECIFIED: DatasourceType
DATASOURCE_TYPE_VFS: DatasourceType
DATASOURCE_TYPE_CLICKHOUSE: DatasourceType

class SchemaField(_message.Message):
    __slots__ = ("name", "column_type", "is_primary_key", "is_low_cardinality", "column_description", "is_time_filter", "is_default_time_filter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    column_type: SchemaType
    is_primary_key: bool
    is_low_cardinality: bool
    column_description: str
    is_time_filter: bool
    is_default_time_filter: bool
    def __init__(self, name: _Optional[str] = ..., column_type: _Optional[_Union[SchemaType, str]] = ..., is_primary_key: bool = ..., is_low_cardinality: bool = ..., column_description: _Optional[str] = ..., is_time_filter: bool = ..., is_default_time_filter: bool = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ("name", "datasource_type", "fields", "table_description", "category", "sub_category")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TABLE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    name: str
    datasource_type: DatasourceType
    fields: _containers.RepeatedCompositeFieldContainer[SchemaField]
    table_description: str
    category: str
    sub_category: str
    def __init__(self, name: _Optional[str] = ..., datasource_type: _Optional[_Union[DatasourceType, str]] = ..., fields: _Optional[_Iterable[_Union[SchemaField, _Mapping]]] = ..., table_description: _Optional[str] = ..., category: _Optional[str] = ..., sub_category: _Optional[str] = ...) -> None: ...

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
