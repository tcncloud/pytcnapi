import datetime

from api.commons import ana_pb2 as _ana_pb2
from api.commons import classifier_pb2 as _classifier_pb2
from api.commons import country_pb2 as _country_pb2
from api.commons import enums_pb2 as _enums_pb2
from api.commons import lms_pb2 as _lms_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import org_preferences_pb2 as _org_preferences_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_country: _country_pb2.Country
    time_zone: _org_pb2.TimeZone
    display_language: _org_pb2.DisplayLanguage
    locale_preferences: _org_preferences_pb2.LocalePreferences
    def __init__(self, org_id: _Optional[str] = ..., default_country: _Optional[_Union[_country_pb2.Country, str]] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., display_language: _Optional[_Union[_org_pb2.DisplayLanguage, str]] = ..., locale_preferences: _Optional[_Union[_org_preferences_pb2.LocalePreferences, _Mapping]] = ...) -> None: ...

class AgentPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_DIAL_IN_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_IN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_OUT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_DIAL_IN_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DIAL_IN_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_CALLER_ID_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    USE_MANUAL_DIAL_CALLER_ID_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_agent_dial_in: str
    pbx_extension_length: int
    default_softphone_volume_in: int
    default_softphone_volume_out: int
    config_dial_in_numbers: _containers.RepeatedScalarFieldContainer[str]
    client_dial_in_numbers: _containers.RepeatedScalarFieldContainer[str]
    manual_dial_caller_id_privacy: bool
    use_manual_dial_caller_id_privacy: bool
    def __init__(self, org_id: _Optional[str] = ..., default_agent_dial_in: _Optional[str] = ..., pbx_extension_length: _Optional[int] = ..., default_softphone_volume_in: _Optional[int] = ..., default_softphone_volume_out: _Optional[int] = ..., config_dial_in_numbers: _Optional[_Iterable[str]] = ..., client_dial_in_numbers: _Optional[_Iterable[str]] = ..., manual_dial_caller_id_privacy: _Optional[bool] = ..., use_manual_dial_caller_id_privacy: _Optional[bool] = ...) -> None: ...

class ContactPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTACT_IMPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    USE_CONTACT_IMPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTACT_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    USE_CONTACT_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    DISCARD_RECORD_DEFAULT_ABSENT_NUMBERS_HANDLING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTACTS_IMPORT_RANDOMIZATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EMAIL_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DUPLICATE_HANDLING_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_contact_import_format: ImportFormat
    use_contact_import_format: bool
    default_contact_area_code: ContactAreaCode
    use_contact_area_code: bool
    discard_record_default_absent_numbers_handling: bool
    default_contacts_import_randomization: bool
    default_email_column: str
    default_duplicate_handling: _org_pb2.DefaultDuplicateHandling
    def __init__(self, org_id: _Optional[str] = ..., default_contact_import_format: _Optional[_Union[ImportFormat, _Mapping]] = ..., use_contact_import_format: _Optional[bool] = ..., default_contact_area_code: _Optional[_Union[ContactAreaCode, _Mapping]] = ..., use_contact_area_code: _Optional[bool] = ..., discard_record_default_absent_numbers_handling: _Optional[bool] = ..., default_contacts_import_randomization: _Optional[bool] = ..., default_email_column: _Optional[str] = ..., default_duplicate_handling: _Optional[_Union[_org_pb2.DefaultDuplicateHandling, str]] = ...) -> None: ...

class ImportFormat(_message.Message):
    __slots__ = ()
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _org_pb2.StandardImportFormat
    custom: CustomImportFormat
    def __init__(self, standard: _Optional[_Union[_org_pb2.StandardImportFormat, str]] = ..., custom: _Optional[_Union[CustomImportFormat, _Mapping]] = ...) -> None: ...

