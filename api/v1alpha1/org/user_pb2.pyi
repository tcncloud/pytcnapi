from api.commons import org_pb2 as _org_pb2
from api.commons.org import labels_pb2 as _labels_pb2
from api.commons.org import permissions_pb2 as _permissions_pb2
from api.commons.org import trusts_pb2 as _trusts_pb2
from api.commons.org import user_pb2 as _user_pb2
from api.commons import perms_pb2 as _perms_pb2
from api.commons import user_pb2 as _user_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ("org_id", "first_name", "last_name", "email", "user_name", "password", "permission_group_ids", "partner_agent_id", "p3_permission_group_id", "linkback_numbers", "caller_ids", "default_app", "user_caller_id", "agent_profile_group_id", "label_ids", "time_zone_override", "hunt_group_sid")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    first_name: str
    last_name: str
    email: str
    user_name: str
    password: str
    permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
    partner_agent_id: str
    p3_permission_group_id: str
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    default_app: _org_pb2.OperatorApplications
    user_caller_id: str
    agent_profile_group_id: str
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    time_zone_override: _org_pb2.TimeZoneWrapper
    hunt_group_sid: int
    def __init__(self, org_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., user_name: _Optional[str] = ..., password: _Optional[str] = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., partner_agent_id: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., agent_profile_group_id: _Optional[str] = ..., label_ids: _Optional[_Iterable[str]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CreateDelegatedUserRequest(_message.Message):
    __slots__ = ("auth_user_id", "org_id", "email", "username", "first_name", "last_name", "groups", "connection_id")
    AUTH_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    auth_user_id: str
    org_id: str
    email: str
    username: str
    first_name: str
    last_name: str
    groups: _containers.RepeatedScalarFieldContainer[str]
    connection_id: str
    def __init__(self, auth_user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., email: _Optional[str] = ..., username: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., groups: _Optional[_Iterable[str]] = ..., connection_id: _Optional[str] = ...) -> None: ...

class CreateDelegatedUserResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetMyUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMyUserResponse(_message.Message):
    __slots__ = ("user_id", "org_id", "username", "delegated", "org_name", "hunt_group", "labels", "skills", "permission_groups", "p3_permission_group", "agent_profile_group", "trusts", "account_owner")
    class HuntGroup(_message.Message):
        __slots__ = ("hunt_group_sid", "hunt_group_name")
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    class AgentProfileGroup(_message.Message):
        __slots__ = ("agent_profile_group_id", "agent_profile_group_name")
        AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        agent_profile_group_id: str
        agent_profile_group_name: str
        def __init__(self, agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    username: str
    delegated: bool
    org_name: str
    hunt_group: GetMyUserResponse.HuntGroup
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    skills: _containers.RepeatedCompositeFieldContainer[_user_pb2.Skill]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    agent_profile_group: GetMyUserResponse.AgentProfileGroup
    trusts: _containers.RepeatedCompositeFieldContainer[_trusts_pb2.Trust]
    account_owner: bool
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., username: _Optional[str] = ..., delegated: bool = ..., org_name: _Optional[str] = ..., hunt_group: _Optional[_Union[GetMyUserResponse.HuntGroup, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_user_pb2.Skill, _Mapping]]] = ..., permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ..., p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ..., agent_profile_group: _Optional[_Union[GetMyUserResponse.AgentProfileGroup, _Mapping]] = ..., trusts: _Optional[_Iterable[_Union[_trusts_pb2.Trust, _Mapping]]] = ..., account_owner: bool = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user_id", "org_id", "delegated", "time_zone_override", "hunt_group", "labels", "skills", "permission_groups", "p3_permission_group", "agent_profile_group", "org_name", "first_name", "username", "last_name", "login_disabled", "partner_agent_id", "user_caller_id", "linkback_numbers", "caller_ids", "default_app", "login_sid", "agent_sid", "trusts", "email", "default_region", "created_at", "last_updated", "password_reset_required", "account_owner")
    class HuntGroup(_message.Message):
        __slots__ = ("hunt_group_sid", "hunt_group_name")
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    class AgentProfileGroup(_message.Message):
        __slots__ = ("agent_profile_group_id", "agent_profile_group_name")
        AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        agent_profile_group_id: str
        agent_profile_group_name: str
        def __init__(self, agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REGION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    delegated: bool
    time_zone_override: _org_pb2.TimeZoneWrapper
    hunt_group: GetUserResponse.HuntGroup
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    skills: _containers.RepeatedCompositeFieldContainer[_user_pb2.Skill]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    agent_profile_group: GetUserResponse.AgentProfileGroup
    org_name: str
    first_name: str
    username: str
    last_name: str
    login_disabled: bool
    partner_agent_id: str
    user_caller_id: str
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    default_app: _org_pb2.OperatorApplications
    login_sid: int
    agent_sid: int
    trusts: _containers.RepeatedCompositeFieldContainer[_trusts_pb2.Trust]
    email: str
    default_region: str
    created_at: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    password_reset_required: bool
    account_owner: bool
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., delegated: bool = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., hunt_group: _Optional[_Union[GetUserResponse.HuntGroup, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_user_pb2.Skill, _Mapping]]] = ..., permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ..., p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ..., agent_profile_group: _Optional[_Union[GetUserResponse.AgentProfileGroup, _Mapping]] = ..., org_name: _Optional[str] = ..., first_name: _Optional[str] = ..., username: _Optional[str] = ..., last_name: _Optional[str] = ..., login_disabled: bool = ..., partner_agent_id: _Optional[str] = ..., user_caller_id: _Optional[str] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., login_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., trusts: _Optional[_Iterable[_Union[_trusts_pb2.Trust, _Mapping]]] = ..., email: _Optional[str] = ..., default_region: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_reset_required: bool = ..., account_owner: bool = ...) -> None: ...

class GetUserByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetUserByOrgIdResponse(_message.Message):
    __slots__ = ("user_id", "org_id", "username", "delegated", "org_name", "hunt_group", "labels", "skills", "permission_groups", "p3_permission_group", "agent_profile_group", "trusts", "account_owner")
    class HuntGroup(_message.Message):
        __slots__ = ("hunt_group_sid", "hunt_group_name")
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    class AgentProfileGroup(_message.Message):
        __slots__ = ("agent_profile_group_id", "agent_profile_group_name")
        AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        agent_profile_group_id: str
        agent_profile_group_name: str
        def __init__(self, agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    username: str
    delegated: bool
    org_name: str
    hunt_group: GetUserByOrgIdResponse.HuntGroup
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    skills: _containers.RepeatedCompositeFieldContainer[_user_pb2.Skill]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    p3_permission_group: _permissions_pb2.P3PermissionGroup
    agent_profile_group: GetUserByOrgIdResponse.AgentProfileGroup
    trusts: _containers.RepeatedCompositeFieldContainer[_trusts_pb2.Trust]
    account_owner: bool
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., username: _Optional[str] = ..., delegated: bool = ..., org_name: _Optional[str] = ..., hunt_group: _Optional[_Union[GetUserByOrgIdResponse.HuntGroup, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., skills: _Optional[_Iterable[_Union[_user_pb2.Skill, _Mapping]]] = ..., permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ..., p3_permission_group: _Optional[_Union[_permissions_pb2.P3PermissionGroup, _Mapping]] = ..., agent_profile_group: _Optional[_Union[GetUserByOrgIdResponse.AgentProfileGroup, _Mapping]] = ..., trusts: _Optional[_Iterable[_Union[_trusts_pb2.Trust, _Mapping]]] = ..., account_owner: bool = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents",)
    class AgentDetails(_message.Message):
        __slots__ = ("user_id", "org_id", "first_name", "last_name", "username", "skills", "login_disabled", "hunt_group", "labels", "delegated", "trust_ids", "permission_groups", "agent_sid", "name", "partner_agent_id", "user_caller_id", "created", "last_updated", "agent_profile_group", "agent", "time_zone_override", "email")
        class HuntGroup(_message.Message):
            __slots__ = ("hunt_group_sid", "hunt_group_name")
            HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
            HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            hunt_group_sid: int
            hunt_group_name: str
            def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
        class AgentProfileGroup(_message.Message):
            __slots__ = ("agent_profile_group_id", "agent_profile_group_name")
            AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            agent_profile_group_id: str
            agent_profile_group_name: str
            def __init__(self, agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ...) -> None: ...
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        SKILLS_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        DELEGATED_FIELD_NUMBER: _ClassVar[int]
        TRUST_IDS_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
        AGENT_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
        USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
        AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        org_id: str
        first_name: str
        last_name: str
        username: str
        skills: _containers.RepeatedCompositeFieldContainer[_user_pb2.Skill]
        login_disabled: bool
        hunt_group: ListAgentsResponse.AgentDetails.HuntGroup
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
        delegated: bool
        trust_ids: _containers.RepeatedScalarFieldContainer[str]
        permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
        agent_sid: int
        name: str
        partner_agent_id: str
        user_caller_id: str
        created: _timestamp_pb2.Timestamp
        last_updated: _timestamp_pb2.Timestamp
        agent_profile_group: ListAgentsResponse.AgentDetails.AgentProfileGroup
        agent: bool
        time_zone_override: _org_pb2.TimeZoneWrapper
        email: str
        def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[_user_pb2.Skill, _Mapping]]] = ..., login_disabled: bool = ..., hunt_group: _Optional[_Union[ListAgentsResponse.AgentDetails.HuntGroup, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., delegated: bool = ..., trust_ids: _Optional[_Iterable[str]] = ..., permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ..., agent_sid: _Optional[int] = ..., name: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., user_caller_id: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_profile_group: _Optional[_Union[ListAgentsResponse.AgentDetails.AgentProfileGroup, _Mapping]] = ..., agent: bool = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., email: _Optional[str] = ...) -> None: ...
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[ListAgentsResponse.AgentDetails]
    def __init__(self, agents: _Optional[_Iterable[_Union[ListAgentsResponse.AgentDetails, _Mapping]]] = ...) -> None: ...

class ListPublicUsersRequest(_message.Message):
    __slots__ = ("agent_filter", "archived_filter")
    AGENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    agent_filter: bool
    archived_filter: _user_pb2_1.UserArchivedStateFilter
    def __init__(self, agent_filter: bool = ..., archived_filter: _Optional[_Union[_user_pb2_1.UserArchivedStateFilter, str]] = ...) -> None: ...

class ListPublicUsersResponse(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "username", "users")
    class User(_message.Message):
        __slots__ = ("user_id", "first_name", "last_name", "username")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        first_name: str
        last_name: str
        username: str
        def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    first_name: str
    last_name: str
    username: str
    users: _containers.RepeatedCompositeFieldContainer[ListPublicUsersResponse.User]
    def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ..., users: _Optional[_Iterable[_Union[ListPublicUsersResponse.User, _Mapping]]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users",)
    class UserDetails(_message.Message):
        __slots__ = ("user_id", "org_id", "first_name", "last_name", "username", "login_disabled", "permission_group_ids", "labels", "account_owner", "agent", "trust_ids")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        TRUST_IDS_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        org_id: str
        first_name: str
        last_name: str
        username: str
        login_disabled: bool
        permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
        account_owner: bool
        agent: bool
        trust_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ..., login_disabled: bool = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., account_owner: bool = ..., agent: bool = ..., trust_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[ListUsersResponse.UserDetails]
    def __init__(self, users: _Optional[_Iterable[_Union[ListUsersResponse.UserDetails, _Mapping]]] = ...) -> None: ...

class ListUsersByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "archived_filter")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    archived_filter: _user_pb2_1.UserArchivedStateFilter
    def __init__(self, org_id: _Optional[str] = ..., archived_filter: _Optional[_Union[_user_pb2_1.UserArchivedStateFilter, str]] = ...) -> None: ...

class ListUsersByOrgIdResponse(_message.Message):
    __slots__ = ("users",)
    class UserDetails(_message.Message):
        __slots__ = ("user_id", "org_id", "org_name", "first_name", "last_name", "username", "login_disabled", "permission_group_ids", "labels", "account_owner", "agent", "trust_ids")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_NAME_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        TRUST_IDS_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        org_id: str
        org_name: str
        first_name: str
        last_name: str
        username: str
        login_disabled: bool
        permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
        account_owner: bool
        agent: bool
        trust_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., org_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ..., login_disabled: bool = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., account_owner: bool = ..., agent: bool = ..., trust_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[ListUsersByOrgIdResponse.UserDetails]
    def __init__(self, users: _Optional[_Iterable[_Union[ListUsersByOrgIdResponse.UserDetails, _Mapping]]] = ...) -> None: ...

class ListUsersByRegionRequest(_message.Message):
    __slots__ = ("region_id", "agent", "archived_filter")
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    agent: bool
    archived_filter: _user_pb2_1.UserArchivedStateFilter
    def __init__(self, region_id: _Optional[str] = ..., agent: bool = ..., archived_filter: _Optional[_Union[_user_pb2_1.UserArchivedStateFilter, str]] = ...) -> None: ...

class ListUsersByRegionResponse(_message.Message):
    __slots__ = ("users",)
    class UserDetails(_message.Message):
        __slots__ = ("user_id", "org_id", "first_name", "last_name", "username", "login_disabled", "permission_group_ids", "labels", "account_owner", "agent", "trust_ids")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        TRUST_IDS_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        org_id: str
        first_name: str
        last_name: str
        username: str
        login_disabled: bool
        permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
        labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
        account_owner: bool
        agent: bool
        trust_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., username: _Optional[str] = ..., login_disabled: bool = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., account_owner: bool = ..., agent: bool = ..., trust_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[ListUsersByRegionResponse.UserDetails]
    def __init__(self, users: _Optional[_Iterable[_Union[ListUsersByRegionResponse.UserDetails, _Mapping]]] = ...) -> None: ...

class UpdateMyUserRequest(_message.Message):
    __slots__ = ("linkback_numbers", "caller_ids", "time_zone_override", "default_app", "field_mask")
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    time_zone_override: _org_pb2.TimeZoneWrapper
    default_app: _org_pb2.OperatorApplications
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateMyUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "partner_agent_id", "time_zone_override", "linkback_numbers", "caller_ids", "default_app", "password_reset_required", "agent_profile_group_id", "username", "email", "user_caller_id", "label_ids", "field_mask")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    first_name: str
    last_name: str
    partner_agent_id: str
    time_zone_override: _org_pb2.TimeZoneWrapper
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    default_app: _org_pb2.OperatorApplications
    password_reset_required: bool
    agent_profile_group_id: str
    username: str
    email: str
    user_caller_id: str
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., password_reset_required: bool = ..., agent_profile_group_id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., user_caller_id: _Optional[str] = ..., label_ids: _Optional[_Iterable[str]] = ..., field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserLabelsRequest(_message.Message):
    __slots__ = ("user_id", "org_id", "label_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    label_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., label_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserLabelsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserCallerIdRequest(_message.Message):
    __slots__ = ("user_id", "user_caller_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_caller_id: str
    def __init__(self, user_id: _Optional[str] = ..., user_caller_id: _Optional[str] = ...) -> None: ...

class UpdateUserCallerIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserDisabledRequest(_message.Message):
    __slots__ = ("user_id", "login_disabled")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    login_disabled: bool
    def __init__(self, user_id: _Optional[str] = ..., login_disabled: bool = ...) -> None: ...

class UpdateUserDisabledResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserDisabledByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id", "login_disabled")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    login_disabled: bool
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., login_disabled: bool = ...) -> None: ...

class UpdateUserDisabledByOrgIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMyUserPasswordResetLinkRequest(_message.Message):
    __slots__ = ("ttl",)
    TTL_FIELD_NUMBER: _ClassVar[int]
    ttl: int
    def __init__(self, ttl: _Optional[int] = ...) -> None: ...

class GetMyUserPasswordResetLinkResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetUserPasswordResetLinkRequest(_message.Message):
    __slots__ = ("user_id", "ttl")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    ttl: int
    def __init__(self, user_id: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...

class GetUserPasswordResetLinkResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetUserPasswordResetLinkByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id", "ttl")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    ttl: int
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...

class GetUserPasswordResetLinkByOrgIdResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CreatePasswordResetLinkRequest(_message.Message):
    __slots__ = ("user_id", "expiration")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreatePasswordResetLinkResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CreatePasswordResetLinkByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class CreatePasswordResetLinkByOrgIdResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetUserLoginInfoRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetUserLoginInfoResponse(_message.Message):
    __slots__ = ("blocked", "last_ip", "last_login", "last_password_reset", "logins_count", "created_at", "updated_at", "has_blocked_ips")
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    LAST_IP_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_FIELD_NUMBER: _ClassVar[int]
    LAST_PASSWORD_RESET_FIELD_NUMBER: _ClassVar[int]
    LOGINS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    HAS_BLOCKED_IPS_FIELD_NUMBER: _ClassVar[int]
    blocked: bool
    last_ip: str
    last_login: _timestamp_pb2.Timestamp
    last_password_reset: _timestamp_pb2.Timestamp
    logins_count: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    has_blocked_ips: bool
    def __init__(self, blocked: bool = ..., last_ip: _Optional[str] = ..., last_login: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_password_reset: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., logins_count: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., has_blocked_ips: bool = ...) -> None: ...

class SendPasswordResetRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class SendPasswordResetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendPasswordResetByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "email")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    email: str
    def __init__(self, org_id: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class SendPasswordResetByOrgIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetMyPasswordRequest(_message.Message):
    __slots__ = ("password",)
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class ResetMyPasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetUserPasswordRequest(_message.Message):
    __slots__ = ("password", "user_id")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    password: str
    user_id: str
    def __init__(self, password: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ResetUserPasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetUserPasswordByOrgIdRequest(_message.Message):
    __slots__ = ("password", "user_id", "org_id")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    password: str
    user_id: str
    org_id: str
    def __init__(self, password: _Optional[str] = ..., user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class ResetUserPasswordByOrgIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserEmailVerifiedRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserEmailVerifiedResponse(_message.Message):
    __slots__ = ("email_verified",)
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    email_verified: bool
    def __init__(self, email_verified: bool = ...) -> None: ...

class GetUserEmailVerifiedByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetUserEmailVerifiedByOrgIdResponse(_message.Message):
    __slots__ = ("email_verified",)
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    email_verified: bool
    def __init__(self, email_verified: bool = ...) -> None: ...

class SendUserEmailVerificationRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class SendUserEmailVerificationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendUserEmailVerificationByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class SendUserEmailVerificationByOrgIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserSessionDataRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserSessionDataResponse(_message.Message):
    __slots__ = ("user", "org_name", "p3_permissions", "permission_groups", "labels", "org_allowed_mfa")
    class User(_message.Message):
        __slots__ = ("user_id", "org_id", "username", "p3_permission_group_id", "partner_agent_id", "region_sid_map", "default_region", "api_key", "email", "login_disabled", "caller_ids", "linkback_numbers", "auth_user_id", "enable_mfa", "first_name", "last_name", "created", "last_updated", "password_reset_required", "connection_id", "time_zone_override", "permission_group_ids", "trust_ids", "default_application", "user_caller_id", "agent_profile_group_id", "agent", "account_owner", "mfa_timestamp")
        class RegionSids(_message.Message):
            __slots__ = ("login_sid", "agent_sid", "client_sid")
            LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
            AGENT_SID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
            login_sid: int
            agent_sid: int
            client_sid: int
            def __init__(self, login_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., client_sid: _Optional[int] = ...) -> None: ...
        class RegionSidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: GetUserSessionDataResponse.User.RegionSids
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GetUserSessionDataResponse.User.RegionSids, _Mapping]] = ...) -> None: ...
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_SID_MAP_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_REGION_FIELD_NUMBER: _ClassVar[int]
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
        CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
        LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        AUTH_USER_ID_FIELD_NUMBER: _ClassVar[int]
        ENABLE_MFA_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        TRUST_IDS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_APPLICATION_FIELD_NUMBER: _ClassVar[int]
        USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
        MFA_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        org_id: str
        username: str
        p3_permission_group_id: str
        partner_agent_id: str
        region_sid_map: _containers.MessageMap[str, GetUserSessionDataResponse.User.RegionSids]
        default_region: str
        api_key: str
        email: str
        login_disabled: bool
        caller_ids: _containers.RepeatedScalarFieldContainer[str]
        linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
        auth_user_id: str
        enable_mfa: bool
        first_name: str
        last_name: str
        created: _timestamp_pb2.Timestamp
        last_updated: _timestamp_pb2.Timestamp
        password_reset_required: bool
        connection_id: _wrappers_pb2.StringValue
        time_zone_override: _org_pb2.TimeZoneWrapper
        permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
        trust_ids: _containers.RepeatedScalarFieldContainer[str]
        default_application: _org_pb2.OperatorApplications
        user_caller_id: str
        agent_profile_group_id: str
        agent: bool
        account_owner: bool
        mfa_timestamp: _timestamp_pb2.Timestamp
        def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., username: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., region_sid_map: _Optional[_Mapping[str, GetUserSessionDataResponse.User.RegionSids]] = ..., default_region: _Optional[str] = ..., api_key: _Optional[str] = ..., email: _Optional[str] = ..., login_disabled: bool = ..., caller_ids: _Optional[_Iterable[str]] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., auth_user_id: _Optional[str] = ..., enable_mfa: bool = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_reset_required: bool = ..., connection_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., trust_ids: _Optional[_Iterable[str]] = ..., default_application: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., agent_profile_group_id: _Optional[str] = ..., agent: bool = ..., account_owner: bool = ..., mfa_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ORG_ALLOWED_MFA_FIELD_NUMBER: _ClassVar[int]
    user: GetUserSessionDataResponse.User
    org_name: str
    p3_permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    permission_groups: _containers.RepeatedCompositeFieldContainer[_permissions_pb2.PermissionGroup]
    labels: _containers.RepeatedCompositeFieldContainer[_labels_pb2.Label]
    org_allowed_mfa: bool
    def __init__(self, user: _Optional[_Union[GetUserSessionDataResponse.User, _Mapping]] = ..., org_name: _Optional[str] = ..., p3_permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., permission_groups: _Optional[_Iterable[_Union[_permissions_pb2.PermissionGroup, _Mapping]]] = ..., labels: _Optional[_Iterable[_Union[_labels_pb2.Label, _Mapping]]] = ..., org_allowed_mfa: bool = ...) -> None: ...

class RefreshMfaLockoutRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RefreshMfaLockoutResponse(_message.Message):
    __slots__ = ("timeout",)
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timeout: _timestamp_pb2.Timestamp
    def __init__(self, timeout: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RefreshMfaLockoutByOrgIdRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class RefreshMfaLockoutByOrgIdResponse(_message.Message):
    __slots__ = ("timeout",)
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timeout: _timestamp_pb2.Timestamp
    def __init__(self, timeout: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetMfaTypeRequest(_message.Message):
    __slots__ = ("otp",)
    OTP_FIELD_NUMBER: _ClassVar[int]
    otp: _user_pb2.MfaInfo.OtpType
    def __init__(self, otp: _Optional[_Union[_user_pb2.MfaInfo.OtpType, _Mapping]] = ...) -> None: ...

class SetMfaTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableUserMfaRequest(_message.Message):
    __slots__ = ("user_id", "enabled")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    enabled: bool
    def __init__(self, user_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class EnableUserMfaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableMyUserMfaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableMyUserMfaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserMfaInfoRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserMfaInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _user_pb2.MfaInfo
    def __init__(self, info: _Optional[_Union[_user_pb2.MfaInfo, _Mapping]] = ...) -> None: ...

class GetMyUserMfaInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMyUserMfaInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _user_pb2.MfaInfo
    def __init__(self, info: _Optional[_Union[_user_pb2.MfaInfo, _Mapping]] = ...) -> None: ...
