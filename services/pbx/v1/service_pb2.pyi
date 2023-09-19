from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
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

class PBXUser(_message.Message):
    __slots__ = ["pbx_user_id", "org_user_id", "sip_accounts"]
    PBX_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SIP_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    pbx_user_id: str
    org_user_id: str
    sip_accounts: _containers.RepeatedCompositeFieldContainer[SIPAccount]
    def __init__(self, pbx_user_id: _Optional[str] = ..., org_user_id: _Optional[str] = ..., sip_accounts: _Optional[_Iterable[_Union[SIPAccount, _Mapping]]] = ...) -> None: ...

class SIPAccount(_message.Message):
    __slots__ = ["sip_id", "is_active", "extension", "ring_groups"]
    SIP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_GROUPS_FIELD_NUMBER: _ClassVar[int]
    sip_id: str
    is_active: bool
    extension: int
    ring_groups: _containers.RepeatedCompositeFieldContainer[RingGroup]
    def __init__(self, sip_id: _Optional[str] = ..., is_active: bool = ..., extension: _Optional[int] = ..., ring_groups: _Optional[_Iterable[_Union[RingGroup, _Mapping]]] = ...) -> None: ...

class RingGroup(_message.Message):
    __slots__ = ["id", "name", "description", "extension", "ring_strategy", "pbx_users"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PBX_USERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    extension: int
    ring_strategy: RingStrategy
    pbx_users: _containers.RepeatedCompositeFieldContainer[PBXUser]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., extension: _Optional[int] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ..., pbx_users: _Optional[_Iterable[_Union[PBXUser, _Mapping]]] = ...) -> None: ...

class QueryPbxUsersRequest(_message.Message):
    __slots__ = ["pbx_user_id", "response_mask"]
    PBX_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MASK_FIELD_NUMBER: _ClassVar[int]
    pbx_user_id: str
    response_mask: _field_mask_pb2.FieldMask
    def __init__(self, pbx_user_id: _Optional[str] = ..., response_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class QueryPbxUsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[PBXUser]
    def __init__(self, users: _Optional[_Iterable[_Union[PBXUser, _Mapping]]] = ...) -> None: ...

class QueryRingGroupsRequest(_message.Message):
    __slots__ = ["group_id", "response_mask"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MASK_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    response_mask: _field_mask_pb2.FieldMask
    def __init__(self, group_id: _Optional[str] = ..., response_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class QueryRingGroupsResponse(_message.Message):
    __slots__ = ["groups"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[RingGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[RingGroup, _Mapping]]] = ...) -> None: ...

class UpdatePbxUserRequest(_message.Message):
    __slots__ = ["user", "update_mask"]
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: PBXUser
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[PBXUser, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePbxUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: PBXUser
    def __init__(self, user: _Optional[_Union[PBXUser, _Mapping]] = ...) -> None: ...

class UpdateRingGroupRequest(_message.Message):
    __slots__ = ["group", "update_mask"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRingGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class AssignRandomExtensionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AssignRandomExtensionResponse(_message.Message):
    __slots__ = ["extension"]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: int
    def __init__(self, extension: _Optional[int] = ...) -> None: ...

class CreateRingGroupRequest(_message.Message):
    __slots__ = ["name", "description", "ring_strategy", "pbx_user_ids"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PBX_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    ring_strategy: RingStrategy
    pbx_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ..., pbx_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRingGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class DeleteRingGroupRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteRingGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
