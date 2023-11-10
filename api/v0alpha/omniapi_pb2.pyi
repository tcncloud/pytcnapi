from annotations import authz_pb2 as _authz_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from api.commons import types_pb2 as _types_pb2
from api.commons import wfm_pb2 as _wfm_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestResponseReq(_message.Message):
    __slots__ = ("conversation_id",)
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class SuggestResponseRes(_message.Message):
    __slots__ = ("suggested_response",)
    SUGGESTED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    suggested_response: str
    def __init__(self, suggested_response: _Optional[str] = ...) -> None: ...

class CreateCampaignReq(_message.Message):
    __slots__ = ("campaign", "modules")
    class CampaignModule(_message.Message):
        __slots__ = ("module", "omni_contact_list")
        MODULE_FIELD_NUMBER: _ClassVar[int]
        OMNI_CONTACT_LIST_FIELD_NUMBER: _ClassVar[int]
        module: _omnichannel_pb2.OmniCampaignModule
        omni_contact_list: ContactListsDataSource
        def __init__(self, module: _Optional[_Union[_omnichannel_pb2.OmniCampaignModule, _Mapping]] = ..., omni_contact_list: _Optional[_Union[ContactListsDataSource, _Mapping]] = ...) -> None: ...
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    campaign: _omnichannel_pb2.OmniCampaign
    modules: _containers.RepeatedCompositeFieldContainer[CreateCampaignReq.CampaignModule]
    def __init__(self, campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., modules: _Optional[_Iterable[_Union[CreateCampaignReq.CampaignModule, _Mapping]]] = ...) -> None: ...

class ContactListsDataSource(_message.Message):
    __slots__ = ("contact_lists_data_source",)
    CONTACT_LISTS_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    contact_lists_data_source: _containers.RepeatedCompositeFieldContainer[ContactListDataSource]
    def __init__(self, contact_lists_data_source: _Optional[_Iterable[_Union[ContactListDataSource, _Mapping]]] = ...) -> None: ...

class ContactListDataSource(_message.Message):
    __slots__ = ("contact_list_sid",)
    CONTACT_LIST_SID_FIELD_NUMBER: _ClassVar[int]
    contact_list_sid: int
    def __init__(self, contact_list_sid: _Optional[int] = ...) -> None: ...

class ListCampaignsReq(_message.Message):
    __slots__ = ("statuses", "field_mask", "by_ids", "by_project", "by_time", "by_unsubscribe_link", "by_connected_inbox", "by_verified_email", "by_sms_number")
    class ByConnectedInbox(_message.Message):
        __slots__ = ("inbox_sid",)
        INBOX_SID_FIELD_NUMBER: _ClassVar[int]
        inbox_sid: int
        def __init__(self, inbox_sid: _Optional[int] = ...) -> None: ...
    class ByIds(_message.Message):
        __slots__ = ("campaign_sids",)
        CAMPAIGN_SIDS_FIELD_NUMBER: _ClassVar[int]
        campaign_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, campaign_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    class ByProject(_message.Message):
        __slots__ = ("project_sid",)
        PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
        project_sid: int
        def __init__(self, project_sid: _Optional[int] = ...) -> None: ...
    class ByTime(_message.Message):
        __slots__ = ("search_from", "search_to")
        SEARCH_FROM_FIELD_NUMBER: _ClassVar[int]
        SEARCH_TO_FIELD_NUMBER: _ClassVar[int]
        search_from: _timestamp_pb2.Timestamp
        search_to: _timestamp_pb2.Timestamp
        def __init__(self, search_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., search_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class ByUnsubscribeLink(_message.Message):
        __slots__ = ("link_sid",)
        LINK_SID_FIELD_NUMBER: _ClassVar[int]
        link_sid: int
        def __init__(self, link_sid: _Optional[int] = ...) -> None: ...
    class ByVerifiedEmail(_message.Message):
        __slots__ = ("email_sid",)
        EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
        email_sid: int
        def __init__(self, email_sid: _Optional[int] = ...) -> None: ...
    class BySmsNumber(_message.Message):
        __slots__ = ("number",)
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        number: str
        def __init__(self, number: _Optional[str] = ...) -> None: ...
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    BY_IDS_FIELD_NUMBER: _ClassVar[int]
    BY_PROJECT_FIELD_NUMBER: _ClassVar[int]
    BY_TIME_FIELD_NUMBER: _ClassVar[int]
    BY_UNSUBSCRIBE_LINK_FIELD_NUMBER: _ClassVar[int]
    BY_CONNECTED_INBOX_FIELD_NUMBER: _ClassVar[int]
    BY_VERIFIED_EMAIL_FIELD_NUMBER: _ClassVar[int]
    BY_SMS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.OmniCampaignStatus]
    field_mask: _field_mask_pb2.FieldMask
    by_ids: ListCampaignsReq.ByIds
    by_project: ListCampaignsReq.ByProject
    by_time: ListCampaignsReq.ByTime
    by_unsubscribe_link: ListCampaignsReq.ByUnsubscribeLink
    by_connected_inbox: ListCampaignsReq.ByConnectedInbox
    by_verified_email: ListCampaignsReq.ByVerifiedEmail
    by_sms_number: ListCampaignsReq.BySmsNumber
    def __init__(self, statuses: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniCampaignStatus, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., by_ids: _Optional[_Union[ListCampaignsReq.ByIds, _Mapping]] = ..., by_project: _Optional[_Union[ListCampaignsReq.ByProject, _Mapping]] = ..., by_time: _Optional[_Union[ListCampaignsReq.ByTime, _Mapping]] = ..., by_unsubscribe_link: _Optional[_Union[ListCampaignsReq.ByUnsubscribeLink, _Mapping]] = ..., by_connected_inbox: _Optional[_Union[ListCampaignsReq.ByConnectedInbox, _Mapping]] = ..., by_verified_email: _Optional[_Union[ListCampaignsReq.ByVerifiedEmail, _Mapping]] = ..., by_sms_number: _Optional[_Union[ListCampaignsReq.BySmsNumber, _Mapping]] = ...) -> None: ...

