from api.commons import org_pb2 as _org_pb2
from api.commons.org import preferences_pb2 as _preferences_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOrganizationPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetOrganizationPreferencesResponse(_message.Message):
    __slots__ = ("organization_preferences",)
    ORGANIZATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    organization_preferences: _preferences_pb2.OrganizationPreferences
    def __init__(self, organization_preferences: _Optional[_Union[_preferences_pb2.OrganizationPreferences, _Mapping]] = ...) -> None: ...

class UpdateOrganizationPreferencesRequest(_message.Message):
    __slots__ = ("organization_preferences", "field_mask")
    ORGANIZATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_preferences: _preferences_pb2.OrganizationPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization_preferences: _Optional[_Union[_preferences_pb2.OrganizationPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateOrganizationPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAgentPreferencesResponse(_message.Message):
    __slots__ = ("agent_preferences",)
    AGENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    agent_preferences: _preferences_pb2.AgentPreferences
    def __init__(self, agent_preferences: _Optional[_Union[_preferences_pb2.AgentPreferences, _Mapping]] = ...) -> None: ...

class UpdateAgentPreferencesRequest(_message.Message):
    __slots__ = ("agent_preferences", "field_mask")
    AGENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    agent_preferences: _preferences_pb2.AgentPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, agent_preferences: _Optional[_Union[_preferences_pb2.AgentPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAgentPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetContactPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetContactPreferencesResponse(_message.Message):
    __slots__ = ("contact_preferences",)
    CONTACT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    contact_preferences: _preferences_pb2.ContactPreferences
    def __init__(self, contact_preferences: _Optional[_Union[_preferences_pb2.ContactPreferences, _Mapping]] = ...) -> None: ...

class UpdateContactPreferencesRequest(_message.Message):
    __slots__ = ("contact_preferences", "field_mask")
    CONTACT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    contact_preferences: _preferences_pb2.ContactPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, contact_preferences: _Optional[_Union[_preferences_pb2.ContactPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateContactPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAuthenticationPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAuthenticationPreferencesResponse(_message.Message):
    __slots__ = ("authentication_preferences",)
    AUTHENTICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    authentication_preferences: _preferences_pb2.AuthenticationPreferences
    def __init__(self, authentication_preferences: _Optional[_Union[_preferences_pb2.AuthenticationPreferences, _Mapping]] = ...) -> None: ...

class UpdateAuthenticationPreferencesRequest(_message.Message):
    __slots__ = ("authentication_preferences", "duo_client_secret", "field_mask")
    AUTHENTICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    DUO_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    authentication_preferences: _preferences_pb2.AuthenticationPreferences
    duo_client_secret: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, authentication_preferences: _Optional[_Union[_preferences_pb2.AuthenticationPreferences, _Mapping]] = ..., duo_client_secret: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAuthenticationPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWebhookPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetWebhookPreferencesResponse(_message.Message):
    __slots__ = ("webhook_preferences",)
    WEBHOOK_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    webhook_preferences: _preferences_pb2.WebhookPreferences
    def __init__(self, webhook_preferences: _Optional[_Union[_preferences_pb2.WebhookPreferences, _Mapping]] = ...) -> None: ...

class UpdateWebhookPreferencesRequest(_message.Message):
    __slots__ = ("webhook_preferences", "field_mask")
    WEBHOOK_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    webhook_preferences: _preferences_pb2.WebhookPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, webhook_preferences: _Optional[_Union[_preferences_pb2.WebhookPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateWebhookPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDashboardGeneralPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDashboardGeneralPreferencesResponse(_message.Message):
    __slots__ = ("dashboard_preferences",)
    DASHBOARD_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_preferences: _preferences_pb2.DashboardPreferences
    def __init__(self, dashboard_preferences: _Optional[_Union[_preferences_pb2.DashboardPreferences, _Mapping]] = ...) -> None: ...

class UpdateDashboardGeneralPreferencesRequest(_message.Message):
    __slots__ = ("dashboard_preferences", "field_mask")
    DASHBOARD_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    dashboard_preferences: _preferences_pb2.DashboardPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, dashboard_preferences: _Optional[_Union[_preferences_pb2.DashboardPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDashboardGeneralPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDashboardQueuePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDashboardQueuePreferencesResponse(_message.Message):
    __slots__ = ("dashboard_queue_preferences",)
    DASHBOARD_QUEUE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    dashboard_queue_preferences: _preferences_pb2.DashboardQueuePreferences
    def __init__(self, dashboard_queue_preferences: _Optional[_Union[_preferences_pb2.DashboardQueuePreferences, _Mapping]] = ...) -> None: ...

class UpdateDashboardQueuePreferencesRequest(_message.Message):
    __slots__ = ("dashboard_queue_preferences", "field_mask")
    DASHBOARD_QUEUE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    dashboard_queue_preferences: _preferences_pb2.DashboardQueuePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, dashboard_queue_preferences: _Optional[_Union[_preferences_pb2.DashboardQueuePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDashboardQueuePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPhonePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetPhonePreferencesResponse(_message.Message):
    __slots__ = ("phone_preferences",)
    PHONE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    phone_preferences: _preferences_pb2.PhonePreferences
    def __init__(self, phone_preferences: _Optional[_Union[_preferences_pb2.PhonePreferences, _Mapping]] = ...) -> None: ...

class UpdatePhonePreferencesRequest(_message.Message):
    __slots__ = ("phone_preferences", "field_mask")
    PHONE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    phone_preferences: _preferences_pb2.PhonePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, phone_preferences: _Optional[_Union[_preferences_pb2.PhonePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePhonePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhonePreferencesDB(_message.Message):
    __slots__ = ("org_id", "phone_preferences_json")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_PREFERENCES_JSON_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    phone_preferences_json: str
    def __init__(self, org_id: _Optional[str] = ..., phone_preferences_json: _Optional[str] = ...) -> None: ...

class GetCompliancePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetCompliancePreferencesResponse(_message.Message):
    __slots__ = ("compliance_preferences",)
    COMPLIANCE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    compliance_preferences: _preferences_pb2.CompliancePreferences
    def __init__(self, compliance_preferences: _Optional[_Union[_preferences_pb2.CompliancePreferences, _Mapping]] = ...) -> None: ...

class UpdateCompliancePreferencesRequest(_message.Message):
    __slots__ = ("compliance_preferences", "field_mask")
    COMPLIANCE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    compliance_preferences: _preferences_pb2.CompliancePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, compliance_preferences: _Optional[_Union[_preferences_pb2.CompliancePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCompliancePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBroadcastPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBroadcastPreferencesResponse(_message.Message):
    __slots__ = ("broadcast_preferences",)
    BROADCAST_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    broadcast_preferences: _preferences_pb2.BroadcastPreferences
    def __init__(self, broadcast_preferences: _Optional[_Union[_preferences_pb2.BroadcastPreferences, _Mapping]] = ...) -> None: ...

class UpdateBroadcastPreferencesRequest(_message.Message):
    __slots__ = ("broadcast_preferences", "field_mask")
    BROADCAST_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    broadcast_preferences: _preferences_pb2.BroadcastPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, broadcast_preferences: _Optional[_Union[_preferences_pb2.BroadcastPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBroadcastPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSchedulePreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSchedulePreferencesResponse(_message.Message):
    __slots__ = ("schedule_preferences",)
    SCHEDULE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    schedule_preferences: _preferences_pb2.SchedulePreferences
    def __init__(self, schedule_preferences: _Optional[_Union[_preferences_pb2.SchedulePreferences, _Mapping]] = ...) -> None: ...

class UpdateSchedulePreferencesRequest(_message.Message):
    __slots__ = ("schedule_preferences", "field_mask")
    SCHEDULE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    schedule_preferences: _preferences_pb2.SchedulePreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, schedule_preferences: _Optional[_Union[_preferences_pb2.SchedulePreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSchedulePreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetEmailSmsPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEmailSmsPreferencesResponse(_message.Message):
    __slots__ = ("email_sms_preferences",)
    EMAIL_SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    email_sms_preferences: _preferences_pb2.EmailSmsPreferences
    def __init__(self, email_sms_preferences: _Optional[_Union[_preferences_pb2.EmailSmsPreferences, _Mapping]] = ...) -> None: ...

class UpdateEmailSmsPreferencesRequest(_message.Message):
    __slots__ = ("email_sms_preferences", "field_mask")
    EMAIL_SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    email_sms_preferences: _preferences_pb2.EmailSmsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, email_sms_preferences: _Optional[_Union[_preferences_pb2.EmailSmsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEmailSmsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBusinessPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBusinessPreferencesResponse(_message.Message):
    __slots__ = ("business_preferences",)
    BUSINESS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    business_preferences: _preferences_pb2.BusinessPreferences
    def __init__(self, business_preferences: _Optional[_Union[_preferences_pb2.BusinessPreferences, _Mapping]] = ...) -> None: ...

class UpdateBusinessPreferencesRequest(_message.Message):
    __slots__ = ("business_preferences", "field_mask")
    BUSINESS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    business_preferences: _preferences_pb2.BusinessPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_preferences: _Optional[_Union[_preferences_pb2.BusinessPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBusinessPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAdminBusinessPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "business_preferences", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    business_preferences: _preferences_pb2.BusinessPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., business_preferences: _Optional[_Union[_preferences_pb2.BusinessPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAdminBusinessPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetScorecardsPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetScorecardsPreferencesResponse(_message.Message):
    __slots__ = ("scorecards_preferences",)
    SCORECARDS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    scorecards_preferences: _preferences_pb2.ScorecardsPreferences
    def __init__(self, scorecards_preferences: _Optional[_Union[_preferences_pb2.ScorecardsPreferences, _Mapping]] = ...) -> None: ...

class UpdateScorecardsPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "scorecards_preferences", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    scorecards_preferences: _preferences_pb2.ScorecardsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., scorecards_preferences: _Optional[_Union[_preferences_pb2.ScorecardsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateScorecardsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVoiceAnalyticsPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetVoiceAnalyticsPreferencesResponse(_message.Message):
    __slots__ = ("voice_analytics_preferences",)
    VOICE_ANALYTICS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    voice_analytics_preferences: _preferences_pb2.VoiceAnalyticsPreferences
    def __init__(self, voice_analytics_preferences: _Optional[_Union[_preferences_pb2.VoiceAnalyticsPreferences, _Mapping]] = ...) -> None: ...

class ListVoiceAnalyticsPreferencesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVoiceAnalyticsPreferencesResponse(_message.Message):
    __slots__ = ("voice_analytics_preferences",)
    VOICE_ANALYTICS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    voice_analytics_preferences: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.VoiceAnalyticsPreferences]
    def __init__(self, voice_analytics_preferences: _Optional[_Iterable[_Union[_preferences_pb2.VoiceAnalyticsPreferences, _Mapping]]] = ...) -> None: ...

class UpdateVoiceAnalyticsPreferencesRequest(_message.Message):
    __slots__ = ("voice_analytics_preferences", "field_mask")
    VOICE_ANALYTICS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    voice_analytics_preferences: _preferences_pb2.VoiceAnalyticsPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, voice_analytics_preferences: _Optional[_Union[_preferences_pb2.VoiceAnalyticsPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateVoiceAnalyticsPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetEndOfDayPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEndOfDayPreferencesResponse(_message.Message):
    __slots__ = ("end_of_day_preferences",)
    END_OF_DAY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    end_of_day_preferences: _preferences_pb2.EndOfDayPreferences
    def __init__(self, end_of_day_preferences: _Optional[_Union[_preferences_pb2.EndOfDayPreferences, _Mapping]] = ...) -> None: ...

class UpdateEndOfDayPreferencesRequest(_message.Message):
    __slots__ = ("end_of_day_preferences", "field_mask")
    END_OF_DAY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_of_day_preferences: _preferences_pb2.EndOfDayPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_of_day_preferences: _Optional[_Union[_preferences_pb2.EndOfDayPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEndOfDayPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFilterPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetFilterPreferencesResponse(_message.Message):
    __slots__ = ("filter_preferences",)
    FILTER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    filter_preferences: _preferences_pb2.FilterPreferences
    def __init__(self, filter_preferences: _Optional[_Union[_preferences_pb2.FilterPreferences, _Mapping]] = ...) -> None: ...

class UpdateFilterPreferencesRequest(_message.Message):
    __slots__ = ("filter_preferences", "field_mask")
    FILTER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    filter_preferences: _preferences_pb2.FilterPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, filter_preferences: _Optional[_Union[_preferences_pb2.FilterPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateFilterPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRecordingPreferencesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetRecordingPreferencesResponse(_message.Message):
    __slots__ = ("recording_preferences",)
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    recording_preferences: _preferences_pb2.RecordingPreferences
    def __init__(self, recording_preferences: _Optional[_Union[_preferences_pb2.RecordingPreferences, _Mapping]] = ...) -> None: ...

class UpdateRecordingPreferencesRequest(_message.Message):
    __slots__ = ("recording_preferences", "field_mask")
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    recording_preferences: _preferences_pb2.RecordingPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, recording_preferences: _Optional[_Union[_preferences_pb2.RecordingPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRecordingPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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
    admin_client_preferences: _preferences_pb2.AdminClientPreferences
    def __init__(self, admin_client_preferences: _Optional[_Union[_preferences_pb2.AdminClientPreferences, _Mapping]] = ...) -> None: ...

class UpdateAdminClientPreferencesRequest(_message.Message):
    __slots__ = ("org_id", "admin_client_preferences", "field_mask")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CLIENT_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    admin_client_preferences: _preferences_pb2.AdminClientPreferences
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, org_id: _Optional[str] = ..., admin_client_preferences: _Optional[_Union[_preferences_pb2.AdminClientPreferences, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAdminClientPreferencesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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

class CreateBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _preferences_pb2.BusinessHours
    def __init__(self, business_hours: _Optional[_Union[_preferences_pb2.BusinessHours, _Mapping]] = ...) -> None: ...

class CreateBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class UpdateBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _preferences_pb2.BusinessHours
    def __init__(self, business_hours: _Optional[_Union[_preferences_pb2.BusinessHours, _Mapping]] = ...) -> None: ...

class UpdateBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBusinessHoursRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.BusinessHours]
    def __init__(self, business_hours: _Optional[_Iterable[_Union[_preferences_pb2.BusinessHours, _Mapping]]] = ...) -> None: ...

class GetBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class GetBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _preferences_pb2.BusinessHours
    def __init__(self, business_hours: _Optional[_Union[_preferences_pb2.BusinessHours, _Mapping]] = ...) -> None: ...

class SetBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_name", "description", "day_intervals", "timezone")
    BUSINESS_HOURS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    business_hours_name: str
    description: str
    day_intervals: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.DayInterval]
    timezone: _org_pb2.TimeZone
    def __init__(self, business_hours_name: _Optional[str] = ..., description: _Optional[str] = ..., day_intervals: _Optional[_Iterable[_Union[_preferences_pb2.DayInterval, _Mapping]]] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class SetBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class AddIntervalToBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id", "day_interval")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    day_interval: _preferences_pb2.DayInterval
    def __init__(self, business_hours_id: _Optional[str] = ..., day_interval: _Optional[_Union[_preferences_pb2.DayInterval, _Mapping]] = ...) -> None: ...

class AddIntervalToBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveIntervalFromBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id", "day_interval")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    day_interval: _preferences_pb2.DayInterval
    def __init__(self, business_hours_id: _Optional[str] = ..., day_interval: _Optional[_Union[_preferences_pb2.DayInterval, _Mapping]] = ...) -> None: ...

class RemoveIntervalFromBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBusinessHoursInfoRequest(_message.Message):
    __slots__ = ("business_hours_id", "business_hours_name", "description", "timezone", "field_mask")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_HOURS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    business_hours_name: str
    description: str
    timezone: _org_pb2.TimeZone
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_hours_id: _Optional[str] = ..., business_hours_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBusinessHoursInfoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class DeleteBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EvaluateBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class EvaluateBusinessHoursResponse(_message.Message):
    __slots__ = ("within_range",)
    WITHIN_RANGE_FIELD_NUMBER: _ClassVar[int]
    within_range: bool
    def __init__(self, within_range: bool = ...) -> None: ...

class CreateCertificateInfoRequest(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateCertificateInfoResponse(_message.Message):
    __slots__ = ("encoded_certificate",)
    ENCODED_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    encoded_certificate: str
    def __init__(self, encoded_certificate: _Optional[str] = ...) -> None: ...

class DeleteCertificateInfoRequest(_message.Message):
    __slots__ = ("certificate_info_id",)
    CERTIFICATE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_info_id: str
    def __init__(self, certificate_info_id: _Optional[str] = ...) -> None: ...

class DeleteCertificateInfoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCertificateInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCertificateInfoResponse(_message.Message):
    __slots__ = ("certificate_info_list",)
    CERTIFICATE_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    certificate_info_list: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.CertificateInfo]
    def __init__(self, certificate_info_list: _Optional[_Iterable[_Union[_preferences_pb2.CertificateInfo, _Mapping]]] = ...) -> None: ...
