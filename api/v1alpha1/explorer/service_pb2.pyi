from annotations import authz_pb2 as _authz_pb2
from api.commons import bireportgenerator_pb2 as _bireportgenerator_pb2
from api.v1alpha1.explorer import entities_pb2 as _entities_pb2
from api.v1alpha1.insights import insight_content_pb2 as _insight_content_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWeeksOfDataRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetWeeksOfDataResponse(_message.Message):
    __slots__ = ("weeks_of_data", "access_start_date")
    WEEKS_OF_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCESS_START_DATE_FIELD_NUMBER: _ClassVar[int]
    weeks_of_data: int
    access_start_date: _timestamp_pb2.Timestamp
    def __init__(self, weeks_of_data: _Optional[int] = ..., access_start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListDatasourceSchemasRequest(_message.Message):
    __slots__ = ("datasource_names", "datasource_type")
    DATASOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    datasource_names: _containers.RepeatedScalarFieldContainer[str]
    datasource_type: _entities_pb2.DatasourceType
    def __init__(self, datasource_names: _Optional[_Iterable[str]] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ...) -> None: ...

class ListDatasourceSchemasResponse(_message.Message):
    __slots__ = ("schemas",)
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[_entities_pb2.Schema]
    def __init__(self, schemas: _Optional[_Iterable[_Union[_entities_pb2.Schema, _Mapping]]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("datasource_name", "datasource_type", "pipeline", "prql", "insight_body", "org_ids", "start_time", "end_time", "timezone", "pipeline_parameters", "ui_trace_id", "comment", "format", "time_period", "report_date")
    DATASOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_BODY_FIELD_NUMBER: _ClassVar[int]
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
    datasource_name: str
    datasource_type: _entities_pb2.DatasourceType
    pipeline: str
    prql: str
    insight_body: _insight_content_pb2.Pipeline
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
    def __init__(self, datasource_name: _Optional[str] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ..., pipeline: _Optional[str] = ..., prql: _Optional[str] = ..., insight_body: _Optional[_Union[_insight_content_pb2.Pipeline, _Mapping]] = ..., org_ids: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timezone: _Optional[str] = ..., pipeline_parameters: _Optional[_Union[_entities_pb2.Parameters, _Mapping]] = ..., ui_trace_id: _Optional[str] = ..., comment: _Optional[str] = ..., format: _Optional[_Union[_entities_pb2.ExportFormat, str]] = ..., time_period: _Optional[_Union[_bireportgenerator_pb2.TimePeriod, str]] = ..., report_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("result_url", "result_size_bytes", "time_filtered_datasources")
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class SupportQueryRequest(_message.Message):
    __slots__ = ("query_request", "debug")
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    query_request: QueryRequest
    debug: bool
    def __init__(self, query_request: _Optional[_Union[QueryRequest, _Mapping]] = ..., debug: bool = ...) -> None: ...

class SupportQueryResponse(_message.Message):
    __slots__ = ("result_url", "result_size_bytes", "prql", "sql", "explain", "time_filtered_datasources")
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    prql: str
    sql: str
    explain: str
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., prql: _Optional[str] = ..., sql: _Optional[str] = ..., explain: _Optional[str] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class QueryExplainRequest(_message.Message):
    __slots__ = ("query_request",)
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    query_request: QueryRequest
    def __init__(self, query_request: _Optional[_Union[QueryRequest, _Mapping]] = ...) -> None: ...

class QueryExplainResponse(_message.Message):
    __slots__ = ("result_url", "result_size_bytes", "prql", "sql", "explain", "time_filtered_datasources")
    class TimeFilteredDatasourcesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERED_DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    prql: str
    sql: str
    explain: str
    time_filtered_datasources: _containers.ScalarMap[str, bool]
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ..., prql: _Optional[str] = ..., sql: _Optional[str] = ..., explain: _Optional[str] = ..., time_filtered_datasources: _Optional[_Mapping[str, bool]] = ...) -> None: ...
