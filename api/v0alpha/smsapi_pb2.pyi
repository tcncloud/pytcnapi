import datetime

from annotations import authz_pb2 as _authz_pb2
from api.commons import sms_pb2 as _sms_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSmsTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmsTemplatesRes(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    sms_template_with_intents: _containers.RepeatedCompositeFieldContainer[SmsTemplateWithIntents]
    def __init__(self, sms_template_with_intents: _Optional[_Iterable[_Union[SmsTemplateWithIntents, _Mapping]]] = ...) -> None: ...

class SmsTemplateWithIntents(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    sms_template: SmsTemplate
    sms_intent_templates: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, sms_template: _Optional[_Union[SmsTemplate, _Mapping]] = ..., sms_intent_templates: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class SmsTemplate(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    message: str
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, sms_template_sid: _Optional[int] = ..., message: _Optional[str] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateSmsTemplateReq(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    message: str
    sms_intent_template_sid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, message: _Optional[str] = ..., sms_intent_template_sid: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateSmsTemplateRes(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    def __init__(self, sms_template_sid: _Optional[int] = ...) -> None: ...

class UpdateSmsTemplateReq(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    message: str
    sms_intent_template_sid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sms_template_sid: _Optional[int] = ..., message: _Optional[str] = ..., sms_intent_template_sid: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateSmsTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteSmsTemplateReq(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    def __init__(self, sms_template_sid: _Optional[int] = ...) -> None: ...

class DeleteSmsTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class GetSmsTemplateBySidReq(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    def __init__(self, sms_template_sid: _Optional[int] = ...) -> None: ...

class GetSmsTemplateBySidRes(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    sms_template: SmsTemplate
    sms_intent_templates: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, sms_template: _Optional[_Union[SmsTemplate, _Mapping]] = ..., sms_intent_templates: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class SmsIntentTemplate(_message.Message):
    __slots__ = ()
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTION_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    sms_intent_template_sid: int
    name: str
    description: str
    action_key: str
    action_detail: str
    action_trigger: str
    priority: int
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, sms_intent_template_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., action_key: _Optional[str] = ..., action_detail: _Optional[str] = ..., action_trigger: _Optional[str] = ..., priority: _Optional[int] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSmsIntentTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmsIntentTemplatesRes(_message.Message):
    __slots__ = ()
    SMS_INTENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    sms_intent_template: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, sms_intent_template: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class UpdateSmsIntentTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteSmsIntentTemplateReq(_message.Message):
    __slots__ = ()
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_intent_template_sid: int
    def __init__(self, sms_intent_template_sid: _Optional[int] = ...) -> None: ...

class DeleteSmsIntentTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class CreateSmsIntentTemplateRes(_message.Message):
    __slots__ = ()
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_intent_template_sid: int
    def __init__(self, sms_intent_template_sid: _Optional[int] = ...) -> None: ...

class GetSmsIntentTemplateBySidReq(_message.Message):
    __slots__ = ()
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_intent_template_sid: int
    def __init__(self, sms_intent_template_sid: _Optional[int] = ...) -> None: ...

class SmsNumbers(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    IVR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ISTOLLFREE_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    country_sid: int
    number: str
    provider_name: str
    notes: str
    ivr_reference: _wrappers_pb2.StringValue
    client_name: str
    isTollFree: bool
    src_number_type: str
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, sms_number_sid: _Optional[int] = ..., country_sid: _Optional[int] = ..., number: _Optional[str] = ..., provider_name: _Optional[str] = ..., notes: _Optional[str] = ..., ivr_reference: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., client_name: _Optional[str] = ..., isTollFree: _Optional[bool] = ..., src_number_type: _Optional[str] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSmsSourceNumbersReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmsSourceNumbersRes(_message.Message):
    __slots__ = ()
    SMS_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    sms_numbers: _containers.RepeatedCompositeFieldContainer[SmsNumbers]
    def __init__(self, sms_numbers: _Optional[_Iterable[_Union[SmsNumbers, _Mapping]]] = ...) -> None: ...

class UpdateSmsSourceNumberReq(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    IVR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    country_sid: int
    number: str
    provider_name: str
    notes: str
    ivr_reference: str
    src_number_type: str
    def __init__(self, sms_number_sid: _Optional[int] = ..., country_sid: _Optional[int] = ..., number: _Optional[str] = ..., provider_name: _Optional[str] = ..., notes: _Optional[str] = ..., ivr_reference: _Optional[str] = ..., src_number_type: _Optional[str] = ...) -> None: ...

class UpdateSmsSourceNumberRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteSmsSourceNumberReq(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    def __init__(self, sms_number_sid: _Optional[int] = ...) -> None: ...

class DeleteSmsSourceNumberRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class CreateSmsSourceNumberReq(_message.Message):
    __slots__ = ()
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    IVR_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    country_sid: int
    number: str
    provider_name: str
    notes: str
    ivr_reference: str
    src_number_type: str
    def __init__(self, country_sid: _Optional[int] = ..., number: _Optional[str] = ..., provider_name: _Optional[str] = ..., notes: _Optional[str] = ..., ivr_reference: _Optional[str] = ..., src_number_type: _Optional[str] = ...) -> None: ...

class CreateSmsSourceNumberRes(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    def __init__(self, sms_number_sid: _Optional[int] = ...) -> None: ...

class GetSmsSourceNumberBySidReq(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    def __init__(self, sms_number_sid: _Optional[int] = ...) -> None: ...

class SendSmsNotificationReq(_message.Message):
    __slots__ = ()
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TO_PHONE_NUM_ARR_FIELD_NUMBER: _ClassVar[int]
    message: str
    to_phone_num_arr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message: _Optional[str] = ..., to_phone_num_arr: _Optional[_Iterable[str]] = ...) -> None: ...

class SendSmsNotificationRes(_message.Message):
    __slots__ = ()
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class ListSmsGroupByFiltersReq(_message.Message):
    __slots__ = ()
    SEARCH_FROM_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    search_from: _timestamp_pb2.Timestamp
    search_to: _timestamp_pb2.Timestamp
    status: str
    name: str
    def __init__(self, search_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., search_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SmsGroupWithIntents(_message.Message):
    __slots__ = ()
    SMS_GROUP_INFO_RES_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SMS_MAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    sms_group_info_res: SmsGroupInfo
    sms_intent_groups: _containers.RepeatedCompositeFieldContainer[SmsIntentGroup]
    sms_mam_settings: SmsMamSettings
    def __init__(self, sms_group_info_res: _Optional[_Union[SmsGroupInfo, _Mapping]] = ..., sms_intent_groups: _Optional[_Iterable[_Union[SmsIntentGroup, _Mapping]]] = ..., sms_mam_settings: _Optional[_Union[SmsMamSettings, _Mapping]] = ...) -> None: ...

class ListSmsGroupByFiltersRes(_message.Message):
    __slots__ = ()
    SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[SmsGroupWithIntents]
    def __init__(self, sms_group_with_intents: _Optional[_Iterable[_Union[SmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class ListSmsGroupsByGroupSidsReq(_message.Message):
    __slots__ = ()
    SMS_GROUP_SIDS_ARR_FIELD_NUMBER: _ClassVar[int]
    sms_group_sids_arr: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sms_group_sids_arr: _Optional[_Iterable[int]] = ...) -> None: ...

class ListSmsGroupsByGroupSidsRes(_message.Message):
    __slots__ = ()
    SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[SmsGroupWithIntents]
    def __init__(self, sms_group_with_intents: _Optional[_Iterable[_Union[SmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class SmsGroupInfo(_message.Message):
    __slots__ = ()
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    SENDS_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_SID_STR_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUM_COL_FIELD_NUMBER: _ClassVar[int]
    USE_TZ_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TODAYS_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    sms_group_sid: int
    country_sid: int
    sms_message_sid: int
    name: str
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    sends_per_minute: int
    status: int
    total_cost: float
    caller_ids: _containers.RepeatedScalarFieldContainer[str]
    client_name: str
    total_scheduled: int
    total_completed: int
    contact_group_sid_str: _wrappers_pb2.StringValue
    contact_group_sid: int
    phone_num_col: _wrappers_pb2.StringValue
    use_tz_restrictions: _wrappers_pb2.StringValue
    message_count: int
    todays_message_count: int
    date_created: _timestamp_pb2.Timestamp
    def __init__(self, sms_group_sid: _Optional[int] = ..., country_sid: _Optional[int] = ..., sms_message_sid: _Optional[int] = ..., name: _Optional[str] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sends_per_minute: _Optional[int] = ..., status: _Optional[int] = ..., total_cost: _Optional[float] = ..., caller_ids: _Optional[_Iterable[str]] = ..., client_name: _Optional[str] = ..., total_scheduled: _Optional[int] = ..., total_completed: _Optional[int] = ..., contact_group_sid_str: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., contact_group_sid: _Optional[int] = ..., phone_num_col: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., use_tz_restrictions: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., message_count: _Optional[int] = ..., todays_message_count: _Optional[int] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSmsTasksByGroupSidsReq(_message.Message):
    __slots__ = ()
    SMS_GROUP_SIDS_ARR_FIELD_NUMBER: _ClassVar[int]
    sms_group_sids_arr: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sms_group_sids_arr: _Optional[_Iterable[int]] = ...) -> None: ...

class ListSmsTasksByGroupSidsRes(_message.Message):
    __slots__ = ()
    SMS_TASK_INFO_WITH_REPLY_FIELD_NUMBER: _ClassVar[int]
    sms_task_info_with_reply: _containers.RepeatedCompositeFieldContainer[SmsTaskInfoWithReply]
    def __init__(self, sms_task_info_with_reply: _Optional[_Iterable[_Union[SmsTaskInfoWithReply, _Mapping]]] = ...) -> None: ...

class ListSmsTasksWithDetailedStatusReq(_message.Message):
    __slots__ = ()
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    sms_group_sid: int
    def __init__(self, sms_group_sid: _Optional[int] = ...) -> None: ...

class ListSmsTasksWithDetailedStatusRes(_message.Message):
    __slots__ = ()
    SMS_TASK_INFO_WITH_REPLY_FIELD_NUMBER: _ClassVar[int]
    sms_task_info_with_reply: _containers.RepeatedCompositeFieldContainer[SmsTaskInfoWithReply]
    def __init__(self, sms_task_info_with_reply: _Optional[_Iterable[_Union[SmsTaskInfoWithReply, _Mapping]]] = ...) -> None: ...

class SmsTaskInfoWithReply(_message.Message):
    __slots__ = ()
    SMS_TASK_INFO_RES_FIELD_NUMBER: _ClassVar[int]
    SMS_RECEIVED_REPLIES_FIELD_NUMBER: _ClassVar[int]
    sms_task_info_res: SmsTaskInfoRes
    sms_received_replies: _containers.RepeatedCompositeFieldContainer[SmsReceivedReplies]
    def __init__(self, sms_task_info_res: _Optional[_Union[SmsTaskInfoRes, _Mapping]] = ..., sms_received_replies: _Optional[_Iterable[_Union[SmsReceivedReplies, _Mapping]]] = ...) -> None: ...

class SmsTaskInfoRes(_message.Message):
    __slots__ = ()
    SMS_TASK_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    MSG_UUID_FIELD_NUMBER: _ClassVar[int]
    MSG_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUM_COL_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_PARENT_FIELD_NUMBER: _ClassVar[int]
    MAM_AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    sms_task_sid: int
    sms_group_sid: int
    delivery_status: int
    delivery_status_message: str
    data: str
    cost: float
    msg_uuid: _wrappers_pb2.StringValue
    msg_time: _timestamp_pb2.Timestamp
    status: int
    phone_num_col: _wrappers_pb2.StringValue
    units: int
    sms_task_parent: _wrappers_pb2.Int64Value
    mam_agent_response: MamAgentResponse
    def __init__(self, sms_task_sid: _Optional[int] = ..., sms_group_sid: _Optional[int] = ..., delivery_status: _Optional[int] = ..., delivery_status_message: _Optional[str] = ..., data: _Optional[str] = ..., cost: _Optional[float] = ..., msg_uuid: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., msg_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[int] = ..., phone_num_col: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., units: _Optional[int] = ..., sms_task_parent: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., mam_agent_response: _Optional[_Union[MamAgentResponse, _Mapping]] = ...) -> None: ...

class SmsReceivedReplies(_message.Message):
    __slots__ = ()
    SMS_RECEIVED_REPLIES_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_SID_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MSG_UUID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_REPLY_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_REPORT_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    sms_received_replies_sid: int
    sms_task_sid: int
    src_number: str
    dst_number: str
    msg_uuid: str
    received_reply: str
    received_time: _timestamp_pb2.Timestamp
    analysis_report: str
    inbound_sms_group_id: str
    cost: float
    status: _sms_pb2.SMSIBTaskStatus
    units: int
    def __init__(self, sms_received_replies_sid: _Optional[int] = ..., sms_task_sid: _Optional[int] = ..., src_number: _Optional[str] = ..., dst_number: _Optional[str] = ..., msg_uuid: _Optional[str] = ..., received_reply: _Optional[str] = ..., received_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., analysis_report: _Optional[str] = ..., inbound_sms_group_id: _Optional[str] = ..., cost: _Optional[float] = ..., status: _Optional[_Union[_sms_pb2.SMSIBTaskStatus, str]] = ..., units: _Optional[int] = ...) -> None: ...

class UpdateSmsGroupRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class ScheduleSmsReq(_message.Message):
    __slots__ = ()
    SMS_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_PACE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_PHONE_COL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_MAM_HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    sms_template_sid: int
    initial_pace: int
    selected_phone_col: str
    source_number: str
    country_sid: int
    timezone_restrictions: bool
    group_name: str
    contact_group_sid: int
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    selected_mam_hunt_group: str
    def __init__(self, sms_template_sid: _Optional[int] = ..., initial_pace: _Optional[int] = ..., selected_phone_col: _Optional[str] = ..., source_number: _Optional[str] = ..., country_sid: _Optional[int] = ..., timezone_restrictions: _Optional[bool] = ..., group_name: _Optional[str] = ..., contact_group_sid: _Optional[int] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., selected_mam_hunt_group: _Optional[str] = ...) -> None: ...

class ScheduleSmsRes(_message.Message):
    __slots__ = ()
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    sms_group_sid: int
    def __init__(self, sms_group_sid: _Optional[int] = ...) -> None: ...

class ResendUnconnectedSmsReq(_message.Message):
    __slots__ = ()
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    sms_group_sid: int
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    def __init__(self, sms_group_sid: _Optional[int] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ResendUnconnectedSmsRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class SmsActivitySearchReq(_message.Message):
    __slots__ = ()
    TO_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    TO_DATE_FIELD_NUMBER: _ClassVar[int]
    ENTIRE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SENT_ONLY_FIELD_NUMBER: _ClassVar[int]
    to_number: str
    src_number: str
    from_date: _timestamp_pb2.Timestamp
    to_date: _timestamp_pb2.Timestamp
    entire_history: bool
    sent_only: bool
    def __init__(self, to_number: _Optional[str] = ..., src_number: _Optional[str] = ..., from_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., to_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entire_history: _Optional[bool] = ..., sent_only: _Optional[bool] = ...) -> None: ...

class SmsActivitySearchRes(_message.Message):
    __slots__ = ()
    SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_INFO_RES_FIELD_NUMBER: _ClassVar[int]
    sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[SmsGroupWithIntents]
    sms_task_info_res: _containers.RepeatedCompositeFieldContainer[SmsTaskInfoRes]
    def __init__(self, sms_group_with_intents: _Optional[_Iterable[_Union[SmsGroupWithIntents, _Mapping]]] = ..., sms_task_info_res: _Optional[_Iterable[_Union[SmsTaskInfoRes, _Mapping]]] = ...) -> None: ...

class InboundSmsTemplate(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    sms_number_sid: int
    name: str
    report_settings: ReportSettings
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, inbound_sms_template_id: _Optional[str] = ..., sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ..., last_updated: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInboundSmsTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListInboundSmsTemplatesRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_with_intents: _containers.RepeatedCompositeFieldContainer[InboundSmsTemplateWithIntents]
    def __init__(self, inbound_sms_template_with_intents: _Optional[_Iterable[_Union[InboundSmsTemplateWithIntents, _Mapping]]] = ...) -> None: ...

class InboundSmsTemplateWithIntents(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template: InboundSmsTemplate
    sms_intent_templates: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, inbound_sms_template: _Optional[_Union[InboundSmsTemplate, _Mapping]] = ..., sms_intent_templates: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class UpdateInboundSmsTemplateReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    sms_number_sid: int
    name: str
    sms_intent_template_sid: _containers.RepeatedScalarFieldContainer[int]
    report_settings: ReportSettings
    def __init__(self, inbound_sms_template_id: _Optional[str] = ..., sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., sms_intent_template_sid: _Optional[_Iterable[int]] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ...) -> None: ...

class UpdateInboundSmsTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteInboundSmsTemplateReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    def __init__(self, inbound_sms_template_id: _Optional[str] = ...) -> None: ...

class DeleteInboundSmsTemplateRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class CreateInboundSmsTemplateReq(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    name: str
    sms_intent_template_sid: _containers.RepeatedScalarFieldContainer[int]
    report_settings: ReportSettings
    def __init__(self, sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., sms_intent_template_sid: _Optional[_Iterable[int]] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ...) -> None: ...

class CreateInboundSmsTemplateRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    def __init__(self, inbound_sms_template_id: _Optional[str] = ...) -> None: ...

class GetInboundSmsTemplateByIdReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    def __init__(self, inbound_sms_template_id: _Optional[str] = ...) -> None: ...

class GetInboundSmsTemplateByIdRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template: InboundSmsTemplate
    sms_intent_templates: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, inbound_sms_template: _Optional[_Union[InboundSmsTemplate, _Mapping]] = ..., sms_intent_templates: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class InboundSmsGroupWithIntents(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_FIELD_NUMBER: _ClassVar[int]
    SMS_INTENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group: InboundSmsGroup
    sms_intent_templates: _containers.RepeatedCompositeFieldContainer[SmsIntentTemplate]
    def __init__(self, inbound_sms_group: _Optional[_Union[InboundSmsGroup, _Mapping]] = ..., sms_intent_templates: _Optional[_Iterable[_Union[SmsIntentTemplate, _Mapping]]] = ...) -> None: ...

class InboundSmsGroup(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TODAYS_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    sms_number_sid: int
    name: str
    status: _sms_pb2.SMSIBGroupStatus
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    total_cost: float
    inbound_sms_template_id: str
    message_count: int
    todays_message_count: int
    report_settings: ReportSettings
    date_created: _timestamp_pb2.Timestamp
    def __init__(self, inbound_sms_group_id: _Optional[str] = ..., sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_sms_pb2.SMSIBGroupStatus, str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_cost: _Optional[float] = ..., inbound_sms_template_id: _Optional[str] = ..., message_count: _Optional[int] = ..., todays_message_count: _Optional[int] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ..., date_created: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInboundSmsGroupsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListInboundSmsGroupsRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[InboundSmsGroupWithIntents]
    def __init__(self, inbound_sms_group_with_intents: _Optional[_Iterable[_Union[InboundSmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class UpdateInboundSmsGroupReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    sms_number_sid: int
    name: str
    status: _sms_pb2.SMSIBGroupStatus
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    total_cost: float
    inbound_sms_template_id: str
    report_settings: ReportSettings
    def __init__(self, inbound_sms_group_id: _Optional[str] = ..., sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_sms_pb2.SMSIBGroupStatus, str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_cost: _Optional[float] = ..., inbound_sms_template_id: _Optional[str] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ...) -> None: ...

class UpdateInboundSmsGroupRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteInboundSmsGroupReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    def __init__(self, inbound_sms_group_id: _Optional[str] = ...) -> None: ...

class DeleteInboundSmsGroupRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class CreateInboundSmsGroupReq(_message.Message):
    __slots__ = ()
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    sms_number_sid: int
    name: str
    status: _sms_pb2.SMSIBGroupStatus
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    total_cost: float
    inbound_sms_template_id: str
    report_settings: ReportSettings
    def __init__(self, sms_number_sid: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_sms_pb2.SMSIBGroupStatus, str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_cost: _Optional[float] = ..., inbound_sms_template_id: _Optional[str] = ..., report_settings: _Optional[_Union[ReportSettings, _Mapping]] = ...) -> None: ...

class CreateInboundSmsGroupRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    def __init__(self, inbound_sms_group_id: _Optional[str] = ...) -> None: ...

class GetInboundSmsGroupByIdReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    def __init__(self, inbound_sms_group_id: _Optional[str] = ...) -> None: ...

class GetInboundSmsGroupByIdRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_with_intents: InboundSmsGroupWithIntents
    def __init__(self, inbound_sms_group_with_intents: _Optional[_Union[InboundSmsGroupWithIntents, _Mapping]] = ...) -> None: ...

class ListActiveInboundSmsGroupsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListActiveInboundSmsGroupsRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[InboundSmsGroupWithIntents]
    def __init__(self, inbound_sms_group_with_intents: _Optional[_Iterable[_Union[InboundSmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class ListInboundSmsGroupByFiltersReq(_message.Message):
    __slots__ = ()
    SEARCH_FROM_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    search_from: _timestamp_pb2.Timestamp
    search_to: _timestamp_pb2.Timestamp
    status: str
    name: str
    def __init__(self, search_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., search_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListInboundSmsGroupByFiltersRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[InboundSmsGroupWithIntents]
    def __init__(self, inbound_sms_group_with_intents: _Optional[_Iterable[_Union[InboundSmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class ListInboundSmsGroupsByGroupIdsReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_IDS_ARR_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_ids_arr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, inbound_sms_group_ids_arr: _Optional[_Iterable[str]] = ...) -> None: ...

class ListInboundSmsGroupsByGroupIdsRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_WITH_INTENTS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_with_intents: _containers.RepeatedCompositeFieldContainer[InboundSmsGroupWithIntents]
    def __init__(self, inbound_sms_group_with_intents: _Optional[_Iterable[_Union[InboundSmsGroupWithIntents, _Mapping]]] = ...) -> None: ...

class ScheduleInboundSmsReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_template_id: str
    sms_number_sid: int
    group_name: str
    def __init__(self, inbound_sms_template_id: _Optional[str] = ..., sms_number_sid: _Optional[int] = ..., group_name: _Optional[str] = ...) -> None: ...

class ScheduleInboundSmsRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    def __init__(self, inbound_sms_group_id: _Optional[str] = ...) -> None: ...

class StopInboundSmsGroupReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    def __init__(self, inbound_sms_group_id: _Optional[str] = ...) -> None: ...

class StopInboundSmsGroupRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class SmsConversation(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    inbound_sms_group_id: str
    sms_task_parent: _wrappers_pb2.Int64Value
    created_on: _timestamp_pb2.Timestamp
    def __init__(self, sms_conversation_id: _Optional[str] = ..., inbound_sms_group_id: _Optional[str] = ..., sms_task_parent: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSmsConversationsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmsConversationsRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    sms_conversations: _containers.RepeatedCompositeFieldContainer[SmsConversation]
    def __init__(self, sms_conversations: _Optional[_Iterable[_Union[SmsConversation, _Mapping]]] = ...) -> None: ...

class UpdateSmsConversationReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_PARENT_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    inbound_sms_group_id: str
    sms_task_parent: _wrappers_pb2.Int64Value
    def __init__(self, sms_conversation_id: _Optional[str] = ..., inbound_sms_group_id: _Optional[str] = ..., sms_task_parent: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class UpdateSmsConversationRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class DeleteSmsConversationReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    def __init__(self, sms_conversation_id: _Optional[str] = ...) -> None: ...

class DeleteSmsConversationRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class CreateSmsConversationReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_PARENT_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_id: str
    sms_task_parent: _wrappers_pb2.Int64Value
    def __init__(self, inbound_sms_group_id: _Optional[str] = ..., sms_task_parent: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class CreateSmsConversationRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    def __init__(self, sms_conversation_id: _Optional[str] = ...) -> None: ...

class GetSmsConversationByIdReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    def __init__(self, sms_conversation_id: _Optional[str] = ...) -> None: ...

class GetSmsConversationByIdRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    sms_conversation: SmsConversation
    def __init__(self, sms_conversation: _Optional[_Union[SmsConversation, _Mapping]] = ...) -> None: ...

class ListSmsConversationAuditsReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    def __init__(self, sms_conversation_id: _Optional[str] = ...) -> None: ...

class ListSmsConversationAuditsRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_AUDITS_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_audits: _containers.RepeatedCompositeFieldContainer[SmsConversationAudit]
    def __init__(self, sms_conversation_audits: _Optional[_Iterable[_Union[SmsConversationAudit, _Mapping]]] = ...) -> None: ...

class CreateSmsConversationAuditRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_audit_id: str
    def __init__(self, sms_conversation_audit_id: _Optional[str] = ...) -> None: ...

class GetSmsConversationAuditByIdReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_audit_id: str
    def __init__(self, sms_conversation_audit_id: _Optional[str] = ...) -> None: ...

class GetSmsConversationAuditByIdRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_AUDIT_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_audit: SmsConversationAudit
    def __init__(self, sms_conversation_audit: _Optional[_Union[SmsConversationAudit, _Mapping]] = ...) -> None: ...

class ListSmsConversationAssignedAgentsReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    def __init__(self, sms_conversation_id: _Optional[str] = ...) -> None: ...

class ListSmsConversationAssignedAgentsRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ASSIGNED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_assigned_agents: _containers.RepeatedCompositeFieldContainer[SmsConversationAssignedAgent]
    def __init__(self, sms_conversation_assigned_agents: _Optional[_Iterable[_Union[SmsConversationAssignedAgent, _Mapping]]] = ...) -> None: ...

class CreateSmsConversationAssignedAgentRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class GetSmsConversationAssignedAgentByIdReq(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    assigned_agent_id: int
    def __init__(self, sms_conversation_id: _Optional[str] = ..., assigned_agent_id: _Optional[int] = ...) -> None: ...

class GetSmsConversationAssignedAgentByIdRes(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ASSIGNED_AGENT_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_assigned_agent: SmsConversationAssignedAgent
    def __init__(self, sms_conversation_assigned_agent: _Optional[_Union[SmsConversationAssignedAgent, _Mapping]] = ...) -> None: ...

class SmsConversationAudit(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_AUDIT_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_RECEIVED_REPLIES_SID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_audit_id: str
    sms_conversation_id: str
    sms_task_sid: int
    sms_received_replies_sid: int
    action: int
    description: str
    agent_id: int
    created_on: _timestamp_pb2.Timestamp
    def __init__(self, sms_conversation_audit_id: _Optional[str] = ..., sms_conversation_id: _Optional[str] = ..., sms_task_sid: _Optional[int] = ..., sms_received_replies_sid: _Optional[int] = ..., action: _Optional[int] = ..., description: _Optional[str] = ..., agent_id: _Optional[int] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SmsConversationAssignedAgent(_message.Message):
    __slots__ = ()
    SMS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_AGENT_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    sms_conversation_id: str
    assigned_agent_id: int
    primary_agent: bool
    notify: bool
    created_on: _timestamp_pb2.Timestamp
    def __init__(self, sms_conversation_id: _Optional[str] = ..., assigned_agent_id: _Optional[int] = ..., primary_agent: _Optional[bool] = ..., notify: _Optional[bool] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetSmsMessageReq(_message.Message):
    __slots__ = ()
    SMS_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    sms_message_sid: int
    def __init__(self, sms_message_sid: _Optional[int] = ...) -> None: ...

class GetSmsMessageRes(_message.Message):
    __slots__ = ()
    SMS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sms_message: SmsMessage
    def __init__(self, sms_message: _Optional[_Union[SmsMessage, _Mapping]] = ...) -> None: ...

class SmsMessage(_message.Message):
    __slots__ = ()
    SMS_MESSAGE_SID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sms_message_sid: int
    message: str
    def __init__(self, sms_message_sid: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class SmsIntentGroup(_message.Message):
    __slots__ = ()
    SMS_INTENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ACTION_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    sms_intent_group_sid: int
    sms_group_sid: int
    name: str
    description: str
    action_key: str
    action_detail: str
    action_trigger: str
    priority: int
    def __init__(self, sms_intent_group_sid: _Optional[int] = ..., sms_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., action_key: _Optional[str] = ..., action_detail: _Optional[str] = ..., action_trigger: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class InboundSmsTask(_message.Message):
    __slots__ = ()
    SMS_RECEIVED_REPLIES_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_REPLY_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SMS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_REPORT_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    sms_received_replies_id: int
    src_number: str
    dst_number: str
    msg_id: str
    received_reply: str
    received_time: _timestamp_pb2.Timestamp
    inbound_sms_group_id: str
    cost: float
    status: _sms_pb2.SMSIBTaskStatus
    analysis_report: str
    units: int
    def __init__(self, sms_received_replies_id: _Optional[int] = ..., src_number: _Optional[str] = ..., dst_number: _Optional[str] = ..., msg_id: _Optional[str] = ..., received_reply: _Optional[str] = ..., received_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., inbound_sms_group_id: _Optional[str] = ..., cost: _Optional[float] = ..., status: _Optional[_Union[_sms_pb2.SMSIBTaskStatus, str]] = ..., analysis_report: _Optional[str] = ..., units: _Optional[int] = ...) -> None: ...

class ListInboundSmsTasksByGroupIdsReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_IDS_ARR_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_ids_arr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, inbound_sms_group_ids_arr: _Optional[_Iterable[str]] = ...) -> None: ...

class ListInboundSmsTasksByGroupIdsRes(_message.Message):
    __slots__ = ()
    INBOUND_SMS_TASKS_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_tasks: _containers.RepeatedCompositeFieldContainer[InboundSmsTask]
    def __init__(self, inbound_sms_tasks: _Optional[_Iterable[_Union[InboundSmsTask, _Mapping]]] = ...) -> None: ...

class ReportSettings(_message.Message):
    __slots__ = ()
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    REPORT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FTP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SFTP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    delivery_method: str
    report_template_sid: int
    sms_settings: SmsSettings
    email_settings: EmailSettings
    ftp_settings: FtpSettings
    sftp_settings: SftpSettings
    def __init__(self, enabled: _Optional[bool] = ..., delivery_method: _Optional[str] = ..., report_template_sid: _Optional[int] = ..., sms_settings: _Optional[_Union[SmsSettings, _Mapping]] = ..., email_settings: _Optional[_Union[EmailSettings, _Mapping]] = ..., ftp_settings: _Optional[_Union[FtpSettings, _Mapping]] = ..., sftp_settings: _Optional[_Union[SftpSettings, _Mapping]] = ...) -> None: ...

class SmsSettings(_message.Message):
    __slots__ = ()
    PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    SRC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_numbers: _containers.RepeatedScalarFieldContainer[str]
    src_number: str
    def __init__(self, phone_numbers: _Optional[_Iterable[str]] = ..., src_number: _Optional[str] = ...) -> None: ...

class EmailSettings(_message.Message):
    __slots__ = ()
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    REPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FROM_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    report_type: str
    email_addresses: _containers.RepeatedScalarFieldContainer[str]
    report_format: str
    from_email_address: str
    def __init__(self, report_type: _Optional[str] = ..., email_addresses: _Optional[_Iterable[str]] = ..., report_format: _Optional[str] = ..., from_email_address: _Optional[str] = ...) -> None: ...

class FtpSettings(_message.Message):
    __slots__ = ()
    PASSWD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    passwd: str
    username: str
    report_format: str
    path: str
    url: str
    def __init__(self, passwd: _Optional[str] = ..., username: _Optional[str] = ..., report_format: _Optional[str] = ..., path: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class SftpSettings(_message.Message):
    __slots__ = ()
    PASSWD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    passwd: str
    username: str
    report_format: str
    path: str
    authentication_type: str
    url: str
    private_key: str
    def __init__(self, passwd: _Optional[str] = ..., username: _Optional[str] = ..., report_format: _Optional[str] = ..., path: _Optional[str] = ..., authentication_type: _Optional[str] = ..., url: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class SmsMamSettings(_message.Message):
    __slots__ = ()
    MAM_HG_SID_FIELD_NUMBER: _ClassVar[int]
    MAM_HG_NAME_FIELD_NUMBER: _ClassVar[int]
    mam_hg_sid: str
    mam_hg_name: str
    def __init__(self, mam_hg_sid: _Optional[str] = ..., mam_hg_name: _Optional[str] = ...) -> None: ...

class MamAgentResponse(_message.Message):
    __slots__ = ()
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    status: _sms_pb2.SMSMamStatus
    agent_response_time: _timestamp_pb2.Timestamp
    agent_name: str
    def __init__(self, status: _Optional[_Union[_sms_pb2.SMSMamStatus, str]] = ..., agent_response_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., agent_name: _Optional[str] = ...) -> None: ...

class StopAllOutboundSmsGroupsReq(_message.Message):
    __slots__ = ()
    SMS_GROUP_SIDS_ARR_FIELD_NUMBER: _ClassVar[int]
    sms_group_sids_arr: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sms_group_sids_arr: _Optional[_Iterable[int]] = ...) -> None: ...

class StopAllOutboundSmsGroupsRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...

class StopAllInboundSmsGroupsReq(_message.Message):
    __slots__ = ()
    INBOUND_SMS_GROUP_IDS_ARR_FIELD_NUMBER: _ClassVar[int]
    inbound_sms_group_ids_arr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, inbound_sms_group_ids_arr: _Optional[_Iterable[str]] = ...) -> None: ...

class StopAllInboundSmsGroupsRes(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: _Optional[bool] = ...) -> None: ...
