from annotations.perms import tcn_pb2 as _tcn_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PERMISSION_UNSPECIFIED: _ClassVar[Permission]
    PERMISSION_DEV: _ClassVar[Permission]
    PERMISSION_LEARN_EDIT: _ClassVar[Permission]
    PERMISSION_ORG_EDIT: _ClassVar[Permission]
    PERMISSION_ORG_VIEW: _ClassVar[Permission]
    PERMISSION_OWNING_ORG_IMITATION: _ClassVar[Permission]
    PERMISSION_USER_CREATE: _ClassVar[Permission]
    PERMISSION_USER_EDIT: _ClassVar[Permission]
    PERMISSION_USER_EDIT_PASSWORD: _ClassVar[Permission]
    PERMISSION_USER_EDIT_OPTIONS: _ClassVar[Permission]
    PERMISSION_LOGIN_CONNECTIONS: _ClassVar[Permission]
    PERMISSION_USER_EDIT_AGENT_CALLER_ID: _ClassVar[Permission]
    PERMISSION_AGENT_MANAGEMENT: _ClassVar[Permission]
    PERMISSION_PERMISSION_GROUP_EDIT: _ClassVar[Permission]
    PERMISSION_PERMISSION_GROUP_ASSIGN: _ClassVar[Permission]
    PERMISSION_LABEL_MANAGEMENT: _ClassVar[Permission]
    PERMISSION_TRUST_MANAGEMENT: _ClassVar[Permission]
    PERMISSION_HUNTGROUP_VIEW: _ClassVar[Permission]
    PERMISSION_HUNTGROUP_EDIT: _ClassVar[Permission]
    PERMISSION_SOUNDBOARD_VIEW: _ClassVar[Permission]
    PERMISSION_SOUNDBOARD_EDIT: _ClassVar[Permission]
    PERMISSION_SUBSCRIPTION_MANAGEMENT: _ClassVar[Permission]
    PERMISSION_CUSTOMER_SUPPORT: _ClassVar[Permission]
    PERMISSION_IMITATION: _ClassVar[Permission]
    PERMISSION_BILLING_EDIT: _ClassVar[Permission]
    PERMISSION_TCN_ADMIN_SETTINGS: _ClassVar[Permission]
    PERMISSION_TCN_BILLING: _ClassVar[Permission]
    PERMISSION_SUPPORT_TCN_INSIGHTS_ADMIN: _ClassVar[Permission]
    PERMISSION_SUPPORT_TCN_DASHBOARDS_ADMIN: _ClassVar[Permission]
    PERMISSION_AGENT: _ClassVar[Permission]
    PERMISSION_ACCEPT_QUEUED_CALLS: _ClassVar[Permission]
    PERMISSION_VIEW_CAMPAIGN_COMPLETION: _ClassVar[Permission]
    PERMISSION_VIEW_VOICE_MAIL: _ClassVar[Permission]
    PERMISSION_AGENT_COMPLIANCE_SCRUBLIST_OPTIONS: _ClassVar[Permission]
    PERMISSION_EXTENSION_EDIT: _ClassVar[Permission]
    PERMISSION_VOICEMAIL_DOWNLOAD: _ClassVar[Permission]
    PERMISSION_MANUAL_APPROVE: _ClassVar[Permission]
    PERMISSION_AGENT_PORTALS_VIEW: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_FLAG: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_CONFIG: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_RECORDING_DOWNLOAD: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DOWNLOAD: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DELETE: _ClassVar[Permission]
    PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING_DELETE: _ClassVar[Permission]
    PERMISSION_BUSINESS_INTELLIGENCE: _ClassVar[Permission]
    PERMISSION_DASHBOARDS_VIEW: _ClassVar[Permission]
    PERMISSION_DASHBOARDS_EDIT: _ClassVar[Permission]
    PERMISSION_INSIGHTS_COMMON_LIBRARY_MANAGE: _ClassVar[Permission]
    PERMISSION_INSIGHTS_MANAGE: _ClassVar[Permission]
    PERMISSION_INSIGHTS_INSIGHT_VIEW: _ClassVar[Permission]
    PERMISSION_INSIGHTS_INSIGHT_EDIT: _ClassVar[Permission]
    PERMISSION_INSIGHTS_DASHBOARD_VIEW: _ClassVar[Permission]
    PERMISSION_INSIGHTS_DASHBOARD_EDIT: _ClassVar[Permission]
    PERMISSION_ROOM303: _ClassVar[Permission]
    PERMISSION_AGENT_CALL_SCRIPTS: _ClassVar[Permission]
    PERMISSION_COMPLIANCE: _ClassVar[Permission]
    PERMISSION_COMPLIANCE_CONSENT: _ClassVar[Permission]
    PERMISSION_LMS_VIEW: _ClassVar[Permission]
    PERMISSION_LMS_EDIT: _ClassVar[Permission]
    PERMISSION_OMNI_BOSS: _ClassVar[Permission]
    PERMISSION_OMNI_PORTALS_VIEW: _ClassVar[Permission]
    PERMISSION_INTEGRATIONS_VIEW: _ClassVar[Permission]
    PERMISSION_INTEGRATIONS_PAYMENT: _ClassVar[Permission]
    PERMISSION_INTEGRATIONS_JOURNEY: _ClassVar[Permission]
    PERMISSION_WFM: _ClassVar[Permission]
    PERMISSION_AGENT_PORTAL: _ClassVar[Permission]
    PERMISSION_SCORECARDS: _ClassVar[Permission]
    PERMISSION_SCORECARDS_MANAGE: _ClassVar[Permission]
    PERMISSION_SCORECARDS_EVALUATE: _ClassVar[Permission]
    PERMISSION_SCORECARDS_FLAG_EVAL: _ClassVar[Permission]
    PERMISSION_DEV_TOOLS: _ClassVar[Permission]
    PERMISSION_DELIVERY_NOTIFICATIONS_VIEW: _ClassVar[Permission]
    PERMISSION_DELIVERY_NOTIFICATIONS_EDIT: _ClassVar[Permission]
    PERMISSION_TICKETS_APP: _ClassVar[Permission]
    PERMISSION_TICKETS_ADMIN: _ClassVar[Permission]
    PERMISSION_WORKFLOWS: _ClassVar[Permission]
    PERMISSION_PBX_MANAGER_VIEW: _ClassVar[Permission]
    PERMISSION_PBX_MANAGER_EDIT: _ClassVar[Permission]
    PERMISSION_NEWSROOM_EDIT: _ClassVar[Permission]
    PERMISSION_NEWSROOM_PUBLISH: _ClassVar[Permission]
