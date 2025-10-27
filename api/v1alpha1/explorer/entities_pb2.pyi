from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_FORMAT_UNSPECIFIED: _ClassVar[ExportFormat]
    REPORT_FORMAT_CSV: _ClassVar[ExportFormat]
    REPORT_FORMAT_PARQUET: _ClassVar[ExportFormat]
    REPORT_FORMAT_TSV: _ClassVar[ExportFormat]
    REPORT_FORMAT_TXT: _ClassVar[ExportFormat]

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
    DATASOURCE_TYPE_INSTANT_DATA: _ClassVar[DatasourceType]

class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_TYPE_UNSPECIFIED: _ClassVar[ResultType]
    RESULT_TYPE_FORMAT: _ClassVar[ResultType]
    RESULT_TYPE_SUMMARY: _ClassVar[ResultType]
    RESULT_TYPE_REPORT: _ClassVar[ResultType]

class QuoteCharacter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUOTE_CHARACTER_UNSPECIFIED: _ClassVar[QuoteCharacter]
    QUOTE_CHARACTER_DOUBLE_QUOTE: _ClassVar[QuoteCharacter]
    QUOTE_CHARACTER_SINGLE_QUOTE: _ClassVar[QuoteCharacter]
REPORT_FORMAT_UNSPECIFIED: ExportFormat
REPORT_FORMAT_CSV: ExportFormat
REPORT_FORMAT_PARQUET: ExportFormat
REPORT_FORMAT_TSV: ExportFormat
REPORT_FORMAT_TXT: ExportFormat
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
DATASOURCE_TYPE_INSTANT_DATA: DatasourceType
RESULT_TYPE_UNSPECIFIED: ResultType
RESULT_TYPE_FORMAT: ResultType
RESULT_TYPE_SUMMARY: ResultType
RESULT_TYPE_REPORT: ResultType
QUOTE_CHARACTER_UNSPECIFIED: QuoteCharacter
QUOTE_CHARACTER_DOUBLE_QUOTE: QuoteCharacter
QUOTE_CHARACTER_SINGLE_QUOTE: QuoteCharacter

class SchemaField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_JOIN_COLUMN_FIELD_NUMBER: _ClassVar[int]
    name: str
    column_type: SchemaType
    is_primary_key: bool
    is_low_cardinality: bool
    column_description: str
    is_time_filter: bool
    is_default_time_filter: bool
    is_join_column: bool
    def __init__(self, name: _Optional[str] = ..., column_type: _Optional[_Union[SchemaType, str]] = ..., is_primary_key: _Optional[bool] = ..., is_low_cardinality: _Optional[bool] = ..., column_description: _Optional[str] = ..., is_time_filter: _Optional[bool] = ..., is_default_time_filter: _Optional[bool] = ..., is_join_column: _Optional[bool] = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ()
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
    __slots__ = ()
    class Parameter(_message.Message):
        __slots__ = ()
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        data_type: str
        def __init__(self, value: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...
    class ParametersEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Parameters.Parameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Parameters.Parameter, _Mapping]] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.MessageMap[str, Parameters.Parameter]
    def __init__(self, parameters: _Optional[_Mapping[str, Parameters.Parameter]] = ...) -> None: ...

class ResultFile(_message.Message):
    __slots__ = ()
    URL_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    url: str
    size_bytes: int
    def __init__(self, url: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class ExportOptions(_message.Message):
    __slots__ = ()
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_CHARACTER_FIELD_NUMBER: _ClassVar[int]
    NO_HEADER_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    delimiter: str
    quote_character: QuoteCharacter
    no_header: bool
    export_format: ExportFormat
    def __init__(self, delimiter: _Optional[str] = ..., quote_character: _Optional[_Union[QuoteCharacter, str]] = ..., no_header: _Optional[bool] = ..., export_format: _Optional[_Union[ExportFormat, str]] = ...) -> None: ...
