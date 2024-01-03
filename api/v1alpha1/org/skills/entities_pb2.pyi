from api.commons.org import skill_group_pb2 as _skill_group_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSkillGroupRequest(_message.Message):
    __slots__ = ("skill_group",)
    SKILL_GROUP_FIELD_NUMBER: _ClassVar[int]
    skill_group: _skill_group_pb2.SkillGroup
    def __init__(self, skill_group: _Optional[_Union[_skill_group_pb2.SkillGroup, _Mapping]] = ...) -> None: ...

class CreateSkillGroupResponse(_message.Message):
    __slots__ = ("skill_group_id",)
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    def __init__(self, skill_group_id: _Optional[str] = ...) -> None: ...

class ListSkillGroupsRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSkillGroupsResponse(_message.Message):
    __slots__ = ("skill_groups",)
    SKILL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    skill_groups: _containers.RepeatedCompositeFieldContainer[_skill_group_pb2.SkillGroup]
    def __init__(self, skill_groups: _Optional[_Iterable[_Union[_skill_group_pb2.SkillGroup, _Mapping]]] = ...) -> None: ...

class UpdateSkillGroupRequest(_message.Message):
    __slots__ = ("skill_group", "field_mask")
    SKILL_GROUP_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    skill_group: _skill_group_pb2.SkillGroup
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill_group: _Optional[_Union[_skill_group_pb2.SkillGroup, _Mapping]] = ..., field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateSkillGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSkillGroupRequest(_message.Message):
    __slots__ = ("skill_group_id", "field_mask")
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill_group_id: _Optional[str] = ..., field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSkillGroupResponse(_message.Message):
    __slots__ = ("skill_group",)
    SKILL_GROUP_FIELD_NUMBER: _ClassVar[int]
    skill_group: _skill_group_pb2.SkillGroup
    def __init__(self, skill_group: _Optional[_Union[_skill_group_pb2.SkillGroup, _Mapping]] = ...) -> None: ...

class DeleteSkillGroupRequest(_message.Message):
    __slots__ = ("skill_group_id",)
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    def __init__(self, skill_group_id: _Optional[str] = ...) -> None: ...

class DeleteSkillGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignSkillGroupsRequest(_message.Message):
    __slots__ = ("skill_group_ids", "user_id")
    SKILL_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    skill_group_ids: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, skill_group_ids: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class AssignSkillGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeSkillGroupsRequest(_message.Message):
    __slots__ = ("skill_group_ids", "user_id")
    SKILL_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    skill_group_ids: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, skill_group_ids: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class RevokeSkillGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserSkillGroupsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserSkillGroupsResponse(_message.Message):
    __slots__ = ("skill_group_ids",)
    SKILL_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    skill_group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUserSkillsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserSkillsResponse(_message.Message):
    __slots__ = ("skill_sets",)
    SKILL_SETS_FIELD_NUMBER: _ClassVar[int]
    skill_sets: _containers.RepeatedCompositeFieldContainer[_skill_group_pb2.SkillSet]
    def __init__(self, skill_sets: _Optional[_Iterable[_Union[_skill_group_pb2.SkillSet, _Mapping]]] = ...) -> None: ...

class GetSkillGroupMembersRequest(_message.Message):
    __slots__ = ("skill_group_id",)
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    def __init__(self, skill_group_id: _Optional[str] = ...) -> None: ...

class GetSkillGroupMembersResponse(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListSkillGroupsMembersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillGroupsMembersResponse(_message.Message):
    __slots__ = ("skill_group_members",)
    SKILL_GROUP_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    skill_group_members: _containers.RepeatedCompositeFieldContainer[SkillGroupMembers]
    def __init__(self, skill_group_members: _Optional[_Iterable[_Union[SkillGroupMembers, _Mapping]]] = ...) -> None: ...

class SkillGroupMembers(_message.Message):
    __slots__ = ("skill_group_id", "user_ids")
    SKILL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    skill_group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill_group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...
