import datetime

from annotations import authz_pb2 as _authz_pb2
from api.commons import bireportgenerator_pb2 as _bireportgenerator_pb2
from api.v1alpha1.explorer import entities_pb2 as _entities_pb2
from api.v1alpha1.explorer import pipeline_pb2 as _pipeline_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWeeksOfDataRequest(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetWeeksOfDataResponse(_message.Message):
    __slots__ = ()
    WEEKS_OF_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCESS_START_DATE_FIELD_NUMBER: _ClassVar[int]
    weeks_of_data: int
    access_start_date: _timestamp_pb2.Timestamp
    def __init__(self, weeks_of_data: _Optional[int] = ..., access_start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListDatasourceSchemasRequest(_message.Message):
    __slots__ = ()
    DATASOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    datasource_names: _containers.RepeatedScalarFieldContainer[str]
    datasource_type: _entities_pb2.DatasourceType
    def __init__(self, datasource_names: _Optional[_Iterable[str]] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ...) -> None: ...

class ListDatasourceSchemasResponse(_message.Message):
    __slots__ = ()
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[_entities_pb2.Schema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[_entities_pb2.Schema, _Mapping]]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ()
    DATASOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    QUERY_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    UI_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPES_FIELD_NUMBER: _ClassVar[int]
    datasource_name: str
    datasource_type: _entities_pb2.DatasourceType
    pipeline: str
    prql: str
    query_pipeline: _pipeline_pb2.Pipeline
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    timezone: str
    pipeline_parameters: _entities_pb2.Parameters
    ui_trace_id: str
    comment: str
    format: _entities_pb2.ExportFormat
    time_period: _bireportgenerator_pb2.TimePeriod
    report_date: _timestamp_pb2.Timestamp
    export_options: _entities_pb2.ExportOptions
    result_types: _containers.RepeatedScalarFieldContainer[_entities_pb2.ResultType]
    def __init__(self, datasource_name: _Optional[str] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ..., pipeline: _Optional[str] = ..., prql: _Optional[str] = ..., query_pipeline: _Optional[_Union[_pipeline_pb2.Pipeline, _Mapping]] = ..., org_ids: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., timezone: _Optional[str] = ..., pipeline_parameters: _Optional[_Union[_entities_pb2.Parameters, _Mapping]] = ..., ui_trace_id: _Optional[str] = ..., comment: _Optional[str] = ..., format: _Optional[_Union[_entities_pb2.ExportFormat, str]] = ..., time_period: _Optional[_Union[_bireportgenerator_pb2.TimePeriod, str]] = ..., report_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., export_options: _Optional[_Union[_entities_pb2.ExportOptions, _Mapping]] = ..., result_types: _Optional[_Iterable[_Union[_entities_pb2.ResultType, str]]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ()
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    class ResultUrlsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _entities_pb2.ResultFile
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_entities_pb2.ResultFile, _Mapping]] = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_TABLE_QUERY_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_SUMMARY_QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_URLS_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    post_processing_table_query: str
    post_processing_summary_query: str
    result_urls: _containers.MessageMap[int, _entities_pb2.ResultFile]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ..., post_processing_table_query: _Optional[str] = ..., post_processing_summary_query: _Optional[str] = ..., result_urls: _Optional[_Mapping[int, _entities_pb2.ResultFile]] = ...) -> None: ...

class SupportQueryRequest(_message.Message):
    __slots__ = ()
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    query_request: QueryRequest
    debug: bool
    def __init__(self, query_request: _Optional[_Union[QueryRequest, _Mapping]] = ..., debug: _Optional[bool] = ...) -> None: ...

class SupportQueryResponse(_message.Message):
    __slots__ = ()
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    class ResultUrlsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _entities_pb2.ResultFile
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_entities_pb2.ResultFile, _Mapping]] = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_TABLE_QUERY_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_SUMMARY_QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_URLS_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    prql: str
    sql: str
    explain: str
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    post_processing_table_query: str
    post_processing_summary_query: str
    result_urls: _containers.MessageMap[int, _entities_pb2.ResultFile]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., prql: _Optional[str] = ..., sql: _Optional[str] = ..., explain: _Optional[str] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ..., post_processing_table_query: _Optional[str] = ..., post_processing_summary_query: _Optional[str] = ..., result_urls: _Optional[_Mapping[int, _entities_pb2.ResultFile]] = ...) -> None: ...

class QueryExplainRequest(_message.Message):
    __slots__ = ()
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    query_request: QueryRequest
    def __init__(self, query_request: _Optional[_Union[QueryRequest, _Mapping]] = ...) -> None: ...

class QueryExplainResponse(_message.Message):
    __slots__ = ()
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    class ResultUrlsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _entities_pb2.ResultFile
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_entities_pb2.ResultFile, _Mapping]] = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_TABLE_QUERY_FIELD_NUMBER: _ClassVar[int]
    POST_PROCESSING_SUMMARY_QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_URLS_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    prql: str
    sql: str
    explain: str
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    post_processing_table_query: str
    post_processing_summary_query: str
    result_urls: _containers.MessageMap[int, _entities_pb2.ResultFile]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., prql: _Optional[str] = ..., sql: _Optional[str] = ..., explain: _Optional[str] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ..., post_processing_table_query: _Optional[str] = ..., post_processing_summary_query: _Optional[str] = ..., result_urls: _Optional[_Mapping[int, _entities_pb2.ResultFile]] = ...) -> None: ...
