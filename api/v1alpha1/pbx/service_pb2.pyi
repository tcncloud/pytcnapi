from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RING_STRATEGY_UNSPECIFIED: _ClassVar[RingStrategy]
    RING_STRATEGY_RING_ALL: _ClassVar[RingStrategy]
    RING_STRATEGY_ROUND_ROBIN: _ClassVar[RingStrategy]
    RING_STRATEGY_RANDOM: _ClassVar[RingStrategy]
RING_STRATEGY_UNSPECIFIED: RingStrategy
RING_STRATEGY_RING_ALL: RingStrategy
RING_STRATEGY_ROUND_ROBIN: RingStrategy
RING_STRATEGY_RANDOM: RingStrategy

class HuntGroup(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PBXUser(_message.Message):
    __slots__ = ["id", "name", "is_active", "extension", "ring_groups", "user_type", "hunt_group", "skills", "permission_groups"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_GROUPS_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    is_active: bool
    extension: int
    ring_groups: _containers.RepeatedCompositeFieldContainer[RingGroupDesc]
    user_type: str
    hunt_group: str
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., is_active: bool = ..., extension: _Optional[int] = ..., ring_groups: _Optional[_Iterable[_Union[RingGroupDesc, _Mapping]]] = ..., user_type: _Optional[str] = ..., hunt_group: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ...) -> None: ...

class PermissionGroup(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RingGroup(_message.Message):
    __slots__ = ["id", "name", "description", "extension", "ring_strategy", "members"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    extension: int
    ring_strategy: RingStrategy
    members: _containers.RepeatedCompositeFieldContainer[PBXUser]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., extension: _Optional[int] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ..., members: _Optional[_Iterable[_Union[PBXUser, _Mapping]]] = ...) -> None: ...

class RingGroupDesc(_message.Message):
    __slots__ = ["id", "name", "description"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ActivatePbxUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ActivatePbxUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AddUsersToRingGroupRequest(_message.Message):
    __slots__ = ["group_id", "user_ids"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AddUsersToRingGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AssignRandomGroupExtensionRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class AssignRandomGroupExtensionResponse(_message.Message):
    __slots__ = ["extension"]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: int
    def __init__(self, extension: _Optional[int] = ...) -> None: ...

class AssignRandomUserExtensionRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AssignRandomUserExtensionResponse(_message.Message):
    __slots__ = ["extension"]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: int
    def __init__(self, extension: _Optional[int] = ...) -> None: ...

class CreateRingGroupRequest(_message.Message):
    __slots__ = ["name", "description", "extension", "ring_strategy", "member_ids"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    extension: int
    ring_strategy: RingStrategy
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., extension: _Optional[int] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ..., member_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRingGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class DeactivatePbxUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DeactivatePbxUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteRingGroupRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteRingGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPbxUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPbxUsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[PBXUser]
    def __init__(self, users: _Optional[_Iterable[_Union[PBXUser, _Mapping]]] = ...) -> None: ...

class ListRingGroupsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListRingGroupsResponse(_message.Message):
    __slots__ = ["groups"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[RingGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[RingGroup, _Mapping]]] = ...) -> None: ...

class RemoveUsersFromRingGroupRequest(_message.Message):
    __slots__ = ["group_id", "user_ids"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoveUsersFromRingGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateRingGroupRequest(_message.Message):
    __slots__ = ["id", "name", "description", "extension", "ring_strategy"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    extension: int
    ring_strategy: RingStrategy
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., extension: _Optional[int] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ...) -> None: ...

class UpdateRingGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class UpdateUserExtensionRequest(_message.Message):
    __slots__ = ["user_id", "extension"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    extension: int
    def __init__(self, user_id: _Optional[str] = ..., extension: _Optional[int] = ...) -> None: ...

class UpdateUserExtensionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