PERMISSION_UNSPECIFIED: Permission
PERMISSION_DEV: Permission
PERMISSION_LEARN_EDIT: Permission
PERMISSION_ORG_EDIT: Permission
PERMISSION_ORG_VIEW: Permission
PERMISSION_OWNING_ORG_IMITATION: Permission
PERMISSION_USER_CREATE: Permission
PERMISSION_USER_EDIT: Permission
PERMISSION_USER_EDIT_PASSWORD: Permission
PERMISSION_USER_EDIT_OPTIONS: Permission
PERMISSION_LOGIN_CONNECTIONS: Permission
PERMISSION_USER_EDIT_AGENT_CALLER_ID: Permission
PERMISSION_AGENT_MANAGEMENT: Permission
PERMISSION_PERMISSION_GROUP_EDIT: Permission
PERMISSION_PERMISSION_GROUP_ASSIGN: Permission
PERMISSION_LABEL_MANAGEMENT: Permission
PERMISSION_TRUST_MANAGEMENT: Permission
PERMISSION_HUNTGROUP_VIEW: Permission
PERMISSION_HUNTGROUP_EDIT: Permission
PERMISSION_SOUNDBOARD_VIEW: Permission
PERMISSION_SOUNDBOARD_EDIT: Permission
PERMISSION_SUBSCRIPTION_MANAGEMENT: Permission
PERMISSION_CUSTOMER_SUPPORT: Permission
PERMISSION_IMITATION: Permission
PERMISSION_BILLING_EDIT: Permission
PERMISSION_TCN_ADMIN_SETTINGS: Permission
PERMISSION_TCN_BILLING: Permission
PERMISSION_SUPPORT_TCN_INSIGHTS_ADMIN: Permission
PERMISSION_SUPPORT_TCN_DASHBOARDS_ADMIN: Permission
PERMISSION_AGENT: Permission
PERMISSION_ACCEPT_QUEUED_CALLS: Permission
PERMISSION_VIEW_CAMPAIGN_COMPLETION: Permission
PERMISSION_VIEW_VOICE_MAIL: Permission
PERMISSION_AGENT_COMPLIANCE_SCRUBLIST_OPTIONS: Permission
PERMISSION_EXTENSION_EDIT: Permission
PERMISSION_VOICEMAIL_DOWNLOAD: Permission
PERMISSION_MANUAL_APPROVE: Permission
PERMISSION_AGENT_PORTALS_VIEW: Permission
PERMISSION_VOICE_ANALYTICS: Permission
PERMISSION_VOICE_ANALYTICS_FLAG: Permission
PERMISSION_VOICE_ANALYTICS_CONFIG: Permission
PERMISSION_VOICE_ANALYTICS_RECORDING_DOWNLOAD: Permission
PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DOWNLOAD: Permission
PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING: Permission
PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DELETE: Permission
PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING_DELETE: Permission
PERMISSION_BUSINESS_INTELLIGENCE: Permission
PERMISSION_DASHBOARDS_VIEW: Permission
PERMISSION_DASHBOARDS_EDIT: Permission
PERMISSION_INSIGHTS_COMMON_LIBRARY_MANAGE: Permission
PERMISSION_INSIGHTS_MANAGE: Permission
PERMISSION_INSIGHTS_INSIGHT_VIEW: Permission
PERMISSION_INSIGHTS_INSIGHT_EDIT: Permission
PERMISSION_INSIGHTS_DASHBOARD_VIEW: Permission
PERMISSION_INSIGHTS_DASHBOARD_EDIT: Permission
PERMISSION_ROOM303: Permission
PERMISSION_AGENT_CALL_SCRIPTS: Permission
PERMISSION_COMPLIANCE: Permission
PERMISSION_COMPLIANCE_CONSENT: Permission
PERMISSION_LMS_VIEW: Permission
PERMISSION_LMS_EDIT: Permission
PERMISSION_OMNI_BOSS: Permission
PERMISSION_OMNI_PORTALS_VIEW: Permission
PERMISSION_INTEGRATIONS_VIEW: Permission
PERMISSION_INTEGRATIONS_PAYMENT: Permission
PERMISSION_INTEGRATIONS_JOURNEY: Permission
PERMISSION_WFM: Permission
PERMISSION_AGENT_PORTAL: Permission
PERMISSION_SCORECARDS: Permission
PERMISSION_SCORECARDS_MANAGE: Permission
PERMISSION_SCORECARDS_EVALUATE: Permission
PERMISSION_SCORECARDS_FLAG_EVAL: Permission
PERMISSION_DEV_TOOLS: Permission
PERMISSION_DELIVERY_NOTIFICATIONS_VIEW: Permission
PERMISSION_DELIVERY_NOTIFICATIONS_EDIT: Permission
PERMISSION_TICKETS_APP: Permission
PERMISSION_TICKETS_ADMIN: Permission
PERMISSION_WORKFLOWS: Permission
PERMISSION_PBX_MANAGER_VIEW: Permission
PERMISSION_PBX_MANAGER_EDIT: Permission
PERMISSION_NEWSROOM_EDIT: Permission
PERMISSION_NEWSROOM_PUBLISH: Permission
