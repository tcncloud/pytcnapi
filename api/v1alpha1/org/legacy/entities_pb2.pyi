from api.commons import ana_pb2 as _ana_pb2
from api.commons.audit import event_types_pb2 as _event_types_pb2
from api.commons.auth import perms_pb2 as _perms_pb2
from api.commons import country_pb2 as _country_pb2
from api.commons import lms_pb2 as _lms_pb2
from api.commons import logging_pb2 as _logging_pb2
from api.commons import notifications_pb2 as _notifications_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons.org import agent_profile_group_pb2 as _agent_profile_group_pb2
from api.commons.org import trusts_pb2 as _trusts_pb2
from api.commons import org_preferences_pb2 as _org_preferences_pb2
from api.commons import perms_pb2 as _perms_pb2_1
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAgentQuickViewPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAgentQuickViewPreferencesResponse(_message.Message):
    __slots__ = ("agent_status_display_template",)
    AGENT_STATUS_DISPLAY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    agent_status_display_template: AgentStatusDisplayTemplate
    def __init__(self, agent_status_display_template: _Optional[_Union[AgentStatusDisplayTemplate, _Mapping]] = ...) -> None: ...

class EditAgentQuickViewPreferencesRequest(_message.Message):
    __slots__ = ("agent_status_display_template",)
    AGENT_STATUS_DISPLAY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    agent_status_display_template: AgentStatusDisplayTemplate
    def __init__(self, agent_status_display_template: _Optional[_Union[AgentStatusDisplayTemplate, _Mapping]] = ...) -> None: ...

class EditAgentQuickViewPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentStatusDisplayTemplate(_message.Message):
    __slots__ = ("ready_styles", "in_conference_styles", "wrap_up_styles", "paused_styles", "transfer_call_styles", "preview_call_styles", "manual_call_styles", "pbx_call_styles", "agent_intercom_styles", "xml_client_property_sid", "call_connecting_styles", "intercom_source_styles", "intercom_destination_styles", "transfer_lost_styles")
    class AgentStatusSinceStyle(_message.Message):
        __slots__ = ("bg_red", "bg_green", "bg_blue", "fg_red", "fg_green", "fg_blue", "agent_gui_status", "duration_in_status")
        BG_RED_FIELD_NUMBER: _ClassVar[int]
        BG_GREEN_FIELD_NUMBER: _ClassVar[int]
        BG_BLUE_FIELD_NUMBER: _ClassVar[int]
        FG_RED_FIELD_NUMBER: _ClassVar[int]
        FG_GREEN_FIELD_NUMBER: _ClassVar[int]
        FG_BLUE_FIELD_NUMBER: _ClassVar[int]
        AGENT_GUI_STATUS_FIELD_NUMBER: _ClassVar[int]
        DURATION_IN_STATUS_FIELD_NUMBER: _ClassVar[int]
        bg_red: str
        bg_green: str
        bg_blue: str
        fg_red: str
        fg_green: str
        fg_blue: str
        agent_gui_status: int
        duration_in_status: int
        def __init__(self, bg_red: _Optional[str] = ..., bg_green: _Optional[str] = ..., bg_blue: _Optional[str] = ..., fg_red: _Optional[str] = ..., fg_green: _Optional[str] = ..., fg_blue: _Optional[str] = ..., agent_gui_status: _Optional[int] = ..., duration_in_status: _Optional[int] = ...) -> None: ...
    READY_STYLES_FIELD_NUMBER: _ClassVar[int]
    IN_CONFERENCE_STYLES_FIELD_NUMBER: _ClassVar[int]
    WRAP_UP_STYLES_FIELD_NUMBER: _ClassVar[int]
    PAUSED_STYLES_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CALL_STYLES_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_CALL_STYLES_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CALL_STYLES_FIELD_NUMBER: _ClassVar[int]
    PBX_CALL_STYLES_FIELD_NUMBER: _ClassVar[int]
    AGENT_INTERCOM_STYLES_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_CONNECTING_STYLES_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_SOURCE_STYLES_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_DESTINATION_STYLES_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_LOST_STYLES_FIELD_NUMBER: _ClassVar[int]
    ready_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    in_conference_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    wrap_up_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    paused_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    transfer_call_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    preview_call_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    manual_call_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    pbx_call_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    agent_intercom_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    xml_client_property_sid: int
    call_connecting_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    intercom_source_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    intercom_destination_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    transfer_lost_styles: _containers.RepeatedCompositeFieldContainer[AgentStatusDisplayTemplate.AgentStatusSinceStyle]
    def __init__(self, ready_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., in_conference_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., wrap_up_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., paused_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., transfer_call_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., preview_call_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., manual_call_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., pbx_call_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., agent_intercom_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., xml_client_property_sid: _Optional[int] = ..., call_connecting_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., intercom_source_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., intercom_destination_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ..., transfer_lost_styles: _Optional[_Iterable[_Union[AgentStatusDisplayTemplate.AgentStatusSinceStyle, _Mapping]]] = ...) -> None: ...

class LocationDescription(_message.Message):
    __slots__ = ("location_name", "address", "zip", "state", "phone", "fax", "email", "contact_first_name", "contact_last_name", "company_name", "city", "country")
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    FAX_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    location_name: str
    address: str
    zip: str
    state: str
    phone: str
    fax: str
    email: str
    contact_first_name: str
    contact_last_name: str
    company_name: str
    city: str
    country: str
    def __init__(self, location_name: _Optional[str] = ..., address: _Optional[str] = ..., zip: _Optional[str] = ..., state: _Optional[str] = ..., phone: _Optional[str] = ..., fax: _Optional[str] = ..., email: _Optional[str] = ..., contact_first_name: _Optional[str] = ..., contact_last_name: _Optional[str] = ..., company_name: _Optional[str] = ..., city: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class GetOrganizationProfileRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrganizationProfileResponse(_message.Message):
    __slots__ = ("org_id", "name", "is_manual_only_account", "region_id", "crm_id", "billing_id", "timezone", "add_date", "allowed_regions")
    class AllowedRegionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RegionUrls
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RegionUrls, _Mapping]] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_ONLY_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CRM_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ADD_DATE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    name: str
    is_manual_only_account: bool
    region_id: str
    crm_id: str
    billing_id: str
    timezone: _org_pb2.TimeZone
    add_date: _timestamp_pb2.Timestamp
    allowed_regions: _containers.MessageMap[str, RegionUrls]
    def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., is_manual_only_account: bool = ..., region_id: _Optional[str] = ..., crm_id: _Optional[str] = ..., billing_id: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allowed_regions: _Optional[_Mapping[str, RegionUrls]] = ...) -> None: ...

class RegionUrls(_message.Message):
    __slots__ = ("api_endpoints",)
    API_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    api_endpoints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, api_endpoints: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOrganizationProfileByIdRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListOrganizationDescriptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OrganizationDescription(_message.Message):
    __slots__ = ("billing_id", "add_date", "client_sid", "name", "org_id", "region_id", "last_scheduled_date")
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_DATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    billing_id: str
    add_date: _timestamp_pb2.Timestamp
    client_sid: int
    name: str
    org_id: str
    region_id: str
    last_scheduled_date: _timestamp_pb2.Timestamp
    def __init__(self, billing_id: _Optional[str] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., client_sid: _Optional[int] = ..., name: _Optional[str] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListOrganizationDescriptionsResponse(_message.Message):
    __slots__ = ("organization_descriptions",)
    ORGANIZATION_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_descriptions: _containers.RepeatedCompositeFieldContainer[OrganizationDescription]
    def __init__(self, organization_descriptions: _Optional[_Iterable[_Union[OrganizationDescription, _Mapping]]] = ...) -> None: ...

class UserDescription(_message.Message):
    __slots__ = ("user_id", "org_id", "user_name", "login_disabled", "account_owner", "org_name", "org_billing_id", "linkback_numbers", "caller_ids", "login_sid", "permission_groups", "agent_sid", "agent_profile_group_id", "agent_profile_group_name", "p3_permission_group_id", "p3_permission_group_name", "first_name", "last_name", "strike_count", "created", "last_updated", "label_entities", "delegated", "time_zone_override", "email", "hunt_group_sid", "hunt_group_name", "trusts")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    STRIKE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    LABEL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    user_name: str
    login_disabled: bool
    account_owner: bool
    org_name: str
    org_billing_id: str
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    login_sid: int
    permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    agent_sid: int
    agent_profile_group_id: str
    agent_profile_group_name: str
    p3_permission_group_id: str
    p3_permission_group_name: str
    first_name: str
    last_name: str
    strike_count: int
    created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    label_entities: _containers.RepeatedCompositeFieldContainer[Label]
    delegated: bool
    time_zone_override: _org_pb2.TimeZoneWrapper
    email: str
    hunt_group_sid: int
    hunt_group_name: str
    trusts: _containers.RepeatedCompositeFieldContainer[_trusts_pb2.Trust]
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., user_name: _Optional[str] = ..., login_disabled: bool = ..., account_owner: bool = ..., org_name: _Optional[str] = ..., org_billing_id: _Optional[str] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., login_sid: _Optional[int] = ..., permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ..., agent_sid: _Optional[int] = ..., agent_profile_group_id: _Optional[str] = ..., agent_profile_group_name: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., p3_permission_group_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., strike_count: _Optional[int] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., label_entities: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., delegated: bool = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., email: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ..., trusts: _Optional[_Iterable[_Union[_trusts_pb2.Trust, _Mapping]]] = ...) -> None: ...

class ListOrganizationUserDescriptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListOrganizationUserDescriptionsResponse(_message.Message):
    __slots__ = ("user_descriptions",)
    USER_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    user_descriptions: _containers.RepeatedCompositeFieldContainer[UserDescription]
    def __init__(self, user_descriptions: _Optional[_Iterable[_Union[UserDescription, _Mapping]]] = ...) -> None: ...

class ListRegionalOrganizationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRegionalOrganizationsResponse(_message.Message):
    __slots__ = ("organization_descriptions",)
    ORGANIZATION_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_descriptions: _containers.RepeatedCompositeFieldContainer[OrganizationDescription]
    def __init__(self, organization_descriptions: _Optional[_Iterable[_Union[OrganizationDescription, _Mapping]]] = ...) -> None: ...

class GetUserDirectoryRequest(_message.Message):
    __slots__ = ("agents_only",)
    AGENTS_ONLY_FIELD_NUMBER: _ClassVar[int]
    agents_only: bool
    def __init__(self, agents_only: bool = ...) -> None: ...

class GetUserDirectoryResponse(_message.Message):
    __slots__ = ("user_directory",)
    USER_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    user_directory: _containers.RepeatedCompositeFieldContainer[UserDirectoryEntry]
    def __init__(self, user_directory: _Optional[_Iterable[_Union[UserDirectoryEntry, _Mapping]]] = ...) -> None: ...

class UserDirectoryEntry(_message.Message):
    __slots__ = ("user_id", "full_name", "user_name", "first_name", "last_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    full_name: str
    user_name: str
    first_name: str
    last_name: str
    def __init__(self, user_id: _Optional[str] = ..., full_name: _Optional[str] = ..., user_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class GetTempUserTokenReq(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetTempUserTokenRes(_message.Message):
    __slots__ = ("region_id", "token")
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    token: str
    def __init__(self, region_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class ListUserDescriptionsRequest(_message.Message):
    __slots__ = ("region_id", "org_id_filter")
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    org_id_filter: str
    def __init__(self, region_id: _Optional[str] = ..., org_id_filter: _Optional[str] = ...) -> None: ...

class ListUserDescriptionsResponse(_message.Message):
    __slots__ = ("user_descriptions",)
    USER_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    user_descriptions: _containers.RepeatedCompositeFieldContainer[UserDescription]
    def __init__(self, user_descriptions: _Optional[_Iterable[_Union[UserDescription, _Mapping]]] = ...) -> None: ...

class GetRegionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRegionsResponse(_message.Message):
    __slots__ = ("region_names",)
    REGION_NAMES_FIELD_NUMBER: _ClassVar[int]
    region_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, region_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUserDetailsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AdminGetUserDetailsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

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

class UserDetails(_message.Message):
    __slots__ = ("user_id", "user_name", "organization_name", "location_name", "p3_permission_group", "permission_groups", "default_region", "allowed_regions", "disabled", "partner_agent_id", "agent_sid", "org_id", "linkback_numbers", "caller_ids", "login_sid", "default_app", "user_caller_id", "hunt_group_sid", "hunt_group_name", "skills", "first_name", "last_name", "created", "last_updated", "password_reset_required", "agent_profile_group_id", "label_entities", "delegated", "time_zone_override", "email", "email_verified", "trusts")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REGION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    TRUSTS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_name: str
    organization_name: str
    location_name: str
    p3_permission_group: str
    permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    default_region: str
    allowed_regions: _containers.RepeatedScalarFieldContainer[str]
    disabled: bool
    partner_agent_id: str
    agent_sid: int
    org_id: str
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    login_sid: int
    default_app: _org_pb2.OperatorApplications
    user_caller_id: str
    hunt_group_sid: int
    hunt_group_name: str
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    first_name: str
    last_name: str
    created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    password_reset_required: bool
    agent_profile_group_id: str
    label_entities: _containers.RepeatedCompositeFieldContainer[Label]
    delegated: bool
    time_zone_override: _org_pb2.TimeZoneWrapper
    email: str
    email_verified: bool
    trusts: _containers.RepeatedCompositeFieldContainer[_trusts_pb2.Trust]
    def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., organization_name: _Optional[str] = ..., location_name: _Optional[str] = ..., p3_permission_group: _Optional[str] = ..., permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ..., default_region: _Optional[str] = ..., allowed_regions: _Optional[_Iterable[str]] = ..., disabled: bool = ..., partner_agent_id: _Optional[str] = ..., agent_sid: _Optional[int] = ..., org_id: _Optional[str] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., login_sid: _Optional[int] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_reset_required: bool = ..., agent_profile_group_id: _Optional[str] = ..., label_entities: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., delegated: bool = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., email: _Optional[str] = ..., email_verified: bool = ..., trusts: _Optional[_Iterable[_Union[_trusts_pb2.Trust, _Mapping]]] = ...) -> None: ...

class AgentUser(_message.Message):
    __slots__ = ("user_id", "name", "user_name", "hunt_group_name", "skills", "partner_agent_id", "callback_extension", "callback_number", "hunt_group_sid", "agent_sid", "user_caller_id", "first_name", "last_name", "created", "last_updated", "agent_profile_group_id", "delegated", "agent_profile_group_name", "disabled", "has_agent_perm", "time_zone_override", "email", "label_entities", "permission_groups")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    HAS_AGENT_PERM_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LABEL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    user_name: str
    hunt_group_name: str
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    partner_agent_id: str
    callback_extension: str
    callback_number: str
    hunt_group_sid: int
    agent_sid: int
    user_caller_id: str
    first_name: str
    last_name: str
    created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    agent_profile_group_id: str
    delegated: bool
    agent_profile_group_name: str
    disabled: bool
    has_agent_perm: bool
    time_zone_override: _org_pb2.TimeZoneWrapper
    email: str
    label_entities: _containers.RepeatedCompositeFieldContainer[Label]
    permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., user_name: _Optional[str] = ..., hunt_group_name: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., partner_agent_id: _Optional[str] = ..., callback_extension: _Optional[str] = ..., callback_number: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., user_caller_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_profile_group_id: _Optional[str] = ..., delegated: bool = ..., agent_profile_group_name: _Optional[str] = ..., disabled: bool = ..., has_agent_perm: bool = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., email: _Optional[str] = ..., label_entities: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ...) -> None: ...

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

class GetAgentUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentUsersResponse(_message.Message):
    __slots__ = ("agent_users",)
    AGENT_USERS_FIELD_NUMBER: _ClassVar[int]
    agent_users: _containers.RepeatedCompositeFieldContainer[AgentUser]
    def __init__(self, agent_users: _Optional[_Iterable[_Union[AgentUser, _Mapping]]] = ...) -> None: ...

class GetAgentSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentSettingsResponse(_message.Message):
    __slots__ = ("user_caller_id", "priority_groups", "reserved_carriers")
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CARRIERS_FIELD_NUMBER: _ClassVar[int]
    user_caller_id: str
    priority_groups: _containers.RepeatedCompositeFieldContainer[PriorityGroup]
    reserved_carriers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_caller_id: _Optional[str] = ..., priority_groups: _Optional[_Iterable[_Union[PriorityGroup, _Mapping]]] = ..., reserved_carriers: _Optional[_Iterable[str]] = ...) -> None: ...

class PriorityGroup(_message.Message):
    __slots__ = ("threshold", "channel_type")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    channel_type: _omnichannel_pb2.ChannelType
    def __init__(self, threshold: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ...) -> None: ...

class GetAgentProfileGroupRequest(_message.Message):
    __slots__ = ("agent_profile_group_id",)
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class GetAgentProfileGroupResponse(_message.Message):
    __slots__ = ("agent_profile_group",)
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class UpdateAgentProfileGroupRequest(_message.Message):
    __slots__ = ("agent_profile_group",)
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class UpdateAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateAgentProfileGroupRequest(_message.Message):
    __slots__ = ("agent_profile_group",)
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class CreateAgentProfileGroupResponse(_message.Message):
    __slots__ = ("agent_profile_group_id",)
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class ListAgentProfileGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentProfileGroupsResponse(_message.Message):
    __slots__ = ("agent_profile_groups",)
    AGENT_PROFILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    agent_profile_groups: _containers.RepeatedCompositeFieldContainer[_agent_profile_group_pb2.AgentProfileGroup]
    def __init__(self, agent_profile_groups: _Optional[_Iterable[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]]] = ...) -> None: ...

class DeleteAgentProfileGroupRequest(_message.Message):
    __slots__ = ("agent_profile_group_id",)
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class DeleteAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignAgentProfileGroupsRequest(_message.Message):
    __slots__ = ("agent_profile_group_id", "user_ids")
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_profile_group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignAgentProfileGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "partner_agent_id", "time_zone_override", "linkback_numbers", "caller_ids", "user_name", "default_app", "user_caller_id", "password_reset_required", "agent_profile_group_id", "label_entities", "email", "field_mask")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    first_name: str
    last_name: str
    partner_agent_id: str
    time_zone_override: _org_pb2.TimeZoneWrapper
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    user_name: str
    default_app: _org_pb2.OperatorApplications
    user_caller_id: str
    password_reset_required: bool
    agent_profile_group_id: str
    label_entities: _containers.RepeatedCompositeFieldContainer[Label]
    email: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., user_name: _Optional[str] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., password_reset_required: bool = ..., agent_profile_group_id: _Optional[str] = ..., label_entities: _Optional[_Iterable[_Union[Label, _Mapping]]] = ..., email: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Country(_message.Message):
    __slots__ = ("country_id", "country_sid", "country_name", "phone_digits", "region_digits", "total_digits", "country_code", "region_codes", "country")
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_DIGITS_FIELD_NUMBER: _ClassVar[int]
    REGION_DIGITS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIGITS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country_id: str
    country_sid: int
    country_name: str
    phone_digits: int
    region_digits: int
    total_digits: int
    country_code: int
    region_codes: _containers.RepeatedScalarFieldContainer[str]
    country: _country_pb2.Country
    def __init__(self, country_id: _Optional[str] = ..., country_sid: _Optional[int] = ..., country_name: _Optional[str] = ..., phone_digits: _Optional[int] = ..., region_digits: _Optional[int] = ..., total_digits: _Optional[int] = ..., country_code: _Optional[int] = ..., region_codes: _Optional[_Iterable[str]] = ..., country: _Optional[_Union[_country_pb2.Country, str]] = ...) -> None: ...

class GetCountriesListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCountriesListResponse(_message.Message):
    __slots__ = ("countries",)
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(self, countries: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("user_id", "org_id", "region_id", "partner_agent_id", "login_sid", "agent_sid", "regions", "email", "caller_ids", "linkback_numbers", "user_name", "first_name", "last_name", "created", "last_updated", "password_reset_required", "connection_id", "time_zone_override", "label_entities")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LABEL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    region_id: str
    partner_agent_id: str
    login_sid: int
    agent_sid: int
    regions: _containers.RepeatedScalarFieldContainer[str]
    email: str
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    user_name: str
    first_name: str
    last_name: str
    created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    password_reset_required: bool
    connection_id: _wrappers_pb2.StringValue
    time_zone_override: _org_pb2.TimeZoneWrapper
    label_entities: _containers.RepeatedCompositeFieldContainer[Label]
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., partner_agent_id: _Optional[str] = ..., login_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., regions: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., caller_ids: _Optional[_Iterable[str]] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., user_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_reset_required: bool = ..., connection_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ..., label_entities: _Optional[_Iterable[_Union[Label, _Mapping]]] = ...) -> None: ...

class GetPermissionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPermissionsResponse(_message.Message):
    __slots__ = ("user", "permissions", "ui_log_level", "org_name", "log_level", "p3_permissions", "org_default_region_id", "default_app")
    USER_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    UI_LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ORG_DEFAULT_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    user: User
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    ui_log_level: str
    org_name: str
    log_level: _logging_pb2.Level
    p3_permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    org_default_region_id: str
    default_app: _org_pb2.OperatorApplications
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., ui_log_level: _Optional[str] = ..., org_name: _Optional[str] = ..., log_level: _Optional[_Union[_logging_pb2.Level, str]] = ..., p3_permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ..., org_default_region_id: _Optional[str] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ...) -> None: ...

class UpdateUserDisabledRequest(_message.Message):
    __slots__ = ("user_id", "disable", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    disable: bool
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., disable: bool = ..., org_id: _Optional[str] = ...) -> None: ...

class UpdateUserDisabledResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBulkUsersDisabledRequest(_message.Message):
    __slots__ = ("user_ids", "disable")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    disable: bool
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., disable: bool = ...) -> None: ...

class UpdateBulkUsersDisabledResponse(_message.Message):
    __slots__ = ("updated_ids",)
    UPDATED_IDS_FIELD_NUMBER: _ClassVar[int]
    updated_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, updated_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteOrganizationPropertiesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BillingRegion(_message.Message):
    __slots__ = ("name", "description", "prefixes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., prefixes: _Optional[_Iterable[str]] = ...) -> None: ...

class BillingRate(_message.Message):
    __slots__ = ("standard_ppi", "linkback_ppi", "vocal_direct_msg_rate", "sms_msg_rate", "billing_increment_seconds", "min_billed_increments", "min_linkback_billed_increments", "inbound_ppi", "max_billed_increments", "max_linkback_billed_increments", "machine_hangup_increments", "human_hangup_increments")
    STANDARD_PPI_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_PPI_FIELD_NUMBER: _ClassVar[int]
    VOCAL_DIRECT_MSG_RATE_FIELD_NUMBER: _ClassVar[int]
    SMS_MSG_RATE_FIELD_NUMBER: _ClassVar[int]
    BILLING_INCREMENT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MIN_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    MIN_LINKBACK_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    INBOUND_PPI_FIELD_NUMBER: _ClassVar[int]
    MAX_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_LINKBACK_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_HANGUP_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    HUMAN_HANGUP_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    standard_ppi: float
    linkback_ppi: float
    vocal_direct_msg_rate: float
    sms_msg_rate: float
    billing_increment_seconds: int
    min_billed_increments: int
    min_linkback_billed_increments: int
    inbound_ppi: _wrappers_pb2.DoubleValue
    max_billed_increments: _wrappers_pb2.Int64Value
    max_linkback_billed_increments: _wrappers_pb2.Int64Value
    machine_hangup_increments: _wrappers_pb2.Int64Value
    human_hangup_increments: _wrappers_pb2.Int64Value
    def __init__(self, standard_ppi: _Optional[float] = ..., linkback_ppi: _Optional[float] = ..., vocal_direct_msg_rate: _Optional[float] = ..., sms_msg_rate: _Optional[float] = ..., billing_increment_seconds: _Optional[int] = ..., min_billed_increments: _Optional[int] = ..., min_linkback_billed_increments: _Optional[int] = ..., inbound_ppi: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., max_billed_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_linkback_billed_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., machine_hangup_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., human_hangup_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class BillingRegionRate(_message.Message):
    __slots__ = ("billing_region", "billing_rate", "billing_region_id", "country_id", "is_custom")
    BILLING_REGION_FIELD_NUMBER: _ClassVar[int]
    BILLING_RATE_FIELD_NUMBER: _ClassVar[int]
    BILLING_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    billing_region: BillingRegion
    billing_rate: BillingRate
    billing_region_id: str
    country_id: str
    is_custom: bool
    def __init__(self, billing_region: _Optional[_Union[BillingRegion, _Mapping]] = ..., billing_rate: _Optional[_Union[BillingRate, _Mapping]] = ..., billing_region_id: _Optional[str] = ..., country_id: _Optional[str] = ..., is_custom: bool = ...) -> None: ...

class ListBillingRegionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBillingRegionsResponse(_message.Message):
    __slots__ = ("billing_region_rates",)
    BILLING_REGION_RATES_FIELD_NUMBER: _ClassVar[int]
    billing_region_rates: _containers.RepeatedCompositeFieldContainer[BillingRegionRate]
    def __init__(self, billing_region_rates: _Optional[_Iterable[_Union[BillingRegionRate, _Mapping]]] = ...) -> None: ...

class PermissionGroup(_message.Message):
    __slots__ = ("id", "name", "description", "permissions", "read_only")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    read_only: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ..., read_only: bool = ...) -> None: ...

class ListPermissionGroupsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListPermissionGroupsResponse(_message.Message):
    __slots__ = ("permission_groups",)
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    def __init__(self, permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ...) -> None: ...

class CreatePermissionGroupRequest(_message.Message):
    __slots__ = ("name", "description", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class CreatePermissionGroupResponse(_message.Message):
    __slots__ = ("permission_group",)
    PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    permission_group: PermissionGroup
    def __init__(self, permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class UpdatePermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group",)
    PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    permission_group: PermissionGroup
    def __init__(self, permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class UpdatePermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id",)
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    def __init__(self, permission_group_id: _Optional[str] = ...) -> None: ...

class DeletePermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignUserToAccountOwnerPermissionGroupRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AssignUserToAccountOwnerPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignUserPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "assign_user_id")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_USER_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    assign_user_id: str
    def __init__(self, permission_group_id: _Optional[str] = ..., assign_user_id: _Optional[str] = ...) -> None: ...

class AssignUserPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignUsersPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "assign_user_ids")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    assign_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission_group_id: _Optional[str] = ..., assign_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignUsersPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateUserNeoPermissionGroupsRequest(_message.Message):
    __slots__ = ("assign_user_id", "permission_group_ids")
    ASSIGN_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    assign_user_id: str
    permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, assign_user_id: _Optional[str] = ..., permission_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserNeoPermissionGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeUserPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "revoke_user_id")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_USER_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    revoke_user_id: str
    def __init__(self, permission_group_id: _Optional[str] = ..., revoke_user_id: _Optional[str] = ...) -> None: ...

class RevokeUserPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeUsersPermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id", "revoke_user_ids")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    revoke_user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission_group_id: _Optional[str] = ..., revoke_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeUsersPermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListP3PermissionGroupsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListP3PermissionGroupsResponse(_message.Message):
    __slots__ = ("permission_groups",)
    PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    permission_groups: _containers.RepeatedCompositeFieldContainer[P3PermissionGroup]
    def __init__(self, permission_groups: _Optional[_Iterable[_Union[P3PermissionGroup, _Mapping]]] = ...) -> None: ...

class P3PermissionGroup(_message.Message):
    __slots__ = ("permission_group_id", "name", "description", "permissions", "permission_group_sid")
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    permission_group_sid: int
    def __init__(self, permission_group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ..., permission_group_sid: _Optional[int] = ...) -> None: ...

class CreateP3PermissionGroupRequest(_message.Message):
    __slots__ = ("name", "description", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ...) -> None: ...

class CreateP3PermissionGroupResponse(_message.Message):
    __slots__ = ("p3_permission_group",)
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group: P3PermissionGroup
    def __init__(self, p3_permission_group: _Optional[_Union[P3PermissionGroup, _Mapping]] = ...) -> None: ...

class UpdateP3PermissionGroupRequest(_message.Message):
    __slots__ = ("org_id", "permission_group_id", "name", "description", "permissions")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permission_group_id: str
    name: str
    description: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2_1.Permission]
    def __init__(self, org_id: _Optional[str] = ..., permission_group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2_1.Permission, str]]] = ...) -> None: ...

class UpdateP3PermissionGroupResponse(_message.Message):
    __slots__ = ("p3_permission_group",)
    P3_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    p3_permission_group: P3PermissionGroup
    def __init__(self, p3_permission_group: _Optional[_Union[P3PermissionGroup, _Mapping]] = ...) -> None: ...

class DeleteP3PermissionGroupRequest(_message.Message):
    __slots__ = ("permission_group_id",)
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    def __init__(self, permission_group_id: _Optional[str] = ...) -> None: ...

class DeleteP3PermissionGroupResponse(_message.Message):
    __slots__ = ("permission_group_id",)
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    permission_group_id: str
    def __init__(self, permission_group_id: _Optional[str] = ...) -> None: ...

class AddLoginToUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AddLoginToUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignUsersP3PermissionGroupRequest(_message.Message):
    __slots__ = ("user_ids", "permission_group_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class AssignUsersP3PermissionGroupResponse(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RevokeUsersP3PermissionGroupRequest(_message.Message):
    __slots__ = ("user_ids", "permission_group_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    permission_group_id: str
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., permission_group_id: _Optional[str] = ...) -> None: ...

class RevokeUsersP3PermissionGroupResponse(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SyncP3PermissionGroupRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class SyncP3PermissionGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterOrganizationRequest(_message.Message):
    __slots__ = ("organization", "allowed_countries", "p3_parent_account")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    P3_PARENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    allowed_countries: _containers.RepeatedScalarFieldContainer[_country_pb2.Country]
    p3_parent_account: str
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ..., p3_parent_account: _Optional[str] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ("is_manual_only_account", "backoffice_theme", "contract_number", "crm_id", "time_zone_enum", "name")
    IS_MANUAL_ONLY_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKOFFICE_THEME_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CRM_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_ENUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    is_manual_only_account: bool
    backoffice_theme: _org_pb2.ClientSkin
    contract_number: str
    crm_id: str
    time_zone_enum: _org_pb2.TimeZone
    name: str
    def __init__(self, is_manual_only_account: bool = ..., backoffice_theme: _Optional[_Union[_org_pb2.ClientSkin, str]] = ..., contract_number: _Optional[str] = ..., crm_id: _Optional[str] = ..., time_zone_enum: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., name: _Optional[str] = ...) -> None: ...

class RegisterOrganizationResponse(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("org_id", "time_zone", "name", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    time_zone: _org_pb2.TimeZone
    name: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., name: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveOrganizationRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ArchiveOrganizationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnArchiveOrganizationRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class UnArchiveOrganizationResponse(_message.Message):
    __slots__ = ("organization_description",)
    ORGANIZATION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    organization_description: OrganizationDescription
    def __init__(self, organization_description: _Optional[_Union[OrganizationDescription, _Mapping]] = ...) -> None: ...

class ListArchivedOrganizationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListArchivedOrganizationsResponse(_message.Message):
    __slots__ = ("archived_organization_descriptions",)
    ARCHIVED_ORGANIZATION_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    archived_organization_descriptions: _containers.RepeatedCompositeFieldContainer[OrganizationDescription]
    def __init__(self, archived_organization_descriptions: _Optional[_Iterable[_Union[OrganizationDescription, _Mapping]]] = ...) -> None: ...

class AddUserRegionRequest(_message.Message):
    __slots__ = ("user_id", "region_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    region_id: str
    def __init__(self, user_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class AddUserRegionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveUserRegionRequest(_message.Message):
    __slots__ = ("user_id", "region_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    region_id: str
    def __init__(self, user_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class RemoveUserRegionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitDefaultPermissionGroupsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class InitDefaultPermissionGroupsResponse(_message.Message):
    __slots__ = ("default_permission_groups",)
    DEFAULT_PERMISSION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    default_permission_groups: _containers.RepeatedCompositeFieldContainer[PermissionGroup]
    def __init__(self, default_permission_groups: _Optional[_Iterable[_Union[PermissionGroup, _Mapping]]] = ...) -> None: ...

class AddPermissionToAccountOwnerPermissionGroupRequest(_message.Message):
    __slots__ = ("org_id", "permissions")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, org_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class AddPermissionToAccountOwnerPermissionGroupResponse(_message.Message):
    __slots__ = ("default_permission_group",)
    DEFAULT_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_permission_group: PermissionGroup
    def __init__(self, default_permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class RevokePermissionToAccountOwnerPermissionGroupRequest(_message.Message):
    __slots__ = ("org_id", "permissions")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permissions: _containers.RepeatedScalarFieldContainer[_perms_pb2.Permission]
    def __init__(self, org_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_perms_pb2.Permission, str]]] = ...) -> None: ...

class RevokePermissionToAccountOwnerPermissionGroupResponse(_message.Message):
    __slots__ = ("default_permission_group",)
    DEFAULT_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_permission_group: PermissionGroup
    def __init__(self, default_permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class AddPermissionToOrgDefaultGroupRequest(_message.Message):
    __slots__ = ("org_id", "permission")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permission: _perms_pb2.Permission
    def __init__(self, org_id: _Optional[str] = ..., permission: _Optional[_Union[_perms_pb2.Permission, str]] = ...) -> None: ...

class AddPermissionToOrgDefaultGroupResponse(_message.Message):
    __slots__ = ("default_permission_group",)
    DEFAULT_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_permission_group: PermissionGroup
    def __init__(self, default_permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class RemovePermissionFromOrgDefaultGroupRequest(_message.Message):
    __slots__ = ("org_id", "permission")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    permission: _perms_pb2.Permission
    def __init__(self, org_id: _Optional[str] = ..., permission: _Optional[_Union[_perms_pb2.Permission, str]] = ...) -> None: ...

class RemovePermissionFromOrgDefaultGroupResponse(_message.Message):
    __slots__ = ("default_permission_group",)
    DEFAULT_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_permission_group: PermissionGroup
    def __init__(self, default_permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class GetOrgDefaultSuperUserGroupRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetOrgDefaultSuperUserGroupResponse(_message.Message):
    __slots__ = ("default_permission_group",)
    DEFAULT_PERMISSION_GROUP_FIELD_NUMBER: _ClassVar[int]
    default_permission_group: PermissionGroup
    def __init__(self, default_permission_group: _Optional[_Union[PermissionGroup, _Mapping]] = ...) -> None: ...

class GetOrganizationPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetOrganizationPreferencesResponse(_message.Message):
    __slots__ = ("organization_preferences",)
    ORGANIZATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    organization_preferences: OrganizationPreferences
    def __init__(self, organization_preferences: _Optional[_Union[OrganizationPreferences, _Mapping]] = ...) -> None: ...

class UpdateOrganizationPreferencesRequest(_message.Message):
    __slots__ = ("organization_preferences", "field_mask")
    ORGANIZATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_preferences: OrganizationPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization_preferences: _Optional[_Union[OrganizationPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateOrganizationPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OrganizationPreferences(_message.Message):
    __slots__ = ("allowed_countries", "default_country", "time_zone", "display_language")
    ALLOWED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    allowed_countries: _containers.RepeatedScalarFieldContainer[_country_pb2.Country]
    default_country: _country_pb2.Country
    time_zone: _org_pb2.TimeZone
    display_language: _org_pb2.DisplayLanguage
    def __init__(self, allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ..., default_country: _Optional[_Union[_country_pb2.Country, str]] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., display_language: _Optional[_Union[_org_pb2.DisplayLanguage, str]] = ...) -> None: ...

class GetAgentPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAgentPreferencesResponse(_message.Message):
    __slots__ = ("agent_preferences",)
    AGENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    agent_preferences: AgentPreferences
    def __init__(self, agent_preferences: _Optional[_Union[AgentPreferences, _Mapping]] = ...) -> None: ...

class UpdateAgentPreferencesRequest(_message.Message):
    __slots__ = ("agent_preferences", "field_mask")
    AGENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    agent_preferences: AgentPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, agent_preferences: _Optional[_Union[AgentPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAgentPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentPreferences(_message.Message):
    __slots__ = ("default_agent_dial_in", "pbx_extension_length", "default_softphone_volume_in", "default_softphone_volume_out", "config_dial_in_numbers", "client_dial_in_numbers", "manual_dial_caller_id_privacy", "use_manual_dial_caller_id_privacy", "message_notifications_disabled")
    DEFAULT_AGENT_DIAL_IN_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_IN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_OUT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_DIAL_IN_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DIAL_IN_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_CALLER_ID_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    USE_MANUAL_DIAL_CALLER_ID_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_NOTIFICATIONS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    default_agent_dial_in: str
    pbx_extension_length: int
    default_softphone_volume_in: int
    default_softphone_volume_out: int
    config_dial_in_numbers: _containers.RepeatedScalarFieldContainer[str]
    client_dial_in_numbers: _containers.RepeatedScalarFieldContainer[str]
    manual_dial_caller_id_privacy: bool
    use_manual_dial_caller_id_privacy: bool
    message_notifications_disabled: bool
    def __init__(self, default_agent_dial_in: _Optional[str] = ..., pbx_extension_length: _Optional[int] = ..., default_softphone_volume_in: _Optional[int] = ..., default_softphone_volume_out: _Optional[int] = ..., config_dial_in_numbers: _Optional[_Iterable[str]] = ..., client_dial_in_numbers: _Optional[_Iterable[str]] = ..., manual_dial_caller_id_privacy: bool = ..., use_manual_dial_caller_id_privacy: bool = ..., message_notifications_disabled: bool = ...) -> None: ...

class GetContactPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetContactPreferencesResponse(_message.Message):
    __slots__ = ("contact_preferences",)
    CONTACT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    contact_preferences: ContactPreferences
    def __init__(self, contact_preferences: _Optional[_Union[ContactPreferences, _Mapping]] = ...) -> None: ...

class UpdateContactPreferencesRequest(_message.Message):
    __slots__ = ("contact_preferences", "field_mask")
    CONTACT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    contact_preferences: ContactPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, contact_preferences: _Optional[_Union[ContactPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateContactPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactPreferences(_message.Message):
    __slots__ = ("default_contact_import_format", "use_contact_import_format", "default_contact_area_code", "use_contact_area_code", "discard_record_default_absent_numbers_handling", "default_contacts_import_randomization", "default_email_column", "default_duplicate_handling")
    DEFAULT_CONTACT_IMPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    USE_CONTACT_IMPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTACT_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    USE_CONTACT_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    DISCARD_RECORD_DEFAULT_ABSENT_NUMBERS_HANDLING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTACTS_IMPORT_RANDOMIZATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EMAIL_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DUPLICATE_HANDLING_FIELD_NUMBER: _ClassVar[int]
    default_contact_import_format: ImportFormat
    use_contact_import_format: bool
    default_contact_area_code: ContactAreaCode
    use_contact_area_code: bool
    discard_record_default_absent_numbers_handling: bool
    default_contacts_import_randomization: bool
    default_email_column: str
    default_duplicate_handling: _org_pb2.DefaultDuplicateHandling
    def __init__(self, default_contact_import_format: _Optional[_Union[ImportFormat, _Mapping]] = ..., use_contact_import_format: bool = ..., default_contact_area_code: _Optional[_Union[ContactAreaCode, _Mapping]] = ..., use_contact_area_code: bool = ..., discard_record_default_absent_numbers_handling: bool = ..., default_contacts_import_randomization: bool = ..., default_email_column: _Optional[str] = ..., default_duplicate_handling: _Optional[_Union[_org_pb2.DefaultDuplicateHandling, str]] = ...) -> None: ...

class ImportFormat(_message.Message):
    __slots__ = ("custom", "standard")
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    custom: CustomImportFormat
    standard: _org_pb2.StandardImportFormat
    def __init__(self, custom: _Optional[_Union[CustomImportFormat, _Mapping]] = ..., standard: _Optional[_Union[_org_pb2.StandardImportFormat, str]] = ...) -> None: ...

class CustomImportFormat(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: int
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class ContactAreaCode(_message.Message):
    __slots__ = ("custom", "contact_field")
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_FIELD_NUMBER: _ClassVar[int]
    custom: int
    contact_field: ContactFieldDesc
    def __init__(self, custom: _Optional[int] = ..., contact_field: _Optional[_Union[ContactFieldDesc, _Mapping]] = ...) -> None: ...

class ContactFieldDesc(_message.Message):
    __slots__ = ("id", "field_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    field_name: str
    def __init__(self, id: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class GetAuthenticationPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAuthenticationPreferencesResponse(_message.Message):
    __slots__ = ("authentication_preferences",)
    AUTHENTICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    authentication_preferences: AuthenticationPreferences
    def __init__(self, authentication_preferences: _Optional[_Union[AuthenticationPreferences, _Mapping]] = ...) -> None: ...

class UpdateAuthenticationPreferencesRequest(_message.Message):
    __slots__ = ("authentication_preferences", "field_mask")
    AUTHENTICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    authentication_preferences: AuthenticationPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, authentication_preferences: _Optional[_Union[AuthenticationPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAuthenticationPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AuthenticationPreferences(_message.Message):
    __slots__ = ("authorization_via_ip", "allowed_ips", "agent_api_key", "user_authorization_via_ip")
    AUTHORIZATION_VIA_IP_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_API_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHORIZATION_VIA_IP_FIELD_NUMBER: _ClassVar[int]
    authorization_via_ip: bool
    allowed_ips: _containers.RepeatedScalarFieldContainer[str]
    agent_api_key: str
    user_authorization_via_ip: bool
    def __init__(self, authorization_via_ip: bool = ..., allowed_ips: _Optional[_Iterable[str]] = ..., agent_api_key: _Optional[str] = ..., user_authorization_via_ip: bool = ...) -> None: ...

class GetWebhookPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetWebhookPreferencesResponse(_message.Message):
    __slots__ = ("webhook_preferences",)
    WEBHOOK_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    webhook_preferences: WebhookPreferences
    def __init__(self, webhook_preferences: _Optional[_Union[WebhookPreferences, _Mapping]] = ...) -> None: ...

class UpdateWebhookPreferencesRequest(_message.Message):
    __slots__ = ("webhook_preferences", "field_mask")
    WEBHOOK_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    webhook_preferences: WebhookPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, webhook_preferences: _Optional[_Union[WebhookPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateWebhookPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WebhookPreferences(_message.Message):
    __slots__ = ("push_urls_enabled", "call_result_push_url", "agent_response_push_url")
    PUSH_URLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_RESULT_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    push_urls_enabled: bool
    call_result_push_url: str
    agent_response_push_url: str
    def __init__(self, push_urls_enabled: bool = ..., call_result_push_url: _Optional[str] = ..., agent_response_push_url: _Optional[str] = ...) -> None: ...

class GetDashboardGeneralPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDashboardGeneralPreferencesResponse(_message.Message):
    __slots__ = ("dashboard_preferences",)
    DASHBOARD_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_preferences: DashboardPreferences
    def __init__(self, dashboard_preferences: _Optional[_Union[DashboardPreferences, _Mapping]] = ...) -> None: ...

class UpdateDashboardGeneralPreferencesRequest(_message.Message):
    __slots__ = ("dashboard_preferences", "field_mask")
    DASHBOARD_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    dashboard_preferences: DashboardPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, dashboard_preferences: _Optional[_Union[DashboardPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDashboardGeneralPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashboardPreferences(_message.Message):
    __slots__ = ("default_info_view", "default_table_inclusion", "default_info_grouping", "default_small_icon", "default_descending_sort", "table_template_sid", "default_call_types", "default_info_sort_by_value", "default_barge_in_filtering")
    DEFAULT_INFO_VIEW_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TABLE_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_GROUPING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SMALL_ICON_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DESCENDING_SORT_FIELD_NUMBER: _ClassVar[int]
    TABLE_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_SORT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BARGE_IN_FILTERING_FIELD_NUMBER: _ClassVar[int]
    default_info_view: bool
    default_table_inclusion: bool
    default_info_grouping: bool
    default_small_icon: bool
    default_descending_sort: bool
    table_template_sid: int
    default_call_types: IncludedCallTypes
    default_info_sort_by_value: _org_pb2.AgentInfoSortBy
    default_barge_in_filtering: BargeInFiltering
    def __init__(self, default_info_view: bool = ..., default_table_inclusion: bool = ..., default_info_grouping: bool = ..., default_small_icon: bool = ..., default_descending_sort: bool = ..., table_template_sid: _Optional[int] = ..., default_call_types: _Optional[_Union[IncludedCallTypes, _Mapping]] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.AgentInfoSortBy, str]] = ..., default_barge_in_filtering: _Optional[_Union[BargeInFiltering, _Mapping]] = ...) -> None: ...

class IncludedCallTypes(_message.Message):
    __slots__ = ("outbound", "inbound", "manual_dial", "preview_dial")
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_FIELD_NUMBER: _ClassVar[int]
    outbound: bool
    inbound: bool
    manual_dial: bool
    preview_dial: bool
    def __init__(self, outbound: bool = ..., inbound: bool = ..., manual_dial: bool = ..., preview_dial: bool = ...) -> None: ...

class BargeInFiltering(_message.Message):
    __slots__ = ("hunt_group", "agent_status")
    class HuntGroup(_message.Message):
        __slots__ = ("any", "hunt_group_sid")
        ANY_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        any: bool
        hunt_group_sid: int
        def __init__(self, any: bool = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...
    class AgentStatus(_message.Message):
        __slots__ = ("any", "waiting", "on_call", "wrap_up", "paused", "transfer", "preview", "manual", "pbx", "intercom")
        ANY_FIELD_NUMBER: _ClassVar[int]
        WAITING_FIELD_NUMBER: _ClassVar[int]
        ON_CALL_FIELD_NUMBER: _ClassVar[int]
        WRAP_UP_FIELD_NUMBER: _ClassVar[int]
        PAUSED_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PBX_FIELD_NUMBER: _ClassVar[int]
        INTERCOM_FIELD_NUMBER: _ClassVar[int]
        any: bool
        waiting: bool
        on_call: bool
        wrap_up: bool
        paused: bool
        transfer: bool
        preview: bool
        manual: bool
        pbx: bool
        intercom: bool
        def __init__(self, any: bool = ..., waiting: bool = ..., on_call: bool = ..., wrap_up: bool = ..., paused: bool = ..., transfer: bool = ..., preview: bool = ..., manual: bool = ..., pbx: bool = ..., intercom: bool = ...) -> None: ...
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    hunt_group: BargeInFiltering.HuntGroup
    agent_status: BargeInFiltering.AgentStatus
    def __init__(self, hunt_group: _Optional[_Union[BargeInFiltering.HuntGroup, _Mapping]] = ..., agent_status: _Optional[_Union[BargeInFiltering.AgentStatus, _Mapping]] = ...) -> None: ...

class GetDashboardQueuePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDashboardQueuePreferencesResponse(_message.Message):
    __slots__ = ("dashboard_queue_preferences",)
    DASHBOARD_QUEUE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_queue_preferences: DashboardQueuePreferences
    def __init__(self, dashboard_queue_preferences: _Optional[_Union[DashboardQueuePreferences, _Mapping]] = ...) -> None: ...

class UpdateDashboardQueuePreferencesRequest(_message.Message):
    __slots__ = ("dashboard_queue_preferences", "field_mask")
    DASHBOARD_QUEUE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    dashboard_queue_preferences: DashboardQueuePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, dashboard_queue_preferences: _Optional[_Union[DashboardQueuePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDashboardQueuePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashboardQueuePreferences(_message.Message):
    __slots__ = ("default_info_view", "default_info_grouping", "default_small_icon", "default_descending_sort", "default_agent_skills_filter", "default_info_table_template", "default_info_sort_by_value")
    DEFAULT_INFO_VIEW_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_GROUPING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SMALL_ICON_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DESCENDING_SORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_SKILLS_FILTER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_TABLE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_SORT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    default_info_view: bool
    default_info_grouping: bool
    default_small_icon: bool
    default_descending_sort: bool
    default_agent_skills_filter: int
    default_info_table_template: int
    default_info_sort_by_value: _org_pb2.QueueInfoSortBy
    def __init__(self, default_info_view: bool = ..., default_info_grouping: bool = ..., default_small_icon: bool = ..., default_descending_sort: bool = ..., default_agent_skills_filter: _Optional[int] = ..., default_info_table_template: _Optional[int] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.QueueInfoSortBy, str]] = ...) -> None: ...

class GetPhonePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetPhonePreferencesResponse(_message.Message):
    __slots__ = ("phone_preferences",)
    PHONE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    phone_preferences: PhonePreferences
    def __init__(self, phone_preferences: _Optional[_Union[PhonePreferences, _Mapping]] = ...) -> None: ...

class UpdatePhonePreferencesRequest(_message.Message):
    __slots__ = ("phone_preferences", "field_mask")
    PHONE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    phone_preferences: PhonePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, phone_preferences: _Optional[_Union[PhonePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePhonePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhonePreferences(_message.Message):
    __slots__ = ("agent_preview_dialing", "default_ring_length_threshold", "display_ring_length_threshold", "show_caller_id", "default_use_caller_id", "override_linkback_recording", "caller_id_cfd_sid", "default_dial_order", "answering_machine_detection", "linkback_recording")
    AGENT_PREVIEW_DIALING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RING_LENGTH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_RING_LENGTH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_LINKBACK_RECORDING_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_CFD_SID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DIAL_ORDER_FIELD_NUMBER: _ClassVar[int]
    ANSWERING_MACHINE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_RECORDING_FIELD_NUMBER: _ClassVar[int]
    agent_preview_dialing: bool
    default_ring_length_threshold: int
    display_ring_length_threshold: bool
    show_caller_id: bool
    default_use_caller_id: bool
    override_linkback_recording: bool
    caller_id_cfd_sid: int
    default_dial_order: DialOrder
    answering_machine_detection: _org_preferences_pb2.AnsweringMachineDetection
    linkback_recording: bool
    def __init__(self, agent_preview_dialing: bool = ..., default_ring_length_threshold: _Optional[int] = ..., display_ring_length_threshold: bool = ..., show_caller_id: bool = ..., default_use_caller_id: bool = ..., override_linkback_recording: bool = ..., caller_id_cfd_sid: _Optional[int] = ..., default_dial_order: _Optional[_Union[DialOrder, _Mapping]] = ..., answering_machine_detection: _Optional[_Union[_org_preferences_pb2.AnsweringMachineDetection, str]] = ..., linkback_recording: bool = ...) -> None: ...

class DialOrder(_message.Message):
    __slots__ = ("standard_order", "custom_order")
    STANDARD_ORDER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ORDER_FIELD_NUMBER: _ClassVar[int]
    standard_order: _lms_pb2.DialOrderType
    custom_order: CustomDialOrder
    def __init__(self, standard_order: _Optional[_Union[_lms_pb2.DialOrderType, str]] = ..., custom_order: _Optional[_Union[CustomDialOrder, _Mapping]] = ...) -> None: ...

class CustomDialOrder(_message.Message):
    __slots__ = ("dial_order_fields",)
    DIAL_ORDER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    dial_order_fields: _containers.RepeatedCompositeFieldContainer[DialOrderField]
    def __init__(self, dial_order_fields: _Optional[_Iterable[_Union[DialOrderField, _Mapping]]] = ...) -> None: ...

class DialOrderField(_message.Message):
    __slots__ = ("cfd_sid", "field_name")
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class GetCompliancePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetCompliancePreferencesResponse(_message.Message):
    __slots__ = ("compliance_preferences",)
    COMPLIANCE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    compliance_preferences: CompliancePreferences
    def __init__(self, compliance_preferences: _Optional[_Union[CompliancePreferences, _Mapping]] = ...) -> None: ...

class UpdateCompliancePreferencesRequest(_message.Message):
    __slots__ = ("compliance_preferences", "field_mask")
    COMPLIANCE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    compliance_preferences: CompliancePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, compliance_preferences: _Optional[_Union[CompliancePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCompliancePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CompliancePreferences(_message.Message):
    __slots__ = ("display_after_hours_calls", "after_hours_calls", "display_natural_compliance", "use_natural_compliance", "default_compliance_rule_set", "display_cell_phone_scrub", "cell_phone_scrub", "display_schedule_rules", "use_schedule_rules", "default_schedule_rule", "do_zip_code_scrub", "zip_code_scrub", "default_email_compliance_list", "default_sms_compliance_list")
    DISPLAY_AFTER_HOURS_CALLS_FIELD_NUMBER: _ClassVar[int]
    AFTER_HOURS_CALLS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NATURAL_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    USE_NATURAL_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COMPLIANCE_RULE_SET_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CELL_PHONE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    CELL_PHONE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SCHEDULE_RULES_FIELD_NUMBER: _ClassVar[int]
    USE_SCHEDULE_RULES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEDULE_RULE_FIELD_NUMBER: _ClassVar[int]
    DO_ZIP_CODE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EMAIL_COMPLIANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SMS_COMPLIANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    display_after_hours_calls: bool
    after_hours_calls: bool
    display_natural_compliance: bool
    use_natural_compliance: bool
    default_compliance_rule_set: str
    display_cell_phone_scrub: bool
    cell_phone_scrub: bool
    display_schedule_rules: bool
    use_schedule_rules: bool
    default_schedule_rule: ScheduleRuleField
    do_zip_code_scrub: bool
    zip_code_scrub: ZipCodeField
    default_email_compliance_list: str
    default_sms_compliance_list: str
    def __init__(self, display_after_hours_calls: bool = ..., after_hours_calls: bool = ..., display_natural_compliance: bool = ..., use_natural_compliance: bool = ..., default_compliance_rule_set: _Optional[str] = ..., display_cell_phone_scrub: bool = ..., cell_phone_scrub: bool = ..., display_schedule_rules: bool = ..., use_schedule_rules: bool = ..., default_schedule_rule: _Optional[_Union[ScheduleRuleField, _Mapping]] = ..., do_zip_code_scrub: bool = ..., zip_code_scrub: _Optional[_Union[ZipCodeField, _Mapping]] = ..., default_email_compliance_list: _Optional[str] = ..., default_sms_compliance_list: _Optional[str] = ...) -> None: ...

class ScheduleRuleField(_message.Message):
    __slots__ = ("rule_id", "name")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    rule_id: int
    name: str
    def __init__(self, rule_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ZipCodeField(_message.Message):
    __slots__ = ("cfd_sid", "field_name")
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class GetBroadcastPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBroadcastPreferencesResponse(_message.Message):
    __slots__ = ("broadcast_preferences",)
    BROADCAST_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    broadcast_preferences: BroadcastPreferences
    def __init__(self, broadcast_preferences: _Optional[_Union[BroadcastPreferences, _Mapping]] = ...) -> None: ...

class UpdateBroadcastPreferencesRequest(_message.Message):
    __slots__ = ("broadcast_preferences", "field_mask")
    BROADCAST_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    broadcast_preferences: BroadcastPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, broadcast_preferences: _Optional[_Union[BroadcastPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBroadcastPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BroadcastPreferences(_message.Message):
    __slots__ = ("dial_list_penetration_strategy", "display_list_penetration_strategy", "display_follow_the_sun", "follow_the_sun", "sequence_terminator_override", "broadcast_template_ordering", "email_from_addresses", "start_time_enabled", "default_start_time", "stop_time_enabled", "default_stop_time")
    DIAL_LIST_PENETRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LIST_PENETRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FOLLOW_THE_SUN_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_THE_SUN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_TERMINATOR_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_TEMPLATE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    dial_list_penetration_strategy: bool
    display_list_penetration_strategy: bool
    display_follow_the_sun: bool
    follow_the_sun: bool
    sequence_terminator_override: bool
    broadcast_template_ordering: _org_preferences_pb2.BroadcastTemplateOrdering
    email_from_addresses: _containers.RepeatedScalarFieldContainer[str]
    start_time_enabled: bool
    default_start_time: BroadcastTime
    stop_time_enabled: bool
    default_stop_time: BroadcastTime
    def __init__(self, dial_list_penetration_strategy: bool = ..., display_list_penetration_strategy: bool = ..., display_follow_the_sun: bool = ..., follow_the_sun: bool = ..., sequence_terminator_override: bool = ..., broadcast_template_ordering: _Optional[_Union[_org_preferences_pb2.BroadcastTemplateOrdering, str]] = ..., email_from_addresses: _Optional[_Iterable[str]] = ..., start_time_enabled: bool = ..., default_start_time: _Optional[_Union[BroadcastTime, _Mapping]] = ..., stop_time_enabled: bool = ..., default_stop_time: _Optional[_Union[BroadcastTime, _Mapping]] = ...) -> None: ...

class BroadcastTime(_message.Message):
    __slots__ = ("hours", "minutes", "timezone")
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    timezone: _org_pb2.TimeZone
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class GetSchedulePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSchedulePreferencesResponse(_message.Message):
    __slots__ = ("schedule_preferences",)
    SCHEDULE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    schedule_preferences: SchedulePreferences
    def __init__(self, schedule_preferences: _Optional[_Union[SchedulePreferences, _Mapping]] = ...) -> None: ...

class UpdateSchedulePreferencesRequest(_message.Message):
    __slots__ = ("schedule_preferences", "field_mask")
    SCHEDULE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    schedule_preferences: SchedulePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, schedule_preferences: _Optional[_Union[SchedulePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSchedulePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SchedulePreferences(_message.Message):
    __slots__ = ("display_schedule_by_time_zone", "use_schedule_by_time_zone", "schedule_by_time_zone_scope", "display_schedule_as_paused", "schedule_as_paused", "default_completion_threshold", "display_campaign_linking", "use_campaign_linking", "campaign_links", "default_campaign_link_id")
    class CampaignLinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISPLAY_SCHEDULE_BY_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    USE_SCHEDULE_BY_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_BY_TIME_ZONE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SCHEDULE_AS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_AS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COMPLETION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CAMPAIGN_LINKING_FIELD_NUMBER: _ClassVar[int]
    USE_CAMPAIGN_LINKING_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_LINKS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CAMPAIGN_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    display_schedule_by_time_zone: bool
    use_schedule_by_time_zone: bool
    schedule_by_time_zone_scope: _org_preferences_pb2.ScheduleByTimeZoneScope
    display_schedule_as_paused: bool
    schedule_as_paused: bool
    default_completion_threshold: int
    display_campaign_linking: bool
    use_campaign_linking: bool
    campaign_links: _containers.ScalarMap[str, str]
    default_campaign_link_id: str
    def __init__(self, display_schedule_by_time_zone: bool = ..., use_schedule_by_time_zone: bool = ..., schedule_by_time_zone_scope: _Optional[_Union[_org_preferences_pb2.ScheduleByTimeZoneScope, str]] = ..., display_schedule_as_paused: bool = ..., schedule_as_paused: bool = ..., default_completion_threshold: _Optional[int] = ..., display_campaign_linking: bool = ..., use_campaign_linking: bool = ..., campaign_links: _Optional[_Mapping[str, str]] = ..., default_campaign_link_id: _Optional[str] = ...) -> None: ...

class GetEmailSmsPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEmailSmsPreferencesResponse(_message.Message):
    __slots__ = ("email_sms_preferences",)
    EMAIL_SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    email_sms_preferences: EmailSmsPreferences
    def __init__(self, email_sms_preferences: _Optional[_Union[EmailSmsPreferences, _Mapping]] = ...) -> None: ...

class UpdateEmailSmsPreferencesRequest(_message.Message):
    __slots__ = ("email_sms_preferences", "field_mask")
    EMAIL_SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    email_sms_preferences: EmailSmsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, email_sms_preferences: _Optional[_Union[EmailSmsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEmailSmsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmailSmsPreferences(_message.Message):
    __slots__ = ("use_custom_links", "client_acknowledgement", "email_from_addresses")
    USE_CUSTOM_LINKS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    use_custom_links: bool
    client_acknowledgement: bool
    email_from_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, use_custom_links: bool = ..., client_acknowledgement: bool = ..., email_from_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBusinessPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBusinessPreferencesResponse(_message.Message):
    __slots__ = ("business_preferences",)
    BUSINESS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    business_preferences: BusinessPreferences
    def __init__(self, business_preferences: _Optional[_Union[BusinessPreferences, _Mapping]] = ...) -> None: ...

class UpdateBusinessPreferencesRequest(_message.Message):
    __slots__ = ("business_preferences", "field_mask")
    BUSINESS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    business_preferences: BusinessPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_preferences: _Optional[_Union[BusinessPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBusinessPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusinessPreferences(_message.Message):
    __slots__ = ("weeks_of_data", "time_zone", "multi_client_access", "custom_visualizations", "time_filter")
    WEEKS_OF_DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLIENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VISUALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    weeks_of_data: int
    time_zone: _ana_pb2.AnaTimeZone
    multi_client_access: bool
    custom_visualizations: bool
    time_filter: str
    def __init__(self, weeks_of_data: _Optional[int] = ..., time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ..., multi_client_access: bool = ..., custom_visualizations: bool = ..., time_filter: _Optional[str] = ...) -> None: ...

class GetVoiceAnalyticsPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetVoiceAnalyticsPreferencesResponse(_message.Message):
    __slots__ = ("voice_analytics_preferences",)
    VOICE_ANALYTICS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    voice_analytics_preferences: VoiceAnalyticsPreferences
    def __init__(self, voice_analytics_preferences: _Optional[_Union[VoiceAnalyticsPreferences, _Mapping]] = ...) -> None: ...

class UpdateVoiceAnalyticsPreferencesRequest(_message.Message):
    __slots__ = ("voice_analytics_preferences", "field_mask")
    VOICE_ANALYTICS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    voice_analytics_preferences: VoiceAnalyticsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, voice_analytics_preferences: _Optional[_Union[VoiceAnalyticsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateVoiceAnalyticsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VoiceAnalyticsPreferences(_message.Message):
    __slots__ = ("enabled", "redact", "notify", "billing_notify", "number_format", "redact_all_digits", "silence_threshold", "talk_over_threshold")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REDACT_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    BILLING_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    REDACT_ALL_DIGITS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TALK_OVER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    redact: _containers.RepeatedCompositeFieldContainer[VoiceAnalytics.Redact]
    notify: VoiceAnalytics.Notify
    billing_notify: VoiceAnalytics.Notify
    number_format: str
    redact_all_digits: bool
    silence_threshold: int
    talk_over_threshold: int
    def __init__(self, enabled: bool = ..., redact: _Optional[_Iterable[_Union[VoiceAnalytics.Redact, _Mapping]]] = ..., notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., billing_notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., number_format: _Optional[str] = ..., redact_all_digits: bool = ..., silence_threshold: _Optional[int] = ..., talk_over_threshold: _Optional[int] = ...) -> None: ...

class VoiceAnalytics(_message.Message):
    __slots__ = ()
    class Redact(_message.Message):
        __slots__ = ("number",)
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        number: VoiceAnalytics.Number
        def __init__(self, number: _Optional[_Union[VoiceAnalytics.Number, _Mapping]] = ...) -> None: ...
    class Number(_message.Message):
        __slots__ = ("kind", "min_consecutive", "max_consecutive", "slop")
        class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KIND_CARDINAL_UNSPECIFIED: _ClassVar[VoiceAnalytics.Number.Kind]
            KIND_ORDINAL: _ClassVar[VoiceAnalytics.Number.Kind]
            KIND_ANY: _ClassVar[VoiceAnalytics.Number.Kind]
        KIND_CARDINAL_UNSPECIFIED: VoiceAnalytics.Number.Kind
        KIND_ORDINAL: VoiceAnalytics.Number.Kind
        KIND_ANY: VoiceAnalytics.Number.Kind
        KIND_FIELD_NUMBER: _ClassVar[int]
        MIN_CONSECUTIVE_FIELD_NUMBER: _ClassVar[int]
        MAX_CONSECUTIVE_FIELD_NUMBER: _ClassVar[int]
        SLOP_FIELD_NUMBER: _ClassVar[int]
        kind: VoiceAnalytics.Number.Kind
        min_consecutive: int
        max_consecutive: int
        slop: int
        def __init__(self, kind: _Optional[_Union[VoiceAnalytics.Number.Kind, str]] = ..., min_consecutive: _Optional[int] = ..., max_consecutive: _Optional[int] = ..., slop: _Optional[int] = ...) -> None: ...
    class Notify(_message.Message):
        __slots__ = ("cron",)
        CRON_FIELD_NUMBER: _ClassVar[int]
        cron: str
        def __init__(self, cron: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetScorecardsPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetScorecardsPreferencesResponse(_message.Message):
    __slots__ = ("scorecards_preferences",)
    SCORECARDS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    scorecards_preferences: ScorecardsPreferences
    def __init__(self, scorecards_preferences: _Optional[_Union[ScorecardsPreferences, _Mapping]] = ...) -> None: ...

class UpdateScorecardsPreferencesRequest(_message.Message):
    __slots__ = ("scorecards_preferences", "field_mask")
    SCORECARDS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    scorecards_preferences: ScorecardsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, scorecards_preferences: _Optional[_Union[ScorecardsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateScorecardsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScorecardsPreferences(_message.Message):
    __slots__ = ("call_sample_percentage", "max_user_evaluations", "evaluation_interval")
    CALL_SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_USER_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    call_sample_percentage: int
    max_user_evaluations: int
    evaluation_interval: Scorecards.EvaluationInterval
    def __init__(self, call_sample_percentage: _Optional[int] = ..., max_user_evaluations: _Optional[int] = ..., evaluation_interval: _Optional[_Union[Scorecards.EvaluationInterval, str]] = ...) -> None: ...

class Scorecards(_message.Message):
    __slots__ = ()
    class EvaluationInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_INTERVAL_DAY_UNSPECIFIED: _ClassVar[Scorecards.EvaluationInterval]
        EVALUATION_INTERVAL_WEEK: _ClassVar[Scorecards.EvaluationInterval]
        EVALUATION_INTERVAL_MONTH: _ClassVar[Scorecards.EvaluationInterval]
    EVALUATION_INTERVAL_DAY_UNSPECIFIED: Scorecards.EvaluationInterval
    EVALUATION_INTERVAL_WEEK: Scorecards.EvaluationInterval
    EVALUATION_INTERVAL_MONTH: Scorecards.EvaluationInterval
    def __init__(self) -> None: ...

class GetEndOfDayPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEndOfDayPreferencesResponse(_message.Message):
    __slots__ = ("end_of_day_preferences",)
    END_OF_DAY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    end_of_day_preferences: EndOfDayPreferences
    def __init__(self, end_of_day_preferences: _Optional[_Union[EndOfDayPreferences, _Mapping]] = ...) -> None: ...

class UpdateEndOfDayPreferencesRequest(_message.Message):
    __slots__ = ("end_of_day_preferences", "field_mask")
    END_OF_DAY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_of_day_preferences: EndOfDayPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_of_day_preferences: _Optional[_Union[EndOfDayPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEndOfDayPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndOfDayPreferences(_message.Message):
    __slots__ = ("eod_monday", "eod_tuesday", "eod_wednesday", "eod_thursday", "eod_friday", "eod_saturday", "eod_sunday")
    EOD_MONDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_TUESDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_THURSDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_FRIDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_SATURDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_SUNDAY_FIELD_NUMBER: _ClassVar[int]
    eod_monday: int
    eod_tuesday: int
    eod_wednesday: int
    eod_thursday: int
    eod_friday: int
    eod_saturday: int
    eod_sunday: int
    def __init__(self, eod_monday: _Optional[int] = ..., eod_tuesday: _Optional[int] = ..., eod_wednesday: _Optional[int] = ..., eod_thursday: _Optional[int] = ..., eod_friday: _Optional[int] = ..., eod_saturday: _Optional[int] = ..., eod_sunday: _Optional[int] = ...) -> None: ...

class GetFilterPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetFilterPreferencesResponse(_message.Message):
    __slots__ = ("filter_preferences",)
    FILTER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    filter_preferences: FilterPreferences
    def __init__(self, filter_preferences: _Optional[_Union[FilterPreferences, _Mapping]] = ...) -> None: ...

class UpdateFilterPreferencesRequest(_message.Message):
    __slots__ = ("filter_preferences", "field_mask")
    FILTER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    filter_preferences: FilterPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, filter_preferences: _Optional[_Union[FilterPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateFilterPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FilterPreferences(_message.Message):
    __slots__ = ("default_auto_report_filter", "send_empty_auto_reports", "display_broadcast_resend_filter", "default_broadcast_resend_filter", "custom_report_filters")
    DEFAULT_AUTO_REPORT_FILTER_FIELD_NUMBER: _ClassVar[int]
    SEND_EMPTY_AUTO_REPORTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BROADCAST_RESEND_FILTER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BROADCAST_RESEND_FILTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REPORT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    default_auto_report_filter: ReportFilter
    send_empty_auto_reports: bool
    display_broadcast_resend_filter: bool
    default_broadcast_resend_filter: ReportFilter
    custom_report_filters: _containers.RepeatedCompositeFieldContainer[CustomReportFilter]
    def __init__(self, default_auto_report_filter: _Optional[_Union[ReportFilter, _Mapping]] = ..., send_empty_auto_reports: bool = ..., display_broadcast_resend_filter: bool = ..., default_broadcast_resend_filter: _Optional[_Union[ReportFilter, _Mapping]] = ..., custom_report_filters: _Optional[_Iterable[_Union[CustomReportFilter, _Mapping]]] = ...) -> None: ...

class ReportFilter(_message.Message):
    __slots__ = ("standard", "custom")
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _org_preferences_pb2.StandardReportFilter
    custom: int
    def __init__(self, standard: _Optional[_Union[_org_preferences_pb2.StandardReportFilter, str]] = ..., custom: _Optional[int] = ...) -> None: ...

class CustomReportFilter(_message.Message):
    __slots__ = ("name", "description", "conjunction", "call_results_filter_list", "dtmf_expression_list", "agent_response_expression_list", "last_template_element_expression_list", "exclude_dtmf_expression_list", "hunt_group_sid_include_list", "hunt_group_sid_exclude_list", "xml_client_property_sid")
    class FilterConjunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTER_CONJUNCTION_AND_UNSPECIFIED: _ClassVar[CustomReportFilter.FilterConjunction]
        FILTER_CONJUNCTION_OR: _ClassVar[CustomReportFilter.FilterConjunction]
    FILTER_CONJUNCTION_AND_UNSPECIFIED: CustomReportFilter.FilterConjunction
    FILTER_CONJUNCTION_OR: CustomReportFilter.FilterConjunction
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONJUNCTION_FIELD_NUMBER: _ClassVar[int]
    CALL_RESULTS_FILTER_LIST_FIELD_NUMBER: _ClassVar[int]
    DTMF_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    LAST_TEMPLATE_ELEMENT_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_DTMF_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_INCLUDE_LIST_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_EXCLUDE_LIST_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    conjunction: CustomReportFilter.FilterConjunction
    call_results_filter_list: _containers.RepeatedScalarFieldContainer[int]
    dtmf_expression_list: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpr]
    agent_response_expression_list: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpr]
    last_template_element_expression_list: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpr]
    exclude_dtmf_expression_list: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpr]
    hunt_group_sid_include_list: _containers.RepeatedScalarFieldContainer[int]
    hunt_group_sid_exclude_list: _containers.RepeatedScalarFieldContainer[int]
    xml_client_property_sid: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., conjunction: _Optional[_Union[CustomReportFilter.FilterConjunction, str]] = ..., call_results_filter_list: _Optional[_Iterable[int]] = ..., dtmf_expression_list: _Optional[_Iterable[_Union[ComplexBooleanExpr, _Mapping]]] = ..., agent_response_expression_list: _Optional[_Iterable[_Union[ComplexBooleanExpr, _Mapping]]] = ..., last_template_element_expression_list: _Optional[_Iterable[_Union[ComplexBooleanExpr, _Mapping]]] = ..., exclude_dtmf_expression_list: _Optional[_Iterable[_Union[ComplexBooleanExpr, _Mapping]]] = ..., hunt_group_sid_include_list: _Optional[_Iterable[int]] = ..., hunt_group_sid_exclude_list: _Optional[_Iterable[int]] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class ComplexBooleanExpr(_message.Message):
    __slots__ = ("compare_expression_list",)
    COMPARE_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    compare_expression_list: CompareExprList
    def __init__(self, compare_expression_list: _Optional[_Union[CompareExprList, _Mapping]] = ...) -> None: ...

class CompareExprList(_message.Message):
    __slots__ = ("simple_compare_expression",)
    SIMPLE_COMPARE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    simple_compare_expression: _containers.RepeatedCompositeFieldContainer[SimpleCompareExpression]
    def __init__(self, simple_compare_expression: _Optional[_Iterable[_Union[SimpleCompareExpression, _Mapping]]] = ...) -> None: ...

class SimpleCompareExpression(_message.Message):
    __slots__ = ("operator_type", "value_key", "compare_value")
    OPERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPARE_VALUE_FIELD_NUMBER: _ClassVar[int]
    operator_type: str
    value_key: str
    compare_value: str
    def __init__(self, operator_type: _Optional[str] = ..., value_key: _Optional[str] = ..., compare_value: _Optional[str] = ...) -> None: ...

class GetRecordingPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetRecordingPreferencesResponse(_message.Message):
    __slots__ = ("recording_preferences", "call_recording_redaction")
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CALL_RECORDING_REDACTION_FIELD_NUMBER: _ClassVar[int]
    recording_preferences: RecordingPreferences
    call_recording_redaction: bool
    def __init__(self, recording_preferences: _Optional[_Union[RecordingPreferences, _Mapping]] = ..., call_recording_redaction: bool = ...) -> None: ...

class UpdateRecordingPreferencesRequest(_message.Message):
    __slots__ = ("recording_preferences", "field_mask")
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    recording_preferences: RecordingPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, recording_preferences: _Optional[_Union[RecordingPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRecordingPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordingPreferences(_message.Message):
    __slots__ = ("convention_enabled", "file_name_convention", "zip_convention_enabled", "zip_file_name_convention", "export_file_type")
    CONVENTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    ZIP_CONVENTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ZIP_FILE_NAME_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    convention_enabled: bool
    file_name_convention: RecordingsFileNamingConvention
    zip_convention_enabled: bool
    zip_file_name_convention: RecordingsZipFileNamingConvention
    export_file_type: _org_pb2.RecordingFileType
    def __init__(self, convention_enabled: bool = ..., file_name_convention: _Optional[_Union[RecordingsFileNamingConvention, _Mapping]] = ..., zip_convention_enabled: bool = ..., zip_file_name_convention: _Optional[_Union[RecordingsZipFileNamingConvention, _Mapping]] = ..., export_file_type: _Optional[_Union[_org_pb2.RecordingFileType, str]] = ...) -> None: ...

class RecordingsFileNamingConvention(_message.Message):
    __slots__ = ("inbound", "manual", "outbound", "preview", "xml_client_property_sid")
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    inbound: FileNamingConvention
    manual: FileNamingConvention
    outbound: FileNamingConvention
    preview: FileNamingConvention
    xml_client_property_sid: int
    def __init__(self, inbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., manual: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., outbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., preview: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class RecordingsZipFileNamingConvention(_message.Message):
    __slots__ = ("inbound", "manual", "outbound", "combined", "xml_client_property_sid")
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    COMBINED_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    inbound: FileNamingConvention
    manual: FileNamingConvention
    outbound: FileNamingConvention
    combined: FileNamingConvention
    xml_client_property_sid: int
    def __init__(self, inbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., manual: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., outbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., combined: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class FileNamingConvention(_message.Message):
    __slots__ = ("segments",)
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[FileNameSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[FileNameSegment, _Mapping]]] = ...) -> None: ...

class FileNameSegment(_message.Message):
    __slots__ = ("segment_type", "format_pattern", "time_zone_id")
    SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    segment_type: str
    format_pattern: str
    time_zone_id: str
    def __init__(self, segment_type: _Optional[str] = ..., format_pattern: _Optional[str] = ..., time_zone_id: _Optional[str] = ...) -> None: ...

class GetAdminClientPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAdminClientPreferencesResponse(_message.Message):
    __slots__ = ("admin_client_preferences",)
    ADMIN_CLIENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    admin_client_preferences: AdminClientPreferences
    def __init__(self, admin_client_preferences: _Optional[_Union[AdminClientPreferences, _Mapping]] = ...) -> None: ...

class UpdateAdminClientPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "admin_client_preferences", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CLIENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    admin_client_preferences: AdminClientPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., admin_client_preferences: _Optional[_Union[AdminClientPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAdminClientPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminClientPreferences(_message.Message):
    __slots__ = ("use_reserved_carrier", "reserved_carriers", "email_key", "email_id", "email_name", "whitelist_ips", "whitelist_domains", "callbacks_service_id", "agent_screen_recording", "allowed_countries")
    USE_RESERVED_CARRIER_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CARRIERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_KEY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_NAME_FIELD_NUMBER: _ClassVar[int]
    WHITELIST_IPS_FIELD_NUMBER: _ClassVar[int]
    WHITELIST_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    CALLBACKS_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SCREEN_RECORDING_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    use_reserved_carrier: bool
    reserved_carriers: _containers.RepeatedScalarFieldContainer[str]
    email_key: str
    email_id: str
    email_name: str
    whitelist_ips: _containers.RepeatedScalarFieldContainer[str]
    whitelist_domains: _containers.RepeatedScalarFieldContainer[str]
    callbacks_service_id: str
    agent_screen_recording: bool
    allowed_countries: _containers.RepeatedScalarFieldContainer[_country_pb2.Country]
    def __init__(self, use_reserved_carrier: bool = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., email_key: _Optional[str] = ..., email_id: _Optional[str] = ..., email_name: _Optional[str] = ..., whitelist_ips: _Optional[_Iterable[str]] = ..., whitelist_domains: _Optional[_Iterable[str]] = ..., callbacks_service_id: _Optional[str] = ..., agent_screen_recording: bool = ..., allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ...) -> None: ...

class AcceptLinkbackRecordingTermsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptLinkbackRecordingTermsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LinkbackUpdateBroadcastTemplatesRequest(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class LinkbackUpdateBroadcastTemplatesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordEmailUnsubscribeAcknowledgementRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordEmailUnsubscribeAcknowledgementResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearEmailUnsubscribeAcknowledgementRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearEmailUnsubscribeAcknowledgementResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomReportFilterPreferences(_message.Message):
    __slots__ = ("name", "xml_client_property_sid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    xml_client_property_sid: int
    def __init__(self, name: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class GetBackofficeThemePreferenceRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetBackofficeThemePreferenceResponse(_message.Message):
    __slots__ = ("backoffice_theme",)
    BACKOFFICE_THEME_FIELD_NUMBER: _ClassVar[int]
    backoffice_theme: _org_pb2.ClientSkin
    def __init__(self, backoffice_theme: _Optional[_Union[_org_pb2.ClientSkin, str]] = ...) -> None: ...

class EditBackofficeThemePreferenceRequest(_message.Message):
    __slots__ = ("org_id", "backoffice_theme")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    BACKOFFICE_THEME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    backoffice_theme: _org_pb2.ClientSkin
    def __init__(self, org_id: _Optional[str] = ..., backoffice_theme: _Optional[_Union[_org_pb2.ClientSkin, str]] = ...) -> None: ...

class EditBackofficeThemePreferenceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WebLinkTemplate(_message.Message):
    __slots__ = ("web_link_template_id", "display_name", "description", "is_js_link", "base_url", "parameters")
    WEB_LINK_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_JS_LINK_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    web_link_template_id: str
    display_name: str
    description: str
    is_js_link: bool
    base_url: _containers.RepeatedCompositeFieldContainer[WebLinkBaseOption]
    parameters: _containers.RepeatedCompositeFieldContainer[WebLinkParameter]
    def __init__(self, web_link_template_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., is_js_link: bool = ..., base_url: _Optional[_Iterable[_Union[WebLinkBaseOption, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[WebLinkParameter, _Mapping]]] = ...) -> None: ...

class WebLinkParameter(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _containers.RepeatedCompositeFieldContainer[WebLinkBaseOption]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Iterable[_Union[WebLinkBaseOption, _Mapping]]] = ...) -> None: ...

class WebLinkBaseOption(_message.Message):
    __slots__ = ("static_text", "tts_field", "agent_field", "data_key_field", "data_collect", "data_dip", "ivr_data", "phone_field", "sip_header_data", "postal_field")
    class StaticText(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class TtsField(_message.Message):
        __slots__ = ("contact_field_description_sid", "field_name", "display_format_string")
        CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
        contact_field_description_sid: int
        field_name: str
        display_format_string: str
        def __init__(self, contact_field_description_sid: _Optional[int] = ..., field_name: _Optional[str] = ..., display_format_string: _Optional[str] = ...) -> None: ...
    class AgentField(_message.Message):
        __slots__ = ("option",)
        OPTION_FIELD_NUMBER: _ClassVar[int]
        option: _org_pb2.AgentFieldOption
        def __init__(self, option: _Optional[_Union[_org_pb2.AgentFieldOption, str]] = ...) -> None: ...
    class DataKeyField(_message.Message):
        __slots__ = ("client_properties_sid", "property_key", "property_value")
        CLIENT_PROPERTIES_SID_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_KEY_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_VALUE_FIELD_NUMBER: _ClassVar[int]
        client_properties_sid: int
        property_key: str
        property_value: str
        def __init__(self, client_properties_sid: _Optional[int] = ..., property_key: _Optional[str] = ..., property_value: _Optional[str] = ...) -> None: ...
    class DataCollect(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class DataDip(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class IvrData(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class PhoneField(_message.Message):
        __slots__ = ("option",)
        OPTION_FIELD_NUMBER: _ClassVar[int]
        option: _org_pb2.PhoneFieldOption
        def __init__(self, option: _Optional[_Union[_org_pb2.PhoneFieldOption, str]] = ...) -> None: ...
    class SipHeaderData(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class PostalField(_message.Message):
        __slots__ = ("option",)
        OPTION_FIELD_NUMBER: _ClassVar[int]
        option: _org_pb2.PostalFieldOption
        def __init__(self, option: _Optional[_Union[_org_pb2.PostalFieldOption, str]] = ...) -> None: ...
    STATIC_TEXT_FIELD_NUMBER: _ClassVar[int]
    TTS_FIELD_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_FIELD_NUMBER: _ClassVar[int]
    DATA_KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECT_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_FIELD_NUMBER: _ClassVar[int]
    IVR_DATA_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_FIELD_NUMBER: _ClassVar[int]
    SIP_HEADER_DATA_FIELD_NUMBER: _ClassVar[int]
    POSTAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    static_text: WebLinkBaseOption.StaticText
    tts_field: WebLinkBaseOption.TtsField
    agent_field: WebLinkBaseOption.AgentField
    data_key_field: WebLinkBaseOption.DataKeyField
    data_collect: WebLinkBaseOption.DataCollect
    data_dip: WebLinkBaseOption.DataDip
    ivr_data: WebLinkBaseOption.IvrData
    phone_field: WebLinkBaseOption.PhoneField
    sip_header_data: WebLinkBaseOption.SipHeaderData
    postal_field: WebLinkBaseOption.PostalField
    def __init__(self, static_text: _Optional[_Union[WebLinkBaseOption.StaticText, _Mapping]] = ..., tts_field: _Optional[_Union[WebLinkBaseOption.TtsField, _Mapping]] = ..., agent_field: _Optional[_Union[WebLinkBaseOption.AgentField, _Mapping]] = ..., data_key_field: _Optional[_Union[WebLinkBaseOption.DataKeyField, _Mapping]] = ..., data_collect: _Optional[_Union[WebLinkBaseOption.DataCollect, _Mapping]] = ..., data_dip: _Optional[_Union[WebLinkBaseOption.DataDip, _Mapping]] = ..., ivr_data: _Optional[_Union[WebLinkBaseOption.IvrData, _Mapping]] = ..., phone_field: _Optional[_Union[WebLinkBaseOption.PhoneField, _Mapping]] = ..., sip_header_data: _Optional[_Union[WebLinkBaseOption.SipHeaderData, _Mapping]] = ..., postal_field: _Optional[_Union[WebLinkBaseOption.PostalField, _Mapping]] = ...) -> None: ...

class CreateWebLinkTemplateRequest(_message.Message):
    __slots__ = ("web_link_template",)
    WEB_LINK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    web_link_template: WebLinkTemplate
    def __init__(self, web_link_template: _Optional[_Union[WebLinkTemplate, _Mapping]] = ...) -> None: ...

class CreateWebLinkTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWebLinkTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWebLinkTemplatesResponse(_message.Message):
    __slots__ = ("web_link_templates",)
    WEB_LINK_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    web_link_templates: _containers.RepeatedCompositeFieldContainer[WebLinkTemplate]
    def __init__(self, web_link_templates: _Optional[_Iterable[_Union[WebLinkTemplate, _Mapping]]] = ...) -> None: ...

class GetWebLinkTemplateRequest(_message.Message):
    __slots__ = ("web_link_template_id",)
    WEB_LINK_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    web_link_template_id: str
    def __init__(self, web_link_template_id: _Optional[str] = ...) -> None: ...

class GetWebLinkTemplateResponse(_message.Message):
    __slots__ = ("web_link_template",)
    WEB_LINK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    web_link_template: WebLinkTemplate
    def __init__(self, web_link_template: _Optional[_Union[WebLinkTemplate, _Mapping]] = ...) -> None: ...

class UpdateWebLinkTemplateRequest(_message.Message):
    __slots__ = ("web_link_template",)
    WEB_LINK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    web_link_template: WebLinkTemplate
    def __init__(self, web_link_template: _Optional[_Union[WebLinkTemplate, _Mapping]] = ...) -> None: ...

class UpdateWebLinkTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWebLinkTemplateRequest(_message.Message):
    __slots__ = ("web_link_template_id",)
    WEB_LINK_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    web_link_template_id: str
    def __init__(self, web_link_template_id: _Optional[str] = ...) -> None: ...

class DeleteWebLinkTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentTriggerTemplate(_message.Message):
    __slots__ = ("description", "logged_in", "waiting", "paused", "on_call", "transfer_call", "transfer_lost", "transfer_target_lost", "preview_call", "manual_dial_call", "wrap_up", "id")
    class LoggedIn(_message.Message):
        __slots__ = ("display_message", "eject_agent", "execute_web_link")
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class Waiting(_message.Message):
        __slots__ = ("duration", "advance_status", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class Paused(_message.Message):
        __slots__ = ("duration", "custom_pause_code_sid", "automatic_system_code", "advance_status", "display_message", "eject_agent", "execute_web_link", "pause_code")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PAUSE_CODE_SID_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_SYSTEM_CODE_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
        duration: int
        custom_pause_code_sid: int
        automatic_system_code: _org_pb2.AutomaticSystemCode
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        pause_code: PauseCode
        def __init__(self, duration: _Optional[int] = ..., custom_pause_code_sid: _Optional[int] = ..., automatic_system_code: _Optional[_Union[_org_pb2.AutomaticSystemCode, str]] = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ..., pause_code: _Optional[_Union[PauseCode, _Mapping]] = ...) -> None: ...
    class OnCall(_message.Message):
        __slots__ = ("outbound", "inbound", "manual", "preview", "duration", "advance_status", "display_message", "eject_agent", "execute_web_link")
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        outbound: bool
        inbound: bool
        manual: bool
        preview: bool
        duration: int
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, outbound: bool = ..., inbound: bool = ..., manual: bool = ..., preview: bool = ..., duration: _Optional[int] = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class TransferCall(_message.Message):
        __slots__ = ("duration", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class TransferLost(_message.Message):
        __slots__ = ("duration", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class TransferTargetLost(_message.Message):
        __slots__ = ("duration", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class PreviewCall(_message.Message):
        __slots__ = ("duration", "advance_status", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class ManualDialCall(_message.Message):
        __slots__ = ("duration", "scheduled_callback_present", "advance_status", "display_message", "eject_agent", "execute_web_link")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_CALLBACK_PRESENT_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        duration: int
        scheduled_callback_present: bool
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, duration: _Optional[int] = ..., scheduled_callback_present: bool = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class WrapUp(_message.Message):
        __slots__ = ("outbound", "inbound", "manual", "preview", "duration", "advance_status", "display_message", "eject_agent", "execute_web_link")
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ADVANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        EJECT_AGENT_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_WEB_LINK_FIELD_NUMBER: _ClassVar[int]
        outbound: bool
        inbound: bool
        manual: bool
        preview: bool
        duration: int
        advance_status: AgentTriggerTemplate.AdvanceStatus
        display_message: AgentTriggerTemplate.DisplayMessage
        eject_agent: AgentTriggerTemplate.EjectAgent
        execute_web_link: AgentTriggerTemplate.ExecuteWebLink
        def __init__(self, outbound: bool = ..., inbound: bool = ..., manual: bool = ..., preview: bool = ..., duration: _Optional[int] = ..., advance_status: _Optional[_Union[AgentTriggerTemplate.AdvanceStatus, _Mapping]] = ..., display_message: _Optional[_Union[AgentTriggerTemplate.DisplayMessage, _Mapping]] = ..., eject_agent: _Optional[_Union[AgentTriggerTemplate.EjectAgent, _Mapping]] = ..., execute_web_link: _Optional[_Union[AgentTriggerTemplate.ExecuteWebLink, _Mapping]] = ...) -> None: ...
    class AdvanceStatus(_message.Message):
        __slots__ = ("status_type",)
        STATUS_TYPE_FIELD_NUMBER: _ClassVar[int]
        status_type: _org_pb2.AdvanceStatusType
        def __init__(self, status_type: _Optional[_Union[_org_pb2.AdvanceStatusType, str]] = ...) -> None: ...
    class DisplayMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class EjectAgent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ExecuteWebLink(_message.Message):
        __slots__ = ("web_link_id",)
        WEB_LINK_ID_FIELD_NUMBER: _ClassVar[int]
        web_link_id: str
        def __init__(self, web_link_id: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    WAITING_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    ON_CALL_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CALL_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_LOST_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TARGET_LOST_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_CALL_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_CALL_FIELD_NUMBER: _ClassVar[int]
    WRAP_UP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    logged_in: AgentTriggerTemplate.LoggedIn
    waiting: AgentTriggerTemplate.Waiting
    paused: AgentTriggerTemplate.Paused
    on_call: AgentTriggerTemplate.OnCall
    transfer_call: AgentTriggerTemplate.TransferCall
    transfer_lost: AgentTriggerTemplate.TransferLost
    transfer_target_lost: AgentTriggerTemplate.TransferTargetLost
    preview_call: AgentTriggerTemplate.PreviewCall
    manual_dial_call: AgentTriggerTemplate.ManualDialCall
    wrap_up: AgentTriggerTemplate.WrapUp
    id: str
    def __init__(self, description: _Optional[str] = ..., logged_in: _Optional[_Union[AgentTriggerTemplate.LoggedIn, _Mapping]] = ..., waiting: _Optional[_Union[AgentTriggerTemplate.Waiting, _Mapping]] = ..., paused: _Optional[_Union[AgentTriggerTemplate.Paused, _Mapping]] = ..., on_call: _Optional[_Union[AgentTriggerTemplate.OnCall, _Mapping]] = ..., transfer_call: _Optional[_Union[AgentTriggerTemplate.TransferCall, _Mapping]] = ..., transfer_lost: _Optional[_Union[AgentTriggerTemplate.TransferLost, _Mapping]] = ..., transfer_target_lost: _Optional[_Union[AgentTriggerTemplate.TransferTargetLost, _Mapping]] = ..., preview_call: _Optional[_Union[AgentTriggerTemplate.PreviewCall, _Mapping]] = ..., manual_dial_call: _Optional[_Union[AgentTriggerTemplate.ManualDialCall, _Mapping]] = ..., wrap_up: _Optional[_Union[AgentTriggerTemplate.WrapUp, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class CreateAgentTriggerTemplateRequest(_message.Message):
    __slots__ = ("agent_trigger_template",)
    AGENT_TRIGGER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    agent_trigger_template: AgentTriggerTemplate
    def __init__(self, agent_trigger_template: _Optional[_Union[AgentTriggerTemplate, _Mapping]] = ...) -> None: ...

class CreateAgentTriggerTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentTriggerTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentTriggerTemplatesResponse(_message.Message):
    __slots__ = ("agent_trigger_templates",)
    AGENT_TRIGGER_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    agent_trigger_templates: _containers.RepeatedCompositeFieldContainer[AgentTriggerTemplate]
    def __init__(self, agent_trigger_templates: _Optional[_Iterable[_Union[AgentTriggerTemplate, _Mapping]]] = ...) -> None: ...

class UpdateAgentTriggerTemplateRequest(_message.Message):
    __slots__ = ("agent_trigger_template",)
    AGENT_TRIGGER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    agent_trigger_template: AgentTriggerTemplate
    def __init__(self, agent_trigger_template: _Optional[_Union[AgentTriggerTemplate, _Mapping]] = ...) -> None: ...

class UpdateAgentTriggerTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAgentTriggerTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteAgentTriggerTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentTriggerTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAgentTriggerTemplateResponse(_message.Message):
    __slots__ = ("agent_trigger_template",)
    AGENT_TRIGGER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    agent_trigger_template: AgentTriggerTemplate
    def __init__(self, agent_trigger_template: _Optional[_Union[AgentTriggerTemplate, _Mapping]] = ...) -> None: ...

class ListAgentPauseCodesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentPauseCodesResponse(_message.Message):
    __slots__ = ("pause_codes",)
    PAUSE_CODES_FIELD_NUMBER: _ClassVar[int]
    pause_codes: _containers.RepeatedCompositeFieldContainer[PauseCode]
    def __init__(self, pause_codes: _Optional[_Iterable[_Union[PauseCode, _Mapping]]] = ...) -> None: ...

class CreateAgentPauseCodeRequest(_message.Message):
    __slots__ = ("pause_code",)
    PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    pause_code: PauseCode
    def __init__(self, pause_code: _Optional[_Union[PauseCode, _Mapping]] = ...) -> None: ...

class CreateAgentPauseCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentPauseCodeRequest(_message.Message):
    __slots__ = ("pause_code",)
    PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    pause_code: PauseCode
    def __init__(self, pause_code: _Optional[_Union[PauseCode, _Mapping]] = ...) -> None: ...

class UpdateAgentPauseCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAgentPauseCodeRequest(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class DeleteAgentPauseCodeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseCode(_message.Message):
    __slots__ = ("name", "description", "codes", "xml_client_property_sid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODES_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    codes: _containers.RepeatedScalarFieldContainer[str]
    xml_client_property_sid: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., codes: _Optional[_Iterable[str]] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class ListCustomReportFiltersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCustomReportFiltersResponse(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[CustomReportFilter]
    def __init__(self, filters: _Optional[_Iterable[_Union[CustomReportFilter, _Mapping]]] = ...) -> None: ...

class GetCustomReportFilterRequest(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class GetCustomReportFilterResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: CustomReportFilter
    def __init__(self, filter: _Optional[_Union[CustomReportFilter, _Mapping]] = ...) -> None: ...

class CreateCustomReportFilterRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: CustomReportFilter
    def __init__(self, filter: _Optional[_Union[CustomReportFilter, _Mapping]] = ...) -> None: ...

class CreateCustomReportFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateCustomReportFilterRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: CustomReportFilter
    def __init__(self, filter: _Optional[_Union[CustomReportFilter, _Mapping]] = ...) -> None: ...

class UpdateCustomReportFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCustomReportFilterRequest(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class DeleteCustomReportFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentResponseGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentResponseGroupsResponse(_message.Message):
    __slots__ = ("agent_responses",)
    AGENT_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    agent_responses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_responses: _Optional[_Iterable[str]] = ...) -> None: ...

class ListLastTemplateElementsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLastTemplateElementsResponse(_message.Message):
    __slots__ = ("template_elements",)
    TEMPLATE_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    template_elements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, template_elements: _Optional[_Iterable[str]] = ...) -> None: ...

class ClientInfoDisplayTemplate(_message.Message):
    __slots__ = ("name", "description", "display_all_fields", "dialed_number_field_style", "contact_field_styles", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ALL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DIALED_NUMBER_FIELD_STYLE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_STYLES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    display_all_fields: bool
    dialed_number_field_style: DialedNumberFieldStyle
    contact_field_styles: _containers.RepeatedCompositeFieldContainer[ContactFieldStyle]
    id: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., display_all_fields: bool = ..., dialed_number_field_style: _Optional[_Union[DialedNumberFieldStyle, _Mapping]] = ..., contact_field_styles: _Optional[_Iterable[_Union[ContactFieldStyle, _Mapping]]] = ..., id: _Optional[str] = ...) -> None: ...

class DialedNumberFieldStyle(_message.Message):
    __slots__ = ("text_color", "background_color")
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    text_color: Color
    background_color: Color
    def __init__(self, text_color: _Optional[_Union[Color, _Mapping]] = ..., background_color: _Optional[_Union[Color, _Mapping]] = ...) -> None: ...

class ContactFieldStyle(_message.Message):
    __slots__ = ("contact_field_description_sid", "text_color", "background_color")
    CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    contact_field_description_sid: int
    text_color: Color
    background_color: Color
    def __init__(self, contact_field_description_sid: _Optional[int] = ..., text_color: _Optional[_Union[Color, _Mapping]] = ..., background_color: _Optional[_Union[Color, _Mapping]] = ...) -> None: ...

class Color(_message.Message):
    __slots__ = ("red", "green", "blue")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class CreateClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("client_info_display_template",)
    CLIENT_INFO_DISPLAY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    client_info_display_template: ClientInfoDisplayTemplate
    def __init__(self, client_info_display_template: _Optional[_Union[ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClientInfoDisplayTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClientInfoDisplayTemplatesResponse(_message.Message):
    __slots__ = ("client_info_display_templates",)
    CLIENT_INFO_DISPLAY_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    client_info_display_templates: _containers.RepeatedCompositeFieldContainer[ClientInfoDisplayTemplate]
    def __init__(self, client_info_display_templates: _Optional[_Iterable[_Union[ClientInfoDisplayTemplate, _Mapping]]] = ...) -> None: ...

class UpdateClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("client_info_display_template",)
    CLIENT_INFO_DISPLAY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    client_info_display_template: ClientInfoDisplayTemplate
    def __init__(self, client_info_display_template: _Optional[_Union[ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class UpdateClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("client_info_display_template",)
    CLIENT_INFO_DISPLAY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    client_info_display_template: ClientInfoDisplayTemplate
    def __init__(self, client_info_display_template: _Optional[_Union[ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("org_id", "first_name", "last_name", "email", "user_name", "password", "permission_group_ids", "hunt_group_sid", "partner_agent_id", "p3_permission_group_id", "linkback_numbers", "caller_ids", "default_app", "user_caller_id", "agent_profile_group_id", "labels", "time_zone_override")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APP_FIELD_NUMBER: _ClassVar[int]
    USER_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    first_name: str
    last_name: str
    email: str
    user_name: str
    password: str
    permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
    hunt_group_sid: int
    partner_agent_id: str
    p3_permission_group_id: str
    linkback_numbers: _containers.RepeatedScalarFieldContainer[str]
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    default_app: _org_pb2.OperatorApplications
    user_caller_id: str
    agent_profile_group_id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    time_zone_override: _org_pb2.TimeZoneWrapper
    def __init__(self, org_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., user_name: _Optional[str] = ..., password: _Optional[str] = ..., permission_group_ids: _Optional[_Iterable[str]] = ..., hunt_group_sid: _Optional[int] = ..., partner_agent_id: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., linkback_numbers: _Optional[_Iterable[str]] = ..., caller_ids: _Optional[_Iterable[str]] = ..., default_app: _Optional[_Union[_org_pb2.OperatorApplications, str]] = ..., user_caller_id: _Optional[str] = ..., agent_profile_group_id: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., time_zone_override: _Optional[_Union[_org_pb2.TimeZoneWrapper, _Mapping]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UpdateUserPasswordRequest(_message.Message):
    __slots__ = ("user_id", "password", "current_password", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    password: str
    current_password: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., password: _Optional[str] = ..., current_password: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetUserPasswordResetLinkRequest(_message.Message):
    __slots__ = ("user_id", "org_id", "ttl")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    ttl: int
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...

class ResetUserRequirePasswordResetRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ResetUserRequirePasswordResetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserPasswordResetLinkResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class UpdateUserPasswordResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateP3OwningOrgRequest(_message.Message):
    __slots__ = ("org_id", "owner_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    owner_id: str
    def __init__(self, org_id: _Optional[str] = ..., owner_id: _Optional[str] = ...) -> None: ...

class UpdateP3OwningOrgResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetP3OwningOrgRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetP3OwningOrgResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RevokeAccountOwnerPermissionFromUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RevokeAccountOwnerPermissionFromUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConvertOrgToManualRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ConvertOrgToManualResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListQueueConfigsReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListQueueConfigsRes(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[QueueConfig]
    def __init__(self, configs: _Optional[_Iterable[_Union[QueueConfig, _Mapping]]] = ...) -> None: ...

class DeleteQueueConfigReq(_message.Message):
    __slots__ = ("config_name",)
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    def __init__(self, config_name: _Optional[str] = ...) -> None: ...

class DeleteQueueConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetQueueConfigReq(_message.Message):
    __slots__ = ("name", "merge")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    merge: bool
    def __init__(self, name: _Optional[str] = ..., merge: bool = ...) -> None: ...

class GetQueueConfigRes(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: QueueConfig
    def __init__(self, config: _Optional[_Union[QueueConfig, _Mapping]] = ...) -> None: ...

class UpdateQueueConfigReq(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: QueueConfig
    def __init__(self, config: _Optional[_Union[QueueConfig, _Mapping]] = ...) -> None: ...

class UpdateQueueConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateQueueConfigReq(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: QueueConfig
    def __init__(self, config: _Optional[_Union[QueueConfig, _Mapping]] = ...) -> None: ...

class CreateQueueConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyQueueConfigReq(_message.Message):
    __slots__ = ("from_org_id", "to_org_id", "from_name", "to_name")
    FROM_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_NAME_FIELD_NUMBER: _ClassVar[int]
    from_org_id: str
    to_org_id: str
    from_name: str
    to_name: str
    def __init__(self, from_org_id: _Optional[str] = ..., to_org_id: _Optional[str] = ..., from_name: _Optional[str] = ..., to_name: _Optional[str] = ...) -> None: ...

class CopyQueueConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueueConfig(_message.Message):
    __slots__ = ("name", "config_modified", "sounds_modified", "sounds_language", "sounds_gender", "announcement_mixing", "position_announcements", "wait_time_announcements", "attention_tones", "in_queue_conditions", "key_press_events", "pbx_ring_strategy", "queue_monitoring_silence_wait_times", "callback_timeout_minutes", "number_update", "inbound_override", "intercom_connection")
    class AnnouncementMixing(_message.Message):
        __slots__ = ("inbound", "outbound", "manual", "preview", "any")
        class Config(_message.Message):
            __slots__ = ("option",)
            OPTION_FIELD_NUMBER: _ClassVar[int]
            option: _org_pb2.AnnouncementMixingOption
            def __init__(self, option: _Optional[_Union[_org_pb2.AnnouncementMixingOption, str]] = ...) -> None: ...
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        ANY_FIELD_NUMBER: _ClassVar[int]
        inbound: QueueConfig.AnnouncementMixing.Config
        outbound: QueueConfig.AnnouncementMixing.Config
        manual: QueueConfig.AnnouncementMixing.Config
        preview: QueueConfig.AnnouncementMixing.Config
        any: QueueConfig.AnnouncementMixing.Config
        def __init__(self, inbound: _Optional[_Union[QueueConfig.AnnouncementMixing.Config, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.AnnouncementMixing.Config, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.AnnouncementMixing.Config, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.AnnouncementMixing.Config, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.AnnouncementMixing.Config, _Mapping]] = ...) -> None: ...
    class PositionAnnouncements(_message.Message):
        __slots__ = ("inbound", "outbound", "manual", "preview", "any")
        class Disableable(_message.Message):
            __slots__ = ("config", "disable")
            CONFIG_FIELD_NUMBER: _ClassVar[int]
            DISABLE_FIELD_NUMBER: _ClassVar[int]
            config: QueueConfig.PositionAnnouncements.Config
            disable: QueueConfig.Disable
            def __init__(self, config: _Optional[_Union[QueueConfig.PositionAnnouncements.Config, _Mapping]] = ..., disable: _Optional[_Union[QueueConfig.Disable, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("first_seconds", "repeating_seconds", "threshold")
            FIRST_SECONDS_FIELD_NUMBER: _ClassVar[int]
            REPEATING_SECONDS_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            first_seconds: int
            repeating_seconds: int
            threshold: int
            def __init__(self, first_seconds: _Optional[int] = ..., repeating_seconds: _Optional[int] = ..., threshold: _Optional[int] = ...) -> None: ...
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        ANY_FIELD_NUMBER: _ClassVar[int]
        inbound: QueueConfig.PositionAnnouncements.Disableable
        outbound: QueueConfig.PositionAnnouncements.Disableable
        manual: QueueConfig.PositionAnnouncements.Disableable
        preview: QueueConfig.PositionAnnouncements.Disableable
        any: QueueConfig.PositionAnnouncements.Disableable
        def __init__(self, inbound: _Optional[_Union[QueueConfig.PositionAnnouncements.Disableable, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.PositionAnnouncements.Disableable, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.PositionAnnouncements.Disableable, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.PositionAnnouncements.Disableable, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.PositionAnnouncements.Disableable, _Mapping]] = ...) -> None: ...
    class WaitTimeAnnouncements(_message.Message):
        __slots__ = ("inbound", "outbound", "manual", "preview", "any")
        class Disableable(_message.Message):
            __slots__ = ("config", "disable")
            CONFIG_FIELD_NUMBER: _ClassVar[int]
            DISABLE_FIELD_NUMBER: _ClassVar[int]
            config: QueueConfig.WaitTimeAnnouncements.Config
            disable: QueueConfig.Disable
            def __init__(self, config: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Config, _Mapping]] = ..., disable: _Optional[_Union[QueueConfig.Disable, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("first_seconds", "repeating_seconds", "threshold")
            FIRST_SECONDS_FIELD_NUMBER: _ClassVar[int]
            REPEATING_SECONDS_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            first_seconds: int
            repeating_seconds: int
            threshold: int
            def __init__(self, first_seconds: _Optional[int] = ..., repeating_seconds: _Optional[int] = ..., threshold: _Optional[int] = ...) -> None: ...
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        ANY_FIELD_NUMBER: _ClassVar[int]
        inbound: QueueConfig.WaitTimeAnnouncements.Disableable
        outbound: QueueConfig.WaitTimeAnnouncements.Disableable
        manual: QueueConfig.WaitTimeAnnouncements.Disableable
        preview: QueueConfig.WaitTimeAnnouncements.Disableable
        any: QueueConfig.WaitTimeAnnouncements.Disableable
        def __init__(self, inbound: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Disableable, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Disableable, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Disableable, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Disableable, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.WaitTimeAnnouncements.Disableable, _Mapping]] = ...) -> None: ...
    class AttentionTones(_message.Message):
        __slots__ = ("inbound", "outbound", "manual", "preview", "any")
        class Disableable(_message.Message):
            __slots__ = ("config", "disable")
            CONFIG_FIELD_NUMBER: _ClassVar[int]
            DISABLE_FIELD_NUMBER: _ClassVar[int]
            config: QueueConfig.AttentionTones.Config
            disable: QueueConfig.Disable
            def __init__(self, config: _Optional[_Union[QueueConfig.AttentionTones.Config, _Mapping]] = ..., disable: _Optional[_Union[QueueConfig.Disable, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("agent_status_paused", "agent_status_wrap_up", "tones")
            AGENT_STATUS_PAUSED_FIELD_NUMBER: _ClassVar[int]
            AGENT_STATUS_WRAP_UP_FIELD_NUMBER: _ClassVar[int]
            TONES_FIELD_NUMBER: _ClassVar[int]
            agent_status_paused: bool
            agent_status_wrap_up: bool
            tones: _containers.RepeatedCompositeFieldContainer[QueueConfig.AttentionTones.Tones]
            def __init__(self, agent_status_paused: bool = ..., agent_status_wrap_up: bool = ..., tones: _Optional[_Iterable[_Union[QueueConfig.AttentionTones.Tones, _Mapping]]] = ...) -> None: ...
        class Tones(_message.Message):
            __slots__ = ("tone", "pause")
            TONE_FIELD_NUMBER: _ClassVar[int]
            PAUSE_FIELD_NUMBER: _ClassVar[int]
            tone: _wrappers_pb2.Int64Value
            pause: _wrappers_pb2.DoubleValue
            def __init__(self, tone: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., pause: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_FIELD_NUMBER: _ClassVar[int]
        ANY_FIELD_NUMBER: _ClassVar[int]
        inbound: QueueConfig.AttentionTones.Disableable
        outbound: QueueConfig.AttentionTones.Disableable
        manual: QueueConfig.AttentionTones.Disableable
        preview: QueueConfig.AttentionTones.Disableable
        any: QueueConfig.AttentionTones.Disableable
        def __init__(self, inbound: _Optional[_Union[QueueConfig.AttentionTones.Disableable, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.AttentionTones.Disableable, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.AttentionTones.Disableable, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.AttentionTones.Disableable, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.AttentionTones.Disableable, _Mapping]] = ...) -> None: ...
    class InQueueConditions(_message.Message):
        __slots__ = ("no_agents_logged_in", "no_agents_with_required_skills_logged_in", "no_agents_available", "no_agents_with_required_skills_available", "pbx_ringing", "agent_lost", "default")
        class Condition(_message.Message):
            __slots__ = ("inbound", "outbound", "manual", "preview", "any")
            INBOUND_FIELD_NUMBER: _ClassVar[int]
            OUTBOUND_FIELD_NUMBER: _ClassVar[int]
            MANUAL_FIELD_NUMBER: _ClassVar[int]
            PREVIEW_FIELD_NUMBER: _ClassVar[int]
            ANY_FIELD_NUMBER: _ClassVar[int]
            inbound: QueueConfig.InQueueConditions.Config
            outbound: QueueConfig.InQueueConditions.Config
            manual: QueueConfig.InQueueConditions.Config
            preview: QueueConfig.InQueueConditions.Config
            any: QueueConfig.InQueueConditions.Config
            def __init__(self, inbound: _Optional[_Union[QueueConfig.InQueueConditions.Config, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.InQueueConditions.Config, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.InQueueConditions.Config, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.InQueueConditions.Config, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.InQueueConditions.Config, _Mapping]] = ...) -> None: ...
        class LimitedCondition(_message.Message):
            __slots__ = ("inbound", "outbound", "manual", "preview", "any")
            INBOUND_FIELD_NUMBER: _ClassVar[int]
            OUTBOUND_FIELD_NUMBER: _ClassVar[int]
            MANUAL_FIELD_NUMBER: _ClassVar[int]
            PREVIEW_FIELD_NUMBER: _ClassVar[int]
            ANY_FIELD_NUMBER: _ClassVar[int]
            inbound: QueueConfig.InQueueConditions.LimitedConfig
            outbound: QueueConfig.InQueueConditions.LimitedConfig
            manual: QueueConfig.InQueueConditions.LimitedConfig
            preview: QueueConfig.InQueueConditions.LimitedConfig
            any: QueueConfig.InQueueConditions.LimitedConfig
            def __init__(self, inbound: _Optional[_Union[QueueConfig.InQueueConditions.LimitedConfig, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.InQueueConditions.LimitedConfig, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.InQueueConditions.LimitedConfig, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.InQueueConditions.LimitedConfig, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.InQueueConditions.LimitedConfig, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("actions",)
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            actions: _containers.RepeatedCompositeFieldContainer[QueueConfig.InQueueConditions.Action]
            def __init__(self, actions: _Optional[_Iterable[_Union[QueueConfig.InQueueConditions.Action, _Mapping]]] = ...) -> None: ...
        class LimitedConfig(_message.Message):
            __slots__ = ("actions",)
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            actions: _containers.RepeatedCompositeFieldContainer[QueueConfig.InQueueConditions.LimitedAction]
            def __init__(self, actions: _Optional[_Iterable[_Union[QueueConfig.InQueueConditions.LimitedAction, _Mapping]]] = ...) -> None: ...
        class Action(_message.Message):
            __slots__ = ("after_seconds", "hang_up", "voicemail", "queued_callback", "trigger_ivr", "add_skills", "drop_skills")
            AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
            HANG_UP_FIELD_NUMBER: _ClassVar[int]
            VOICEMAIL_FIELD_NUMBER: _ClassVar[int]
            QUEUED_CALLBACK_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_IVR_FIELD_NUMBER: _ClassVar[int]
            ADD_SKILLS_FIELD_NUMBER: _ClassVar[int]
            DROP_SKILLS_FIELD_NUMBER: _ClassVar[int]
            after_seconds: int
            hang_up: QueueConfig.Optionless
            voicemail: QueueConfig.Optionless
            queued_callback: QueueConfig.Optionless
            trigger_ivr: _org_pb2.DigitWrapper
            add_skills: QueueConfig.Skills
            drop_skills: QueueConfig.Skills
            def __init__(self, after_seconds: _Optional[int] = ..., hang_up: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., voicemail: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., queued_callback: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., trigger_ivr: _Optional[_Union[_org_pb2.DigitWrapper, _Mapping]] = ..., add_skills: _Optional[_Union[QueueConfig.Skills, _Mapping]] = ..., drop_skills: _Optional[_Union[QueueConfig.Skills, _Mapping]] = ...) -> None: ...
        class LimitedAction(_message.Message):
            __slots__ = ("after_seconds", "hang_up", "voicemail", "queued_callback", "trigger_ivr")
            AFTER_SECONDS_FIELD_NUMBER: _ClassVar[int]
            HANG_UP_FIELD_NUMBER: _ClassVar[int]
            VOICEMAIL_FIELD_NUMBER: _ClassVar[int]
            QUEUED_CALLBACK_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_IVR_FIELD_NUMBER: _ClassVar[int]
            after_seconds: int
            hang_up: QueueConfig.Optionless
            voicemail: QueueConfig.Optionless
            queued_callback: QueueConfig.Optionless
            trigger_ivr: _org_pb2.DigitWrapper
            def __init__(self, after_seconds: _Optional[int] = ..., hang_up: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., voicemail: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., queued_callback: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., trigger_ivr: _Optional[_Union[_org_pb2.DigitWrapper, _Mapping]] = ...) -> None: ...
        NO_AGENTS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        NO_AGENTS_WITH_REQUIRED_SKILLS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        NO_AGENTS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        NO_AGENTS_WITH_REQUIRED_SKILLS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        PBX_RINGING_FIELD_NUMBER: _ClassVar[int]
        AGENT_LOST_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        no_agents_logged_in: QueueConfig.InQueueConditions.LimitedCondition
        no_agents_with_required_skills_logged_in: QueueConfig.InQueueConditions.Condition
        no_agents_available: QueueConfig.InQueueConditions.LimitedCondition
        no_agents_with_required_skills_available: QueueConfig.InQueueConditions.Condition
        pbx_ringing: QueueConfig.InQueueConditions.Condition
        agent_lost: QueueConfig.InQueueConditions.Condition
        default: QueueConfig.InQueueConditions.LimitedCondition
        def __init__(self, no_agents_logged_in: _Optional[_Union[QueueConfig.InQueueConditions.LimitedCondition, _Mapping]] = ..., no_agents_with_required_skills_logged_in: _Optional[_Union[QueueConfig.InQueueConditions.Condition, _Mapping]] = ..., no_agents_available: _Optional[_Union[QueueConfig.InQueueConditions.LimitedCondition, _Mapping]] = ..., no_agents_with_required_skills_available: _Optional[_Union[QueueConfig.InQueueConditions.Condition, _Mapping]] = ..., pbx_ringing: _Optional[_Union[QueueConfig.InQueueConditions.Condition, _Mapping]] = ..., agent_lost: _Optional[_Union[QueueConfig.InQueueConditions.Condition, _Mapping]] = ..., default: _Optional[_Union[QueueConfig.InQueueConditions.LimitedCondition, _Mapping]] = ...) -> None: ...
    class KeyPressEvents(_message.Message):
        __slots__ = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "asterisk", "hashtag")
        class Action(_message.Message):
            __slots__ = ("inbound", "outbound", "manual", "preview", "any")
            INBOUND_FIELD_NUMBER: _ClassVar[int]
            OUTBOUND_FIELD_NUMBER: _ClassVar[int]
            MANUAL_FIELD_NUMBER: _ClassVar[int]
            PREVIEW_FIELD_NUMBER: _ClassVar[int]
            ANY_FIELD_NUMBER: _ClassVar[int]
            inbound: QueueConfig.KeyPressEvents.Config
            outbound: QueueConfig.KeyPressEvents.Config
            manual: QueueConfig.KeyPressEvents.Config
            preview: QueueConfig.KeyPressEvents.Config
            any: QueueConfig.KeyPressEvents.Config
            def __init__(self, inbound: _Optional[_Union[QueueConfig.KeyPressEvents.Config, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.KeyPressEvents.Config, _Mapping]] = ..., manual: _Optional[_Union[QueueConfig.KeyPressEvents.Config, _Mapping]] = ..., preview: _Optional[_Union[QueueConfig.KeyPressEvents.Config, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.KeyPressEvents.Config, _Mapping]] = ...) -> None: ...
        class Config(_message.Message):
            __slots__ = ("hang_up", "trigger_ivr", "voicemail", "queued_callback", "add_skills", "drop_skills")
            HANG_UP_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_IVR_FIELD_NUMBER: _ClassVar[int]
            VOICEMAIL_FIELD_NUMBER: _ClassVar[int]
            QUEUED_CALLBACK_FIELD_NUMBER: _ClassVar[int]
            ADD_SKILLS_FIELD_NUMBER: _ClassVar[int]
            DROP_SKILLS_FIELD_NUMBER: _ClassVar[int]
            hang_up: QueueConfig.Optionless
            trigger_ivr: QueueConfig.Optionless
            voicemail: QueueConfig.Optionless
            queued_callback: QueueConfig.Optionless
            add_skills: QueueConfig.Skills
            drop_skills: QueueConfig.Skills
            def __init__(self, hang_up: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., trigger_ivr: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., voicemail: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., queued_callback: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., add_skills: _Optional[_Union[QueueConfig.Skills, _Mapping]] = ..., drop_skills: _Optional[_Union[QueueConfig.Skills, _Mapping]] = ...) -> None: ...
        ZERO_FIELD_NUMBER: _ClassVar[int]
        ONE_FIELD_NUMBER: _ClassVar[int]
        TWO_FIELD_NUMBER: _ClassVar[int]
        THREE_FIELD_NUMBER: _ClassVar[int]
        FOUR_FIELD_NUMBER: _ClassVar[int]
        FIVE_FIELD_NUMBER: _ClassVar[int]
        SIX_FIELD_NUMBER: _ClassVar[int]
        SEVEN_FIELD_NUMBER: _ClassVar[int]
        EIGHT_FIELD_NUMBER: _ClassVar[int]
        NINE_FIELD_NUMBER: _ClassVar[int]
        ASTERISK_FIELD_NUMBER: _ClassVar[int]
        HASHTAG_FIELD_NUMBER: _ClassVar[int]
        zero: QueueConfig.KeyPressEvents.Action
        one: QueueConfig.KeyPressEvents.Action
        two: QueueConfig.KeyPressEvents.Action
        three: QueueConfig.KeyPressEvents.Action
        four: QueueConfig.KeyPressEvents.Action
        five: QueueConfig.KeyPressEvents.Action
        six: QueueConfig.KeyPressEvents.Action
        seven: QueueConfig.KeyPressEvents.Action
        eight: QueueConfig.KeyPressEvents.Action
        nine: QueueConfig.KeyPressEvents.Action
        asterisk: QueueConfig.KeyPressEvents.Action
        hashtag: QueueConfig.KeyPressEvents.Action
        def __init__(self, zero: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., one: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., two: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., three: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., four: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., five: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., six: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., seven: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., eight: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., nine: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., asterisk: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ..., hashtag: _Optional[_Union[QueueConfig.KeyPressEvents.Action, _Mapping]] = ...) -> None: ...
    class PbxRingStrategy(_message.Message):
        __slots__ = ("inbound", "outbound", "any")
        class Config(_message.Message):
            __slots__ = ("ring_all", "highest_score_only", "random", "agent_score", "agent_score_memory")
            RING_ALL_FIELD_NUMBER: _ClassVar[int]
            HIGHEST_SCORE_ONLY_FIELD_NUMBER: _ClassVar[int]
            RANDOM_FIELD_NUMBER: _ClassVar[int]
            AGENT_SCORE_FIELD_NUMBER: _ClassVar[int]
            AGENT_SCORE_MEMORY_FIELD_NUMBER: _ClassVar[int]
            ring_all: QueueConfig.Optionless
            highest_score_only: QueueConfig.Optionless
            random: QueueConfig.Optionless
            agent_score: int
            agent_score_memory: int
            def __init__(self, ring_all: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., highest_score_only: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., random: _Optional[_Union[QueueConfig.Optionless, _Mapping]] = ..., agent_score: _Optional[int] = ..., agent_score_memory: _Optional[int] = ...) -> None: ...
        INBOUND_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_FIELD_NUMBER: _ClassVar[int]
        ANY_FIELD_NUMBER: _ClassVar[int]
        inbound: QueueConfig.PbxRingStrategy.Config
        outbound: QueueConfig.PbxRingStrategy.Config
        any: QueueConfig.PbxRingStrategy.Config
        def __init__(self, inbound: _Optional[_Union[QueueConfig.PbxRingStrategy.Config, _Mapping]] = ..., outbound: _Optional[_Union[QueueConfig.PbxRingStrategy.Config, _Mapping]] = ..., any: _Optional[_Union[QueueConfig.PbxRingStrategy.Config, _Mapping]] = ...) -> None: ...
    class QueueMonitoringSilenceWaitTimes(_message.Message):
        __slots__ = ("first_milliseconds", "second_milliseconds")
        FIRST_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
        SECOND_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
        first_milliseconds: int
        second_milliseconds: int
        def __init__(self, first_milliseconds: _Optional[int] = ..., second_milliseconds: _Optional[int] = ...) -> None: ...
    class Disable(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Optionless(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Skills(_message.Message):
        __slots__ = ("p3_ids",)
        P3_IDS_FIELD_NUMBER: _ClassVar[int]
        p3_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, p3_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_GENDER_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_MIXING_FIELD_NUMBER: _ClassVar[int]
    POSITION_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_TONES_FIELD_NUMBER: _ClassVar[int]
    IN_QUEUE_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    KEY_PRESS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    PBX_RING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    QUEUE_MONITORING_SILENCE_WAIT_TIMES_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    NUMBER_UPDATE_FIELD_NUMBER: _ClassVar[int]
    INBOUND_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    INTERCOM_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    config_modified: _timestamp_pb2.Timestamp
    sounds_modified: _timestamp_pb2.Timestamp
    sounds_language: str
    sounds_gender: str
    announcement_mixing: QueueConfig.AnnouncementMixing
    position_announcements: QueueConfig.PositionAnnouncements
    wait_time_announcements: QueueConfig.WaitTimeAnnouncements
    attention_tones: QueueConfig.AttentionTones
    in_queue_conditions: QueueConfig.InQueueConditions
    key_press_events: QueueConfig.KeyPressEvents
    pbx_ring_strategy: QueueConfig.PbxRingStrategy
    queue_monitoring_silence_wait_times: QueueConfig.QueueMonitoringSilenceWaitTimes
    callback_timeout_minutes: int
    number_update: bool
    inbound_override: _org_pb2.InboundOverrideOption
    intercom_connection: _org_pb2.IntercomConnection
    def __init__(self, name: _Optional[str] = ..., config_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sounds_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sounds_language: _Optional[str] = ..., sounds_gender: _Optional[str] = ..., announcement_mixing: _Optional[_Union[QueueConfig.AnnouncementMixing, _Mapping]] = ..., position_announcements: _Optional[_Union[QueueConfig.PositionAnnouncements, _Mapping]] = ..., wait_time_announcements: _Optional[_Union[QueueConfig.WaitTimeAnnouncements, _Mapping]] = ..., attention_tones: _Optional[_Union[QueueConfig.AttentionTones, _Mapping]] = ..., in_queue_conditions: _Optional[_Union[QueueConfig.InQueueConditions, _Mapping]] = ..., key_press_events: _Optional[_Union[QueueConfig.KeyPressEvents, _Mapping]] = ..., pbx_ring_strategy: _Optional[_Union[QueueConfig.PbxRingStrategy, _Mapping]] = ..., queue_monitoring_silence_wait_times: _Optional[_Union[QueueConfig.QueueMonitoringSilenceWaitTimes, _Mapping]] = ..., callback_timeout_minutes: _Optional[int] = ..., number_update: bool = ..., inbound_override: _Optional[_Union[_org_pb2.InboundOverrideOption, str]] = ..., intercom_connection: _Optional[_Union[_org_pb2.IntercomConnection, str]] = ...) -> None: ...

class GetAllQueueConfigSoundsReq(_message.Message):
    __slots__ = ("config_name",)
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    def __init__(self, config_name: _Optional[str] = ...) -> None: ...

class GetAllQueueConfigSoundsRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class ListOwnedUsersRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListOwnedUsersResponse(_message.Message):
    __slots__ = ("user_descriptions",)
    USER_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    user_descriptions: _containers.RepeatedCompositeFieldContainer[UserDescription]
    def __init__(self, user_descriptions: _Optional[_Iterable[_Union[UserDescription, _Mapping]]] = ...) -> None: ...

class ListOwnedOrgsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListOwnedOrgsResponse(_message.Message):
    __slots__ = ("organization_descriptions",)
    ORGANIZATION_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    organization_descriptions: _containers.RepeatedCompositeFieldContainer[OrganizationDescription]
    def __init__(self, organization_descriptions: _Optional[_Iterable[_Union[OrganizationDescription, _Mapping]]] = ...) -> None: ...

class GetUserBlockedRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserBlockedResponse(_message.Message):
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

class UnblockUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UnblockUserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnMigratedUser(_message.Message):
    __slots__ = ("agent_sid", "login_sid", "client_sid", "user_name", "user_id", "login_disabled", "first_name", "last_name")
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    login_sid: int
    client_sid: int
    user_name: str
    user_id: str
    login_disabled: bool
    first_name: str
    last_name: str
    def __init__(self, agent_sid: _Optional[int] = ..., login_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., user_name: _Optional[str] = ..., user_id: _Optional[str] = ..., login_disabled: bool = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class ListP3UnMigratedUsersRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ListP3UnMigratedUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UnMigratedUser]
    def __init__(self, users: _Optional[_Iterable[_Union[UnMigratedUser, _Mapping]]] = ...) -> None: ...

class MigrateP3UserRequest(_message.Message):
    __slots__ = ("agent_sid", "login_sid", "client_sid", "password")
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    login_sid: int
    client_sid: int
    password: str
    def __init__(self, agent_sid: _Optional[int] = ..., login_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class MigrateP3UserResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateP3UserNameRequest(_message.Message):
    __slots__ = ("agent_sid", "login_sid", "user_name", "client_sid")
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    login_sid: int
    user_name: str
    client_sid: int
    def __init__(self, agent_sid: _Optional[int] = ..., login_sid: _Optional[int] = ..., user_name: _Optional[str] = ..., client_sid: _Optional[int] = ...) -> None: ...

class UpdateP3UserNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetQueueConfigSoundReq(_message.Message):
    __slots__ = ("config", "sound")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    config: str
    sound: _org_pb2.ConfigSound
    def __init__(self, config: _Optional[str] = ..., sound: _Optional[_Union[_org_pb2.ConfigSound, str]] = ...) -> None: ...

class GetQueueConfigSoundRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class SetQueueConfigSoundReq(_message.Message):
    __slots__ = ("config", "sound", "file_name")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    config: str
    sound: _org_pb2.ConfigSound
    file_name: str
    def __init__(self, config: _Optional[str] = ..., sound: _Optional[_Union[_org_pb2.ConfigSound, str]] = ..., file_name: _Optional[str] = ...) -> None: ...

class SetQueueConfigSoundRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAllQueueConfigSoundsFromSourceReq(_message.Message):
    __slots__ = ("to_config", "config", "default_profile")
    class DefaultProfile(_message.Message):
        __slots__ = ("language", "gender")
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        GENDER_FIELD_NUMBER: _ClassVar[int]
        language: _org_pb2.SoundLanguage
        gender: _org_pb2.SoundGender
        def __init__(self, language: _Optional[_Union[_org_pb2.SoundLanguage, str]] = ..., gender: _Optional[_Union[_org_pb2.SoundGender, str]] = ...) -> None: ...
    TO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    to_config: str
    config: _wrappers_pb2.StringValue
    default_profile: SetAllQueueConfigSoundsFromSourceReq.DefaultProfile
    def __init__(self, to_config: _Optional[str] = ..., config: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_profile: _Optional[_Union[SetAllQueueConfigSoundsFromSourceReq.DefaultProfile, _Mapping]] = ...) -> None: ...

class SetAllQueueConfigSoundsFromSourceRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveLoginStrikesRequest(_message.Message):
    __slots__ = ("login_log_sids",)
    LOGIN_LOG_SIDS_FIELD_NUMBER: _ClassVar[int]
    login_log_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, login_log_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class RemoveLoginStrikesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveUserLoginStrikesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RemoveUserLoginStrikesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLoginHistoryRequest(_message.Message):
    __slots__ = ("user_id", "origination_ip", "duration", "strikes_only")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATION_IP_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STRIKES_ONLY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    origination_ip: str
    duration: int
    strikes_only: bool
    def __init__(self, user_id: _Optional[str] = ..., origination_ip: _Optional[str] = ..., duration: _Optional[int] = ..., strikes_only: bool = ...) -> None: ...

class ListLoginHistoryResponse(_message.Message):
    __slots__ = ("login_events",)
    LOGIN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    login_events: _containers.RepeatedCompositeFieldContainer[LoginEvent]
    def __init__(self, login_events: _Optional[_Iterable[_Union[LoginEvent, _Mapping]]] = ...) -> None: ...

class LoginEvent(_message.Message):
    __slots__ = ("login_log_sid", "user_name", "origination_ip", "login_success", "strike", "notes", "date_attempted")
    LOGIN_LOG_SID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATION_IP_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    DATE_ATTEMPTED_FIELD_NUMBER: _ClassVar[int]
    login_log_sid: int
    user_name: str
    origination_ip: str
    login_success: bool
    strike: bool
    notes: str
    date_attempted: _timestamp_pb2.Timestamp
    def __init__(self, login_log_sid: _Optional[int] = ..., user_name: _Optional[str] = ..., origination_ip: _Optional[str] = ..., login_success: bool = ..., strike: bool = ..., notes: _Optional[str] = ..., date_attempted: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OrgBillingSettings(_message.Message):
    __slots__ = ("org_id", "voice_analytics_price_per_hour", "analytics_price_per_doc", "default", "country_region_overrides", "agent_rates", "email_price_per_message")
    class CountryRegionOverridesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BillingRegionMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BillingRegionMap, _Mapping]] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_ANALYTICS_PRICE_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_PRICE_PER_DOC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_REGION_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    AGENT_RATES_FIELD_NUMBER: _ClassVar[int]
    EMAIL_PRICE_PER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    voice_analytics_price_per_hour: float
    analytics_price_per_doc: float
    default: PhoneBillingRates
    country_region_overrides: _containers.MessageMap[int, BillingRegionMap]
    agent_rates: AgentBillingRates
    email_price_per_message: _wrappers_pb2.FloatValue
    def __init__(self, org_id: _Optional[str] = ..., voice_analytics_price_per_hour: _Optional[float] = ..., analytics_price_per_doc: _Optional[float] = ..., default: _Optional[_Union[PhoneBillingRates, _Mapping]] = ..., country_region_overrides: _Optional[_Mapping[int, BillingRegionMap]] = ..., agent_rates: _Optional[_Union[AgentBillingRates, _Mapping]] = ..., email_price_per_message: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class BillingRegionMap(_message.Message):
    __slots__ = ("region_rates",)
    class RegionRatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PhoneBillingRates
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PhoneBillingRates, _Mapping]] = ...) -> None: ...
    REGION_RATES_FIELD_NUMBER: _ClassVar[int]
    region_rates: _containers.MessageMap[str, PhoneBillingRates]
    def __init__(self, region_rates: _Optional[_Mapping[str, PhoneBillingRates]] = ...) -> None: ...

class AgentBillingRates(_message.Message):
    __slots__ = ("agent_toll_free_ppi", "agent_softphone_ppi", "agent_local_ppi")
    AGENT_TOLL_FREE_PPI_FIELD_NUMBER: _ClassVar[int]
    AGENT_SOFTPHONE_PPI_FIELD_NUMBER: _ClassVar[int]
    AGENT_LOCAL_PPI_FIELD_NUMBER: _ClassVar[int]
    agent_toll_free_ppi: float
    agent_softphone_ppi: float
    agent_local_ppi: float
    def __init__(self, agent_toll_free_ppi: _Optional[float] = ..., agent_softphone_ppi: _Optional[float] = ..., agent_local_ppi: _Optional[float] = ...) -> None: ...

class PhoneBillingRates(_message.Message):
    __slots__ = ("billing_increment_seconds", "inbound_ppi", "sms_price_per_attempt", "vocal_direct_price_per_message", "seconds", "attempts", "connected_calls")
    class Seconds(_message.Message):
        __slots__ = ("ppi", "linkback_ppi", "agent_linkcall_ppi", "minimum_billed_increments", "maximum_billed_increments", "minimum_linkback_billed_increments", "maximum_linkback_billed_increments", "machine_hangup_increments_billed", "human_hangup_increments_billed")
        PPI_FIELD_NUMBER: _ClassVar[int]
        LINKBACK_PPI_FIELD_NUMBER: _ClassVar[int]
        AGENT_LINKCALL_PPI_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_LINKBACK_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_LINKBACK_BILLED_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
        MACHINE_HANGUP_INCREMENTS_BILLED_FIELD_NUMBER: _ClassVar[int]
        HUMAN_HANGUP_INCREMENTS_BILLED_FIELD_NUMBER: _ClassVar[int]
        ppi: float
        linkback_ppi: float
        agent_linkcall_ppi: float
        minimum_billed_increments: int
        maximum_billed_increments: _wrappers_pb2.Int64Value
        minimum_linkback_billed_increments: int
        maximum_linkback_billed_increments: _wrappers_pb2.Int64Value
        machine_hangup_increments_billed: _wrappers_pb2.Int64Value
        human_hangup_increments_billed: _wrappers_pb2.Int64Value
        def __init__(self, ppi: _Optional[float] = ..., linkback_ppi: _Optional[float] = ..., agent_linkcall_ppi: _Optional[float] = ..., minimum_billed_increments: _Optional[int] = ..., maximum_billed_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., minimum_linkback_billed_increments: _Optional[int] = ..., maximum_linkback_billed_increments: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., machine_hangup_increments_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., human_hangup_increments_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    class Attempts(_message.Message):
        __slots__ = ("ppa", "linkback_ppa", "agent_linkcall_ppa")
        PPA_FIELD_NUMBER: _ClassVar[int]
        LINKBACK_PPA_FIELD_NUMBER: _ClassVar[int]
        AGENT_LINKCALL_PPA_FIELD_NUMBER: _ClassVar[int]
        ppa: float
        linkback_ppa: float
        agent_linkcall_ppa: float
        def __init__(self, ppa: _Optional[float] = ..., linkback_ppa: _Optional[float] = ..., agent_linkcall_ppa: _Optional[float] = ...) -> None: ...
    class ConnectedCalls(_message.Message):
        __slots__ = ("ppc", "linkback_ppc", "agent_linkcall_ppc")
        PPC_FIELD_NUMBER: _ClassVar[int]
        LINKBACK_PPC_FIELD_NUMBER: _ClassVar[int]
        AGENT_LINKCALL_PPC_FIELD_NUMBER: _ClassVar[int]
        ppc: float
        linkback_ppc: float
        agent_linkcall_ppc: float
        def __init__(self, ppc: _Optional[float] = ..., linkback_ppc: _Optional[float] = ..., agent_linkcall_ppc: _Optional[float] = ...) -> None: ...
    BILLING_INCREMENT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INBOUND_PPI_FIELD_NUMBER: _ClassVar[int]
    SMS_PRICE_PER_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    VOCAL_DIRECT_PRICE_PER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_CALLS_FIELD_NUMBER: _ClassVar[int]
    billing_increment_seconds: int
    inbound_ppi: float
    sms_price_per_attempt: float
    vocal_direct_price_per_message: float
    seconds: PhoneBillingRates.Seconds
    attempts: PhoneBillingRates.Attempts
    connected_calls: PhoneBillingRates.ConnectedCalls
    def __init__(self, billing_increment_seconds: _Optional[int] = ..., inbound_ppi: _Optional[float] = ..., sms_price_per_attempt: _Optional[float] = ..., vocal_direct_price_per_message: _Optional[float] = ..., seconds: _Optional[_Union[PhoneBillingRates.Seconds, _Mapping]] = ..., attempts: _Optional[_Union[PhoneBillingRates.Attempts, _Mapping]] = ..., connected_calls: _Optional[_Union[PhoneBillingRates.ConnectedCalls, _Mapping]] = ...) -> None: ...

class GetOrgBillingSettingsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetOrgBillingSettingsResponse(_message.Message):
    __slots__ = ("settings", "country_default_regions")
    class CountryDefaultRegionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BillingRegionMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BillingRegionMap, _Mapping]] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DEFAULT_REGIONS_FIELD_NUMBER: _ClassVar[int]
    settings: OrgBillingSettings
    country_default_regions: _containers.MessageMap[int, BillingRegionMap]
    def __init__(self, settings: _Optional[_Union[OrgBillingSettings, _Mapping]] = ..., country_default_regions: _Optional[_Mapping[int, BillingRegionMap]] = ...) -> None: ...

class SetOrgBillingSettingsRequest(_message.Message):
    __slots__ = ("settings", "field_mask")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    settings: OrgBillingSettings
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, settings: _Optional[_Union[OrgBillingSettings, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetOrgBillingSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddOrgBillingOverrideRequest(_message.Message):
    __slots__ = ("org_id", "region", "rates", "country")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region: str
    rates: PhoneBillingRates
    country: _country_pb2.Country
    def __init__(self, org_id: _Optional[str] = ..., region: _Optional[str] = ..., rates: _Optional[_Union[PhoneBillingRates, _Mapping]] = ..., country: _Optional[_Union[_country_pb2.Country, str]] = ...) -> None: ...

class AddOrgBillingOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveOrgBillingOverrideRequest(_message.Message):
    __slots__ = ("org_id", "region", "country")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region: str
    country: _country_pb2.Country
    def __init__(self, org_id: _Optional[str] = ..., region: _Optional[str] = ..., country: _Optional[_Union[_country_pb2.Country, str]] = ...) -> None: ...

class RemoveOrgBillingOverrideResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemDefaultBillingRatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemDefaultBillingRatesResponse(_message.Message):
    __slots__ = ("email_price_per_message", "phone_rates", "agent_rates")
    EMAIL_PRICE_PER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PHONE_RATES_FIELD_NUMBER: _ClassVar[int]
    AGENT_RATES_FIELD_NUMBER: _ClassVar[int]
    email_price_per_message: float
    phone_rates: PhoneBillingRates
    agent_rates: AgentBillingRates
    def __init__(self, email_price_per_message: _Optional[float] = ..., phone_rates: _Optional[_Union[PhoneBillingRates, _Mapping]] = ..., agent_rates: _Optional[_Union[AgentBillingRates, _Mapping]] = ...) -> None: ...

class UpdateP3UserSidsRequest(_message.Message):
    __slots__ = ("user_id", "agent_sid", "login_sid", "field_mask")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    agent_sid: int
    login_sid: int
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, user_id: _Optional[str] = ..., agent_sid: _Optional[int] = ..., login_sid: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateP3UserSidsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AuthConnectionSettings(_message.Message):
    __slots__ = ("provider", "issuer_url", "tenant_url", "client_id", "connection_id", "secret_expiration", "default_group", "custom_groups")
    class SecretExpiration(_message.Message):
        __slots__ = ("date",)
        DATE_FIELD_NUMBER: _ClassVar[int]
        date: _timestamp_pb2.Timestamp
        def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    TENANT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GROUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GROUPS_FIELD_NUMBER: _ClassVar[int]
    provider: _org_pb2.IdentityProvider
    issuer_url: str
    tenant_url: str
    client_id: str
    connection_id: str
    secret_expiration: AuthConnectionSettings.SecretExpiration
    default_group: GroupItem
    custom_groups: _containers.RepeatedCompositeFieldContainer[GroupItem]
    def __init__(self, provider: _Optional[_Union[_org_pb2.IdentityProvider, str]] = ..., issuer_url: _Optional[str] = ..., tenant_url: _Optional[str] = ..., client_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., secret_expiration: _Optional[_Union[AuthConnectionSettings.SecretExpiration, _Mapping]] = ..., default_group: _Optional[_Union[GroupItem, _Mapping]] = ..., custom_groups: _Optional[_Iterable[_Union[GroupItem, _Mapping]]] = ...) -> None: ...

class GroupItem(_message.Message):
    __slots__ = ("group_name", "hunt_group_sid", "agent_profile_group_id", "p3_permission_group_id", "permission_group_ids")
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    P3_PERMISSION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    group_name: str
    hunt_group_sid: int
    agent_profile_group_id: str
    p3_permission_group_id: str
    permission_group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_name: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., agent_profile_group_id: _Optional[str] = ..., p3_permission_group_id: _Optional[str] = ..., permission_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateAuthConnectionRequest(_message.Message):
    __slots__ = ("settings", "client_secret")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    settings: AuthConnectionSettings
    client_secret: str
    def __init__(self, settings: _Optional[_Union[AuthConnectionSettings, _Mapping]] = ..., client_secret: _Optional[str] = ...) -> None: ...

class CreateAuthConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthConnectionSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthConnectionSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: AuthConnectionSettings
    def __init__(self, settings: _Optional[_Union[AuthConnectionSettings, _Mapping]] = ...) -> None: ...

class UpdateAuthConnectionSettingsRequest(_message.Message):
    __slots__ = ("settings", "client_secret", "field_mask")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    settings: AuthConnectionSettings
    client_secret: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, settings: _Optional[_Union[AuthConnectionSettings, _Mapping]] = ..., client_secret: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAuthConnectionSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAuthConnectionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAuthConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserSubscription(_message.Message):
    __slots__ = ("subscription_id", "event_type", "user_id", "room303", "version", "filters")
    class Room303(_message.Message):
        __slots__ = ("room_name",)
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        room_name: str
        def __init__(self, room_name: _Optional[str] = ...) -> None: ...
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM303_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    event_type: _event_types_pb2.EventType
    user_id: str
    room303: UserSubscription.Room303
    version: int
    filters: _containers.RepeatedCompositeFieldContainer[_notifications_pb2.FieldValueFilter]
    def __init__(self, subscription_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., user_id: _Optional[str] = ..., room303: _Optional[_Union[UserSubscription.Room303, _Mapping]] = ..., version: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[_notifications_pb2.FieldValueFilter, _Mapping]]] = ...) -> None: ...

class AddUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class AddUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class GetUserSubscriptionRequest(_message.Message):
    __slots__ = ("user_id", "subscription_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class GetUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription", "field_mask")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class RemoveUserSubscriptionRequest(_message.Message):
    __slots__ = ("user_id", "subscription_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class RemoveUserSubscriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUserSubscriptionsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListUserSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[UserSubscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[UserSubscription, _Mapping]]] = ...) -> None: ...

class ListOrgSubscriptionsRequest(_message.Message):
    __slots__ = ("org_id", "event_type")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    event_type: _event_types_pb2.EventType
    def __init__(self, org_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ...) -> None: ...

class ListOrgSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[UserSubscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[UserSubscription, _Mapping]]] = ...) -> None: ...

class GetSystemEnvironmentDetailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemEnvironmentDetailsResponse(_message.Message):
    __slots__ = ("region_id", "cluster_id")
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    cluster_id: str
    def __init__(self, region_id: _Optional[str] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class CreateDelegatedUserRequest(_message.Message):
    __slots__ = ("user_id", "org_id", "email", "user_name", "first_name", "last_name", "groups", "connection_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    email: str
    user_name: str
    first_name: str
    last_name: str
    groups: _containers.RepeatedScalarFieldContainer[str]
    connection_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., email: _Optional[str] = ..., user_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., groups: _Optional[_Iterable[str]] = ..., connection_id: _Optional[str] = ...) -> None: ...

class CreateDelegatedUserResponse(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserEmailVerifiedRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetUserEmailVerifiedResponse(_message.Message):
    __slots__ = ("verified",)
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    def __init__(self, verified: bool = ...) -> None: ...

class SendUserVerificationEmailRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class SendUserVerificationEmailResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManualUserEmailVerificationRequest(_message.Message):
    __slots__ = ("user_id", "org_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class ManualUserEmailVerificationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentStatisticsTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentStatisticsTemplatesResponse(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[AgentLoginGuiStatisticsTemplate]
    def __init__(self, templates: _Optional[_Iterable[_Union[AgentLoginGuiStatisticsTemplate, _Mapping]]] = ...) -> None: ...

class CreateAgentStatisticsTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: AgentLoginGuiStatisticsTemplate
    def __init__(self, template: _Optional[_Union[AgentLoginGuiStatisticsTemplate, _Mapping]] = ...) -> None: ...

class CreateAgentStatisticsTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentStatisticsTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: AgentLoginGuiStatisticsTemplate
    def __init__(self, template: _Optional[_Union[AgentLoginGuiStatisticsTemplate, _Mapping]] = ...) -> None: ...

class UpdateAgentStatisticsTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAgentStatisticsTemplateRequest(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class DeleteAgentStatisticsTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentLoginGuiStatisticsTemplate(_message.Message):
    __slots__ = ("description", "generic_statistic_format_rule", "xml_client_property_sid", "inclusion_type", "statistic_table_id", "name")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GENERIC_STATISTIC_FORMAT_RULE_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATISTIC_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    description: str
    generic_statistic_format_rule: _containers.RepeatedCompositeFieldContainer[GenericStatisticFormatRule]
    xml_client_property_sid: int
    inclusion_type: str
    statistic_table_id: str
    name: str
    def __init__(self, description: _Optional[str] = ..., generic_statistic_format_rule: _Optional[_Iterable[_Union[GenericStatisticFormatRule, _Mapping]]] = ..., xml_client_property_sid: _Optional[int] = ..., inclusion_type: _Optional[str] = ..., statistic_table_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GenericStatisticFormatRule(_message.Message):
    __slots__ = ("statistic_id", "database_field_name", "header_text", "header_tooltip_text", "simple_date_format_string", "timezone_id_string", "time_zone_enum")
    STATISTIC_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    HEADER_TOOLTIP_TEXT_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_DATE_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_STRING_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_ENUM_FIELD_NUMBER: _ClassVar[int]
    statistic_id: str
    database_field_name: str
    header_text: str
    header_tooltip_text: str
    simple_date_format_string: str
    timezone_id_string: str
    time_zone_enum: _org_pb2.TimeZone
    def __init__(self, statistic_id: _Optional[str] = ..., database_field_name: _Optional[str] = ..., header_text: _Optional[str] = ..., header_tooltip_text: _Optional[str] = ..., simple_date_format_string: _Optional[str] = ..., timezone_id_string: _Optional[str] = ..., time_zone_enum: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...
