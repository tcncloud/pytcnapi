from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMessageSenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_MESSAGE_SENDER_TYPE_AGENT: _ClassVar[ChatMessageSenderType]
    CHAT_MESSAGE_SENDER_TYPE_CUSTOMER: _ClassVar[ChatMessageSenderType]
    CHAT_MESSAGE_SENDER_TYPE_MANAGER: _ClassVar[ChatMessageSenderType]

class ChatCampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_CAMPAIGN_UNKNOWN: _ClassVar[ChatCampaignStatus]
    CHAT_CAMPAIGN_RUNNING: _ClassVar[ChatCampaignStatus]
    CHAT_CAMPAIGN_STOPPED: _ClassVar[ChatCampaignStatus]
    CHAT_CAMPAIGN_ARCHIVED: _ClassVar[ChatCampaignStatus]
    CHAT_CAMPAIGN_PAUSED: _ClassVar[ChatCampaignStatus]

class ChatCampaignEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_CAMPAIGN_EVENT_UNKNOWN: _ClassVar[ChatCampaignEvent]
    CHAT_CAMPAIGN_EVENT_SCHEDULED: _ClassVar[ChatCampaignEvent]
    CHAT_CAMPAIGN_EVENT_STOPPED: _ClassVar[ChatCampaignEvent]
    CHAT_CAMPAIGN_EVENT_ARCHIVED: _ClassVar[ChatCampaignEvent]
    CHAT_CAMPAIGN_EVENT_PAUSED: _ClassVar[ChatCampaignEvent]

class ChatMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAT_REPLY_FROM_CUSTOMER: _ClassVar[ChatMessageType]
    CHAT_REPLY_FROM_AGENT: _ClassVar[ChatMessageType]
CHAT_MESSAGE_SENDER_TYPE_AGENT: ChatMessageSenderType
CHAT_MESSAGE_SENDER_TYPE_CUSTOMER: ChatMessageSenderType
CHAT_MESSAGE_SENDER_TYPE_MANAGER: ChatMessageSenderType
CHAT_CAMPAIGN_UNKNOWN: ChatCampaignStatus
CHAT_CAMPAIGN_RUNNING: ChatCampaignStatus
CHAT_CAMPAIGN_STOPPED: ChatCampaignStatus
CHAT_CAMPAIGN_ARCHIVED: ChatCampaignStatus
CHAT_CAMPAIGN_PAUSED: ChatCampaignStatus
CHAT_CAMPAIGN_EVENT_UNKNOWN: ChatCampaignEvent
CHAT_CAMPAIGN_EVENT_SCHEDULED: ChatCampaignEvent
CHAT_CAMPAIGN_EVENT_STOPPED: ChatCampaignEvent
CHAT_CAMPAIGN_EVENT_ARCHIVED: ChatCampaignEvent
CHAT_CAMPAIGN_EVENT_PAUSED: ChatCampaignEvent
CHAT_REPLY_FROM_CUSTOMER: ChatMessageType
CHAT_REPLY_FROM_AGENT: ChatMessageType

class ChatColorProperties(_message.Message):
    __slots__ = ("primary_color", "header_text_color", "paragraph_text_color")
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPH_TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    primary_color: str
    header_text_color: str
    paragraph_text_color: str
    def __init__(self, primary_color: _Optional[str] = ..., header_text_color: _Optional[str] = ..., paragraph_text_color: _Optional[str] = ...) -> None: ...

class ChatHeader(_message.Message):
    __slots__ = ("header", "subheader")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SUBHEADER_FIELD_NUMBER: _ClassVar[int]
    header: str
    subheader: str
    def __init__(self, header: _Optional[str] = ..., subheader: _Optional[str] = ...) -> None: ...

class HoursOfOperation(_message.Message):
    __slots__ = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    MONDAY_FIELD_NUMBER: _ClassVar[int]
    TUESDAY_FIELD_NUMBER: _ClassVar[int]
    WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    THURSDAY_FIELD_NUMBER: _ClassVar[int]
    FRIDAY_FIELD_NUMBER: _ClassVar[int]
    SATURDAY_FIELD_NUMBER: _ClassVar[int]
    SUNDAY_FIELD_NUMBER: _ClassVar[int]
    monday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    tuesday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    wednesday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    thursday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    friday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    saturday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    sunday: _containers.RepeatedCompositeFieldContainer[HoursOfOperationRange]
    def __init__(self, monday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., tuesday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., wednesday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., thursday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., friday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., saturday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ..., sunday: _Optional[_Iterable[_Union[HoursOfOperationRange, _Mapping]]] = ...) -> None: ...

class HoursOfOperationRange(_message.Message):
    __slots__ = ("start_hour", "start_minute", "end_hour", "end_minute")
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    def __init__(self, start_hour: _Optional[int] = ..., start_minute: _Optional[int] = ..., end_hour: _Optional[int] = ..., end_minute: _Optional[int] = ...) -> None: ...
