# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/audit/omnichannel_events.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/commons/audit/omnichannel_events.proto\x12\x11\x61pi.commons.audit\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xcb\x01\n\x1dOmnichannelCreateProjectEvent\x12\x1d\n\nclient_sid\x18\x01 \x01(\x03R\tclientSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12U\n\x11\x63ompliance_config\x18\x04 \x01(\x0b\x32(.api.commons.OmniProjectComplianceConfigR\x10\x63omplianceConfig\"\xee\x02\n\x1eOmnichannelCreateCampaignEvent\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12M\n\x12\x63\x61mpaign_direction\x18\x04 \x01(\x0e\x32\x1e.api.commons.CampaignDirectionR\x11\x63\x61mpaignDirection\x12%\n\x0c\x63\x61mpaign_sid\x18\x05 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12>\n\romni_campaign\x18\x06 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12#\n\x0bproject_sid\x18\x07 \x01(\x03\x42\x02\x30\x01R\nprojectSid\"\x9f\x02\n\x13OmnichannelT10Event\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\"G\n\"OmnichannelDailyProjectReportEvent\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"L\n\'OmnichannelDailyConversationReportEvent\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"\x91\x03\n\'OmnichannelAgentAssignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\x93\x03\n)OmnichannelAgentUnassignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xeb\x03\n)OmnichannelAgentReassignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12&\n\x0f\x63urrent_user_id\x18\x05 \x01(\tR\rcurrentUserId\x12\x1e\n\x0bnew_user_id\x18\x06 \x01(\tR\tnewUserId\x12\x41\n\x0c\x63onversation\x18\x07 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x08 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12S\n\x18new_user_asm_session_sid\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x14newUserAsmSessionSid\"\xcb\x01\n#OmnichannelCustomerTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xa6\x02\n OmnichannelAgentTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId\"\xa8\x02\n\"OmnichannelManagerTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId\"\xed\x02\n\x1cOmnichannelFinishWrapUpEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\x85\x03\n\x1bOmnichannelBeginWrapUpEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId\"\xeb\x01\n\x13OmnichannelT11Event\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xff\x01\n\"OmnichannelCreateConversationEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\"\xda\x01\n\x1cOmnichannelAgentSuspendEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x02 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xf8\x01\n!OmnichannelCloseConversationEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x02 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\"\xfa\x01\n\x1eOmnichannelUpdateCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x96\x03\n,OmnichannelSetConversationCollectedDataEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12M\n\x12\x63\x61mpaign_direction\x18\x04 \x01(\x0e\x32\x1e.api.commons.CampaignDirectionR\x11\x63\x61mpaignDirection\x12M\n\x0e\x63ollected_data\x18\x05 \x01(\x0b\x32&.api.commons.ConversationCollectedDataR\rcollectedData\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xfc\x01\n OmnichannelCompleteCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xfb\x01\n\x1fOmnichannelArchiveCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xf9\x01\n\x1dOmnichannelStartCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xf9\x01\n\x1dOmnichannelPauseCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xfa\x01\n\x1eOmnichannelResumeCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x83\x01\n\x1eOmnichannelScheduleModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelStartModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelPauseModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x81\x01\n\x1cOmnichannelResumeModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelErrorModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x82\x01\n\x1dOmnichannelSuccessModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x7f\n\x1aOmnichannelFailModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x83\x01\n\x1eOmnichannelCompleteModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x82\x01\n\x1dOmnichannelArchiveModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x81\x01\n\x1cOmnichannelUpdateModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xe2\x01\n$OmnichannelSmsMessageSentModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12#\n\rmessage_units\x18\x02 \x01(\x03R\x0cmessageUnits\x12>\n\romni_campaign\x18\x03 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\"\xe1\x02\n\"OmnichannelModuleInitialReplyEvent\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSid\x12.\n\x13\x63\x61mpaign_module_sid\x18\x03 \x01(\x03R\x11\x63\x61mpaignModuleSid\x12)\n\x10\x63onversation_sid\x18\x04 \x01(\x03R\x0f\x63onversationSid\x12;\n\x0c\x63hannel_type\x18\x05 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x35\n\x08\x63\x61mpaign\x18\x07 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x08\x63\x61mpaign\"\xb9\x02\n\x1fOmnichannelTaskMessageSentEvent\x12\x19\n\x08task_sid\x18\x01 \x01(\x03R\x07taskSid\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSid\x12\x1d\n\nmodule_sid\x18\x03 \x01(\x03R\tmoduleSid\x12#\n\rmessage_units\x18\x04 \x01(\x03R\x0cmessageUnits\x12\x35\n\x08\x63\x61mpaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x08\x63\x61mpaign\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12)\n\x04task\x18\x07 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\"\xda\x01\n\"OmnichannelConnectedInboxPollEvent\x12>\n\romni_campaign\x18\x01 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12.\n\x13\x63\x61mpaign_module_sid\x18\x02 \x01(\x03R\x11\x63\x61mpaignModuleSid\x12\x44\n\x0f\x63onnected_inbox\x18\x03 \x01(\x0b\x32\x1b.api.commons.ConnectedInboxR\x0e\x63onnectedInbox\"m\n%OmnichannelConnectedInboxCreatedEvent\x12\x44\n\x0f\x63onnected_inbox\x18\x01 \x01(\x0b\x32\x1b.api.commons.ConnectedInboxR\x0e\x63onnectedInbox\"|\n!OmnichannelAgentMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits\"~\n#OmnichannelManagerMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits\"\x7f\n$OmnichannelCustomerMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits\"}\n\"OmnichannelSystemMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits\"i\n\x1fOmnichannelPaymentLinkSentEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x12\n\x04link\x18\x02 \x01(\tR\x04link\"\x97\x01\n)OmnichannelManualApproveTaskAcceptedEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x97\x01\n)OmnichannelManualApproveTaskRejectedEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x96\x01\n(OmnichannelManualApproveTaskTimeoutEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x96\x01\n(OmnichannelManualApproveTaskRequeueEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSidB\x95\x01\n\x15\x63om.api.commons.auditB\x16OmnichannelEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.omnichannel_events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\026OmnichannelEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['project_sid']._options = None
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT'].fields_by_name['conversation_sid']._options = None
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT'].fields_by_name['campaign_sid']._options = None
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSTARTMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELSTARTMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELPAUSEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELPAUSEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELRESUMEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELRESUMEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELERRORMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELERRORMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSUCCESSMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELSUCCESSMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELFAILMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELFAILMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELARCHIVEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELARCHIVEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELUPDATEMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELUPDATEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT'].fields_by_name['module_sid']._options = None
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCREATEPROJECTEVENT']._serialized_start=129
  _globals['_OMNICHANNELCREATEPROJECTEVENT']._serialized_end=332
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT']._serialized_start=335
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT']._serialized_end=701
  _globals['_OMNICHANNELT10EVENT']._serialized_start=704
  _globals['_OMNICHANNELT10EVENT']._serialized_end=991
  _globals['_OMNICHANNELDAILYPROJECTREPORTEVENT']._serialized_start=993
  _globals['_OMNICHANNELDAILYPROJECTREPORTEVENT']._serialized_end=1064
  _globals['_OMNICHANNELDAILYCONVERSATIONREPORTEVENT']._serialized_start=1066
  _globals['_OMNICHANNELDAILYCONVERSATIONREPORTEVENT']._serialized_end=1142
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT']._serialized_start=1145
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT']._serialized_end=1546
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT']._serialized_start=1549
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT']._serialized_end=1952
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT']._serialized_start=1955
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT']._serialized_end=2446
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT']._serialized_start=2449
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT']._serialized_end=2652
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._serialized_start=2655
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._serialized_end=2949
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._serialized_start=2952
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._serialized_end=3248
  _globals['_OMNICHANNELFINISHWRAPUPEVENT']._serialized_start=3251
  _globals['_OMNICHANNELFINISHWRAPUPEVENT']._serialized_end=3616
  _globals['_OMNICHANNELBEGINWRAPUPEVENT']._serialized_start=3619
  _globals['_OMNICHANNELBEGINWRAPUPEVENT']._serialized_end=4008
  _globals['_OMNICHANNELT11EVENT']._serialized_start=4011
  _globals['_OMNICHANNELT11EVENT']._serialized_end=4246
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT']._serialized_start=4249
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT']._serialized_end=4504
  _globals['_OMNICHANNELAGENTSUSPENDEVENT']._serialized_start=4507
  _globals['_OMNICHANNELAGENTSUSPENDEVENT']._serialized_end=4725
  _globals['_OMNICHANNELCLOSECONVERSATIONEVENT']._serialized_start=4728
  _globals['_OMNICHANNELCLOSECONVERSATIONEVENT']._serialized_end=4976
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT']._serialized_start=4979
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT']._serialized_end=5229
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT']._serialized_start=5232
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT']._serialized_end=5638
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT']._serialized_start=5641
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT']._serialized_end=5893
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT']._serialized_start=5896
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT']._serialized_end=6147
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT']._serialized_start=6150
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT']._serialized_end=6399
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT']._serialized_start=6402
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT']._serialized_end=6651
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT']._serialized_start=6654
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT']._serialized_end=6904
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT']._serialized_start=6907
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT']._serialized_end=7038
  _globals['_OMNICHANNELSTARTMODULEEVENT']._serialized_start=7041
  _globals['_OMNICHANNELSTARTMODULEEVENT']._serialized_end=7169
  _globals['_OMNICHANNELPAUSEMODULEEVENT']._serialized_start=7172
  _globals['_OMNICHANNELPAUSEMODULEEVENT']._serialized_end=7300
  _globals['_OMNICHANNELRESUMEMODULEEVENT']._serialized_start=7303
  _globals['_OMNICHANNELRESUMEMODULEEVENT']._serialized_end=7432
  _globals['_OMNICHANNELERRORMODULEEVENT']._serialized_start=7435
  _globals['_OMNICHANNELERRORMODULEEVENT']._serialized_end=7563
  _globals['_OMNICHANNELSUCCESSMODULEEVENT']._serialized_start=7566
  _globals['_OMNICHANNELSUCCESSMODULEEVENT']._serialized_end=7696
  _globals['_OMNICHANNELFAILMODULEEVENT']._serialized_start=7698
  _globals['_OMNICHANNELFAILMODULEEVENT']._serialized_end=7825
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT']._serialized_start=7828
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT']._serialized_end=7959
  _globals['_OMNICHANNELARCHIVEMODULEEVENT']._serialized_start=7962
  _globals['_OMNICHANNELARCHIVEMODULEEVENT']._serialized_end=8092
  _globals['_OMNICHANNELUPDATEMODULEEVENT']._serialized_start=8095
  _globals['_OMNICHANNELUPDATEMODULEEVENT']._serialized_end=8224
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._serialized_start=8227
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._serialized_end=8453
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._serialized_start=8456
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._serialized_end=8809
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._serialized_start=8812
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._serialized_end=9125
  _globals['_OMNICHANNELCONNECTEDINBOXPOLLEVENT']._serialized_start=9128
  _globals['_OMNICHANNELCONNECTEDINBOXPOLLEVENT']._serialized_end=9346
  _globals['_OMNICHANNELCONNECTEDINBOXCREATEDEVENT']._serialized_start=9348
  _globals['_OMNICHANNELCONNECTEDINBOXCREATEDEVENT']._serialized_end=9457
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._serialized_start=9459
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._serialized_end=9583
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._serialized_start=9585
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._serialized_end=9711
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._serialized_start=9713
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._serialized_end=9840
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._serialized_start=9842
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._serialized_end=9967
  _globals['_OMNICHANNELPAYMENTLINKSENTEVENT']._serialized_start=9969
  _globals['_OMNICHANNELPAYMENTLINKSENTEVENT']._serialized_end=10074
  _globals['_OMNICHANNELMANUALAPPROVETASKACCEPTEDEVENT']._serialized_start=10077
  _globals['_OMNICHANNELMANUALAPPROVETASKACCEPTEDEVENT']._serialized_end=10228
  _globals['_OMNICHANNELMANUALAPPROVETASKREJECTEDEVENT']._serialized_start=10231
  _globals['_OMNICHANNELMANUALAPPROVETASKREJECTEDEVENT']._serialized_end=10382
  _globals['_OMNICHANNELMANUALAPPROVETASKTIMEOUTEVENT']._serialized_start=10385
  _globals['_OMNICHANNELMANUALAPPROVETASKTIMEOUTEVENT']._serialized_end=10535
  _globals['_OMNICHANNELMANUALAPPROVETASKREQUEUEEVENT']._serialized_start=10538
  _globals['_OMNICHANNELMANUALAPPROVETASKREQUEUEEVENT']._serialized_end=10688
# @@protoc_insertion_point(module_scope)
