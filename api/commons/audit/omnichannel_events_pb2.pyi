from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OmnichannelCreateProjectEvent(_message.Message):
    __slots__ = ()
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    name: str
    description: str
    compliance_config: _omnichannel_pb2.OmniProjectComplianceConfig
    def __init__(self, client_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., compliance_config: _Optional[_Union[_omnichannel_pb2.OmniProjectComplianceConfig, _Mapping]] = ...) -> None: ...

class OmnichannelCreateCampaignEvent(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.CampaignDirection
    campaign_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    project_sid: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.CampaignDirection, str]] = ..., campaign_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., project_sid: _Optional[int] = ...) -> None: ...

class OmnichannelT10Event(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ...) -> None: ...

class OmnichannelDailyProjectReportEvent(_message.Message):
    __slots__ = ()
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    def __init__(self, download_url: _Optional[str] = ...) -> None: ...

class OmnichannelDailyConversationReportEvent(_message.Message):
    __slots__ = ()
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    def __init__(self, download_url: _Optional[str] = ...) -> None: ...

class OmnichannelAgentAssignConversationEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    user_id: str
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., user_id: _Optional[str] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelAgentUnassignConversationEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    user_id: str
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., user_id: _Optional[str] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelAgentReassignConversationEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    user_id: str
    current_user_id: str
    new_user_id: str
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    new_user_asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., user_id: _Optional[str] = ..., current_user_id: _Optional[str] = ..., new_user_id: _Optional[str] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., new_user_asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelCustomerTextMessageEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    message: _omnichannel_pb2.OmniMessage
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation_sid: _Optional[int] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class OmnichannelAgentTextMessageEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    message: _omnichannel_pb2.OmniMessage
    conversation: _omnichannel_pb2.OmniConversation
    asm_session_sid: _wrappers_pb2.Int64Value
    user_id: str
    def __init__(self, conversation_sid: _Optional[int] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class OmnichannelManagerTextMessageEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    message: _omnichannel_pb2.OmniMessage
    conversation: _omnichannel_pb2.OmniConversation
    asm_session_sid: _wrappers_pb2.Int64Value
    user_id: str
    def __init__(self, conversation_sid: _Optional[int] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class OmnichannelFinishWrapUpEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelBeginWrapUpEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    asm_session_sid: _wrappers_pb2.Int64Value
    user_id: str
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class OmnichannelT11Event(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class OmnichannelCreateConversationEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    conversation: _omnichannel_pb2.OmniConversation
    message: _omnichannel_pb2.OmniMessage
    def __init__(self, campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ...) -> None: ...

class OmnichannelAgentSuspendEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    conversation: _omnichannel_pb2.OmniConversation
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelCloseConversationEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    conversation: _omnichannel_pb2.OmniConversation
    asm_session_sid: _wrappers_pb2.Int64Value
    user_id: str
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class OmnichannelTranscriptSavedEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    transcript_path: str
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation_sid: _Optional[int] = ..., transcript_path: _Optional[str] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class OmnichannelUpdateCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelSetConversationCollectedDataEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    user_id: str
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.CampaignDirection
    collected_data: _omnichannel_pb2.ConversationCollectedData
    asm_session_sid: _wrappers_pb2.Int64Value
    def __init__(self, conversation_sid: _Optional[int] = ..., user_id: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.CampaignDirection, str]] = ..., collected_data: _Optional[_Union[_omnichannel_pb2.ConversationCollectedData, _Mapping]] = ..., asm_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class OmnichannelCompleteCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelArchiveCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelStartCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelPauseCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelResumeCampaignEvent(_message.Message):
    __slots__ = ()
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    name: str
    description: str
    channel_type: _omnichannel_pb2.ChannelType
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, campaign_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelScheduleModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelStartModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelPauseModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelResumeModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelErrorModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelSuccessModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelFailModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelCompleteModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelArchiveModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelUpdateModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, module_sid: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelSmsMessageSentModuleEvent(_message.Message):
    __slots__ = ()
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    module_sid: int
    message_units: int
    omni_campaign: _omnichannel_pb2.OmniCampaign
    message: _omnichannel_pb2.OmniMessage
    def __init__(self, module_sid: _Optional[int] = ..., message_units: _Optional[int] = ..., omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ...) -> None: ...

class OmnichannelModuleInitialReplyEvent(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    campaign_sid: int
    campaign_module_sid: int
    conversation_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    message: _omnichannel_pb2.OmniMessage
    campaign: _omnichannel_pb2.OmniCampaign
    def __init__(self, org_id: _Optional[str] = ..., campaign_sid: _Optional[int] = ..., campaign_module_sid: _Optional[int] = ..., conversation_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ...) -> None: ...

class OmnichannelTaskMessageSentEvent(_message.Message):
    __slots__ = ()
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    campaign_sid: int
    module_sid: int
    message_units: int
    campaign: _omnichannel_pb2.OmniCampaign
    message: _omnichannel_pb2.OmniMessage
    task: _omnichannel_pb2.OmniTask
    def __init__(self, task_sid: _Optional[int] = ..., campaign_sid: _Optional[int] = ..., module_sid: _Optional[int] = ..., message_units: _Optional[int] = ..., campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ...) -> None: ...

class OmnichannelConnectedInboxPollEvent(_message.Message):
    __slots__ = ()
    OMNI_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_FIELD_NUMBER: _ClassVar[int]
    omni_campaign: _omnichannel_pb2.OmniCampaign
    campaign_module_sid: int
    connected_inbox: _omnichannel_pb2.ConnectedInbox
    def __init__(self, omni_campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., campaign_module_sid: _Optional[int] = ..., connected_inbox: _Optional[_Union[_omnichannel_pb2.ConnectedInbox, _Mapping]] = ...) -> None: ...

class OmnichannelConnectedInboxCreatedEvent(_message.Message):
    __slots__ = ()
    CONNECTED_INBOX_FIELD_NUMBER: _ClassVar[int]
    connected_inbox: _omnichannel_pb2.ConnectedInbox
    def __init__(self, connected_inbox: _Optional[_Union[_omnichannel_pb2.ConnectedInbox, _Mapping]] = ...) -> None: ...

class OmnichannelAgentMessageUnitsEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    message_units: int
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., message_units: _Optional[int] = ...) -> None: ...

class OmnichannelManagerMessageUnitsEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    message_units: int
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., message_units: _Optional[int] = ...) -> None: ...

class OmnichannelCustomerMessageUnitsEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    message_units: int
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., message_units: _Optional[int] = ...) -> None: ...

class OmnichannelSystemMessageUnitsEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    message_units: int
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., message_units: _Optional[int] = ...) -> None: ...

class OmnichannelPaymentLinkSentEvent(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    message: _omnichannel_pb2.OmniMessage
    link: str
    def __init__(self, message: _Optional[_Union[_omnichannel_pb2.OmniMessage, _Mapping]] = ..., link: _Optional[str] = ...) -> None: ...

class OmnichannelManualApproveTaskAcceptedEvent(_message.Message):
    __slots__ = ()
    TASK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    task: _omnichannel_pb2.OmniTask
    user_id: str
    asm_session_sid: int
    def __init__(self, task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ..., user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class OmnichannelManualApproveTaskRejectedEvent(_message.Message):
    __slots__ = ()
    TASK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    task: _omnichannel_pb2.OmniTask
    user_id: str
    asm_session_sid: int
    def __init__(self, task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ..., user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class OmnichannelManualApproveTaskTimeoutEvent(_message.Message):
    __slots__ = ()
    TASK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    task: _omnichannel_pb2.OmniTask
    user_id: str
    asm_session_sid: int
    def __init__(self, task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ..., user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class OmnichannelManualApproveTaskRequeueEvent(_message.Message):
    __slots__ = ()
    TASK_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    task: _omnichannel_pb2.OmniTask
    user_id: str
    asm_session_sid: int
    def __init__(self, task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ..., user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class OmnichannelMessageSentEvent(_message.Message):
    __slots__ = ()
    MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENT_FROM_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    message_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    sent_from: str
    sent_to: str
    message_size: int
    attachment_size: int
    sender_type: _omnichannel_pb2.OmniSenderType
    user_id: str
    message_type: _omnichannel_pb2.OmniMessageType
    provider_type: _omnichannel_pb2.SmsNumberProvider
    def __init__(self, message_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., sent_from: _Optional[str] = ..., sent_to: _Optional[str] = ..., message_size: _Optional[int] = ..., attachment_size: _Optional[int] = ..., sender_type: _Optional[_Union[_omnichannel_pb2.OmniSenderType, str]] = ..., user_id: _Optional[str] = ..., message_type: _Optional[_Union[_omnichannel_pb2.OmniMessageType, str]] = ..., provider_type: _Optional[_Union[_omnichannel_pb2.SmsNumberProvider, str]] = ...) -> None: ...

class OmnichannelProviderResponseEvent(_message.Message):
    __slots__ = ()
    OMNI_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENT_FROM_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    omni_message_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    sent_from: str
    sent_to: str
    message_size: int
    attachment_size: int
    sender_type: _omnichannel_pb2.OmniSenderType
    user_id: str
    provider_message_count: int
    message_type: _omnichannel_pb2.OmniMessageType
    provider_type: _omnichannel_pb2.SmsNumberProvider
    def __init__(self, omni_message_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., sent_from: _Optional[str] = ..., sent_to: _Optional[str] = ..., message_size: _Optional[int] = ..., attachment_size: _Optional[int] = ..., sender_type: _Optional[_Union[_omnichannel_pb2.OmniSenderType, str]] = ..., user_id: _Optional[str] = ..., provider_message_count: _Optional[int] = ..., message_type: _Optional[_Union[_omnichannel_pb2.OmniMessageType, str]] = ..., provider_type: _Optional[_Union[_omnichannel_pb2.SmsNumberProvider, str]] = ...) -> None: ...

class OmnichannelProviderMessageFailedEvent(_message.Message):
    __slots__ = ()
    OMNI_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENT_FROM_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    omni_message_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    sent_from: str
    sent_to: str
    message_size: int
    attachment_size: int
    sender_type: _omnichannel_pb2.OmniSenderType
    user_id: str
    provider_message_count: int
    message_type: _omnichannel_pb2.OmniMessageType
    provider: _omnichannel_pb2.SmsNumberProvider
    status: _omnichannel_pb2.OmniMessageStatus
    def __init__(self, omni_message_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., sent_from: _Optional[str] = ..., sent_to: _Optional[str] = ..., message_size: _Optional[int] = ..., attachment_size: _Optional[int] = ..., sender_type: _Optional[_Union[_omnichannel_pb2.OmniSenderType, str]] = ..., user_id: _Optional[str] = ..., provider_message_count: _Optional[int] = ..., message_type: _Optional[_Union[_omnichannel_pb2.OmniMessageType, str]] = ..., provider: _Optional[_Union[_omnichannel_pb2.SmsNumberProvider, str]] = ..., status: _Optional[_Union[_omnichannel_pb2.OmniMessageStatus, str]] = ...) -> None: ...

class OmnichannelInboundProviderMessageEvent(_message.Message):
    __slots__ = ()
    OMNI_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENT_FROM_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    omni_message_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    sent_from: str
    sent_to: str
    message_size: int
    attachment_size: int
    sender_type: _omnichannel_pb2.OmniSenderType
    user_id: str
    provider_message_count: int
    message_type: _omnichannel_pb2.OmniMessageType
    provider: _omnichannel_pb2.SmsNumberProvider
    status: _omnichannel_pb2.OmniMessageStatus
    def __init__(self, omni_message_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., sent_from: _Optional[str] = ..., sent_to: _Optional[str] = ..., message_size: _Optional[int] = ..., attachment_size: _Optional[int] = ..., sender_type: _Optional[_Union[_omnichannel_pb2.OmniSenderType, str]] = ..., user_id: _Optional[str] = ..., provider_message_count: _Optional[int] = ..., message_type: _Optional[_Union[_omnichannel_pb2.OmniMessageType, str]] = ..., provider: _Optional[_Union[_omnichannel_pb2.SmsNumberProvider, str]] = ..., status: _Optional[_Union[_omnichannel_pb2.OmniMessageStatus, str]] = ...) -> None: ...