class CustomImportFormat(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ContactAreaCode(_message.Message):
    __slots__ = ()
    CFD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    cfd: ContactFieldDescription
    custom: int
    def __init__(self, cfd: _Optional[_Union[ContactFieldDescription, _Mapping]] = ..., custom: _Optional[int] = ...) -> None: ...

class ContactFieldDescription(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
    id: int
    field_name: str
    is_phone: bool
    display_format_string: str
    def __init__(self, id: _Optional[int] = ..., field_name: _Optional[str] = ..., is_phone: _Optional[bool] = ..., display_format_string: _Optional[str] = ...) -> None: ...

class AuthenticationPreferences(_message.Message):
    __slots__ = ()
    class DuoMfaSettings(_message.Message):
        __slots__ = ()
        DUO_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        DUO_API_HOST_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        duo_client_id: str
        duo_api_host: str
        enabled: bool
        def __init__(self, duo_client_id: _Optional[str] = ..., duo_api_host: _Optional[str] = ..., enabled: _Optional[bool] = ...) -> None: ...
    class EmailMfaSettings(_message.Message):
        __slots__ = ()
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: _Optional[bool] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_VIA_IP_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_API_KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_2FA_FIELD_NUMBER: _ClassVar[int]
    BLOCK_UNVERIFIED_USERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MFA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DUO_MFA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FORCE_PASSWORD_RESET_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_DAY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    USER_AUTHORIZATION_VIA_IP_FIELD_NUMBER: _ClassVar[int]
    FORCE_SSO_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TOTP_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    authorization_via_ip: bool
    allowed_ips: _containers.RepeatedScalarFieldContainer[str]
    agent_api_key: str
    enable_2fa: bool
    block_unverified_users: bool
    email_mfa_settings: AuthenticationPreferences.EmailMfaSettings
    duo_mfa_settings: AuthenticationPreferences.DuoMfaSettings
    allow_force_password_reset_interval: bool
    password_reset_day_interval: int
    user_authorization_via_ip: bool
    force_sso_provider: bool
    enable_totp: bool
    def __init__(self, org_id: _Optional[str] = ..., authorization_via_ip: _Optional[bool] = ..., allowed_ips: _Optional[_Iterable[str]] = ..., agent_api_key: _Optional[str] = ..., enable_2fa: _Optional[bool] = ..., block_unverified_users: _Optional[bool] = ..., email_mfa_settings: _Optional[_Union[AuthenticationPreferences.EmailMfaSettings, _Mapping]] = ..., duo_mfa_settings: _Optional[_Union[AuthenticationPreferences.DuoMfaSettings, _Mapping]] = ..., allow_force_password_reset_interval: _Optional[bool] = ..., password_reset_day_interval: _Optional[int] = ..., user_authorization_via_ip: _Optional[bool] = ..., force_sso_provider: _Optional[bool] = ..., enable_totp: _Optional[bool] = ...) -> None: ...

class WebhookPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PUSH_URLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_RESULT_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    push_urls_enabled: bool
    call_result_push_url: str
    agent_response_push_url: str
    def __init__(self, org_id: _Optional[str] = ..., push_urls_enabled: _Optional[bool] = ..., call_result_push_url: _Optional[str] = ..., agent_response_push_url: _Optional[str] = ...) -> None: ...

class DashboardPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_VIEW_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TABLE_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_GROUPING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SMALL_ICON_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DESCENDING_SORT_FIELD_NUMBER: _ClassVar[int]
    TABLE_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_SORT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BARGE_IN_FILTERING_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_info_view: bool
    default_table_inclusion: bool
    default_info_grouping: bool
    default_small_icon: bool
    default_descending_sort: bool
    table_template_sid: int
    default_call_types: IncludedCallTypes
    default_info_sort_by_value: _org_pb2.AgentInfoSortBy
    default_barge_in_filtering: BargeInFiltering
    def __init__(self, org_id: _Optional[str] = ..., default_info_view: _Optional[bool] = ..., default_table_inclusion: _Optional[bool] = ..., default_info_grouping: _Optional[bool] = ..., default_small_icon: _Optional[bool] = ..., default_descending_sort: _Optional[bool] = ..., table_template_sid: _Optional[int] = ..., default_call_types: _Optional[_Union[IncludedCallTypes, _Mapping]] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.AgentInfoSortBy, str]] = ..., default_barge_in_filtering: _Optional[_Union[BargeInFiltering, _Mapping]] = ...) -> None: ...

