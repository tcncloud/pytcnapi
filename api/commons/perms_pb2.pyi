from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NO_PERMISSION: _ClassVar[Permission]
    VIEW_LIST_MANAGER: _ClassVar[Permission]
    CREATE_LIST_MANAGER: _ClassVar[Permission]
    EDIT_LIST_MANAGER: _ClassVar[Permission]
    DELETE_LIST_MANAGER: _ClassVar[Permission]
    EXECUTE_LIST_MANAGER: _ClassVar[Permission]
    VIEW_FIELD_DEFINITIONS: _ClassVar[Permission]
    CREATE_FIELD_DEFINITIONS: _ClassVar[Permission]
    EDIT_FIELD_DEFINITIONS: _ClassVar[Permission]
    DELETE_FIELD_DEFINITIONS: _ClassVar[Permission]
    EXECUTE_FIELD_DEFINITIONS: _ClassVar[Permission]
    VIEW_IMPORT_TEMPLATES: _ClassVar[Permission]
    CREATE_IMPORT_TEMPLATES: _ClassVar[Permission]
    EDIT_IMPORT_TEMPLATES: _ClassVar[Permission]
    DELETE_IMPORT_TEMPLATES: _ClassVar[Permission]
    EXECUTE_IMPORT_TEMPLATES: _ClassVar[Permission]
    VIEW_ADMIN_TOOLS: _ClassVar[Permission]
    CREATE_ADMIN_TOOLS: _ClassVar[Permission]
    EDIT_ADMIN_TOOLS: _ClassVar[Permission]
    DELETE_ADMIN_TOOLS: _ClassVar[Permission]
    EXECUTE_ADMIN_TOOLS: _ClassVar[Permission]
    VIEW_COUNTRY_MANAGER: _ClassVar[Permission]
    CREATE_COUNTRY_MANAGER: _ClassVar[Permission]
    EDIT_COUNTRY_MANAGER: _ClassVar[Permission]
    DELETE_COUNTRY_MANAGER: _ClassVar[Permission]
    EXECUTE_COUNTRY_MANAGER: _ClassVar[Permission]
    VIEW_DIAL_REGION_GROUPS: _ClassVar[Permission]
    CREATE_DIAL_REGION_GROUPS: _ClassVar[Permission]
    EDIT_DIAL_REGION_GROUPS: _ClassVar[Permission]
    DELETE_DIAL_REGION_GROUPS: _ClassVar[Permission]
    EXECUTE_DIAL_REGION_GROUPS: _ClassVar[Permission]
    VIEW_DIAL_REGION: _ClassVar[Permission]
    CREATE_DIAL_REGION: _ClassVar[Permission]
    EDIT_DIAL_REGION: _ClassVar[Permission]
    DELETE_DIAL_REGION: _ClassVar[Permission]
    EXECUTE_DIAL_REGION: _ClassVar[Permission]
    VIEW_TTS_MANAGER: _ClassVar[Permission]
    CREATE_TTS_MANAGER: _ClassVar[Permission]
    EDIT_TTS_MANAGER: _ClassVar[Permission]
    DELETE_TTS_MANAGER: _ClassVar[Permission]
    EXECUTE_TTS_MANAGER: _ClassVar[Permission]
    VIEW_USER_MANAGEMENT: _ClassVar[Permission]
    CREATE_USER_MANAGEMENT: _ClassVar[Permission]
    EDIT_USER_MANAGEMENT: _ClassVar[Permission]
    DELETE_USER_MANAGEMENT: _ClassVar[Permission]
    EXECUTE_USER_MANAGEMENT: _ClassVar[Permission]
    VIEW_CLIENT: _ClassVar[Permission]
    CREATE_CLIENT: _ClassVar[Permission]
    EDIT_CLIENT: _ClassVar[Permission]
    DELETE_CLIENT: _ClassVar[Permission]
    EXECUTE_CLIENT: _ClassVar[Permission]
    VIEW_LOGIN: _ClassVar[Permission]
    CREATE_LOGIN: _ClassVar[Permission]
    EDIT_LOGIN: _ClassVar[Permission]
    DELETE_LOGIN: _ClassVar[Permission]
    EXECUTE_LOGIN: _ClassVar[Permission]
    VIEW_PERMISSIONS: _ClassVar[Permission]
    CREATE_PERMISSIONS: _ClassVar[Permission]
    EDIT_PERMISSIONS: _ClassVar[Permission]
    DELETE_PERMISSIONS: _ClassVar[Permission]
    EXECUTE_PERMISSIONS: _ClassVar[Permission]
    VIEW_PERMISSIONS_GROUPS: _ClassVar[Permission]
    CREATE_PERMISSIONS_GROUPS: _ClassVar[Permission]
    EDIT_PERMISSIONS_GROUPS: _ClassVar[Permission]
    DELETE_PERMISSIONS_GROUPS: _ClassVar[Permission]
    EXECUTE_PERMISSIONS_GROUPS: _ClassVar[Permission]
    VIEW_PERMISSIONS_GROUP_ADMINISTRATOR: _ClassVar[Permission]
    CREATE_PERMISSIONS_GROUP_ADMINISTRATOR: _ClassVar[Permission]
    EDIT_PERMISSIONS_GROUP_ADMINISTRATOR: _ClassVar[Permission]
    DELETE_PERMISSIONS_GROUP_ADMINISTRATOR: _ClassVar[Permission]
    EXECUTE_PERMISSIONS_GROUP_ADMINISTRATOR: _ClassVar[Permission]
    VIEW_CONTACT_US: _ClassVar[Permission]
    CREATE_CONTACT_US: _ClassVar[Permission]
    EDIT_CONTACT_US: _ClassVar[Permission]
    DELETE_CONTACT_US: _ClassVar[Permission]
    EXECUTE_CONTACT_US: _ClassVar[Permission]
    VIEW_USER_OPTIONS: _ClassVar[Permission]
    CREATE_USER_OPTIONS: _ClassVar[Permission]
    EDIT_USER_OPTIONS: _ClassVar[Permission]
    DELETE_USER_OPTIONS: _ClassVar[Permission]
    EXECUTE_USER_OPTIONS: _ClassVar[Permission]
    VIEW_CHANGE_PASSWORD: _ClassVar[Permission]
    CREATE_CHANGE_PASSWORD: _ClassVar[Permission]
    EDIT_CHANGE_PASSWORD: _ClassVar[Permission]
    DELETE_CHANGE_PASSWORD: _ClassVar[Permission]
    EXECUTE_CHANGE_PASSWORD: _ClassVar[Permission]
    VIEW_PREFERENCES: _ClassVar[Permission]
    CREATE_PREFERENCES: _ClassVar[Permission]
    EDIT_PREFERENCES: _ClassVar[Permission]
    DELETE_PREFERENCES: _ClassVar[Permission]
    EXECUTE_PREFERENCES: _ClassVar[Permission]
    VIEW_WEB_BROADCASTING: _ClassVar[Permission]
    CREATE_WEB_BROADCASTING: _ClassVar[Permission]
    EDIT_WEB_BROADCASTING: _ClassVar[Permission]
    DELETE_WEB_BROADCASTING: _ClassVar[Permission]
    EXECUTE_WEB_BROADCASTING: _ClassVar[Permission]
    VIEW_REPORTS: _ClassVar[Permission]
    CREATE_REPORTS: _ClassVar[Permission]
    EDIT_REPORTS: _ClassVar[Permission]
    DELETE_REPORTS: _ClassVar[Permission]
    EXECUTE_REPORTS: _ClassVar[Permission]
    VIEW_SEND_BROADCAST: _ClassVar[Permission]
    CREATE_SEND_BROADCAST: _ClassVar[Permission]
    EDIT_SEND_BROADCAST: _ClassVar[Permission]
    DELETE_SEND_BROADCAST: _ClassVar[Permission]
    EXECUTE_SEND_BROADCAST: _ClassVar[Permission]
    VIEW_MESSAGE_MANAGER: _ClassVar[Permission]
    CREATE_MESSAGE_MANAGER: _ClassVar[Permission]
    EDIT_MESSAGE_MANAGER: _ClassVar[Permission]
    DELETE_MESSAGE_MANAGER: _ClassVar[Permission]
    EXECUTE_MESSAGE_MANAGER: _ClassVar[Permission]
    VIEW_TEMPLATE_MANAGER: _ClassVar[Permission]
    CREATE_TEMPLATE_MANAGER: _ClassVar[Permission]
    EDIT_TEMPLATE_MANAGER: _ClassVar[Permission]
    DELETE_TEMPLATE_MANAGER: _ClassVar[Permission]
    EXECUTE_TEMPLATE_MANAGER: _ClassVar[Permission]
    VIEW_DO_NOT_CALL_LIST: _ClassVar[Permission]
    CREATE_DO_NOT_CALL_LIST: _ClassVar[Permission]
    EDIT_DO_NOT_CALL_LIST: _ClassVar[Permission]
    DELETE_DO_NOT_CALL_LIST: _ClassVar[Permission]
    EXECUTE_DO_NOT_CALL_LIST: _ClassVar[Permission]
    VIEW_SCHEDULE_RULES: _ClassVar[Permission]
    CREATE_SCHEDULE_RULES: _ClassVar[Permission]
    EDIT_SCHEDULE_RULES: _ClassVar[Permission]
    DELETE_SCHEDULE_RULES: _ClassVar[Permission]
    EXECUTE_SCHEDULE_RULES: _ClassVar[Permission]
    VIEW_BILLING: _ClassVar[Permission]
    CREATE_BILLING: _ClassVar[Permission]
    EDIT_BILLING: _ClassVar[Permission]
    DELETE_BILLING: _ClassVar[Permission]
    EXECUTE_BILLING: _ClassVar[Permission]
    VIEW_SAP_EXPORT: _ClassVar[Permission]
    CREATE_SAP_EXPORT: _ClassVar[Permission]
    EDIT_SAP_EXPORT: _ClassVar[Permission]
    DELETE_SAP_EXPORT: _ClassVar[Permission]
    EXECUTE_SAP_EXPORT: _ClassVar[Permission]
    VIEW_AUDIT: _ClassVar[Permission]
    CREATE_AUDIT: _ClassVar[Permission]
    EDIT_AUDIT: _ClassVar[Permission]
    DELETE_AUDIT: _ClassVar[Permission]
    EXECUTE_AUDIT: _ClassVar[Permission]
    VIEW_AUTOMATED_REPORTING: _ClassVar[Permission]
    CREATE_AUTOMATED_REPORTING: _ClassVar[Permission]
    EDIT_AUTOMATED_REPORTING: _ClassVar[Permission]
    DELETE_AUTOMATED_REPORTING: _ClassVar[Permission]
    EXECUTE_AUTOMATED_REPORTING: _ClassVar[Permission]
    VIEW_CUSTOMER_SERVICE: _ClassVar[Permission]
    CREATE_CUSTOMER_SERVICE: _ClassVar[Permission]
    EDIT_CUSTOMER_SERVICE: _ClassVar[Permission]
    DELETE_CUSTOMER_SERVICE: _ClassVar[Permission]
    EXECUTE_CUSTOMER_SERVICE: _ClassVar[Permission]
    VIEW_SCRIPTS: _ClassVar[Permission]
    CREATE_SCRIPTS: _ClassVar[Permission]
    EDIT_SCRIPTS: _ClassVar[Permission]
    DELETE_SCRIPTS: _ClassVar[Permission]
    EXECUTE_SCRIPTS: _ClassVar[Permission]
    VIEW_CLIENT_PREFERENCES: _ClassVar[Permission]
    CREATE_CLIENT_PREFERENCES: _ClassVar[Permission]
    EDIT_CLIENT_PREFERENCES: _ClassVar[Permission]
    DELETE_CLIENT_PREFERENCES: _ClassVar[Permission]
    EXECUTE_CLIENT_PREFERENCES: _ClassVar[Permission]
    VIEW_RECORDINGS_REPORTING: _ClassVar[Permission]
    CREATE_RECORDINGS_REPORTING: _ClassVar[Permission]
    EDIT_RECORDINGS_REPORTING: _ClassVar[Permission]
    DELETE_RECORDINGS_REPORTING: _ClassVar[Permission]
    EXECUTE_RECORDINGS_REPORTING: _ClassVar[Permission]
    VIEW_DEBUG_MODE: _ClassVar[Permission]
    CREATE_DEBUG_MODE: _ClassVar[Permission]
    EDIT_DEBUG_MODE: _ClassVar[Permission]
    DELETE_DEBUG_MODE: _ClassVar[Permission]
    EXECUTE_DEBUG_MODE: _ClassVar[Permission]
    CREATE_DNCL_MAP: _ClassVar[Permission]
    VIEW_DNCL_MAP: _ClassVar[Permission]
    EXECUTE_COPY_DOWN: _ClassVar[Permission]
    VIEW_AGENTS: _ClassVar[Permission]
    VIEW_ADMIN_CUSTOMER_SERVICE: _ClassVar[Permission]
    EDIT_AGENTS: _ClassVar[Permission]
    DELETE_AGENTS: _ClassVar[Permission]
    EXECUTE_AGENTS: _ClassVar[Permission]
    EDIT_HUNT_GROUP: _ClassVar[Permission]
    DELETE_HUNT_GROUP: _ClassVar[Permission]
    EXECUTE_HUNT_GROUP: _ClassVar[Permission]
    VIEW_HUNT_GROUP: _ClassVar[Permission]
    VIEW_AGENTS_REPORT: _ClassVar[Permission]
    VIEW_AGENTS_DASHBOARD: _ClassVar[Permission]
    VIEW_CALLER_ID_BUCKETS: _ClassVar[Permission]
    EDIT_CALLER_ID_BUCKETS: _ClassVar[Permission]
    CREATE_CALLER_ID_BUCKETS: _ClassVar[Permission]
    DELETE_CALLER_ID_BUCKETS: _ClassVar[Permission]
    EXECUTE_CALLER_ID_BUCKETS: _ClassVar[Permission]
    VIEW_REPORT_REQUEST: _ClassVar[Permission]
    CREATE_REPORT_REQUEST: _ClassVar[Permission]
    VIEW_INBOUND_SCRIPTS: _ClassVar[Permission]
    EDIT_INBOUND_SCRIPTS: _ClassVar[Permission]
    CREATE_INBOUND_SCRIPTS: _ClassVar[Permission]
    DELETE_INBOUND_SCRIPTS: _ClassVar[Permission]
    EDIT_BACKOFFICE_THEME: _ClassVar[Permission]
    CREATE_PHONE_NUMBER_MANAGEMENT: _ClassVar[Permission]
    EDIT_PHONE_NUMBER_MANAGEMENT: _ClassVar[Permission]
    VIEW_PHONE_NUMBER_MANAGEMENT: _ClassVar[Permission]
    DELETE_PHONE_NUMBER_MANAGEMENT: _ClassVar[Permission]
    EXECUTE_PHONE_NUMBER_MANAGEMENT: _ClassVar[Permission]
    EXECUTE_INBOUND_SCRIPTS: _ClassVar[Permission]
    EXECUTE_CELL_PHONE_SCRUB: _ClassVar[Permission]
    EDIT_ADMIN_CLIENT_PREFERENCES: _ClassVar[Permission]
    VIEW_ONTARIO_SYSTEMS_ADMINISTRATOR: _ClassVar[Permission]
    EXECUTE_ONTARIO_SYSTEMS_ADMINISTRATOR: _ClassVar[Permission]
    EXECUTE_ONTARIO_SYSTEMS_USER: _ClassVar[Permission]
    VIEW_INTEGRATION_MESSAGES: _ClassVar[Permission]
    VIEW_ONTARIO_SYSTEMS_USER: _ClassVar[Permission]
    EXECUTE_BROADCAST_CONTROL_INBOUND: _ClassVar[Permission]
    EXECUTE_BROADCAST_CONTROL_MANUAL: _ClassVar[Permission]
    EXECUTE_BROADCAST_CONTROL_OUTBOUND: _ClassVar[Permission]
    CREATE_PREVIEW_ONLY_TEMPLATES: _ClassVar[Permission]
    CREATE_MAC_ONLY_TEMPLATES: _ClassVar[Permission]
    EDIT_TRIGGER_ADVANCE_ON_CALL: _ClassVar[Permission]
    CREATE_TRIGGER_ADVANCE_ON_CALL: _ClassVar[Permission]
    DELETE_MAC_ONLY_TEMPLATES: _ClassVar[Permission]
    EXECUTE_MAC_ONLY_TEMPLATES: _ClassVar[Permission]
    VIEW_MAC_ONLY_TEMPLATES: _ClassVar[Permission]
    EDIT_MAC_ONLY_TEMPLATES: _ClassVar[Permission]
    EXECUTE_PREVIEW_ONLY_TEMPLATES: _ClassVar[Permission]
    VIEW_PREVIEW_ONLY_TEMPLATES: _ClassVar[Permission]
    EDIT_PREVIEW_ONLY_TEMPLATES: _ClassVar[Permission]
    DELETE_PREVIEW_ONLY_TEMPLATES: _ClassVar[Permission]
    VIEW_ANALYTICS_REPORTING: _ClassVar[Permission]
    CREATE_HUNT_GROUP: _ClassVar[Permission]
    CREATE_AGENTS: _ClassVar[Permission]
    CREATE_AGENTS_DASHBOARD: _ClassVar[Permission]
    CREATE_AGENTS_REPORT: _ClassVar[Permission]
    DELETE_AGENTS_DASHBOARD: _ClassVar[Permission]
    DELETE_AGENTS_REPORT: _ClassVar[Permission]
    EDIT_AGENTS_DASHBOARD: _ClassVar[Permission]
    EDIT_AGENTS_REPORT: _ClassVar[Permission]
    EXECUTE_AGENTS_DASHBOARD: _ClassVar[Permission]
    EXECUTE_AGENTS_REPORT: _ClassVar[Permission]
    DELETE_TRIGGER_ADVANCE_ON_CALL: _ClassVar[Permission]
    DELETE_CELL_PHONE_SCRUB: _ClassVar[Permission]
    CREATE_RINGLESS_VOICEMAIL_TEMPLATES: _ClassVar[Permission]
    EDIT_RINGLESS_VOICEMAIL_TEMPLATES: _ClassVar[Permission]
    CREATE_VOCALDIRECT_TEMPLATES: _ClassVar[Permission]
    EDIT_VOCALDIRECT_TEMPLATES: _ClassVar[Permission]
    VIEW_EMAIL: _ClassVar[Permission]
    VIEW_SMS: _ClassVar[Permission]
    VIEW_EMAIL_REPORTS: _ClassVar[Permission]
    VIEW_EMAIL_AUDIT: _ClassVar[Permission]
    VIEW_SMS_REPORTS: _ClassVar[Permission]
    VIEW_SMS_AUDIT: _ClassVar[Permission]
    FAKE_PERMISSION: _ClassVar[Permission]
    VIEW_CHAT: _ClassVar[Permission]
    VIEW_CHAT_REPORTS: _ClassVar[Permission]
    VIEW_CHAT_AUDIT: _ClassVar[Permission]
    VIEW_CAMPAIGN: _ClassVar[Permission]
    VIEW_CAMPAIGN_REPORT: _ClassVar[Permission]
    VIEW_CAMPAIGN_AUDIT: _ClassVar[Permission]
    EDIT_SAP_ADMIN: _ClassVar[Permission]
    EDIT_REPORT_REQUEST: _ClassVar[Permission]
    DELETE_REPORT_REQUEST: _ClassVar[Permission]
    EXECUTE_REPORT_REQUEST: _ClassVar[Permission]
    VIEW_BACKOFFICE_THEME: _ClassVar[Permission]
    CREATE_BACKOFFICE_THEME: _ClassVar[Permission]
    DELETE_BACKOFFICE_THEME: _ClassVar[Permission]
    EXECUTE_BACKOFFICE_THEME: _ClassVar[Permission]
    CREATE_CELL_PHONE_SCRUB: _ClassVar[Permission]
    EDIT_CELL_PHONE_SCRUB: _ClassVar[Permission]
    VIEW_CELL_PHONE_SCRUB: _ClassVar[Permission]
    VIEW_ADMIN_CLIENT_PREFERENCES: _ClassVar[Permission]
    DELETE_ADMIN_CLIENT_PREFERENCES: _ClassVar[Permission]
    CREATE_ADMIN_CLIENT_PREFERENCES: _ClassVar[Permission]
    EXECUTE_ADMIN_CLIENT_PREFERENCES: _ClassVar[Permission]
    CREATE_ONTARIO_SYSTEMS_ADMINISTRATOR: _ClassVar[Permission]
    DELETE_ONTARIO_SYSTEMS_ADMINISTRATOR: _ClassVar[Permission]
    EDIT_ONTARIO_SYSTEMS_ADMINISTRATOR: _ClassVar[Permission]
    CREATE_ONTARIO_SYSTEMS_USER: _ClassVar[Permission]
    DELETE_ONTARIO_SYSTEMS_USER: _ClassVar[Permission]
    EDIT_ONTARIO_SYSTEMS_USER: _ClassVar[Permission]
    CREATE_INTEGRATION_MESSAGES: _ClassVar[Permission]
    DELETE_INTEGRATION_MESSAGES: _ClassVar[Permission]
    EDIT_INTEGRATION_MESSAGES: _ClassVar[Permission]
    EXECUTE_INTEGRATION_MESSAGES: _ClassVar[Permission]
    APP_AGENT: _ClassVar[Permission]
    APP_BACKOFFICE: _ClassVar[Permission]
