# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/preferences.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'api/v1alpha1/org/preferences.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import preferences_pb2 as api_dot_commons_dot_org_dot_preferences__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/org/preferences.proto\x12\x10\x61pi.v1alpha1.org\x1a\x15\x61pi/commons/org.proto\x1a!api/commons/org/preferences.proto\x1a google/protobuf/field_mask.proto\"^\n!GetOrganizationPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x89\x01\n\"GetOrganizationPreferencesResponse\x12\x63\n\x18organization_preferences\x18\x01 \x01(\x0b\x32(.api.commons.org.OrganizationPreferencesR\x17organizationPreferences\"\xc6\x01\n$UpdateOrganizationPreferencesRequest\x12\x63\n\x18organization_preferences\x18\x01 \x01(\x0b\x32(.api.commons.org.OrganizationPreferencesR\x17organizationPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\'\n%UpdateOrganizationPreferencesResponse\"W\n\x1aGetAgentPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"m\n\x1bGetAgentPreferencesResponse\x12N\n\x11\x61gent_preferences\x18\x01 \x01(\x0b\x32!.api.commons.org.AgentPreferencesR\x10\x61gentPreferences\"\xaa\x01\n\x1dUpdateAgentPreferencesRequest\x12N\n\x11\x61gent_preferences\x18\x01 \x01(\x0b\x32!.api.commons.org.AgentPreferencesR\x10\x61gentPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\" \n\x1eUpdateAgentPreferencesResponse\"Y\n\x1cGetContactPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"u\n\x1dGetContactPreferencesResponse\x12T\n\x13\x63ontact_preferences\x18\x01 \x01(\x0b\x32#.api.commons.org.ContactPreferencesR\x12\x63ontactPreferences\"\xb2\x01\n\x1fUpdateContactPreferencesRequest\x12T\n\x13\x63ontact_preferences\x18\x01 \x01(\x0b\x32#.api.commons.org.ContactPreferencesR\x12\x63ontactPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\"\n UpdateContactPreferencesResponse\"`\n#GetAuthenticationPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x91\x01\n$GetAuthenticationPreferencesResponse\x12i\n\x1a\x61uthentication_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.AuthenticationPreferencesR\x19\x61uthenticationPreferences\"\xfa\x01\n&UpdateAuthenticationPreferencesRequest\x12i\n\x1a\x61uthentication_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.AuthenticationPreferencesR\x19\x61uthenticationPreferences\x12*\n\x11\x64uo_client_secret\x18\x05 \x01(\tR\x0f\x64uoClientSecret\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\")\n\'UpdateAuthenticationPreferencesResponse\"Y\n\x1cGetWebhookPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"u\n\x1dGetWebhookPreferencesResponse\x12T\n\x13webhook_preferences\x18\x01 \x01(\x0b\x32#.api.commons.org.WebhookPreferencesR\x12webhookPreferences\"\xb2\x01\n\x1fUpdateWebhookPreferencesRequest\x12T\n\x13webhook_preferences\x18\x01 \x01(\x0b\x32#.api.commons.org.WebhookPreferencesR\x12webhookPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\"\n UpdateWebhookPreferencesResponse\"b\n%GetDashboardGeneralPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x84\x01\n&GetDashboardGeneralPreferencesResponse\x12Z\n\x15\x64\x61shboard_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.DashboardPreferencesR\x14\x64\x61shboardPreferences\"\xc1\x01\n(UpdateDashboardGeneralPreferencesRequest\x12Z\n\x15\x64\x61shboard_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.DashboardPreferencesR\x14\x64\x61shboardPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"+\n)UpdateDashboardGeneralPreferencesResponse\"`\n#GetDashboardQueuePreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x92\x01\n$GetDashboardQueuePreferencesResponse\x12j\n\x1b\x64\x61shboard_queue_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.DashboardQueuePreferencesR\x19\x64\x61shboardQueuePreferences\"\xcf\x01\n&UpdateDashboardQueuePreferencesRequest\x12j\n\x1b\x64\x61shboard_queue_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.DashboardQueuePreferencesR\x19\x64\x61shboardQueuePreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\")\n\'UpdateDashboardQueuePreferencesResponse\"W\n\x1aGetPhonePreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"m\n\x1bGetPhonePreferencesResponse\x12N\n\x11phone_preferences\x18\x01 \x01(\x0b\x32!.api.commons.org.PhonePreferencesR\x10phonePreferences\"\xaa\x01\n\x1dUpdatePhonePreferencesRequest\x12N\n\x11phone_preferences\x18\x01 \x01(\x0b\x32!.api.commons.org.PhonePreferencesR\x10phonePreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\" \n\x1eUpdatePhonePreferencesResponse\"a\n\x12PhonePreferencesDB\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x34\n\x16phone_preferences_json\x18\n \x01(\tR\x14phonePreferencesJson\"\\\n\x1fGetCompliancePreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x81\x01\n GetCompliancePreferencesResponse\x12]\n\x16\x63ompliance_preferences\x18\x01 \x01(\x0b\x32&.api.commons.org.CompliancePreferencesR\x15\x63ompliancePreferences\"\xbe\x01\n\"UpdateCompliancePreferencesRequest\x12]\n\x16\x63ompliance_preferences\x18\x01 \x01(\x0b\x32&.api.commons.org.CompliancePreferencesR\x15\x63ompliancePreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"%\n#UpdateCompliancePreferencesResponse\"[\n\x1eGetBroadcastPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"}\n\x1fGetBroadcastPreferencesResponse\x12Z\n\x15\x62roadcast_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.BroadcastPreferencesR\x14\x62roadcastPreferences\"\xba\x01\n!UpdateBroadcastPreferencesRequest\x12Z\n\x15\x62roadcast_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.BroadcastPreferencesR\x14\x62roadcastPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"$\n\"UpdateBroadcastPreferencesResponse\"Z\n\x1dGetSchedulePreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"y\n\x1eGetSchedulePreferencesResponse\x12W\n\x14schedule_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.SchedulePreferencesR\x13schedulePreferences\"\xb6\x01\n UpdateSchedulePreferencesRequest\x12W\n\x14schedule_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.SchedulePreferencesR\x13schedulePreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"#\n!UpdateSchedulePreferencesResponse\"Z\n\x1dGetEmailSmsPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"z\n\x1eGetEmailSmsPreferencesResponse\x12X\n\x15\x65mail_sms_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.EmailSmsPreferencesR\x13\x65mailSmsPreferences\"\xb7\x01\n UpdateEmailSmsPreferencesRequest\x12X\n\x15\x65mail_sms_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.EmailSmsPreferencesR\x13\x65mailSmsPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"#\n!UpdateEmailSmsPreferencesResponse\"Z\n\x1dGetBusinessPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"y\n\x1eGetBusinessPreferencesResponse\x12W\n\x14\x62usiness_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.BusinessPreferencesR\x13\x62usinessPreferences\"\xb6\x01\n UpdateBusinessPreferencesRequest\x12W\n\x14\x62usiness_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.BusinessPreferencesR\x13\x62usinessPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"#\n!UpdateBusinessPreferencesResponse\"\xd2\x01\n%UpdateAdminBusinessPreferencesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12W\n\x14\x62usiness_preferences\x18\x02 \x01(\x0b\x32$.api.commons.org.BusinessPreferencesR\x13\x62usinessPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"(\n&UpdateAdminBusinessPreferencesResponse\"s\n\x1fGetScorecardsPreferencesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x81\x01\n GetScorecardsPreferencesResponse\x12]\n\x16scorecards_preferences\x18\x01 \x01(\x0b\x32&.api.commons.org.ScorecardsPreferencesR\x15scorecardsPreferences\"\xd5\x01\n\"UpdateScorecardsPreferencesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12]\n\x16scorecards_preferences\x18\x02 \x01(\x0b\x32&.api.commons.org.ScorecardsPreferencesR\x15scorecardsPreferences\x12\x39\n\nfield_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"%\n#UpdateScorecardsPreferencesResponse\"`\n#GetVoiceAnalyticsPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x92\x01\n$GetVoiceAnalyticsPreferencesResponse\x12j\n\x1bvoice_analytics_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.VoiceAnalyticsPreferencesR\x19voiceAnalyticsPreferences\"&\n$ListVoiceAnalyticsPreferencesRequest\"\x93\x01\n%ListVoiceAnalyticsPreferencesResponse\x12j\n\x1bvoice_analytics_preferences\x18\x01 \x03(\x0b\x32*.api.commons.org.VoiceAnalyticsPreferencesR\x19voiceAnalyticsPreferences\"\xcf\x01\n&UpdateVoiceAnalyticsPreferencesRequest\x12j\n\x1bvoice_analytics_preferences\x18\x01 \x01(\x0b\x32*.api.commons.org.VoiceAnalyticsPreferencesR\x19voiceAnalyticsPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\")\n\'UpdateVoiceAnalyticsPreferencesResponse\"Z\n\x1dGetEndOfDayPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"{\n\x1eGetEndOfDayPreferencesResponse\x12Y\n\x16\x65nd_of_day_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.EndOfDayPreferencesR\x13\x65ndOfDayPreferences\"\xb8\x01\n UpdateEndOfDayPreferencesRequest\x12Y\n\x16\x65nd_of_day_preferences\x18\x01 \x01(\x0b\x32$.api.commons.org.EndOfDayPreferencesR\x13\x65ndOfDayPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"#\n!UpdateEndOfDayPreferencesResponse\"X\n\x1bGetFilterPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"q\n\x1cGetFilterPreferencesResponse\x12Q\n\x12\x66ilter_preferences\x18\x01 \x01(\x0b\x32\".api.commons.org.FilterPreferencesR\x11\x66ilterPreferences\"\xae\x01\n\x1eUpdateFilterPreferencesRequest\x12Q\n\x12\x66ilter_preferences\x18\x01 \x01(\x0b\x32\".api.commons.org.FilterPreferencesR\x11\x66ilterPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"!\n\x1fUpdateFilterPreferencesResponse\"[\n\x1eGetRecordingPreferencesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"}\n\x1fGetRecordingPreferencesResponse\x12Z\n\x15recording_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.RecordingPreferencesR\x14recordingPreferences\"\xba\x01\n!UpdateRecordingPreferencesRequest\x12Z\n\x15recording_preferences\x18\x01 \x01(\x0b\x32%.api.commons.org.RecordingPreferencesR\x14recordingPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"$\n\"UpdateRecordingPreferencesResponse\"t\n GetAdminClientPreferencesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x86\x01\n!GetAdminClientPreferencesResponse\x12\x61\n\x18\x61\x64min_client_preferences\x18\x01 \x01(\x0b\x32\'.api.commons.org.AdminClientPreferencesR\x16\x61\x64minClientPreferences\"\xda\x01\n#UpdateAdminClientPreferencesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x61\n\x18\x61\x64min_client_preferences\x18\x02 \x01(\x0b\x32\'.api.commons.org.AdminClientPreferencesR\x16\x61\x64minClientPreferences\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"&\n$UpdateAdminClientPreferencesResponse\"%\n#AcceptLinkbackRecordingTermsRequest\"&\n$AcceptLinkbackRecordingTermsResponse\"?\n\'LinkbackUpdateBroadcastTemplatesRequest\x12\x14\n\x05value\x18\x01 \x01(\x08R\x05value\"*\n(LinkbackUpdateBroadcastTemplatesResponse\".\n,RecordEmailUnsubscribeAcknowledgementRequest\"/\n-RecordEmailUnsubscribeAcknowledgementResponse\"-\n+ClearEmailUnsubscribeAcknowledgementRequest\".\n,ClearEmailUnsubscribeAcknowledgementResponse\"g\n\x1a\x43reateBusinessHoursRequest\x12\x45\n\x0e\x62usiness_hours\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.BusinessHoursR\rbusinessHours:\x02\x18\x01\"M\n\x1b\x43reateBusinessHoursResponse\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId:\x02\x18\x01\"g\n\x1aUpdateBusinessHoursRequest\x12\x45\n\x0e\x62usiness_hours\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.BusinessHoursR\rbusinessHours:\x02\x18\x01\"!\n\x1bUpdateBusinessHoursResponse:\x02\x18\x01\"\x1e\n\x18ListBusinessHoursRequest:\x02\x18\x01\"\x82\x01\n\x19ListBusinessHoursResponse\x12\x45\n\x0e\x62usiness_hours\x18\x02 \x03(\x0b\x32\x1e.api.commons.org.BusinessHoursR\rbusinessHours:\x02\x18\x01J\x04\x08\x01\x10\x02R\x14\x62usiness_hours_lists\"I\n\x17GetBusinessHoursRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId:\x02\x18\x01\"e\n\x18GetBusinessHoursResponse\x12\x45\n\x0e\x62usiness_hours\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.BusinessHoursR\rbusinessHours:\x02\x18\x01\"\xe5\x01\n\x17SetBusinessHoursRequest\x12.\n\x13\x62usiness_hours_name\x18\x01 \x01(\tR\x11\x62usinessHoursName\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x41\n\rday_intervals\x18\x03 \x03(\x0b\x32\x1c.api.commons.org.DayIntervalR\x0c\x64\x61yIntervals\x12\x31\n\x08timezone\x18\x04 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone:\x02\x18\x01\"J\n\x18SetBusinessHoursResponse\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId:\x02\x18\x01\"\x94\x01\n!AddIntervalToBusinessHoursRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId\x12?\n\x0c\x64\x61y_interval\x18\x02 \x01(\x0b\x32\x1c.api.commons.org.DayIntervalR\x0b\x64\x61yInterval:\x02\x18\x01\"(\n\"AddIntervalToBusinessHoursResponse:\x02\x18\x01\"\x99\x01\n&RemoveIntervalFromBusinessHoursRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId\x12?\n\x0c\x64\x61y_interval\x18\x02 \x01(\x0b\x32\x1c.api.commons.org.DayIntervalR\x0b\x64\x61yInterval:\x02\x18\x01\"-\n\'RemoveIntervalFromBusinessHoursResponse:\x02\x18\x01\"\x90\x02\n\x1eUpdateBusinessHoursInfoRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId\x12.\n\x13\x62usiness_hours_name\x18\x02 \x01(\tR\x11\x62usinessHoursName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x31\n\x08timezone\x18\x04 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask:\x02\x18\x01\"%\n\x1fUpdateBusinessHoursInfoResponse:\x02\x18\x01\"L\n\x1a\x44\x65leteBusinessHoursRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId:\x02\x18\x01\"!\n\x1b\x44\x65leteBusinessHoursResponse:\x02\x18\x01\"N\n\x1c\x45valuateBusinessHoursRequest\x12*\n\x11\x62usiness_hours_id\x18\x01 \x01(\tR\x0f\x62usinessHoursId:\x02\x18\x01\"F\n\x1d\x45valuateBusinessHoursResponse\x12!\n\x0cwithin_range\x18\x01 \x01(\x08R\x0bwithinRange:\x02\x18\x01\"X\n\x1c\x43reateCertificateInfoRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription:\x02\x18\x01\"T\n\x1d\x43reateCertificateInfoResponse\x12/\n\x13\x65ncoded_certificate\x18\x01 \x01(\tR\x12\x65ncodedCertificate:\x02\x18\x01\"R\n\x1c\x44\x65leteCertificateInfoRequest\x12.\n\x13\x63\x65rtificate_info_id\x18\x01 \x01(\tR\x11\x63\x65rtificateInfoId:\x02\x18\x01\"#\n\x1d\x44\x65leteCertificateInfoResponse:\x02\x18\x01\"R\n\x1cRevokeCertificateInfoRequest\x12.\n\x13\x63\x65rtificate_info_id\x18\x01 \x01(\tR\x11\x63\x65rtificateInfoId:\x02\x18\x01\"#\n\x1dRevokeCertificateInfoResponse:\x02\x18\x01\" \n\x1aListCertificateInfoRequest:\x02\x18\x01\"w\n\x1bListCertificateInfoResponse\x12T\n\x15\x63\x65rtificate_info_list\x18\x01 \x03(\x0b\x32 .api.commons.org.CertificateInfoR\x13\x63\x65rtificateInfoList:\x02\x18\x01\x42\x8a\x01\n\x14\x63om.api.v1alpha1.orgB\x10PreferencesProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.preferences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\020PreferencesProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_CREATEBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_CREATEBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_CREATEBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_CREATEBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_UPDATEBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_UPDATEBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_UPDATEBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_UPDATEBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_LISTBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_LISTBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_LISTBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_LISTBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_GETBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_GETBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_GETBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_GETBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_SETBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_SETBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_SETBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_SETBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_ADDINTERVALTOBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_ADDINTERVALTOBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_ADDINTERVALTOBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_ADDINTERVALTOBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_UPDATEBUSINESSHOURSINFOREQUEST']._loaded_options = None
  _globals['_UPDATEBUSINESSHOURSINFOREQUEST']._serialized_options = b'\030\001'
  _globals['_UPDATEBUSINESSHOURSINFORESPONSE']._loaded_options = None
  _globals['_UPDATEBUSINESSHOURSINFORESPONSE']._serialized_options = b'\030\001'
  _globals['_DELETEBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_DELETEBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_DELETEBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_DELETEBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_EVALUATEBUSINESSHOURSREQUEST']._loaded_options = None
  _globals['_EVALUATEBUSINESSHOURSREQUEST']._serialized_options = b'\030\001'
  _globals['_EVALUATEBUSINESSHOURSRESPONSE']._loaded_options = None
  _globals['_EVALUATEBUSINESSHOURSRESPONSE']._serialized_options = b'\030\001'
  _globals['_CREATECERTIFICATEINFOREQUEST']._loaded_options = None
  _globals['_CREATECERTIFICATEINFOREQUEST']._serialized_options = b'\030\001'
  _globals['_CREATECERTIFICATEINFORESPONSE']._loaded_options = None
  _globals['_CREATECERTIFICATEINFORESPONSE']._serialized_options = b'\030\001'
  _globals['_DELETECERTIFICATEINFOREQUEST']._loaded_options = None
  _globals['_DELETECERTIFICATEINFOREQUEST']._serialized_options = b'\030\001'
  _globals['_DELETECERTIFICATEINFORESPONSE']._loaded_options = None
  _globals['_DELETECERTIFICATEINFORESPONSE']._serialized_options = b'\030\001'
  _globals['_REVOKECERTIFICATEINFOREQUEST']._loaded_options = None
  _globals['_REVOKECERTIFICATEINFOREQUEST']._serialized_options = b'\030\001'
  _globals['_REVOKECERTIFICATEINFORESPONSE']._loaded_options = None
  _globals['_REVOKECERTIFICATEINFORESPONSE']._serialized_options = b'\030\001'
  _globals['_LISTCERTIFICATEINFOREQUEST']._loaded_options = None
  _globals['_LISTCERTIFICATEINFOREQUEST']._serialized_options = b'\030\001'
  _globals['_LISTCERTIFICATEINFORESPONSE']._loaded_options = None
  _globals['_LISTCERTIFICATEINFORESPONSE']._serialized_options = b'\030\001'
  _globals['_GETORGANIZATIONPREFERENCESREQUEST']._serialized_start=148
  _globals['_GETORGANIZATIONPREFERENCESREQUEST']._serialized_end=242
  _globals['_GETORGANIZATIONPREFERENCESRESPONSE']._serialized_start=245
  _globals['_GETORGANIZATIONPREFERENCESRESPONSE']._serialized_end=382
  _globals['_UPDATEORGANIZATIONPREFERENCESREQUEST']._serialized_start=385
  _globals['_UPDATEORGANIZATIONPREFERENCESREQUEST']._serialized_end=583
  _globals['_UPDATEORGANIZATIONPREFERENCESRESPONSE']._serialized_start=585
  _globals['_UPDATEORGANIZATIONPREFERENCESRESPONSE']._serialized_end=624
  _globals['_GETAGENTPREFERENCESREQUEST']._serialized_start=626
  _globals['_GETAGENTPREFERENCESREQUEST']._serialized_end=713
  _globals['_GETAGENTPREFERENCESRESPONSE']._serialized_start=715
  _globals['_GETAGENTPREFERENCESRESPONSE']._serialized_end=824
  _globals['_UPDATEAGENTPREFERENCESREQUEST']._serialized_start=827
  _globals['_UPDATEAGENTPREFERENCESREQUEST']._serialized_end=997
  _globals['_UPDATEAGENTPREFERENCESRESPONSE']._serialized_start=999
  _globals['_UPDATEAGENTPREFERENCESRESPONSE']._serialized_end=1031
  _globals['_GETCONTACTPREFERENCESREQUEST']._serialized_start=1033
  _globals['_GETCONTACTPREFERENCESREQUEST']._serialized_end=1122
  _globals['_GETCONTACTPREFERENCESRESPONSE']._serialized_start=1124
  _globals['_GETCONTACTPREFERENCESRESPONSE']._serialized_end=1241
  _globals['_UPDATECONTACTPREFERENCESREQUEST']._serialized_start=1244
  _globals['_UPDATECONTACTPREFERENCESREQUEST']._serialized_end=1422
  _globals['_UPDATECONTACTPREFERENCESRESPONSE']._serialized_start=1424
  _globals['_UPDATECONTACTPREFERENCESRESPONSE']._serialized_end=1458
  _globals['_GETAUTHENTICATIONPREFERENCESREQUEST']._serialized_start=1460
  _globals['_GETAUTHENTICATIONPREFERENCESREQUEST']._serialized_end=1556
  _globals['_GETAUTHENTICATIONPREFERENCESRESPONSE']._serialized_start=1559
  _globals['_GETAUTHENTICATIONPREFERENCESRESPONSE']._serialized_end=1704
  _globals['_UPDATEAUTHENTICATIONPREFERENCESREQUEST']._serialized_start=1707
  _globals['_UPDATEAUTHENTICATIONPREFERENCESREQUEST']._serialized_end=1957
  _globals['_UPDATEAUTHENTICATIONPREFERENCESRESPONSE']._serialized_start=1959
  _globals['_UPDATEAUTHENTICATIONPREFERENCESRESPONSE']._serialized_end=2000
  _globals['_GETWEBHOOKPREFERENCESREQUEST']._serialized_start=2002
  _globals['_GETWEBHOOKPREFERENCESREQUEST']._serialized_end=2091
  _globals['_GETWEBHOOKPREFERENCESRESPONSE']._serialized_start=2093
  _globals['_GETWEBHOOKPREFERENCESRESPONSE']._serialized_end=2210
  _globals['_UPDATEWEBHOOKPREFERENCESREQUEST']._serialized_start=2213
  _globals['_UPDATEWEBHOOKPREFERENCESREQUEST']._serialized_end=2391
  _globals['_UPDATEWEBHOOKPREFERENCESRESPONSE']._serialized_start=2393
  _globals['_UPDATEWEBHOOKPREFERENCESRESPONSE']._serialized_end=2427
  _globals['_GETDASHBOARDGENERALPREFERENCESREQUEST']._serialized_start=2429
  _globals['_GETDASHBOARDGENERALPREFERENCESREQUEST']._serialized_end=2527
  _globals['_GETDASHBOARDGENERALPREFERENCESRESPONSE']._serialized_start=2530
  _globals['_GETDASHBOARDGENERALPREFERENCESRESPONSE']._serialized_end=2662
  _globals['_UPDATEDASHBOARDGENERALPREFERENCESREQUEST']._serialized_start=2665
  _globals['_UPDATEDASHBOARDGENERALPREFERENCESREQUEST']._serialized_end=2858
  _globals['_UPDATEDASHBOARDGENERALPREFERENCESRESPONSE']._serialized_start=2860
  _globals['_UPDATEDASHBOARDGENERALPREFERENCESRESPONSE']._serialized_end=2903
  _globals['_GETDASHBOARDQUEUEPREFERENCESREQUEST']._serialized_start=2905
  _globals['_GETDASHBOARDQUEUEPREFERENCESREQUEST']._serialized_end=3001
  _globals['_GETDASHBOARDQUEUEPREFERENCESRESPONSE']._serialized_start=3004
  _globals['_GETDASHBOARDQUEUEPREFERENCESRESPONSE']._serialized_end=3150
  _globals['_UPDATEDASHBOARDQUEUEPREFERENCESREQUEST']._serialized_start=3153
  _globals['_UPDATEDASHBOARDQUEUEPREFERENCESREQUEST']._serialized_end=3360
  _globals['_UPDATEDASHBOARDQUEUEPREFERENCESRESPONSE']._serialized_start=3362
  _globals['_UPDATEDASHBOARDQUEUEPREFERENCESRESPONSE']._serialized_end=3403
  _globals['_GETPHONEPREFERENCESREQUEST']._serialized_start=3405
  _globals['_GETPHONEPREFERENCESREQUEST']._serialized_end=3492
  _globals['_GETPHONEPREFERENCESRESPONSE']._serialized_start=3494
  _globals['_GETPHONEPREFERENCESRESPONSE']._serialized_end=3603
  _globals['_UPDATEPHONEPREFERENCESREQUEST']._serialized_start=3606
  _globals['_UPDATEPHONEPREFERENCESREQUEST']._serialized_end=3776
  _globals['_UPDATEPHONEPREFERENCESRESPONSE']._serialized_start=3778
  _globals['_UPDATEPHONEPREFERENCESRESPONSE']._serialized_end=3810
  _globals['_PHONEPREFERENCESDB']._serialized_start=3812
  _globals['_PHONEPREFERENCESDB']._serialized_end=3909
  _globals['_GETCOMPLIANCEPREFERENCESREQUEST']._serialized_start=3911
  _globals['_GETCOMPLIANCEPREFERENCESREQUEST']._serialized_end=4003
  _globals['_GETCOMPLIANCEPREFERENCESRESPONSE']._serialized_start=4006
  _globals['_GETCOMPLIANCEPREFERENCESRESPONSE']._serialized_end=4135
  _globals['_UPDATECOMPLIANCEPREFERENCESREQUEST']._serialized_start=4138
  _globals['_UPDATECOMPLIANCEPREFERENCESREQUEST']._serialized_end=4328
  _globals['_UPDATECOMPLIANCEPREFERENCESRESPONSE']._serialized_start=4330
  _globals['_UPDATECOMPLIANCEPREFERENCESRESPONSE']._serialized_end=4367
  _globals['_GETBROADCASTPREFERENCESREQUEST']._serialized_start=4369
  _globals['_GETBROADCASTPREFERENCESREQUEST']._serialized_end=4460
  _globals['_GETBROADCASTPREFERENCESRESPONSE']._serialized_start=4462
  _globals['_GETBROADCASTPREFERENCESRESPONSE']._serialized_end=4587
  _globals['_UPDATEBROADCASTPREFERENCESREQUEST']._serialized_start=4590
  _globals['_UPDATEBROADCASTPREFERENCESREQUEST']._serialized_end=4776
  _globals['_UPDATEBROADCASTPREFERENCESRESPONSE']._serialized_start=4778
  _globals['_UPDATEBROADCASTPREFERENCESRESPONSE']._serialized_end=4814
  _globals['_GETSCHEDULEPREFERENCESREQUEST']._serialized_start=4816
  _globals['_GETSCHEDULEPREFERENCESREQUEST']._serialized_end=4906
  _globals['_GETSCHEDULEPREFERENCESRESPONSE']._serialized_start=4908
  _globals['_GETSCHEDULEPREFERENCESRESPONSE']._serialized_end=5029
  _globals['_UPDATESCHEDULEPREFERENCESREQUEST']._serialized_start=5032
  _globals['_UPDATESCHEDULEPREFERENCESREQUEST']._serialized_end=5214
  _globals['_UPDATESCHEDULEPREFERENCESRESPONSE']._serialized_start=5216
  _globals['_UPDATESCHEDULEPREFERENCESRESPONSE']._serialized_end=5251
  _globals['_GETEMAILSMSPREFERENCESREQUEST']._serialized_start=5253
  _globals['_GETEMAILSMSPREFERENCESREQUEST']._serialized_end=5343
  _globals['_GETEMAILSMSPREFERENCESRESPONSE']._serialized_start=5345
  _globals['_GETEMAILSMSPREFERENCESRESPONSE']._serialized_end=5467
  _globals['_UPDATEEMAILSMSPREFERENCESREQUEST']._serialized_start=5470
  _globals['_UPDATEEMAILSMSPREFERENCESREQUEST']._serialized_end=5653
  _globals['_UPDATEEMAILSMSPREFERENCESRESPONSE']._serialized_start=5655
  _globals['_UPDATEEMAILSMSPREFERENCESRESPONSE']._serialized_end=5690
  _globals['_GETBUSINESSPREFERENCESREQUEST']._serialized_start=5692
  _globals['_GETBUSINESSPREFERENCESREQUEST']._serialized_end=5782
  _globals['_GETBUSINESSPREFERENCESRESPONSE']._serialized_start=5784
  _globals['_GETBUSINESSPREFERENCESRESPONSE']._serialized_end=5905
  _globals['_UPDATEBUSINESSPREFERENCESREQUEST']._serialized_start=5908
  _globals['_UPDATEBUSINESSPREFERENCESREQUEST']._serialized_end=6090
  _globals['_UPDATEBUSINESSPREFERENCESRESPONSE']._serialized_start=6092
  _globals['_UPDATEBUSINESSPREFERENCESRESPONSE']._serialized_end=6127
  _globals['_UPDATEADMINBUSINESSPREFERENCESREQUEST']._serialized_start=6130
  _globals['_UPDATEADMINBUSINESSPREFERENCESREQUEST']._serialized_end=6340
  _globals['_UPDATEADMINBUSINESSPREFERENCESRESPONSE']._serialized_start=6342
  _globals['_UPDATEADMINBUSINESSPREFERENCESRESPONSE']._serialized_end=6382
  _globals['_GETSCORECARDSPREFERENCESREQUEST']._serialized_start=6384
  _globals['_GETSCORECARDSPREFERENCESREQUEST']._serialized_end=6499
  _globals['_GETSCORECARDSPREFERENCESRESPONSE']._serialized_start=6502
  _globals['_GETSCORECARDSPREFERENCESRESPONSE']._serialized_end=6631
  _globals['_UPDATESCORECARDSPREFERENCESREQUEST']._serialized_start=6634
  _globals['_UPDATESCORECARDSPREFERENCESREQUEST']._serialized_end=6847
  _globals['_UPDATESCORECARDSPREFERENCESRESPONSE']._serialized_start=6849
  _globals['_UPDATESCORECARDSPREFERENCESRESPONSE']._serialized_end=6886
  _globals['_GETVOICEANALYTICSPREFERENCESREQUEST']._serialized_start=6888
  _globals['_GETVOICEANALYTICSPREFERENCESREQUEST']._serialized_end=6984
  _globals['_GETVOICEANALYTICSPREFERENCESRESPONSE']._serialized_start=6987
  _globals['_GETVOICEANALYTICSPREFERENCESRESPONSE']._serialized_end=7133
  _globals['_LISTVOICEANALYTICSPREFERENCESREQUEST']._serialized_start=7135
  _globals['_LISTVOICEANALYTICSPREFERENCESREQUEST']._serialized_end=7173
  _globals['_LISTVOICEANALYTICSPREFERENCESRESPONSE']._serialized_start=7176
  _globals['_LISTVOICEANALYTICSPREFERENCESRESPONSE']._serialized_end=7323
  _globals['_UPDATEVOICEANALYTICSPREFERENCESREQUEST']._serialized_start=7326
  _globals['_UPDATEVOICEANALYTICSPREFERENCESREQUEST']._serialized_end=7533
  _globals['_UPDATEVOICEANALYTICSPREFERENCESRESPONSE']._serialized_start=7535
  _globals['_UPDATEVOICEANALYTICSPREFERENCESRESPONSE']._serialized_end=7576
  _globals['_GETENDOFDAYPREFERENCESREQUEST']._serialized_start=7578
  _globals['_GETENDOFDAYPREFERENCESREQUEST']._serialized_end=7668
  _globals['_GETENDOFDAYPREFERENCESRESPONSE']._serialized_start=7670
  _globals['_GETENDOFDAYPREFERENCESRESPONSE']._serialized_end=7793
  _globals['_UPDATEENDOFDAYPREFERENCESREQUEST']._serialized_start=7796
  _globals['_UPDATEENDOFDAYPREFERENCESREQUEST']._serialized_end=7980
  _globals['_UPDATEENDOFDAYPREFERENCESRESPONSE']._serialized_start=7982
  _globals['_UPDATEENDOFDAYPREFERENCESRESPONSE']._serialized_end=8017
  _globals['_GETFILTERPREFERENCESREQUEST']._serialized_start=8019
  _globals['_GETFILTERPREFERENCESREQUEST']._serialized_end=8107
  _globals['_GETFILTERPREFERENCESRESPONSE']._serialized_start=8109
  _globals['_GETFILTERPREFERENCESRESPONSE']._serialized_end=8222
  _globals['_UPDATEFILTERPREFERENCESREQUEST']._serialized_start=8225
  _globals['_UPDATEFILTERPREFERENCESREQUEST']._serialized_end=8399
  _globals['_UPDATEFILTERPREFERENCESRESPONSE']._serialized_start=8401
  _globals['_UPDATEFILTERPREFERENCESRESPONSE']._serialized_end=8434
  _globals['_GETRECORDINGPREFERENCESREQUEST']._serialized_start=8436
  _globals['_GETRECORDINGPREFERENCESREQUEST']._serialized_end=8527
  _globals['_GETRECORDINGPREFERENCESRESPONSE']._serialized_start=8529
  _globals['_GETRECORDINGPREFERENCESRESPONSE']._serialized_end=8654
  _globals['_UPDATERECORDINGPREFERENCESREQUEST']._serialized_start=8657
  _globals['_UPDATERECORDINGPREFERENCESREQUEST']._serialized_end=8843
  _globals['_UPDATERECORDINGPREFERENCESRESPONSE']._serialized_start=8845
  _globals['_UPDATERECORDINGPREFERENCESRESPONSE']._serialized_end=8881
  _globals['_GETADMINCLIENTPREFERENCESREQUEST']._serialized_start=8883
  _globals['_GETADMINCLIENTPREFERENCESREQUEST']._serialized_end=8999
  _globals['_GETADMINCLIENTPREFERENCESRESPONSE']._serialized_start=9002
  _globals['_GETADMINCLIENTPREFERENCESRESPONSE']._serialized_end=9136
  _globals['_UPDATEADMINCLIENTPREFERENCESREQUEST']._serialized_start=9139
  _globals['_UPDATEADMINCLIENTPREFERENCESREQUEST']._serialized_end=9357
  _globals['_UPDATEADMINCLIENTPREFERENCESRESPONSE']._serialized_start=9359
  _globals['_UPDATEADMINCLIENTPREFERENCESRESPONSE']._serialized_end=9397
  _globals['_ACCEPTLINKBACKRECORDINGTERMSREQUEST']._serialized_start=9399
  _globals['_ACCEPTLINKBACKRECORDINGTERMSREQUEST']._serialized_end=9436
  _globals['_ACCEPTLINKBACKRECORDINGTERMSRESPONSE']._serialized_start=9438
  _globals['_ACCEPTLINKBACKRECORDINGTERMSRESPONSE']._serialized_end=9476
  _globals['_LINKBACKUPDATEBROADCASTTEMPLATESREQUEST']._serialized_start=9478
  _globals['_LINKBACKUPDATEBROADCASTTEMPLATESREQUEST']._serialized_end=9541
  _globals['_LINKBACKUPDATEBROADCASTTEMPLATESRESPONSE']._serialized_start=9543
  _globals['_LINKBACKUPDATEBROADCASTTEMPLATESRESPONSE']._serialized_end=9585
  _globals['_RECORDEMAILUNSUBSCRIBEACKNOWLEDGEMENTREQUEST']._serialized_start=9587
  _globals['_RECORDEMAILUNSUBSCRIBEACKNOWLEDGEMENTREQUEST']._serialized_end=9633
  _globals['_RECORDEMAILUNSUBSCRIBEACKNOWLEDGEMENTRESPONSE']._serialized_start=9635
  _globals['_RECORDEMAILUNSUBSCRIBEACKNOWLEDGEMENTRESPONSE']._serialized_end=9682
  _globals['_CLEAREMAILUNSUBSCRIBEACKNOWLEDGEMENTREQUEST']._serialized_start=9684
  _globals['_CLEAREMAILUNSUBSCRIBEACKNOWLEDGEMENTREQUEST']._serialized_end=9729
  _globals['_CLEAREMAILUNSUBSCRIBEACKNOWLEDGEMENTRESPONSE']._serialized_start=9731
  _globals['_CLEAREMAILUNSUBSCRIBEACKNOWLEDGEMENTRESPONSE']._serialized_end=9777
  _globals['_CREATEBUSINESSHOURSREQUEST']._serialized_start=9779
  _globals['_CREATEBUSINESSHOURSREQUEST']._serialized_end=9882
  _globals['_CREATEBUSINESSHOURSRESPONSE']._serialized_start=9884
  _globals['_CREATEBUSINESSHOURSRESPONSE']._serialized_end=9961
  _globals['_UPDATEBUSINESSHOURSREQUEST']._serialized_start=9963
  _globals['_UPDATEBUSINESSHOURSREQUEST']._serialized_end=10066
  _globals['_UPDATEBUSINESSHOURSRESPONSE']._serialized_start=10068
  _globals['_UPDATEBUSINESSHOURSRESPONSE']._serialized_end=10101
  _globals['_LISTBUSINESSHOURSREQUEST']._serialized_start=10103
  _globals['_LISTBUSINESSHOURSREQUEST']._serialized_end=10133
  _globals['_LISTBUSINESSHOURSRESPONSE']._serialized_start=10136
  _globals['_LISTBUSINESSHOURSRESPONSE']._serialized_end=10266
  _globals['_GETBUSINESSHOURSREQUEST']._serialized_start=10268
  _globals['_GETBUSINESSHOURSREQUEST']._serialized_end=10341
  _globals['_GETBUSINESSHOURSRESPONSE']._serialized_start=10343
  _globals['_GETBUSINESSHOURSRESPONSE']._serialized_end=10444
  _globals['_SETBUSINESSHOURSREQUEST']._serialized_start=10447
  _globals['_SETBUSINESSHOURSREQUEST']._serialized_end=10676
  _globals['_SETBUSINESSHOURSRESPONSE']._serialized_start=10678
  _globals['_SETBUSINESSHOURSRESPONSE']._serialized_end=10752
  _globals['_ADDINTERVALTOBUSINESSHOURSREQUEST']._serialized_start=10755
  _globals['_ADDINTERVALTOBUSINESSHOURSREQUEST']._serialized_end=10903
  _globals['_ADDINTERVALTOBUSINESSHOURSRESPONSE']._serialized_start=10905
  _globals['_ADDINTERVALTOBUSINESSHOURSRESPONSE']._serialized_end=10945
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSREQUEST']._serialized_start=10948
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSREQUEST']._serialized_end=11101
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSRESPONSE']._serialized_start=11103
  _globals['_REMOVEINTERVALFROMBUSINESSHOURSRESPONSE']._serialized_end=11148
  _globals['_UPDATEBUSINESSHOURSINFOREQUEST']._serialized_start=11151
  _globals['_UPDATEBUSINESSHOURSINFOREQUEST']._serialized_end=11423
  _globals['_UPDATEBUSINESSHOURSINFORESPONSE']._serialized_start=11425
  _globals['_UPDATEBUSINESSHOURSINFORESPONSE']._serialized_end=11462
  _globals['_DELETEBUSINESSHOURSREQUEST']._serialized_start=11464
  _globals['_DELETEBUSINESSHOURSREQUEST']._serialized_end=11540
  _globals['_DELETEBUSINESSHOURSRESPONSE']._serialized_start=11542
  _globals['_DELETEBUSINESSHOURSRESPONSE']._serialized_end=11575
  _globals['_EVALUATEBUSINESSHOURSREQUEST']._serialized_start=11577
  _globals['_EVALUATEBUSINESSHOURSREQUEST']._serialized_end=11655
  _globals['_EVALUATEBUSINESSHOURSRESPONSE']._serialized_start=11657
  _globals['_EVALUATEBUSINESSHOURSRESPONSE']._serialized_end=11727
  _globals['_CREATECERTIFICATEINFOREQUEST']._serialized_start=11729
  _globals['_CREATECERTIFICATEINFOREQUEST']._serialized_end=11817
  _globals['_CREATECERTIFICATEINFORESPONSE']._serialized_start=11819
  _globals['_CREATECERTIFICATEINFORESPONSE']._serialized_end=11903
  _globals['_DELETECERTIFICATEINFOREQUEST']._serialized_start=11905
  _globals['_DELETECERTIFICATEINFOREQUEST']._serialized_end=11987
  _globals['_DELETECERTIFICATEINFORESPONSE']._serialized_start=11989
  _globals['_DELETECERTIFICATEINFORESPONSE']._serialized_end=12024
  _globals['_REVOKECERTIFICATEINFOREQUEST']._serialized_start=12026
  _globals['_REVOKECERTIFICATEINFOREQUEST']._serialized_end=12108
  _globals['_REVOKECERTIFICATEINFORESPONSE']._serialized_start=12110
  _globals['_REVOKECERTIFICATEINFORESPONSE']._serialized_end=12145
  _globals['_LISTCERTIFICATEINFOREQUEST']._serialized_start=12147
  _globals['_LISTCERTIFICATEINFOREQUEST']._serialized_end=12179
  _globals['_LISTCERTIFICATEINFORESPONSE']._serialized_start=12181
  _globals['_LISTCERTIFICATEINFORESPONSE']._serialized_end=12300
# @@protoc_insertion_point(module_scope)
