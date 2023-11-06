from api.commons import labels_pb2 as _labels_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Label(_message.Message):
    __slots__ = ("org_id", "name", "description", "color", "label_id", "deleted")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    name: str
    description: str
    color: str
    label_id: str
    deleted: bool
    def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., color: _Optional[str] = ..., label_id: _Optional[str] = ..., deleted: bool = ...) -> None: ...

class LabelAssignment(_message.Message):
    __slots__ = ("label_id", "type", "entity_id", "org_id", "label")
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    type: _labels_pb2.EntityType
    entity_id: str
    org_id: str
    label: Label
    def __init__(self, label_id: _Optional[str] = ..., type: _Optional[_Union[_labels_pb2.EntityType, str]] = ..., entity_id: _Optional[str] = ..., org_id: _Optional[str] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...
