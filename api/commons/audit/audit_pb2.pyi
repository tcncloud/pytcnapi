from api.commons.audit import agent_training_events_pb2 as _agent_training_events_pb2
from api.commons.audit import asm_events_pb2 as _asm_events_pb2
from api.commons.audit import compliance_events_pb2 as _compliance_events_pb2
from api.commons.audit import event_types_pb2 as _event_types_pb2
from api.commons.audit import events_pb2 as _events_pb2
from api.commons.audit import lms_events_pb2 as _lms_events_pb2
from api.commons.audit import omnichannel_events_pb2 as _omnichannel_events_pb2
from api.commons.audit import scorecards_events_pb2 as _scorecards_events_pb2
from api.commons.audit import tickets_events_pb2 as _tickets_events_pb2
from api.commons.audit import vana_events_pb2 as _vana_events_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditEvent(_message.Message):
    __slots__ = ["org_id", "region_id", "cluster_id", "event_time", "audit_id", "event_type", "_dummy_event", "vana_flag_event", "vana_flag_review_event", "vana_billing_report_event", "vana_flag_summary_event", "vana_phrase_correction_event", "omnichannel_create_project_event", "omnichannel_create_campaign_event", "omnichannel_daily_project_report_event", "omnichannel_daily_conversation_report_event", "omnichannel_agent_assign_conversation_event", "omnichannel_agent_unassign_conversation_event", "omnichannel_agent_reassign_conversation_event", "omnichannel_t10_event", "omnichannel_customer_text_Message_event", "omnichannel_agent_text_message_event", "omnichannel_finish_wrap_up_event", "omnichannel_begin_wrap_up_event", "omnichannel_t11_event", "omnichannel_create_conversation_event", "omnichannel_agent_suspend_event", "omnichannel_close_conversation_event", "omnichannel_manager_text_message_event", "omnichannel_update_campaign_event", "omnichannel_set_conversation_collected_data_event", "omnichannel_complete_campaign_event", "omnichannel_archive_campaign_event", "omnichannel_pause_campaign_event", "omnichannel_resume_campaign_event", "omnichannel_start_campaign_event", "omnichannel_schedule_module_event", "omnichannel_start_module_event", "omnichannel_pause_module_event", "omnichannel_resume_module_event", "omnichannel_error_module_event", "omnichannel_success_module_event", "omnichannel_fail_module_event", "omnichannel_complete_module_event", "omnichannel_archive_module_event", "omnichannel_update_module_event", "omnichannel_add_sms_message_sent_module_event", "omnichannel_module_initial_reply_event", "omnichannel_task_message_sent_event", "omnichannel_connected_inbox_poll_event", "omnichannel_connected_inbox_created_event", "omnichannel_agent_message_units_event", "omnichannel_manager_message_units_event", "omnichannel_customer_message_units_event", "omnichannel_system_message_units_event", "omnichannel_payment_link_sent_event", "omnichannel_manual_approve_task_accepted_event", "omnichannel_manual_approve_task_rejected_event", "omnichannel_manual_approve_task_timeout_event", "omnichannel_manual_approve_task_requeue_event", "asm_agent_login_event", "asm_open_voice_event", "asm_open_omni_agent_event", "asm_activate_conversation_event", "asm_deactivate_conversation_event", "asm_agent_state_changed_event", "asm_agent_logout_event", "asm_pause_event", "asm_resume_event", "asm_conversation_pulled_event", "scorecards_create_question_event", "scorecards_update_question_event", "scorecards_delete_question_event", "scorecards_create_scorecard_event", "scorecards_update_scorecard_event", "scorecards_delete_scorecard_event", "scorecards_clone_scorecard_event", "scorecards_create_evaluation_event", "scorecards_delete_evaluation_event", "scorecards_create_section_event", "scorecards_update_section_event", "scorecards_delete_section_event", "scorecards_create_category_event", "scorecards_update_category_event", "scorecards_delete_category_event", "scorecards_create_evaluation_question_event", "scorecards_update_evaluation_question_event", "scorecards_delete_evaluation_question_event", "scorecards_create_scorecard_question_event", "scorecards_update_scorecard_question_event", "scorecards_delete_scorecard_question_event", "scorecards_create_auto_evaluation_event", "scorecards_update_evaluation_event", "ticket_event", "compliance_rnd_query_event", "compliance_rnd_query_cached_event", "agent_training_create_learning_opportunity_event", "lms_pipeline_failure_event"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    _DUMMY_EVENT_FIELD_NUMBER: _ClassVar[int]
    VANA_FLAG_EVENT_FIELD_NUMBER: _ClassVar[int]
    VANA_FLAG_REVIEW_EVENT_FIELD_NUMBER: _ClassVar[int]
    VANA_BILLING_REPORT_EVENT_FIELD_NUMBER: _ClassVar[int]
    VANA_FLAG_SUMMARY_EVENT_FIELD_NUMBER: _ClassVar[int]
    VANA_PHRASE_CORRECTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CREATE_PROJECT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CREATE_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_DAILY_PROJECT_REPORT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_DAILY_CONVERSATION_REPORT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_ASSIGN_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_UNASSIGN_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_REASSIGN_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_T10_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CUSTOMER_TEXT_MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_TEXT_MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_FINISH_WRAP_UP_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_BEGIN_WRAP_UP_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_T11_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CREATE_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_SUSPEND_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CLOSE_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANAGER_TEXT_MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_UPDATE_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_SET_CONVERSATION_COLLECTED_DATA_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_COMPLETE_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_ARCHIVE_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_PAUSE_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_RESUME_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_START_CAMPAIGN_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_SCHEDULE_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_START_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_PAUSE_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_RESUME_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_ERROR_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_SUCCESS_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_FAIL_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_COMPLETE_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_ARCHIVE_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_UPDATE_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_ADD_SMS_MESSAGE_SENT_MODULE_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MODULE_INITIAL_REPLY_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_TASK_MESSAGE_SENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CONNECTED_INBOX_POLL_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CONNECTED_INBOX_CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_AGENT_MESSAGE_UNITS_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANAGER_MESSAGE_UNITS_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_CUSTOMER_MESSAGE_UNITS_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_SYSTEM_MESSAGE_UNITS_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_PAYMENT_LINK_SENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANUAL_APPROVE_TASK_ACCEPTED_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANUAL_APPROVE_TASK_REJECTED_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANUAL_APPROVE_TASK_TIMEOUT_EVENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_MANUAL_APPROVE_TASK_REQUEUE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_AGENT_LOGIN_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_OPEN_VOICE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_OPEN_OMNI_AGENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_ACTIVATE_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_DEACTIVATE_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_AGENT_STATE_CHANGED_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_AGENT_LOGOUT_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_PAUSE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_RESUME_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASM_CONVERSATION_PULLED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_SCORECARD_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_SCORECARD_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_SCORECARD_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CLONE_SCORECARD_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_EVALUATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_EVALUATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_SECTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_SECTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_SECTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_CATEGORY_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_CATEGORY_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_CATEGORY_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_EVALUATION_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_EVALUATION_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_EVALUATION_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_SCORECARD_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_SCORECARD_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_DELETE_SCORECARD_QUESTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_CREATE_AUTO_EVALUATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCORECARDS_UPDATE_EVALUATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_EVENT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_EVENT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CACHED_EVENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRAINING_CREATE_LEARNING_OPPORTUNITY_EVENT_FIELD_NUMBER: _ClassVar[int]
    LMS_PIPELINE_FAILURE_EVENT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region_id: str
    cluster_id: str
    event_time: _timestamp_pb2.Timestamp
    audit_id: str
    event_type: _event_types_pb2.EventType
    _dummy_event: _events_pb2.DummyEvent
    vana_flag_event: _vana_events_pb2.VanaFlagEvent
    vana_flag_review_event: _vana_events_pb2.VanaFlagReviewEvent
    vana_billing_report_event: _vana_events_pb2.VanaBillingReportEvent
    vana_flag_summary_event: _vana_events_pb2.VanaFlagSummaryEvent
    vana_phrase_correction_event: _vana_events_pb2.VanaPhraseCorrectionEvent
    omnichannel_create_project_event: _omnichannel_events_pb2.OmnichannelCreateProjectEvent
    omnichannel_create_campaign_event: _omnichannel_events_pb2.OmnichannelCreateCampaignEvent
    omnichannel_daily_project_report_event: _omnichannel_events_pb2.OmnichannelDailyProjectReportEvent
    omnichannel_daily_conversation_report_event: _omnichannel_events_pb2.OmnichannelDailyConversationReportEvent
    omnichannel_agent_assign_conversation_event: _omnichannel_events_pb2.OmnichannelAgentAssignConversationEvent
    omnichannel_agent_unassign_conversation_event: _omnichannel_events_pb2.OmnichannelAgentUnassignConversationEvent
    omnichannel_agent_reassign_conversation_event: _omnichannel_events_pb2.OmnichannelAgentReassignConversationEvent
    omnichannel_t10_event: _omnichannel_events_pb2.OmnichannelT10Event
    omnichannel_customer_text_Message_event: _omnichannel_events_pb2.OmnichannelCustomerTextMessageEvent
    omnichannel_agent_text_message_event: _omnichannel_events_pb2.OmnichannelAgentTextMessageEvent
    omnichannel_finish_wrap_up_event: _omnichannel_events_pb2.OmnichannelFinishWrapUpEvent
    omnichannel_begin_wrap_up_event: _omnichannel_events_pb2.OmnichannelBeginWrapUpEvent
    omnichannel_t11_event: _omnichannel_events_pb2.OmnichannelT11Event
    omnichannel_create_conversation_event: _omnichannel_events_pb2.OmnichannelCreateConversationEvent
    omnichannel_agent_suspend_event: _omnichannel_events_pb2.OmnichannelAgentSuspendEvent
    omnichannel_close_conversation_event: _omnichannel_events_pb2.OmnichannelCloseConversationEvent
    omnichannel_manager_text_message_event: _omnichannel_events_pb2.OmnichannelManagerTextMessageEvent
    omnichannel_update_campaign_event: _omnichannel_events_pb2.OmnichannelUpdateCampaignEvent
    omnichannel_set_conversation_collected_data_event: _omnichannel_events_pb2.OmnichannelSetConversationCollectedDataEvent
    omnichannel_complete_campaign_event: _omnichannel_events_pb2.OmnichannelCompleteCampaignEvent
    omnichannel_archive_campaign_event: _omnichannel_events_pb2.OmnichannelArchiveCampaignEvent
    omnichannel_pause_campaign_event: _omnichannel_events_pb2.OmnichannelPauseCampaignEvent
    omnichannel_resume_campaign_event: _omnichannel_events_pb2.OmnichannelResumeCampaignEvent
    omnichannel_start_campaign_event: _omnichannel_events_pb2.OmnichannelStartCampaignEvent
    omnichannel_schedule_module_event: _omnichannel_events_pb2.OmnichannelScheduleModuleEvent
    omnichannel_start_module_event: _omnichannel_events_pb2.OmnichannelStartModuleEvent
    omnichannel_pause_module_event: _omnichannel_events_pb2.OmnichannelPauseModuleEvent
    omnichannel_resume_module_event: _omnichannel_events_pb2.OmnichannelResumeModuleEvent
    omnichannel_error_module_event: _omnichannel_events_pb2.OmnichannelErrorModuleEvent
    omnichannel_success_module_event: _omnichannel_events_pb2.OmnichannelSuccessModuleEvent
    omnichannel_fail_module_event: _omnichannel_events_pb2.OmnichannelFailModuleEvent
    omnichannel_complete_module_event: _omnichannel_events_pb2.OmnichannelCompleteModuleEvent
    omnichannel_archive_module_event: _omnichannel_events_pb2.OmnichannelArchiveModuleEvent
    omnichannel_update_module_event: _omnichannel_events_pb2.OmnichannelUpdateModuleEvent
    omnichannel_add_sms_message_sent_module_event: _omnichannel_events_pb2.OmnichannelSmsMessageSentModuleEvent
    omnichannel_module_initial_reply_event: _omnichannel_events_pb2.OmnichannelModuleInitialReplyEvent
    omnichannel_task_message_sent_event: _omnichannel_events_pb2.OmnichannelTaskMessageSentEvent
    omnichannel_connected_inbox_poll_event: _omnichannel_events_pb2.OmnichannelConnectedInboxPollEvent
    omnichannel_connected_inbox_created_event: _omnichannel_events_pb2.OmnichannelConnectedInboxCreatedEvent
    omnichannel_agent_message_units_event: _omnichannel_events_pb2.OmnichannelAgentMessageUnitsEvent
    omnichannel_manager_message_units_event: _omnichannel_events_pb2.OmnichannelManagerMessageUnitsEvent
    omnichannel_customer_message_units_event: _omnichannel_events_pb2.OmnichannelCustomerMessageUnitsEvent
    omnichannel_system_message_units_event: _omnichannel_events_pb2.OmnichannelSystemMessageUnitsEvent
    omnichannel_payment_link_sent_event: _omnichannel_events_pb2.OmnichannelPaymentLinkSentEvent
    omnichannel_manual_approve_task_accepted_event: _omnichannel_events_pb2.OmnichannelManualApproveTaskAcceptedEvent
    omnichannel_manual_approve_task_rejected_event: _omnichannel_events_pb2.OmnichannelManualApproveTaskRejectedEvent
    omnichannel_manual_approve_task_timeout_event: _omnichannel_events_pb2.OmnichannelManualApproveTaskTimeoutEvent
    omnichannel_manual_approve_task_requeue_event: _omnichannel_events_pb2.OmnichannelManualApproveTaskRequeueEvent
    asm_agent_login_event: _asm_events_pb2.AsmAgentLoginEvent
    asm_open_voice_event: _asm_events_pb2.AsmOpenVoiceEvent
    asm_open_omni_agent_event: _asm_events_pb2.AsmOpenOmniAgentEvent
    asm_activate_conversation_event: _asm_events_pb2.AsmActivateConversationEvent
    asm_deactivate_conversation_event: _asm_events_pb2.AsmDeactivateConversationEvent
    asm_agent_state_changed_event: _asm_events_pb2.AsmAgentStateChangedEvent
    asm_agent_logout_event: _asm_events_pb2.AsmAgentLogoutEvent
    asm_pause_event: _asm_events_pb2.AsmPauseEvent
    asm_resume_event: _asm_events_pb2.AsmResumeEvent
    asm_conversation_pulled_event: _asm_events_pb2.AsmConversationPulledEvent
    scorecards_create_question_event: _scorecards_events_pb2.ScorecardsCreateQuestionEvent
    scorecards_update_question_event: _scorecards_events_pb2.ScorecardsUpdateQuestionEvent
    scorecards_delete_question_event: _scorecards_events_pb2.ScorecardsDeleteQuestionEvent
    scorecards_create_scorecard_event: _scorecards_events_pb2.ScorecardsCreateScorecardEvent
    scorecards_update_scorecard_event: _scorecards_events_pb2.ScorecardsUpdateScorecardEvent
    scorecards_delete_scorecard_event: _scorecards_events_pb2.ScorecardsDeleteScorecardEvent
    scorecards_clone_scorecard_event: _scorecards_events_pb2.ScorecardsCloneScorecardEvent
    scorecards_create_evaluation_event: _scorecards_events_pb2.ScorecardsCreateEvaluationEvent
    scorecards_delete_evaluation_event: _scorecards_events_pb2.ScorecardsDeleteEvaluationEvent
    scorecards_create_section_event: _scorecards_events_pb2.ScorecardsCreateSectionEvent
    scorecards_update_section_event: _scorecards_events_pb2.ScorecardsUpdateSectionEvent
    scorecards_delete_section_event: _scorecards_events_pb2.ScorecardsDeleteSectionEvent
    scorecards_create_category_event: _scorecards_events_pb2.ScorecardsCreateCategoryEvent
    scorecards_update_category_event: _scorecards_events_pb2.ScorecardsUpdateCategoryEvent
    scorecards_delete_category_event: _scorecards_events_pb2.ScorecardsDeleteCategoryEvent
    scorecards_create_evaluation_question_event: _scorecards_events_pb2.ScorecardsCreateEvaluationQuestionEvent
    scorecards_update_evaluation_question_event: _scorecards_events_pb2.ScorecardsUpdateEvaluationQuestionEvent
    scorecards_delete_evaluation_question_event: _scorecards_events_pb2.ScorecardsDeleteEvaluationQuestionEvent
    scorecards_create_scorecard_question_event: _scorecards_events_pb2.ScorecardsCreateScorecardQuestionEvent
    scorecards_update_scorecard_question_event: _scorecards_events_pb2.ScorecardsUpdateScorecardQuestionEvent
    scorecards_delete_scorecard_question_event: _scorecards_events_pb2.ScorecardsDeleteScorecardQuestionEvent
    scorecards_create_auto_evaluation_event: _scorecards_events_pb2.ScorecardsCreateAutoEvaluationEvent
    scorecards_update_evaluation_event: _scorecards_events_pb2.ScorecardsUpdateEvaluationEvent
    ticket_event: _tickets_events_pb2.TicketEvent
    compliance_rnd_query_event: _compliance_events_pb2.ComplianceRndQueryEvent
    compliance_rnd_query_cached_event: _compliance_events_pb2.ComplianceRndQueryEvent
    agent_training_create_learning_opportunity_event: _agent_training_events_pb2.AgentTrainingCreateLearningOpportunityEvent
    lms_pipeline_failure_event: _lms_events_pb2.LMSPipelineFailureEvent
    def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., audit_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., _dummy_event: _Optional[_Union[_events_pb2.DummyEvent, _Mapping]] = ..., vana_flag_event: _Optional[_Union[_vana_events_pb2.VanaFlagEvent, _Mapping]] = ..., vana_flag_review_event: _Optional[_Union[_vana_events_pb2.VanaFlagReviewEvent, _Mapping]] = ..., vana_billing_report_event: _Optional[_Union[_vana_events_pb2.VanaBillingReportEvent, _Mapping]] = ..., vana_flag_summary_event: _Optional[_Union[_vana_events_pb2.VanaFlagSummaryEvent, _Mapping]] = ..., vana_phrase_correction_event: _Optional[_Union[_vana_events_pb2.VanaPhraseCorrectionEvent, _Mapping]] = ..., omnichannel_create_project_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCreateProjectEvent, _Mapping]] = ..., omnichannel_create_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCreateCampaignEvent, _Mapping]] = ..., omnichannel_daily_project_report_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelDailyProjectReportEvent, _Mapping]] = ..., omnichannel_daily_conversation_report_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelDailyConversationReportEvent, _Mapping]] = ..., omnichannel_agent_assign_conversation_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentAssignConversationEvent, _Mapping]] = ..., omnichannel_agent_unassign_conversation_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentUnassignConversationEvent, _Mapping]] = ..., omnichannel_agent_reassign_conversation_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentReassignConversationEvent, _Mapping]] = ..., omnichannel_t10_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelT10Event, _Mapping]] = ..., omnichannel_customer_text_Message_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCustomerTextMessageEvent, _Mapping]] = ..., omnichannel_agent_text_message_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentTextMessageEvent, _Mapping]] = ..., omnichannel_finish_wrap_up_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelFinishWrapUpEvent, _Mapping]] = ..., omnichannel_begin_wrap_up_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelBeginWrapUpEvent, _Mapping]] = ..., omnichannel_t11_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelT11Event, _Mapping]] = ..., omnichannel_create_conversation_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCreateConversationEvent, _Mapping]] = ..., omnichannel_agent_suspend_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentSuspendEvent, _Mapping]] = ..., omnichannel_close_conversation_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCloseConversationEvent, _Mapping]] = ..., omnichannel_manager_text_message_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManagerTextMessageEvent, _Mapping]] = ..., omnichannel_update_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelUpdateCampaignEvent, _Mapping]] = ..., omnichannel_set_conversation_collected_data_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelSetConversationCollectedDataEvent, _Mapping]] = ..., omnichannel_complete_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCompleteCampaignEvent, _Mapping]] = ..., omnichannel_archive_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelArchiveCampaignEvent, _Mapping]] = ..., omnichannel_pause_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelPauseCampaignEvent, _Mapping]] = ..., omnichannel_resume_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelResumeCampaignEvent, _Mapping]] = ..., omnichannel_start_campaign_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelStartCampaignEvent, _Mapping]] = ..., omnichannel_schedule_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelScheduleModuleEvent, _Mapping]] = ..., omnichannel_start_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelStartModuleEvent, _Mapping]] = ..., omnichannel_pause_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelPauseModuleEvent, _Mapping]] = ..., omnichannel_resume_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelResumeModuleEvent, _Mapping]] = ..., omnichannel_error_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelErrorModuleEvent, _Mapping]] = ..., omnichannel_success_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelSuccessModuleEvent, _Mapping]] = ..., omnichannel_fail_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelFailModuleEvent, _Mapping]] = ..., omnichannel_complete_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCompleteModuleEvent, _Mapping]] = ..., omnichannel_archive_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelArchiveModuleEvent, _Mapping]] = ..., omnichannel_update_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelUpdateModuleEvent, _Mapping]] = ..., omnichannel_add_sms_message_sent_module_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelSmsMessageSentModuleEvent, _Mapping]] = ..., omnichannel_module_initial_reply_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelModuleInitialReplyEvent, _Mapping]] = ..., omnichannel_task_message_sent_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelTaskMessageSentEvent, _Mapping]] = ..., omnichannel_connected_inbox_poll_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelConnectedInboxPollEvent, _Mapping]] = ..., omnichannel_connected_inbox_created_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelConnectedInboxCreatedEvent, _Mapping]] = ..., omnichannel_agent_message_units_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelAgentMessageUnitsEvent, _Mapping]] = ..., omnichannel_manager_message_units_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManagerMessageUnitsEvent, _Mapping]] = ..., omnichannel_customer_message_units_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelCustomerMessageUnitsEvent, _Mapping]] = ..., omnichannel_system_message_units_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelSystemMessageUnitsEvent, _Mapping]] = ..., omnichannel_payment_link_sent_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelPaymentLinkSentEvent, _Mapping]] = ..., omnichannel_manual_approve_task_accepted_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManualApproveTaskAcceptedEvent, _Mapping]] = ..., omnichannel_manual_approve_task_rejected_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManualApproveTaskRejectedEvent, _Mapping]] = ..., omnichannel_manual_approve_task_timeout_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManualApproveTaskTimeoutEvent, _Mapping]] = ..., omnichannel_manual_approve_task_requeue_event: _Optional[_Union[_omnichannel_events_pb2.OmnichannelManualApproveTaskRequeueEvent, _Mapping]] = ..., asm_agent_login_event: _Optional[_Union[_asm_events_pb2.AsmAgentLoginEvent, _Mapping]] = ..., asm_open_voice_event: _Optional[_Union[_asm_events_pb2.AsmOpenVoiceEvent, _Mapping]] = ..., asm_open_omni_agent_event: _Optional[_Union[_asm_events_pb2.AsmOpenOmniAgentEvent, _Mapping]] = ..., asm_activate_conversation_event: _Optional[_Union[_asm_events_pb2.AsmActivateConversationEvent, _Mapping]] = ..., asm_deactivate_conversation_event: _Optional[_Union[_asm_events_pb2.AsmDeactivateConversationEvent, _Mapping]] = ..., asm_agent_state_changed_event: _Optional[_Union[_asm_events_pb2.AsmAgentStateChangedEvent, _Mapping]] = ..., asm_agent_logout_event: _Optional[_Union[_asm_events_pb2.AsmAgentLogoutEvent, _Mapping]] = ..., asm_pause_event: _Optional[_Union[_asm_events_pb2.AsmPauseEvent, _Mapping]] = ..., asm_resume_event: _Optional[_Union[_asm_events_pb2.AsmResumeEvent, _Mapping]] = ..., asm_conversation_pulled_event: _Optional[_Union[_asm_events_pb2.AsmConversationPulledEvent, _Mapping]] = ..., scorecards_create_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateQuestionEvent, _Mapping]] = ..., scorecards_update_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateQuestionEvent, _Mapping]] = ..., scorecards_delete_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteQuestionEvent, _Mapping]] = ..., scorecards_create_scorecard_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateScorecardEvent, _Mapping]] = ..., scorecards_update_scorecard_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateScorecardEvent, _Mapping]] = ..., scorecards_delete_scorecard_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteScorecardEvent, _Mapping]] = ..., scorecards_clone_scorecard_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCloneScorecardEvent, _Mapping]] = ..., scorecards_create_evaluation_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateEvaluationEvent, _Mapping]] = ..., scorecards_delete_evaluation_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteEvaluationEvent, _Mapping]] = ..., scorecards_create_section_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateSectionEvent, _Mapping]] = ..., scorecards_update_section_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateSectionEvent, _Mapping]] = ..., scorecards_delete_section_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteSectionEvent, _Mapping]] = ..., scorecards_create_category_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateCategoryEvent, _Mapping]] = ..., scorecards_update_category_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateCategoryEvent, _Mapping]] = ..., scorecards_delete_category_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteCategoryEvent, _Mapping]] = ..., scorecards_create_evaluation_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateEvaluationQuestionEvent, _Mapping]] = ..., scorecards_update_evaluation_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateEvaluationQuestionEvent, _Mapping]] = ..., scorecards_delete_evaluation_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteEvaluationQuestionEvent, _Mapping]] = ..., scorecards_create_scorecard_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateScorecardQuestionEvent, _Mapping]] = ..., scorecards_update_scorecard_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateScorecardQuestionEvent, _Mapping]] = ..., scorecards_delete_scorecard_question_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsDeleteScorecardQuestionEvent, _Mapping]] = ..., scorecards_create_auto_evaluation_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsCreateAutoEvaluationEvent, _Mapping]] = ..., scorecards_update_evaluation_event: _Optional[_Union[_scorecards_events_pb2.ScorecardsUpdateEvaluationEvent, _Mapping]] = ..., ticket_event: _Optional[_Union[_tickets_events_pb2.TicketEvent, _Mapping]] = ..., compliance_rnd_query_event: _Optional[_Union[_compliance_events_pb2.ComplianceRndQueryEvent, _Mapping]] = ..., compliance_rnd_query_cached_event: _Optional[_Union[_compliance_events_pb2.ComplianceRndQueryEvent, _Mapping]] = ..., agent_training_create_learning_opportunity_event: _Optional[_Union[_agent_training_events_pb2.AgentTrainingCreateLearningOpportunityEvent, _Mapping]] = ..., lms_pipeline_failure_event: _Optional[_Union[_lms_events_pb2.LMSPipelineFailureEvent, _Mapping]] = ...) -> None: ...
