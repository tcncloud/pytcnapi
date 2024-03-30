# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/asm/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import asm_pb2 as api_dot_commons_dot_asm__pb2
from api.commons.auth import user_pb2 as api_dot_commons_dot_auth_dot_user__pb2
from api.commons import event_pb2 as api_dot_commons_dot_event__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/v1alpha1/asm/service.proto\x12\x10\x61pi.v1alpha1.asm\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x15\x61pi/commons/asm.proto\x1a\x1b\x61pi/commons/auth/user.proto\x1a\x17\x61pi/commons/event.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x02\n\x10\x43reateSessionReq\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x46\n\x06skills\x18\x02 \x03(\x0b\x32..api.v1alpha1.asm.CreateSessionReq.SkillsEntryR\x06skills\x12G\n\x0fsubsession_type\x18\x03 \x01(\x0e\x32\x1e.api.commons.AsmSubsessionTypeR\x0esubsessionType\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\xba\x01\n\x10\x43reateSessionRes\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12*\n\x11voice_session_sid\x18\x02 \x01(\x03R\x0fvoiceSessionSid\x12R\n\x12voice_registration\x18\x03 \x01(\x0b\x32#.api.v1alpha1.asm.VoiceRegistrationR\x11voiceRegistration\"\xe4\x01\n\x11VoiceRegistration\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\x12\x19\n\x08\x64ial_url\x18\x04 \x01(\tR\x07\x64ialUrl\x12\x1d\n\npstn_phone\x18\x05 \x01(\tR\tpstnPhone\x12*\n\x11\x64\x65\x66\x61ult_time_zone\x18\x06 \x01(\tR\x0f\x64\x65\x66\x61ultTimeZone\x12\x31\n\x14\x65xpiration_timestamp\x18\x07 \x01(\x03R\x13\x65xpirationTimestamp\"\\\n\x13StreamAgentStateReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12\x1d\n\nkeep_alive\x18\x02 \x01(\x08R\tkeepAlive\"\x1c\n\x1aManagerStreamAgentStateReq\"\xff\x02\n\x0cGetStatusReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12,\n\x12perform_keep_alive\x18\x02 \x01(\x08R\x10performKeepAlive\x12\x37\n\x18perform_get_queued_calls\x18\x03 \x01(\x08R\x15performGetQueuedCalls\x12.\n\x13perform_get_message\x18\x04 \x01(\x08R\x11performGetMessage\x12:\n\x19minimum_message_timestamp\x18\x05 \x01(\x03R\x17minimumMessageTimestamp\x12\x16\n\x06skills\x18\x06 \x03(\tR\x06skills\x12*\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x12.api.commons.EventR\x06\x65vents\x12\x30\n\x14\x61gent_pbx_extensions\x18\x08 \x03(\tR\x12\x61gentPbxExtensions\"P\n\x0cGetStatusRes\x12@\n\x0cvoice_status\x18\x01 \x01(\x0b\x32\x1d.api.v1alpha1.asm.VoiceStatusR\x0bvoiceStatus\"\xf1\x06\n\x0bVoiceStatus\x12\x16\n\x06status\x18\x02 \x01(\x03R\x06status\x12>\n\x0bstatus_desc\x18\x03 \x01(\x0e\x32\x1d.api.commons.AgentStatus.EnumR\nstatusDesc\x12\x16\n\x06paused\x18\x04 \x01(\x08R\x06paused\x12\x14\n\x05queue\x18\x05 \x01(\tR\x05queue\x12,\n\x12\x63urrent_session_id\x18\x06 \x01(\x03R\x10\x63urrentSessionId\x12,\n\x12last_status_change\x18\x07 \x01(\x03R\x10lastStatusChange\x12\x1e\n\nmonitoring\x18\x08 \x01(\x08R\nmonitoring\x12\x1f\n\x0b\x63\x61lls_count\x18\t \x01(\x03R\ncallsCount\x12\"\n\rlast_sip_code\x18\n \x01(\x03R\x0blastSipCode\x12\x34\n\x17\x61gent_peer_is_lost_call\x18\x0b \x01(\x08R\x13\x61gentPeerIsLostCall\x12\x1a\n\x08\x64isabled\x18\x0c \x01(\x08R\x08\x64isabled\x12\x30\n\x14keep_alive_succeeded\x18\r \x01(\x08R\x12keepAliveSucceeded\x12\x18\n\x07message\x18\x0e \x01(\tR\x07message\x12+\n\x11message_timestamp\x18\x0f \x01(\x03R\x10messageTimestamp\x12@\n\x0cqueued_calls\x18\x10 \x01(\x0b\x32\x1d.api.v1alpha1.asm.QueuedCallsR\x0bqueuedCalls\x12\x30\n\x14\x63\x61ller_was_suspended\x18\x11 \x01(\x08R\x12\x63\x61llerWasSuspended\x12\x46\n\x10transfer_members\x18\x12 \x03(\x0b\x32\x1b.api.commons.TransferMemberR\x0ftransferMembers\x12-\n\x05\x61lert\x18\x13 \x01(\x0b\x32\x17.api.commons.AgentAlertR\x05\x61lert\x12?\n\x1d\x61gent_peer_is_direct_to_agent\x18\x14 \x01(\x08R\x18\x61gentPeerIsDirectToAgent\x12$\n\x0e\x61gent_is_muted\x18\x15 \x01(\x08R\x0c\x61gentIsMuted\"\xbd\x05\n\x0bQueuedCalls\x12X\n\x11\x61gent_queue_calls\x18\x10 \x03(\x0b\x32,.api.v1alpha1.asm.QueuedCalls.QueuedCallDataR\x0f\x61gentQueueCalls\x12P\n\ron_hold_calls\x18\x11 \x03(\x0b\x32,.api.v1alpha1.asm.QueuedCalls.QueuedCallDataR\x0bonHoldCalls\x12I\n\thqm_calls\x18\x12 \x03(\x0b\x32,.api.v1alpha1.asm.QueuedCalls.QueuedCallDataR\x08hqmCalls\x1a\xb6\x03\n\x0eQueuedCallData\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x03 \x01(\tR\x08\x63\x61llerId\x12\x37\n\tcall_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x39\n\nstart_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartDate\x12\x37\n\thold_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08holdDate\x12\x16\n\x06skills\x18\x07 \x03(\tR\x06skills\x12%\n\x0e\x61gent_specific\x18\x08 \x01(\x08R\ragentSpecific\x12]\n\x18queued_notification_type\x18\t \x01(\x0e\x32#.api.commons.QueuedNotificationTypeR\x16queuedNotificationType\"O\n\rEndSessionReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\"\x0f\n\rEndSessionRes\"\x16\n\x14GetCurrentSessionReq\"\x85\x02\n\nAsmSession\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12\x46\n\x11\x61sm_session_start\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x61smSessionStart\x12\x42\n\x0f\x61sm_session_end\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rasmSessionEnd\x12\x43\n\rvoice_session\x18\x06 \x01(\x0b\x32\x1e.api.v1alpha1.asm.VoiceSessionR\x0cvoiceSession\"\xce\x01\n\x0cVoiceSession\x12*\n\x11voice_session_sid\x18\x01 \x01(\x03R\x0fvoiceSessionSid\x12J\n\x13voice_session_start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11voiceSessionStart\x12\x46\n\x11voice_session_end\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0fvoiceSessionEnd\"\xac\x02\n\x13SwitchSubsessionReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12I\n\x06skills\x18\x03 \x03(\x0b\x32\x31.api.v1alpha1.asm.SwitchSubsessionReq.SkillsEntryR\x06skills\x12\x41\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x1e.api.commons.AsmSubsessionTypeR\x0b\x63hannelType\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\x95\x01\n\x13SwitchSubsessionRes\x12*\n\x11voice_session_sid\x18\x01 \x01(\x03R\x0fvoiceSessionSid\x12R\n\x12voice_registration\x18\x02 \x01(\x0b\x32#.api.v1alpha1.asm.VoiceRegistrationR\x11voiceRegistration\"\xd6\x08\n\x0c\x43onversation\x12-\n\x10\x63onversation_sid\x18\x06 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12V\n\x19\x63onversation_created_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x17\x63onversationCreatedTime\x12W\n\x1a\x61ssigned_last_updated_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x17\x61ssignedLastUpdatedTime\x12P\n\x13\x63onversation_status\x18\t \x01(\x0e\x32\x1f.api.commons.ConversationStatusR\x12\x63onversationStatus\x12;\n\x0c\x63hannel_type\x18\n \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12Q\n\rcustomer_info\x18\x0b \x01(\x0b\x32,.api.commons.ConversationCustomerInformationR\x0c\x63ustomerInfo\x12\x46\n\x11last_message_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0flastMessageTime\x12<\n\x06skills\x18\r \x01(\x0b\x32$.api.v1alpha1.asm.ConversationSkillsR\x06skills\x12[\n\x11\x61ssignment_status\x18\x0e \x01(\x0e\x32..api.commons.AgentConversationAssignmentStatusR\x10\x61ssignmentStatus\x12U\n\x0f\x61ssignment_type\x18\x0f \x01(\x0e\x32,.api.commons.AgentConversationAssignmentTypeR\x0e\x61ssignmentType\x12;\n\x0csla_timeouts\x18\x10 \x01(\x0b\x32\x18.api.commons.SLATimeoutsR\x0bslaTimeouts\x12\x66\n\x1b\x63onversation_collected_data\x18\x11 \x01(\x0b\x32&.api.commons.ConversationCollectedDataR\x19\x63onversationCollectedData\x12Q\n\x17last_message_group_time\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x14lastMessageGroupTime\x12R\n\x17last_message_group_type\x18\x13 \x01(\x0e\x32\x1b.api.commons.OmniSenderTypeR\x14lastMessageGroupType\"\x99\x01\n\x12\x43onversationSkills\x12H\n\x06skills\x18\x01 \x03(\x0b\x32\x30.api.v1alpha1.asm.ConversationSkills.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"\x8c\x02\n\x18\x41ssignNewConversationReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12N\n\x06skills\x18\x02 \x03(\x0b\x32\x36.api.v1alpha1.asm.AssignNewConversationReq.SkillsEntryR\x06skills\x12=\n\rchannel_types\x18\x03 \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x0c\x63hannelTypes\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\x81\x01\n\x18\x41ssignNewConversationRes\x12\x42\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.asm.ConversationR\x0c\x63onversation\x12!\n\x0creference_id\x18\x02 \x01(\tR\x0breferenceId\"\x0f\n\rListAgentsReq\"H\n\rListAgentsRes\x12\x37\n\x06\x61gents\x18\x01 \x03(\x0b\x32\x1f.api.commons.DashboardAgentInfoR\x06\x61gents\"\xe4\x02\n\x1fSetConversationCollectedDataReq\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12k\n\x0e\x63ollected_data\x18\x03 \x03(\x0b\x32\x44.api.v1alpha1.asm.SetConversationCollectedDataReq.CollectedDataEntryR\rcollectedData\x12&\n\x0f\x61sm_session_sid\x18\x04 \x01(\x03R\rasmSessionSid\x1a@\n\x12\x43ollectedDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"!\n\x1fSetConversationCollectedDataRes\"\xe2\x02\n\x14ListConversationsReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12R\n\x12\x61uthenticated_user\x18\x02 \x01(\x0b\x32#.api.commons.auth.AuthenticatedUserR\x11\x61uthenticatedUser\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x12;\n\x08statuses\x18\x04 \x03(\x0e\x32\x1f.api.commons.ConversationStatusR\x08statuses\x12\x39\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\x12=\n\rchannel_types\x18\x06 \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x0c\x63hannelTypes\"\x83\x01\n\x14ListConversationsRes\x12\x43\n\rconversations\x18\x01 \x03(\x0b\x32\x1d.api.commons.OmniConversationR\rconversations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x82\x02\n\x13GetQueuesDetailsReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12=\n\rchannel_types\x18\x02 \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x0c\x63hannelTypes\x12I\n\x06skills\x18\x03 \x03(\x0b\x32\x31.api.v1alpha1.asm.GetQueuesDetailsReq.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"f\n\rPushEventsReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12-\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x15.api.commons.AsmEventR\x06\x65vents\"\x0f\n\rPushEventsRes\"\xdf\x01\n\x0e\x45nableVoiceReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12\x44\n\x06skills\x18\x03 \x03(\x0b\x32,.api.v1alpha1.asm.EnableVoiceReq.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\x90\x01\n\x0e\x45nableVoiceRes\x12*\n\x11voice_session_sid\x18\x01 \x01(\x03R\x0fvoiceSessionSid\x12R\n\x12voice_registration\x18\x02 \x01(\x0b\x32#.api.v1alpha1.asm.VoiceRegistrationR\x11voiceRegistration\"\xe1\x01\n\x0f\x44isableVoiceReq\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12\x45\n\x06skills\x18\x03 \x03(\x0b\x32-.api.v1alpha1.asm.DisableVoiceReq.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\x11\n\x0f\x44isableVoiceRes2\xc1\x0c\n\x06\x41smApi\x12\x91\x01\n\rCreateSession\x12\".api.v1alpha1.asm.CreateSessionReq\x1a\".api.v1alpha1.asm.CreateSessionRes\"8\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/asm/asmapi/createsession:\x01*\x12\x81\x01\n\tGetStatus\x12\x1e.api.v1alpha1.asm.GetStatusReq\x1a\x1e.api.v1alpha1.asm.GetStatusRes\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v1alpha1/asm/asmapi/getstatus:\x01*\x12\x85\x01\n\nEndSession\x12\x1f.api.v1alpha1.asm.EndSessionReq\x1a\x1f.api.v1alpha1.asm.EndSessionRes\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/asm/asmapi/endsession:\x01*\x12\x97\x01\n\x11GetCurrentSession\x12&.api.v1alpha1.asm.GetCurrentSessionReq\x1a\x1c.api.v1alpha1.asm.AsmSession\"<\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/asm/asmapi/getcurrentsession:\x01*\x12\x9d\x01\n\x10SwitchSubsession\x12%.api.v1alpha1.asm.SwitchSubsessionReq\x1a%.api.v1alpha1.asm.SwitchSubsessionRes\";\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/asm/asmapi/switchsubsession:\x01*\x12\xa4\x01\n\x11ListConversations\x12&.api.v1alpha1.asm.ListConversationsReq\x1a&.api.v1alpha1.asm.ListConversationsRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/asm/asmapi/listconversations:\x01*\x12\xb4\x01\n\x15\x41ssignNewConversation\x12*.api.v1alpha1.asm.AssignNewConversationReq\x1a*.api.v1alpha1.asm.AssignNewConversationRes\"C\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/asm/asmapi/assignnewconversation:\x01*\x12\x88\x01\n\nListAgents\x12\x1f.api.v1alpha1.asm.ListAgentsReq\x1a\x1f.api.v1alpha1.asm.ListAgentsRes\"8\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/asm/asmapi/listagents:\x01*\x12\xd5\x01\n\x1cSetConversationCollectedData\x12\x31.api.v1alpha1.asm.SetConversationCollectedDataReq\x1a\x31.api.v1alpha1.asm.SetConversationCollectedDataRes\"O\xba\xb8\x91\x02\n\n\x03\x08\xac\x02\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02:\"5/api/v1alpha1/asm/asmapi/setconversationcollecteddata:\x01*\x12\x9b\x01\n\x10GetQueuesDetails\x12%.api.v1alpha1.asm.GetQueuesDetailsReq\x1a .api.commons.GetQueuesDetailsRes\">\xba\xb8\x91\x02\x05\n\x03\x08\xac\x02\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/asm/asmapi/getqueuesdetails:\x01*B\x86\x01\n\x14\x63om.api.v1alpha1.asmB\x0cServiceProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x10\x41pi.V1alpha1.Asm\xca\x02\x10\x41pi\\V1alpha1\\Asm\xe2\x02\x1c\x41pi\\V1alpha1\\Asm\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Asmb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.asm.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.asmB\014ServiceProtoP\001\242\002\003AVA\252\002\020Api.V1alpha1.Asm\312\002\020Api\\V1alpha1\\Asm\342\002\034Api\\V1alpha1\\Asm\\GPBMetadata\352\002\022Api::V1alpha1::Asm'
  _globals['_CREATESESSIONREQ_SKILLSENTRY']._loaded_options = None
  _globals['_CREATESESSIONREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_SWITCHSUBSESSIONREQ_SKILLSENTRY']._loaded_options = None
  _globals['_SWITCHSUBSESSIONREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_CONVERSATION'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_CONVERSATION'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_CONVERSATIONSKILLS_SKILLSENTRY']._loaded_options = None
  _globals['_CONVERSATIONSKILLS_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_ASSIGNNEWCONVERSATIONREQ_SKILLSENTRY']._loaded_options = None
  _globals['_ASSIGNNEWCONVERSATIONREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ_COLLECTEDDATAENTRY']._loaded_options = None
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ_COLLECTEDDATAENTRY']._serialized_options = b'8\001'
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_GETQUEUESDETAILSREQ_SKILLSENTRY']._loaded_options = None
  _globals['_GETQUEUESDETAILSREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_ENABLEVOICEREQ_SKILLSENTRY']._loaded_options = None
  _globals['_ENABLEVOICEREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_DISABLEVOICEREQ_SKILLSENTRY']._loaded_options = None
  _globals['_DISABLEVOICEREQ_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_ASMAPI'].methods_by_name['CreateSession']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['CreateSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002+\"&/api/v1alpha1/asm/asmapi/createsession:\001*'
  _globals['_ASMAPI'].methods_by_name['GetStatus']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['GetStatus']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v1alpha1/asm/asmapi/getstatus:\001*'
  _globals['_ASMAPI'].methods_by_name['EndSession']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['EndSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v1alpha1/asm/asmapi/endsession:\001*'
  _globals['_ASMAPI'].methods_by_name['GetCurrentSession']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['GetCurrentSession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002/\"*/api/v1alpha1/asm/asmapi/getcurrentsession:\001*'
  _globals['_ASMAPI'].methods_by_name['SwitchSubsession']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['SwitchSubsession']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002.\")/api/v1alpha1/asm/asmapi/switchsubsession:\001*'
  _globals['_ASMAPI'].methods_by_name['ListConversations']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['ListConversations']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002/\"*/api/v1alpha1/asm/asmapi/listconversations:\001*'
  _globals['_ASMAPI'].methods_by_name['AssignNewConversation']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['AssignNewConversation']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\0023\"./api/v1alpha1/asm/asmapi/assignnewconversation:\001*'
  _globals['_ASMAPI'].methods_by_name['ListAgents']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['ListAgents']._serialized_options = b'\272\270\221\002\005\n\003\010\260\t\202\323\344\223\002(\"#/api/v1alpha1/asm/asmapi/listagents:\001*'
  _globals['_ASMAPI'].methods_by_name['SetConversationCollectedData']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['SetConversationCollectedData']._serialized_options = b'\272\270\221\002\n\n\003\010\254\002\n\003\010\260\t\202\323\344\223\002:\"5/api/v1alpha1/asm/asmapi/setconversationcollecteddata:\001*'
  _globals['_ASMAPI'].methods_by_name['GetQueuesDetails']._loaded_options = None
  _globals['_ASMAPI'].methods_by_name['GetQueuesDetails']._serialized_options = b'\272\270\221\002\005\n\003\010\254\002\202\323\344\223\002.\")/api/v1alpha1/asm/asmapi/getqueuesdetails:\001*'
  _globals['_CREATESESSIONREQ']._serialized_start=306
  _globals['_CREATESESSIONREQ']._serialized_end=566
  _globals['_CREATESESSIONREQ_SKILLSENTRY']._serialized_start=509
  _globals['_CREATESESSIONREQ_SKILLSENTRY']._serialized_end=566
  _globals['_CREATESESSIONRES']._serialized_start=569
  _globals['_CREATESESSIONRES']._serialized_end=755
  _globals['_VOICEREGISTRATION']._serialized_start=758
  _globals['_VOICEREGISTRATION']._serialized_end=986
  _globals['_STREAMAGENTSTATEREQ']._serialized_start=988
  _globals['_STREAMAGENTSTATEREQ']._serialized_end=1080
  _globals['_MANAGERSTREAMAGENTSTATEREQ']._serialized_start=1082
  _globals['_MANAGERSTREAMAGENTSTATEREQ']._serialized_end=1110
  _globals['_GETSTATUSREQ']._serialized_start=1113
  _globals['_GETSTATUSREQ']._serialized_end=1496
  _globals['_GETSTATUSRES']._serialized_start=1498
  _globals['_GETSTATUSRES']._serialized_end=1578
  _globals['_VOICESTATUS']._serialized_start=1581
  _globals['_VOICESTATUS']._serialized_end=2462
  _globals['_QUEUEDCALLS']._serialized_start=2465
  _globals['_QUEUEDCALLS']._serialized_end=3166
  _globals['_QUEUEDCALLS_QUEUEDCALLDATA']._serialized_start=2728
  _globals['_QUEUEDCALLS_QUEUEDCALLDATA']._serialized_end=3166
  _globals['_ENDSESSIONREQ']._serialized_start=3168
  _globals['_ENDSESSIONREQ']._serialized_end=3247
  _globals['_ENDSESSIONRES']._serialized_start=3249
  _globals['_ENDSESSIONRES']._serialized_end=3264
  _globals['_GETCURRENTSESSIONREQ']._serialized_start=3266
  _globals['_GETCURRENTSESSIONREQ']._serialized_end=3288
  _globals['_ASMSESSION']._serialized_start=3291
  _globals['_ASMSESSION']._serialized_end=3552
  _globals['_VOICESESSION']._serialized_start=3555
  _globals['_VOICESESSION']._serialized_end=3761
  _globals['_SWITCHSUBSESSIONREQ']._serialized_start=3764
  _globals['_SWITCHSUBSESSIONREQ']._serialized_end=4064
  _globals['_SWITCHSUBSESSIONREQ_SKILLSENTRY']._serialized_start=509
  _globals['_SWITCHSUBSESSIONREQ_SKILLSENTRY']._serialized_end=566
  _globals['_SWITCHSUBSESSIONRES']._serialized_start=4067
  _globals['_SWITCHSUBSESSIONRES']._serialized_end=4216
  _globals['_CONVERSATION']._serialized_start=4219
  _globals['_CONVERSATION']._serialized_end=5329
  _globals['_CONVERSATIONSKILLS']._serialized_start=5332
  _globals['_CONVERSATIONSKILLS']._serialized_end=5485
  _globals['_CONVERSATIONSKILLS_SKILLSENTRY']._serialized_start=5428
  _globals['_CONVERSATIONSKILLS_SKILLSENTRY']._serialized_end=5485
  _globals['_ASSIGNNEWCONVERSATIONREQ']._serialized_start=5488
  _globals['_ASSIGNNEWCONVERSATIONREQ']._serialized_end=5756
  _globals['_ASSIGNNEWCONVERSATIONREQ_SKILLSENTRY']._serialized_start=509
  _globals['_ASSIGNNEWCONVERSATIONREQ_SKILLSENTRY']._serialized_end=566
  _globals['_ASSIGNNEWCONVERSATIONRES']._serialized_start=5759
  _globals['_ASSIGNNEWCONVERSATIONRES']._serialized_end=5888
  _globals['_LISTAGENTSREQ']._serialized_start=5890
  _globals['_LISTAGENTSREQ']._serialized_end=5905
  _globals['_LISTAGENTSRES']._serialized_start=5907
  _globals['_LISTAGENTSRES']._serialized_end=5979
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ']._serialized_start=5982
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ']._serialized_end=6338
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ_COLLECTEDDATAENTRY']._serialized_start=6274
  _globals['_SETCONVERSATIONCOLLECTEDDATAREQ_COLLECTEDDATAENTRY']._serialized_end=6338
  _globals['_SETCONVERSATIONCOLLECTEDDATARES']._serialized_start=6340
  _globals['_SETCONVERSATIONCOLLECTEDDATARES']._serialized_end=6373
  _globals['_LISTCONVERSATIONSREQ']._serialized_start=6376
  _globals['_LISTCONVERSATIONSREQ']._serialized_end=6730
  _globals['_LISTCONVERSATIONSRES']._serialized_start=6733
  _globals['_LISTCONVERSATIONSRES']._serialized_end=6864
  _globals['_GETQUEUESDETAILSREQ']._serialized_start=6867
  _globals['_GETQUEUESDETAILSREQ']._serialized_end=7125
  _globals['_GETQUEUESDETAILSREQ_SKILLSENTRY']._serialized_start=509
  _globals['_GETQUEUESDETAILSREQ_SKILLSENTRY']._serialized_end=566
  _globals['_PUSHEVENTSREQ']._serialized_start=7127
  _globals['_PUSHEVENTSREQ']._serialized_end=7229
  _globals['_PUSHEVENTSRES']._serialized_start=7231
  _globals['_PUSHEVENTSRES']._serialized_end=7246
  _globals['_ENABLEVOICEREQ']._serialized_start=7249
  _globals['_ENABLEVOICEREQ']._serialized_end=7472
  _globals['_ENABLEVOICEREQ_SKILLSENTRY']._serialized_start=509
  _globals['_ENABLEVOICEREQ_SKILLSENTRY']._serialized_end=566
  _globals['_ENABLEVOICERES']._serialized_start=7475
  _globals['_ENABLEVOICERES']._serialized_end=7619
  _globals['_DISABLEVOICEREQ']._serialized_start=7622
  _globals['_DISABLEVOICEREQ']._serialized_end=7847
  _globals['_DISABLEVOICEREQ_SKILLSENTRY']._serialized_start=509
  _globals['_DISABLEVOICEREQ_SKILLSENTRY']._serialized_end=566
  _globals['_DISABLEVOICERES']._serialized_start=7849
  _globals['_DISABLEVOICERES']._serialized_end=7866
  _globals['_ASMAPI']._serialized_start=7869
  _globals['_ASMAPI']._serialized_end=9470
# @@protoc_insertion_point(module_scope)
