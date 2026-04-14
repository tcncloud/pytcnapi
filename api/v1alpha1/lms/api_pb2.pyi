from annotations import authz_pb2 as _authz_pb2
from api.v1alpha1.lms import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class DeleteFileTemplateResponse(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class GetFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class GetFileTemplateResponse(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class ListFileTemplatesRequest(_message.Message):
    __slots__ = ("value", "last_id", "page_size")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LAST_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    value: _entities_pb2.FileTemplateV2
    last_id: str
    page_size: int
    def __init__(self, value: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ..., last_id: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListFileTemplatesResponse(_message.Message):
    __slots__ = ("file_templates",)
    FILE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    file_templates: _containers.RepeatedCompositeFieldContainer[_entities_pb2.FileTemplateV2]
    def __init__(self, file_templates: _Optional[_Iterable[_Union[_entities_pb2.FileTemplateV2, _Mapping]]] = ...) -> None: ...

class ParseFileTemplateRequest(_message.Message):
    __slots__ = ("new_template", "existing_template")
    NEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    new_template: _entities_pb2.NewTemplate
    existing_template: _entities_pb2.ExistingTemplate
    def __init__(self, new_template: _Optional[_Union[_entities_pb2.NewTemplate, _Mapping]] = ..., existing_template: _Optional[_Union[_entities_pb2.ExistingTemplate, _Mapping]] = ...) -> None: ...

class ParseFileTemplateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class UpdateFileTemplateResponse(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...
