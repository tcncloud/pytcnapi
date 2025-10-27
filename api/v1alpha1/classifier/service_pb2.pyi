import datetime

from annotations import authz_pb2 as _authz_pb2
from api.commons import classifier_pb2 as _classifier_pb2
from api.v1alpha1.classifier import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParseFileRequest(_message.Message):
    __slots__ = ()
    class ReParseFile(_message.Message):
        __slots__ = ()
        FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        HINTS_FIELD_NUMBER: _ClassVar[int]
        OPTS_FIELD_NUMBER: _ClassVar[int]
        file_template_id: int
        hints: _entities_pb2.ParseHints
        opts: _entities_pb2.Opts
        def __init__(self, file_template_id: _Optional[int] = ..., hints: _Optional[_Union[_entities_pb2.ParseHints, _Mapping]] = ..., opts: _Optional[_Union[_entities_pb2.Opts, _Mapping]] = ...) -> None: ...
    class ParseWithHints(_message.Message):
        __slots__ = ()
        RAW_DATA_FIELD_NUMBER: _ClassVar[int]
        OPTS_FIELD_NUMBER: _ClassVar[int]
        raw_data: bytes
        opts: _entities_pb2.Opts
        def __init__(self, raw_data: _Optional[bytes] = ..., opts: _Optional[_Union[_entities_pb2.Opts, _Mapping]] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    REPARSE_FILE_FIELD_NUMBER: _ClassVar[int]
    PARSE_WITH_HINTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    raw_data: bytes
    reparse_file: ParseFileRequest.ReParseFile
    parse_with_hints: ParseFileRequest.ParseWithHints
    name: str
    def __init__(self, raw_data: _Optional[bytes] = ..., reparse_file: _Optional[_Union[ParseFileRequest.ReParseFile, _Mapping]] = ..., parse_with_hints: _Optional[_Union[ParseFileRequest.ParseWithHints, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ParseFileResponse(_message.Message):
    __slots__ = ()
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...

class UpdateFileTemplateRequest(_message.Message):
    __slots__ = ()
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...

class UpdateFileTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFileTemplateRequest(_message.Message):
    __slots__ = ()
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: int
    def __init__(self, file_template: _Optional[int] = ...) -> None: ...

class DeleteFileTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFileTemplatesRequest(_message.Message):
    __slots__ = ()
    PREV_ID_FIELD_NUMBER: _ClassVar[int]
    ASC_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    prev_id: int
    asc: bool
    page_size: int
    def __init__(self, prev_id: _Optional[int] = ..., asc: _Optional[bool] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListFileTemplatesResponse(_message.Message):
    __slots__ = ()
    FILE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    file_templates: _containers.RepeatedCompositeFieldContainer[_entities_pb2.FileTemplate]
    def __init__(self, file_templates: _Optional[_Iterable[_Union[_entities_pb2.FileTemplate, _Mapping]]] = ...) -> None: ...

class GetFileTemplateRequest(_message.Message):
    __slots__ = ()
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    file_template_id: int
    def __init__(self, file_template_id: _Optional[int] = ...) -> None: ...

class GetFileTemplateResponse(_message.Message):
    __slots__ = ()
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...

class ListEventsRequest(_message.Message):
    __slots__ = ()
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    time_range: str
    entrypoint_id: str
    parent_id: str
    def __init__(self, element_id: _Optional[str] = ..., begin: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_range: _Optional[str] = ..., entrypoint_id: _Optional[str] = ..., parent_id: _Optional[str] = ...) -> None: ...

class ListEventsResponse(_message.Message):
    __slots__ = ()
    class Row(_message.Message):
        __slots__ = ()
        INPUT_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISCARDED_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        BEGIN_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ENTRYPOINTS_FIELD_NUMBER: _ClassVar[int]
        PARENT_IDS_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_QUEUE_WAIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PROCESSING_SECONDS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_QUEUE_WAIT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PROCESSING_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
        MSGS_FIELD_NUMBER: _ClassVar[int]
        input_record_count: int
        output_record_count: int
        discarded_record_count: int
        begin: _timestamp_pb2.Timestamp
        end: _timestamp_pb2.Timestamp
        element_id: str
        entrypoints: _containers.RepeatedScalarFieldContainer[str]
        parent_ids: _containers.RepeatedScalarFieldContainer[str]
        columns: _containers.RepeatedScalarFieldContainer[str]
        total_queue_wait_seconds: int
        total_processing_seconds: int
        total_queue_wait_milliseconds: int
        total_processing_milliseconds: int
        msgs: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, input_record_count: _Optional[int] = ..., output_record_count: _Optional[int] = ..., discarded_record_count: _Optional[int] = ..., begin: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., element_id: _Optional[str] = ..., entrypoints: _Optional[_Iterable[str]] = ..., parent_ids: _Optional[_Iterable[str]] = ..., columns: _Optional[_Iterable[str]] = ..., total_queue_wait_seconds: _Optional[int] = ..., total_processing_seconds: _Optional[int] = ..., total_queue_wait_milliseconds: _Optional[int] = ..., total_processing_milliseconds: _Optional[int] = ..., msgs: _Optional[_Iterable[str]] = ...) -> None: ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[ListEventsResponse.Row]
    def __init__(self, rows: _Optional[_Iterable[_Union[ListEventsResponse.Row, _Mapping]]] = ...) -> None: ...

class PeekListRequest(_message.Message):
    __slots__ = ()
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TAG_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ASC_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    begin: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    external_tag: str
    page_token: str
    asc: bool
    page_size: int
    element_id: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    entrypoint_id: str
    parent_id: str
    view_discards: bool
    def __init__(self, begin: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., external_tag: _Optional[str] = ..., page_token: _Optional[str] = ..., asc: _Optional[bool] = ..., page_size: _Optional[int] = ..., element_id: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., entrypoint_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., view_discards: _Optional[bool] = ...) -> None: ...

class PeekListResponse(_message.Message):
    __slots__ = ()
    JSON_RECORDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    json_records: _containers.RepeatedScalarFieldContainer[str]
    page_token: str
    def __init__(self, json_records: _Optional[_Iterable[str]] = ..., page_token: _Optional[str] = ...) -> None: ...
