from api.commons import labels_pb2 as _labels_pb2
from api.commons.org import labels_pb2 as _labels_pb2_1
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateLabelRequest(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: _labels_pb2_1.Label
    def __init__(self, label: _Optional[_Union[_labels_pb2_1.Label, _Mapping]] = ...) -> None: ...

class CreateLabelResponse(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class UpdateLabelRequest(_message.Message):
    __slots__ = ("label", "field_mask")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    label: _labels_pb2_1.Label
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, label: _Optional[_Union[_labels_pb2_1.Label, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateLabelResponse(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: _labels_pb2_1.Label
    def __init__(self, label: _Optional[_Union[_labels_pb2_1.Label, _Mapping]] = ...) -> None: ...

class GetLabelRequest(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class GetLabelResponse(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: _labels_pb2_1.Label
    def __init__(self, label: _Optional[_Union[_labels_pb2_1.Label, _Mapping]] = ...) -> None: ...

class ListLabelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLabelsResponse(_message.Message):
    __slots__ = ("label",)
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: _containers.RepeatedCompositeFieldContainer[_labels_pb2_1.Label]
    def __init__(self, label: _Optional[_Iterable[_Union[_labels_pb2_1.Label, _Mapping]]] = ...) -> None: ...

class DeleteLabelRequest(_message.Message):
    __slots__ = ("label_id",)
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    def __init__(self, label_id: _Optional[str] = ...) -> None: ...

class DeleteLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AttachLabelRequest(_message.Message):
    __slots__ = ("label_id", "entity_id", "entity_type")
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    entity_id: str
    entity_type: _labels_pb2.LabeledEntity
    def __init__(self, label_id: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_type: _Optional[_Union[_labels_pb2.LabeledEntity, str]] = ...) -> None: ...

class AttachLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetachLabelRequest(_message.Message):
    __slots__ = ("label_id", "entity_id", "entity_type")
    LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    label_id: str
    entity_id: str
    entity_type: _labels_pb2.LabeledEntity
    def __init__(self, label_id: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_type: _Optional[_Union[_labels_pb2.LabeledEntity, str]] = ...) -> None: ...

class DetachLabelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLabeledEntityMapRequest(_message.Message):
    __slots__ = ("entity_type",)
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_type: _labels_pb2.LabeledEntity
    def __init__(self, entity_type: _Optional[_Union[_labels_pb2.LabeledEntity, str]] = ...) -> None: ...

class GetLabeledEntityMapResponse(_message.Message):
    __slots__ = ("entity_map",)
    class EntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GetLabeledEntityMapResponse.EntityLabels
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GetLabeledEntityMapResponse.EntityLabels, _Mapping]] = ...) -> None: ...
    class EntityLabels(_message.Message):
        __slots__ = ("labels",)
        LABELS_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2_1.Label]
        def __init__(self, labels: _Optional[_Iterable[_Union[_labels_pb2_1.Label, _Mapping]]] = ...) -> None: ...
    ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    entity_map: _containers.MessageMap[str, GetLabeledEntityMapResponse.EntityLabels]
    def __init__(self, entity_map: _Optional[_Mapping[str, GetLabeledEntityMapResponse.EntityLabels]] = ...) -> None: ...

class AssignLabelsRequest(_message.Message):
    __slots__ = ("label_ids", "permission_group_id")
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, label_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class AssignLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeLabelsRequest(_message.Message):
    __slots__ = ("label_ids", "permission_group_id")
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, label_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class RevokeLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
