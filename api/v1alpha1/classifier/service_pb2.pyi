from api.v1alpha1.classifier import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParseFileRequest(_message.Message):
    __slots__ = ("raw_data", "reparse_file", "name")
    class ReParseFile(_message.Message):
        __slots__ = ("file_template_id", "hints")
        FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        HINTS_FIELD_NUMBER: _ClassVar[int]
        file_template_id: int
        hints: _entities_pb2.ParseHints
        def __init__(self, file_template_id: _Optional[int] = ..., hints: _Optional[_Union[_entities_pb2.ParseHints, _Mapping]] = ...) -> None: ...
    RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    REPARSE_FILE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    raw_data: bytes
    reparse_file: ParseFileRequest.ReParseFile
    name: str
    def __init__(self, raw_data: _Optional[bytes] = ..., reparse_file: _Optional[_Union[ParseFileRequest.ReParseFile, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

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