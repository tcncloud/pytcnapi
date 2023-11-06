# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/org/huntgroup.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import country_pb2 as api_dot_commons_dot_country__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/commons/org/huntgroup.proto\x12\x0f\x61pi.commons.org\x1a\x19\x61pi/commons/country.proto\x1a\x15\x61pi/commons/org.proto\"\xfd\x04\n\x11HuntGroupSettings\x12K\n\x10general_settings\x18\x01 \x01(\x0b\x32 .api.commons.org.GeneralSettingsR\x0fgeneralSettings\x12]\n\x16\x63ommunication_settings\x18\x02 \x01(\x0b\x32&.api.commons.org.CommunicationSettingsR\x15\x63ommunicationSettings\x12N\n\x11\x63\x61llback_settings\x18\x03 \x01(\x0b\x32!.api.commons.org.CallbackSettingsR\x10\x63\x61llbackSettings\x12X\n\x15preview_dial_settings\x18\x04 \x01(\x0b\x32$.api.commons.org.PreviewDialSettingsR\x13previewDialSettings\x12U\n\x14manual_dial_settings\x18\x05 \x01(\x0b\x32#.api.commons.org.ManualDialSettingsR\x12manualDialSettings\x12[\n\x16transfer_call_settings\x18\x06 \x01(\x0b\x32%.api.commons.org.TransferCallSettingsR\x14transferCallSettings\x12^\n\x17number_history_settings\x18\x07 \x01(\x0b\x32&.api.commons.org.NumberHistorySettingsR\x15numberHistorySettings\"\xee&\n\x0fGeneralSettings\x12\x42\n\x1e\x65nable_agent_gateway_title_bar\x18\x01 \x01(\x08R\x1a\x65nableAgentGatewayTitleBar\x12\x31\n\x15\x64\x65\x66\x61ult_agent_dial_in\x18\x02 \x01(\tR\x12\x64\x65\x66\x61ultAgentDialIn\x12\x41\n\x1drequire_end_call_confirmation\x18\x03 \x01(\x08R\x1arequireEndCallConfirmation\x12;\n\x1a\x65nable_authorization_by_ip\x18\x04 \x01(\x08R\x17\x65nableAuthorizationByIp\x12\x36\n\x17\x61uthorized_ip_addresses\x18\x05 \x03(\tR\x15\x61uthorizedIpAddresses\x12Q\n\x14initial_agent_status\x18\x64 \x01(\x0e\x32\x1f.api.commons.InitialAgentStatusR\x12initialAgentStatus\x12,\n\x12\x65nable_agent_pause\x18\x65 \x01(\x08R\x10\x65nableAgentPause\x12\x64\n\x16\x61gent_pause_option_set\x18\x66 \x01(\x0b\x32/.api.commons.org.GeneralSettings.PauseOptionSetR\x13\x61gentPauseOptionSet\x12;\n\x1a\x64\x65\x66\x61ult_agent_pause_option\x18g \x01(\tR\x17\x64\x65\x66\x61ultAgentPauseOption\x12\x39\n\x19\x65nable_pause_option_reset\x18h \x01(\x08R\x16\x65nablePauseOptionReset\x12?\n\x1b\x64isplay_recording_indicator\x18\xc8\x01 \x01(\x08R\x19\x64isplayRecordingIndicator\x12>\n\x1b\x65nable_call_recording_pause\x18\xc9\x01 \x01(\x08R\x18\x65nableCallRecordingPause\x12J\n!call_recording_pause_confirmation\x18\xca\x01 \x01(\x08R\x1e\x63\x61llRecordingPauseConfirmation\x12\x31\n\x14\x63\x61ll_recording_delay\x18\xcb\x01 \x01(\x03R\x12\x63\x61llRecordingDelay\x12\x43\n\x1e\x65nable_pause_recording_on_hold\x18\xcc\x01 \x01(\x08R\x1a\x65nablePauseRecordingOnHold\x12H\n enable_envision_screen_recording\x18\xac\x02 \x01(\x08R\x1d\x65nableEnvisionScreenRecording\x12\x38\n\x18\x65nable_agent_simple_hold\x18\x90\x03 \x01(\x08R\x15\x65nableAgentSimpleHold\x12:\n\x19\x65nable_agent_multi_accept\x18\x91\x03 \x01(\x08R\x16\x65nableAgentMultiAccept\x12\x43\n\x1epause_agent_after_multi_accept\x18\x92\x03 \x01(\x08R\x1apauseAgentAfterMultiAccept\x12i\n\x15hold_queue_monitoring\x18\x93\x03 \x01(\x0b\x32\x34.api.commons.org.GeneralSettings.HoldQueueMonitoringR\x13holdQueueMonitoring\x12\x37\n\x17\x64isplay_machine_deliver\x18\xf4\x03 \x01(\x08R\x15\x64isplayMachineDeliver\x12>\n\x1b\x64isplay_linkback_hunt_group\x18\xf5\x03 \x01(\x08R\x18\x64isplayLinkbackHuntGroup\x12\x36\n\x17\x64isplay_sip_header_data\x18\xf6\x03 \x01(\x08R\x14\x64isplaySipHeaderData\x12>\n\x1b\x64isplay_ivr_navigation_keys\x18\xf7\x03 \x01(\x08R\x18\x64isplayIvrNavigationKeys\x12:\n\x19\x64isplay_data_collect_data\x18\xf8\x03 \x01(\x08R\x16\x64isplayDataCollectData\x12m\n\x18\x64isplay_data_dipped_data\x18\xf9\x03 \x01(\x0b\x32\x33.api.commons.org.GeneralSettings.DataDipDataDisplayR\x15\x64isplayDataDippedData\x12r\n\x18integration_data_display\x18\xfa\x03 \x01(\x0b\x32\x37.api.commons.org.GeneralSettings.IntegrationDataDisplayR\x16integrationDataDisplay\x12\x66\n\x14journey_data_display\x18\xfb\x03 \x01(\x0b\x32\x33.api.commons.org.GeneralSettings.JourneyDataDisplayR\x12journeyDataDisplay\x12\\\n\x18\x61gent_call_history_scope\x18\xfc\x03 \x01(\x0e\x32\".api.commons.AgentCallHistoryScopeR\x15\x61gentCallHistoryScope\x12\x8c\x01\n\"agent_login_gui_statistics_display\x18\xfd\x03 \x01(\x0b\x32?.api.commons.org.GeneralSettings.AgentLoginGuiStatisticsDisplayR\x1e\x61gentLoginGuiStatisticsDisplay\x12v\n\x1aphone_zip_metadata_display\x18\xfe\x03 \x01(\x0b\x32\x38.api.commons.org.GeneralSettings.PhoneZipMetadataDisplayR\x17phoneZipMetadataDisplay\x12&\n\x0e\x64isplay_skills\x18\xff\x03 \x01(\x08R\rdisplaySkills\x12+\n\x11\x64isplay_web_links\x18\x80\x04 \x01(\x08R\x0f\x64isplayWebLinks\x12O\n$enable_agent_hunt_group_reassignment\x18\xd8\x04 \x01(\x08R enableAgentHuntGroupReassignment\x12l\n\x16\x64isallowed_hunt_groups\x18\xd9\x04 \x01(\x0b\x32\x35.api.commons.org.GeneralSettings.DisallowedHuntGroupsR\x14\x64isallowedHuntGroups\x12\x45\n\x1f\x65nable_manual_approval_of_calls\x18\xbc\x05 \x01(\x08R\x1b\x65nableManualApprovalOfCalls\x12\x44\n\x1erequire_manual_approval_number\x18\xbd\x05 \x01(\x08R\x1brequireManualApprovalNumber\x12\x41\n\x1d\x65nable_manual_approval_of_sms\x18\xbe\x05 \x01(\x08R\x19\x65nableManualApprovalOfSms\x12K\n\"require_manual_approval_number_sms\x18\xbf\x05 \x01(\x08R\x1erequireManualApprovalNumberSms\x12M\n#disable_reject_option_for_approvers\x18\xc0\x05 \x01(\x08R\x1f\x64isableRejectOptionForApprovers\x12\x65\n\x13\x61lphanumeric_keypad\x18\xa0\x06 \x01(\x0b\x32\x33.api.commons.org.GeneralSettings.AlphanumericKeypadR\x12\x61lphanumericKeypad\x12J\n!enable_call_desktop_notifications\x18\xa1\x06 \x01(\x08R\x1e\x65nableCallDesktopNotifications\x12{\n\x1binbound_compliance_metadata\x18\xa2\x06 \x01(\x0b\x32:.api.commons.org.GeneralSettings.InboundComplianceMetadataR\x19inboundComplianceMetadata\x12\x33\n\x15\x65nable_agent_intercom\x18\xa3\x06 \x01(\x08R\x13\x65nableAgentIntercom\x12y\n\x1bprepare_state_call_delivery\x18\xa4\x06 \x01(\x0b\x32\x39.api.commons.org.GeneralSettings.PrepareStateCallDeliveryR\x18prepareStateCallDelivery\x1a\x43\n\x0ePauseOptionSet\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x17\n\x07set_sid\x18\x02 \x01(\x03R\x06setSid\x1a\xef\x01\n\x13HoldQueueMonitoring\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12>\n\ragent_routing\x18\x02 \x01(\x0e\x32\x19.api.commons.AgentRoutingR\x0c\x61gentRouting\x12=\n\x1brequired_hunt_group_routing\x18\x03 \x01(\x03R\x18requiredHuntGroupRouting\x12?\n\x1cpreferred_hunt_group_routing\x18\x04 \x01(\x03R\x19preferredHuntGroupRouting\x1az\n\x12\x44\x61taDipDataDisplay\x12\x31\n\x15\x64isplay_data_dip_data\x18\x01 \x01(\x08R\x12\x64isplayDataDipData\x12\x31\n\x15\x64\x61ta_dip_display_keys\x18\x02 \x03(\tR\x12\x64\x61taDipDisplayKeys\x1a\x8c\x01\n\x16IntegrationDataDisplay\x12\x38\n\x18\x64isplay_integration_data\x18\x01 \x01(\x08R\x16\x64isplayIntegrationData\x12\x38\n\x18integration_display_keys\x18\x02 \x03(\tR\x16integrationDisplayKeys\x1ax\n\x12JourneyDataDisplay\x12\x30\n\x14\x64isplay_journey_data\x18\x01 \x01(\x08R\x12\x64isplayJourneyData\x12\x30\n\x14journey_display_keys\x18\x02 \x03(\tR\x12journeyDisplayKeys\x1a\xba\x01\n\x1e\x41gentLoginGuiStatisticsDisplay\x12J\n\"display_agent_login_gui_statistics\x18\x01 \x01(\x08R\x1e\x64isplayAgentLoginGuiStatistics\x12L\n#agent_login_gui_statistics_template\x18\x02 \x01(\x03R\x1f\x61gentLoginGuiStatisticsTemplate\x1a\xb5\x01\n\x17PhoneZipMetadataDisplay\x12;\n\x1a\x64isplay_phone_zip_metadata\x18\x01 \x01(\x08R\x17\x64isplayPhoneZipMetadata\x12]\n\x17phone_zip_metadata_keys\x18\x02 \x03(\x0e\x32&.api.commons.PhonePostalDisplayOptionsR\x14phoneZipMetadataKeys\x1aQ\n\x14\x44isallowedHuntGroups\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x1f\n\x0bhunt_groups\x18\x02 \x03(\x03R\nhuntGroups\x1av\n\x12\x41lphanumericKeypad\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x46\n\tdelimiter\x18\x02 \x01(\x0e\x32(.api.commons.AlphanumericKeypadDelimiterR\tdelimiter\x1a\x7f\n\x19InboundComplianceMetadata\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12#\n\roptional_data\x18\x02 \x03(\x03R\x0coptionalData\x12#\n\rrequired_data\x18\x03 \x03(\x03R\x0crequiredData\x1a^\n\x18PrepareStateCallDelivery\x12\x1f\n\x0bmanual_dial\x18\x01 \x01(\x08R\nmanualDial\x12!\n\x0cpreview_dial\x18\x02 \x01(\x08R\x0bpreviewDial\"\xec\x0e\n\x15\x43ommunicationSettings\x12\x37\n\x18\x65nable_scrub_list_adding\x18\x01 \x01(\x08R\x15\x65nableScrubListAdding\x12\x1f\n\x0bscrub_lists\x18\x02 \x03(\tR\nscrubLists\x12\x39\n\x19\x65nable_scrub_list_removal\x18\x03 \x01(\x08R\x16\x65nableScrubListRemoval\x12=\n\x1bscrub_lists_removal_allowed\x18\x04 \x03(\tR\x18scrubListsRemovalAllowed\x12R\n\x1a\x63ompliance_default_country\x18\x05 \x01(\x0e\x32\x14.api.commons.CountryR\x18\x63omplianceDefaultCountry\x12\x39\n\x19\x64isplay_options_in_wrapup\x18\x06 \x01(\x08R\x16\x64isplayOptionsInWrapup\x12}\n\x1dinbound_scrub_list_expiration\x18\x64 \x01(\x0b\x32:.api.commons.org.CommunicationSettings.ScrubListExpirationR\x1ainboundScrubListExpiration\x12{\n\x1cmanual_scrub_list_expiration\x18\x65 \x01(\x0b\x32:.api.commons.org.CommunicationSettings.ScrubListExpirationR\x19manualScrubListExpiration\x12\x7f\n\x1eoutbound_scrub_list_expiration\x18\x66 \x01(\x0b\x32:.api.commons.org.CommunicationSettings.ScrubListExpirationR\x1boutboundScrubListExpiration\x12}\n\x1dpreview_scrub_list_expiration\x18g \x01(\x0b\x32:.api.commons.org.CommunicationSettings.ScrubListExpirationR\x1apreviewScrubListExpiration\x12M\n#automate_manually_dialed_scrub_list\x18\xc8\x01 \x01(\x08R\x1f\x61utomateManuallyDialedScrubList\x12K\n\"automate_preview_dialed_scrub_list\x18\xc9\x01 \x01(\x08R\x1e\x61utomatePreviewDialedScrubList\x12u\n\x17\x61utomate_response_rules\x18\xca\x01 \x01(\x0b\x32<.api.commons.org.CommunicationSettings.AutomateResponseRulesR\x15\x61utomateResponseRules\x12\x83\x01\n\x1d\x61utomate_scrub_list_call_data\x18\xcb\x01 \x01(\x0b\x32@.api.commons.org.CommunicationSettings.AutomateScrubListCallDataR\x19\x61utomateScrubListCallData\x1a\xec\x01\n\x13ScrubListExpiration\x12S\n\x12\x64\x65\x66\x61ult_expiration\x18\x01 \x01(\x0e\x32$.api.commons.CommunicationExpirationR\x11\x64\x65\x66\x61ultExpiration\x12)\n\x10limit_expiration\x18\x02 \x01(\x08R\x0flimitExpiration\x12U\n\x13limited_expirations\x18\x03 \x03(\x0e\x32$.api.commons.CommunicationExpirationR\x12limitedExpirations\x1aL\n\x15\x41utomateResponseRules\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x19\n\x08rule_sid\x18\x02 \x01(\x03R\x07ruleSid\x1a\x9d\x02\n\x19\x41utomateScrubListCallData\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x88\x01\n\x16scrub_list_data_fields\x18\x02 \x03(\x0b\x32S.api.commons.org.CommunicationSettings.AutomateScrubListCallData.ScrubListDataFieldR\x13scrubListDataFields\x1a[\n\x12ScrubListDataField\x12\x1d\n\nscrub_list\x18\x01 \x01(\tR\tscrubList\x12&\n\x0f\x63\x61ll_data_field\x18\x02 \x01(\x03R\rcallDataField\"\xe2\x07\n\x10\x43\x61llbackSettings\x12<\n\x1a\x65nable_callback_scheduling\x18\x01 \x01(\x08R\x18\x65nableCallbackScheduling\x12j\n\x18\x64\x65\x66\x61ult_callback_routing\x18\x02 \x01(\x0b\x32\x30.api.commons.org.CallbackSettings.DefaultRoutingR\x16\x64\x65\x66\x61ultCallbackRouting\x12\x36\n\x17\x65nable_callback_calling\x18\x03 \x01(\x08R\x15\x65nableCallbackCalling\x12<\n\x1a\x65nable_automatic_retrieval\x18\x04 \x01(\x08R\x18\x65nableAutomaticRetrieval\x12{\n\x1b\x63\x61llback_routing_disallowed\x18\x05 \x01(\x0b\x32;.api.commons.org.CallbackSettings.CallbackRoutingDisallowedR\x19\x63\x61llbackRoutingDisallowed\x12\x41\n\x1d\x65nable_customizable_caller_id\x18\x06 \x01(\x08R\x1a\x65nableCustomizableCallerId\x12*\n\x11\x64\x65\x66\x61ult_caller_id\x18\x07 \x01(\tR\x0f\x64\x65\x66\x61ultCallerId\x12\x38\n\x18\x65nable_callback_calendar\x18\x08 \x01(\x08R\x16\x65nableCallbackCalendar\x1a\xc6\x01\n\x0e\x44\x65\x66\x61ultRouting\x12\x46\n\x0crouting_mode\x18\x01 \x01(\x0e\x32#.api.commons.DefaultCallbackRoutingR\x0broutingMode\x12\x1b\n\tagent_sid\x18\x02 \x01(\x03R\x08\x61gentSid\x12\'\n\x0f\x61gent_skillsets\x18\x03 \x03(\x03R\x0e\x61gentSkillsets\x12&\n\x0fhunt_group_sids\x18\x04 \x03(\x03R\rhuntGroupSids\x1a\xbe\x01\n\x19\x43\x61llbackRoutingDisallowed\x12\x30\n\x14use_routing_limiting\x18\x01 \x01(\x08R\x12useRoutingLimiting\x12\x1d\n\nagent_sids\x18\x02 \x03(\x03R\tagentSids\x12&\n\x0fhunt_group_sids\x18\x03 \x03(\x03R\rhuntGroupSids\x12(\n\x10\x61gent_skill_sids\x18\x04 \x03(\x03R\x0e\x61gentSkillSids\"\xab\x02\n\x13PreviewDialSettings\x12;\n\x1a\x65nable_preview_dial_cancel\x18\x01 \x01(\x08R\x17\x65nablePreviewDialCancel\x12<\n\x1b\x65nable_auto_pause_on_cancel\x18\x02 \x01(\x08R\x17\x65nableAutoPauseOnCancel\x12\'\n\x0ftimeout_minutes\x18\x03 \x01(\x03R\x0etimeoutMinutes\x12>\n\x1brequire_number_confirmation\x18\x04 \x01(\x08R\x19requireNumberConfirmation\x12\x30\n\x14preview_queue_config\x18\x05 \x01(\tR\x12previewQueueConfig\"\xe0\x16\n\x12ManualDialSettings\x12,\n\x12\x65nable_manual_dial\x18\x01 \x01(\x08R\x10\x65nableManualDial\x12\x38\n\x18queue_configuration_name\x18\x02 \x01(\tR\x16queueConfigurationName\x12\\\n\x16\x64\x65\x66\x61ult_call_recording\x18\x03 \x01(\x0e\x32&.api.commons.HuntGroupOrgDefaultCustomR\x14\x64\x65\x66\x61ultCallRecording\x12P\n\x10\x63\x65ll_phone_scrub\x18\x04 \x01(\x0e\x32&.api.commons.HuntGroupOrgDefaultCustomR\x0e\x63\x65llPhoneScrub\x12Z\n\x15time_zone_restriction\x18\x05 \x01(\x0e\x32&.api.commons.HuntGroupOrgDefaultCustomR\x13timeZoneRestriction\x12q\n time_zone_validation_postal_code\x18\x06 \x01(\x0e\x32).api.commons.ManualDialTimeZoneValidationR\x1ctimeZoneValidationPostalCode\x12i\n\x18natural_compliance_scrub\x18\x07 \x01(\x0b\x32/.api.commons.org.NaturalLanguageComplianceScrubR\x16naturalComplianceScrub\x12X\n\x0escrub_override\x18\x08 \x01(\x0b\x32\x31.api.commons.org.ManualDialSettings.ScrubOverrideR\rscrubOverride\x12)\n\x10\x65nable_whitelist\x18\t \x01(\x08R\x0f\x65nableWhitelist\x12N\n\x18\x64\x65\x66\x61ult_outbound_country\x18\n \x01(\x0e\x32\x14.api.commons.CountryR\x16\x64\x65\x66\x61ultOutboundCountry\x12K\n\"display_outbound_country_selection\x18\x0b \x01(\x08R\x1f\x64isplayOutboundCountrySelection\x12J\n\"display_outbound_number_phone_book\x18\x0c \x01(\x08R\x1e\x64isplayOutboundNumberPhoneBook\x12O\n\x19\x64\x65\x66\x61ult_caller_id_country\x18\r \x01(\x0e\x32\x14.api.commons.CountryR\x16\x64\x65\x66\x61ultCallerIdCountry\x12L\n#display_caller_id_country_selection\x18\x0e \x01(\x08R\x1f\x64isplayCallerIdCountrySelection\x12>\n\x1c\x64isplay_caller_id_phone_book\x18\x0f \x01(\x08R\x18\x64isplayCallerIdPhoneBook\x12\x41\n\x1d\x65nable_customizable_caller_id\x18\x10 \x01(\x08R\x1a\x65nableCustomizableCallerId\x12_\n\x11\x64\x65\x66\x61ult_caller_id\x18\x11 \x01(\x0b\x32\x33.api.commons.org.ManualDialSettings.DefaultCallerIdR\x0f\x64\x65\x66\x61ultCallerId\x12\x35\n\x17\x65nable_caller_id_bucket\x18\x12 \x01(\x08R\x14\x65nableCallerIdBucket\x12\x35\n\x17random_caller_id_bucket\x18\x13 \x01(\x03R\x14randomCallerIdBucket\x12\x39\n\x19\x61utomate_random_caller_id\x18\x14 \x01(\x08R\x16\x61utomateRandomCallerId\x12\x31\n\x15\x65nable_mask_caller_id\x18\x15 \x01(\x08R\x12\x65nableMaskCallerId\x12,\n\x12\x65nable_sip_address\x18\x16 \x01(\x08R\x10\x65nableSipAddress\x12\x83\x01\n$natural_language_compliance_metadata\x18\x17 \x01(\x0b\x32\x32.api.commons.org.NaturalLanguageComplianceMetadataR!naturalLanguageComplianceMetadata\x12I\n\x0e\x64\x61ta_dip_scope\x18\x18 \x01(\x0e\x32#.api.commons.ManualDialDataDipScopeR\x0c\x64\x61taDipScope\x12-\n\x13\x64\x61ta_dip_config_sid\x18\x19 \x01(\x03R\x10\x64\x61taDipConfigSid\x12_\n\x18\x64\x61ta_dip_result_handling\x18\x1a \x01(\x0e\x32&.api.commons.ManualDialDataDipHandlingR\x15\x64\x61taDipResultHandling\x12\x80\x01\n\x1d\x64\x61ta_dip_integration_mappings\x18\x1b \x03(\x0b\x32=.api.commons.org.ManualDialSettings.DataDipIntegrationMappingR\x1a\x64\x61taDipIntegrationMappings\x12i\n\x1d\x64\x61ta_dip_integration_handling\x18\x1c \x01(\x0e\x32&.api.commons.ManualDialDataDipHandlingR\x1a\x64\x61taDipIntegrationHandling\x12N\n\"enable_reject_option_for_approvers\x18\x1d \x01(\x08\x42\x02\x18\x01R\x1e\x65nableRejectOptionForApprovers\x1a\x84\x02\n\rScrubOverride\x12\x30\n\x14\x65nable_dncl_override\x18\x01 \x01(\x08R\x12\x65nableDnclOverride\x12;\n\x1a\x65nable_cell_scrub_override\x18\x02 \x01(\x08R\x17\x65nableCellScrubOverride\x12\x44\n\x1f\x65nable_time_zone_scrub_override\x18\x03 \x01(\x08R\x1b\x65nableTimeZoneScrubOverride\x12>\n\x1bnatural_compliance_override\x18\x04 \x01(\x08R\x19naturalComplianceOverride\x1ay\n\x0f\x44\x65\x66\x61ultCallerId\x12<\n\x05usage\x18\x01 \x01(\x0e\x32&.api.commons.DefaultManualDialCallerIdR\x05usage\x12(\n\x10\x63ustom_caller_id\x18\x02 \x01(\tR\x0e\x63ustomCallerId\x1a\xdb\x01\n\x19\x44\x61taDipIntegrationMapping\x12L\n\x0cmapping_type\x18\x01 \x01(\x0e\x32).api.commons.ManualDialDataDipIntegrationR\x0bmappingType\x12-\n\x13\x64\x61ta_dip_return_key\x18\x02 \x01(\tR\x10\x64\x61taDipReturnKey\x12\x41\n\x1d\x63ontact_field_description_sid\x18\x03 \x01(\x03R\x1a\x63ontactFieldDescriptionSid\"\x93\x01\n\x1eNaturalLanguageComplianceScrub\x12Q\n\x10\x63ompliance_scrub\x18\x01 \x01(\x0e\x32&.api.commons.HuntGroupOrgDefaultCustomR\x0f\x63omplianceScrub\x12\x1e\n\x0brule_set_id\x18\x02 \x01(\tR\truleSetId\"\x87\x01\n!NaturalLanguageComplianceMetadata\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12#\n\roptional_data\x18\x02 \x03(\x03R\x0coptionalData\x12#\n\rrequired_data\x18\x03 \x03(\x03R\x0crequiredData\"l\n\x12\x43\x61llerIdBucketData\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\x12\x1f\n\x0b\x62ucket_name\x18\x02 \x01(\tR\nbucketName\"\x8b\x17\n\x14TransferCallSettings\x12\'\n\x0f\x65nable_transfer\x18\x01 \x01(\x08R\x0e\x65nableTransfer\x12X\n\x0ehand_off_types\x18\x02 \x01(\x0b\x32\x32.api.commons.org.TransferCallSettings.HandOffTypesR\x0chandOffTypes\x12O\n\x10recording_status\x18\x03 \x01(\x0e\x32$.api.commons.TransferRecordingStatusR\x0frecordingStatus\x12Z\n\x0etransfer_types\x18\x04 \x01(\x0b\x32\x33.api.commons.org.TransferCallSettings.TransferTypesR\rtransferTypes\x12J\n\"display_transfer_number_phone_book\x18\x05 \x01(\x08R\x1e\x64isplayTransferNumberPhoneBook\x12\x43\n\x1e\x65nable_transfer_number_editing\x18\x06 \x01(\x08R\x1b\x65nableTransferNumberEditing\x12\x36\n\x17\x64\x65\x66\x61ult_transfer_number\x18\x07 \x01(\tR\x15\x64\x65\x66\x61ultTransferNumber\x12\x36\n\x17start_recording_numbers\x18\x08 \x03(\tR\x15startRecordingNumbers\x12\x34\n\x16stop_recording_numbers\x18\t \x03(\tR\x14stopRecordingNumbers\x12L\n\x17transfer_number_country\x18\n \x01(\x0e\x32\x14.api.commons.CountryR\x15transferNumberCountry\x12K\n\"display_transfer_country_selection\x18\x0b \x01(\x08R\x1f\x64isplayTransferCountrySelection\x12>\n\x1c\x64isplay_caller_id_phone_book\x18\x0c \x01(\x08R\x18\x64isplayCallerIdPhoneBook\x12\x37\n\x18\x65nable_caller_id_editing\x18\r \x01(\x08R\x15\x65nableCallerIdEditing\x12\x61\n\x11\x64\x65\x66\x61ult_caller_id\x18\x0e \x01(\x0b\x32\x35.api.commons.org.TransferCallSettings.DefaultCallerIdR\x0f\x64\x65\x66\x61ultCallerId\x12@\n\x11\x63\x61ller_id_country\x18\x0f \x01(\x0e\x32\x14.api.commons.CountryR\x0f\x63\x61llerIdCountry\x12L\n#display_caller_id_country_selection\x18\x10 \x01(\x08R\x1f\x64isplayCallerIdCountrySelection\x12G\n display_agent_transfer_filtering\x18\x11 \x01(\x08R\x1d\x64isplayAgentTransferFiltering\x12G\n default_agent_transfer_filtering\x18\x12 \x01(\x08R\x1d\x64\x65\x66\x61ultAgentTransferFiltering\x12=\n\x1b\x65nable_hunt_group_filtering\x18\x13 \x01(\x08R\x18\x65nableHuntGroupFiltering\x12q\n\x14requeue_queue_config\x18\x14 \x01(\x0b\x32?.api.commons.org.TransferCallSettings.RequeueQueueConfigurationR\x12requeueQueueConfig\x12\x7f\n\x1brequeue_transfer_disallowed\x18\x15 \x01(\x0b\x32?.api.commons.org.TransferCallSettings.RequeueTransferDisallowedR\x19requeueTransferDisallowed\x12s\n\x17pbx_transfer_disallowed\x18\x16 \x01(\x0b\x32;.api.commons.org.TransferCallSettings.PbxTransferDisallowedR\x15pbxTransferDisallowed\x12\x32\n\x15\x65nable_scrub_override\x18\x17 \x01(\x08R\x13\x65nableScrubOverride\x12)\n\x10\x65nable_whitelist\x18\x18 \x01(\x08R\x0f\x65nableWhitelist\x12i\n\x18natural_compliance_scrub\x18\x19 \x01(\x0b\x32/.api.commons.org.NaturalLanguageComplianceScrubR\x16naturalComplianceScrub\x12\x83\x01\n$natural_language_compliance_metadata\x18\x1a \x01(\x0b\x32\x32.api.commons.org.NaturalLanguageComplianceMetadataR!naturalLanguageComplianceMetadata\x1a}\n\x0cHandOffTypes\x12+\n\x11\x65nable_conference\x18\x01 \x01(\x08R\x10\x65nableConference\x12\x1f\n\x0b\x65nable_warm\x18\x02 \x01(\x08R\nenableWarm\x12\x1f\n\x0b\x65nable_cold\x18\x03 \x01(\x08R\nenableCold\x1a\xac\x02\n\rTransferTypes\x12\x32\n\x15\x65nable_agent_transfer\x18\x01 \x01(\x08R\x13\x65nableAgentTransfer\x12\x30\n\x14\x65nable_open_transfer\x18\x02 \x01(\x08R\x12\x65nableOpenTransfer\x12\x36\n\x17\x65nable_requeue_transfer\x18\x03 \x01(\x08R\x15\x65nableRequeueTransfer\x12\x41\n\x1d\x65nable_pbx_extension_transfer\x18\x04 \x01(\x08R\x1a\x65nablePbxExtensionTransfer\x12:\n\x19\x65nable_voicemail_transfer\x18\x05 \x01(\x08R\x17\x65nableVoicemailTransfer\x1a\x85\x01\n\x19RequeueTransferDisallowed\x12\x16\n\x06\x65nable\x18\x01 \x01(\x08R\x06\x65nable\x12(\n\x10\x61gent_skill_sids\x18\x02 \x03(\x03R\x0e\x61gentSkillSids\x12&\n\x0fhunt_group_sids\x18\x03 \x03(\x03R\rhuntGroupSids\x1aO\n\x15PbxTransferDisallowed\x12\x16\n\x06\x65nable\x18\x01 \x01(\x08R\x06\x65nable\x12\x1e\n\nextensions\x18\x02 \x03(\tR\nextensions\x1a{\n\x19RequeueQueueConfiguration\x12=\n\x05usage\x18\x01 \x01(\x0e\x32\'.api.commons.RequeueTransferQueueConfigR\x05usage\x12\x1f\n\x0b\x63ustom_name\x18\x02 \x01(\tR\ncustomName\x1aw\n\x0f\x44\x65\x66\x61ultCallerId\x12:\n\x05usage\x18\x01 \x01(\x0e\x32$.api.commons.DefaultTransferCallerIdR\x05usage\x12(\n\x10\x63ustom_caller_id\x18\x02 \x01(\tR\x0e\x63ustomCallerId\"\xf3\x01\n\x15NumberHistorySettings\x12#\n\renable_search\x18\x01 \x01(\x08R\x0c\x65nableSearch\x12\x34\n\x16\x65nable_report_download\x18\x02 \x01(\x08R\x14\x65nableReportDownload\x12<\n\x1a\x65nable_recordings_download\x18\x03 \x01(\x08R\x18\x65nableRecordingsDownload\x12\x41\n\x1d\x65nable_agent_response_editing\x18\x04 \x01(\x08R\x1a\x65nableAgentResponseEditing\"\xe4\x01\n\x18\x41gentResponseAutoRuleSet\x12\x1f\n\x0bruleset_sid\x18\x01 \x01(\x03R\nrulesetSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12.\n\x07\x63ountry\x18\x04 \x01(\x0e\x32\x14.api.commons.CountryR\x07\x63ountry\x12\x41\n\tresponses\x18\x05 \x03(\x0b\x32#.api.commons.org.AutoResponseChoiceR\tresponses\"\x91\x01\n\x12\x41utoResponseChoice\x12.\n\x13\x61gent_call_response\x18\x01 \x01(\tR\x11\x61gentCallResponse\x12K\n\x0b\x63omparitors\x18\x02 \x03(\x0b\x32).api.commons.org.AgentResponseComparitorsR\x0b\x63omparitors\"P\n\x18\x41gentResponseComparitors\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x1e\n\nexpiration\x18\x02 \x01(\x03R\nexpiration\"\xea\x07\n\rDataDipConfig\x12\x1f\n\x0b\x63onfig_name\x18\x01 \x01(\tR\nconfigName\x12\x1f\n\x0b\x63onfig_type\x18\x02 \x01(\tR\nconfigType\x12\x1d\n\nremote_url\x18\x03 \x01(\tR\tremoteUrl\x12i\n\x17param_type_value_tuples\x18\x04 \x03(\x0b\x32\x32.api.commons.org.DataDipConfig.ParamTypeValueTupleR\x14paramTypeValueTuples\x12<\n\x06params\x18\x05 \x03(\x0b\x32$.api.commons.org.DataDipConfig.ParamR\x06params\x12=\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32).api.commons.org.DataDipConfig.ReturnDataR\x04\x64\x61ta\x12%\n\x0erequest_method\x18\x07 \x01(\tR\rrequestMethod\x12\x35\n\x17xml_client_property_sid\x18\x08 \x01(\x03R\x14xmlClientPropertySid\x12?\n\x07headers\x18\t \x03(\x0b\x32%.api.commons.org.DataDipConfig.HeaderR\x07headers\x1a\xad\x01\n\x05Param\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x1d\n\nparam_type\x18\x03 \x01(\tR\tparamType\x12[\n\x0f\x63omposite_value\x18\x04 \x03(\x0b\x32\x32.api.commons.org.DataDipConfig.ParamTypeValueTupleR\x0e\x63ompositeValue\x1a=\n\x13ParamTypeValueTuple\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x1a\x41\n\nReturnData\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0b\x61\x63\x63\x65ss_type\x18\x02 \x01(\tR\naccessType\x1a\xbe\x01\n\x06Header\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x1f\n\x0bheader_type\x18\x03 \x01(\tR\nheaderType\x12i\n\x17param_type_value_tuples\x18\x04 \x03(\x0b\x32\x32.api.commons.org.DataDipConfig.ParamTypeValueTupleR\x14paramTypeValueTuplesB\x83\x01\n\x13\x63om.api.commons.orgB\x0eHuntgroupProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.huntgroup_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\016HuntgroupProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_MANUALDIALSETTINGS'].fields_by_name['enable_reject_option_for_approvers']._options = None
  _globals['_MANUALDIALSETTINGS'].fields_by_name['enable_reject_option_for_approvers']._serialized_options = b'\030\001'
  _globals['_HUNTGROUPSETTINGS']._serialized_start=103
  _globals['_HUNTGROUPSETTINGS']._serialized_end=740
  _globals['_GENERALSETTINGS']._serialized_start=743
  _globals['_GENERALSETTINGS']._serialized_end=5717
  _globals['_GENERALSETTINGS_PAUSEOPTIONSET']._serialized_start=4218
  _globals['_GENERALSETTINGS_PAUSEOPTIONSET']._serialized_end=4285
  _globals['_GENERALSETTINGS_HOLDQUEUEMONITORING']._serialized_start=4288
  _globals['_GENERALSETTINGS_HOLDQUEUEMONITORING']._serialized_end=4527
  _globals['_GENERALSETTINGS_DATADIPDATADISPLAY']._serialized_start=4529
  _globals['_GENERALSETTINGS_DATADIPDATADISPLAY']._serialized_end=4651
  _globals['_GENERALSETTINGS_INTEGRATIONDATADISPLAY']._serialized_start=4654
  _globals['_GENERALSETTINGS_INTEGRATIONDATADISPLAY']._serialized_end=4794
  _globals['_GENERALSETTINGS_JOURNEYDATADISPLAY']._serialized_start=4796
  _globals['_GENERALSETTINGS_JOURNEYDATADISPLAY']._serialized_end=4916
  _globals['_GENERALSETTINGS_AGENTLOGINGUISTATISTICSDISPLAY']._serialized_start=4919
  _globals['_GENERALSETTINGS_AGENTLOGINGUISTATISTICSDISPLAY']._serialized_end=5105
  _globals['_GENERALSETTINGS_PHONEZIPMETADATADISPLAY']._serialized_start=5108
  _globals['_GENERALSETTINGS_PHONEZIPMETADATADISPLAY']._serialized_end=5289
  _globals['_GENERALSETTINGS_DISALLOWEDHUNTGROUPS']._serialized_start=5291
  _globals['_GENERALSETTINGS_DISALLOWEDHUNTGROUPS']._serialized_end=5372
  _globals['_GENERALSETTINGS_ALPHANUMERICKEYPAD']._serialized_start=5374
  _globals['_GENERALSETTINGS_ALPHANUMERICKEYPAD']._serialized_end=5492
  _globals['_GENERALSETTINGS_INBOUNDCOMPLIANCEMETADATA']._serialized_start=5494
  _globals['_GENERALSETTINGS_INBOUNDCOMPLIANCEMETADATA']._serialized_end=5621
  _globals['_GENERALSETTINGS_PREPARESTATECALLDELIVERY']._serialized_start=5623
  _globals['_GENERALSETTINGS_PREPARESTATECALLDELIVERY']._serialized_end=5717
  _globals['_COMMUNICATIONSETTINGS']._serialized_start=5720
  _globals['_COMMUNICATIONSETTINGS']._serialized_end=7620
  _globals['_COMMUNICATIONSETTINGS_SCRUBLISTEXPIRATION']._serialized_start=7018
  _globals['_COMMUNICATIONSETTINGS_SCRUBLISTEXPIRATION']._serialized_end=7254
  _globals['_COMMUNICATIONSETTINGS_AUTOMATERESPONSERULES']._serialized_start=7256
  _globals['_COMMUNICATIONSETTINGS_AUTOMATERESPONSERULES']._serialized_end=7332
  _globals['_COMMUNICATIONSETTINGS_AUTOMATESCRUBLISTCALLDATA']._serialized_start=7335
  _globals['_COMMUNICATIONSETTINGS_AUTOMATESCRUBLISTCALLDATA']._serialized_end=7620
  _globals['_COMMUNICATIONSETTINGS_AUTOMATESCRUBLISTCALLDATA_SCRUBLISTDATAFIELD']._serialized_start=7529
  _globals['_COMMUNICATIONSETTINGS_AUTOMATESCRUBLISTCALLDATA_SCRUBLISTDATAFIELD']._serialized_end=7620
  _globals['_CALLBACKSETTINGS']._serialized_start=7623
  _globals['_CALLBACKSETTINGS']._serialized_end=8617
  _globals['_CALLBACKSETTINGS_DEFAULTROUTING']._serialized_start=8226
  _globals['_CALLBACKSETTINGS_DEFAULTROUTING']._serialized_end=8424
  _globals['_CALLBACKSETTINGS_CALLBACKROUTINGDISALLOWED']._serialized_start=8427
  _globals['_CALLBACKSETTINGS_CALLBACKROUTINGDISALLOWED']._serialized_end=8617
  _globals['_PREVIEWDIALSETTINGS']._serialized_start=8620
  _globals['_PREVIEWDIALSETTINGS']._serialized_end=8919
  _globals['_MANUALDIALSETTINGS']._serialized_start=8922
  _globals['_MANUALDIALSETTINGS']._serialized_end=11834
  _globals['_MANUALDIALSETTINGS_SCRUBOVERRIDE']._serialized_start=11229
  _globals['_MANUALDIALSETTINGS_SCRUBOVERRIDE']._serialized_end=11489
  _globals['_MANUALDIALSETTINGS_DEFAULTCALLERID']._serialized_start=11491
  _globals['_MANUALDIALSETTINGS_DEFAULTCALLERID']._serialized_end=11612
  _globals['_MANUALDIALSETTINGS_DATADIPINTEGRATIONMAPPING']._serialized_start=11615
  _globals['_MANUALDIALSETTINGS_DATADIPINTEGRATIONMAPPING']._serialized_end=11834
  _globals['_NATURALLANGUAGECOMPLIANCESCRUB']._serialized_start=11837
  _globals['_NATURALLANGUAGECOMPLIANCESCRUB']._serialized_end=11984
  _globals['_NATURALLANGUAGECOMPLIANCEMETADATA']._serialized_start=11987
  _globals['_NATURALLANGUAGECOMPLIANCEMETADATA']._serialized_end=12122
  _globals['_CALLERIDBUCKETDATA']._serialized_start=12124
  _globals['_CALLERIDBUCKETDATA']._serialized_end=12232
  _globals['_TRANSFERCALLSETTINGS']._serialized_start=12235
  _globals['_TRANSFERCALLSETTINGS']._serialized_end=15190
  _globals['_TRANSFERCALLSETTINGS_HANDOFFTYPES']._serialized_start=14299
  _globals['_TRANSFERCALLSETTINGS_HANDOFFTYPES']._serialized_end=14424
  _globals['_TRANSFERCALLSETTINGS_TRANSFERTYPES']._serialized_start=14427
  _globals['_TRANSFERCALLSETTINGS_TRANSFERTYPES']._serialized_end=14727
  _globals['_TRANSFERCALLSETTINGS_REQUEUETRANSFERDISALLOWED']._serialized_start=14730
  _globals['_TRANSFERCALLSETTINGS_REQUEUETRANSFERDISALLOWED']._serialized_end=14863
  _globals['_TRANSFERCALLSETTINGS_PBXTRANSFERDISALLOWED']._serialized_start=14865
  _globals['_TRANSFERCALLSETTINGS_PBXTRANSFERDISALLOWED']._serialized_end=14944
  _globals['_TRANSFERCALLSETTINGS_REQUEUEQUEUECONFIGURATION']._serialized_start=14946
  _globals['_TRANSFERCALLSETTINGS_REQUEUEQUEUECONFIGURATION']._serialized_end=15069
  _globals['_TRANSFERCALLSETTINGS_DEFAULTCALLERID']._serialized_start=15071
  _globals['_TRANSFERCALLSETTINGS_DEFAULTCALLERID']._serialized_end=15190
  _globals['_NUMBERHISTORYSETTINGS']._serialized_start=15193
  _globals['_NUMBERHISTORYSETTINGS']._serialized_end=15436
  _globals['_AGENTRESPONSEAUTORULESET']._serialized_start=15439
  _globals['_AGENTRESPONSEAUTORULESET']._serialized_end=15667
  _globals['_AUTORESPONSECHOICE']._serialized_start=15670
  _globals['_AUTORESPONSECHOICE']._serialized_end=15815
  _globals['_AGENTRESPONSECOMPARITORS']._serialized_start=15817
  _globals['_AGENTRESPONSECOMPARITORS']._serialized_end=15897
  _globals['_DATADIPCONFIG']._serialized_start=15900
  _globals['_DATADIPCONFIG']._serialized_end=16902
  _globals['_DATADIPCONFIG_PARAM']._serialized_start=16406
  _globals['_DATADIPCONFIG_PARAM']._serialized_end=16579
  _globals['_DATADIPCONFIG_PARAMTYPEVALUETUPLE']._serialized_start=16581
  _globals['_DATADIPCONFIG_PARAMTYPEVALUETUPLE']._serialized_end=16642
  _globals['_DATADIPCONFIG_RETURNDATA']._serialized_start=16644
  _globals['_DATADIPCONFIG_RETURNDATA']._serialized_end=16709
  _globals['_DATADIPCONFIG_HEADER']._serialized_start=16712
  _globals['_DATADIPCONFIG_HEADER']._serialized_end=16902
# @@protoc_insertion_point(module_scope)
