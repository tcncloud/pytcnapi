from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillGroup(_message.Message):
    __slots__ = ()
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILL_SETS_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    org_id: str
    name: str
    description: str
    skill_sets: _containers.RepeatedCompositeFieldContainer[SkillSet]
    def __init__(self, skill_group_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skill_sets: _Optional[_Iterable[_Union[SkillSet, _Mapping]]] = ...) -> None: ...

class SkillSet(_message.Message):
    __slots__ = ()
    PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    proficiency: int
    skill_sid: int
    def __init__(self, proficiency: _Optional[int] = ..., skill_sid: _Optional[int] = ...) -> None: ...
