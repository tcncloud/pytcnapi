# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/audit.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'api/commons/audit/audit.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import agent_training_events_pb2 as api_dot_commons_dot_audit_dot_agent__training__events__pb2
from api.commons.audit import asm_events_pb2 as api_dot_commons_dot_audit_dot_asm__events__pb2
from api.commons.audit import billing_events_pb2 as api_dot_commons_dot_audit_dot_billing__events__pb2
from api.commons.audit import compliance_events_pb2 as api_dot_commons_dot_audit_dot_compliance__events__pb2
from api.commons.audit import contactmanager_events_pb2 as api_dot_commons_dot_audit_dot_contactmanager__events__pb2
from api.commons.audit import delivery_events_pb2 as api_dot_commons_dot_audit_dot_delivery__events__pb2
from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from api.commons.audit import events_pb2 as api_dot_commons_dot_audit_dot_events__pb2
from api.commons.audit import lms_events_pb2 as api_dot_commons_dot_audit_dot_lms__events__pb2
from api.commons.audit import omnichannel_events_pb2 as api_dot_commons_dot_audit_dot_omnichannel__events__pb2
from api.commons.audit import organization_events_pb2 as api_dot_commons_dot_audit_dot_organization__events__pb2
from api.commons.audit import scorecards_events_pb2 as api_dot_commons_dot_audit_dot_scorecards__events__pb2
from api.commons.audit import tickets_events_pb2 as api_dot_commons_dot_audit_dot_tickets__events__pb2
from api.commons.audit import vana_events_pb2 as api_dot_commons_dot_audit_dot_vana__events__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/commons/audit/audit.proto\x12\x11\x61pi.commons.audit\x1a-api/commons/audit/agent_training_events.proto\x1a\"api/commons/audit/asm_events.proto\x1a&api/commons/audit/billing_events.proto\x1a)api/commons/audit/compliance_events.proto\x1a-api/commons/audit/contactmanager_events.proto\x1a\'api/commons/audit/delivery_events.proto\x1a#api/commons/audit/event_types.proto\x1a\x1e\x61pi/commons/audit/events.proto\x1a\"api/commons/audit/lms_events.proto\x1a*api/commons/audit/omnichannel_events.proto\x1a+api/commons/audit/organization_events.proto\x1a)api/commons/audit/scorecards_events.proto\x1a&api/commons/audit/tickets_events.proto\x1a#api/commons/audit/vana_events.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9b\x81\x01\n\nAuditEvent\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tregion_id\x18\x02 \x01(\tR\x08regionId\x12\x1d\n\ncluster_id\x18\x03 \x01(\tR\tclusterId\x12\x39\n\nevent_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\teventTime\x12\x19\n\x08\x61udit_id\x18\x05 \x01(\tR\x07\x61uditId\x12;\n\nevent_type\x18\n \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\x12\x41\n\x0c_dummy_event\x18\x64 \x01(\x0b\x32\x1d.api.commons.audit.DummyEventH\x00R\nDummyEvent\x12K\n\x0fvana_flag_event\x18\xc8\x01 \x01(\x0b\x32 .api.commons.audit.VanaFlagEventH\x00R\rvanaFlagEvent\x12^\n\x16vana_flag_review_event\x18\xc9\x01 \x01(\x0b\x32&.api.commons.audit.VanaFlagReviewEventH\x00R\x13vanaFlagReviewEvent\x12g\n\x19vana_billing_report_event\x18\xca\x01 \x01(\x0b\x32).api.commons.audit.VanaBillingReportEventH\x00R\x16vanaBillingReportEvent\x12\x61\n\x17vana_flag_summary_event\x18\xcb\x01 \x01(\x0b\x32\'.api.commons.audit.VanaFlagSummaryEventH\x00R\x14vanaFlagSummaryEvent\x12p\n\x1cvana_phrase_correction_event\x18\xcc\x01 \x01(\x0b\x32,.api.commons.audit.VanaPhraseCorrectionEventH\x00R\x19vanaPhraseCorrectionEvent\x12p\n\x1cvana_create_transcript_event\x18\xcd\x01 \x01(\x0b\x32,.api.commons.audit.VanaCreateTranscriptEventH\x00R\x19vanaCreateTranscriptEvent\x12m\n\x1bvana_create_sentiment_event\x18\xce\x01 \x01(\x0b\x32+.api.commons.audit.VanaCreateSentimentEventH\x00R\x18vanaCreateSentimentEvent\x12g\n\x19vana_create_summary_event\x18\xcf\x01 \x01(\x0b\x32).api.commons.audit.VanaCreateSummaryEventH\x00R\x16vanaCreateSummaryEvent\x12|\n omnichannel_create_project_event\x18\xac\x02 \x01(\x0b\x32\x30.api.commons.audit.OmnichannelCreateProjectEventH\x00R\x1domnichannelCreateProjectEvent\x12\x7f\n!omnichannel_create_campaign_event\x18\xad\x02 \x01(\x0b\x32\x31.api.commons.audit.OmnichannelCreateCampaignEventH\x00R\x1eomnichannelCreateCampaignEvent\x12\x8c\x01\n&omnichannel_daily_project_report_event\x18\xae\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelDailyProjectReportEventH\x00R\"omnichannelDailyProjectReportEvent\x12\x9b\x01\n+omnichannel_daily_conversation_report_event\x18\xaf\x02 \x01(\x0b\x32:.api.commons.audit.OmnichannelDailyConversationReportEventH\x00R\'omnichannelDailyConversationReportEvent\x12\x9b\x01\n+omnichannel_agent_assign_conversation_event\x18\xb1\x02 \x01(\x0b\x32:.api.commons.audit.OmnichannelAgentAssignConversationEventH\x00R\'omnichannelAgentAssignConversationEvent\x12\xa1\x01\n-omnichannel_agent_unassign_conversation_event\x18\xb2\x02 \x01(\x0b\x32<.api.commons.audit.OmnichannelAgentUnassignConversationEventH\x00R)omnichannelAgentUnassignConversationEvent\x12\xa1\x01\n-omnichannel_agent_reassign_conversation_event\x18\xb3\x02 \x01(\x0b\x32<.api.commons.audit.OmnichannelAgentReassignConversationEventH\x00R)omnichannelAgentReassignConversationEvent\x12]\n\x15omnichannel_t10_event\x18\xb4\x02 \x01(\x0b\x32&.api.commons.audit.OmnichannelT10EventH\x00R\x13omnichannelT10Event\x12\x93\x01\n\'omnichannel_customer_text_Message_event\x18\xb5\x02 \x01(\x0b\x32\x36.api.commons.audit.OmnichannelCustomerTextMessageEventB\x02\x18\x01H\x00R#omnichannelCustomerTextMessageEvent\x12\x8a\x01\n$omnichannel_agent_text_message_event\x18\xb6\x02 \x01(\x0b\x32\x33.api.commons.audit.OmnichannelAgentTextMessageEventB\x02\x18\x01H\x00R omnichannelAgentTextMessageEvent\x12z\n omnichannel_finish_wrap_up_event\x18\xb7\x02 \x01(\x0b\x32/.api.commons.audit.OmnichannelFinishWrapUpEventH\x00R\x1comnichannelFinishWrapUpEvent\x12w\n\x1fomnichannel_begin_wrap_up_event\x18\xb8\x02 \x01(\x0b\x32..api.commons.audit.OmnichannelBeginWrapUpEventH\x00R\x1bomnichannelBeginWrapUpEvent\x12]\n\x15omnichannel_t11_event\x18\xb9\x02 \x01(\x0b\x32&.api.commons.audit.OmnichannelT11EventH\x00R\x13omnichannelT11Event\x12\x8b\x01\n%omnichannel_create_conversation_event\x18\xba\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelCreateConversationEventH\x00R\"omnichannelCreateConversationEvent\x12y\n\x1fomnichannel_agent_suspend_event\x18\xbb\x02 \x01(\x0b\x32/.api.commons.audit.OmnichannelAgentSuspendEventH\x00R\x1comnichannelAgentSuspendEvent\x12\x88\x01\n$omnichannel_close_conversation_event\x18\xc2\x02 \x01(\x0b\x32\x34.api.commons.audit.OmnichannelCloseConversationEventH\x00R!omnichannelCloseConversationEvent\x12\x90\x01\n&omnichannel_manager_text_message_event\x18\xcc\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelManagerTextMessageEventB\x02\x18\x01H\x00R\"omnichannelManagerTextMessageEvent\x12\x7f\n!omnichannel_update_campaign_event\x18\xca\x02 \x01(\x0b\x32\x31.api.commons.audit.OmnichannelUpdateCampaignEventH\x00R\x1eomnichannelUpdateCampaignEvent\x12\xab\x01\n1omnichannel_set_conversation_collected_data_event\x18\xcb\x02 \x01(\x0b\x32?.api.commons.audit.OmnichannelSetConversationCollectedDataEventH\x00R,omnichannelSetConversationCollectedDataEvent\x12\x85\x01\n#omnichannel_complete_campaign_event\x18\xdc\x02 \x01(\x0b\x32\x33.api.commons.audit.OmnichannelCompleteCampaignEventH\x00R omnichannelCompleteCampaignEvent\x12\x82\x01\n\"omnichannel_archive_campaign_event\x18\xcd\x02 \x01(\x0b\x32\x32.api.commons.audit.OmnichannelArchiveCampaignEventH\x00R\x1fomnichannelArchiveCampaignEvent\x12|\n omnichannel_pause_campaign_event\x18\xce\x02 \x01(\x0b\x32\x30.api.commons.audit.OmnichannelPauseCampaignEventH\x00R\x1domnichannelPauseCampaignEvent\x12\x7f\n!omnichannel_resume_campaign_event\x18\xcf\x02 \x01(\x0b\x32\x31.api.commons.audit.OmnichannelResumeCampaignEventH\x00R\x1eomnichannelResumeCampaignEvent\x12|\n omnichannel_start_campaign_event\x18\xd0\x02 \x01(\x0b\x32\x30.api.commons.audit.OmnichannelStartCampaignEventH\x00R\x1domnichannelStartCampaignEvent\x12\x7f\n!omnichannel_schedule_module_event\x18\xd1\x02 \x01(\x0b\x32\x31.api.commons.audit.OmnichannelScheduleModuleEventH\x00R\x1eomnichannelScheduleModuleEvent\x12v\n\x1eomnichannel_start_module_event\x18\xd2\x02 \x01(\x0b\x32..api.commons.audit.OmnichannelStartModuleEventH\x00R\x1bomnichannelStartModuleEvent\x12v\n\x1eomnichannel_pause_module_event\x18\xd3\x02 \x01(\x0b\x32..api.commons.audit.OmnichannelPauseModuleEventH\x00R\x1bomnichannelPauseModuleEvent\x12y\n\x1fomnichannel_resume_module_event\x18\xd4\x02 \x01(\x0b\x32/.api.commons.audit.OmnichannelResumeModuleEventH\x00R\x1comnichannelResumeModuleEvent\x12v\n\x1eomnichannel_error_module_event\x18\xd5\x02 \x01(\x0b\x32..api.commons.audit.OmnichannelErrorModuleEventH\x00R\x1bomnichannelErrorModuleEvent\x12|\n omnichannel_success_module_event\x18\xd6\x02 \x01(\x0b\x32\x30.api.commons.audit.OmnichannelSuccessModuleEventH\x00R\x1domnichannelSuccessModuleEvent\x12s\n\x1domnichannel_fail_module_event\x18\xd7\x02 \x01(\x0b\x32-.api.commons.audit.OmnichannelFailModuleEventH\x00R\x1aomnichannelFailModuleEvent\x12\x7f\n!omnichannel_complete_module_event\x18\xd8\x02 \x01(\x0b\x32\x31.api.commons.audit.OmnichannelCompleteModuleEventH\x00R\x1eomnichannelCompleteModuleEvent\x12|\n omnichannel_archive_module_event\x18\xd9\x02 \x01(\x0b\x32\x30.api.commons.audit.OmnichannelArchiveModuleEventH\x00R\x1domnichannelArchiveModuleEvent\x12y\n\x1fomnichannel_update_module_event\x18\xda\x02 \x01(\x0b\x32/.api.commons.audit.OmnichannelUpdateModuleEventH\x00R\x1comnichannelUpdateModuleEvent\x12\x9e\x01\n-omnichannel_add_sms_message_sent_module_event\x18\xdb\x02 \x01(\x0b\x32\x37.api.commons.audit.OmnichannelSmsMessageSentModuleEventB\x02\x18\x01H\x00R\'omnichannelAddSmsMessageSentModuleEvent\x12\x90\x01\n&omnichannel_module_initial_reply_event\x18\xdd\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelModuleInitialReplyEventB\x02\x18\x01H\x00R\"omnichannelModuleInitialReplyEvent\x12\x87\x01\n#omnichannel_task_message_sent_event\x18\xde\x02 \x01(\x0b\x32\x32.api.commons.audit.OmnichannelTaskMessageSentEventB\x02\x18\x01H\x00R\x1fomnichannelTaskMessageSentEvent\x12\x8c\x01\n&omnichannel_connected_inbox_poll_event\x18\xdf\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelConnectedInboxPollEventH\x00R\"omnichannelConnectedInboxPollEvent\x12\x95\x01\n)omnichannel_connected_inbox_created_event\x18\xe0\x02 \x01(\x0b\x32\x38.api.commons.audit.OmnichannelConnectedInboxCreatedEventH\x00R%omnichannelConnectedInboxCreatedEvent\x12\x8d\x01\n%omnichannel_agent_message_units_event\x18\xe1\x02 \x01(\x0b\x32\x34.api.commons.audit.OmnichannelAgentMessageUnitsEventB\x02\x18\x01H\x00R!omnichannelAgentMessageUnitsEvent\x12\x93\x01\n\'omnichannel_manager_message_units_event\x18\xe2\x02 \x01(\x0b\x32\x36.api.commons.audit.OmnichannelManagerMessageUnitsEventB\x02\x18\x01H\x00R#omnichannelManagerMessageUnitsEvent\x12\x96\x01\n(omnichannel_customer_message_units_event\x18\xe3\x02 \x01(\x0b\x32\x37.api.commons.audit.OmnichannelCustomerMessageUnitsEventB\x02\x18\x01H\x00R$omnichannelCustomerMessageUnitsEvent\x12\x90\x01\n&omnichannel_system_message_units_event\x18\xe4\x02 \x01(\x0b\x32\x35.api.commons.audit.OmnichannelSystemMessageUnitsEventB\x02\x18\x01H\x00R\"omnichannelSystemMessageUnitsEvent\x12\x83\x01\n#omnichannel_payment_link_sent_event\x18\xe5\x02 \x01(\x0b\x32\x32.api.commons.audit.OmnichannelPaymentLinkSentEventH\x00R\x1fomnichannelPaymentLinkSentEvent\x12\xa2\x01\n.omnichannel_manual_approve_task_accepted_event\x18\xe6\x02 \x01(\x0b\x32<.api.commons.audit.OmnichannelManualApproveTaskAcceptedEventH\x00R)omnichannelManualApproveTaskAcceptedEvent\x12\xa2\x01\n.omnichannel_manual_approve_task_rejected_event\x18\xe7\x02 \x01(\x0b\x32<.api.commons.audit.OmnichannelManualApproveTaskRejectedEventH\x00R)omnichannelManualApproveTaskRejectedEvent\x12\x9f\x01\n-omnichannel_manual_approve_task_timeout_event\x18\xe8\x02 \x01(\x0b\x32;.api.commons.audit.OmnichannelManualApproveTaskTimeoutEventH\x00R(omnichannelManualApproveTaskTimeoutEvent\x12\x9f\x01\n-omnichannel_manual_approve_task_requeue_event\x18\xe9\x02 \x01(\x0b\x32;.api.commons.audit.OmnichannelManualApproveTaskRequeueEventH\x00R(omnichannelManualApproveTaskRequeueEvent\x12\x82\x01\n\"omnichannel_transcript_saved_event\x18\xea\x02 \x01(\x0b\x32\x32.api.commons.audit.OmnichannelTranscriptSavedEventH\x00R\x1fomnichannelTranscriptSavedEvent\x12v\n\x1eomnichannel_message_sent_event\x18\xeb\x02 \x01(\x0b\x32..api.commons.audit.OmnichannelMessageSentEventH\x00R\x1bomnichannelMessageSentEvent\x12\x85\x01\n#omnichannel_provider_response_event\x18\xec\x02 \x01(\x0b\x32\x33.api.commons.audit.OmnichannelProviderResponseEventH\x00R omnichannelProviderResponseEvent\x12\x95\x01\n)omnichannel_provider_message_failed_event\x18\xed\x02 \x01(\x0b\x32\x38.api.commons.audit.OmnichannelProviderMessageFailedEventH\x00R%omnichannelProviderMessageFailedEvent\x12[\n\x15\x61sm_agent_login_event\x18\x90\x03 \x01(\x0b\x32%.api.commons.audit.AsmAgentLoginEventH\x00R\x12\x61smAgentLoginEvent\x12X\n\x14\x61sm_open_voice_event\x18\x91\x03 \x01(\x0b\x32$.api.commons.audit.AsmOpenVoiceEventH\x00R\x11\x61smOpenVoiceEvent\x12\x65\n\x19\x61sm_open_omni_agent_event\x18\x92\x03 \x01(\x0b\x32(.api.commons.audit.AsmOpenOmniAgentEventH\x00R\x15\x61smOpenOmniAgentEvent\x12y\n\x1f\x61sm_activate_conversation_event\x18\x93\x03 \x01(\x0b\x32/.api.commons.audit.AsmActivateConversationEventH\x00R\x1c\x61smActivateConversationEvent\x12\x7f\n!asm_deactivate_conversation_event\x18\x94\x03 \x01(\x0b\x32\x31.api.commons.audit.AsmDeactivateConversationEventH\x00R\x1e\x61smDeactivateConversationEvent\x12q\n\x1d\x61sm_agent_state_changed_event\x18\x95\x03 \x01(\x0b\x32,.api.commons.audit.AsmAgentStateChangedEventH\x00R\x19\x61smAgentStateChangedEvent\x12^\n\x16\x61sm_agent_logout_event\x18\x96\x03 \x01(\x0b\x32&.api.commons.audit.AsmAgentLogoutEventH\x00R\x13\x61smAgentLogoutEvent\x12K\n\x0f\x61sm_pause_event\x18\x97\x03 \x01(\x0b\x32 .api.commons.audit.AsmPauseEventH\x00R\rasmPauseEvent\x12N\n\x10\x61sm_resume_event\x18\x98\x03 \x01(\x0b\x32!.api.commons.audit.AsmResumeEventH\x00R\x0e\x61smResumeEvent\x12s\n\x1d\x61sm_conversation_pulled_event\x18\x99\x03 \x01(\x0b\x32-.api.commons.audit.AsmConversationPulledEventH\x00R\x1a\x61smConversationPulledEvent\x12|\n scorecards_create_question_event\x18\xf4\x03 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsCreateQuestionEventH\x00R\x1dscorecardsCreateQuestionEvent\x12|\n scorecards_update_question_event\x18\xf5\x03 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsUpdateQuestionEventH\x00R\x1dscorecardsUpdateQuestionEvent\x12|\n scorecards_delete_question_event\x18\xf6\x03 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsDeleteQuestionEventH\x00R\x1dscorecardsDeleteQuestionEvent\x12\x7f\n!scorecards_create_scorecard_event\x18\xf7\x03 \x01(\x0b\x32\x31.api.commons.audit.ScorecardsCreateScorecardEventH\x00R\x1escorecardsCreateScorecardEvent\x12\x7f\n!scorecards_update_scorecard_event\x18\xf8\x03 \x01(\x0b\x32\x31.api.commons.audit.ScorecardsUpdateScorecardEventH\x00R\x1escorecardsUpdateScorecardEvent\x12\x7f\n!scorecards_delete_scorecard_event\x18\xf9\x03 \x01(\x0b\x32\x31.api.commons.audit.ScorecardsDeleteScorecardEventH\x00R\x1escorecardsDeleteScorecardEvent\x12|\n scorecards_clone_scorecard_event\x18\xfa\x03 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsCloneScorecardEventH\x00R\x1dscorecardsCloneScorecardEvent\x12\x82\x01\n\"scorecards_create_evaluation_event\x18\xfb\x03 \x01(\x0b\x32\x32.api.commons.audit.ScorecardsCreateEvaluationEventH\x00R\x1fscorecardsCreateEvaluationEvent\x12\x82\x01\n\"scorecards_delete_evaluation_event\x18\xfc\x03 \x01(\x0b\x32\x32.api.commons.audit.ScorecardsDeleteEvaluationEventH\x00R\x1fscorecardsDeleteEvaluationEvent\x12y\n\x1fscorecards_create_section_event\x18\xfd\x03 \x01(\x0b\x32/.api.commons.audit.ScorecardsCreateSectionEventH\x00R\x1cscorecardsCreateSectionEvent\x12y\n\x1fscorecards_update_section_event\x18\xfe\x03 \x01(\x0b\x32/.api.commons.audit.ScorecardsUpdateSectionEventH\x00R\x1cscorecardsUpdateSectionEvent\x12y\n\x1fscorecards_delete_section_event\x18\xff\x03 \x01(\x0b\x32/.api.commons.audit.ScorecardsDeleteSectionEventH\x00R\x1cscorecardsDeleteSectionEvent\x12|\n scorecards_create_category_event\x18\x80\x04 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsCreateCategoryEventH\x00R\x1dscorecardsCreateCategoryEvent\x12|\n scorecards_update_category_event\x18\x81\x04 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsUpdateCategoryEventH\x00R\x1dscorecardsUpdateCategoryEvent\x12|\n scorecards_delete_category_event\x18\x82\x04 \x01(\x0b\x32\x30.api.commons.audit.ScorecardsDeleteCategoryEventH\x00R\x1dscorecardsDeleteCategoryEvent\x12\x9b\x01\n+scorecards_create_evaluation_question_event\x18\x83\x04 \x01(\x0b\x32:.api.commons.audit.ScorecardsCreateEvaluationQuestionEventH\x00R\'scorecardsCreateEvaluationQuestionEvent\x12\x9b\x01\n+scorecards_update_evaluation_question_event\x18\x84\x04 \x01(\x0b\x32:.api.commons.audit.ScorecardsUpdateEvaluationQuestionEventH\x00R\'scorecardsUpdateEvaluationQuestionEvent\x12\x9b\x01\n+scorecards_delete_evaluation_question_event\x18\x85\x04 \x01(\x0b\x32:.api.commons.audit.ScorecardsDeleteEvaluationQuestionEventH\x00R\'scorecardsDeleteEvaluationQuestionEvent\x12\x98\x01\n*scorecards_create_scorecard_question_event\x18\x86\x04 \x01(\x0b\x32\x39.api.commons.audit.ScorecardsCreateScorecardQuestionEventH\x00R&scorecardsCreateScorecardQuestionEvent\x12\x98\x01\n*scorecards_update_scorecard_question_event\x18\x87\x04 \x01(\x0b\x32\x39.api.commons.audit.ScorecardsUpdateScorecardQuestionEventH\x00R&scorecardsUpdateScorecardQuestionEvent\x12\x98\x01\n*scorecards_delete_scorecard_question_event\x18\x88\x04 \x01(\x0b\x32\x39.api.commons.audit.ScorecardsDeleteScorecardQuestionEventH\x00R&scorecardsDeleteScorecardQuestionEvent\x12\x8f\x01\n\'scorecards_create_auto_evaluation_event\x18\x89\x04 \x01(\x0b\x32\x36.api.commons.audit.ScorecardsCreateAutoEvaluationEventH\x00R#scorecardsCreateAutoEvaluationEvent\x12\x82\x01\n\"scorecards_update_evaluation_event\x18\x8a\x04 \x01(\x0b\x32\x32.api.commons.audit.ScorecardsUpdateEvaluationEventH\x00R\x1fscorecardsUpdateEvaluationEvent\x12\x92\x01\n(scorecards_create_smart_evaluation_event\x18\x8b\x04 \x01(\x0b\x32\x37.api.commons.audit.ScorecardsCreateSmartEvaluationEventH\x00R$scorecardsCreateSmartEvaluationEvent\x12\x44\n\x0cticket_event\x18\xd9\x04 \x01(\x0b\x32\x1e.api.commons.audit.TicketEventH\x00R\x0bticketEvent\x12j\n\x1a\x63ompliance_rnd_query_event\x18\xbc\x05 \x01(\x0b\x32*.api.commons.audit.ComplianceRndQueryEventH\x00R\x17\x63omplianceRndQueryEvent\x12w\n!compliance_rnd_query_cached_event\x18\xbd\x05 \x01(\x0b\x32*.api.commons.audit.ComplianceRndQueryEventH\x00R\x1d\x63omplianceRndQueryCachedEvent\x12\xa8\x01\n0agent_training_create_learning_opportunity_event\x18\xa0\x06 \x01(\x0b\x32>.api.commons.audit.AgentTrainingCreateLearningOpportunityEventH\x00R+agentTrainingCreateLearningOpportunityEvent\x12j\n\x1alms_pipeline_failure_event\x18\x84\x07 \x01(\x0b\x32*.api.commons.audit.LMSPipelineFailureEventH\x00R\x17lmsPipelineFailureEvent\x12n\n\x1clms_pipeline_no_output_event\x18\x85\x07 \x01(\x0b\x32+.api.commons.audit.LMSPipelineNoOutputEventH\x00R\x18lmsPipelineNoOutputEvent\x12s\n\x1dlms_pipeline_successful_event\x18\x86\x07 \x01(\x0b\x32-.api.commons.audit.LMSPipelineSuccessfulEventH\x00R\x1almsPipelineSuccessfulEvent\x12\x81\x01\n!billing_commit_billing_plan_event\x18\xe8\x07 \x01(\x0b\x32\x30.api.commons.audit.BillingCommitBillingPlanEventB\x02\x18\x01H\x00R\x1d\x62illingCommitBillingPlanEvent\x12\x81\x01\n!billing_create_billing_plan_event\x18\xe9\x07 \x01(\x0b\x32\x30.api.commons.audit.BillingCreateBillingPlanEventB\x02\x18\x01H\x00R\x1d\x62illingCreateBillingPlanEvent\x12t\n\x1c\x62illing_create_invoice_event\x18\xea\x07 \x01(\x0b\x32,.api.commons.audit.BillingCreateInvoiceEventB\x02\x18\x01H\x00R\x19\x62illingCreateInvoiceEvent\x12\x8a\x01\n$billing_create_rate_definition_event\x18\xeb\x07 \x01(\x0b\x32\x33.api.commons.audit.BillingCreateRateDefinitionEventB\x02\x18\x01H\x00R billingCreateRateDefinitionEvent\x12\x81\x01\n!billing_delete_billing_plan_event\x18\xec\x07 \x01(\x0b\x32\x30.api.commons.audit.BillingDeleteBillingPlanEventB\x02\x18\x01H\x00R\x1d\x62illingDeleteBillingPlanEvent\x12t\n\x1c\x62illing_delete_invoice_event\x18\xed\x07 \x01(\x0b\x32,.api.commons.audit.BillingDeleteInvoiceEventB\x02\x18\x01H\x00R\x19\x62illingDeleteInvoiceEvent\x12\x8a\x01\n$billing_delete_rate_definition_event\x18\xee\x07 \x01(\x0b\x32\x33.api.commons.audit.BillingDeleteRateDefinitionEventB\x02\x18\x01H\x00R billingDeleteRateDefinitionEvent\x12t\n\x1c\x62illing_export_invoice_event\x18\xef\x07 \x01(\x0b\x32,.api.commons.audit.BillingExportInvoiceEventB\x02\x18\x01H\x00R\x19\x62illingExportInvoiceEvent\x12\x81\x01\n!billing_update_billing_plan_event\x18\xf0\x07 \x01(\x0b\x32\x30.api.commons.audit.BillingUpdateBillingPlanEventB\x02\x18\x01H\x00R\x1d\x62illingUpdateBillingPlanEvent\x12t\n\x1c\x62illing_update_invoice_event\x18\xf1\x07 \x01(\x0b\x32,.api.commons.audit.BillingUpdateInvoiceEventB\x02\x18\x01H\x00R\x19\x62illingUpdateInvoiceEvent\x12\x8a\x01\n$billing_update_rate_definition_event\x18\xf2\x07 \x01(\x0b\x32\x33.api.commons.audit.BillingUpdateRateDefinitionEventB\x02\x18\x01H\x00R billingUpdateRateDefinitionEvent\x12\x83\x01\n#billing_rated_items_generated_event\x18\xf3\x07 \x01(\x0b\x32\x32.api.commons.audit.BillingRatedItemsGeneratedEventH\x00R\x1f\x62illingRatedItemsGeneratedEvent\x12`\n\x16\x64\x65livery_failure_event\x18\xcc\x08 \x01(\x0b\x32\'.api.commons.audit.DeliveryFailureEventH\x00R\x14\x64\x65liveryFailureEvent\x12`\n\x16\x64\x65livery_success_event\x18\xcd\x08 \x01(\x0b\x32\'.api.commons.audit.DeliverySuccessEventH\x00R\x14\x64\x65liverySuccessEvent\x12w\n\x1f\x63ontact_manager_entry_add_event\x18\xb0\t \x01(\x0b\x32..api.commons.audit.ContactManagerEntryAddEventH\x00R\x1b\x63ontactManagerEntryAddEvent\x12\x81\x01\n#contact_manager_entry_get_enc_event\x18\xb1\t \x01(\x0b\x32\x31.api.commons.audit.ContactManagerEntryGetEncEventH\x00R\x1e\x63ontactManagerEntryGetEncEvent\x12t\n\x1c\x63ontact_manager_delete_event\x18\xb2\t \x01(\x0b\x32,.api.commons.audit.ContactManagerDeleteEventB\x02\x18\x01H\x00R\x19\x63ontactManagerDeleteEvent\x12k\n\x19\x63ontact_manager_kyc_event\x18\xb3\t \x01(\x0b\x32).api.commons.audit.ContactManagerKycEventB\x02\x18\x01H\x00R\x16\x63ontactManagerKycEvent\x12z\n contact_manager_entry_edit_event\x18\xb4\t \x01(\x0b\x32/.api.commons.audit.ContactManagerEntryEditEventH\x00R\x1c\x63ontactManagerEntryEditEvent\x12}\n!contact_manager_list_upload_event\x18\xb5\t \x01(\x0b\x32\x30.api.commons.audit.ContactManagerListUploadEventH\x00R\x1d\x63ontactManagerListUploadEvent\x12\x80\x01\n&contact_manager_kyc_verification_event\x18\xb6\t \x01(\x0b\x32).api.commons.audit.ContactManagerKycEventH\x00R\"contactManagerKycVerificationEvent\x12{\n\"contact_manager_entry_delete_event\x18\xb7\t \x01(\x0b\x32,.api.commons.audit.ContactManagerDeleteEventH\x00R\x1e\x63ontactManagerEntryDeleteEvent\x12}\n#contact_manager_entry_expunge_event\x18\xb8\t \x01(\x0b\x32,.api.commons.audit.ContactManagerDeleteEventH\x00R\x1f\x63ontactManagerEntryExpungeEvent\x12\x92\x01\n(contact_manager_entity_association_event\x18\xb9\t \x01(\x0b\x32\x37.api.commons.audit.ContactManagerEntityAssociationEventH\x00R$contactManagerEntityAssociationEvent\x12p\n\x1c\x61\x63\x63\x65ss_tokens_expiring_event\x18\x94\n \x01(\x0b\x32,.api.commons.audit.AccessTokensExpiringEventH\x00R\x19\x61\x63\x63\x65ssTokensExpiringEventB\x07\n\x05\x65ventB\x89\x01\n\x15\x63om.api.commons.auditB\nAuditProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.audit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\nAuditProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_customer_text_Message_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_customer_text_Message_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_agent_text_message_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_agent_text_message_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_manager_text_message_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_manager_text_message_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_add_sms_message_sent_module_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_add_sms_message_sent_module_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_module_initial_reply_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_module_initial_reply_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_task_message_sent_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_task_message_sent_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_agent_message_units_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_agent_message_units_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_manager_message_units_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_manager_message_units_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_customer_message_units_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_customer_message_units_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_system_message_units_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['omnichannel_system_message_units_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_commit_billing_plan_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_commit_billing_plan_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_create_billing_plan_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_create_billing_plan_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_create_invoice_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_create_invoice_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_create_rate_definition_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_create_rate_definition_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_billing_plan_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_billing_plan_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_invoice_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_invoice_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_rate_definition_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_delete_rate_definition_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_export_invoice_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_export_invoice_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_update_billing_plan_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_update_billing_plan_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_update_invoice_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_update_invoice_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['billing_update_rate_definition_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['billing_update_rate_definition_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['contact_manager_delete_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['contact_manager_delete_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT'].fields_by_name['contact_manager_kyc_event']._loaded_options = None
  _globals['_AUDITEVENT'].fields_by_name['contact_manager_kyc_event']._serialized_options = b'\030\001'
  _globals['_AUDITEVENT']._serialized_start=655
  _globals['_AUDITEVENT']._serialized_end=17194
# @@protoc_insertion_point(module_scope)
