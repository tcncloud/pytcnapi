from api.commons import org_pb2 as _org_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_id", "org_id", "username", "p3_permission_group_id", "login_sid", "agent_sid", "region_id", "partner_agent_id", "client_sid", "region_sid_map", "api_key", "email", "login_disabled", "caller_ids", "linkback_numbers", "auth_user_id", "enable_mfa", "first_name", "last_name", "created", "last_updated", "password_reset_required", "connection_id", "time_zone_override", "permission_group_ids", "trust_ids", "default_region", "default_application", "user_caller_id", "agent_profile_group_id", "skills", "agent", "account_owner", "email_verified", "whitelisted_ips")
    class RegionSidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: User.RegionSids
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[User.RegionSids, _Mapping]] = ...) -> None: ...
    class RegionSids(_message.Message):
        __slots__ = ("login_sid", "agent_sid", "client_sid")
        LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
        AGENT_SID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
        login_sid: int
        agent_sid: int
        client_sid: int
        def __init__(self, login_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., client_sid: _Optional[int] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    REGION_SID_MAP_FIELD_NUMBER: _ClassVar[int]
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
    DEFAULT_REGION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_IPS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    username: str
    p3_permission_group_id: str
    login_sid: int
    agent_sid: int
    region_id: str
    partner_agent_id: str
    client_sid: int
    region_sid_map: _containers.MessageMap[str, User.RegionSids]
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
    default_region: str
    default_application: _org_pb2.OperatorApplications
    user_caller_id: str
    agent_profile_group_id: str
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    agent: bool
    account_owner: bool
    email_verified: bool
    whitelisted_ips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., username: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., login_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., region_id: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., client_sid: _Optional[int] = ..., region_sid_map: _Optional[_Mapping[str, User.RegionSids]] = ..., api_key: _Optional[str] = ..., email: _Optional[str] = ..., login_disabled: bool = ..., caller_ids: _Optional[_Iterable[str]] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., auth_user_id: _Optional[str] = ..., enable_mfa: bool = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_reset_required: bool = ..., connection_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., trust_ids: _Optional[_Iterable[str]] = ..., default_region: _Optional[str] = ..., default_application: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., agent_profile_group_id: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., agent: bool = ..., account_owner: bool = ..., email_verified: bool = ..., whitelisted_ips: _Optional[_Iterable[str]] = ...) -> None: ...

class MfaInfo(_message.Message):
    __slots__ = ("org_id", "user_id", "mfa_enabled", "none", "otp", "duo", "totp")
    class NoneSelected(_message.Message):
        __slots__ = ("timeout",)
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        timeout: _timestamp_pb2.Timestamp
        def __init__(self, timeout: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class OtpType(_message.Message):
        __slots__ = ("email",)
        class EmailDeliveryMethod(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        email: MfaInfo.OtpType.EmailDeliveryMethod
        def __init__(self, email: _Optional[_Union[MfaInfo.OtpType.EmailDeliveryMethod, _Mapping]] = ...) -> None: ...
    class Duo(_message.Message):
        __slots__ = ("duo_username",)
        DUO_USERNAME_FIELD_NUMBER: _ClassVar[int]
        duo_username: str
        def __init__(self, duo_username: _Optional[str] = ...) -> None: ...
    class Totp(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MFA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NONE_FIELD_NUMBER: _ClassVar[int]
    OTP_FIELD_NUMBER: _ClassVar[int]
    DUO_FIELD_NUMBER: _ClassVar[int]
    TOTP_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    user_id: str
    mfa_enabled: bool
    none: MfaInfo.NoneSelected
    otp: MfaInfo.OtpType
    duo: MfaInfo.Duo
    totp: MfaInfo.Totp
    def __init__(self, org_id: _Optional[str] = ..., user_id: _Optional[str] = ..., mfa_enabled: bool = ..., none: _Optional[_Union[MfaInfo.NoneSelected, _Mapping]] = ..., otp: _Optional[_Union[MfaInfo.OtpType, _Mapping]] = ..., duo: _Optional[_Union[MfaInfo.Duo, _Mapping]] = ..., totp: _Optional[_Union[MfaInfo.Totp, _Mapping]] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("level", "name", "description", "skill_sid")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    level: int
    name: str
    description: str
    skill_sid: int
    def __init__(self, level: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skill_sid: _Optional[int] = ...) -> None: ...

class PasswordResetLink(_message.Message):
    __slots__ = ("link_id", "user_id", "org_id", "expiration")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    user_id: str
    org_id: str
    expiration: _timestamp_pb2.Timestamp
    def __init__(self, link_id: _Optional[str] = ..., user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
