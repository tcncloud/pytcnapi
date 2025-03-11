from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons import labels_pb2 as _labels_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Label(_message.Message):
    __slots__ = ("name", "description", "color", "label_id", "deleted")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    color: str
    label_id: str
    deleted: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., color: _Optional[str] = ..., label_id: _Optional[str] = ..., deleted: bool = ...) -> None: ...

class CreateLabelRequest(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: Label
    def __init__(self, label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class CreateLabelResponse(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class DeleteLabelRequest(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class DeleteLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLabelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLabelsResponse(_message.Message):
    __slots__ = ("labels",)
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...

class GetLabelRequest(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class GetLabelResponse(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: Label
    def __init__(self, label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class UpdateLabelRequest(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: Label
    def __init__(self, label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class UpdateLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LabelAssignment(_message.Message):
    __slots__ = ("label_id", "type", "entity_id", "label")
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    type: _labels_pb2.EntityType
    entity_id: str
    label: Label
    def __init__(self, label_id: _Optional[str] = ..., type: _Optional[_Union[_labels_pb2.EntityType, str]] = ..., entity_id: _Optional[str] = ..., label: _Optional[_Union[Label, _Mapping]] = ...) -> None: ...

class AssignLabelRequest(_message.Message):
    __slots__ = ("assignments",)
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[LabelAssignment]
    def __init__(self, assignments: _Optional[_Iterable[_Union[LabelAssignment, _Mapping]]] = ...) -> None: ...

class AssignLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnassignLabelRequest(_message.Message):
    __slots__ = ("assignments",)
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[LabelAssignment]
    def __init__(self, assignments: _Optional[_Iterable[_Union[LabelAssignment, _Mapping]]] = ...) -> None: ...

class UnassignLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAssignmentCountsRequest(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class GetAssignmentCountsResponse(_message.Message):
    __slots__ = ("counts",)
    class CountsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    counts: _containers.ScalarMap[int, int]
    def __init__(self, counts: _Optional[_Mapping[int, int]] = ...) -> None: ...

class GetAssignableLabelsRequest(_message.Message):
    __slots__ = ("permission",)
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _perms_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_perms_pb2.Permission, str]] = ...) -> None: ...

class GetAssignableLabelsResponse(_message.Message):
    __slots__ = ("labels",)
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, labels: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...