class IncludedCallTypes(_message.Message):
    __slots__ = ()
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_FIELD_NUMBER: _ClassVar[int]
    outbound: bool
    inbound: bool
    manual_dial: bool
    preview_dial: bool
    def __init__(self, outbound: _Optional[bool] = ..., inbound: _Optional[bool] = ..., manual_dial: _Optional[bool] = ..., preview_dial: _Optional[bool] = ...) -> None: ...

class BargeInFiltering(_message.Message):
    __slots__ = ()
    class HuntGroup(_message.Message):
        __slots__ = ()
        ANY_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        any: bool
        hunt_group_sid: int
        def __init__(self, any: _Optional[bool] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...
    class AgentStatus(_message.Message):
        __slots__ = ()
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
        def __init__(self, any: _Optional[bool] = ..., waiting: _Optional[bool] = ..., on_call: _Optional[bool] = ..., wrap_up: _Optional[bool] = ..., paused: _Optional[bool] = ..., transfer: _Optional[bool] = ..., preview: _Optional[bool] = ..., manual: _Optional[bool] = ..., pbx: _Optional[bool] = ..., intercom: _Optional[bool] = ...) -> None: ...
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    hunt_group: BargeInFiltering.HuntGroup
    agent_status: BargeInFiltering.AgentStatus
    def __init__(self, hunt_group: _Optional[_Union[BargeInFiltering.HuntGroup, _Mapping]] = ..., agent_status: _Optional[_Union[BargeInFiltering.AgentStatus, _Mapping]] = ...) -> None: ...

class DashboardQueuePreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_VIEW_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_GROUPING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SMALL_ICON_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DESCENDING_SORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_SKILLS_FILTER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_TABLE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INFO_SORT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_info_view: bool
    default_info_grouping: bool
    default_small_icon: bool
    default_descending_sort: bool
    default_agent_skills_filter: int
    default_info_table_template: int
    default_info_sort_by_value: _org_pb2.QueueInfoSortBy
    def __init__(self, org_id: _Optional[str] = ..., default_info_view: _Optional[bool] = ..., default_info_grouping: _Optional[bool] = ..., default_small_icon: _Optional[bool] = ..., default_descending_sort: _Optional[bool] = ..., default_agent_skills_filter: _Optional[int] = ..., default_info_table_template: _Optional[int] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.QueueInfoSortBy, str]] = ...) -> None: ...

class PhonePreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
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
    org_id: str
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
    def __init__(self, org_id: _Optional[str] = ..., agent_preview_dialing: _Optional[bool] = ..., default_ring_length_threshold: _Optional[int] = ..., display_ring_length_threshold: _Optional[bool] = ..., show_caller_id: _Optional[bool] = ..., default_use_caller_id: _Optional[bool] = ..., override_linkback_recording: _Optional[bool] = ..., caller_id_cfd_sid: _Optional[int] = ..., default_dial_order: _Optional[_Union[DialOrder, _Mapping]] = ..., answering_machine_detection: _Optional[_Union[_org_preferences_pb2.AnsweringMachineDetection, str]] = ..., linkback_recording: _Optional[bool] = ...) -> None: ...

class DialOrder(_message.Message):
    __slots__ = ()
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _lms_pb2.DialOrderType
    custom: CustomDialOrder
    def __init__(self, standard: _Optional[_Union[_lms_pb2.DialOrderType, str]] = ..., custom: _Optional[_Union[CustomDialOrder, _Mapping]] = ...) -> None: ...

