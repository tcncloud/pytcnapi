from api.commons import ana_pb2 as _ana_pb2
from api.commons import country_pb2 as _country_pb2
from api.commons import lms_pb2 as _lms_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import org_preferences_pb2 as _org_preferences_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationPreferences(_message.Message):
    __slots__ = ["org_id", "default_country", "time_zone", "display_language"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    default_country: _country_pb2.Country
    time_zone: _org_pb2.TimeZone
    display_language: _org_pb2.DisplayLanguage
    def __init__(self, org_id: _Optional[str] = ..., default_country: _Optional[_Union[_country_pb2.Country, str]] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., display_language: _Optional[_Union[_org_pb2.DisplayLanguage, str]] = ...) -> None: ...

class AgentPreferences(_message.Message):
    __slots__ = ["org_id", "default_agent_dial_in", "pbx_extension_length", "default_softphone_volume_in", "default_softphone_volume_out", "config_dial_in_numbers", "client_dial_in_numbers", "manual_dial_caller_id_privacy", "use_manual_dial_caller_id_privacy"]
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
    def __init__(self, org_id: _Optional[str] = ..., default_agent_dial_in: _Optional[str] = ..., pbx_extension_length: _Optional[int] = ..., default_softphone_volume_in: _Optional[int] = ..., default_softphone_volume_out: _Optional[int] = ..., config_dial_in_numbers: _Optional[_Iterable[str]] = ..., client_dial_in_numbers: _Optional[_Iterable[str]] = ..., manual_dial_caller_id_privacy: bool = ..., use_manual_dial_caller_id_privacy: bool = ...) -> None: ...

class ContactPreferences(_message.Message):
    __slots__ = ["org_id", "default_contact_import_format", "use_contact_import_format", "default_contact_area_code", "use_contact_area_code", "discard_record_default_absent_numbers_handling", "default_contacts_import_randomization", "default_email_column", "default_duplicate_handling"]
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
    def __init__(self, org_id: _Optional[str] = ..., default_contact_import_format: _Optional[_Union[ImportFormat, _Mapping]] = ..., use_contact_import_format: bool = ..., default_contact_area_code: _Optional[_Union[ContactAreaCode, _Mapping]] = ..., use_contact_area_code: bool = ..., discard_record_default_absent_numbers_handling: bool = ..., default_contacts_import_randomization: bool = ..., default_email_column: _Optional[str] = ..., default_duplicate_handling: _Optional[_Union[_org_pb2.DefaultDuplicateHandling, str]] = ...) -> None: ...

class ImportFormat(_message.Message):
    __slots__ = ["standard", "custom"]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _org_pb2.StandardImportFormat
    custom: CustomImportFormat
    def __init__(self, standard: _Optional[_Union[_org_pb2.StandardImportFormat, str]] = ..., custom: _Optional[_Union[CustomImportFormat, _Mapping]] = ...) -> None: ...

class CustomImportFormat(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ContactAreaCode(_message.Message):
    __slots__ = ["cfd", "custom"]
    CFD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    cfd: ContactFieldDescription
    custom: int
    def __init__(self, cfd: _Optional[_Union[ContactFieldDescription, _Mapping]] = ..., custom: _Optional[int] = ...) -> None: ...

class ContactFieldDescription(_message.Message):
    __slots__ = ["id", "field_name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    field_name: str
    def __init__(self, id: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class AuthenticationPreferences(_message.Message):
    __slots__ = ["org_id", "authorization_via_ip", "allowed_ips", "agent_api_key"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_VIA_IP_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_API_KEY_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    authorization_via_ip: bool
    allowed_ips: _containers.RepeatedScalarFieldContainer[str]
    agent_api_key: str
    def __init__(self, org_id: _Optional[str] = ..., authorization_via_ip: bool = ..., allowed_ips: _Optional[_Iterable[str]] = ..., agent_api_key: _Optional[str] = ...) -> None: ...

class WebhookPreferences(_message.Message):
    __slots__ = ["org_id", "push_urls_enabled", "call_result_push_url", "agent_response_push_url"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PUSH_URLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_RESULT_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    push_urls_enabled: bool
    call_result_push_url: str
    agent_response_push_url: str
    def __init__(self, org_id: _Optional[str] = ..., push_urls_enabled: bool = ..., call_result_push_url: _Optional[str] = ..., agent_response_push_url: _Optional[str] = ...) -> None: ...

class DashboardPreferences(_message.Message):
    __slots__ = ["org_id", "default_info_view", "default_table_inclusion", "default_info_grouping", "default_small_icon", "default_descending_sort", "table_template_sid", "default_call_types", "default_info_sort_by_value", "default_barge_in_filtering"]
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
    def __init__(self, org_id: _Optional[str] = ..., default_info_view: bool = ..., default_table_inclusion: bool = ..., default_info_grouping: bool = ..., default_small_icon: bool = ..., default_descending_sort: bool = ..., table_template_sid: _Optional[int] = ..., default_call_types: _Optional[_Union[IncludedCallTypes, _Mapping]] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.AgentInfoSortBy, str]] = ..., default_barge_in_filtering: _Optional[_Union[BargeInFiltering, _Mapping]] = ...) -> None: ...

class IncludedCallTypes(_message.Message):
    __slots__ = ["outbound", "inbound", "manual_dial", "preview_dial"]
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
    __slots__ = ["hunt_group", "agent_status"]
    class HuntGroup(_message.Message):
        __slots__ = ["any", "hunt_group_sid"]
        ANY_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        any: bool
        hunt_group_sid: int
        def __init__(self, any: bool = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...
    class AgentStatus(_message.Message):
        __slots__ = ["any", "waiting", "on_call", "wrap_up", "paused", "transfer", "preview", "manual", "pbx", "intercom"]
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

class DashboardQueuePreferences(_message.Message):
    __slots__ = ["org_id", "default_info_view", "default_info_grouping", "default_small_icon", "default_descending_sort", "default_agent_skills_filter", "default_info_table_template", "default_info_sort_by_value"]
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
    def __init__(self, org_id: _Optional[str] = ..., default_info_view: bool = ..., default_info_grouping: bool = ..., default_small_icon: bool = ..., default_descending_sort: bool = ..., default_agent_skills_filter: _Optional[int] = ..., default_info_table_template: _Optional[int] = ..., default_info_sort_by_value: _Optional[_Union[_org_pb2.QueueInfoSortBy, str]] = ...) -> None: ...

class PhonePreferences(_message.Message):
    __slots__ = ["org_id", "agent_preview_dialing", "default_ring_length_threshold", "display_ring_length_threshold", "show_caller_id", "default_use_caller_id", "override_linkback_recording", "caller_id_cfd_sid", "default_dial_order", "answering_machine_detection", "linkback_recording"]
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
    def __init__(self, org_id: _Optional[str] = ..., agent_preview_dialing: bool = ..., default_ring_length_threshold: _Optional[int] = ..., display_ring_length_threshold: bool = ..., show_caller_id: bool = ..., default_use_caller_id: bool = ..., override_linkback_recording: bool = ..., caller_id_cfd_sid: _Optional[int] = ..., default_dial_order: _Optional[_Union[DialOrder, _Mapping]] = ..., answering_machine_detection: _Optional[_Union[_org_preferences_pb2.AnsweringMachineDetection, str]] = ..., linkback_recording: bool = ...) -> None: ...

class DialOrder(_message.Message):
    __slots__ = ["standard", "custom"]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _lms_pb2.DialOrderType
    custom: CustomDialOrder
    def __init__(self, standard: _Optional[_Union[_lms_pb2.DialOrderType, str]] = ..., custom: _Optional[_Union[CustomDialOrder, _Mapping]] = ...) -> None: ...

class CustomDialOrder(_message.Message):
    __slots__ = ["dial_order_fields"]
    DIAL_ORDER_FIELDS_FIELD_NUMBER: _ClassVar[int]
    dial_order_fields: _containers.RepeatedCompositeFieldContainer[DialOrderField]
    def __init__(self, dial_order_fields: _Optional[_Iterable[_Union[DialOrderField, _Mapping]]] = ...) -> None: ...

class DialOrderField(_message.Message):
    __slots__ = ["cfd_sid", "field_name"]
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class CompliancePreferences(_message.Message):
    __slots__ = ["org_id", "display_after_hours_calls", "after_hours_calls", "display_natural_compliance", "use_natural_compliance", "default_compliance_rule_set", "display_cell_phone_scrub", "cell_phone_scrub", "display_schedule_rules", "use_schedule_rules", "default_schedule_rule", "do_zip_code_scrub", "zip_code_scrub", "default_email_compliance_list", "default_sms_compliance_list"]
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
    def __init__(self, org_id: _Optional[str] = ..., display_after_hours_calls: bool = ..., after_hours_calls: bool = ..., display_natural_compliance: bool = ..., use_natural_compliance: bool = ..., default_compliance_rule_set: _Optional[str] = ..., display_cell_phone_scrub: bool = ..., cell_phone_scrub: bool = ..., display_schedule_rules: bool = ..., use_schedule_rules: bool = ..., default_schedule_rule: _Optional[_Union[ScheduleRuleField, _Mapping]] = ..., do_zip_code_scrub: bool = ..., zip_code_scrub: _Optional[_Union[ZipCodeField, _Mapping]] = ..., default_email_compliance_list: _Optional[str] = ..., default_sms_compliance_list: _Optional[str] = ...) -> None: ...

class ScheduleRuleField(_message.Message):
    __slots__ = ["rule_id", "name"]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    rule_id: int
    name: str
    def __init__(self, rule_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ZipCodeField(_message.Message):
    __slots__ = ["cfd_sid", "field_name"]
    CFD_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    cfd_sid: int
    field_name: str
    def __init__(self, cfd_sid: _Optional[int] = ..., field_name: _Optional[str] = ...) -> None: ...

class BroadcastPreferences(_message.Message):
    __slots__ = ["org_id", "display_list_penetration_strategy", "dial_list_penetration_strategy", "display_follow_the_sun", "follow_the_sun", "sequence_terminator_override", "broadcast_template_ordering", "start_time_enabled", "default_start_time", "stop_time_enabled", "default_stop_time"]
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
    def __init__(self, org_id: _Optional[str] = ..., display_list_penetration_strategy: bool = ..., dial_list_penetration_strategy: bool = ..., display_follow_the_sun: bool = ..., follow_the_sun: bool = ..., sequence_terminator_override: bool = ..., broadcast_template_ordering: _Optional[_Union[_org_preferences_pb2.BroadcastTemplateOrdering, str]] = ..., start_time_enabled: bool = ..., default_start_time: _Optional[_Union[BroadcastTime, _Mapping]] = ..., stop_time_enabled: bool = ..., default_stop_time: _Optional[_Union[BroadcastTime, _Mapping]] = ...) -> None: ...

class BroadcastTime(_message.Message):
    __slots__ = ["hours", "minutes", "timezone"]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    hours: int
    minutes: int
    timezone: _org_pb2.TimeZone
    def __init__(self, hours: _Optional[int] = ..., minutes: _Optional[int] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class SchedulePreferences(_message.Message):
    __slots__ = ["org_id", "display_schedule_by_time_zone", "use_schedule_by_time_zone", "schedule_by_time_zone_scope", "display_schedule_as_paused", "schedule_as_paused", "default_completion_threshold", "display_campaign_linking", "use_campaign_linking", "campaign_links", "default_campaign_link_id"]
    class CampaignLinksEntry(_message.Message):
        __slots__ = ["key", "value"]
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
    def __init__(self, org_id: _Optional[str] = ..., display_schedule_by_time_zone: bool = ..., use_schedule_by_time_zone: bool = ..., schedule_by_time_zone_scope: _Optional[_Union[_org_preferences_pb2.ScheduleByTimeZoneScope, str]] = ..., display_schedule_as_paused: bool = ..., schedule_as_paused: bool = ..., default_completion_threshold: _Optional[int] = ..., display_campaign_linking: bool = ..., use_campaign_linking: bool = ..., campaign_links: _Optional[_Mapping[str, str]] = ..., default_campaign_link_id: _Optional[str] = ...) -> None: ...

class EmailSmsPreferences(_message.Message):
    __slots__ = ["org_id", "use_custom_links", "client_acknowledgement", "email_from_addresses"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_LINKS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    use_custom_links: bool
    client_acknowledgement: bool
    email_from_addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., use_custom_links: bool = ..., client_acknowledgement: bool = ..., email_from_addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class BusinessPreferences(_message.Message):
    __slots__ = ["org_id", "weeks_of_data", "time_zone", "multi_client_access", "custom_visualizations", "time_filter"]
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
    def __init__(self, org_id: _Optional[str] = ..., weeks_of_data: _Optional[int] = ..., time_zone: _Optional[_Union[_ana_pb2.AnaTimeZone, str]] = ..., multi_client_access: bool = ..., custom_visualizations: bool = ..., time_filter: _Optional[str] = ...) -> None: ...

class ScorecardsPreferences(_message.Message):
    __slots__ = ["org_id", "call_sample_percentage", "max_user_evaluations", "evaluation_interval"]
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
    __slots__ = []
    class EvaluationInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        EVALUATION_INTERVAL_DAY_UNSPECIFIED: _ClassVar[Scorecards.EvaluationInterval]
        EVALUATION_INTERVAL_WEEK: _ClassVar[Scorecards.EvaluationInterval]
        EVALUATION_INTERVAL_MONTH: _ClassVar[Scorecards.EvaluationInterval]
    EVALUATION_INTERVAL_DAY_UNSPECIFIED: Scorecards.EvaluationInterval
    EVALUATION_INTERVAL_WEEK: Scorecards.EvaluationInterval
    EVALUATION_INTERVAL_MONTH: Scorecards.EvaluationInterval
    def __init__(self) -> None: ...

class VoiceAnalyticsPreferences(_message.Message):
    __slots__ = ["org_id", "enabled", "redact", "notify", "billing_notify", "number_format", "redact_all_digits", "silence_threshold", "talk_over_threshold"]
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
    def __init__(self, org_id: _Optional[str] = ..., enabled: bool = ..., redact: _Optional[_Iterable[_Union[VoiceAnalytics.Redact, _Mapping]]] = ..., notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., billing_notify: _Optional[_Union[VoiceAnalytics.Notify, _Mapping]] = ..., number_format: _Optional[str] = ..., redact_all_digits: bool = ..., silence_threshold: _Optional[int] = ..., talk_over_threshold: _Optional[int] = ...) -> None: ...

class VoiceAnalytics(_message.Message):
    __slots__ = []
    class Redact(_message.Message):
        __slots__ = ["number"]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        number: VoiceAnalytics.Number
        def __init__(self, number: _Optional[_Union[VoiceAnalytics.Number, _Mapping]] = ...) -> None: ...
    class Number(_message.Message):
        __slots__ = ["kind", "min_consecutive", "max_consecutive", "slop"]
        class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
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
        __slots__ = ["cron"]
        CRON_FIELD_NUMBER: _ClassVar[int]
        cron: str
        def __init__(self, cron: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class EndOfDayPreferences(_message.Message):
    __slots__ = ["org_id", "eod_monday", "eod_tuesday", "eod_wednesday", "eod_thursday", "eod_friday", "eod_saturday", "eod_sunday"]
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
    __slots__ = ["org_id", "default_auto_report_filter", "send_empty_auto_reports", "display_broadcast_resend_filter", "default_broadcast_resend_filter"]
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
    def __init__(self, org_id: _Optional[str] = ..., default_auto_report_filter: _Optional[_Union[ReportFilter, _Mapping]] = ..., send_empty_auto_reports: bool = ..., display_broadcast_resend_filter: bool = ..., default_broadcast_resend_filter: _Optional[_Union[ReportFilter, _Mapping]] = ...) -> None: ...

class ReportFilter(_message.Message):
    __slots__ = ["standard", "custom"]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    standard: _org_preferences_pb2.StandardReportFilter
    custom: int
    def __init__(self, standard: _Optional[_Union[_org_preferences_pb2.StandardReportFilter, str]] = ..., custom: _Optional[int] = ...) -> None: ...

class RecordingPreferences(_message.Message):
    __slots__ = ["org_id", "convention_enabled", "file_name_convention", "zip_convention_enabled", "zip_file_name_convention", "export_file_type"]
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
    def __init__(self, org_id: _Optional[str] = ..., convention_enabled: bool = ..., file_name_convention: _Optional[_Union[RecordingsFileNamingConvention, _Mapping]] = ..., zip_convention_enabled: bool = ..., zip_file_name_convention: _Optional[_Union[RecordingsZipFileNamingConvention, _Mapping]] = ..., export_file_type: _Optional[_Union[_org_pb2.RecordingFileType, str]] = ...) -> None: ...

class RecordingsFileNamingConvention(_message.Message):
    __slots__ = ["xml_client_property_sid", "inbound", "manual", "outbound", "preview"]
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
    __slots__ = ["xml_client_property_sid", "inbound", "manual", "outbound", "combined"]
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
    __slots__ = ["segments"]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[FileNameSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[FileNameSegment, _Mapping]]] = ...) -> None: ...

class FileNameSegment(_message.Message):
    __slots__ = ["segment_type", "format_pattern", "time_zone_id"]
    SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    segment_type: str
    format_pattern: str
    time_zone_id: str
    def __init__(self, segment_type: _Optional[str] = ..., format_pattern: _Optional[str] = ..., time_zone_id: _Optional[str] = ...) -> None: ...

class AdminClientPreferences(_message.Message):
    __slots__ = ["org_id", "use_reserved_carrier", "reserved_carriers", "email_key", "email_id", "email_name", "whitelist_ips", "whitelist_domains", "callbacks_service_id", "agent_screen_recording", "allowed_countries"]
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
    def __init__(self, org_id: _Optional[str] = ..., use_reserved_carrier: bool = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., email_key: _Optional[str] = ..., email_id: _Optional[str] = ..., email_name: _Optional[str] = ..., whitelist_ips: _Optional[_Iterable[str]] = ..., whitelist_domains: _Optional[_Iterable[str]] = ..., callbacks_service_id: _Optional[str] = ..., agent_screen_recording: bool = ..., allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ...) -> None: ...