class ListCampaignsRes(_message.Message):
    __slots__ = ("campaigns", "modules")
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    campaigns: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniCampaign]
    modules: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniCampaignModule]
    def __init__(self, campaigns: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]]] = ..., modules: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniCampaignModule, _Mapping]]] = ...) -> None: ...

class GetCampaignByIdReq(_message.Message):
    __slots__ = ("campaign_sid",)
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    def __init__(self, campaign_sid: _Optional[int] = ...) -> None: ...

class GetOffLoadedTextMessageReq(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str
    def __init__(self, location: _Optional[str] = ...) -> None: ...

class GetOffLoadedTextMessageRes(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ManagerListMessagesReq(_message.Message):
    __slots__ = ("timestamp", "user_id", "live", "channel_type", "by_conversation_sid", "by_task_sid")
    class ByConversationSid(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    class ByTaskSid(_message.Message):
        __slots__ = ("task_sid",)
        TASK_SID_FIELD_NUMBER: _ClassVar[int]
        task_sid: int
        def __init__(self, task_sid: _Optional[int] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BY_CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    BY_TASK_SID_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    user_id: str
    live: bool
    channel_type: _omnichannel_pb2.ChannelType
    by_conversation_sid: ManagerListMessagesReq.ByConversationSid
    by_task_sid: ManagerListMessagesReq.ByTaskSid
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., live: bool = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., by_conversation_sid: _Optional[_Union[ManagerListMessagesReq.ByConversationSid, _Mapping]] = ..., by_task_sid: _Optional[_Union[ManagerListMessagesReq.ByTaskSid, _Mapping]] = ...) -> None: ...

class ListMessagesReq(_message.Message):
    __slots__ = ("timestamp", "live", "channel_type", "by_conversation_sid")
    class ByConversationSid(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BY_CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    live: bool
    channel_type: _omnichannel_pb2.ChannelType
    by_conversation_sid: ListMessagesReq.ByConversationSid
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., live: bool = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., by_conversation_sid: _Optional[_Union[ListMessagesReq.ByConversationSid, _Mapping]] = ...) -> None: ...

class ChatMessageUserInformation(_message.Message):
    __slots__ = ("user_id", "name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SendOmniMessageReq(_message.Message):
    __slots__ = ("conversation_sid", "payload", "campaign_sid", "ui_reference_id", "channel_type")
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    UI_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    payload: _omnichannel_pb2.OmniMessagePayload
    campaign_sid: int
    ui_reference_id: str
    channel_type: _omnichannel_pb2.ChannelType
    def __init__(self, conversation_sid: _Optional[int] = ..., payload: _Optional[_Union[_omnichannel_pb2.OmniMessagePayload, _Mapping]] = ..., campaign_sid: _Optional[int] = ..., ui_reference_id: _Optional[str] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ...) -> None: ...

class UpdateCampaignReq(_message.Message):
    __slots__ = ("campaign", "user_id", "field_mask")
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    campaign: _omnichannel_pb2.OmniCampaign
    user_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, campaign: _Optional[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]] = ..., user_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCampaignRes(_message.Message):
    __slots__ = ("notifier_id",)
    NOTIFIER_ID_FIELD_NUMBER: _ClassVar[int]
    notifier_id: str
    def __init__(self, notifier_id: _Optional[str] = ...) -> None: ...

class ListConversationsReq(_message.Message):
    __slots__ = ("channel_types", "field_mask", "statuses", "by_time", "by_assigned_user")
    class ByTime(_message.Message):
        __slots__ = ("start_time", "end_time", "page_size", "page_token")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        page_size: int
        page_token: str
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
    class ByAssignedUser(_message.Message):
        __slots__ = ("user_id", "statuses", "page_size", "page_token")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        statuses: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ConversationStatus]
        page_size: int
        page_token: str
        def __init__(self, user_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[_omnichannel_pb2.ConversationStatus, str]]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
    CHANNEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    BY_TIME_FIELD_NUMBER: _ClassVar[int]
    BY_ASSIGNED_USER_FIELD_NUMBER: _ClassVar[int]
    channel_types: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ChannelType]
    field_mask: _field_mask_pb2.FieldMask
    statuses: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ConversationStatus]
    by_time: ListConversationsReq.ByTime
    by_assigned_user: ListConversationsReq.ByAssignedUser
    def __init__(self, channel_types: _Optional[_Iterable[_Union[_omnichannel_pb2.ChannelType, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., statuses: _Optional[_Iterable[_Union[_omnichannel_pb2.ConversationStatus, str]]] = ..., by_time: _Optional[_Union[ListConversationsReq.ByTime, _Mapping]] = ..., by_assigned_user: _Optional[_Union[ListConversationsReq.ByAssignedUser, _Mapping]] = ...) -> None: ...

class ListConversationsRes(_message.Message):
    __slots__ = ("conversations", "next_page_token")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniConversation]
    next_page_token: str
    def __init__(self, conversations: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniConversation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateDispositionReq(_message.Message):
    __slots__ = ("disposition",)
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    disposition: str
    def __init__(self, disposition: _Optional[str] = ...) -> None: ...

class CreateDispositionRes(_message.Message):
    __slots__ = ("disposition_sid",)
    DISPOSITION_SID_FIELD_NUMBER: _ClassVar[int]
    disposition_sid: int
    def __init__(self, disposition_sid: _Optional[int] = ...) -> None: ...

class DeleteDispositionReq(_message.Message):
    __slots__ = ("disposition",)
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    disposition: _omnichannel_pb2.Disposition
    def __init__(self, disposition: _Optional[_Union[_omnichannel_pb2.Disposition, _Mapping]] = ...) -> None: ...

class ListDispositionsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDispositionsRes(_message.Message):
    __slots__ = ("dispositions",)
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    dispositions: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.Disposition]
    def __init__(self, dispositions: _Optional[_Iterable[_Union[_omnichannel_pb2.Disposition, _Mapping]]] = ...) -> None: ...

class UpdateDispositionReq(_message.Message):
    __slots__ = ("disposition_sid", "disposition")
    DISPOSITION_SID_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    disposition_sid: int
    disposition: str
    def __init__(self, disposition_sid: _Optional[int] = ..., disposition: _Optional[str] = ...) -> None: ...

class ListCustomUnsubscribeLinksRes(_message.Message):
    __slots__ = ("custom_unsubscribe_links",)
    CUSTOM_UNSUBSCRIBE_LINKS_FIELD_NUMBER: _ClassVar[int]
    custom_unsubscribe_links: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniCustomUnsubscribeLink]
    def __init__(self, custom_unsubscribe_links: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniCustomUnsubscribeLink, _Mapping]]] = ...) -> None: ...