class CustomDialOrder(_message.Message):
    __slots__ = ()
    DIAL_ORDER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    dial_order_fields: _containers.RepeatedCompositeFieldContainer[DialOrderField]
    def __init__(self, dial_order_fields: _Optional[_Iterable[_Union[DialOrderField, _Mapping]]] = ...) -> None: ...

class DialOrderField(_message.Message):
    __slots__ = ()
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class CompliancePreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
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
    org_id: str
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
    def __init__(self, org_id: _Optional[str] = ..., display_after_hours_calls: _Optional[bool] = ..., after_hours_calls: _Optional[bool] = ..., display_natural_compliance: _Optional[bool] = ..., use_natural_compliance: _Optional[bool] = ..., default_compliance_rule_set: _Optional[str] = ..., display_cell_phone_scrub: _Optional[bool] = ..., cell_phone_scrub: _Optional[bool] = ..., display_schedule_rules: _Optional[bool] = ..., use_schedule_rules: _Optional[bool] = ..., default_schedule_rule: _Optional[_Union[ScheduleRuleField, _Mapping]] = ..., do_zip_code_scrub: _Optional[bool] = ..., zip_code_scrub: _Optional[_Union[ZipCodeField, _Mapping]] = ..., default_email_compliance_list: _Optional[str] = ..., default_sms_compliance_list: _Optional[str] = ...) -> None: ...

