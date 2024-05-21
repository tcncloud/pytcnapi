from annotations import authz_pb2 as _authz_pb2
from api.v1alpha1.classifier import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParseFileRequest(_message.Message):
    __slots__ = ("raw_data", "reparse_file", "parse_with_hints", "name")
    class ReParseFile(_message.Message):
        __slots__ = ("file_template_id", "hints", "opts")
        FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        HINTS_FIELD_NUMBER: _ClassVar[int]
        OPTS_FIELD_NUMBER: _ClassVar[int]
        file_template_id: int
        hints: _entities_pb2.ParseHints
        opts: _entities_pb2.Opts
        def __init__(self, file_template_id: _Optional[int] = ..., hints: _Optional[_Union[_entities_pb2.ParseHints, _Mapping]] = ..., opts: _Optional[_Union[_entities_pb2.Opts, _Mapping]] = ...) -> None: ...
    class ParseWithHints(_message.Message):
        __slots__ = ("raw_data", "opts")
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
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...

class UpdateFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...

class UpdateFileTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: int
    def __init__(self, file_template: _Optional[int] = ...) -> None: ...

class DeleteFileTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFileTemplatesRequest(_message.Message):
    __slots__ = ("prev_id", "asc", "page_size")
    PREV_ID_FIELD_NUMBER: _ClassVar[int]
    ASC_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    prev_id: int
    asc: bool
    page_size: int
    def __init__(self, prev_id: _Optional[int] = ..., asc: bool = ..., page_size: _Optional[int] = ...) -> None: ...

class ListFileTemplatesResponse(_message.Message):
    __slots__ = ("file_templates",)
    FILE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    file_templates: _containers.RepeatedCompositeFieldContainer[_entities_pb2.FileTemplate]
    def __init__(self, file_templates: _Optional[_Iterable[_Union[_entities_pb2.FileTemplate, _Mapping]]] = ...) -> None: ...

class GetFileTemplateRequest(_message.Message):
    __slots__ = ("file_template_id",)
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    file_template_id: int
    def __init__(self, file_template_id: _Optional[int] = ...) -> None: ...

class GetFileTemplateResponse(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplate
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplate, _Mapping]] = ...) -> None: ...
