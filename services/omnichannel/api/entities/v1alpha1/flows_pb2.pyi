from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlowFieldName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIELD_NAME_UNSPECIFIED: _ClassVar[FlowFieldName]
    FIELD_NAME_USER_INPUT: _ClassVar[FlowFieldName]
FIELD_NAME_UNSPECIFIED: FlowFieldName
FIELD_NAME_USER_INPUT: FlowFieldName

class FlowPayload(_message.Message):
    __slots__ = ()
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[FlowField]
    def __init__(self, fields: _Optional[_Iterable[_Union[FlowField, _Mapping]]] = ...) -> None: ...

class FlowField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    name: FlowFieldName
    user_input: str
    def __init__(self, name: _Optional[_Union[FlowFieldName, str]] = ..., user_input: _Optional[str] = ...) -> None: ...