class CreateCustomUnsubscribeLinkRes(_message.Message):
    __slots__ = ("custom_unsubscribe_link_sid", "validated")
    CUSTOM_UNSUBSCRIBE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_FIELD_NUMBER: _ClassVar[int]
    custom_unsubscribe_link_sid: int
    validated: bool
    def __init__(self, custom_unsubscribe_link_sid: _Optional[int] = ..., validated: bool = ...) -> None: ...

class UpdateCustomUnsubscribeLinkReq(_message.Message):
    __slots__ = ("custom_unsubscribe_link_sid", "link_name", "link_url", "description")
    CUSTOM_UNSUBSCRIBE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    custom_unsubscribe_link_sid: int
    link_name: str
    link_url: str
    description: str
    def __init__(self, custom_unsubscribe_link_sid: _Optional[int] = ..., link_name: _Optional[str] = ..., link_url: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateCustomUnsubscribeLinkRes(_message.Message):
    __slots__ = ("validated", "date_validated")
    VALIDATED_FIELD_NUMBER: _ClassVar[int]
    DATE_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    validated: bool
    date_validated: _timestamp_pb2.Timestamp
    def __init__(self, validated: bool = ..., date_validated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteCustomUnsubscribeLinkReq(_message.Message):
    __slots__ = ("custom_unsubscribe_link_sid",)
    CUSTOM_UNSUBSCRIBE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    custom_unsubscribe_link_sid: int
    def __init__(self, custom_unsubscribe_link_sid: _Optional[int] = ...) -> None: ...

class PauseCampaignReq(_message.Message):
    __slots__ = ("campaign_sid", "channel_type", "campaign_direction")
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.OmniCampaignDirection
    def __init__(self, campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.OmniCampaignDirection, str]] = ...) -> None: ...

