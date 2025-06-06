# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/omnichannel_events.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'api/commons/audit/omnichannel_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/commons/audit/omnichannel_events.proto\x12\x11\x61pi.commons.audit\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xcb\x01\n\x1dOmnichannelCreateProjectEvent\x12\x1d\n\nclient_sid\x18\x01 \x01(\x03R\tclientSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12U\n\x11\x63ompliance_config\x18\x04 \x01(\x0b\x32(.api.commons.OmniProjectComplianceConfigR\x10\x63omplianceConfig\"\xee\x02\n\x1eOmnichannelCreateCampaignEvent\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12M\n\x12\x63\x61mpaign_direction\x18\x04 \x01(\x0e\x32\x1e.api.commons.CampaignDirectionR\x11\x63\x61mpaignDirection\x12%\n\x0c\x63\x61mpaign_sid\x18\x05 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12>\n\romni_campaign\x18\x06 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12#\n\x0bproject_sid\x18\x07 \x01(\x03\x42\x02\x30\x01R\nprojectSid\"\x9f\x02\n\x13OmnichannelT10Event\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\"G\n\"OmnichannelDailyProjectReportEvent\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"L\n\'OmnichannelDailyConversationReportEvent\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\"\x91\x03\n\'OmnichannelAgentAssignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\x93\x03\n)OmnichannelAgentUnassignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xeb\x03\n)OmnichannelAgentReassignConversationEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\x12&\n\x0f\x63urrent_user_id\x18\x05 \x01(\tR\rcurrentUserId\x12\x1e\n\x0bnew_user_id\x18\x06 \x01(\tR\tnewUserId\x12\x41\n\x0c\x63onversation\x18\x07 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x08 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12S\n\x18new_user_asm_session_sid\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x14newUserAsmSessionSid\"\xcf\x01\n#OmnichannelCustomerTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation:\x02\x18\x01\"\xaa\x02\n OmnichannelAgentTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId:\x02\x18\x01\"\xac\x02\n\"OmnichannelManagerTextMessageEvent\x12-\n\x10\x63onversation_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x05 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId:\x02\x18\x01\"\xed\x02\n\x1cOmnichannelFinishWrapUpEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\x85\x03\n\x1bOmnichannelBeginWrapUpEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x05 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x07 \x01(\tR\x06userId\"\xeb\x01\n\x13OmnichannelT11Event\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12%\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xff\x01\n\"OmnichannelCreateConversationEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\"\xda\x01\n\x1cOmnichannelAgentSuspendEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x02 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xf8\x01\n!OmnichannelCloseConversationEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x41\n\x0c\x63onversation\x18\x02 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\x12\x43\n\x0f\x61sm_session_sid\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\x12\x17\n\x07user_id\x18\x04 \x01(\tR\x06userId\"\xb8\x01\n\x1fOmnichannelTranscriptSavedEvent\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSid\x12\'\n\x0ftranscript_path\x18\x02 \x01(\tR\x0etranscriptPath\x12\x41\n\x0c\x63onversation\x18\x03 \x01(\x0b\x32\x1d.api.commons.OmniConversationR\x0c\x63onversation\"\xfa\x01\n\x1eOmnichannelUpdateCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x96\x03\n,OmnichannelSetConversationCollectedDataEvent\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12;\n\x0c\x63hannel_type\x18\x03 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12M\n\x12\x63\x61mpaign_direction\x18\x04 \x01(\x0e\x32\x1e.api.commons.CampaignDirectionR\x11\x63\x61mpaignDirection\x12M\n\x0e\x63ollected_data\x18\x05 \x01(\x0b\x32&.api.commons.ConversationCollectedDataR\rcollectedData\x12\x43\n\x0f\x61sm_session_sid\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rasmSessionSid\"\xfc\x01\n OmnichannelCompleteCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xfb\x01\n\x1fOmnichannelArchiveCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xf9\x01\n\x1dOmnichannelStartCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xf9\x01\n\x1dOmnichannelPauseCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xfa\x01\n\x1eOmnichannelResumeCampaignEvent\x12%\n\x0c\x63\x61mpaign_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0b\x63\x61mpaignSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12;\n\x0c\x63hannel_type\x18\x04 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\romni_campaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x83\x01\n\x1eOmnichannelScheduleModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelStartModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelPauseModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x81\x01\n\x1cOmnichannelResumeModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x80\x01\n\x1bOmnichannelErrorModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x82\x01\n\x1dOmnichannelSuccessModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x7f\n\x1aOmnichannelFailModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x83\x01\n\x1eOmnichannelCompleteModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x82\x01\n\x1dOmnichannelArchiveModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\x81\x01\n\x1cOmnichannelUpdateModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12>\n\romni_campaign\x18\x02 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\"\xe6\x01\n$OmnichannelSmsMessageSentModuleEvent\x12!\n\nmodule_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tmoduleSid\x12#\n\rmessage_units\x18\x02 \x01(\x03R\x0cmessageUnits\x12>\n\romni_campaign\x18\x03 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12\x32\n\x07message\x18\x04 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message:\x02\x18\x01\"\xe5\x02\n\"OmnichannelModuleInitialReplyEvent\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSid\x12.\n\x13\x63\x61mpaign_module_sid\x18\x03 \x01(\x03R\x11\x63\x61mpaignModuleSid\x12)\n\x10\x63onversation_sid\x18\x04 \x01(\x03R\x0f\x63onversationSid\x12;\n\x0c\x63hannel_type\x18\x05 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x35\n\x08\x63\x61mpaign\x18\x07 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x08\x63\x61mpaign:\x02\x18\x01\"\xbd\x02\n\x1fOmnichannelTaskMessageSentEvent\x12\x19\n\x08task_sid\x18\x01 \x01(\x03R\x07taskSid\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSid\x12\x1d\n\nmodule_sid\x18\x03 \x01(\x03R\tmoduleSid\x12#\n\rmessage_units\x18\x04 \x01(\x03R\x0cmessageUnits\x12\x35\n\x08\x63\x61mpaign\x18\x05 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x08\x63\x61mpaign\x12\x32\n\x07message\x18\x06 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12)\n\x04task\x18\x07 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task:\x02\x18\x01\"\xda\x01\n\"OmnichannelConnectedInboxPollEvent\x12>\n\romni_campaign\x18\x01 \x01(\x0b\x32\x19.api.commons.OmniCampaignR\x0comniCampaign\x12.\n\x13\x63\x61mpaign_module_sid\x18\x02 \x01(\x03R\x11\x63\x61mpaignModuleSid\x12\x44\n\x0f\x63onnected_inbox\x18\x03 \x01(\x0b\x32\x1b.api.commons.ConnectedInboxR\x0e\x63onnectedInbox\"m\n%OmnichannelConnectedInboxCreatedEvent\x12\x44\n\x0f\x63onnected_inbox\x18\x01 \x01(\x0b\x32\x1b.api.commons.ConnectedInboxR\x0e\x63onnectedInbox\"\x80\x01\n!OmnichannelAgentMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits:\x02\x18\x01\"\x82\x01\n#OmnichannelManagerMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits:\x02\x18\x01\"\x83\x01\n$OmnichannelCustomerMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits:\x02\x18\x01\"\x81\x01\n\"OmnichannelSystemMessageUnitsEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12#\n\rmessage_units\x18\x02 \x01(\x05R\x0cmessageUnits:\x02\x18\x01\"i\n\x1fOmnichannelPaymentLinkSentEvent\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.api.commons.OmniMessageR\x07message\x12\x12\n\x04link\x18\x02 \x01(\tR\x04link\"\x97\x01\n)OmnichannelManualApproveTaskAcceptedEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x97\x01\n)OmnichannelManualApproveTaskRejectedEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x96\x01\n(OmnichannelManualApproveTaskTimeoutEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x96\x01\n(OmnichannelManualApproveTaskRequeueEvent\x12)\n\x04task\x18\x01 \x01(\x0b\x32\x15.api.commons.OmniTaskR\x04task\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\xda\x03\n\x1bOmnichannelMessageSentEvent\x12\x1f\n\x0bmessage_sid\x18\x01 \x01(\x03R\nmessageSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x1b\n\tsent_from\x18\x03 \x01(\tR\x08sentFrom\x12\x17\n\x07sent_to\x18\x04 \x01(\tR\x06sentTo\x12!\n\x0cmessage_size\x18\x05 \x01(\x03R\x0bmessageSize\x12\'\n\x0f\x61ttachment_size\x18\x06 \x01(\x03R\x0e\x61ttachmentSize\x12<\n\x0bsender_type\x18\x07 \x01(\x0e\x32\x1b.api.commons.OmniSenderTypeR\nsenderType\x12\x17\n\x07user_id\x18\x08 \x01(\tR\x06userId\x12?\n\x0cmessage_type\x18\t \x01(\x0e\x32\x1c.api.commons.OmniMessageTypeR\x0bmessageType\x12\x43\n\rprovider_type\x18\n \x01(\x0e\x32\x1e.api.commons.SmsNumberProviderR\x0cproviderType\"\x9e\x04\n OmnichannelProviderResponseEvent\x12(\n\x10omni_message_sid\x18\x01 \x01(\x03R\x0eomniMessageSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x1b\n\tsent_from\x18\x03 \x01(\tR\x08sentFrom\x12\x17\n\x07sent_to\x18\x04 \x01(\tR\x06sentTo\x12!\n\x0cmessage_size\x18\x05 \x01(\x03R\x0bmessageSize\x12\'\n\x0f\x61ttachment_size\x18\x06 \x01(\x03R\x0e\x61ttachmentSize\x12<\n\x0bsender_type\x18\x07 \x01(\x0e\x32\x1b.api.commons.OmniSenderTypeR\nsenderType\x12\x17\n\x07user_id\x18\x08 \x01(\tR\x06userId\x12\x34\n\x16provider_message_count\x18\t \x01(\x03R\x14providerMessageCount\x12?\n\x0cmessage_type\x18\n \x01(\x0e\x32\x1c.api.commons.OmniMessageTypeR\x0bmessageType\x12\x43\n\rprovider_type\x18\x0b \x01(\x0e\x32\x1e.api.commons.SmsNumberProviderR\x0cproviderType\"\xd2\x04\n%OmnichannelProviderMessageFailedEvent\x12(\n\x10omni_message_sid\x18\x01 \x01(\x03R\x0eomniMessageSid\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12\x1b\n\tsent_from\x18\x03 \x01(\tR\x08sentFrom\x12\x17\n\x07sent_to\x18\x04 \x01(\tR\x06sentTo\x12!\n\x0cmessage_size\x18\x05 \x01(\x03R\x0bmessageSize\x12\'\n\x0f\x61ttachment_size\x18\x06 \x01(\x03R\x0e\x61ttachmentSize\x12<\n\x0bsender_type\x18\x07 \x01(\x0e\x32\x1b.api.commons.OmniSenderTypeR\nsenderType\x12\x17\n\x07user_id\x18\x08 \x01(\tR\x06userId\x12\x34\n\x16provider_message_count\x18\t \x01(\x03R\x14providerMessageCount\x12?\n\x0cmessage_type\x18\n \x01(\x0e\x32\x1c.api.commons.OmniMessageTypeR\x0bmessageType\x12:\n\x08provider\x18\x0b \x01(\x0e\x32\x1e.api.commons.SmsNumberProviderR\x08provider\x12\x36\n\x06status\x18\x0c \x01(\x0e\x32\x1e.api.commons.OmniMessageStatusR\x06statusB\x95\x01\n\x15\x63om.api.commons.auditB\x16OmnichannelEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.omnichannel_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\026OmnichannelEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['project_sid']._loaded_options = None
  _globals['_OMNICHANNELCREATECAMPAIGNEVENT'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELT10EVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTUNASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTREASSIGNCONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT']._loaded_options = None
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._loaded_options = None
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._loaded_options = None
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELFINISHWRAPUPEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELBEGINWRAPUPEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELT11EVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT'].fields_by_name['campaign_sid']._loaded_options = None
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT'].fields_by_name['campaign_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSTARTMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELSTARTMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELPAUSEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELPAUSEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELRESUMEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELRESUMEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELERRORMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELERRORMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSUCCESSMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELSUCCESSMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELFAILMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELFAILMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELARCHIVEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELARCHIVEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELUPDATEMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELUPDATEMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT'].fields_by_name['module_sid']._loaded_options = None
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT'].fields_by_name['module_sid']._serialized_options = b'0\001'
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._loaded_options = None
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._loaded_options = None
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._loaded_options = None
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._loaded_options = None
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._loaded_options = None
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._loaded_options = None
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._serialized_options = b'\030\001'
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._loaded_options = None
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._serialized_options = b'\030\001'
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
  _globals['_OMNICHANNELCUSTOMERTEXTMESSAGEEVENT']._serialized_end=2656
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._serialized_start=2659
  _globals['_OMNICHANNELAGENTTEXTMESSAGEEVENT']._serialized_end=2957
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._serialized_start=2960
  _globals['_OMNICHANNELMANAGERTEXTMESSAGEEVENT']._serialized_end=3260
  _globals['_OMNICHANNELFINISHWRAPUPEVENT']._serialized_start=3263
  _globals['_OMNICHANNELFINISHWRAPUPEVENT']._serialized_end=3628
  _globals['_OMNICHANNELBEGINWRAPUPEVENT']._serialized_start=3631
  _globals['_OMNICHANNELBEGINWRAPUPEVENT']._serialized_end=4020
  _globals['_OMNICHANNELT11EVENT']._serialized_start=4023
  _globals['_OMNICHANNELT11EVENT']._serialized_end=4258
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT']._serialized_start=4261
  _globals['_OMNICHANNELCREATECONVERSATIONEVENT']._serialized_end=4516
  _globals['_OMNICHANNELAGENTSUSPENDEVENT']._serialized_start=4519
  _globals['_OMNICHANNELAGENTSUSPENDEVENT']._serialized_end=4737
  _globals['_OMNICHANNELCLOSECONVERSATIONEVENT']._serialized_start=4740
  _globals['_OMNICHANNELCLOSECONVERSATIONEVENT']._serialized_end=4988
  _globals['_OMNICHANNELTRANSCRIPTSAVEDEVENT']._serialized_start=4991
  _globals['_OMNICHANNELTRANSCRIPTSAVEDEVENT']._serialized_end=5175
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT']._serialized_start=5178
  _globals['_OMNICHANNELUPDATECAMPAIGNEVENT']._serialized_end=5428
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT']._serialized_start=5431
  _globals['_OMNICHANNELSETCONVERSATIONCOLLECTEDDATAEVENT']._serialized_end=5837
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT']._serialized_start=5840
  _globals['_OMNICHANNELCOMPLETECAMPAIGNEVENT']._serialized_end=6092
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT']._serialized_start=6095
  _globals['_OMNICHANNELARCHIVECAMPAIGNEVENT']._serialized_end=6346
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT']._serialized_start=6349
  _globals['_OMNICHANNELSTARTCAMPAIGNEVENT']._serialized_end=6598
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT']._serialized_start=6601
  _globals['_OMNICHANNELPAUSECAMPAIGNEVENT']._serialized_end=6850
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT']._serialized_start=6853
  _globals['_OMNICHANNELRESUMECAMPAIGNEVENT']._serialized_end=7103
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT']._serialized_start=7106
  _globals['_OMNICHANNELSCHEDULEMODULEEVENT']._serialized_end=7237
  _globals['_OMNICHANNELSTARTMODULEEVENT']._serialized_start=7240
  _globals['_OMNICHANNELSTARTMODULEEVENT']._serialized_end=7368
  _globals['_OMNICHANNELPAUSEMODULEEVENT']._serialized_start=7371
  _globals['_OMNICHANNELPAUSEMODULEEVENT']._serialized_end=7499
  _globals['_OMNICHANNELRESUMEMODULEEVENT']._serialized_start=7502
  _globals['_OMNICHANNELRESUMEMODULEEVENT']._serialized_end=7631
  _globals['_OMNICHANNELERRORMODULEEVENT']._serialized_start=7634
  _globals['_OMNICHANNELERRORMODULEEVENT']._serialized_end=7762
  _globals['_OMNICHANNELSUCCESSMODULEEVENT']._serialized_start=7765
  _globals['_OMNICHANNELSUCCESSMODULEEVENT']._serialized_end=7895
  _globals['_OMNICHANNELFAILMODULEEVENT']._serialized_start=7897
  _globals['_OMNICHANNELFAILMODULEEVENT']._serialized_end=8024
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT']._serialized_start=8027
  _globals['_OMNICHANNELCOMPLETEMODULEEVENT']._serialized_end=8158
  _globals['_OMNICHANNELARCHIVEMODULEEVENT']._serialized_start=8161
  _globals['_OMNICHANNELARCHIVEMODULEEVENT']._serialized_end=8291
  _globals['_OMNICHANNELUPDATEMODULEEVENT']._serialized_start=8294
  _globals['_OMNICHANNELUPDATEMODULEEVENT']._serialized_end=8423
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._serialized_start=8426
  _globals['_OMNICHANNELSMSMESSAGESENTMODULEEVENT']._serialized_end=8656
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._serialized_start=8659
  _globals['_OMNICHANNELMODULEINITIALREPLYEVENT']._serialized_end=9016
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._serialized_start=9019
  _globals['_OMNICHANNELTASKMESSAGESENTEVENT']._serialized_end=9336
  _globals['_OMNICHANNELCONNECTEDINBOXPOLLEVENT']._serialized_start=9339
  _globals['_OMNICHANNELCONNECTEDINBOXPOLLEVENT']._serialized_end=9557
  _globals['_OMNICHANNELCONNECTEDINBOXCREATEDEVENT']._serialized_start=9559
  _globals['_OMNICHANNELCONNECTEDINBOXCREATEDEVENT']._serialized_end=9668
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._serialized_start=9671
  _globals['_OMNICHANNELAGENTMESSAGEUNITSEVENT']._serialized_end=9799
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._serialized_start=9802
  _globals['_OMNICHANNELMANAGERMESSAGEUNITSEVENT']._serialized_end=9932
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._serialized_start=9935
  _globals['_OMNICHANNELCUSTOMERMESSAGEUNITSEVENT']._serialized_end=10066
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._serialized_start=10069
  _globals['_OMNICHANNELSYSTEMMESSAGEUNITSEVENT']._serialized_end=10198
  _globals['_OMNICHANNELPAYMENTLINKSENTEVENT']._serialized_start=10200
  _globals['_OMNICHANNELPAYMENTLINKSENTEVENT']._serialized_end=10305
  _globals['_OMNICHANNELMANUALAPPROVETASKACCEPTEDEVENT']._serialized_start=10308
  _globals['_OMNICHANNELMANUALAPPROVETASKACCEPTEDEVENT']._serialized_end=10459
  _globals['_OMNICHANNELMANUALAPPROVETASKREJECTEDEVENT']._serialized_start=10462
  _globals['_OMNICHANNELMANUALAPPROVETASKREJECTEDEVENT']._serialized_end=10613
  _globals['_OMNICHANNELMANUALAPPROVETASKTIMEOUTEVENT']._serialized_start=10616
  _globals['_OMNICHANNELMANUALAPPROVETASKTIMEOUTEVENT']._serialized_end=10766
  _globals['_OMNICHANNELMANUALAPPROVETASKREQUEUEEVENT']._serialized_start=10769
  _globals['_OMNICHANNELMANUALAPPROVETASKREQUEUEEVENT']._serialized_end=10919
  _globals['_OMNICHANNELMESSAGESENTEVENT']._serialized_start=10922
  _globals['_OMNICHANNELMESSAGESENTEVENT']._serialized_end=11396
  _globals['_OMNICHANNELPROVIDERRESPONSEEVENT']._serialized_start=11399
  _globals['_OMNICHANNELPROVIDERRESPONSEEVENT']._serialized_end=11941
  _globals['_OMNICHANNELPROVIDERMESSAGEFAILEDEVENT']._serialized_start=11944
  _globals['_OMNICHANNELPROVIDERMESSAGEFAILEDEVENT']._serialized_end=12538
# @@protoc_insertion_point(module_scope)
