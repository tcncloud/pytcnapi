from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RING_STRATEGY_UNSPECIFIED: _ClassVar[RingStrategy]
    RING_STRATEGY_RING_ALL: _ClassVar[RingStrategy]
    RING_STRATEGY_ROUND_ROBIN: _ClassVar[RingStrategy]
    RING_STRATEGY_RANDOM: _ClassVar[RingStrategy]
    RING_STRATEGY_ORDERED: _ClassVar[RingStrategy]
RING_STRATEGY_UNSPECIFIED: RingStrategy
RING_STRATEGY_RING_ALL: RingStrategy
RING_STRATEGY_ROUND_ROBIN: RingStrategy
RING_STRATEGY_RANDOM: RingStrategy
RING_STRATEGY_ORDERED: RingStrategy

class PBXUser(_message.Message):
    __slots__ = ("pbx_user_id", "org_user_id", "sip_account_ids")
    PBX_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SIP_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    pbx_user_id: str
    org_user_id: str
    sip_account_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, pbx_user_id: _Optional[str] = ..., org_user_id: _Optional[str] = ..., sip_account_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SIPAccountRingGroup(_message.Message):
    __slots__ = ("ring_group_id", "ring_group_name")
    RING_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    RING_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ring_group_id: str
    ring_group_name: str
    def __init__(self, ring_group_id: _Optional[str] = ..., ring_group_name: _Optional[str] = ...) -> None: ...

class OrgSkill(_message.Message):
    __slots__ = ("skill_sid", "skill_name")
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_NAME_FIELD_NUMBER: _ClassVar[int]
    skill_sid: str
    skill_name: str
    def __init__(self, skill_sid: _Optional[str] = ..., skill_name: _Optional[str] = ...) -> None: ...

class OrgPermissionGroup(_message.Message):
    __slots__ = ("permission_group_id", "permission_group_name")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    permission_group_name: str
    def __init__(self, permission_group_id: _Optional[str] = ..., permission_group_name: _Optional[str] = ...) -> None: ...