class PauseCampaignRes(_message.Message):
    __slots__ = ("reference_id",)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    def __init__(self, reference_id: _Optional[str] = ...) -> None: ...

class ResumeCampaignReq(_message.Message):
    __slots__ = ("campaign_sid", "channel_type", "campaign_direction")
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.OmniCampaignDirection
    def __init__(self, campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.OmniCampaignDirection, str]] = ...) -> None: ...

class ResumeCampaignRes(_message.Message):
    __slots__ = ("reference_id",)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    def __init__(self, reference_id: _Optional[str] = ...) -> None: ...

class ArchiveCampaignReq(_message.Message):
    __slots__ = ("campaign_sid", "channel_type", "campaign_direction")
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.OmniCampaignDirection
    def __init__(self, campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.OmniCampaignDirection, str]] = ...) -> None: ...

class ArchiveCampaignRes(_message.Message):
    __slots__ = ("reference_id",)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    def __init__(self, reference_id: _Optional[str] = ...) -> None: ...

class UpdateCampaignPacingSpeedReq(_message.Message):
    __slots__ = ("campaign_sid", "channel_type", "campaign_direction", "sends_per_hour", "campaign_module_sid")
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SENDS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    channel_type: _omnichannel_pb2.ChannelType
    campaign_direction: _omnichannel_pb2.OmniCampaignDirection
    sends_per_hour: int
    campaign_module_sid: int
    def __init__(self, campaign_sid: _Optional[int] = ..., channel_type: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., campaign_direction: _Optional[_Union[_omnichannel_pb2.OmniCampaignDirection, str]] = ..., sends_per_hour: _Optional[int] = ..., campaign_module_sid: _Optional[int] = ...) -> None: ...

class UpdateCampaignPacingSpeedRes(_message.Message):
    __slots__ = ("reference_id",)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    def __init__(self, reference_id: _Optional[str] = ...) -> None: ...

class ListContactListsReq(_message.Message):
    __slots__ = ("field_mask", "by_project")
    class ByProject(_message.Message):
        __slots__ = ("project_sid",)
        PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
        project_sid: int
        def __init__(self, project_sid: _Optional[int] = ...) -> None: ...
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    BY_PROJECT_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    by_project: ListContactListsReq.ByProject
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., by_project: _Optional[_Union[ListContactListsReq.ByProject, _Mapping]] = ...) -> None: ...

class ListContactListsRes(_message.Message):
    __slots__ = ("contact_lists",)
    CONTACT_LISTS_FIELD_NUMBER: _ClassVar[int]
    contact_lists: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.ContactList]
    def __init__(self, contact_lists: _Optional[_Iterable[_Union[_omnichannel_pb2.ContactList, _Mapping]]] = ...) -> None: ...

class GetAvailableHeadersReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAvailableHeadersRes(_message.Message):
    __slots__ = ("headers",)
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    headers: _containers.RepeatedCompositeFieldContainer[HeaderGroup]
    def __init__(self, headers: _Optional[_Iterable[_Union[HeaderGroup, _Mapping]]] = ...) -> None: ...

class HeaderGroup(_message.Message):
    __slots__ = ("name", "headers")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    headers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., headers: _Optional[_Iterable[str]] = ...) -> None: ...

class ApproveTaskRequest(_message.Message):
    __slots__ = ("task_sid",)
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    def __init__(self, task_sid: _Optional[int] = ...) -> None: ...

class ApproveTaskResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNextQueuedTaskRequest(_message.Message):
    __slots__ = ("skills", "agent_skills")
    class AgentSkillsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _omnichannel_pb2.OmniConversationSkills
    agent_skills: _containers.ScalarMap[str, int]
    def __init__(self, skills: _Optional[_Union[_omnichannel_pb2.OmniConversationSkills, _Mapping]] = ..., agent_skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetNextQueuedTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: _omnichannel_pb2.OmniTask
    def __init__(self, task: _Optional[_Union[_omnichannel_pb2.OmniTask, _Mapping]] = ...) -> None: ...

class GetTaskReq(_message.Message):
    __slots__ = ("field_mask", "by_conversation")
    class ByConversation(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    BY_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    by_conversation: GetTaskReq.ByConversation
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., by_conversation: _Optional[_Union[GetTaskReq.ByConversation, _Mapping]] = ...) -> None: ...

class ListTasksReq(_message.Message):
    __slots__ = ("field_mask", "by_campaign")
    class ByCampaign(_message.Message):
        __slots__ = ("campaign_sid", "page_size", "page_token")
        CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
        PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        campaign_sid: int
        page_size: int
        page_token: str
        def __init__(self, campaign_sid: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    BY_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    by_campaign: ListTasksReq.ByCampaign
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., by_campaign: _Optional[_Union[ListTasksReq.ByCampaign, _Mapping]] = ...) -> None: ...

class ListTasksRes(_message.Message):
    __slots__ = ("next_page_token", "tasks")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    tasks: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniTask]
    def __init__(self, next_page_token: _Optional[str] = ..., tasks: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniTask, _Mapping]]] = ...) -> None: ...

class RejectTaskRequest(_message.Message):
    __slots__ = ("task_sid",)
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    def __init__(self, task_sid: _Optional[int] = ...) -> None: ...

class RejectTaskResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequeueTaskRequest(_message.Message):
    __slots__ = ("task_sid",)
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    def __init__(self, task_sid: _Optional[int] = ...) -> None: ...

class RequeueTaskResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateConnectedInboxRes(_message.Message):
    __slots__ = ("connected_inbox_sid",)
    CONNECTED_INBOX_SID_FIELD_NUMBER: _ClassVar[int]
    connected_inbox_sid: int
    def __init__(self, connected_inbox_sid: _Optional[int] = ...) -> None: ...

class DeleteConnectedInboxBySidReq(_message.Message):
    __slots__ = ("connected_inbox_sid",)
    CONNECTED_INBOX_SID_FIELD_NUMBER: _ClassVar[int]
    connected_inbox_sid: int
    def __init__(self, connected_inbox_sid: _Optional[int] = ...) -> None: ...

class GetConnectedInboxBySidReq(_message.Message):
    __slots__ = ("connected_inbox_sid",)
    CONNECTED_INBOX_SID_FIELD_NUMBER: _ClassVar[int]
    connected_inbox_sid: int
    def __init__(self, connected_inbox_sid: _Optional[int] = ...) -> None: ...

class SendgridAccountByClientReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendgridAccountByClientRes(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class ListConnectedInboxesReq(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListConnectedInboxesRes(_message.Message):
    __slots__ = ("connected_inboxes",)
    class ListConnectedInbox(_message.Message):
        __slots__ = ("connected_inbox", "campaigns")
        CONNECTED_INBOX_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
        connected_inbox: _omnichannel_pb2.ConnectedInbox
        campaigns: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniCampaign]
        def __init__(self, connected_inbox: _Optional[_Union[_omnichannel_pb2.ConnectedInbox, _Mapping]] = ..., campaigns: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniCampaign, _Mapping]]] = ...) -> None: ...
    CONNECTED_INBOXES_FIELD_NUMBER: _ClassVar[int]
    connected_inboxes: _containers.RepeatedCompositeFieldContainer[ListConnectedInboxesRes.ListConnectedInbox]
    def __init__(self, connected_inboxes: _Optional[_Iterable[_Union[ListConnectedInboxesRes.ListConnectedInbox, _Mapping]]] = ...) -> None: ...

class TestConnectedInboxRes(_message.Message):
    __slots__ = ("success", "details")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    details: str
    def __init__(self, success: bool = ..., details: _Optional[str] = ...) -> None: ...