class ScheduleRuleField(_message.Message):
    __slots__ = ()
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    rule_id: int
    name: str
    def __init__(self, rule_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ZipCodeField(_message.Message):
    __slots__ = ()
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class BroadcastPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LIST_PENETRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DIAL_LIST_PENETRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FOLLOW_THE_SUN_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_THE_SUN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_TERMINATOR_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_TEMPLATE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    display_list_penetration_strategy: bool
    dial_list_penetration_strategy: bool
    display_follow_the_sun: bool
    follow_the_sun: bool
    sequence_terminator_override: bool
    broadcast_template_ordering: _org_preferences_pb2.BroadcastTemplateOrdering
    start_time_enabled: bool
    default_start_time: BroadcastTime
    stop_time_enabled: bool
    default_stop_time: BroadcastTime
    def __init__(self, org_id: _Optional[str] = ..., display_list_penetration_strategy: _Optional[bool] = ..., dial_list_penetration_strategy: _Optional[bool] = ..., display_follow_the_sun: _Optional[bool] = ..., follow_the_sun: _Optional[bool] = ..., sequence_terminator_override: _Optional[bool] = ..., broadcast_template_ordering: _Optional[_Union[_org_preferences_pb2.BroadcastTemplateOrdering, str]] = ..., start_time_enabled: _Optional[bool] = ..., default_start_time: _Optional[_Union[BroadcastTime, _Mapping]] = ..., stop_time_enabled: _Optional[bool] = ..., default_stop_time: _Optional[_Union[BroadcastTime, _Mapping]] = ...) -> None: ...

class BroadcastTime(_message.Message):
    __slots__ = ()
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    timezone: _org_pb2.TimeZone
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class SchedulePreferences(_message.Message):
    __slots__ = ()
    class CampaignLinksEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
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
    RESEND_CANCELLED_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
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
    resend_cancelled_campaigns: bool
    def __init__(self, org_id: _Optional[str] = ..., display_schedule_by_time_zone: _Optional[bool] = ..., use_schedule_by_time_zone: _Optional[bool] = ..., schedule_by_time_zone_scope: _Optional[_Union[_org_preferences_pb2.ScheduleByTimeZoneScope, str]] = ..., display_schedule_as_paused: _Optional[bool] = ..., schedule_as_paused: _Optional[bool] = ..., default_completion_threshold: _Optional[int] = ..., display_campaign_linking: _Optional[bool] = ..., use_campaign_linking: _Optional[bool] = ..., campaign_links: _Optional[_Mapping[str, str]] = ..., default_campaign_link_id: _Optional[str] = ..., resend_cancelled_campaigns: _Optional[bool] = ...) -> None: ...

class EmailSmsPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_LINKS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    use_custom_links: bool
    client_acknowledgement: bool
    email_from_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., use_custom_links: _Optional[bool] = ..., client_acknowledgement: _Optional[bool] = ..., email_from_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class BusinessPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    WEEKS_OF_DATA_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLIENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VISUALIZATIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    weeks_of_data: int
    time_zone: _ana_pb2.AnaTimeZone
    multi_client_access: bool
    custom_visualizations: bool
    time_filter: str
    def __init__(self, org_id: _Optional[str] = ..., weeks_of_data: _Optional[int] = ..., time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ..., multi_client_access: _Optional[bool] = ..., custom_visualizations: _Optional[bool] = ..., time_filter: _Optional[str] = ...) -> None: ...

class ScorecardsPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_USER_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    call_sample_percentage: int
    max_user_evaluations: int
    evaluation_interval: Scorecards.EvaluationInterval
    def __init__(self, org_id: _Optional[str] = ..., call_sample_percentage: _Optional[int] = ..., max_user_evaluations: _Optional[int] = ..., evaluation_interval: _Optional[_Union[Scorecards.EvaluationInterval, str]] = ...) -> None: ...

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

class VoiceAnalyticsPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REDACT_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    BILLING_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    REDACT_ALL_DIGITS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TALK_OVER_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    enabled: bool
    redact: _containers.RepeatedCompositeFieldContainer[VoiceAnalytics.Redact]
    notify: VoiceAnalytics.Notify
    billing_notify: VoiceAnalytics.Notify
    number_format: str
    redact_all_digits: bool
    silence_threshold: int
    talk_over_threshold: int
    def __init__(self, org_id: _Optional[str] = ..., enabled: _Optional[bool] = ..., redact: _Optional[_Iterable[_Union[VoiceAnalytics.Redact, _Mapping]]] = ..., notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., billing_notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., number_format: _Optional[str] = ..., redact_all_digits: _Optional[bool] = ..., silence_threshold: _Optional[int] = ..., talk_over_threshold: _Optional[int] = ...) -> None: ...

class VoiceAnalytics(_message.Message):
    __slots__ = ()
    class Redact(_message.Message):
        __slots__ = ()
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        REDACT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        number: VoiceAnalytics.Number
        redact_entity: _classifier_pb2.ClassifierEntityType
        def __init__(self, number: _Optional[_Union[VoiceAnalytics.Number, _Mapping]] = ..., redact_entity: _Optional[_Union[_classifier_pb2.ClassifierEntityType, str]] = ...) -> None: ...
    class Number(_message.Message):
        __slots__ = ()
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
        __slots__ = ()
        CRON_FIELD_NUMBER: _ClassVar[int]
        cron: str
        def __init__(self, cron: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class EndOfDayPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EOD_MONDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_TUESDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_THURSDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_FRIDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_SATURDAY_FIELD_NUMBER: _ClassVar[int]
    EOD_SUNDAY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    eod_monday: int
    eod_tuesday: int
    eod_wednesday: int
    eod_thursday: int
    eod_friday: int
    eod_saturday: int
    eod_sunday: int
    def __init__(self, org_id: _Optional[str] = ..., eod_monday: _Optional[int] = ..., eod_tuesday: _Optional[int] = ..., eod_wednesday: _Optional[int] = ..., eod_thursday: _Optional[int] = ..., eod_friday: _Optional[int] = ..., eod_saturday: _Optional[int] = ..., eod_sunday: _Optional[int] = ...) -> None: ...

class FilterPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AUTO_REPORT_FILTER_FIELD_NUMBER: _ClassVar[int]
    SEND_EMPTY_AUTO_REPORTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BROADCAST_RESEND_FILTER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BROADCAST_RESEND_FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_auto_report_filter: ReportFilter
    send_empty_auto_reports: bool
    display_broadcast_resend_filter: bool
    default_broadcast_resend_filter: ReportFilter
    def __init__(self, org_id: _Optional[str] = ..., default_auto_report_filter: _Optional[_Union[ReportFilter, _Mapping]] = ..., send_empty_auto_reports: _Optional[bool] = ..., display_broadcast_resend_filter: _Optional[bool] = ..., default_broadcast_resend_filter: _Optional[_Union[ReportFilter, _Mapping]] = ...) -> None: ...

class ReportFilter(_message.Message):
    __slots__ = ()
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _org_preferences_pb2.StandardReportFilter
    custom: int
    def __init__(self, standard: _Optional[_Union[_org_preferences_pb2.StandardReportFilter, str]] = ..., custom: _Optional[int] = ...) -> None: ...

class RecordingPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CONVENTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    ZIP_CONVENTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ZIP_FILE_NAME_CONVENTION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    convention_enabled: bool
    file_name_convention: RecordingsFileNamingConvention
    zip_convention_enabled: bool
    zip_file_name_convention: RecordingsZipFileNamingConvention
    export_file_type: _org_pb2.RecordingFileType
    def __init__(self, org_id: _Optional[str] = ..., convention_enabled: _Optional[bool] = ..., file_name_convention: _Optional[_Union[RecordingsFileNamingConvention, _Mapping]] = ..., zip_convention_enabled: _Optional[bool] = ..., zip_file_name_convention: _Optional[_Union[RecordingsZipFileNamingConvention, _Mapping]] = ..., export_file_type: _Optional[_Union[_org_pb2.RecordingFileType, str]] = ...) -> None: ...

class RecordingsFileNamingConvention(_message.Message):
    __slots__ = ()
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    inbound: FileNamingConvention
    manual: FileNamingConvention
    outbound: FileNamingConvention
    preview: FileNamingConvention
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., inbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., manual: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., outbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., preview: _Optional[_Union[FileNamingConvention, _Mapping]] = ...) -> None: ...

class RecordingsZipFileNamingConvention(_message.Message):
    __slots__ = ()
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    COMBINED_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    inbound: FileNamingConvention
    manual: FileNamingConvention
    outbound: FileNamingConvention
    combined: FileNamingConvention
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., inbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., manual: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., outbound: _Optional[_Union[FileNamingConvention, _Mapping]] = ..., combined: _Optional[_Union[FileNamingConvention, _Mapping]] = ...) -> None: ...

