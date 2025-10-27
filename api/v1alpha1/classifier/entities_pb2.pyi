from api.commons import classifier_pb2 as _classifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClassifierEntityTypes(_message.Message):
    __slots__ = ()
    TYPES_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[_classifier_pb2.ClassifierEntityType]
    def __init__(self, types: _Optional[_Iterable[_Union[_classifier_pb2.ClassifierEntityType, str]]] = ...) -> None: ...

class FileTemplate(_message.Message):
    __slots__ = ()
    class Field(_message.Message):
        __slots__ = ()
        SYNTAX_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
        syntax_type: str
        entity_type: _classifier_pb2.ClassifierEntityType
        name: str
        format: str
        raw_value: str
        def __init__(self, syntax_type: _Optional[str] = ..., entity_type: _Optional[_Union[_classifier_pb2.ClassifierEntityType, str]] = ..., name: _Optional[str] = ..., format: _Optional[str] = ..., raw_value: _Optional[str] = ...) -> None: ...
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PARSE_OPTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    FOID_FIELD_NUMBER: _ClassVar[int]
    OPTS_FIELD_NUMBER: _ClassVar[int]
    file_template_id: int
    filename: str
    fields: _containers.RepeatedCompositeFieldContainer[FileTemplate.Field]
    parse_opts: ParseOpts
    constraints: Constraints
    foid: int
    opts: Opts
    def __init__(self, file_template_id: _Optional[int] = ..., filename: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[FileTemplate.Field, _Mapping]]] = ..., parse_opts: _Optional[_Union[ParseOpts, _Mapping]] = ..., constraints: _Optional[_Union[Constraints, _Mapping]] = ..., foid: _Optional[int] = ..., opts: _Optional[_Union[Opts, _Mapping]] = ...) -> None: ...

class Opts(_message.Message):
    __slots__ = ()
    class DateFormatsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RenameFieldsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATE_FORMATS_FIELD_NUMBER: _ClassVar[int]
    RENAME_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PARSE_OPTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    date_formats: _containers.ScalarMap[str, str]
    rename_fields: _containers.ScalarMap[str, str]
    parse_opts: ParseOpts
    constraints: Constraints
    def __init__(self, date_formats: _Optional[_Mapping[str, str]] = ..., rename_fields: _Optional[_Mapping[str, str]] = ..., parse_opts: _Optional[_Union[ParseOpts, _Mapping]] = ..., constraints: _Optional[_Union[Constraints, _Mapping]] = ...) -> None: ...

class ParseOpts(_message.Message):
    __slots__ = ()
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
    __slots__ = ()
    HAS_HEADER_FIELD_NUMBER: _ClassVar[int]
    SKIP_ROWS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    has_header: bool
    skip_rows: int
    header: _containers.RepeatedScalarFieldContainer[str]
    separator: str
    def __init__(self, has_header: _Optional[bool] = ..., skip_rows: _Optional[int] = ..., header: _Optional[_Iterable[str]] = ..., separator: _Optional[str] = ...) -> None: ...

class OptsJson(_message.Message):
    __slots__ = ()
    RECORDS_ROOT_FIELD_NUMBER: _ClassVar[int]
    records_root: str
    def __init__(self, records_root: _Optional[str] = ...) -> None: ...

class OptsJsonL(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OptsFixed(_message.Message):
    __slots__ = ()
    class FieldOpts(_message.Message):
        __slots__ = ()
        STARTING_POSITION_FIELD_NUMBER: _ClassVar[int]
        FIELD_LENGTH_FIELD_NUMBER: _ClassVar[int]
        starting_position: int
        field_length: int
        def __init__(self, starting_position: _Optional[int] = ..., field_length: _Optional[int] = ...) -> None: ...
    class PositionsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OptsFixed.FieldOpts
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OptsFixed.FieldOpts, _Mapping]] = ...) -> None: ...
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_HEADER_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.MessageMap[str, OptsFixed.FieldOpts]
    has_header: bool
    def __init__(self, positions: _Optional[_Mapping[str, OptsFixed.FieldOpts]] = ..., has_header: _Optional[bool] = ...) -> None: ...

class OptsParquet(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Constraints(_message.Message):
    __slots__ = ()
    class ForbidEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClassifierEntityTypes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClassifierEntityTypes, _Mapping]] = ...) -> None: ...
    class AllowEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClassifierEntityTypes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClassifierEntityTypes, _Mapping]] = ...) -> None: ...
    FORBID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    forbid: _containers.MessageMap[str, ClassifierEntityTypes]
    allow: _containers.MessageMap[str, ClassifierEntityTypes]
    def __init__(self, forbid: _Optional[_Mapping[str, ClassifierEntityTypes]] = ..., allow: _Optional[_Mapping[str, ClassifierEntityTypes]] = ...) -> None: ...

class ParseHints(_message.Message):
    __slots__ = ()
    PARSE_OPTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    parse_opts: ParseOpts
    constraints: Constraints
    def __init__(self, parse_opts: _Optional[_Union[ParseOpts, _Mapping]] = ..., constraints: _Optional[_Union[Constraints, _Mapping]] = ...) -> None: ...