class UpdateConnectedInboxReq(_message.Message):
    __slots__ = ("connected_inbox", "field_mask")
    CONNECTED_INBOX_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    connected_inbox: _omnichannel_pb2.ConnectedInbox
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, connected_inbox: _Optional[_Union[_omnichannel_pb2.ConnectedInbox, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateVerifiedEmailRes(_message.Message):
    __slots__ = ("verified_email_sid",)
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    def __init__(self, verified_email_sid: _Optional[int] = ...) -> None: ...

class SendEmailNotificationReq(_message.Message):
    __slots__ = ("subject", "data", "message", "to_email_address_arr")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TO_EMAIL_ADDRESS_ARR_FIELD_NUMBER: _ClassVar[int]
    subject: str
    data: str
    message: str
    to_email_address_arr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subject: _Optional[str] = ..., data: _Optional[str] = ..., message: _Optional[str] = ..., to_email_address_arr: _Optional[_Iterable[str]] = ...) -> None: ...

class SendEmailNotificationRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVerifiedEmailBySidReq(_message.Message):
    __slots__ = ("verified_email_sid",)
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    def __init__(self, verified_email_sid: _Optional[int] = ...) -> None: ...

class DeleteVerifiedEmailReq(_message.Message):
    __slots__ = ("verified_email_sid",)
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    def __init__(self, verified_email_sid: _Optional[int] = ...) -> None: ...

class ListVerifiedEmailsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVerifiedEmailsRes(_message.Message):
    __slots__ = ("verified_emails",)
    VERIFIED_EMAILS_FIELD_NUMBER: _ClassVar[int]
    verified_emails: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.VerifiedEmail]
    def __init__(self, verified_emails: _Optional[_Iterable[_Union[_omnichannel_pb2.VerifiedEmail, _Mapping]]] = ...) -> None: ...

class ResendVerifiedEmailReq(_message.Message):
    __slots__ = ("verified_email_sid",)
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    def __init__(self, verified_email_sid: _Optional[int] = ...) -> None: ...

class ResendVerifiedEmailRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateVerifiedEmailReq(_message.Message):
    __slots__ = ("verified_email_sid", "description")
    VERIFIED_EMAIL_SID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    verified_email_sid: int
    description: str
    def __init__(self, verified_email_sid: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class GetPendingGoogleXOAuth2DataReq(_message.Message):
    __slots__ = ("identification_token",)
    IDENTIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identification_token: str
    def __init__(self, identification_token: _Optional[str] = ...) -> None: ...

class GetPendingGoogleXOAuth2DataRes(_message.Message):
    __slots__ = ("email_address",)
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    def __init__(self, email_address: _Optional[str] = ...) -> None: ...

class SendFeedbackEmailReq(_message.Message):
    __slots__ = ("from_email", "description", "session_id", "screenshot")
    FROM_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    from_email: str
    description: str
    session_id: str
    screenshot: str
    def __init__(self, from_email: _Optional[str] = ..., description: _Optional[str] = ..., session_id: _Optional[str] = ..., screenshot: _Optional[str] = ...) -> None: ...

class SendFeedbackEmailRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOmniAttachmentReq(_message.Message):
    __slots__ = ("include_download_url", "by_omni_attachment_sid")
    class ByOmniAttachmentSid(_message.Message):
        __slots__ = ("omni_attachment_sid",)
        OMNI_ATTACHMENT_SID_FIELD_NUMBER: _ClassVar[int]
        omni_attachment_sid: int
        def __init__(self, omni_attachment_sid: _Optional[int] = ...) -> None: ...
    INCLUDE_DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    BY_OMNI_ATTACHMENT_SID_FIELD_NUMBER: _ClassVar[int]
    include_download_url: bool
    by_omni_attachment_sid: GetOmniAttachmentReq.ByOmniAttachmentSid
    def __init__(self, include_download_url: bool = ..., by_omni_attachment_sid: _Optional[_Union[GetOmniAttachmentReq.ByOmniAttachmentSid, _Mapping]] = ...) -> None: ...

class CreateTasksReq(_message.Message):
    __slots__ = ("campaign_sid", "campaign_module_sid", "contact_list_data_source")
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_MODULE_SID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    campaign_sid: int
    campaign_module_sid: int
    contact_list_data_source: ContactListDataSource
    def __init__(self, campaign_sid: _Optional[int] = ..., campaign_module_sid: _Optional[int] = ..., contact_list_data_source: _Optional[_Union[ContactListDataSource, _Mapping]] = ...) -> None: ...

class CreateTasksRes(_message.Message):
    __slots__ = ("reference_id",)
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    reference_id: str
    def __init__(self, reference_id: _Optional[str] = ...) -> None: ...

class CreateSignatureReq(_message.Message):
    __slots__ = ("signature", "name", "description")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    signature: str
    name: str
    description: str
    def __init__(self, signature: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateSignatureRes(_message.Message):
    __slots__ = ("signature",)
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: _omnichannel_pb2.Signature
    def __init__(self, signature: _Optional[_Union[_omnichannel_pb2.Signature, _Mapping]] = ...) -> None: ...

class DeleteSignatureReq(_message.Message):
    __slots__ = ("signature_sid",)
    SIGNATURE_SID_FIELD_NUMBER: _ClassVar[int]
    signature_sid: int
    def __init__(self, signature_sid: _Optional[int] = ...) -> None: ...

class DeleteSignatureRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSignaturesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSignaturesRes(_message.Message):
    __slots__ = ("signatures",)
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.Signature]
    def __init__(self, signatures: _Optional[_Iterable[_Union[_omnichannel_pb2.Signature, _Mapping]]] = ...) -> None: ...

class UpdateSignatureReq(_message.Message):
    __slots__ = ("signature", "field_mask")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    signature: _omnichannel_pb2.Signature
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, signature: _Optional[_Union[_omnichannel_pb2.Signature, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSignatureRes(_message.Message):
    __slots__ = ("signature",)
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: _omnichannel_pb2.Signature
    def __init__(self, signature: _Optional[_Union[_omnichannel_pb2.Signature, _Mapping]] = ...) -> None: ...

class CreateProjectReq(_message.Message):
    __slots__ = ("name", "description", "compliance_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    compliance_config: _omnichannel_pb2.OmniProjectComplianceConfig
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., compliance_config: _Optional[_Union[_omnichannel_pb2.OmniProjectComplianceConfig, _Mapping]] = ...) -> None: ...

class CreateProjectRes(_message.Message):
    __slots__ = ("project", "reference_id")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    project: Project
    reference_id: str
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ("project_sid", "name", "description", "status", "date_created", "compliance_config")
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    project_sid: int
    name: str
    description: str
    status: _omnichannel_pb2.ProjectStatus
    date_created: _timestamp_pb2.Timestamp
    compliance_config: _omnichannel_pb2.OmniProjectComplianceConfig
    def __init__(self, project_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[_omnichannel_pb2.ProjectStatus, str]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., compliance_config: _Optional[_Union[_omnichannel_pb2.OmniProjectComplianceConfig, _Mapping]] = ...) -> None: ...

class ListProjectsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProjectsRes(_message.Message):
    __slots__ = ("projects",)
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[Project]
    def __init__(self, projects: _Optional[_Iterable[_Union[Project, _Mapping]]] = ...) -> None: ...

class EditProjectByIdReq(_message.Message):
    __slots__ = ("project", "field_mask")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    project: Project
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class EditProjectByIdRes(_message.Message):
    __slots__ = ("project", "reference_id")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    project: Project
    reference_id: str
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ..., reference_id: _Optional[str] = ...) -> None: ...

class CloseProjectByIdReq(_message.Message):
    __slots__ = ("project_sid",)
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    project_sid: int
    def __init__(self, project_sid: _Optional[int] = ...) -> None: ...

class CloseProjectByIdRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetProjectByIdReq(_message.Message):
    __slots__ = ("project_sid",)
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    project_sid: int
    def __init__(self, project_sid: _Optional[int] = ...) -> None: ...

class CreateCannedMessageReq(_message.Message):
    __slots__ = ("name", "description", "message_body", "canned_message_group_id", "allows_html", "attachments")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_HTML_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    message_body: str
    canned_message_group_id: str
    allows_html: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniAttachment]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., message_body: _Optional[str] = ..., canned_message_group_id: _Optional[str] = ..., allows_html: bool = ..., attachments: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniAttachment, _Mapping]]] = ...) -> None: ...