class FileNamingConvention(_message.Message):
    __slots__ = ()
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[FileNameSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[FileNameSegment, _Mapping]]] = ...) -> None: ...

class FileNameSegment(_message.Message):
    __slots__ = ()
    SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    segment_type: str
    format_pattern: str
    time_zone_id: str
    def __init__(self, segment_type: _Optional[str] = ..., format_pattern: _Optional[str] = ..., time_zone_id: _Optional[str] = ...) -> None: ...

class AdminClientPreferences(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
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
    org_id: str
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
    def __init__(self, org_id: _Optional[str] = ..., use_reserved_carrier: _Optional[bool] = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., email_key: _Optional[str] = ..., email_id: _Optional[str] = ..., email_name: _Optional[str] = ..., whitelist_ips: _Optional[_Iterable[str]] = ..., whitelist_domains: _Optional[_Iterable[str]] = ..., callbacks_service_id: _Optional[str] = ..., agent_screen_recording: _Optional[bool] = ..., allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ...) -> None: ...

class BusinessHours(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_HOURS_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    description: str
    business_hours_id: str
    business_hours_name: str
    timezone: _org_pb2.TimeZone
    day_intervals: _containers.RepeatedCompositeFieldContainer[DayInterval]
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., description: _Optional[str] = ..., business_hours_id: _Optional[str] = ..., business_hours_name: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., day_intervals: _Optional[_Iterable[_Union[DayInterval, _Mapping]]] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ()
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    def __init__(self, start_hour: _Optional[int] = ..., start_minute: _Optional[int] = ..., end_hour: _Optional[int] = ..., end_minute: _Optional[int] = ...) -> None: ...

class TimeOfDay(_message.Message):
    __slots__ = ()
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...

class DayInterval(_message.Message):
    __slots__ = ()
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Weekday.Enum
    start: TimeOfDay
    end: TimeOfDay
    def __init__(self, day: _Optional[_Union[_enums_pb2.Weekday.Enum, str]] = ..., start: _Optional[_Union[TimeOfDay, _Mapping]] = ..., end: _Optional[_Union[TimeOfDay, _Mapping]] = ...) -> None: ...

class MonthDayDate(_message.Message):
    __slots__ = ()
    DATE_NAME_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    date_name: str
    month: _enums_pb2.Month
    day_of_month: int
    def __init__(self, date_name: _Optional[str] = ..., month: _Optional[_Union[_enums_pb2.Month, str]] = ..., day_of_month: _Optional[int] = ...) -> None: ...

class CountryHoliday(_message.Message):
    __slots__ = ()
    HOLIDAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    holiday_name: str
    country: _country_pb2.Country
    country_name: str
    types: _containers.RepeatedScalarFieldContainer[str]
    states: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, holiday_name: _Optional[str] = ..., country: _Optional[_Union[_country_pb2.Country, str]] = ..., country_name: _Optional[str] = ..., types: _Optional[_Iterable[str]] = ..., states: _Optional[_Iterable[str]] = ...) -> None: ...

class ProgrammedDay(_message.Message):
    __slots__ = ()
    DAY_FIELD_NUMBER: _ClassVar[int]
    HOLIDAY_FIELD_NUMBER: _ClassVar[int]
    day: MonthDayDate
    holiday: CountryHoliday
    def __init__(self, day: _Optional[_Union[MonthDayDate, _Mapping]] = ..., holiday: _Optional[_Union[CountryHoliday, _Mapping]] = ...) -> None: ...

class ProgrammedDates(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMED_DATES_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    programmed_dates_id: str
    programmed_dates_name: str
    description: str
    timezone: _org_pb2.TimeZone
    days: _containers.RepeatedCompositeFieldContainer[ProgrammedDay]
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., programmed_dates_id: _Optional[str] = ..., programmed_dates_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., days: _Optional[_Iterable[_Union[ProgrammedDay, _Mapping]]] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ObservedHolidays(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_HOLIDAYS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    observed_holidays_id: str
    observed_holidays_name: str
    description: str
    timezone: _org_pb2.TimeZone
    days: _containers.RepeatedCompositeFieldContainer[ObservedHoliday]
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., observed_holidays_id: _Optional[str] = ..., observed_holidays_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., days: _Optional[_Iterable[_Union[ObservedHoliday, _Mapping]]] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ObservedHoliday(_message.Message):
    __slots__ = ()
    DAY_FIELD_NUMBER: _ClassVar[int]
    HOLIDAY_FIELD_NUMBER: _ClassVar[int]
    day: MonthDayDate
    holiday: CountryHoliday
    def __init__(self, day: _Optional[_Union[MonthDayDate, _Mapping]] = ..., holiday: _Optional[_Union[CountryHoliday, _Mapping]] = ...) -> None: ...

class CertificateInfo(_message.Message):
    __slots__ = ()
    CERTIFICATE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    certificate_info_id: str
    org_id: str
    name: str
    description: str
    hash: str
    expiration_date: _timestamp_pb2.Timestamp
    creation_date: _timestamp_pb2.Timestamp
    request_by: str
    deleted: bool
    revoked: bool
    def __init__(self, certificate_info_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., hash: _Optional[str] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., creation_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., request_by: _Optional[str] = ..., deleted: _Optional[bool] = ..., revoked: _Optional[bool] = ...) -> None: ...