NO_PERMISSION: Permission
VIEW_LIST_MANAGER: Permission
CREATE_LIST_MANAGER: Permission
EDIT_LIST_MANAGER: Permission
DELETE_LIST_MANAGER: Permission
EXECUTE_LIST_MANAGER: Permission
VIEW_FIELD_DEFINITIONS: Permission
CREATE_FIELD_DEFINITIONS: Permission
EDIT_FIELD_DEFINITIONS: Permission
DELETE_FIELD_DEFINITIONS: Permission
EXECUTE_FIELD_DEFINITIONS: Permission
VIEW_IMPORT_TEMPLATES: Permission
CREATE_IMPORT_TEMPLATES: Permission
EDIT_IMPORT_TEMPLATES: Permission
DELETE_IMPORT_TEMPLATES: Permission
EXECUTE_IMPORT_TEMPLATES: Permission
VIEW_ADMIN_TOOLS: Permission
CREATE_ADMIN_TOOLS: Permission
EDIT_ADMIN_TOOLS: Permission
DELETE_ADMIN_TOOLS: Permission
EXECUTE_ADMIN_TOOLS: Permission
VIEW_COUNTRY_MANAGER: Permission
CREATE_COUNTRY_MANAGER: Permission
EDIT_COUNTRY_MANAGER: Permission
DELETE_COUNTRY_MANAGER: Permission
EXECUTE_COUNTRY_MANAGER: Permission
VIEW_DIAL_REGION_GROUPS: Permission
CREATE_DIAL_REGION_GROUPS: Permission
EDIT_DIAL_REGION_GROUPS: Permission
DELETE_DIAL_REGION_GROUPS: Permission
EXECUTE_DIAL_REGION_GROUPS: Permission
VIEW_DIAL_REGION: Permission
CREATE_DIAL_REGION: Permission
EDIT_DIAL_REGION: Permission
DELETE_DIAL_REGION: Permission
EXECUTE_DIAL_REGION: Permission
VIEW_TTS_MANAGER: Permission
CREATE_TTS_MANAGER: Permission
EDIT_TTS_MANAGER: Permission
DELETE_TTS_MANAGER: Permission
EXECUTE_TTS_MANAGER: Permission
VIEW_USER_MANAGEMENT: Permission
CREATE_USER_MANAGEMENT: Permission
EDIT_USER_MANAGEMENT: Permission
DELETE_USER_MANAGEMENT: Permission
EXECUTE_USER_MANAGEMENT: Permission
VIEW_CLIENT: Permission
CREATE_CLIENT: Permission
EDIT_CLIENT: Permission
DELETE_CLIENT: Permission
EXECUTE_CLIENT: Permission
VIEW_LOGIN: Permission
CREATE_LOGIN: Permission
EDIT_LOGIN: Permission
DELETE_LOGIN: Permission
EXECUTE_LOGIN: Permission
VIEW_PERMISSIONS: Permission
CREATE_PERMISSIONS: Permission
EDIT_PERMISSIONS: Permission
DELETE_PERMISSIONS: Permission
EXECUTE_PERMISSIONS: Permission
VIEW_PERMISSIONS_GROUPS: Permission
CREATE_PERMISSIONS_GROUPS: Permission
EDIT_PERMISSIONS_GROUPS: Permission
DELETE_PERMISSIONS_GROUPS: Permission
EXECUTE_PERMISSIONS_GROUPS: Permission
VIEW_PERMISSIONS_GROUP_ADMINISTRATOR: Permission
CREATE_PERMISSIONS_GROUP_ADMINISTRATOR: Permission
EDIT_PERMISSIONS_GROUP_ADMINISTRATOR: Permission
DELETE_PERMISSIONS_GROUP_ADMINISTRATOR: Permission
EXECUTE_PERMISSIONS_GROUP_ADMINISTRATOR: Permission
VIEW_CONTACT_US: Permission
CREATE_CONTACT_US: Permission
EDIT_CONTACT_US: Permission
DELETE_CONTACT_US: Permission
EXECUTE_CONTACT_US: Permission
VIEW_USER_OPTIONS: Permission
CREATE_USER_OPTIONS: Permission
EDIT_USER_OPTIONS: Permission
DELETE_USER_OPTIONS: Permission
EXECUTE_USER_OPTIONS: Permission
VIEW_CHANGE_PASSWORD: Permission
CREATE_CHANGE_PASSWORD: Permission
EDIT_CHANGE_PASSWORD: Permission
DELETE_CHANGE_PASSWORD: Permission
EXECUTE_CHANGE_PASSWORD: Permission
VIEW_PREFERENCES: Permission
CREATE_PREFERENCES: Permission
EDIT_PREFERENCES: Permission
DELETE_PREFERENCES: Permission
EXECUTE_PREFERENCES: Permission
VIEW_WEB_BROADCASTING: Permission
CREATE_WEB_BROADCASTING: Permission
EDIT_WEB_BROADCASTING: Permission
DELETE_WEB_BROADCASTING: Permission
EXECUTE_WEB_BROADCASTING: Permission
VIEW_REPORTS: Permission
CREATE_REPORTS: Permission
EDIT_REPORTS: Permission
DELETE_REPORTS: Permission
EXECUTE_REPORTS: Permission
VIEW_SEND_BROADCAST: Permission
CREATE_SEND_BROADCAST: Permission
EDIT_SEND_BROADCAST: Permission
DELETE_SEND_BROADCAST: Permission
EXECUTE_SEND_BROADCAST: Permission
VIEW_MESSAGE_MANAGER: Permission
CREATE_MESSAGE_MANAGER: Permission
EDIT_MESSAGE_MANAGER: Permission
DELETE_MESSAGE_MANAGER: Permission
EXECUTE_MESSAGE_MANAGER: Permission
VIEW_TEMPLATE_MANAGER: Permission
CREATE_TEMPLATE_MANAGER: Permission
EDIT_TEMPLATE_MANAGER: Permission
DELETE_TEMPLATE_MANAGER: Permission
EXECUTE_TEMPLATE_MANAGER: Permission
VIEW_DO_NOT_CALL_LIST: Permission
CREATE_DO_NOT_CALL_LIST: Permission
EDIT_DO_NOT_CALL_LIST: Permission
DELETE_DO_NOT_CALL_LIST: Permission
EXECUTE_DO_NOT_CALL_LIST: Permission
VIEW_SCHEDULE_RULES: Permission
CREATE_SCHEDULE_RULES: Permission
EDIT_SCHEDULE_RULES: Permission
DELETE_SCHEDULE_RULES: Permission
EXECUTE_SCHEDULE_RULES: Permission
VIEW_BILLING: Permission
CREATE_BILLING: Permission
EDIT_BILLING: Permission
DELETE_BILLING: Permission
EXECUTE_BILLING: Permission
VIEW_SAP_EXPORT: Permission
CREATE_SAP_EXPORT: Permission
EDIT_SAP_EXPORT: Permission
DELETE_SAP_EXPORT: Permission
EXECUTE_SAP_EXPORT: Permission
VIEW_AUDIT: Permission
CREATE_AUDIT: Permission
EDIT_AUDIT: Permission
DELETE_AUDIT: Permission
EXECUTE_AUDIT: Permission
VIEW_AUTOMATED_REPORTING: Permission
CREATE_AUTOMATED_REPORTING: Permission
EDIT_AUTOMATED_REPORTING: Permission
DELETE_AUTOMATED_REPORTING: Permission
EXECUTE_AUTOMATED_REPORTING: Permission
VIEW_CUSTOMER_SERVICE: Permission
CREATE_CUSTOMER_SERVICE: Permission
EDIT_CUSTOMER_SERVICE: Permission
DELETE_CUSTOMER_SERVICE: Permission
EXECUTE_CUSTOMER_SERVICE: Permission
VIEW_SCRIPTS: Permission
CREATE_SCRIPTS: Permission
EDIT_SCRIPTS: Permission
DELETE_SCRIPTS: Permission
EXECUTE_SCRIPTS: Permission
VIEW_CLIENT_PREFERENCES: Permission
CREATE_CLIENT_PREFERENCES: Permission
EDIT_CLIENT_PREFERENCES: Permission
DELETE_CLIENT_PREFERENCES: Permission
EXECUTE_CLIENT_PREFERENCES: Permission
VIEW_RECORDINGS_REPORTING: Permission
CREATE_RECORDINGS_REPORTING: Permission
EDIT_RECORDINGS_REPORTING: Permission
DELETE_RECORDINGS_REPORTING: Permission
EXECUTE_RECORDINGS_REPORTING: Permission
VIEW_DEBUG_MODE: Permission
CREATE_DEBUG_MODE: Permission
EDIT_DEBUG_MODE: Permission
DELETE_DEBUG_MODE: Permission
EXECUTE_DEBUG_MODE: Permission
CREATE_DNCL_MAP: Permission
VIEW_DNCL_MAP: Permission
EXECUTE_COPY_DOWN: Permission
VIEW_AGENTS: Permission
VIEW_ADMIN_CUSTOMER_SERVICE: Permission
EDIT_AGENTS: Permission
DELETE_AGENTS: Permission
EXECUTE_AGENTS: Permission
EDIT_HUNT_GROUP: Permission
DELETE_HUNT_GROUP: Permission
EXECUTE_HUNT_GROUP: Permission
VIEW_HUNT_GROUP: Permission
VIEW_AGENTS_REPORT: Permission
VIEW_AGENTS_DASHBOARD: Permission
VIEW_CALLER_ID_BUCKETS: Permission
EDIT_CALLER_ID_BUCKETS: Permission
CREATE_CALLER_ID_BUCKETS: Permission
DELETE_CALLER_ID_BUCKETS: Permission
EXECUTE_CALLER_ID_BUCKETS: Permission
VIEW_REPORT_REQUEST: Permission
CREATE_REPORT_REQUEST: Permission
VIEW_INBOUND_SCRIPTS: Permission
EDIT_INBOUND_SCRIPTS: Permission
CREATE_INBOUND_SCRIPTS: Permission
DELETE_INBOUND_SCRIPTS: Permission
EDIT_BACKOFFICE_THEME: Permission
CREATE_PHONE_NUMBER_MANAGEMENT: Permission
EDIT_PHONE_NUMBER_MANAGEMENT: Permission
VIEW_PHONE_NUMBER_MANAGEMENT: Permission
DELETE_PHONE_NUMBER_MANAGEMENT: Permission
EXECUTE_PHONE_NUMBER_MANAGEMENT: Permission
EXECUTE_INBOUND_SCRIPTS: Permission
EXECUTE_CELL_PHONE_SCRUB: Permission
EDIT_ADMIN_CLIENT_PREFERENCES: Permission
VIEW_ONTARIO_SYSTEMS_ADMINISTRATOR: Permission
EXECUTE_ONTARIO_SYSTEMS_ADMINISTRATOR: Permission
EXECUTE_ONTARIO_SYSTEMS_USER: Permission
VIEW_INTEGRATION_MESSAGES: Permission
VIEW_ONTARIO_SYSTEMS_USER: Permission
EXECUTE_BROADCAST_CONTROL_INBOUND: Permission
EXECUTE_BROADCAST_CONTROL_MANUAL: Permission
EXECUTE_BROADCAST_CONTROL_OUTBOUND: Permission
CREATE_PREVIEW_ONLY_TEMPLATES: Permission
CREATE_MAC_ONLY_TEMPLATES: Permission
EDIT_TRIGGER_ADVANCE_ON_CALL: Permission
CREATE_TRIGGER_ADVANCE_ON_CALL: Permission
DELETE_MAC_ONLY_TEMPLATES: Permission
EXECUTE_MAC_ONLY_TEMPLATES: Permission
VIEW_MAC_ONLY_TEMPLATES: Permission
EDIT_MAC_ONLY_TEMPLATES: Permission
EXECUTE_PREVIEW_ONLY_TEMPLATES: Permission
VIEW_PREVIEW_ONLY_TEMPLATES: Permission
EDIT_PREVIEW_ONLY_TEMPLATES: Permission
DELETE_PREVIEW_ONLY_TEMPLATES: Permission
VIEW_ANALYTICS_REPORTING: Permission
CREATE_HUNT_GROUP: Permission
CREATE_AGENTS: Permission
CREATE_AGENTS_DASHBOARD: Permission
CREATE_AGENTS_REPORT: Permission
DELETE_AGENTS_DASHBOARD: Permission
DELETE_AGENTS_REPORT: Permission
EDIT_AGENTS_DASHBOARD: Permission
EDIT_AGENTS_REPORT: Permission
EXECUTE_AGENTS_DASHBOARD: Permission
EXECUTE_AGENTS_REPORT: Permission
DELETE_TRIGGER_ADVANCE_ON_CALL: Permission
DELETE_CELL_PHONE_SCRUB: Permission
CREATE_RINGLESS_VOICEMAIL_TEMPLATES: Permission
EDIT_RINGLESS_VOICEMAIL_TEMPLATES: Permission
CREATE_VOCALDIRECT_TEMPLATES: Permission
EDIT_VOCALDIRECT_TEMPLATES: Permission
VIEW_EMAIL: Permission
VIEW_SMS: Permission
VIEW_EMAIL_REPORTS: Permission
VIEW_EMAIL_AUDIT: Permission
VIEW_SMS_REPORTS: Permission
VIEW_SMS_AUDIT: Permission
FAKE_PERMISSION: Permission
VIEW_CHAT: Permission
VIEW_CHAT_REPORTS: Permission
VIEW_CHAT_AUDIT: Permission
VIEW_CAMPAIGN: Permission
VIEW_CAMPAIGN_REPORT: Permission
VIEW_CAMPAIGN_AUDIT: Permission
EDIT_SAP_ADMIN: Permission
EDIT_REPORT_REQUEST: Permission
DELETE_REPORT_REQUEST: Permission
EXECUTE_REPORT_REQUEST: Permission
VIEW_BACKOFFICE_THEME: Permission
CREATE_BACKOFFICE_THEME: Permission
DELETE_BACKOFFICE_THEME: Permission
EXECUTE_BACKOFFICE_THEME: Permission
CREATE_CELL_PHONE_SCRUB: Permission
EDIT_CELL_PHONE_SCRUB: Permission
VIEW_CELL_PHONE_SCRUB: Permission
VIEW_ADMIN_CLIENT_PREFERENCES: Permission
DELETE_ADMIN_CLIENT_PREFERENCES: Permission
CREATE_ADMIN_CLIENT_PREFERENCES: Permission
EXECUTE_ADMIN_CLIENT_PREFERENCES: Permission
CREATE_ONTARIO_SYSTEMS_ADMINISTRATOR: Permission
DELETE_ONTARIO_SYSTEMS_ADMINISTRATOR: Permission
EDIT_ONTARIO_SYSTEMS_ADMINISTRATOR: Permission
CREATE_ONTARIO_SYSTEMS_USER: Permission
DELETE_ONTARIO_SYSTEMS_USER: Permission
EDIT_ONTARIO_SYSTEMS_USER: Permission
CREATE_INTEGRATION_MESSAGES: Permission
DELETE_INTEGRATION_MESSAGES: Permission
EDIT_INTEGRATION_MESSAGES: Permission
EXECUTE_INTEGRATION_MESSAGES: Permission
APP_AGENT: Permission
APP_BACKOFFICE: Permission