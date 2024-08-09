from api.v1alpha1.explorer import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    __slots__ = ("datasource_name", "datasource_type", "pipeline", "prql", "org_ids", "start_time", "end_time", "timezone", "pipeline_parameters", "ui_trace_id", "comment", "format")
    DATASOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PRQL_FIELD_NUMBER: _ClassVar[int]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    UI_TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    datasource_name: str
    datasource_type: _entities_pb2.DatasourceType
    pipeline: str
    prql: str
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    timezone: str
    pipeline_parameters: _entities_pb2.Parameters
    ui_trace_id: str
    comment: str
    format: _entities_pb2.ExportFormat
    def __init__(self, datasource_name: _Optional[str] = ..., datasource_type: _Optional[_Union[_entities_pb2.DatasourceType, str]] = ..., pipeline: _Optional[str] = ..., prql: _Optional[str] = ..., org_ids: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timezone: _Optional[str] = ..., pipeline_parameters: _Optional[_Union[_entities_pb2.Parameters, _Mapping]] = ..., ui_trace_id: _Optional[str] = ..., comment: _Optional[str] = ..., format: _Optional[_Union[_entities_pb2.ExportFormat, str]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("result_url", "result_size_bytes")
    RESULT_URL_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    result_url: str
    result_size_bytes: int
    def __init__(self, result_url: _Optional[str] = ..., result_size_bytes: _Optional[int] = ...) -> None: ...
