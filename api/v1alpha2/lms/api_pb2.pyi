from annotations import authz_pb2 as _authz_pb2
from api.v1alpha2.lms import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileTemplateRequest(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

class CreateFileTemplateResponse(_message.Message):
    __slots__ = ("file_template",)
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    file_template: _entities_pb2.FileTemplateV2
    def __init__(self, file_template: _Optional[_Union[_entities_pb2.FileTemplateV2, _Mapping]] = ...) -> None: ...

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
