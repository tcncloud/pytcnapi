from api.v0alpha import lms_pb2 as _lms_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileTemplateV2(_message.Message):
    __slots__ = ("legacy_template", "dock_template")
    LEGACY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DOCK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    legacy_template: _lms_pb2.FileTemplate
    dock_template: FileTemplate
    def __init__(self, legacy_template: _Optional[_Union[_lms_pb2.FileTemplate, _Mapping]] = ..., dock_template: _Optional[_Union[FileTemplate, _Mapping]] = ...) -> None: ...

class FileTemplates(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[FileTemplateV2]
    def __init__(self, templates: _Optional[_Iterable[_Union[FileTemplateV2, _Mapping]]] = ...) -> None: ...

class FileTemplate(_message.Message):
    __slots__ = ("org_id", "file_template_id", "filename", "fields", "parse_opts", "foid")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PARSE_OPTS_FIELD_NUMBER: _ClassVar[int]
    FOID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    file_template_id: int
    filename: str
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    parse_opts: ParseOpts
    foid: int
    def __init__(self, org_id: _Optional[str] = ..., file_template_id: _Optional[int] = ..., filename: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., parse_opts: _Optional[_Union[ParseOpts, _Mapping]] = ..., foid: _Optional[int] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("syntax_type", "presi_type", "name", "format", "raw_value")
    SYNTAX_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRESI_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    syntax_type: str
    presi_type: str
    name: str
    format: str
    raw_value: str
    def __init__(self, syntax_type: _Optional[str] = ..., presi_type: _Optional[str] = ..., name: _Optional[str] = ..., format: _Optional[str] = ..., raw_value: _Optional[str] = ...) -> None: ...

class ParseOpts(_message.Message):
    __slots__ = ("csv", "json", "jsonl", "fixed", "parquet")
    CSV_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    JSONL_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    PARQUET_FIELD_NUMBER: _ClassVar[int]
    csv: OptsCsv
    json: OptsJson
    jsonl: OptsJsonL
    fixed: OptsFixed
    parquet: OptsParquet
    def __init__(self, csv: _Optional[_Union[OptsCsv, _Mapping]] = ..., json: _Optional[_Union[OptsJson, _Mapping]] = ..., jsonl: _Optional[_Union[OptsJsonL, _Mapping]] = ..., fixed: _Optional[_Union[OptsFixed, _Mapping]] = ..., parquet: _Optional[_Union[OptsParquet, _Mapping]] = ...) -> None: ...

class OptsCsv(_message.Message):
    __slots__ = ("has_header", "skip_rows", "header", "separator")
    HAS_HEADER_FIELD_NUMBER: _ClassVar[int]
    SKIP_ROWS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    has_header: bool
    skip_rows: int
    header: _containers.RepeatedScalarFieldContainer[str]
    separator: str
    def __init__(self, has_header: bool = ..., skip_rows: _Optional[int] = ..., header: _Optional[_Iterable[str]] = ..., separator: _Optional[str] = ...) -> None: ...

class OptsJson(_message.Message):
    __slots__ = ("records_root",)
    RECORDS_ROOT_FIELD_NUMBER: _ClassVar[int]
    records_root: str
    def __init__(self, records_root: _Optional[str] = ...) -> None: ...

class OptsJsonL(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OptsFixed(_message.Message):
    __slots__ = ("has_header", "header")
    class Field(_message.Message):
        __slots__ = ("starting_position", "field_length")
        STARTING_POSITION_FIELD_NUMBER: _ClassVar[int]
        FIELD_LENGTH_FIELD_NUMBER: _ClassVar[int]
        starting_position: int
        field_length: int
        def __init__(self, starting_position: _Optional[int] = ..., field_length: _Optional[int] = ...) -> None: ...
    HAS_HEADER_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    has_header: bool
    header: _containers.RepeatedCompositeFieldContainer[OptsFixed.Field]
    def __init__(self, has_header: bool = ..., header: _Optional[_Iterable[_Union[OptsFixed.Field, _Mapping]]] = ...) -> None: ...

class OptsParquet(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NewTemplate(_message.Message):
    __slots__ = ("org_id", "filename", "data")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    filename: str
    data: bytes
    def __init__(self, org_id: _Optional[str] = ..., filename: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class ExistingTemplate(_message.Message):
    __slots__ = ("file_template_id", "parse_opts")
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PARSE_OPTS_FIELD_NUMBER: _ClassVar[int]
    file_template_id: int
    parse_opts: ParseOpts
    def __init__(self, file_template_id: _Optional[int] = ..., parse_opts: _Optional[_Union[ParseOpts, _Mapping]] = ...) -> None: ...