class CannedMessage(_message.Message):
    __slots__ = ("canned_message_id", "name", "description", "message_body", "date_created", "last_updated", "canned_message_group_id", "allows_html", "attachments")
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_HTML_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    name: str
    description: str
    message_body: str
    date_created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    canned_message_group_id: str
    allows_html: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniAttachment]
    def __init__(self, canned_message_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., message_body: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., canned_message_group_id: _Optional[str] = ..., allows_html: bool = ..., attachments: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniAttachment, _Mapping]]] = ...) -> None: ...

class ListCannedMessagesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCannedMessagesRes(_message.Message):
    __slots__ = ("canned_messages_with_group",)
    CANNED_MESSAGES_WITH_GROUP_FIELD_NUMBER: _ClassVar[int]
    canned_messages_with_group: _containers.RepeatedCompositeFieldContainer[CannedMessageWithGroup]
    def __init__(self, canned_messages_with_group: _Optional[_Iterable[_Union[CannedMessageWithGroup, _Mapping]]] = ...) -> None: ...

class UpdateCannedMessageReq(_message.Message):
    __slots__ = ("canned_message_id", "name", "description", "message_body", "canned_message_group_id", "allows_html", "attachments")
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_HTML_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    name: str
    description: str
    message_body: str
    canned_message_group_id: str
    allows_html: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniAttachment]
    def __init__(self, canned_message_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., message_body: _Optional[str] = ..., canned_message_group_id: _Optional[str] = ..., allows_html: bool = ..., attachments: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniAttachment, _Mapping]]] = ...) -> None: ...