class OrgHuntGroup(_message.Message):
    __slots__ = ("hunt_group_sid", "hunt_group_name")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: str
    hunt_group_name: str
    def __init__(self, hunt_group_sid: _Optional[str] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...

class SIPAccount(_message.Message):
    __slots__ = ("sip_id", "is_active", "extension", "ring_group_ids", "org_user_id", "ring_groups", "org_username", "org_full_name", "org_hunt_group", "org_skills", "org_permission_groups")
    SIP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ORG_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RING_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ORG_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ORG_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    ORG_SKILLS_FIELD_NUMBER: _ClassVar[int]
    ORG_PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    sip_id: str
    is_active: bool
    extension: str
    ring_group_ids: _containers.RepeatedScalarFieldContainer[str]
    org_user_id: str
    ring_groups: _containers.RepeatedCompositeFieldContainer[SIPAccountRingGroup]
    org_username: str
    org_full_name: str
    org_hunt_group: OrgHuntGroup
    org_skills: _containers.RepeatedCompositeFieldContainer[OrgSkill]
    org_permission_groups: _containers.RepeatedCompositeFieldContainer[OrgPermissionGroup]
    def __init__(self, sip_id: _Optional[str] = ..., is_active: bool = ..., extension: _Optional[str] = ..., ring_group_ids: _Optional[_Iterable[str]] = ..., org_user_id: _Optional[str] = ..., ring_groups: _Optional[_Iterable[_Union[SIPAccountRingGroup, _Mapping]]] = ..., org_username: _Optional[str] = ..., org_full_name: _Optional[str] = ..., org_hunt_group: _Optional[_Union[OrgHuntGroup, _Mapping]] = ..., org_skills: _Optional[_Iterable[_Union[OrgSkill, _Mapping]]] = ..., org_permission_groups: _Optional[_Iterable[_Union[OrgPermissionGroup, _Mapping]]] = ...) -> None: ...

class RingGroup(_message.Message):
    __slots__ = ("id", "name", "description", "extension", "ring_strategy", "sip_account_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SIP_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    extension: str
    ring_strategy: RingStrategy
    sip_account_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., extension: _Optional[str] = ..., ring_strategy: _Optional[_Union[RingStrategy, str]] = ..., sip_account_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListPBXUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPBXUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[PBXUser]
    def __init__(self, users: _Optional[_Iterable[_Union[PBXUser, _Mapping]]] = ...) -> None: ...

class ListSIPAccountsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSIPAccountsResponse(_message.Message):
    __slots__ = ("sip_accounts",)
    SIP_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    sip_accounts: _containers.RepeatedCompositeFieldContainer[SIPAccount]
    def __init__(self, sip_accounts: _Optional[_Iterable[_Union[SIPAccount, _Mapping]]] = ...) -> None: ...

class ListSIPAccountsByRingGroupIdRequest(_message.Message):
    __slots__ = ("ring_group_id",)
    RING_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ring_group_id: str
    def __init__(self, ring_group_id: _Optional[str] = ...) -> None: ...

class ListSIPAccountsByRingGroupIdResponse(_message.Message):
    __slots__ = ("sip_accounts",)
    SIP_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    sip_accounts: _containers.RepeatedCompositeFieldContainer[SIPAccount]
    def __init__(self, sip_accounts: _Optional[_Iterable[_Union[SIPAccount, _Mapping]]] = ...) -> None: ...

class GetSIPAccountByUserIdRequest(_message.Message):
    __slots__ = ("org_user_id",)
    ORG_USER_ID_FIELD_NUMBER: _ClassVar[int]
    org_user_id: str
    def __init__(self, org_user_id: _Optional[str] = ...) -> None: ...

class GetSIPAccountByUserIdResponse(_message.Message):
    __slots__ = ("sip_account",)
    SIP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    sip_account: SIPAccount
    def __init__(self, sip_account: _Optional[_Union[SIPAccount, _Mapping]] = ...) -> None: ...

class GetSIPAccountRequest(_message.Message):
    __slots__ = ("sip_account_id",)
    SIP_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    sip_account_id: str
    def __init__(self, sip_account_id: _Optional[str] = ...) -> None: ...

class GetSIPAccountResponse(_message.Message):
    __slots__ = ("sip_account",)
    SIP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    sip_account: _containers.RepeatedCompositeFieldContainer[SIPAccount]
    def __init__(self, sip_account: _Optional[_Iterable[_Union[SIPAccount, _Mapping]]] = ...) -> None: ...

class GetPBXUserRequest(_message.Message):
    __slots__ = ("pbx_user_id",)
    PBX_USER_ID_FIELD_NUMBER: _ClassVar[int]
    pbx_user_id: str
    def __init__(self, pbx_user_id: _Optional[str] = ...) -> None: ...

class GetPBXUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: PBXUser
    def __init__(self, user: _Optional[_Union[PBXUser, _Mapping]] = ...) -> None: ...

class ListRingGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRingGroupsResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[RingGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[RingGroup, _Mapping]]] = ...) -> None: ...

class ListRingGroupsBySipIdRequest(_message.Message):
    __slots__ = ("sip_account_id",)
    SIP_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    sip_account_id: str
    def __init__(self, sip_account_id: _Optional[str] = ...) -> None: ...

class ListRingGroupsBySipIdResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[RingGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[RingGroup, _Mapping]]] = ...) -> None: ...

class GetRingGroupRequest(_message.Message):
    __slots__ = ("ring_group_id",)
    RING_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ring_group_id: str
    def __init__(self, ring_group_id: _Optional[str] = ...) -> None: ...

class GetRingGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class UpdateSIPAccountRequest(_message.Message):
    __slots__ = ("sip_account", "update_mask")
    SIP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sip_account: SIPAccount
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, sip_account: _Optional[_Union[SIPAccount, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSIPAccountResponse(_message.Message):
    __slots__ = ("sip_account",)
    SIP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    sip_account: SIPAccount
    def __init__(self, sip_account: _Optional[_Union[SIPAccount, _Mapping]] = ...) -> None: ...

class UpdateRingGroupRequest(_message.Message):
    __slots__ = ("group", "update_mask")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRingGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class AssignRandomExtensionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignRandomExtensionResponse(_message.Message):
    __slots__ = ("extension",)
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: str
    def __init__(self, extension: _Optional[str] = ...) -> None: ...

class CreateRingGroupRequest(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class CreateRingGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: RingGroup
    def __init__(self, group: _Optional[_Union[RingGroup, _Mapping]] = ...) -> None: ...

class DeleteRingGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteRingGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
