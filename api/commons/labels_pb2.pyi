from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_TYPE_INVALID: _ClassVar[EntityType]
    ENTITY_TYPE_USER: _ClassVar[EntityType]
    ENTITY_TYPE_LMS_PIPELINE: _ClassVar[EntityType]

class LabeledEntity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LABELED_ENTITY_UNSPECIFIED: _ClassVar[LabeledEntity]
    LABELED_ENTITY_SKILL_GROUP: _ClassVar[LabeledEntity]
    LABELED_ENTITY_USER: _ClassVar[LabeledEntity]
ENTITY_TYPE_INVALID: EntityType
ENTITY_TYPE_USER: EntityType
ENTITY_TYPE_LMS_PIPELINE: EntityType
LABELED_ENTITY_UNSPECIFIED: LabeledEntity
LABELED_ENTITY_SKILL_GROUP: LabeledEntity
LABELED_ENTITY_USER: LabeledEntity