class GetCannedMessageByIdReq(_message.Message):
    __slots__ = ("canned_message_id",)
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    def __init__(self, canned_message_id: _Optional[str] = ...) -> None: ...

class DeleteCannedMessageByIdReq(_message.Message):
    __slots__ = ("canned_message_id",)
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    def __init__(self, canned_message_id: _Optional[str] = ...) -> None: ...

class DeleteCannedMessageByIdRes(_message.Message):
    __slots__ = ("Result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    Result: bool
    def __init__(self, Result: bool = ...) -> None: ...

class CreateCannedMessageGroupReq(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CannedMessageGroup(_message.Message):
    __slots__ = ("canned_message_group_id", "name", "description", "date_created", "last_updated")
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    canned_message_group_id: str
    name: str
    description: str
    date_created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, canned_message_group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CannedMessageWithGroup(_message.Message):
    __slots__ = ("canned_message_id", "name", "description", "message_body", "date_created", "last_updated", "canned_message_group_id", "group_name", "group_description", "group_date_created", "group_last_updated", "allows_html", "attachments")
    CANNED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BODY_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    GROUP_LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_HTML_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    canned_message_id: str
    name: str
    description: str
    message_body: str
    date_created: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    canned_message_group_id: str
    group_name: str
    group_description: str
    group_date_created: _timestamp_pb2.Timestamp
    group_last_updated: _timestamp_pb2.Timestamp
    allows_html: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.OmniAttachment]
    def __init__(self, canned_message_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., message_body: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., canned_message_group_id: _Optional[str] = ..., group_name: _Optional[str] = ..., group_description: _Optional[str] = ..., group_date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., group_last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allows_html: bool = ..., attachments: _Optional[_Iterable[_Union[_omnichannel_pb2.OmniAttachment, _Mapping]]] = ...) -> None: ...

class ListCannedMessageGroupsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCannedMessageGroupsRes(_message.Message):
    __slots__ = ("canned_message_groups",)
    CANNED_MESSAGE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    canned_message_groups: _containers.RepeatedCompositeFieldContainer[CannedMessageGroup]
    def __init__(self, canned_message_groups: _Optional[_Iterable[_Union[CannedMessageGroup, _Mapping]]] = ...) -> None: ...

class UpdateCannedMessageGroupReq(_message.Message):
    __slots__ = ("canned_message_group_id", "name", "description")
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    canned_message_group_id: str
    name: str
    description: str
    def __init__(self, canned_message_group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateCannedMessageGroupRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCannedMessageGroupReq(_message.Message):
    __slots__ = ("canned_message_group_id",)
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_group_id: str
    def __init__(self, canned_message_group_id: _Optional[str] = ...) -> None: ...

class DeleteCannedMessageGroupRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCannedMessagesByGroupIdReq(_message.Message):
    __slots__ = ("canned_message_group_id",)
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_group_id: str
    def __init__(self, canned_message_group_id: _Optional[str] = ...) -> None: ...

class ListCannedMessagesByGroupIdRes(_message.Message):
    __slots__ = ("canned_messages_with_group",)
    CANNED_MESSAGES_WITH_GROUP_FIELD_NUMBER: _ClassVar[int]
    canned_messages_with_group: _containers.RepeatedCompositeFieldContainer[CannedMessageWithGroup]
    def __init__(self, canned_messages_with_group: _Optional[_Iterable[_Union[CannedMessageWithGroup, _Mapping]]] = ...) -> None: ...

class GetCannedMessageGroupByIdReq(_message.Message):
    __slots__ = ("canned_message_group_id",)
    CANNED_MESSAGE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    canned_message_group_id: str
    def __init__(self, canned_message_group_id: _Optional[str] = ...) -> None: ...

class ListUserSkillsReq(_message.Message):
    __slots__ = ("type_filters",)
    TYPE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    type_filters: _containers.RepeatedScalarFieldContainer[_wfm_pb2.SkillType.Enum]
    def __init__(self, type_filters: _Optional[_Iterable[_Union[_wfm_pb2.SkillType.Enum, str]]] = ...) -> None: ...

class ListUserSkillsRes(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[OmniSkill]
    def __init__(self, skills: _Optional[_Iterable[_Union[OmniSkill, _Mapping]]] = ...) -> None: ...

class OmniSkill(_message.Message):
    __slots__ = ("region", "p3_id", "name", "description", "type")
    REGION_FIELD_NUMBER: _ClassVar[int]
    P3_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    region: str
    p3_id: str
    name: str
    description: str
    type: _wfm_pb2.SkillType.Enum
    def __init__(self, region: _Optional[str] = ..., p3_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_wfm_pb2.SkillType.Enum, str]] = ...) -> None: ...
