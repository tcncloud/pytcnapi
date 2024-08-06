# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org/preferences.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'api/commons/org/preferences.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import ana_pb2 as api_dot_commons_dot_ana__pb2
from api.commons import country_pb2 as api_dot_commons_dot_country__pb2
from api.commons import enums_pb2 as api_dot_commons_dot_enums__pb2
from api.commons import lms_pb2 as api_dot_commons_dot_lms__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons import org_preferences_pb2 as api_dot_commons_dot_org__preferences__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/commons/org/preferences.proto\x12\x0f\x61pi.commons.org\x1a\x15\x61pi/commons/ana.proto\x1a\x19\x61pi/commons/country.proto\x1a\x17\x61pi/commons/enums.proto\x1a\x15\x61pi/commons/lms.proto\x1a\x15\x61pi/commons/org.proto\x1a!api/commons/org_preferences.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbb\x02\n\x17OrganizationPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12=\n\x0f\x64\x65\x66\x61ult_country\x18\n \x01(\x0e\x32\x14.api.commons.CountryR\x0e\x64\x65\x66\x61ultCountry\x12\x32\n\ttime_zone\x18\x0b \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timeZone\x12G\n\x10\x64isplay_language\x18\x0c \x01(\x0e\x32\x1c.api.commons.DisplayLanguageR\x0f\x64isplayLanguage\x12M\n\x12locale_preferences\x18\r \x01(\x0b\x32\x1e.api.commons.LocalePreferencesR\x11localePreferences\"\x83\x04\n\x10\x41gentPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x31\n\x15\x64\x65\x66\x61ult_agent_dial_in\x18\n \x01(\tR\x12\x64\x65\x66\x61ultAgentDialIn\x12\x30\n\x14pbx_extension_length\x18\x0b \x01(\x05R\x12pbxExtensionLength\x12=\n\x1b\x64\x65\x66\x61ult_softphone_volume_in\x18\x0c \x01(\x05R\x18\x64\x65\x66\x61ultSoftphoneVolumeIn\x12?\n\x1c\x64\x65\x66\x61ult_softphone_volume_out\x18\r \x01(\x05R\x19\x64\x65\x66\x61ultSoftphoneVolumeOut\x12\x33\n\x16\x63onfig_dial_in_numbers\x18\x0e \x03(\tR\x13\x63onfigDialInNumbers\x12\x33\n\x16\x63lient_dial_in_numbers\x18\x0f \x03(\tR\x13\x63lientDialInNumbers\x12@\n\x1dmanual_dial_caller_id_privacy\x18\x10 \x01(\x08R\x19manualDialCallerIdPrivacy\x12G\n!use_manual_dial_caller_id_privacy\x18\x11 \x01(\x08R\x1cuseManualDialCallerIdPrivacy\"\xa5\x05\n\x12\x43ontactPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12`\n\x1d\x64\x65\x66\x61ult_contact_import_format\x18\n \x01(\x0b\x32\x1d.api.commons.org.ImportFormatR\x1a\x64\x65\x66\x61ultContactImportFormat\x12\x39\n\x19use_contact_import_format\x18\x0b \x01(\x08R\x16useContactImportFormat\x12[\n\x19\x64\x65\x66\x61ult_contact_area_code\x18\x0c \x01(\x0b\x32 .api.commons.org.ContactAreaCodeR\x16\x64\x65\x66\x61ultContactAreaCode\x12\x31\n\x15use_contact_area_code\x18\r \x01(\x08R\x12useContactAreaCode\x12\x61\n.discard_record_default_absent_numbers_handling\x18\x0e \x01(\x08R)discardRecordDefaultAbsentNumbersHandling\x12Q\n%default_contacts_import_randomization\x18\x0f \x01(\x08R\"defaultContactsImportRandomization\x12\x30\n\x14\x64\x65\x66\x61ult_email_column\x18\x10 \x01(\tR\x12\x64\x65\x66\x61ultEmailColumn\x12\x63\n\x1a\x64\x65\x66\x61ult_duplicate_handling\x18\x11 \x01(\x0e\x32%.api.commons.DefaultDuplicateHandlingR\x18\x64\x65\x66\x61ultDuplicateHandling\"\x98\x01\n\x0cImportFormat\x12?\n\x08standard\x18\x01 \x01(\x0e\x32!.api.commons.StandardImportFormatH\x00R\x08standard\x12=\n\x06\x63ustom\x18\x02 \x01(\x0b\x32#.api.commons.org.CustomImportFormatH\x00R\x06\x63ustomB\x08\n\x06\x66ormat\"8\n\x12\x43ustomImportFormat\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"v\n\x0f\x43ontactAreaCode\x12<\n\x03\x63\x66\x64\x18\x01 \x01(\x0b\x32(.api.commons.org.ContactFieldDescriptionH\x00R\x03\x63\x66\x64\x12\x18\n\x06\x63ustom\x18\x02 \x01(\x05H\x00R\x06\x63ustomB\x0b\n\tarea_code\"\x97\x01\n\x17\x43ontactFieldDescription\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1d\n\nfield_name\x18\x02 \x01(\tR\tfieldName\x12\x19\n\x08is_phone\x18\x03 \x01(\x08R\x07isPhone\x12\x32\n\x15\x64isplay_format_string\x18\x04 \x01(\tR\x13\x64isplayFormatString\"\x85\x07\n\x19\x41uthenticationPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x30\n\x14\x61uthorization_via_ip\x18\n \x01(\x08R\x12\x61uthorizationViaIp\x12\x1f\n\x0b\x61llowed_ips\x18\x0b \x03(\tR\nallowedIps\x12\"\n\ragent_api_key\x18\x0c \x01(\tR\x0b\x61gentApiKey\x12\x1d\n\nenable_2fa\x18\r \x01(\x08R\tenable2fa\x12\x34\n\x16\x62lock_unverified_users\x18\x0e \x01(\x08R\x14\x62lockUnverifiedUsers\x12i\n\x12\x65mail_mfa_settings\x18\x0f \x01(\x0b\x32;.api.commons.org.AuthenticationPreferences.EmailMfaSettingsR\x10\x65mailMfaSettings\x12\x63\n\x10\x64uo_mfa_settings\x18\x10 \x01(\x0b\x32\x39.api.commons.org.AuthenticationPreferences.DuoMfaSettingsR\x0e\x64uoMfaSettings\x12L\n#allow_force_password_reset_interval\x18\x11 \x01(\x08R\x1f\x61llowForcePasswordResetInterval\x12=\n\x1bpassword_reset_day_interval\x18\x12 \x01(\x05R\x18passwordResetDayInterval\x12\x39\n\x19user_authorization_via_ip\x18\x13 \x01(\x08R\x16userAuthorizationViaIp\x12,\n\x12\x66orce_sso_provider\x18\x14 \x01(\x08R\x10\x66orceSsoProvider\x12\x1f\n\x0b\x65nable_totp\x18\x15 \x01(\x08R\nenableTotp\x1ap\n\x0e\x44uoMfaSettings\x12\"\n\rduo_client_id\x18\x01 \x01(\tR\x0b\x64uoClientId\x12 \n\x0c\x64uo_api_host\x18\x02 \x01(\tR\nduoApiHost\x12\x18\n\x07\x65nabled\x18\x03 \x01(\x08R\x07\x65nabled\x1a,\n\x10\x45mailMfaSettings\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\"\xbf\x01\n\x12WebhookPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12*\n\x11push_urls_enabled\x18\n \x01(\x08R\x0fpushUrlsEnabled\x12/\n\x14\x63\x61ll_result_push_url\x18\x0b \x01(\tR\x11\x63\x61llResultPushUrl\x12\x35\n\x17\x61gent_response_push_url\x18\x0c \x01(\tR\x14\x61gentResponsePushUrl\"\xe5\x04\n\x14\x44\x61shboardPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12*\n\x11\x64\x65\x66\x61ult_info_view\x18\n \x01(\x08R\x0f\x64\x65\x66\x61ultInfoView\x12\x36\n\x17\x64\x65\x66\x61ult_table_inclusion\x18\x0b \x01(\x08R\x15\x64\x65\x66\x61ultTableInclusion\x12\x32\n\x15\x64\x65\x66\x61ult_info_grouping\x18\x0c \x01(\x08R\x13\x64\x65\x66\x61ultInfoGrouping\x12,\n\x12\x64\x65\x66\x61ult_small_icon\x18\r \x01(\x08R\x10\x64\x65\x66\x61ultSmallIcon\x12\x36\n\x17\x64\x65\x66\x61ult_descending_sort\x18\x0e \x01(\x08R\x15\x64\x65\x66\x61ultDescendingSort\x12,\n\x12table_template_sid\x18\x0f \x01(\x03R\x10tableTemplateSid\x12P\n\x12\x64\x65\x66\x61ult_call_types\x18\x10 \x01(\x0b\x32\".api.commons.org.IncludedCallTypesR\x10\x64\x65\x66\x61ultCallTypes\x12X\n\x1a\x64\x65\x66\x61ult_info_sort_by_value\x18\x11 \x01(\x0e\x32\x1c.api.commons.AgentInfoSortByR\x16\x64\x65\x66\x61ultInfoSortByValue\x12^\n\x1a\x64\x65\x66\x61ult_barge_in_filtering\x18\x12 \x01(\x0b\x32!.api.commons.org.BargeInFilteringR\x17\x64\x65\x66\x61ultBargeInFiltering\"\x8d\x01\n\x11IncludedCallTypes\x12\x1a\n\x08outbound\x18\x01 \x01(\x08R\x08outbound\x12\x18\n\x07inbound\x18\x02 \x01(\x08R\x07inbound\x12\x1f\n\x0bmanual_dial\x18\x03 \x01(\x08R\nmanualDial\x12!\n\x0cpreview_dial\x18\x04 \x01(\x08R\x0bpreviewDial\"\xf7\x03\n\x10\x42\x61rgeInFiltering\x12J\n\nhunt_group\x18\x01 \x01(\x0b\x32+.api.commons.org.BargeInFiltering.HuntGroupR\thuntGroup\x12P\n\x0c\x61gent_status\x18\x02 \x01(\x0b\x32-.api.commons.org.BargeInFiltering.AgentStatusR\x0b\x61gentStatus\x1a\x43\n\tHuntGroup\x12\x10\n\x03\x61ny\x18\x01 \x01(\x08R\x03\x61ny\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x1a\xff\x01\n\x0b\x41gentStatus\x12\x10\n\x03\x61ny\x18\x01 \x01(\x08R\x03\x61ny\x12\x18\n\x07waiting\x18\x02 \x01(\x08R\x07waiting\x12\x17\n\x07on_call\x18\x03 \x01(\x08R\x06onCall\x12\x17\n\x07wrap_up\x18\x04 \x01(\x08R\x06wrapUp\x12\x16\n\x06paused\x18\x05 \x01(\x08R\x06paused\x12\x1a\n\x08transfer\x18\x06 \x01(\x08R\x08transfer\x12\x18\n\x07preview\x18\x07 \x01(\x08R\x07preview\x12\x16\n\x06manual\x18\x08 \x01(\x08R\x06manual\x12\x10\n\x03pbx\x18\t \x01(\x08R\x03pbx\x12\x1a\n\x08intercom\x18\n \x01(\x08R\x08intercom\"\xd0\x03\n\x19\x44\x61shboardQueuePreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12*\n\x11\x64\x65\x66\x61ult_info_view\x18\n \x01(\x08R\x0f\x64\x65\x66\x61ultInfoView\x12\x32\n\x15\x64\x65\x66\x61ult_info_grouping\x18\x0b \x01(\x08R\x13\x64\x65\x66\x61ultInfoGrouping\x12,\n\x12\x64\x65\x66\x61ult_small_icon\x18\x0c \x01(\x08R\x10\x64\x65\x66\x61ultSmallIcon\x12\x36\n\x17\x64\x65\x66\x61ult_descending_sort\x18\r \x01(\x08R\x15\x64\x65\x66\x61ultDescendingSort\x12=\n\x1b\x64\x65\x66\x61ult_agent_skills_filter\x18\x0e \x01(\x03R\x18\x64\x65\x66\x61ultAgentSkillsFilter\x12=\n\x1b\x64\x65\x66\x61ult_info_table_template\x18\x0f \x01(\x03R\x18\x64\x65\x66\x61ultInfoTableTemplate\x12X\n\x1a\x64\x65\x66\x61ult_info_sort_by_value\x18\x10 \x01(\x0e\x32\x1c.api.commons.QueueInfoSortByR\x16\x64\x65\x66\x61ultInfoSortByValue\"\x88\x05\n\x10PhonePreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x32\n\x15\x61gent_preview_dialing\x18\n \x01(\x08R\x13\x61gentPreviewDialing\x12\x41\n\x1d\x64\x65\x66\x61ult_ring_length_threshold\x18\x0b \x01(\x05R\x1a\x64\x65\x66\x61ultRingLengthThreshold\x12\x41\n\x1d\x64isplay_ring_length_threshold\x18\x0c \x01(\x08R\x1a\x64isplayRingLengthThreshold\x12$\n\x0eshow_caller_id\x18\r \x01(\x08R\x0cshowCallerId\x12\x31\n\x15\x64\x65\x66\x61ult_use_caller_id\x18\x0e \x01(\x08R\x12\x64\x65\x66\x61ultUseCallerId\x12>\n\x1boverride_linkback_recording\x18\x0f \x01(\x08R\x19overrideLinkbackRecording\x12)\n\x11\x63\x61ller_id_cfd_sid\x18\x10 \x01(\x03R\x0e\x63\x61llerIdCfdSid\x12H\n\x12\x64\x65\x66\x61ult_dial_order\x18\x11 \x01(\x0b\x32\x1a.api.commons.org.DialOrderR\x10\x64\x65\x66\x61ultDialOrder\x12\x66\n\x1b\x61nswering_machine_detection\x18\x12 \x01(\x0e\x32&.api.commons.AnsweringMachineDetectionR\x19\x61nsweringMachineDetection\x12-\n\x12linkback_recording\x18\x13 \x01(\x08R\x11linkbackRecording\"\x89\x01\n\tDialOrder\x12\x38\n\x08standard\x18\x01 \x01(\x0e\x32\x1a.api.commons.DialOrderTypeH\x00R\x08standard\x12:\n\x06\x63ustom\x18\x02 \x01(\x0b\x32 .api.commons.org.CustomDialOrderH\x00R\x06\x63ustomB\x06\n\x04type\"^\n\x0f\x43ustomDialOrder\x12K\n\x11\x64ial_order_fields\x18\x01 \x03(\x0b\x32\x1f.api.commons.org.DialOrderFieldR\x0f\x64ialOrderFields\"H\n\x0e\x44ialOrderField\x12\x17\n\x07\x63\x66\x64_sid\x18\x01 \x01(\x03R\x06\x63\x66\x64Sid\x12\x1d\n\nfield_name\x18\x02 \x01(\tR\tfieldName\"\xd9\x06\n\x15\x43ompliancePreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x39\n\x19\x64isplay_after_hours_calls\x18\n \x01(\x08R\x16\x64isplayAfterHoursCalls\x12*\n\x11\x61\x66ter_hours_calls\x18\x0b \x01(\x08R\x0f\x61\x66terHoursCalls\x12<\n\x1a\x64isplay_natural_compliance\x18\x0c \x01(\x08R\x18\x64isplayNaturalCompliance\x12\x34\n\x16use_natural_compliance\x18\r \x01(\x08R\x14useNaturalCompliance\x12=\n\x1b\x64\x65\x66\x61ult_compliance_rule_set\x18\x0e \x01(\tR\x18\x64\x65\x66\x61ultComplianceRuleSet\x12\x37\n\x18\x64isplay_cell_phone_scrub\x18\x0f \x01(\x08R\x15\x64isplayCellPhoneScrub\x12(\n\x10\x63\x65ll_phone_scrub\x18\x10 \x01(\x08R\x0e\x63\x65llPhoneScrub\x12\x34\n\x16\x64isplay_schedule_rules\x18\x11 \x01(\x08R\x14\x64isplayScheduleRules\x12,\n\x12use_schedule_rules\x18\x12 \x01(\x08R\x10useScheduleRules\x12V\n\x15\x64\x65\x66\x61ult_schedule_rule\x18\x13 \x01(\x0b\x32\".api.commons.org.ScheduleRuleFieldR\x13\x64\x65\x66\x61ultScheduleRule\x12)\n\x11\x64o_zip_code_scrub\x18\x14 \x01(\x08R\x0e\x64oZipCodeScrub\x12\x43\n\x0ezip_code_scrub\x18\x15 \x01(\x0b\x32\x1d.api.commons.org.ZipCodeFieldR\x0czipCodeScrub\x12\x41\n\x1d\x64\x65\x66\x61ult_email_compliance_list\x18\x16 \x01(\tR\x1a\x64\x65\x66\x61ultEmailComplianceList\x12=\n\x1b\x64\x65\x66\x61ult_sms_compliance_list\x18\x17 \x01(\tR\x18\x64\x65\x66\x61ultSmsComplianceList\"@\n\x11ScheduleRuleField\x12\x17\n\x07rule_id\x18\x01 \x01(\x03R\x06ruleId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"F\n\x0cZipCodeField\x12\x17\n\x07\x63\x66\x64_sid\x18\x01 \x01(\x03R\x06\x63\x66\x64Sid\x12\x1d\n\nfield_name\x18\x02 \x01(\tR\tfieldName\"\xb6\x05\n\x14\x42roadcastPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12I\n!display_list_penetration_strategy\x18\n \x01(\x08R\x1e\x64isplayListPenetrationStrategy\x12\x43\n\x1e\x64ial_list_penetration_strategy\x18\x0b \x01(\x08R\x1b\x64ialListPenetrationStrategy\x12\x33\n\x16\x64isplay_follow_the_sun\x18\x0c \x01(\x08R\x13\x64isplayFollowTheSun\x12$\n\x0e\x66ollow_the_sun\x18\r \x01(\x08R\x0c\x66ollowTheSun\x12@\n\x1csequence_terminator_override\x18\x0e \x01(\x08R\x1asequenceTerminatorOverride\x12\x66\n\x1b\x62roadcast_template_ordering\x18\x0f \x01(\x0e\x32&.api.commons.BroadcastTemplateOrderingR\x19\x62roadcastTemplateOrdering\x12,\n\x12start_time_enabled\x18\x10 \x01(\x08R\x10startTimeEnabled\x12L\n\x12\x64\x65\x66\x61ult_start_time\x18\x11 \x01(\x0b\x32\x1e.api.commons.org.BroadcastTimeR\x10\x64\x65\x66\x61ultStartTime\x12*\n\x11stop_time_enabled\x18\x12 \x01(\x08R\x0fstopTimeEnabled\x12J\n\x11\x64\x65\x66\x61ult_stop_time\x18\x13 \x01(\x0b\x32\x1e.api.commons.org.BroadcastTimeR\x0f\x64\x65\x66\x61ultStopTime\"r\n\rBroadcastTime\x12\x14\n\x05hours\x18\x01 \x01(\x05R\x05hours\x12\x18\n\x07minutes\x18\x02 \x01(\x05R\x07minutes\x12\x31\n\x08timezone\x18\x03 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\"\xbe\x06\n\x13SchedulePreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12@\n\x1d\x64isplay_schedule_by_time_zone\x18\n \x01(\x08R\x19\x64isplayScheduleByTimeZone\x12\x38\n\x19use_schedule_by_time_zone\x18\x0b \x01(\x08R\x15useScheduleByTimeZone\x12\x62\n\x1bschedule_by_time_zone_scope\x18\x0c \x01(\x0e\x32$.api.commons.ScheduleByTimeZoneScopeR\x17scheduleByTimeZoneScope\x12;\n\x1a\x64isplay_schedule_as_paused\x18\r \x01(\x08R\x17\x64isplayScheduleAsPaused\x12,\n\x12schedule_as_paused\x18\x0e \x01(\x08R\x10scheduleAsPaused\x12@\n\x1c\x64\x65\x66\x61ult_completion_threshold\x18\x0f \x01(\x03R\x1a\x64\x65\x66\x61ultCompletionThreshold\x12\x38\n\x18\x64isplay_campaign_linking\x18\x10 \x01(\x08R\x16\x64isplayCampaignLinking\x12\x30\n\x14use_campaign_linking\x18\x11 \x01(\x08R\x12useCampaignLinking\x12^\n\x0e\x63\x61mpaign_links\x18\x12 \x03(\x0b\x32\x37.api.commons.org.SchedulePreferences.CampaignLinksEntryR\rcampaignLinks\x12\x37\n\x18\x64\x65\x66\x61ult_campaign_link_id\x18\x13 \x01(\tR\x15\x64\x65\x66\x61ultCampaignLinkId\x12<\n\x1aresend_cancelled_campaigns\x18\x14 \x01(\x08R\x18resendCancelledCampaigns\x1a@\n\x12\x43\x61mpaignLinksEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xbf\x01\n\x13\x45mailSmsPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12(\n\x10use_custom_links\x18\n \x01(\x08R\x0euseCustomLinks\x12\x35\n\x16\x63lient_acknowledgement\x18\x0b \x01(\x08R\x15\x63lientAcknowledgement\x12\x30\n\x14\x65mail_from_addresses\x18\x0c \x03(\tR\x12\x65mailFromAddresses\"\x8d\x02\n\x13\x42usinessPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\"\n\rweeks_of_data\x18\n \x01(\x05R\x0bweeksOfData\x12\x35\n\ttime_zone\x18\x0b \x01(\x0e\x32\x18.api.commons.AnaTimeZoneR\x08timeZone\x12.\n\x13multi_client_access\x18\x0c \x01(\x08R\x11multiClientAccess\x12\x33\n\x15\x63ustom_visualizations\x18\r \x01(\x08R\x14\x63ustomVisualizations\x12\x1f\n\x0btime_filter\x18\x0e \x01(\tR\ntimeFilter\"\xf7\x01\n\x15ScorecardsPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x34\n\x16\x63\x61ll_sample_percentage\x18\x02 \x01(\rR\x14\x63\x61llSamplePercentage\x12\x30\n\x14max_user_evaluations\x18\x03 \x01(\rR\x12maxUserEvaluations\x12_\n\x13\x65valuation_interval\x18\x04 \x01(\x0e\x32..api.commons.org.Scorecards.EvaluationIntervalR\x12\x65valuationInterval\"\x88\x01\n\nScorecards\"z\n\x12\x45valuationInterval\x12\'\n#EVALUATION_INTERVAL_DAY_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x45VALUATION_INTERVAL_WEEK\x10\x01\x12\x1d\n\x19\x45VALUATION_INTERVAL_MONTH\x10\x02\"\xca\x03\n\x19VoiceAnalyticsPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x18\n\x07\x65nabled\x18\x02 \x01(\x08R\x07\x65nabled\x12>\n\x06redact\x18\x03 \x03(\x0b\x32&.api.commons.org.VoiceAnalytics.RedactR\x06redact\x12>\n\x06notify\x18\x04 \x01(\x0b\x32&.api.commons.org.VoiceAnalytics.NotifyR\x06notify\x12M\n\x0e\x62illing_notify\x18\x05 \x01(\x0b\x32&.api.commons.org.VoiceAnalytics.NotifyR\rbillingNotify\x12#\n\rnumber_format\x18\x06 \x01(\tR\x0cnumberFormat\x12*\n\x11redact_all_digits\x18\n \x01(\x08R\x0fredactAllDigits\x12+\n\x11silence_threshold\x18\x64 \x01(\rR\x10silenceThreshold\x12/\n\x13talk_over_threshold\x18\xc8\x01 \x01(\rR\x11talkOverThreshold\"\xfc\x02\n\x0eVoiceAnalytics\x1aS\n\x06Redact\x12@\n\x06number\x18\x01 \x01(\x0b\x32&.api.commons.org.VoiceAnalytics.NumberH\x00R\x06numberB\x07\n\x05where\x1a\xf6\x01\n\x06Number\x12?\n\x04kind\x18\x01 \x01(\x0e\x32+.api.commons.org.VoiceAnalytics.Number.KindR\x04kind\x12\'\n\x0fmin_consecutive\x18\x02 \x01(\rR\x0eminConsecutive\x12\'\n\x0fmax_consecutive\x18\x03 \x01(\rR\x0emaxConsecutive\x12\x12\n\x04slop\x18\x04 \x01(\rR\x04slop\"E\n\x04Kind\x12\x1d\n\x19KIND_CARDINAL_UNSPECIFIED\x10\x00\x12\x10\n\x0cKIND_ORDINAL\x10\x01\x12\x0c\n\x08KIND_ANY\x10\x02\x1a\x1c\n\x06Notify\x12\x12\n\x04\x63ron\x18\x01 \x01(\tR\x04\x63ron\"\x95\x02\n\x13\x45ndOfDayPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\neod_monday\x18\n \x01(\x05R\teodMonday\x12\x1f\n\x0b\x65od_tuesday\x18\x0b \x01(\x05R\neodTuesday\x12#\n\reod_wednesday\x18\x0c \x01(\x05R\x0c\x65odWednesday\x12!\n\x0c\x65od_thursday\x18\r \x01(\x05R\x0b\x65odThursday\x12\x1d\n\neod_friday\x18\x0e \x01(\x05R\teodFriday\x12!\n\x0c\x65od_saturday\x18\x0f \x01(\x05R\x0b\x65odSaturday\x12\x1d\n\neod_sunday\x18\x10 \x01(\x05R\teodSunday\"\xea\x02\n\x11\x46ilterPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12Z\n\x1a\x64\x65\x66\x61ult_auto_report_filter\x18\n \x01(\x0b\x32\x1d.api.commons.org.ReportFilterR\x17\x64\x65\x66\x61ultAutoReportFilter\x12\x35\n\x17send_empty_auto_reports\x18\x0b \x01(\x08R\x14sendEmptyAutoReports\x12\x45\n\x1f\x64isplay_broadcast_resend_filter\x18\x0c \x01(\x08R\x1c\x64isplayBroadcastResendFilter\x12\x64\n\x1f\x64\x65\x66\x61ult_broadcast_resend_filter\x18\r \x01(\x0b\x32\x1d.api.commons.org.ReportFilterR\x1c\x64\x65\x66\x61ultBroadcastResendFilter\"s\n\x0cReportFilter\x12?\n\x08standard\x18\x01 \x01(\x0e\x32!.api.commons.StandardReportFilterH\x00R\x08standard\x12\x18\n\x06\x63ustom\x18\x02 \x01(\x03H\x00R\x06\x63ustomB\x08\n\x06\x63hoice\"\xac\x03\n\x14RecordingPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12-\n\x12\x63onvention_enabled\x18\n \x01(\x08R\x11\x63onventionEnabled\x12\x61\n\x14\x66ile_name_convention\x18\x0b \x01(\x0b\x32/.api.commons.org.RecordingsFileNamingConventionR\x12\x66ileNameConvention\x12\x34\n\x16zip_convention_enabled\x18\x0c \x01(\x08R\x14zipConventionEnabled\x12k\n\x18zip_file_name_convention\x18\r \x01(\x0b\x32\x32.api.commons.org.RecordingsZipFileNamingConventionR\x15zipFileNameConvention\x12H\n\x10\x65xport_file_type\x18\x0e \x01(\x0e\x32\x1e.api.commons.RecordingFileTypeR\x0e\x65xportFileType\"\xdb\x02\n\x1eRecordingsFileNamingConvention\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\x12?\n\x07inbound\x18\x02 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x07inbound\x12=\n\x06manual\x18\x03 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x06manual\x12\x41\n\x08outbound\x18\x04 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x08outbound\x12?\n\x07preview\x18\x05 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x07preview\"\xe0\x02\n!RecordingsZipFileNamingConvention\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\x12?\n\x07inbound\x18\x02 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x07inbound\x12=\n\x06manual\x18\x03 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x06manual\x12\x41\n\x08outbound\x18\x04 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x08outbound\x12\x41\n\x08\x63ombined\x18\x05 \x01(\x0b\x32%.api.commons.org.FileNamingConventionR\x08\x63ombined\"T\n\x14\x46ileNamingConvention\x12<\n\x08segments\x18\x01 \x03(\x0b\x32 .api.commons.org.FileNameSegmentR\x08segments\"}\n\x0f\x46ileNameSegment\x12!\n\x0csegment_type\x18\x01 \x01(\tR\x0bsegmentType\x12%\n\x0e\x66ormat_pattern\x18\x02 \x01(\tR\rformatPattern\x12 \n\x0ctime_zone_id\x18\x03 \x01(\tR\ntimeZoneId\"\xe2\x03\n\x16\x41\x64minClientPreferences\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x30\n\x14use_reserved_carrier\x18\n \x01(\x08R\x12useReservedCarrier\x12+\n\x11reserved_carriers\x18\x0b \x03(\tR\x10reservedCarriers\x12\x1b\n\temail_key\x18\x0c \x01(\tR\x08\x65mailKey\x12\x19\n\x08\x65mail_id\x18\r \x01(\tR\x07\x65mailId\x12\x1d\n\nemail_name\x18\x0e \x01(\tR\temailName\x12#\n\rwhitelist_ips\x18\x0f \x03(\tR\x0cwhitelistIps\x12+\n\x11whitelist_domains\x18\x10 \x03(\tR\x10whitelistDomains\x12\x30\n\x14\x63\x61llbacks_service_id\x18\x11 \x01(\tR\x12\x63\x61llbacksServiceId\x12\x34\n\x16\x61gent_screen_recording\x18\x12 \x01(\x08R\x14\x61gentScreenRecording\x12\x41\n\x11\x61llowed_countries\x18\x13 \x03(\x0e\x32\x14.api.commons.CountryR\x10\x61llowedCountries\"\xfd\x02\n\rBusinessHours\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12*\n\x11\x62usiness_hours_id\x18\x06 \x01(\tR\x0f\x62usinessHoursId\x12.\n\x13\x62usiness_hours_name\x18\x07 \x01(\tR\x11\x62usinessHoursName\x12\x31\n\x08timezone\x18\x08 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x41\n\rday_intervals\x18\t \x03(\x0b\x32\x1c.api.commons.org.DayIntervalR\x0c\x64\x61yIntervals\x12=\n\x0clast_updated\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdatedJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06R\x02idR\x04nameR\x06ranges\"\x87\x01\n\x05Range\x12\x1d\n\nstart_hour\x18\x01 \x01(\x05R\tstartHour\x12!\n\x0cstart_minute\x18\x02 \x01(\x05R\x0bstartMinute\x12\x19\n\x08\x65nd_hour\x18\x03 \x01(\x05R\x07\x65ndHour\x12\x1d\n\nend_minute\x18\x04 \x01(\x05R\tendMinute:\x02\x18\x01\"7\n\tTimeOfDay\x12\x12\n\x04hour\x18\x01 \x01(\x05R\x04hour\x12\x16\n\x06minute\x18\x02 \x01(\x05R\x06minute\"\x9a\x01\n\x0b\x44\x61yInterval\x12+\n\x03\x64\x61y\x18\x01 \x01(\x0e\x32\x19.api.commons.Weekday.EnumR\x03\x64\x61y\x12\x30\n\x05start\x18\x02 \x01(\x0b\x32\x1a.api.commons.org.TimeOfDayR\x05start\x12,\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.api.commons.org.TimeOfDayR\x03\x65nd\"w\n\x0cMonthDayDate\x12\x1b\n\tdate_name\x18\x01 \x01(\tR\x08\x64\x61teName\x12(\n\x05month\x18\x02 \x01(\x0e\x32\x12.api.commons.MonthR\x05month\x12 \n\x0c\x64\x61y_of_month\x18\x03 \x01(\x05R\ndayOfMonth\"\xb8\x01\n\x0e\x43ountryHoliday\x12!\n\x0choliday_name\x18\x01 \x01(\tR\x0bholidayName\x12\x32\n\x07\x63ountry\x18\x02 \x01(\x0e\x32\x14.api.commons.CountryB\x02\x18\x01R\x07\x63ountry\x12!\n\x0c\x63ountry_name\x18\x03 \x01(\tR\x0b\x63ountryName\x12\x14\n\x05types\x18\x04 \x03(\tR\x05types\x12\x16\n\x06states\x18\x05 \x03(\tR\x06states\"\x8a\x01\n\rProgrammedDay\x12\x31\n\x03\x64\x61y\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.MonthDayDateH\x00R\x03\x64\x61y\x12;\n\x07holiday\x18\x02 \x01(\x0b\x32\x1f.api.commons.org.CountryHolidayH\x00R\x07holidayB\t\n\x07\x44\x61yType\"\xd4\x02\n\x0fProgrammedDates\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12.\n\x13programmed_dates_id\x18\x02 \x01(\tR\x11programmedDatesId\x12\x32\n\x15programmed_dates_name\x18\x03 \x01(\tR\x13programmedDatesName\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x31\n\x08timezone\x18\x05 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x32\n\x04\x64\x61ys\x18\x06 \x03(\x0b\x32\x1e.api.commons.org.ProgrammedDayR\x04\x64\x61ys\x12=\n\x0clast_updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\"\xdb\x02\n\x10ObservedHolidays\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x30\n\x14observed_holidays_id\x18\x02 \x01(\tR\x12observedHolidaysId\x12\x34\n\x16observed_holidays_name\x18\x03 \x01(\tR\x14observedHolidaysName\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x31\n\x08timezone\x18\x05 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timezone\x12\x34\n\x04\x64\x61ys\x18\x06 \x03(\x0b\x32 .api.commons.org.ObservedHolidayR\x04\x64\x61ys\x12=\n\x0clast_updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\"\x8c\x01\n\x0fObservedHoliday\x12\x31\n\x03\x64\x61y\x18\x01 \x01(\x0b\x32\x1d.api.commons.org.MonthDayDateH\x00R\x03\x64\x61y\x12;\n\x07holiday\x18\x02 \x01(\x0b\x32\x1f.api.commons.org.CountryHolidayH\x00R\x07holidayB\t\n\x07\x44\x61yType\"\xff\x02\n\x0f\x43\x65rtificateInfo\x12.\n\x13\x63\x65rtificate_info_id\x18\x01 \x01(\tR\x11\x63\x65rtificateInfoId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04hash\x18\x05 \x01(\tR\x04hash\x12\x43\n\x0f\x65xpiration_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x65xpirationDate\x12?\n\rcreation_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x63reationDate\x12\x1d\n\nrequest_by\x18\x08 \x01(\tR\trequestBy\x12\x18\n\x07\x64\x65leted\x18\t \x01(\x08R\x07\x64\x65leted\x12\x18\n\x07revoked\x18\n \x01(\x08R\x07revoked:\x02\x18\x01\x42\x85\x01\n\x13\x63om.api.commons.orgB\x10PreferencesProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.preferences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\020PreferencesProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_SCHEDULEPREFERENCES_CAMPAIGNLINKSENTRY']._loaded_options = None
  _globals['_SCHEDULEPREFERENCES_CAMPAIGNLINKSENTRY']._serialized_options = b'8\001'
  _globals['_RANGE']._loaded_options = None
  _globals['_RANGE']._serialized_options = b'\030\001'
  _globals['_COUNTRYHOLIDAY'].fields_by_name['country']._loaded_options = None
  _globals['_COUNTRYHOLIDAY'].fields_by_name['country']._serialized_options = b'\030\001'
  _globals['_CERTIFICATEINFO']._loaded_options = None
  _globals['_CERTIFICATEINFO']._serialized_options = b'\030\001'
  _globals['_ORGANIZATIONPREFERENCES']._serialized_start=244
  _globals['_ORGANIZATIONPREFERENCES']._serialized_end=559
  _globals['_AGENTPREFERENCES']._serialized_start=562
  _globals['_AGENTPREFERENCES']._serialized_end=1077
  _globals['_CONTACTPREFERENCES']._serialized_start=1080
  _globals['_CONTACTPREFERENCES']._serialized_end=1757
  _globals['_IMPORTFORMAT']._serialized_start=1760
  _globals['_IMPORTFORMAT']._serialized_end=1912
  _globals['_CUSTOMIMPORTFORMAT']._serialized_start=1914
  _globals['_CUSTOMIMPORTFORMAT']._serialized_end=1970
  _globals['_CONTACTAREACODE']._serialized_start=1972
  _globals['_CONTACTAREACODE']._serialized_end=2090
  _globals['_CONTACTFIELDDESCRIPTION']._serialized_start=2093
  _globals['_CONTACTFIELDDESCRIPTION']._serialized_end=2244
  _globals['_AUTHENTICATIONPREFERENCES']._serialized_start=2247
  _globals['_AUTHENTICATIONPREFERENCES']._serialized_end=3148
  _globals['_AUTHENTICATIONPREFERENCES_DUOMFASETTINGS']._serialized_start=2990
  _globals['_AUTHENTICATIONPREFERENCES_DUOMFASETTINGS']._serialized_end=3102
  _globals['_AUTHENTICATIONPREFERENCES_EMAILMFASETTINGS']._serialized_start=3104
  _globals['_AUTHENTICATIONPREFERENCES_EMAILMFASETTINGS']._serialized_end=3148
  _globals['_WEBHOOKPREFERENCES']._serialized_start=3151
  _globals['_WEBHOOKPREFERENCES']._serialized_end=3342
  _globals['_DASHBOARDPREFERENCES']._serialized_start=3345
  _globals['_DASHBOARDPREFERENCES']._serialized_end=3958
  _globals['_INCLUDEDCALLTYPES']._serialized_start=3961
  _globals['_INCLUDEDCALLTYPES']._serialized_end=4102
  _globals['_BARGEINFILTERING']._serialized_start=4105
  _globals['_BARGEINFILTERING']._serialized_end=4608
  _globals['_BARGEINFILTERING_HUNTGROUP']._serialized_start=4283
  _globals['_BARGEINFILTERING_HUNTGROUP']._serialized_end=4350
  _globals['_BARGEINFILTERING_AGENTSTATUS']._serialized_start=4353
  _globals['_BARGEINFILTERING_AGENTSTATUS']._serialized_end=4608
  _globals['_DASHBOARDQUEUEPREFERENCES']._serialized_start=4611
  _globals['_DASHBOARDQUEUEPREFERENCES']._serialized_end=5075
  _globals['_PHONEPREFERENCES']._serialized_start=5078
  _globals['_PHONEPREFERENCES']._serialized_end=5726
  _globals['_DIALORDER']._serialized_start=5729
  _globals['_DIALORDER']._serialized_end=5866
  _globals['_CUSTOMDIALORDER']._serialized_start=5868
  _globals['_CUSTOMDIALORDER']._serialized_end=5962
  _globals['_DIALORDERFIELD']._serialized_start=5964
  _globals['_DIALORDERFIELD']._serialized_end=6036
  _globals['_COMPLIANCEPREFERENCES']._serialized_start=6039
  _globals['_COMPLIANCEPREFERENCES']._serialized_end=6896
  _globals['_SCHEDULERULEFIELD']._serialized_start=6898
  _globals['_SCHEDULERULEFIELD']._serialized_end=6962
  _globals['_ZIPCODEFIELD']._serialized_start=6964
  _globals['_ZIPCODEFIELD']._serialized_end=7034
  _globals['_BROADCASTPREFERENCES']._serialized_start=7037
  _globals['_BROADCASTPREFERENCES']._serialized_end=7731
  _globals['_BROADCASTTIME']._serialized_start=7733
  _globals['_BROADCASTTIME']._serialized_end=7847
  _globals['_SCHEDULEPREFERENCES']._serialized_start=7850
  _globals['_SCHEDULEPREFERENCES']._serialized_end=8680
  _globals['_SCHEDULEPREFERENCES_CAMPAIGNLINKSENTRY']._serialized_start=8616
  _globals['_SCHEDULEPREFERENCES_CAMPAIGNLINKSENTRY']._serialized_end=8680
  _globals['_EMAILSMSPREFERENCES']._serialized_start=8683
  _globals['_EMAILSMSPREFERENCES']._serialized_end=8874
  _globals['_BUSINESSPREFERENCES']._serialized_start=8877
  _globals['_BUSINESSPREFERENCES']._serialized_end=9146
  _globals['_SCORECARDSPREFERENCES']._serialized_start=9149
  _globals['_SCORECARDSPREFERENCES']._serialized_end=9396
  _globals['_SCORECARDS']._serialized_start=9399
  _globals['_SCORECARDS']._serialized_end=9535
  _globals['_SCORECARDS_EVALUATIONINTERVAL']._serialized_start=9413
  _globals['_SCORECARDS_EVALUATIONINTERVAL']._serialized_end=9535
  _globals['_VOICEANALYTICSPREFERENCES']._serialized_start=9538
  _globals['_VOICEANALYTICSPREFERENCES']._serialized_end=9996
  _globals['_VOICEANALYTICS']._serialized_start=9999
  _globals['_VOICEANALYTICS']._serialized_end=10379
  _globals['_VOICEANALYTICS_REDACT']._serialized_start=10017
  _globals['_VOICEANALYTICS_REDACT']._serialized_end=10100
  _globals['_VOICEANALYTICS_NUMBER']._serialized_start=10103
  _globals['_VOICEANALYTICS_NUMBER']._serialized_end=10349
  _globals['_VOICEANALYTICS_NUMBER_KIND']._serialized_start=10280
  _globals['_VOICEANALYTICS_NUMBER_KIND']._serialized_end=10349
  _globals['_VOICEANALYTICS_NOTIFY']._serialized_start=10351
  _globals['_VOICEANALYTICS_NOTIFY']._serialized_end=10379
  _globals['_ENDOFDAYPREFERENCES']._serialized_start=10382
  _globals['_ENDOFDAYPREFERENCES']._serialized_end=10659
  _globals['_FILTERPREFERENCES']._serialized_start=10662
  _globals['_FILTERPREFERENCES']._serialized_end=11024
  _globals['_REPORTFILTER']._serialized_start=11026
  _globals['_REPORTFILTER']._serialized_end=11141
  _globals['_RECORDINGPREFERENCES']._serialized_start=11144
  _globals['_RECORDINGPREFERENCES']._serialized_end=11572
  _globals['_RECORDINGSFILENAMINGCONVENTION']._serialized_start=11575
  _globals['_RECORDINGSFILENAMINGCONVENTION']._serialized_end=11922
  _globals['_RECORDINGSZIPFILENAMINGCONVENTION']._serialized_start=11925
  _globals['_RECORDINGSZIPFILENAMINGCONVENTION']._serialized_end=12277
  _globals['_FILENAMINGCONVENTION']._serialized_start=12279
  _globals['_FILENAMINGCONVENTION']._serialized_end=12363
  _globals['_FILENAMESEGMENT']._serialized_start=12365
  _globals['_FILENAMESEGMENT']._serialized_end=12490
  _globals['_ADMINCLIENTPREFERENCES']._serialized_start=12493
  _globals['_ADMINCLIENTPREFERENCES']._serialized_end=12975
  _globals['_BUSINESSHOURS']._serialized_start=12978
  _globals['_BUSINESSHOURS']._serialized_end=13359
  _globals['_RANGE']._serialized_start=13362
  _globals['_RANGE']._serialized_end=13497
  _globals['_TIMEOFDAY']._serialized_start=13499
  _globals['_TIMEOFDAY']._serialized_end=13554
  _globals['_DAYINTERVAL']._serialized_start=13557
  _globals['_DAYINTERVAL']._serialized_end=13711
  _globals['_MONTHDAYDATE']._serialized_start=13713
  _globals['_MONTHDAYDATE']._serialized_end=13832
  _globals['_COUNTRYHOLIDAY']._serialized_start=13835
  _globals['_COUNTRYHOLIDAY']._serialized_end=14019
  _globals['_PROGRAMMEDDAY']._serialized_start=14022
  _globals['_PROGRAMMEDDAY']._serialized_end=14160
  _globals['_PROGRAMMEDDATES']._serialized_start=14163
  _globals['_PROGRAMMEDDATES']._serialized_end=14503
  _globals['_OBSERVEDHOLIDAYS']._serialized_start=14506
  _globals['_OBSERVEDHOLIDAYS']._serialized_end=14853
  _globals['_OBSERVEDHOLIDAY']._serialized_start=14856
  _globals['_OBSERVEDHOLIDAY']._serialized_end=14996
  _globals['_CERTIFICATEINFO']._serialized_start=14999
  _globals['_CERTIFICATEINFO']._serialized_end=15382
# @@protoc_insertion_point(module_scope)
