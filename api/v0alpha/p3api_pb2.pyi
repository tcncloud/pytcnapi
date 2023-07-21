from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons import broadcasts_pb2 as _broadcasts_pb2
from api.commons import call_pb2 as _call_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from api.commons import p3api_pb2 as _p3api_pb2
from api.commons import task_pb2 as _task_pb2
from api.commons import wfm_pb2 as _wfm_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAgentHuntGroupReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class HuntGroup(_message.Message):
    __slots__ = ["hunt_group_sid", "client_sid", "name", "description", "modify_date", "type", "agent_count"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODIFY_DATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    client_sid: int
    name: str
    description: _wrappers_pb2.StringValue
    modify_date: _timestamp_pb2.Timestamp
    type: _acd_pb2.HuntGroupType.Enum
    agent_count: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[_acd_pb2.HuntGroupType.Enum, str]] = ..., agent_count: _Optional[int] = ...) -> None: ...

class GetAgentSkillsReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetAgentSkillsRes(_message.Message):
    __slots__ = ["skills"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.ScalarMap[str, int]
    def __init__(self, skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class CreateAgentSkillReq(_message.Message):
    __slots__ = ["name", "description"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateAgentSkillRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAgentSkillReq(_message.Message):
    __slots__ = ["agent_skill_sid", "name", "description"]
    AGENT_SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    agent_skill_sid: int
    name: str
    description: str
    def __init__(self, agent_skill_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateAgentSkillRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAgentSkillReq(_message.Message):
    __slots__ = ["agent_skill_sid"]
    AGENT_SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    agent_skill_sid: int
    def __init__(self, agent_skill_sid: _Optional[int] = ...) -> None: ...

class DeleteAgentSkillRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAgentSkillsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAgentSkillsRes(_message.Message):
    __slots__ = ["skills"]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    def __init__(self, skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ...) -> None: ...

class ListSkillsForCurrentAgentReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListSkillsForCurrentAgentRes(_message.Message):
    __slots__ = ["skills"]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    def __init__(self, skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ...) -> None: ...

class GetAgentSessionReq(_message.Message):
    __slots__ = ["agent_session_sid"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    def __init__(self, agent_session_sid: _Optional[int] = ...) -> None: ...

class AgentSession(_message.Message):
    __slots__ = ["agent_session_sid", "web_login_time", "web_logout_time", "ivr_login_time", "ivr_logout_time", "ivr_duration", "ivr_billed_duration", "cost", "agent_sid", "status", "softphone_user", "agent_dial_in", "agent_callerid", "agent_dialed_number", "worker", "hunt_group_sid", "wait_duration", "pause_duration", "transfer_duration", "wrap_up_duration", "talk_duration", "manual_duration", "preview_duration", "hold_duration"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    WEB_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    WEB_LOGOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    IVR_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    IVR_LOGOUT_TIME_FIELD_NUMBER: _ClassVar[int]
    IVR_DURATION_FIELD_NUMBER: _ClassVar[int]
    IVR_BILLED_DURATION_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOFTPHONE_USER_FIELD_NUMBER: _ClassVar[int]
    AGENT_DIAL_IN_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALLERID_FIELD_NUMBER: _ClassVar[int]
    AGENT_DIALED_NUMBER_FIELD_NUMBER: _ClassVar[int]
    WORKER_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_DURATION_FIELD_NUMBER: _ClassVar[int]
    WRAP_UP_DURATION_FIELD_NUMBER: _ClassVar[int]
    TALK_DURATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DURATION_FIELD_NUMBER: _ClassVar[int]
    HOLD_DURATION_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    web_login_time: _timestamp_pb2.Timestamp
    web_logout_time: _timestamp_pb2.Timestamp
    ivr_login_time: _timestamp_pb2.Timestamp
    ivr_logout_time: _timestamp_pb2.Timestamp
    ivr_duration: _wrappers_pb2.Int32Value
    ivr_billed_duration: _wrappers_pb2.Int32Value
    cost: _wrappers_pb2.DoubleValue
    agent_sid: _wrappers_pb2.Int64Value
    status: _wrappers_pb2.Int32Value
    softphone_user: _wrappers_pb2.BoolValue
    agent_dial_in: _acd_pb2.AgentDialIn.Enum
    agent_callerid: _wrappers_pb2.StringValue
    agent_dialed_number: _wrappers_pb2.StringValue
    worker: _wrappers_pb2.StringValue
    hunt_group_sid: _wrappers_pb2.Int64Value
    wait_duration: _wrappers_pb2.Int32Value
    pause_duration: _wrappers_pb2.Int32Value
    transfer_duration: _wrappers_pb2.Int32Value
    wrap_up_duration: _wrappers_pb2.Int32Value
    talk_duration: _wrappers_pb2.Int32Value
    manual_duration: _wrappers_pb2.Int32Value
    preview_duration: _wrappers_pb2.Int32Value
    hold_duration: _wrappers_pb2.Int32Value
    def __init__(self, agent_session_sid: _Optional[int] = ..., web_login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., web_logout_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ivr_login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ivr_logout_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ivr_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., ivr_billed_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., cost: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., agent_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., status: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., softphone_user: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., agent_dial_in: _Optional[_Union[_acd_pb2.AgentDialIn.Enum, str]] = ..., agent_callerid: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., agent_dialed_number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., worker: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., hunt_group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., wait_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., pause_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., transfer_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., wrap_up_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., talk_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., manual_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., preview_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., hold_duration: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class GetCurrentAgentReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Agent(_message.Message):
    __slots__ = ["agent_sid", "client_sid", "agent_profile_sid", "web_login", "agent_id", "agent_pin", "add_date", "modify_date", "callback_number", "callback_extension", "hunt_group_sid", "subscriber_username", "partner_agent_id", "last_password_change_date"]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    WEB_LOGIN_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_PIN_FIELD_NUMBER: _ClassVar[int]
    ADD_DATE_FIELD_NUMBER: _ClassVar[int]
    MODIFY_DATE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PASSWORD_CHANGE_DATE_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    client_sid: int
    agent_profile_sid: int
    web_login: str
    agent_id: _wrappers_pb2.Int64Value
    agent_pin: _wrappers_pb2.Int64Value
    add_date: _timestamp_pb2.Timestamp
    modify_date: _timestamp_pb2.Timestamp
    callback_number: _wrappers_pb2.StringValue
    callback_extension: _wrappers_pb2.StringValue
    hunt_group_sid: _wrappers_pb2.Int64Value
    subscriber_username: _wrappers_pb2.StringValue
    partner_agent_id: _wrappers_pb2.StringValue
    last_password_change_date: _timestamp_pb2.Timestamp
    def __init__(self, agent_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., agent_profile_sid: _Optional[int] = ..., web_login: _Optional[str] = ..., agent_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., agent_pin: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modify_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., callback_number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., callback_extension: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., hunt_group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., subscriber_username: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., partner_agent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., last_password_change_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetClientInfoDataReq(_message.Message):
    __slots__ = ["call_sid", "call_type", "task_sid"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    task_sid: int
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., task_sid: _Optional[int] = ...) -> None: ...

class GetClientInfoDataRes(_message.Message):
    __slots__ = ["phone_number", "caller_id", "rows", "country_sid"]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    caller_id: str
    rows: _containers.RepeatedCompositeFieldContainer[_p3api_pb2.ClientInfoDataRow]
    country_sid: int
    def __init__(self, phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., rows: _Optional[_Iterable[_Union[_p3api_pb2.ClientInfoDataRow, _Mapping]]] = ..., country_sid: _Optional[int] = ...) -> None: ...

class GetClientInfoDisplayTemplateReq(_message.Message):
    __slots__ = ["call_sid", "call_type", "hunt_group_sid"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    hunt_group_sid: int
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetClientInfoDisplayTemplateRes(_message.Message):
    __slots__ = ["display_all_fields", "dialed_number_settings", "rows"]
    DISPLAY_ALL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DIALED_NUMBER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    display_all_fields: bool
    dialed_number_settings: _p3api_pb2.DialedNumberFieldSettings
    rows: _containers.RepeatedCompositeFieldContainer[_p3api_pb2.ClientInfoDisplayTemplateRow]
    def __init__(self, display_all_fields: bool = ..., dialed_number_settings: _Optional[_Union[_p3api_pb2.DialedNumberFieldSettings, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[_p3api_pb2.ClientInfoDisplayTemplateRow, _Mapping]]] = ...) -> None: ...

class ListAgentStatisticsDataReq(_message.Message):
    __slots__ = ["hunt_group_sid", "session_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    session_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class StatisticsData(_message.Message):
    __slots__ = ["agent_session_count", "ivr_duration", "agent_wait_duration", "call_wait_duration", "hold_duration", "manual_duration", "pause_duration", "preview_duration", "suspended_duration", "talk_duration", "transfer_duration", "wrap_up_duration", "agent_name", "hunt_group_name", "call_count", "web_login_time", "agent_sid", "hunt_group_sid"]
    AGENT_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    IVR_DURATION_FIELD_NUMBER: _ClassVar[int]
    AGENT_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    CALL_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    HOLD_DURATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DURATION_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_DURATION_FIELD_NUMBER: _ClassVar[int]
    TALK_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_DURATION_FIELD_NUMBER: _ClassVar[int]
    WRAP_UP_DURATION_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    WEB_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    agent_session_count: _wrappers_pb2.Int64Value
    ivr_duration: _wrappers_pb2.Int64Value
    agent_wait_duration: _wrappers_pb2.Int64Value
    call_wait_duration: _wrappers_pb2.Int64Value
    hold_duration: _wrappers_pb2.Int64Value
    manual_duration: _wrappers_pb2.Int64Value
    pause_duration: _wrappers_pb2.Int64Value
    preview_duration: _wrappers_pb2.Int64Value
    suspended_duration: _wrappers_pb2.Int64Value
    talk_duration: _wrappers_pb2.Int64Value
    transfer_duration: _wrappers_pb2.Int64Value
    wrap_up_duration: _wrappers_pb2.Int64Value
    agent_name: str
    hunt_group_name: str
    call_count: int
    web_login_time: _timestamp_pb2.Timestamp
    agent_sid: int
    hunt_group_sid: int
    def __init__(self, agent_session_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ivr_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., agent_wait_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., call_wait_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., hold_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., manual_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., pause_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., preview_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., suspended_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., talk_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., transfer_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., wrap_up_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., agent_name: _Optional[str] = ..., hunt_group_name: _Optional[str] = ..., call_count: _Optional[int] = ..., web_login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class StatisticsColumnDefinition(_message.Message):
    __slots__ = ["header_label", "statistic_id", "tool_tip"]
    HEADER_LABEL_FIELD_NUMBER: _ClassVar[int]
    STATISTIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_TIP_FIELD_NUMBER: _ClassVar[int]
    header_label: str
    statistic_id: str
    tool_tip: str
    def __init__(self, header_label: _Optional[str] = ..., statistic_id: _Optional[str] = ..., tool_tip: _Optional[str] = ...) -> None: ...

class ListAgentStatisticsDataRes(_message.Message):
    __slots__ = ["statistics_data", "shown_columns"]
    STATISTICS_DATA_FIELD_NUMBER: _ClassVar[int]
    SHOWN_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    statistics_data: _containers.RepeatedCompositeFieldContainer[StatisticsData]
    shown_columns: _containers.RepeatedCompositeFieldContainer[StatisticsColumnDefinition]
    def __init__(self, statistics_data: _Optional[_Iterable[_Union[StatisticsData, _Mapping]]] = ..., shown_columns: _Optional[_Iterable[_Union[StatisticsColumnDefinition, _Mapping]]] = ...) -> None: ...

class PhoneBook(_message.Message):
    __slots__ = ["entry_type", "entry_name", "hunt_group_sid", "phone_number", "phone_number_type", "phone_number_hidden"]
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    entry_type: str
    entry_name: str
    hunt_group_sid: _wrappers_pb2.Int64Value
    phone_number: str
    phone_number_type: _wrappers_pb2.StringValue
    phone_number_hidden: bool
    def __init__(self, entry_type: _Optional[str] = ..., entry_name: _Optional[str] = ..., hunt_group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., phone_number: _Optional[str] = ..., phone_number_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., phone_number_hidden: bool = ...) -> None: ...

class PhoneBookEntry(_message.Message):
    __slots__ = ["phone_book_sid", "entry_name", "standard", "sip_uri", "phone_number_hidden"]
    PHONE_BOOK_SID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    SIP_URI_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    phone_book_sid: int
    entry_name: str
    standard: PhoneBookStandardNumber
    sip_uri: PhoneBookSIPURI
    phone_number_hidden: bool
    def __init__(self, phone_book_sid: _Optional[int] = ..., entry_name: _Optional[str] = ..., standard: _Optional[_Union[PhoneBookStandardNumber, _Mapping]] = ..., sip_uri: _Optional[_Union[PhoneBookSIPURI, _Mapping]] = ..., phone_number_hidden: bool = ...) -> None: ...

class PhoneBookStandardNumber(_message.Message):
    __slots__ = ["phone_number", "phone_number_types", "white_list"]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_TYPES_FIELD_NUMBER: _ClassVar[int]
    WHITE_LIST_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    phone_number_types: _containers.RepeatedScalarFieldContainer[_p3api_pb2.PhoneBookPhoneNumberType]
    white_list: bool
    def __init__(self, phone_number: _Optional[str] = ..., phone_number_types: _Optional[_Iterable[_Union[_p3api_pb2.PhoneBookPhoneNumberType, str]]] = ..., white_list: bool = ...) -> None: ...

class PhoneBookSIPURI(_message.Message):
    __slots__ = ["sip_uri_left", "sip_uri_right", "sip_types"]
    SIP_URI_LEFT_FIELD_NUMBER: _ClassVar[int]
    SIP_URI_RIGHT_FIELD_NUMBER: _ClassVar[int]
    SIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    sip_uri_left: str
    sip_uri_right: str
    sip_types: _containers.RepeatedScalarFieldContainer[_p3api_pb2.PhoneBookSIPType]
    def __init__(self, sip_uri_left: _Optional[str] = ..., sip_uri_right: _Optional[str] = ..., sip_types: _Optional[_Iterable[_Union[_p3api_pb2.PhoneBookSIPType, str]]] = ...) -> None: ...

class ListClientPhoneBookEntriesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListClientPhoneBookEntriesRes(_message.Message):
    __slots__ = ["phone_book_entries", "hunt_group_sid"]
    PHONE_BOOK_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    phone_book_entries: _containers.RepeatedCompositeFieldContainer[PhoneBookEntry]
    hunt_group_sid: int
    def __init__(self, phone_book_entries: _Optional[_Iterable[_Union[PhoneBookEntry, _Mapping]]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupPhoneBookEntriesReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupPhoneBookEntriesRes(_message.Message):
    __slots__ = ["phone_book_entries", "hunt_group_sid"]
    PHONE_BOOK_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    phone_book_entries: _containers.RepeatedCompositeFieldContainer[PhoneBookEntry]
    hunt_group_sid: int
    def __init__(self, phone_book_entries: _Optional[_Iterable[_Union[PhoneBookEntry, _Mapping]]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class CreatePhoneBookEntryReq(_message.Message):
    __slots__ = ["hunt_group_sid", "entry_name", "standard", "sip_uri", "phone_number_hidden"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    SIP_URI_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    entry_name: str
    standard: PhoneBookStandardNumber
    sip_uri: PhoneBookSIPURI
    phone_number_hidden: bool
    def __init__(self, hunt_group_sid: _Optional[int] = ..., entry_name: _Optional[str] = ..., standard: _Optional[_Union[PhoneBookStandardNumber, _Mapping]] = ..., sip_uri: _Optional[_Union[PhoneBookSIPURI, _Mapping]] = ..., phone_number_hidden: bool = ...) -> None: ...

class CreatePhoneBookEntryRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdatePhoneBookEntryReq(_message.Message):
    __slots__ = ["phone_book_sid", "hunt_group_sid", "entry_name", "standard", "sip_uri", "phone_number_hidden"]
    PHONE_BOOK_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    SIP_URI_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    phone_book_sid: int
    hunt_group_sid: int
    entry_name: str
    standard: PhoneBookStandardNumber
    sip_uri: PhoneBookSIPURI
    phone_number_hidden: bool
    def __init__(self, phone_book_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., entry_name: _Optional[str] = ..., standard: _Optional[_Union[PhoneBookStandardNumber, _Mapping]] = ..., sip_uri: _Optional[_Union[PhoneBookSIPURI, _Mapping]] = ..., phone_number_hidden: bool = ...) -> None: ...

class UpdatePhoneBookEntryRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeletePhoneBookEntryReq(_message.Message):
    __slots__ = ["phone_book_sid"]
    PHONE_BOOK_SID_FIELD_NUMBER: _ClassVar[int]
    phone_book_sid: int
    def __init__(self, phone_book_sid: _Optional[int] = ...) -> None: ...

class DeletePhoneBookEntryRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPhoneBooksReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListPhoneBooksRes(_message.Message):
    __slots__ = ["caller_id_phone_books", "outbound_phone_books", "transfer_phone_books"]
    CALLER_ID_PHONE_BOOKS_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_PHONE_BOOKS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_PHONE_BOOKS_FIELD_NUMBER: _ClassVar[int]
    caller_id_phone_books: _containers.RepeatedCompositeFieldContainer[PhoneBook]
    outbound_phone_books: _containers.RepeatedCompositeFieldContainer[PhoneBook]
    transfer_phone_books: _containers.RepeatedCompositeFieldContainer[PhoneBook]
    def __init__(self, caller_id_phone_books: _Optional[_Iterable[_Union[PhoneBook, _Mapping]]] = ..., outbound_phone_books: _Optional[_Iterable[_Union[PhoneBook, _Mapping]]] = ..., transfer_phone_books: _Optional[_Iterable[_Union[PhoneBook, _Mapping]]] = ...) -> None: ...

class ListAgentTriggersReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class TriggerParameters(_message.Message):
    __slots__ = ["action_key", "action_string"]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_STRING_FIELD_NUMBER: _ClassVar[int]
    action_key: str
    action_string: str
    def __init__(self, action_key: _Optional[str] = ..., action_string: _Optional[str] = ...) -> None: ...

class TriggerDetails(_message.Message):
    __slots__ = ["trigger_name", "trigger_desc", "trigger_status", "trigger_duration", "call_types", "trigger_parameters"]
    TRIGGER_NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DESC_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DURATION_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    trigger_name: str
    trigger_desc: str
    trigger_status: int
    trigger_duration: int
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    trigger_parameters: _containers.RepeatedCompositeFieldContainer[TriggerParameters]
    def __init__(self, trigger_name: _Optional[str] = ..., trigger_desc: _Optional[str] = ..., trigger_status: _Optional[int] = ..., trigger_duration: _Optional[int] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., trigger_parameters: _Optional[_Iterable[_Union[TriggerParameters, _Mapping]]] = ...) -> None: ...

class ListAgentTriggersRes(_message.Message):
    __slots__ = ["trigger_details"]
    TRIGGER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    trigger_details: _containers.RepeatedCompositeFieldContainer[TriggerDetails]
    def __init__(self, trigger_details: _Optional[_Iterable[_Union[TriggerDetails, _Mapping]]] = ...) -> None: ...

class PBXExtension(_message.Message):
    __slots__ = ["pbx_extension_sid", "pbx_extension", "join_sid", "join_type", "email_subject", "email_body", "email_addresses", "agent_access"]
    PBX_EXTENSION_SID_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    JOIN_SID_FIELD_NUMBER: _ClassVar[int]
    JOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_BODY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    AGENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    pbx_extension_sid: int
    pbx_extension: str
    join_sid: int
    join_type: str
    email_subject: str
    email_body: str
    email_addresses: str
    agent_access: bool
    def __init__(self, pbx_extension_sid: _Optional[int] = ..., pbx_extension: _Optional[str] = ..., join_sid: _Optional[int] = ..., join_type: _Optional[str] = ..., email_subject: _Optional[str] = ..., email_body: _Optional[str] = ..., email_addresses: _Optional[str] = ..., agent_access: bool = ...) -> None: ...

class ListPBXExtensionsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPBXExtensionsRes(_message.Message):
    __slots__ = ["agent_extensions", "hunt_group_extensions"]
    class AgentExtension(_message.Message):
        __slots__ = ["pbx_extension", "greeting_location", "email", "agent_name", "has_greeting"]
        PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        GREETING_LOCATION_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
        HAS_GREETING_FIELD_NUMBER: _ClassVar[int]
        pbx_extension: str
        greeting_location: str
        email: EmailResponse
        agent_name: str
        has_greeting: bool
        def __init__(self, pbx_extension: _Optional[str] = ..., greeting_location: _Optional[str] = ..., email: _Optional[_Union[EmailResponse, _Mapping]] = ..., agent_name: _Optional[str] = ..., has_greeting: bool = ...) -> None: ...
    class HuntGroupExtension(_message.Message):
        __slots__ = ["pbx_extension", "greeting_location", "email", "hunt_group_name", "has_greeting"]
        PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        GREETING_LOCATION_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        HAS_GREETING_FIELD_NUMBER: _ClassVar[int]
        pbx_extension: str
        greeting_location: str
        email: EmailResponse
        hunt_group_name: str
        has_greeting: bool
        def __init__(self, pbx_extension: _Optional[str] = ..., greeting_location: _Optional[str] = ..., email: _Optional[_Union[EmailResponse, _Mapping]] = ..., hunt_group_name: _Optional[str] = ..., has_greeting: bool = ...) -> None: ...
    AGENT_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    agent_extensions: _containers.RepeatedCompositeFieldContainer[ListPBXExtensionsRes.AgentExtension]
    hunt_group_extensions: _containers.RepeatedCompositeFieldContainer[ListPBXExtensionsRes.HuntGroupExtension]
    def __init__(self, agent_extensions: _Optional[_Iterable[_Union[ListPBXExtensionsRes.AgentExtension, _Mapping]]] = ..., hunt_group_extensions: _Optional[_Iterable[_Union[ListPBXExtensionsRes.HuntGroupExtension, _Mapping]]] = ...) -> None: ...

class EmailResponse(_message.Message):
    __slots__ = ["subject", "body", "addresses"]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    subject: str
    body: str
    addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subject: _Optional[str] = ..., body: _Optional[str] = ..., addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class MailMergeData(_message.Message):
    __slots__ = ["call_sid", "call_type", "scheduled_callback_id"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    scheduled_callback_id: str
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., scheduled_callback_id: _Optional[str] = ...) -> None: ...

class HuntGroupResponse(_message.Message):
    __slots__ = ["hunt_group_response_sid", "hunt_group_sid", "type", "options", "name", "description", "order", "required", "default_value", "manual_dial"]
    HUNT_GROUP_RESPONSE_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
    hunt_group_response_sid: int
    hunt_group_sid: _wrappers_pb2.Int64Value
    type: _wrappers_pb2.StringValue
    options: _containers.RepeatedScalarFieldContainer[str]
    name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    order: _wrappers_pb2.Int32Value
    required: _wrappers_pb2.BoolValue
    default_value: _wrappers_pb2.StringValue
    manual_dial: ManualDialSettings
    def __init__(self, hunt_group_response_sid: _Optional[int] = ..., hunt_group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., options: _Optional[_Iterable[str]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., order: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., default_value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., manual_dial: _Optional[_Union[ManualDialSettings, _Mapping]] = ...) -> None: ...

class DNCL(_message.Message):
    __slots__ = ["country_sid", "dncl_notes", "dncl_number", "expiration_date"]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    DNCL_NOTES_FIELD_NUMBER: _ClassVar[int]
    DNCL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    country_sid: _wrappers_pb2.Int64Value
    dncl_notes: _wrappers_pb2.StringValue
    dncl_number: _wrappers_pb2.StringValue
    expiration_date: _timestamp_pb2.Timestamp
    def __init__(self, country_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., dncl_notes: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., dncl_number: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentLoggingData(_message.Message):
    __slots__ = ["call_sid", "call_type", "action_value_suffix"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_VALUE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    action_value_suffix: str
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., action_value_suffix: _Optional[str] = ...) -> None: ...

class CreateDNCLNumbersReq(_message.Message):
    __slots__ = ["dncls", "agent_logging_data"]
    DNCLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_LOGGING_DATA_FIELD_NUMBER: _ClassVar[int]
    dncls: _containers.RepeatedCompositeFieldContainer[DNCL]
    agent_logging_data: AgentLoggingData
    def __init__(self, dncls: _Optional[_Iterable[_Union[DNCL, _Mapping]]] = ..., agent_logging_data: _Optional[_Union[AgentLoggingData, _Mapping]] = ...) -> None: ...

class CreateDNCLNumbersRes(_message.Message):
    __slots__ = ["success_count", "invalid_count", "failure_count"]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    INVALID_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    invalid_count: int
    failure_count: int
    def __init__(self, success_count: _Optional[int] = ..., invalid_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...

class GetHuntGroupAgentSettingsReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class HuntGroupAgentSettings(_message.Message):
    __slots__ = ["keypad_enabled", "keypad_delimiter", "statistics", "end_call_confirmation", "pause", "hqm", "manual_dial", "transfer", "preview_dial", "phone_number_activity", "dncl", "hold", "manual_approval", "display_linkback_huntgroup", "schedule_callback", "recording", "display_phone_zip_metadata", "phone_zip_metadata_keys", "display_machine_deliver", "allow_agent_intercom", "display_data_settings", "allow_change_hunt_group", "agent_screen_recording", "inbound_compliance_metadata", "notify_queued_calls", "display_journey_retrieved_data", "limit_journey_retrieved_data", "initial_agent_status", "display_web_links", "display_skills", "interrupt_peering"]
    KEYPAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    END_CALL_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    HQM_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    DNCL_FIELD_NUMBER: _ClassVar[int]
    HOLD_FIELD_NUMBER: _ClassVar[int]
    MANUAL_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LINKBACK_HUNTGROUP_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CALLBACK_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_PHONE_ZIP_METADATA_FIELD_NUMBER: _ClassVar[int]
    PHONE_ZIP_METADATA_KEYS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MACHINE_DELIVER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AGENT_INTERCOM_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CHANGE_HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_SCREEN_RECORDING_FIELD_NUMBER: _ClassVar[int]
    INBOUND_COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_QUEUED_CALLS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_JOURNEY_RETRIEVED_DATA_FIELD_NUMBER: _ClassVar[int]
    LIMIT_JOURNEY_RETRIEVED_DATA_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_WEB_LINKS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SKILLS_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_PEERING_FIELD_NUMBER: _ClassVar[int]
    keypad_enabled: bool
    keypad_delimiter: str
    statistics: AgentStatisticsSettings
    end_call_confirmation: bool
    pause: PauseSettings
    hqm: HoldQueueMonitorSettings
    manual_dial: ManualDialSettings
    transfer: TransferSettings
    preview_dial: PreviewDialSettings
    phone_number_activity: PhoneNumberActivitySettings
    dncl: DnclSettings
    hold: AgentHoldSettings
    manual_approval: ManualApprovalSettings
    display_linkback_huntgroup: bool
    schedule_callback: ScheduleCallBackSettings
    recording: RecordingSettings
    display_phone_zip_metadata: bool
    phone_zip_metadata_keys: _containers.RepeatedScalarFieldContainer[str]
    display_machine_deliver: bool
    allow_agent_intercom: bool
    display_data_settings: DisplayDataSettings
    allow_change_hunt_group: bool
    agent_screen_recording: bool
    inbound_compliance_metadata: _containers.RepeatedCompositeFieldContainer[ComplianceMetadata]
    notify_queued_calls: bool
    display_journey_retrieved_data: bool
    limit_journey_retrieved_data: _containers.RepeatedScalarFieldContainer[str]
    initial_agent_status: int
    display_web_links: bool
    display_skills: bool
    interrupt_peering: _containers.RepeatedScalarFieldContainer[_p3api_pb2.InterruptedPeeringStatus]
    def __init__(self, keypad_enabled: bool = ..., keypad_delimiter: _Optional[str] = ..., statistics: _Optional[_Union[AgentStatisticsSettings, _Mapping]] = ..., end_call_confirmation: bool = ..., pause: _Optional[_Union[PauseSettings, _Mapping]] = ..., hqm: _Optional[_Union[HoldQueueMonitorSettings, _Mapping]] = ..., manual_dial: _Optional[_Union[ManualDialSettings, _Mapping]] = ..., transfer: _Optional[_Union[TransferSettings, _Mapping]] = ..., preview_dial: _Optional[_Union[PreviewDialSettings, _Mapping]] = ..., phone_number_activity: _Optional[_Union[PhoneNumberActivitySettings, _Mapping]] = ..., dncl: _Optional[_Union[DnclSettings, _Mapping]] = ..., hold: _Optional[_Union[AgentHoldSettings, _Mapping]] = ..., manual_approval: _Optional[_Union[ManualApprovalSettings, _Mapping]] = ..., display_linkback_huntgroup: bool = ..., schedule_callback: _Optional[_Union[ScheduleCallBackSettings, _Mapping]] = ..., recording: _Optional[_Union[RecordingSettings, _Mapping]] = ..., display_phone_zip_metadata: bool = ..., phone_zip_metadata_keys: _Optional[_Iterable[str]] = ..., display_machine_deliver: bool = ..., allow_agent_intercom: bool = ..., display_data_settings: _Optional[_Union[DisplayDataSettings, _Mapping]] = ..., allow_change_hunt_group: bool = ..., agent_screen_recording: bool = ..., inbound_compliance_metadata: _Optional[_Iterable[_Union[ComplianceMetadata, _Mapping]]] = ..., notify_queued_calls: bool = ..., display_journey_retrieved_data: bool = ..., limit_journey_retrieved_data: _Optional[_Iterable[str]] = ..., initial_agent_status: _Optional[int] = ..., display_web_links: bool = ..., display_skills: bool = ..., interrupt_peering: _Optional[_Iterable[_Union[_p3api_pb2.InterruptedPeeringStatus, str]]] = ...) -> None: ...

class AgentStatisticsSettings(_message.Message):
    __slots__ = ["show_statistics", "show_call_history", "filter_call_history"]
    class HistoryFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        TODAY: _ClassVar[AgentStatisticsSettings.HistoryFilter]
        SESSION: _ClassVar[AgentStatisticsSettings.HistoryFilter]
    TODAY: AgentStatisticsSettings.HistoryFilter
    SESSION: AgentStatisticsSettings.HistoryFilter
    SHOW_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALL_HISTORY_FIELD_NUMBER: _ClassVar[int]
    FILTER_CALL_HISTORY_FIELD_NUMBER: _ClassVar[int]
    show_statistics: bool
    show_call_history: bool
    filter_call_history: AgentStatisticsSettings.HistoryFilter
    def __init__(self, show_statistics: bool = ..., show_call_history: bool = ..., filter_call_history: _Optional[_Union[AgentStatisticsSettings.HistoryFilter, str]] = ...) -> None: ...

class PauseSettings(_message.Message):
    __slots__ = ["allow_agent_pause", "allow_agent_pause_reset", "use_agent_pause_codes", "default_agent_pause_code", "recording_pause_confirmation"]
    ALLOW_AGENT_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AGENT_PAUSE_RESET_FIELD_NUMBER: _ClassVar[int]
    USE_AGENT_PAUSE_CODES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_PAUSE_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    allow_agent_pause: bool
    allow_agent_pause_reset: bool
    use_agent_pause_codes: bool
    default_agent_pause_code: str
    recording_pause_confirmation: bool
    def __init__(self, allow_agent_pause: bool = ..., allow_agent_pause_reset: bool = ..., use_agent_pause_codes: bool = ..., default_agent_pause_code: _Optional[str] = ..., recording_pause_confirmation: bool = ...) -> None: ...

class PhoneNumberActivitySettings(_message.Message):
    __slots__ = ["allow_phone_number_activity", "allow_export_phone_number_activity", "allow_pna_recordings_download", "allow_pna_edit_responses"]
    ALLOW_PHONE_NUMBER_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXPORT_PHONE_NUMBER_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PNA_RECORDINGS_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PNA_EDIT_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    allow_phone_number_activity: bool
    allow_export_phone_number_activity: bool
    allow_pna_recordings_download: bool
    allow_pna_edit_responses: bool
    def __init__(self, allow_phone_number_activity: bool = ..., allow_export_phone_number_activity: bool = ..., allow_pna_recordings_download: bool = ..., allow_pna_edit_responses: bool = ...) -> None: ...

class PreviewDialSettings(_message.Message):
    __slots__ = ["require_confirmation", "timeout_minutes", "allow_cancel", "pause_on_cancel"]
    REQUIRE_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CANCEL_FIELD_NUMBER: _ClassVar[int]
    PAUSE_ON_CANCEL_FIELD_NUMBER: _ClassVar[int]
    require_confirmation: bool
    timeout_minutes: int
    allow_cancel: bool
    pause_on_cancel: bool
    def __init__(self, require_confirmation: bool = ..., timeout_minutes: _Optional[int] = ..., allow_cancel: bool = ..., pause_on_cancel: bool = ...) -> None: ...

class HoldQueueMonitoringAgentRouting(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[HoldQueueMonitoringAgentRouting.Enum]
        ORIGINAL_AGENT_REQUIRED: _ClassVar[HoldQueueMonitoringAgentRouting.Enum]
        ORIGINAL_AGENT_PREFERRED: _ClassVar[HoldQueueMonitoringAgentRouting.Enum]
        ANY_AGENT: _ClassVar[HoldQueueMonitoringAgentRouting.Enum]
    UNKNOWN: HoldQueueMonitoringAgentRouting.Enum
    ORIGINAL_AGENT_REQUIRED: HoldQueueMonitoringAgentRouting.Enum
    ORIGINAL_AGENT_PREFERRED: HoldQueueMonitoringAgentRouting.Enum
    ANY_AGENT: HoldQueueMonitoringAgentRouting.Enum
    def __init__(self) -> None: ...

class HoldQueueMonitorSettings(_message.Message):
    __slots__ = ["monitor", "required_group", "preferred_group", "agent_routing"]
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_GROUP_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_ROUTING_FIELD_NUMBER: _ClassVar[int]
    monitor: bool
    required_group: int
    preferred_group: int
    agent_routing: HoldQueueMonitoringAgentRouting.Enum
    def __init__(self, monitor: bool = ..., required_group: _Optional[int] = ..., preferred_group: _Optional[int] = ..., agent_routing: _Optional[_Union[HoldQueueMonitoringAgentRouting.Enum, str]] = ...) -> None: ...

class ComplianceMetadata(_message.Message):
    __slots__ = ["name", "required"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    required: bool
    def __init__(self, name: _Optional[str] = ..., required: bool = ...) -> None: ...

class ManualDialSettings(_message.Message):
    __slots__ = ["enabled", "show_outbound_phone_book", "show_caller_id_phone_book", "has_custom_caller_id", "default_caller_id", "default_country_sid", "show_country_selector", "timezone_restrictions", "scrub_cell_phones", "call_recording", "agent_override_cell", "agent_override_ccr", "agent_override_dncl", "agent_override_timezone", "use_white_list", "use_random_caller_id", "random_caller_id_bucket", "default_caller_id_country_sid", "display_caller_id_country_select", "use_caller_id_bucket", "agent_override_natural_compliance", "natural_compliance_rule_set_name", "compliance_metadata", "enable_metadata", "use_timezone_validation_zip", "enable_sip_address", "mask_manual_dial_caller_id", "enable_manual_dial_data_dip", "manual_dial_data_dip_config", "manual_dial_data_dip_result_handling", "data_dip_manual_dial_integration", "data_dip_manual_dial_integration_handling"]
    class ZipCodeValidation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        FALSE: _ClassVar[ManualDialSettings.ZipCodeValidation]
        TRUE: _ClassVar[ManualDialSettings.ZipCodeValidation]
        REQUIRED: _ClassVar[ManualDialSettings.ZipCodeValidation]
    FALSE: ManualDialSettings.ZipCodeValidation
    TRUE: ManualDialSettings.ZipCodeValidation
    REQUIRED: ManualDialSettings.ZipCodeValidation
    class DataDipManualDialIntegrationEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOW_OUTBOUND_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALLER_ID_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    HAS_CUSTOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    SHOW_COUNTRY_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    SCRUB_CELL_PHONES_FIELD_NUMBER: _ClassVar[int]
    CALL_RECORDING_FIELD_NUMBER: _ClassVar[int]
    AGENT_OVERRIDE_CELL_FIELD_NUMBER: _ClassVar[int]
    AGENT_OVERRIDE_CCR_FIELD_NUMBER: _ClassVar[int]
    AGENT_OVERRIDE_DNCL_FIELD_NUMBER: _ClassVar[int]
    AGENT_OVERRIDE_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    USE_WHITE_LIST_FIELD_NUMBER: _ClassVar[int]
    USE_RANDOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    RANDOM_CALLER_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CALLER_ID_COUNTRY_SELECT_FIELD_NUMBER: _ClassVar[int]
    USE_CALLER_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    AGENT_OVERRIDE_NATURAL_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    NATURAL_COMPLIANCE_RULE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    USE_TIMEZONE_VALIDATION_ZIP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MASK_MANUAL_DIAL_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MANUAL_DIAL_DATA_DIP_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_DATA_DIP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_DATA_DIP_RESULT_HANDLING_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_MANUAL_DIAL_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_MANUAL_DIAL_INTEGRATION_HANDLING_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    show_outbound_phone_book: bool
    show_caller_id_phone_book: bool
    has_custom_caller_id: bool
    default_caller_id: str
    default_country_sid: int
    show_country_selector: bool
    timezone_restrictions: bool
    scrub_cell_phones: bool
    call_recording: bool
    agent_override_cell: bool
    agent_override_ccr: bool
    agent_override_dncl: bool
    agent_override_timezone: bool
    use_white_list: bool
    use_random_caller_id: bool
    random_caller_id_bucket: int
    default_caller_id_country_sid: int
    display_caller_id_country_select: bool
    use_caller_id_bucket: bool
    agent_override_natural_compliance: bool
    natural_compliance_rule_set_name: str
    compliance_metadata: _containers.RepeatedCompositeFieldContainer[ComplianceMetadata]
    enable_metadata: bool
    use_timezone_validation_zip: ManualDialSettings.ZipCodeValidation
    enable_sip_address: bool
    mask_manual_dial_caller_id: bool
    enable_manual_dial_data_dip: str
    manual_dial_data_dip_config: int
    manual_dial_data_dip_result_handling: ManualDialDataDipHandling.Enum
    data_dip_manual_dial_integration: _containers.ScalarMap[str, str]
    data_dip_manual_dial_integration_handling: ManualDialDataDipHandling.Enum
    def __init__(self, enabled: bool = ..., show_outbound_phone_book: bool = ..., show_caller_id_phone_book: bool = ..., has_custom_caller_id: bool = ..., default_caller_id: _Optional[str] = ..., default_country_sid: _Optional[int] = ..., show_country_selector: bool = ..., timezone_restrictions: bool = ..., scrub_cell_phones: bool = ..., call_recording: bool = ..., agent_override_cell: bool = ..., agent_override_ccr: bool = ..., agent_override_dncl: bool = ..., agent_override_timezone: bool = ..., use_white_list: bool = ..., use_random_caller_id: bool = ..., random_caller_id_bucket: _Optional[int] = ..., default_caller_id_country_sid: _Optional[int] = ..., display_caller_id_country_select: bool = ..., use_caller_id_bucket: bool = ..., agent_override_natural_compliance: bool = ..., natural_compliance_rule_set_name: _Optional[str] = ..., compliance_metadata: _Optional[_Iterable[_Union[ComplianceMetadata, _Mapping]]] = ..., enable_metadata: bool = ..., use_timezone_validation_zip: _Optional[_Union[ManualDialSettings.ZipCodeValidation, str]] = ..., enable_sip_address: bool = ..., mask_manual_dial_caller_id: bool = ..., enable_manual_dial_data_dip: _Optional[str] = ..., manual_dial_data_dip_config: _Optional[int] = ..., manual_dial_data_dip_result_handling: _Optional[_Union[ManualDialDataDipHandling.Enum, str]] = ..., data_dip_manual_dial_integration: _Optional[_Mapping[str, str]] = ..., data_dip_manual_dial_integration_handling: _Optional[_Union[ManualDialDataDipHandling.Enum, str]] = ...) -> None: ...

class ManualDialDataDipHandling(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[ManualDialDataDipHandling.Enum]
        CANCEL: _ClassVar[ManualDialDataDipHandling.Enum]
        NOTIFY_AND_CANCEL: _ClassVar[ManualDialDataDipHandling.Enum]
        NOTIFY_AND_ALLOW_CALL: _ClassVar[ManualDialDataDipHandling.Enum]
        CALL_WITH_ORIGINAL_VALUES: _ClassVar[ManualDialDataDipHandling.Enum]
    NONE: ManualDialDataDipHandling.Enum
    CANCEL: ManualDialDataDipHandling.Enum
    NOTIFY_AND_CANCEL: ManualDialDataDipHandling.Enum
    NOTIFY_AND_ALLOW_CALL: ManualDialDataDipHandling.Enum
    CALL_WITH_ORIGINAL_VALUES: ManualDialDataDipHandling.Enum
    def __init__(self) -> None: ...

class ScrubListsAutoAdd(_message.Message):
    __slots__ = ["scrub_list", "field_id", "field_name"]
    SCRUB_LIST_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    scrub_list: str
    field_id: str
    field_name: str
    def __init__(self, scrub_list: _Optional[str] = ..., field_id: _Optional[str] = ..., field_name: _Optional[str] = ...) -> None: ...

class ScrubListsExpirationLimits(_message.Message):
    __slots__ = ["outbound_expiration_limit", "inbound_expiration_limit", "manual_dial_expiration_limit", "preview_dial_expiration_limit"]
    OUTBOUND_EXPIRATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INBOUND_EXPIRATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_EXPIRATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_EXPIRATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    outbound_expiration_limit: _containers.RepeatedScalarFieldContainer[int]
    inbound_expiration_limit: _containers.RepeatedScalarFieldContainer[int]
    manual_dial_expiration_limit: _containers.RepeatedScalarFieldContainer[int]
    preview_dial_expiration_limit: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, outbound_expiration_limit: _Optional[_Iterable[int]] = ..., inbound_expiration_limit: _Optional[_Iterable[int]] = ..., manual_dial_expiration_limit: _Optional[_Iterable[int]] = ..., preview_dial_expiration_limit: _Optional[_Iterable[int]] = ...) -> None: ...

class DnclSettings(_message.Message):
    __slots__ = ["allow_dncl_add", "manual_dial_auto_dncl_add", "preview_dial_auto_dncl_add", "agent_responses_auto_dncl_add", "default_manual_dncl_expire_hours", "default_preview_dncl_expire_hours", "default_dncl_country", "default_outbound_dncl_expire_hours", "default_inbound_dncl_expire_hours", "hunt_group_compliance_scrub_lists", "scrub_lists_auto_add_options", "display_dncl_options_in_wrapup", "allow_dncl_remove", "hunt_group_compliance_scrub_lists_removal_allowed", "scrub_lists_expiration_limits"]
    ALLOW_DNCL_ADD_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_AUTO_DNCL_ADD_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_AUTO_DNCL_ADD_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSES_AUTO_DNCL_ADD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MANUAL_DNCL_EXPIRE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PREVIEW_DNCL_EXPIRE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DNCL_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_OUTBOUND_DNCL_EXPIRE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INBOUND_DNCL_EXPIRE_HOURS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_COMPLIANCE_SCRUB_LISTS_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LISTS_AUTO_ADD_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DNCL_OPTIONS_IN_WRAPUP_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DNCL_REMOVE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_COMPLIANCE_SCRUB_LISTS_REMOVAL_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LISTS_EXPIRATION_LIMITS_FIELD_NUMBER: _ClassVar[int]
    allow_dncl_add: bool
    manual_dial_auto_dncl_add: bool
    preview_dial_auto_dncl_add: bool
    agent_responses_auto_dncl_add: bool
    default_manual_dncl_expire_hours: int
    default_preview_dncl_expire_hours: int
    default_dncl_country: int
    default_outbound_dncl_expire_hours: int
    default_inbound_dncl_expire_hours: int
    hunt_group_compliance_scrub_lists: _containers.RepeatedScalarFieldContainer[str]
    scrub_lists_auto_add_options: _containers.RepeatedCompositeFieldContainer[ScrubListsAutoAdd]
    display_dncl_options_in_wrapup: bool
    allow_dncl_remove: bool
    hunt_group_compliance_scrub_lists_removal_allowed: _containers.RepeatedScalarFieldContainer[str]
    scrub_lists_expiration_limits: ScrubListsExpirationLimits
    def __init__(self, allow_dncl_add: bool = ..., manual_dial_auto_dncl_add: bool = ..., preview_dial_auto_dncl_add: bool = ..., agent_responses_auto_dncl_add: bool = ..., default_manual_dncl_expire_hours: _Optional[int] = ..., default_preview_dncl_expire_hours: _Optional[int] = ..., default_dncl_country: _Optional[int] = ..., default_outbound_dncl_expire_hours: _Optional[int] = ..., default_inbound_dncl_expire_hours: _Optional[int] = ..., hunt_group_compliance_scrub_lists: _Optional[_Iterable[str]] = ..., scrub_lists_auto_add_options: _Optional[_Iterable[_Union[ScrubListsAutoAdd, _Mapping]]] = ..., display_dncl_options_in_wrapup: bool = ..., allow_dncl_remove: bool = ..., hunt_group_compliance_scrub_lists_removal_allowed: _Optional[_Iterable[str]] = ..., scrub_lists_expiration_limits: _Optional[_Union[ScrubListsExpirationLimits, _Mapping]] = ...) -> None: ...

class TransferSettings(_message.Message):
    __slots__ = ["allowed", "show_filtering", "requeue_type", "type", "default_country_sid", "show_country_selector", "has_custom_transfer_number", "default_transfer_number", "has_custom_caller_id", "default_caller_id", "show_transfers_phone_book", "show_caller_id_phone_book", "hand_off_type", "recording_status", "default_caller_id_country_sid", "show_caller_id_country_selector", "start_record_transfer_targets", "stop_record_transfer_targets", "default_filtering_include_all_online_agents", "requeue_type_custom_value", "agent_transfer_hunt_group_filter", "agent_transfer_recording_status", "requeue_transfer_recording_status", "open_transfer_recording_status", "natural_compliance_override", "transfer_natural_compliance_rule_set_name", "compliance_metadata", "call_whitelist"]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SHOW_FILTERING_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    SHOW_COUNTRY_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    HAS_CUSTOM_TRANSFER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRANSFER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HAS_CUSTOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_TRANSFERS_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALLER_ID_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    HAND_OFF_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALLER_ID_COUNTRY_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    START_RECORD_TRANSFER_TARGETS_FIELD_NUMBER: _ClassVar[int]
    STOP_RECORD_TRANSFER_TARGETS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FILTERING_INCLUDE_ALL_ONLINE_AGENTS_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_TYPE_CUSTOM_VALUE_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRANSFER_HUNT_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRANSFER_RECORDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_TRANSFER_RECORDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OPEN_TRANSFER_RECORDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    NATURAL_COMPLIANCE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_NATURAL_COMPLIANCE_RULE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    CALL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    show_filtering: bool
    requeue_type: RequeueTransferQueueConfigType.Enum
    type: _containers.RepeatedScalarFieldContainer[TransferSettingsType.Enum]
    default_country_sid: int
    show_country_selector: bool
    has_custom_transfer_number: bool
    default_transfer_number: str
    has_custom_caller_id: bool
    default_caller_id: str
    show_transfers_phone_book: bool
    show_caller_id_phone_book: bool
    hand_off_type: _containers.RepeatedScalarFieldContainer[TransferSettingsHandOffType.Enum]
    recording_status: RecordingStatus.Enum
    default_caller_id_country_sid: int
    show_caller_id_country_selector: bool
    start_record_transfer_targets: _containers.RepeatedScalarFieldContainer[str]
    stop_record_transfer_targets: _containers.RepeatedScalarFieldContainer[str]
    default_filtering_include_all_online_agents: bool
    requeue_type_custom_value: str
    agent_transfer_hunt_group_filter: bool
    agent_transfer_recording_status: RecordingStatus.Enum
    requeue_transfer_recording_status: RecordingStatus.Enum
    open_transfer_recording_status: RecordingStatus.Enum
    natural_compliance_override: bool
    transfer_natural_compliance_rule_set_name: str
    compliance_metadata: _containers.RepeatedCompositeFieldContainer[ComplianceMetadata]
    call_whitelist: bool
    def __init__(self, allowed: bool = ..., show_filtering: bool = ..., requeue_type: _Optional[_Union[RequeueTransferQueueConfigType.Enum, str]] = ..., type: _Optional[_Iterable[_Union[TransferSettingsType.Enum, str]]] = ..., default_country_sid: _Optional[int] = ..., show_country_selector: bool = ..., has_custom_transfer_number: bool = ..., default_transfer_number: _Optional[str] = ..., has_custom_caller_id: bool = ..., default_caller_id: _Optional[str] = ..., show_transfers_phone_book: bool = ..., show_caller_id_phone_book: bool = ..., hand_off_type: _Optional[_Iterable[_Union[TransferSettingsHandOffType.Enum, str]]] = ..., recording_status: _Optional[_Union[RecordingStatus.Enum, str]] = ..., default_caller_id_country_sid: _Optional[int] = ..., show_caller_id_country_selector: bool = ..., start_record_transfer_targets: _Optional[_Iterable[str]] = ..., stop_record_transfer_targets: _Optional[_Iterable[str]] = ..., default_filtering_include_all_online_agents: bool = ..., requeue_type_custom_value: _Optional[str] = ..., agent_transfer_hunt_group_filter: bool = ..., agent_transfer_recording_status: _Optional[_Union[RecordingStatus.Enum, str]] = ..., requeue_transfer_recording_status: _Optional[_Union[RecordingStatus.Enum, str]] = ..., open_transfer_recording_status: _Optional[_Union[RecordingStatus.Enum, str]] = ..., natural_compliance_override: bool = ..., transfer_natural_compliance_rule_set_name: _Optional[str] = ..., compliance_metadata: _Optional[_Iterable[_Union[ComplianceMetadata, _Mapping]]] = ..., call_whitelist: bool = ...) -> None: ...

class RecordingSettings(_message.Message):
    __slots__ = ["display_indicator", "enable_pause", "enable_delay", "delay", "pause_recording_on_hold"]
    DISPLAY_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DELAY_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_RECORDING_ON_HOLD_FIELD_NUMBER: _ClassVar[int]
    display_indicator: bool
    enable_pause: bool
    enable_delay: bool
    delay: int
    pause_recording_on_hold: bool
    def __init__(self, display_indicator: bool = ..., enable_pause: bool = ..., enable_delay: bool = ..., delay: _Optional[int] = ..., pause_recording_on_hold: bool = ...) -> None: ...

class SimpleHuntGroup(_message.Message):
    __slots__ = ["hunt_group_sid", "hunt_group_name"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    hunt_group_name: str
    def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...

class DisplayDataSettings(_message.Message):
    __slots__ = ["display_data_dip", "display_data_dip_keys", "display_data_collect", "display_ivr_navigation", "display_sip_header_data"]
    class DisplayDataDip(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[DisplayDataSettings.DisplayDataDip]
        ALL: _ClassVar[DisplayDataSettings.DisplayDataDip]
        LIMITED: _ClassVar[DisplayDataSettings.DisplayDataDip]
    NONE: DisplayDataSettings.DisplayDataDip
    ALL: DisplayDataSettings.DisplayDataDip
    LIMITED: DisplayDataSettings.DisplayDataDip
    DISPLAY_DATA_DIP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_DIP_KEYS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_COLLECT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IVR_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SIP_HEADER_DATA_FIELD_NUMBER: _ClassVar[int]
    display_data_dip: DisplayDataSettings.DisplayDataDip
    display_data_dip_keys: _containers.RepeatedScalarFieldContainer[str]
    display_data_collect: bool
    display_ivr_navigation: bool
    display_sip_header_data: bool
    def __init__(self, display_data_dip: _Optional[_Union[DisplayDataSettings.DisplayDataDip, str]] = ..., display_data_dip_keys: _Optional[_Iterable[str]] = ..., display_data_collect: bool = ..., display_ivr_navigation: bool = ..., display_sip_header_data: bool = ...) -> None: ...

class RequeueTransferQueueConfigType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[RequeueTransferQueueConfigType.Enum]
        DEFAULT: _ClassVar[RequeueTransferQueueConfigType.Enum]
        CURRENT: _ClassVar[RequeueTransferQueueConfigType.Enum]
        CUSTOM: _ClassVar[RequeueTransferQueueConfigType.Enum]
    UNKNOWN: RequeueTransferQueueConfigType.Enum
    DEFAULT: RequeueTransferQueueConfigType.Enum
    CURRENT: RequeueTransferQueueConfigType.Enum
    CUSTOM: RequeueTransferQueueConfigType.Enum
    def __init__(self) -> None: ...

class RecordingStatus(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[RecordingStatus.Enum]
        KEEP_RECORDING: _ClassVar[RecordingStatus.Enum]
        STOP_RECORDING: _ClassVar[RecordingStatus.Enum]
        START_RECORDING: _ClassVar[RecordingStatus.Enum]
    UNKNOWN: RecordingStatus.Enum
    KEEP_RECORDING: RecordingStatus.Enum
    STOP_RECORDING: RecordingStatus.Enum
    START_RECORDING: RecordingStatus.Enum
    def __init__(self) -> None: ...

class TransferSettingsType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[TransferSettingsType.Enum]
        AGENT: _ClassVar[TransferSettingsType.Enum]
        OPEN: _ClassVar[TransferSettingsType.Enum]
        REQUEUE: _ClassVar[TransferSettingsType.Enum]
        VOICE_MAIL: _ClassVar[TransferSettingsType.Enum]
        PBX_EXTENSION: _ClassVar[TransferSettingsType.Enum]
    UNKNOWN: TransferSettingsType.Enum
    AGENT: TransferSettingsType.Enum
    OPEN: TransferSettingsType.Enum
    REQUEUE: TransferSettingsType.Enum
    VOICE_MAIL: TransferSettingsType.Enum
    PBX_EXTENSION: TransferSettingsType.Enum
    def __init__(self) -> None: ...

class TransferSettingsHandOffType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[TransferSettingsHandOffType.Enum]
        CONFERENCE: _ClassVar[TransferSettingsHandOffType.Enum]
        WARM: _ClassVar[TransferSettingsHandOffType.Enum]
        COLD: _ClassVar[TransferSettingsHandOffType.Enum]
    UNKNOWN: TransferSettingsHandOffType.Enum
    CONFERENCE: TransferSettingsHandOffType.Enum
    WARM: TransferSettingsHandOffType.Enum
    COLD: TransferSettingsHandOffType.Enum
    def __init__(self) -> None: ...

class AgentHoldSettings(_message.Message):
    __slots__ = ["allowed", "auto_pause_on_multi_hold"]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    AUTO_PAUSE_ON_MULTI_HOLD_FIELD_NUMBER: _ClassVar[int]
    allowed: AllowedHoldType.Enum
    auto_pause_on_multi_hold: bool
    def __init__(self, allowed: _Optional[_Union[AllowedHoldType.Enum, str]] = ..., auto_pause_on_multi_hold: bool = ...) -> None: ...

class AllowedHoldType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NONE: _ClassVar[AllowedHoldType.Enum]
        SIMPLE: _ClassVar[AllowedHoldType.Enum]
        MULTI: _ClassVar[AllowedHoldType.Enum]
        BOTH: _ClassVar[AllowedHoldType.Enum]
    NONE: AllowedHoldType.Enum
    SIMPLE: AllowedHoldType.Enum
    MULTI: AllowedHoldType.Enum
    BOTH: AllowedHoldType.Enum
    def __init__(self) -> None: ...

class ManualApprovalSettings(_message.Message):
    __slots__ = ["allowed", "confirm", "sms_allowed", "sms_number_confirmation"]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    SMS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SMS_NUMBER_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    confirm: bool
    sms_allowed: bool
    sms_number_confirmation: bool
    def __init__(self, allowed: bool = ..., confirm: bool = ..., sms_allowed: bool = ..., sms_number_confirmation: bool = ...) -> None: ...

class ListHuntGroupWebLinksReq(_message.Message):
    __slots__ = ["hunt_group_sid", "call_sid", "call_type", "service_id", "scheduled_callback_id", "session_sid", "isInitialPreview"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ISINITIALPREVIEW_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    service_id: str
    scheduled_callback_id: str
    session_sid: int
    isInitialPreview: bool
    def __init__(self, hunt_group_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., service_id: _Optional[str] = ..., scheduled_callback_id: _Optional[str] = ..., session_sid: _Optional[int] = ..., isInitialPreview: bool = ...) -> None: ...

class ListHuntGroupWebLinksRes(_message.Message):
    __slots__ = ["web_links"]
    WEB_LINKS_FIELD_NUMBER: _ClassVar[int]
    web_links: _containers.RepeatedCompositeFieldContainer[WebLink]
    def __init__(self, web_links: _Optional[_Iterable[_Union[WebLink, _Mapping]]] = ...) -> None: ...

class WebLink(_message.Message):
    __slots__ = ["display_name", "description", "link_url", "is_js_link", "tooltip_missing_fields", "hunt_group_parameter_sid"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_URL_FIELD_NUMBER: _ClassVar[int]
    IS_JS_LINK_FIELD_NUMBER: _ClassVar[int]
    TOOLTIP_MISSING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_PARAMETER_SID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    link_url: str
    is_js_link: bool
    tooltip_missing_fields: _containers.RepeatedScalarFieldContainer[str]
    hunt_group_parameter_sid: int
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., link_url: _Optional[str] = ..., is_js_link: bool = ..., tooltip_missing_fields: _Optional[_Iterable[str]] = ..., hunt_group_parameter_sid: _Optional[int] = ...) -> None: ...

class GetHuntGroupPauseCodesReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetHuntGroupPauseCodesRes(_message.Message):
    __slots__ = ["name", "description", "pause_codes"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_CODES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    pause_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., pause_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAgentCallHistoryReq(_message.Message):
    __slots__ = ["session_sid", "history_filter"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FILTER_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    history_filter: AgentStatisticsSettings.HistoryFilter
    def __init__(self, session_sid: _Optional[int] = ..., history_filter: _Optional[_Union[AgentStatisticsSettings.HistoryFilter, str]] = ...) -> None: ...

class ListAgentCallHistoryRes(_message.Message):
    __slots__ = ["history"]
    class Entry(_message.Message):
        __slots__ = ["call_sid", "schedule_time", "call_type", "phone_number", "caller_id", "result", "duration"]
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        schedule_time: str
        call_type: _acd_pb2.CallType.Enum
        phone_number: str
        caller_id: str
        result: int
        duration: int
        def __init__(self, call_sid: _Optional[int] = ..., schedule_time: _Optional[str] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., result: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[ListAgentCallHistoryRes.Entry]
    def __init__(self, history: _Optional[_Iterable[_Union[ListAgentCallHistoryRes.Entry, _Mapping]]] = ...) -> None: ...

class GetCampaignCompletionStatusReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetCampaignCompletionStatusRes(_message.Message):
    __slots__ = ["broadcasts_exist", "percent_complete", "completion_status", "total_tasks", "total_tasks_completed"]
    class TaskGroupCompletionStatus(_message.Message):
        __slots__ = ["task_group_sid", "name", "percent_complete", "total_tasks", "total_tasks_completed"]
        TASK_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TASKS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TASKS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        task_group_sid: int
        name: str
        percent_complete: int
        total_tasks: int
        total_tasks_completed: int
        def __init__(self, task_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., percent_complete: _Optional[int] = ..., total_tasks: _Optional[int] = ..., total_tasks_completed: _Optional[int] = ...) -> None: ...
    class CompletionStatusEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: GetCampaignCompletionStatusRes.TaskGroupCompletionStatus
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[GetCampaignCompletionStatusRes.TaskGroupCompletionStatus, _Mapping]] = ...) -> None: ...
    BROADCASTS_EXIST_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TASKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TASKS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    broadcasts_exist: bool
    percent_complete: int
    completion_status: _containers.MessageMap[int, GetCampaignCompletionStatusRes.TaskGroupCompletionStatus]
    total_tasks: int
    total_tasks_completed: int
    def __init__(self, broadcasts_exist: bool = ..., percent_complete: _Optional[int] = ..., completion_status: _Optional[_Mapping[int, GetCampaignCompletionStatusRes.TaskGroupCompletionStatus]] = ..., total_tasks: _Optional[int] = ..., total_tasks_completed: _Optional[int] = ...) -> None: ...

class GetLostPeerInfoReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class GetLostPeerInfoRes(_message.Message):
    __slots__ = ["former_agent_sid", "former_agent_name", "former_hunt_group_name", "hunt_groups", "agents", "agent_skills", "pbx_extensions"]
    FORMER_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    FORMER_AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMER_HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    former_agent_sid: int
    former_agent_name: str
    former_hunt_group_name: str
    hunt_groups: _containers.RepeatedScalarFieldContainer[str]
    agents: _containers.RepeatedScalarFieldContainer[str]
    agent_skills: _containers.RepeatedScalarFieldContainer[str]
    pbx_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, former_agent_sid: _Optional[int] = ..., former_agent_name: _Optional[str] = ..., former_hunt_group_name: _Optional[str] = ..., hunt_groups: _Optional[_Iterable[str]] = ..., agents: _Optional[_Iterable[str]] = ..., agent_skills: _Optional[_Iterable[str]] = ..., pbx_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDispositionKeysReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDispositionKeysRes(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class GetScriptOrResponsesReq(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: MailMergeData
    def __init__(self, data: _Optional[_Union[MailMergeData, _Mapping]] = ...) -> None: ...

class GetScriptOrResponsesRes(_message.Message):
    __slots__ = ["scripts", "responses"]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    scripts: HuntGroupScript
    responses: _containers.RepeatedCompositeFieldContainer[HuntGroupResponse]
    def __init__(self, scripts: _Optional[_Union[HuntGroupScript, _Mapping]] = ..., responses: _Optional[_Iterable[_Union[HuntGroupResponse, _Mapping]]] = ...) -> None: ...

class GetReadyAgentsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetReadyAgentsRes(_message.Message):
    __slots__ = ["ready_agents"]
    READY_AGENTS_FIELD_NUMBER: _ClassVar[int]
    ready_agents: _containers.RepeatedCompositeFieldContainer[AgentsByAgentSidShort]
    def __init__(self, ready_agents: _Optional[_Iterable[_Union[AgentsByAgentSidShort, _Mapping]]] = ...) -> None: ...

class AgentsByAgentSidShort(_message.Message):
    __slots__ = ["agent_sid", "first_name", "last_name"]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    first_name: str
    last_name: str
    def __init__(self, agent_sid: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class ListAgentQueueAndOnHoldCallDataReq(_message.Message):
    __slots__ = ["agent_session_sid", "agent_skills"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    agent_skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_session_sid: _Optional[int] = ..., agent_skills: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAgentQueueAndOnHoldCallDataRes(_message.Message):
    __slots__ = ["agent_queue_calls", "on_hold_calls", "hqm_calls"]
    class CallData(_message.Message):
        __slots__ = ["call_sid", "phone_number", "caller_id", "call_type", "start_date", "hold_date", "skills", "agent_specific", "queued_notification_type"]
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        START_DATE_FIELD_NUMBER: _ClassVar[int]
        HOLD_DATE_FIELD_NUMBER: _ClassVar[int]
        SKILLS_FIELD_NUMBER: _ClassVar[int]
        AGENT_SPECIFIC_FIELD_NUMBER: _ClassVar[int]
        QUEUED_NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        phone_number: str
        caller_id: str
        call_type: _acd_pb2.CallType.Enum
        start_date: _timestamp_pb2.Timestamp
        hold_date: _timestamp_pb2.Timestamp
        skills: _containers.RepeatedScalarFieldContainer[str]
        agent_specific: bool
        queued_notification_type: _acd_pb2.QueuedNotificationType
        def __init__(self, call_sid: _Optional[int] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hold_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Iterable[str]] = ..., agent_specific: bool = ..., queued_notification_type: _Optional[_Union[_acd_pb2.QueuedNotificationType, str]] = ...) -> None: ...
    AGENT_QUEUE_CALLS_FIELD_NUMBER: _ClassVar[int]
    ON_HOLD_CALLS_FIELD_NUMBER: _ClassVar[int]
    HQM_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_queue_calls: _containers.RepeatedCompositeFieldContainer[ListAgentQueueAndOnHoldCallDataRes.CallData]
    on_hold_calls: _containers.RepeatedCompositeFieldContainer[ListAgentQueueAndOnHoldCallDataRes.CallData]
    hqm_calls: _containers.RepeatedCompositeFieldContainer[ListAgentQueueAndOnHoldCallDataRes.CallData]
    def __init__(self, agent_queue_calls: _Optional[_Iterable[_Union[ListAgentQueueAndOnHoldCallDataRes.CallData, _Mapping]]] = ..., on_hold_calls: _Optional[_Iterable[_Union[ListAgentQueueAndOnHoldCallDataRes.CallData, _Mapping]]] = ..., hqm_calls: _Optional[_Iterable[_Union[ListAgentQueueAndOnHoldCallDataRes.CallData, _Mapping]]] = ...) -> None: ...

class AgentCallResponseDetails(_message.Message):
    __slots__ = ["key", "value", "order"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    order: int
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., order: _Optional[int] = ...) -> None: ...

class SaveAgentCallResponsesReq(_message.Message):
    __slots__ = ["call_sid", "agent_session_sid", "agent_call_response_details", "call_type", "compliance_metadata"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    agent_session_sid: int
    agent_call_response_details: _containers.RepeatedCompositeFieldContainer[AgentCallResponseDetails]
    call_type: _acd_pb2.CallType.Enum
    compliance_metadata: _containers.RepeatedCompositeFieldContainer[_call_pb2.SimpleKeyValue]
    def __init__(self, call_sid: _Optional[int] = ..., agent_session_sid: _Optional[int] = ..., agent_call_response_details: _Optional[_Iterable[_Union[AgentCallResponseDetails, _Mapping]]] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., compliance_metadata: _Optional[_Iterable[_Union[_call_pb2.SimpleKeyValue, _Mapping]]] = ...) -> None: ...

class SaveAgentCallResponsesRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentCallLog(_message.Message):
    __slots__ = ["agent_call_log_sid", "call_sid", "call_type", "action_date", "action_key", "action_value"]
    AGENT_CALL_LOG_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    agent_call_log_sid: int
    call_sid: _wrappers_pb2.Int64Value
    call_type: _acd_pb2.CallType.Enum
    action_date: _timestamp_pb2.Timestamp
    action_key: _wrappers_pb2.StringValue
    action_value: _wrappers_pb2.StringValue
    def __init__(self, agent_call_log_sid: _Optional[int] = ..., call_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., action_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., action_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., action_value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class AgentSkill(_message.Message):
    __slots__ = ["agent_skill_sid", "name", "description"]
    AGENT_SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    agent_skill_sid: int
    name: str
    description: _wrappers_pb2.StringValue
    def __init__(self, agent_skill_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ListAgentTransferOptionsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAgentTransferOptionsRes(_message.Message):
    __slots__ = ["agent_info", "hunt_group", "pbx_extensions", "agent_skills", "agent_profile"]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    agent_info: _containers.RepeatedCompositeFieldContainer[Agent]
    hunt_group: _containers.RepeatedCompositeFieldContainer[HuntGroup]
    pbx_extensions: _containers.RepeatedCompositeFieldContainer[PBXExtension]
    agent_skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    agent_profile: _containers.RepeatedCompositeFieldContainer[AgentsByAgentSidShort]
    def __init__(self, agent_info: _Optional[_Iterable[_Union[Agent, _Mapping]]] = ..., hunt_group: _Optional[_Iterable[_Union[HuntGroup, _Mapping]]] = ..., pbx_extensions: _Optional[_Iterable[_Union[PBXExtension, _Mapping]]] = ..., agent_skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ..., agent_profile: _Optional[_Iterable[_Union[AgentsByAgentSidShort, _Mapping]]] = ...) -> None: ...

class GetIntercomPeerInfoReq(_message.Message):
    __slots__ = ["agent_session_sid"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    def __init__(self, agent_session_sid: _Optional[int] = ...) -> None: ...

class GetIntercomPeerInfoRes(_message.Message):
    __slots__ = ["peer_sid", "first_name", "last_name"]
    PEER_SID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    peer_sid: int
    first_name: str
    last_name: str
    def __init__(self, peer_sid: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class ListOrgResponseEvaluatorsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOrgResponseEvaluatorsRes(_message.Message):
    __slots__ = ["evaluators"]
    EVALUATORS_FIELD_NUMBER: _ClassVar[int]
    evaluators: _containers.RepeatedCompositeFieldContainer[ResponseEvaluator]
    def __init__(self, evaluators: _Optional[_Iterable[_Union[ResponseEvaluator, _Mapping]]] = ...) -> None: ...

class ResponseEvaluator(_message.Message):
    __slots__ = ["name", "description", "regular_expression", "xml_client_property_sid"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REGULAR_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    regular_expression: str
    xml_client_property_sid: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., regular_expression: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class GetQueueConfigurationOptionsArrayReq(_message.Message):
    __slots__ = ["localized_account_default_string"]
    LOCALIZED_ACCOUNT_DEFAULT_STRING_FIELD_NUMBER: _ClassVar[int]
    localized_account_default_string: str
    def __init__(self, localized_account_default_string: _Optional[str] = ...) -> None: ...

class GetQueueConfigurationOptionsArrayRes(_message.Message):
    __slots__ = ["filenames"]
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    filenames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filenames: _Optional[_Iterable[str]] = ...) -> None: ...

class AgentCallActivityDetails(_message.Message):
    __slots__ = ["agent_sid", "agent_name", "agent_session_sid", "hunt_group_sid", "hunt_group_name", "agent_call_cost", "agent_wait_duration", "call_wait_duration", "hold_duration", "manual_duration", "pause_duration", "preview_duration", "suspended_duration", "talk_duration", "transfer_duration", "wrap_up_duration", "agent_call_sid", "hunt_group_type"]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_COST_FIELD_NUMBER: _ClassVar[int]
    AGENT_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    CALL_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    HOLD_DURATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DURATION_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_DURATION_FIELD_NUMBER: _ClassVar[int]
    TALK_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_DURATION_FIELD_NUMBER: _ClassVar[int]
    WRAP_UP_DURATION_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    agent_name: _wrappers_pb2.StringValue
    agent_session_sid: _wrappers_pb2.Int64Value
    hunt_group_sid: _wrappers_pb2.Int64Value
    hunt_group_name: _wrappers_pb2.StringValue
    agent_call_cost: _wrappers_pb2.DoubleValue
    agent_wait_duration: _wrappers_pb2.Int64Value
    call_wait_duration: _wrappers_pb2.Int64Value
    hold_duration: _wrappers_pb2.Int64Value
    manual_duration: _wrappers_pb2.Int64Value
    pause_duration: _wrappers_pb2.Int64Value
    preview_duration: _wrappers_pb2.Int64Value
    suspended_duration: _wrappers_pb2.Int64Value
    talk_duration: _wrappers_pb2.Int64Value
    transfer_duration: _wrappers_pb2.Int64Value
    wrap_up_duration: _wrappers_pb2.Int64Value
    agent_call_sid: _wrappers_pb2.Int64Value
    hunt_group_type: _acd_pb2.HuntGroupType.Enum
    def __init__(self, agent_sid: _Optional[int] = ..., agent_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., agent_session_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., hunt_group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., hunt_group_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., agent_call_cost: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., agent_wait_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., call_wait_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., hold_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., manual_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., pause_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., preview_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., suspended_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., talk_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., transfer_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., wrap_up_duration: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., agent_call_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., hunt_group_type: _Optional[_Union[_acd_pb2.HuntGroupType.Enum, str]] = ...) -> None: ...

class GetConditionalDNCLRulesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetConditionalDNCLRulesRes(_message.Message):
    __slots__ = ["disposition_rules"]
    DISPOSITION_RULES_FIELD_NUMBER: _ClassVar[int]
    disposition_rules: _containers.RepeatedCompositeFieldContainer[AgentDispositionConditionalDncl.DispositionRulesTable]
    def __init__(self, disposition_rules: _Optional[_Iterable[_Union[AgentDispositionConditionalDncl.DispositionRulesTable, _Mapping]]] = ...) -> None: ...

class ManualDialStartReq(_message.Message):
    __slots__ = ["simple_call_data", "hunt_group_sid", "agent_session_sid"]
    SIMPLE_CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    simple_call_data: _call_pb2.SimpleCallData
    hunt_group_sid: int
    agent_session_sid: int
    def __init__(self, simple_call_data: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., hunt_group_sid: _Optional[int] = ..., agent_session_sid: _Optional[int] = ...) -> None: ...

class ManualDialStartRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListExtendedCallHistoryReq(_message.Message):
    __slots__ = ["search_type", "call_types", "customer_number", "search_scope", "call_sid", "caller_id"]
    SEARCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    search_type: _p3api_pb2.CallHistorySearchType.Enum
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    customer_number: str
    search_scope: _p3api_pb2.CallHistorySearchScope.Enum
    call_sid: int
    caller_id: str
    def __init__(self, search_type: _Optional[_Union[_p3api_pb2.CallHistorySearchType.Enum, str]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., customer_number: _Optional[str] = ..., search_scope: _Optional[_Union[_p3api_pb2.CallHistorySearchScope.Enum, str]] = ..., call_sid: _Optional[int] = ..., caller_id: _Optional[str] = ...) -> None: ...

class ListExtendedCallHistoryRes(_message.Message):
    __slots__ = ["group_sid", "call_type", "call_sid", "customer_number", "phone", "date", "result", "length", "cost", "keys", "call_details", "linkback_length", "is_call_recorded", "recording_filename", "start_date", "country_sid"]
    GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CALL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IS_CALL_RECORDED_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FILENAME_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    group_sid: int
    call_type: _acd_pb2.CallType.Enum
    call_sid: int
    customer_number: str
    phone: str
    date: str
    result: int
    length: int
    cost: _wrappers_pb2.DoubleValue
    keys: _wrappers_pb2.StringValue
    call_details: GetCallDetailsRes
    linkback_length: int
    is_call_recorded: bool
    recording_filename: str
    start_date: _timestamp_pb2.Timestamp
    country_sid: int
    def __init__(self, group_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., call_sid: _Optional[int] = ..., customer_number: _Optional[str] = ..., phone: _Optional[str] = ..., date: _Optional[str] = ..., result: _Optional[int] = ..., length: _Optional[int] = ..., cost: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., keys: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., call_details: _Optional[_Union[GetCallDetailsRes, _Mapping]] = ..., linkback_length: _Optional[int] = ..., is_call_recorded: bool = ..., recording_filename: _Optional[str] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., country_sid: _Optional[int] = ...) -> None: ...

class ListWhiteListPhoneBooksReq(_message.Message):
    __slots__ = ["hunt_group_sid", "include_null_phone_number_types", "order_bys"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NULL_PHONE_NUMBER_TYPES_FIELD_NUMBER: _ClassVar[int]
    ORDER_BYS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    include_null_phone_number_types: bool
    order_bys: _containers.RepeatedScalarFieldContainer[_p3api_pb2.ListPhoneBookOrderBy.Enum]
    def __init__(self, hunt_group_sid: _Optional[int] = ..., include_null_phone_number_types: bool = ..., order_bys: _Optional[_Iterable[_Union[_p3api_pb2.ListPhoneBookOrderBy.Enum, str]]] = ...) -> None: ...

class ListWhiteListPhoneBooksRes(_message.Message):
    __slots__ = ["white_list_phone_books"]
    WHITE_LIST_PHONE_BOOKS_FIELD_NUMBER: _ClassVar[int]
    white_list_phone_books: _containers.RepeatedCompositeFieldContainer[PhoneBook]
    def __init__(self, white_list_phone_books: _Optional[_Iterable[_Union[PhoneBook, _Mapping]]] = ...) -> None: ...

class UpdateAgentCallResponseValueReq(_message.Message):
    __slots__ = ["response_id", "value"]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    response_id: int
    value: str
    def __init__(self, response_id: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class UpdateAgentCallResponseValueRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlacePreviewDialCallReq(_message.Message):
    __slots__ = ["call", "hunt_group_sid", "agent_session_sid"]
    CALL_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    hunt_group_sid: int
    agent_session_sid: int
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., hunt_group_sid: _Optional[int] = ..., agent_session_sid: _Optional[int] = ...) -> None: ...

class PlacePreviewDialCallRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CancelPreviewDialCallReq(_message.Message):
    __slots__ = ["call", "agent_session_sid", "report_scrub_override"]
    CALL_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REPORT_SCRUB_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    call: _call_pb2.SimpleCallData
    agent_session_sid: int
    report_scrub_override: bool
    def __init__(self, call: _Optional[_Union[_call_pb2.SimpleCallData, _Mapping]] = ..., agent_session_sid: _Optional[int] = ..., report_scrub_override: bool = ...) -> None: ...

class CancelPreviewDialCallRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadRecordingRes(_message.Message):
    __slots__ = ["url", "filename"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    url: str
    filename: str
    def __init__(self, url: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class DownloadCallRecordingReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class DownloadCallRecordingsReq(_message.Message):
    __slots__ = ["call_params", "html_file_name", "html_file_content", "group_sid", "start_date"]
    class CallParams(_message.Message):
        __slots__ = ["call_sid", "call_type"]
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        call_type: _acd_pb2.CallType.Enum
        def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...
    CALL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HTML_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    HTML_FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    call_params: _containers.RepeatedCompositeFieldContainer[DownloadCallRecordingsReq.CallParams]
    html_file_name: str
    html_file_content: str
    group_sid: _wrappers_pb2.Int64Value
    start_date: _timestamp_pb2.Timestamp
    def __init__(self, call_params: _Optional[_Iterable[_Union[DownloadCallRecordingsReq.CallParams, _Mapping]]] = ..., html_file_name: _Optional[str] = ..., html_file_content: _Optional[str] = ..., group_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentDispositionConditionalDncl(_message.Message):
    __slots__ = ["name", "description", "country_sid", "disposition_rules_table"]
    class DispositionRulesTable(_message.Message):
        __slots__ = ["disposition_key", "disposition_expiration_table"]
        DISPOSITION_KEY_FIELD_NUMBER: _ClassVar[int]
        DISPOSITION_EXPIRATION_TABLE_FIELD_NUMBER: _ClassVar[int]
        disposition_key: str
        disposition_expiration_table: _containers.RepeatedCompositeFieldContainer[AgentDispositionConditionalDncl.DispositionExpirationTable]
        def __init__(self, disposition_key: _Optional[str] = ..., disposition_expiration_table: _Optional[_Iterable[_Union[AgentDispositionConditionalDncl.DispositionExpirationTable, _Mapping]]] = ...) -> None: ...
    class DispositionExpirationTable(_message.Message):
        __slots__ = ["disposition_value", "integer"]
        DISPOSITION_VALUE_FIELD_NUMBER: _ClassVar[int]
        INTEGER_FIELD_NUMBER: _ClassVar[int]
        disposition_value: str
        integer: int
        def __init__(self, disposition_value: _Optional[str] = ..., integer: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_RULES_TABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    country_sid: int
    disposition_rules_table: _containers.RepeatedCompositeFieldContainer[AgentDispositionConditionalDncl.DispositionRulesTable]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., country_sid: _Optional[int] = ..., disposition_rules_table: _Optional[_Iterable[_Union[AgentDispositionConditionalDncl.DispositionRulesTable, _Mapping]]] = ...) -> None: ...

class UpdateTaskStatusReq(_message.Message):
    __slots__ = ["task_sid", "status"]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    status: _task_pb2.TaskStatus
    def __init__(self, task_sid: _Optional[int] = ..., status: _Optional[_Union[_task_pb2.TaskStatus, str]] = ...) -> None: ...

class Nil(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListCallbackRoutingAgentsReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListCallbackRoutingAgentsRes(_message.Message):
    __slots__ = ["agent_short"]
    AGENT_SHORT_FIELD_NUMBER: _ClassVar[int]
    agent_short: _containers.RepeatedCompositeFieldContainer[AgentsByAgentSidShort]
    def __init__(self, agent_short: _Optional[_Iterable[_Union[AgentsByAgentSidShort, _Mapping]]] = ...) -> None: ...

class ListCallbackRoutingSkillsReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListCallbackRoutingSkillsRes(_message.Message):
    __slots__ = ["agent_skills"]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    agent_skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    def __init__(self, agent_skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ...) -> None: ...

class HandleRecordingDelayReq(_message.Message):
    __slots__ = ["hunt_group_sid", "agent_session_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    agent_session_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., agent_session_sid: _Optional[int] = ...) -> None: ...

class HandleRecordingDelayRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ScheduleCallBackSettings(_message.Message):
    __slots__ = ["allow_callback_scheduling", "allow_scheduled_callback_calling", "allow_automatic_callback_retrieval_mode", "allow_default_callback_routing", "callbacks_retrieval_mode_settings", "default_callback_routing_settings", "callbacks_service_id", "has_custom_caller_id", "default_caller_id", "allow_scheduled_callback_calendar"]
    ALLOW_CALLBACK_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCHEDULED_CALLBACK_CALLING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AUTOMATIC_CALLBACK_RETRIEVAL_MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DEFAULT_CALLBACK_ROUTING_FIELD_NUMBER: _ClassVar[int]
    CALLBACKS_RETRIEVAL_MODE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLBACK_ROUTING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CALLBACKS_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_CUSTOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCHEDULED_CALLBACK_CALENDAR_FIELD_NUMBER: _ClassVar[int]
    allow_callback_scheduling: bool
    allow_scheduled_callback_calling: bool
    allow_automatic_callback_retrieval_mode: bool
    allow_default_callback_routing: bool
    callbacks_retrieval_mode_settings: str
    default_callback_routing_settings: str
    callbacks_service_id: str
    has_custom_caller_id: bool
    default_caller_id: str
    allow_scheduled_callback_calendar: bool
    def __init__(self, allow_callback_scheduling: bool = ..., allow_scheduled_callback_calling: bool = ..., allow_automatic_callback_retrieval_mode: bool = ..., allow_default_callback_routing: bool = ..., callbacks_retrieval_mode_settings: _Optional[str] = ..., default_callback_routing_settings: _Optional[str] = ..., callbacks_service_id: _Optional[str] = ..., has_custom_caller_id: bool = ..., default_caller_id: _Optional[str] = ..., allow_scheduled_callback_calendar: bool = ...) -> None: ...

class UpdateAgentAssignedHuntGroupReq(_message.Message):
    __slots__ = ["hunt_group_sid", "skills", "replace_skills"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_SKILLS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    replace_skills: bool
    def __init__(self, hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ..., replace_skills: bool = ...) -> None: ...

class UpdateAgentAssignedHuntGroupRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListHuntGroupsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListHuntGroupsRes(_message.Message):
    __slots__ = ["hunt_group"]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    hunt_group: _containers.RepeatedCompositeFieldContainer[HuntGroup]
    def __init__(self, hunt_group: _Optional[_Iterable[_Union[HuntGroup, _Mapping]]] = ...) -> None: ...

class ListReassignmentHuntGroupsReq(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListReassignmentHuntGroupsRes(_message.Message):
    __slots__ = ["hunt_groups"]
    HUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    hunt_groups: _containers.RepeatedCompositeFieldContainer[SimpleHuntGroup]
    def __init__(self, hunt_groups: _Optional[_Iterable[_Union[SimpleHuntGroup, _Mapping]]] = ...) -> None: ...

class GetOrgAgentSettingsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetOrgAgentSettingsRes(_message.Message):
    __slots__ = ["default_time_zone", "default_softphone_volume_in", "default_softphone_volume_out", "linkback_recording"]
    DEFAULT_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_IN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SOFTPHONE_VOLUME_OUT_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_RECORDING_FIELD_NUMBER: _ClassVar[int]
    default_time_zone: str
    default_softphone_volume_in: int
    default_softphone_volume_out: int
    linkback_recording: bool
    def __init__(self, default_time_zone: _Optional[str] = ..., default_softphone_volume_in: _Optional[int] = ..., default_softphone_volume_out: _Optional[int] = ..., linkback_recording: bool = ...) -> None: ...

class ListCallerIdsFromBucketReq(_message.Message):
    __slots__ = ["bucket_number"]
    BUCKET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    bucket_number: int
    def __init__(self, bucket_number: _Optional[int] = ...) -> None: ...

class ListCallerIdsFromBucketRes(_message.Message):
    __slots__ = ["caller_id_info"]
    CALLER_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    caller_id_info: _containers.RepeatedCompositeFieldContainer[CallerIdInfo]
    def __init__(self, caller_id_info: _Optional[_Iterable[_Union[CallerIdInfo, _Mapping]]] = ...) -> None: ...

class CallerIdInfo(_message.Message):
    __slots__ = ["number", "region_code"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    number: str
    region_code: str
    def __init__(self, number: _Optional[str] = ..., region_code: _Optional[str] = ...) -> None: ...

class SaveLastCallResponseReq(_message.Message):
    __slots__ = ["call_type", "call_sid", "response_name"]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_NAME_FIELD_NUMBER: _ClassVar[int]
    call_type: _acd_pb2.CallType.Enum
    call_sid: int
    response_name: str
    def __init__(self, call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., call_sid: _Optional[int] = ..., response_name: _Optional[str] = ...) -> None: ...

class SaveLastCallResponseRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentCallResponse(_message.Message):
    __slots__ = ["agent_call_response_sid", "agent_call_sid", "key", "value", "order"]
    AGENT_CALL_RESPONSE_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_SID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    agent_call_response_sid: int
    agent_call_sid: _wrappers_pb2.Int64Value
    key: _wrappers_pb2.StringValue
    value: _wrappers_pb2.StringValue
    order: _wrappers_pb2.Int32Value
    def __init__(self, agent_call_response_sid: _Optional[int] = ..., agent_call_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., order: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class GetCallDetailsRes(_message.Message):
    __slots__ = ["contact_field_data", "agent_call_activity_details", "agent_call_responses"]
    CONTACT_FIELD_DATA_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_ACTIVITY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    contact_field_data: _containers.RepeatedCompositeFieldContainer[ContactFieldDataRow]
    agent_call_activity_details: _containers.RepeatedCompositeFieldContainer[AgentCallActivityDetails]
    agent_call_responses: _containers.RepeatedCompositeFieldContainer[AgentCallResponse]
    def __init__(self, contact_field_data: _Optional[_Iterable[_Union[ContactFieldDataRow, _Mapping]]] = ..., agent_call_activity_details: _Optional[_Iterable[_Union[AgentCallActivityDetails, _Mapping]]] = ..., agent_call_responses: _Optional[_Iterable[_Union[AgentCallResponse, _Mapping]]] = ...) -> None: ...

class ListAgentCallLogsByCallSidAndTypeReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class ListAgentCallLogsByCallSidAndTypeRes(_message.Message):
    __slots__ = ["agent_call_logs"]
    AGENT_CALL_LOGS_FIELD_NUMBER: _ClassVar[int]
    agent_call_logs: _containers.RepeatedCompositeFieldContainer[AgentCallLog]
    def __init__(self, agent_call_logs: _Optional[_Iterable[_Union[AgentCallLog, _Mapping]]] = ...) -> None: ...

class ContactFieldDataRow(_message.Message):
    __slots__ = ["field_label", "field_value", "is_phone"]
    FIELD_LABEL_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_FIELD_NUMBER: _ClassVar[int]
    field_label: str
    field_value: str
    is_phone: bool
    def __init__(self, field_label: _Optional[str] = ..., field_value: _Optional[str] = ..., is_phone: bool = ...) -> None: ...

class GetCallDataReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class GetCallDataRes(_message.Message):
    __slots__ = ["ivr_data", "phone_enhanced_data", "data_collect_data", "data_dip_data", "caller_id_name", "linkback_hunt_group", "sip_header_data", "queued_callback_data", "journey_retrieved_data", "integration_data"]
    class IvrDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PhoneEnhancedDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DataCollectDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DataDipDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SipHeaderDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class QueuedCallbackDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class JourneyRetrievedDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class IntegrationDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IVR_DATA_FIELD_NUMBER: _ClassVar[int]
    PHONE_ENHANCED_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_COLLECT_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_DATA_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_NAME_FIELD_NUMBER: _ClassVar[int]
    LINKBACK_HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    SIP_HEADER_DATA_FIELD_NUMBER: _ClassVar[int]
    QUEUED_CALLBACK_DATA_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_RETRIEVED_DATA_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_DATA_FIELD_NUMBER: _ClassVar[int]
    ivr_data: _containers.ScalarMap[str, str]
    phone_enhanced_data: _containers.ScalarMap[str, str]
    data_collect_data: _containers.ScalarMap[str, str]
    data_dip_data: _containers.ScalarMap[str, str]
    caller_id_name: str
    linkback_hunt_group: str
    sip_header_data: _containers.ScalarMap[str, str]
    queued_callback_data: _containers.ScalarMap[str, str]
    journey_retrieved_data: _containers.ScalarMap[str, str]
    integration_data: _containers.ScalarMap[str, str]
    def __init__(self, ivr_data: _Optional[_Mapping[str, str]] = ..., phone_enhanced_data: _Optional[_Mapping[str, str]] = ..., data_collect_data: _Optional[_Mapping[str, str]] = ..., data_dip_data: _Optional[_Mapping[str, str]] = ..., caller_id_name: _Optional[str] = ..., linkback_hunt_group: _Optional[str] = ..., sip_header_data: _Optional[_Mapping[str, str]] = ..., queued_callback_data: _Optional[_Mapping[str, str]] = ..., journey_retrieved_data: _Optional[_Mapping[str, str]] = ..., integration_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdatePBXExtensionReq(_message.Message):
    __slots__ = ["pbx_extension", "email_subject", "email_body", "email_addresses"]
    PBX_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_BODY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    pbx_extension: str
    email_subject: str
    email_body: str
    email_addresses: str
    def __init__(self, pbx_extension: _Optional[str] = ..., email_subject: _Optional[str] = ..., email_body: _Optional[str] = ..., email_addresses: _Optional[str] = ...) -> None: ...

class UpdatePBXExtensionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HuntGroupScript(_message.Message):
    __slots__ = ["name", "description", "auto_script_progression", "script_category", "act"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCRIPT_PROGRESSION_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    auto_script_progression: bool
    script_category: str
    act: _containers.RepeatedCompositeFieldContainer[Act]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., auto_script_progression: bool = ..., script_category: _Optional[str] = ..., act: _Optional[_Iterable[_Union[Act, _Mapping]]] = ...) -> None: ...

class Act(_message.Message):
    __slots__ = ["disposition", "verbiage", "default_conditional_navigation_target", "conditional_navigation", "page_arrival_recording_control", "page_exit_recording_control"]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    VERBIAGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONDITIONAL_NAVIGATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_ARRIVAL_RECORDING_CONTROL_FIELD_NUMBER: _ClassVar[int]
    PAGE_EXIT_RECORDING_CONTROL_FIELD_NUMBER: _ClassVar[int]
    disposition: _containers.RepeatedCompositeFieldContainer[Disposition]
    verbiage: _containers.RepeatedCompositeFieldContainer[Verbiage]
    default_conditional_navigation_target: int
    conditional_navigation: _containers.RepeatedCompositeFieldContainer[ConditionalNavigation]
    page_arrival_recording_control: int
    page_exit_recording_control: int
    def __init__(self, disposition: _Optional[_Iterable[_Union[Disposition, _Mapping]]] = ..., verbiage: _Optional[_Iterable[_Union[Verbiage, _Mapping]]] = ..., default_conditional_navigation_target: _Optional[int] = ..., conditional_navigation: _Optional[_Iterable[_Union[ConditionalNavigation, _Mapping]]] = ..., page_arrival_recording_control: _Optional[int] = ..., page_exit_recording_control: _Optional[int] = ...) -> None: ...

class Disposition(_message.Message):
    __slots__ = ["required", "order", "type", "header", "prompt", "defaultValue", "response_options", "bypass_auto_script_progression"]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_AUTO_SCRIPT_PROGRESSION_FIELD_NUMBER: _ClassVar[int]
    required: bool
    order: int
    type: str
    header: str
    prompt: str
    defaultValue: str
    response_options: _containers.RepeatedScalarFieldContainer[str]
    bypass_auto_script_progression: bool
    def __init__(self, required: bool = ..., order: _Optional[int] = ..., type: _Optional[str] = ..., header: _Optional[str] = ..., prompt: _Optional[str] = ..., defaultValue: _Optional[str] = ..., response_options: _Optional[_Iterable[str]] = ..., bypass_auto_script_progression: bool = ...) -> None: ...

class Verbiage(_message.Message):
    __slots__ = ["order", "header", "body"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    order: int
    header: str
    body: str
    def __init__(self, order: _Optional[int] = ..., header: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class ConditionalNavigation(_message.Message):
    __slots__ = ["complex_boolean_expression_list", "target_act_index"]
    COMPLEX_BOOLEAN_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACT_INDEX_FIELD_NUMBER: _ClassVar[int]
    complex_boolean_expression_list: ComplexBooleanExpressionList
    target_act_index: int
    def __init__(self, complex_boolean_expression_list: _Optional[_Union[ComplexBooleanExpressionList, _Mapping]] = ..., target_act_index: _Optional[int] = ...) -> None: ...

class ComplexBooleanExpressionList(_message.Message):
    __slots__ = ["complex_boolean_expression"]
    COMPLEX_BOOLEAN_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    complex_boolean_expression: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpression]
    def __init__(self, complex_boolean_expression: _Optional[_Iterable[_Union[ComplexBooleanExpression, _Mapping]]] = ...) -> None: ...

class ComplexBooleanExpression(_message.Message):
    __slots__ = ["compare_expression_list"]
    COMPARE_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    compare_expression_list: CompareExpressionList
    def __init__(self, compare_expression_list: _Optional[_Union[CompareExpressionList, _Mapping]] = ...) -> None: ...

class CompareExpressionList(_message.Message):
    __slots__ = ["simple_compare_expression"]
    SIMPLE_COMPARE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    simple_compare_expression: _containers.RepeatedCompositeFieldContainer[CompareExpression]
    def __init__(self, simple_compare_expression: _Optional[_Iterable[_Union[CompareExpression, _Mapping]]] = ...) -> None: ...

class CompareExpression(_message.Message):
    __slots__ = ["operator_type", "value_key", "compare_value"]
    OPERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPARE_VALUE_FIELD_NUMBER: _ClassVar[int]
    operator_type: str
    value_key: str
    compare_value: str
    def __init__(self, operator_type: _Optional[str] = ..., value_key: _Optional[str] = ..., compare_value: _Optional[str] = ...) -> None: ...

class ListAgentCallResponseValuesReq(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class ListAgentCallResponseValuesRes(_message.Message):
    __slots__ = ["responses"]
    class Response(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ListAgentCallResponseValuesRes.Response]
    def __init__(self, responses: _Optional[_Iterable[_Union[ListAgentCallResponseValuesRes.Response, _Mapping]]] = ...) -> None: ...

class ContactSchema(_message.Message):
    __slots__ = ["contact_schema_sid", "contact_group_sid", "dfc_sid01", "dfc_sid02", "dfc_sid03", "dfc_sid04", "dfc_sid05", "dfc_sid06", "dfc_sid07", "dfc_sid08", "dfc_sid09", "dfc_sid10", "dfc_sid11", "dfc_sid12", "dfc_sid13", "dfc_sid14", "dfc_sid15", "dfc_sid16", "dfc_sid17", "dfc_sid18", "dfc_sid19", "dfc_sid20", "dfc_sid21", "dfc_sid22", "dfc_sid23", "dfc_sid24", "dfc_sid25", "dfc_sid26", "dfc_sid27", "dfc_sid28", "dfc_sid29", "dfc_sid30"]
    CONTACT_SCHEMA_SID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    DFC_SID01_FIELD_NUMBER: _ClassVar[int]
    DFC_SID02_FIELD_NUMBER: _ClassVar[int]
    DFC_SID03_FIELD_NUMBER: _ClassVar[int]
    DFC_SID04_FIELD_NUMBER: _ClassVar[int]
    DFC_SID05_FIELD_NUMBER: _ClassVar[int]
    DFC_SID06_FIELD_NUMBER: _ClassVar[int]
    DFC_SID07_FIELD_NUMBER: _ClassVar[int]
    DFC_SID08_FIELD_NUMBER: _ClassVar[int]
    DFC_SID09_FIELD_NUMBER: _ClassVar[int]
    DFC_SID10_FIELD_NUMBER: _ClassVar[int]
    DFC_SID11_FIELD_NUMBER: _ClassVar[int]
    DFC_SID12_FIELD_NUMBER: _ClassVar[int]
    DFC_SID13_FIELD_NUMBER: _ClassVar[int]
    DFC_SID14_FIELD_NUMBER: _ClassVar[int]
    DFC_SID15_FIELD_NUMBER: _ClassVar[int]
    DFC_SID16_FIELD_NUMBER: _ClassVar[int]
    DFC_SID17_FIELD_NUMBER: _ClassVar[int]
    DFC_SID18_FIELD_NUMBER: _ClassVar[int]
    DFC_SID19_FIELD_NUMBER: _ClassVar[int]
    DFC_SID20_FIELD_NUMBER: _ClassVar[int]
    DFC_SID21_FIELD_NUMBER: _ClassVar[int]
    DFC_SID22_FIELD_NUMBER: _ClassVar[int]
    DFC_SID23_FIELD_NUMBER: _ClassVar[int]
    DFC_SID24_FIELD_NUMBER: _ClassVar[int]
    DFC_SID25_FIELD_NUMBER: _ClassVar[int]
    DFC_SID26_FIELD_NUMBER: _ClassVar[int]
    DFC_SID27_FIELD_NUMBER: _ClassVar[int]
    DFC_SID28_FIELD_NUMBER: _ClassVar[int]
    DFC_SID29_FIELD_NUMBER: _ClassVar[int]
    DFC_SID30_FIELD_NUMBER: _ClassVar[int]
    contact_schema_sid: int
    contact_group_sid: int
    dfc_sid01: _wrappers_pb2.Int32Value
    dfc_sid02: _wrappers_pb2.Int32Value
    dfc_sid03: _wrappers_pb2.Int32Value
    dfc_sid04: _wrappers_pb2.Int32Value
    dfc_sid05: _wrappers_pb2.Int32Value
    dfc_sid06: _wrappers_pb2.Int32Value
    dfc_sid07: _wrappers_pb2.Int32Value
    dfc_sid08: _wrappers_pb2.Int32Value
    dfc_sid09: _wrappers_pb2.Int32Value
    dfc_sid10: _wrappers_pb2.Int32Value
    dfc_sid11: _wrappers_pb2.Int32Value
    dfc_sid12: _wrappers_pb2.Int32Value
    dfc_sid13: _wrappers_pb2.Int32Value
    dfc_sid14: _wrappers_pb2.Int32Value
    dfc_sid15: _wrappers_pb2.Int32Value
    dfc_sid16: _wrappers_pb2.Int32Value
    dfc_sid17: _wrappers_pb2.Int32Value
    dfc_sid18: _wrappers_pb2.Int32Value
    dfc_sid19: _wrappers_pb2.Int32Value
    dfc_sid20: _wrappers_pb2.Int32Value
    dfc_sid21: _wrappers_pb2.Int32Value
    dfc_sid22: _wrappers_pb2.Int32Value
    dfc_sid23: _wrappers_pb2.Int32Value
    dfc_sid24: _wrappers_pb2.Int32Value
    dfc_sid25: _wrappers_pb2.Int32Value
    dfc_sid26: _wrappers_pb2.Int32Value
    dfc_sid27: _wrappers_pb2.Int32Value
    dfc_sid28: _wrappers_pb2.Int32Value
    dfc_sid29: _wrappers_pb2.Int32Value
    dfc_sid30: _wrappers_pb2.Int32Value
    def __init__(self, contact_schema_sid: _Optional[int] = ..., contact_group_sid: _Optional[int] = ..., dfc_sid01: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid02: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid03: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid04: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid05: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid06: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid07: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid08: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid09: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid10: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid11: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid12: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid13: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid14: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid15: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid16: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid17: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid18: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid19: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid20: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid21: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid22: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid23: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid24: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid25: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid26: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid27: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid28: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid29: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid30: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class GetContactSchemaByContactGroupReq(_message.Message):
    __slots__ = ["contact_group_sid"]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    contact_group_sid: int
    def __init__(self, contact_group_sid: _Optional[int] = ...) -> None: ...

class ContactFieldDescription(_message.Message):
    __slots__ = ["contact_field_description_sid", "field_name", "is_phone", "display_format_string"]
    CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
    contact_field_description_sid: int
    field_name: str
    is_phone: bool
    display_format_string: _wrappers_pb2.StringValue
    def __init__(self, contact_field_description_sid: _Optional[int] = ..., field_name: _Optional[str] = ..., is_phone: bool = ..., display_format_string: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ContactGroup(_message.Message):
    __slots__ = ["contact_group_sid", "name", "country_sid", "last_updated", "sha_digest"]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    SHA_DIGEST_FIELD_NUMBER: _ClassVar[int]
    contact_group_sid: int
    name: _wrappers_pb2.StringValue
    country_sid: int
    last_updated: _timestamp_pb2.Timestamp
    sha_digest: _wrappers_pb2.StringValue
    def __init__(self, contact_group_sid: _Optional[int] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., country_sid: _Optional[int] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sha_digest: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class GetContactGroupReq(_message.Message):
    __slots__ = ["contact_group_sid"]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    contact_group_sid: int
    def __init__(self, contact_group_sid: _Optional[int] = ...) -> None: ...

class GetContactGroupSizeRes(_message.Message):
    __slots__ = ["contact_group_size"]
    CONTACT_GROUP_SIZE_FIELD_NUMBER: _ClassVar[int]
    contact_group_size: int
    def __init__(self, contact_group_size: _Optional[int] = ...) -> None: ...

class ListContactGroupDetailsByClientSidReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListContactGroupDetailsByClientSidRes(_message.Message):
    __slots__ = ["contact_group"]
    CONTACT_GROUP_FIELD_NUMBER: _ClassVar[int]
    contact_group: _containers.RepeatedCompositeFieldContainer[ContactGroup]
    def __init__(self, contact_group: _Optional[_Iterable[_Union[ContactGroup, _Mapping]]] = ...) -> None: ...

class CreateContactFieldDescriptionReq(_message.Message):
    __slots__ = ["field_name", "is_phone", "display_format_string"]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    is_phone: bool
    display_format_string: _wrappers_pb2.StringValue
    def __init__(self, field_name: _Optional[str] = ..., is_phone: bool = ..., display_format_string: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class CreateContactFieldDescriptionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteContactFieldDescriptionReq(_message.Message):
    __slots__ = ["contact_field_description_sid"]
    CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
    contact_field_description_sid: int
    def __init__(self, contact_field_description_sid: _Optional[int] = ...) -> None: ...

class DeleteContactFieldDescriptionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListContactFieldDescriptionsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListContactFieldDescriptionsRes(_message.Message):
    __slots__ = ["contact_field_description"]
    CONTACT_FIELD_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    contact_field_description: _containers.RepeatedCompositeFieldContainer[ContactFieldDescription]
    def __init__(self, contact_field_description: _Optional[_Iterable[_Union[ContactFieldDescription, _Mapping]]] = ...) -> None: ...

class ListContactFieldDescriptionsByCGSidReq(_message.Message):
    __slots__ = ["contact_group_sid"]
    CONTACT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    contact_group_sid: int
    def __init__(self, contact_group_sid: _Optional[int] = ...) -> None: ...

class ListContactFieldDescriptionsByCGSidRes(_message.Message):
    __slots__ = ["contact_field_description"]
    CONTACT_FIELD_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    contact_field_description: _containers.RepeatedCompositeFieldContainer[ContactFieldDescription]
    def __init__(self, contact_field_description: _Optional[_Iterable[_Union[ContactFieldDescription, _Mapping]]] = ...) -> None: ...

class ListTableTemplatePropertiesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListTableTemplatePropertiesRes(_message.Message):
    __slots__ = ["agent_table_templates", "queue_table_templates"]
    AGENT_TABLE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    QUEUE_TABLE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    agent_table_templates: _containers.RepeatedCompositeFieldContainer[TableTemplateProperty]
    queue_table_templates: _containers.RepeatedCompositeFieldContainer[TableTemplateProperty]
    def __init__(self, agent_table_templates: _Optional[_Iterable[_Union[TableTemplateProperty, _Mapping]]] = ..., queue_table_templates: _Optional[_Iterable[_Union[TableTemplateProperty, _Mapping]]] = ...) -> None: ...

class TableTemplateProperty(_message.Message):
    __slots__ = ["xml_client_property_sid", "name"]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    name: str
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ListAgentSkillsFiltersReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAgentSkillsFiltersRes(_message.Message):
    __slots__ = ["agent_skills_filters"]
    AGENT_SKILLS_FILTERS_FIELD_NUMBER: _ClassVar[int]
    agent_skills_filters: _containers.RepeatedCompositeFieldContainer[AgentSkillsFilter]
    def __init__(self, agent_skills_filters: _Optional[_Iterable[_Union[AgentSkillsFilter, _Mapping]]] = ...) -> None: ...

class AgentSkillsFilter(_message.Message):
    __slots__ = ["xml_client_property_sid", "name"]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    name: str
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ListCustomReportFiltersReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListCustomReportFiltersRes(_message.Message):
    __slots__ = ["custom_report_filters"]
    CUSTOM_REPORT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    custom_report_filters: _containers.RepeatedCompositeFieldContainer[CustomReportFilterProperty]
    def __init__(self, custom_report_filters: _Optional[_Iterable[_Union[CustomReportFilterProperty, _Mapping]]] = ...) -> None: ...

class CustomReportFilterProperty(_message.Message):
    __slots__ = ["xml_client_property_sid", "name"]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    name: str
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ContactImportTemplate(_message.Message):
    __slots__ = ["contact_import_template_sid", "name", "description", "delimiter", "quote", "is_fixed_width", "dfc_sid01", "dfc_sid02", "dfc_sid03", "dfc_sid04", "dfc_sid05", "dfc_sid06", "dfc_sid07", "dfc_sid08", "dfc_sid09", "dfc_sid10", "dfc_sid11", "dfc_sid12", "dfc_sid13", "dfc_sid14", "dfc_sid15", "dfc_sid16", "dfc_sid17", "dfc_sid18", "dfc_sid19", "dfc_sid20", "dfc_sid21", "dfc_sid22", "dfc_sid23", "dfc_sid24", "dfc_sid25", "dfc_sid26", "dfc_sid27", "dfc_sid28", "dfc_sid29", "dfc_sid30", "field_length01", "field_length02", "field_length03", "field_length04", "field_length05", "field_length06", "field_length07", "field_length08", "field_length09", "field_length10", "field_length11", "field_length12", "field_length13", "field_length14", "field_length15", "field_length16", "field_length17", "field_length18", "field_length19", "field_length20", "field_length21", "field_length22", "field_length23", "field_length24", "field_length25", "field_length26", "field_length27", "field_length28", "field_length29", "field_length30", "template_number", "exclude_first_row"]
    CONTACT_IMPORT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    IS_FIXED_WIDTH_FIELD_NUMBER: _ClassVar[int]
    DFC_SID01_FIELD_NUMBER: _ClassVar[int]
    DFC_SID02_FIELD_NUMBER: _ClassVar[int]
    DFC_SID03_FIELD_NUMBER: _ClassVar[int]
    DFC_SID04_FIELD_NUMBER: _ClassVar[int]
    DFC_SID05_FIELD_NUMBER: _ClassVar[int]
    DFC_SID06_FIELD_NUMBER: _ClassVar[int]
    DFC_SID07_FIELD_NUMBER: _ClassVar[int]
    DFC_SID08_FIELD_NUMBER: _ClassVar[int]
    DFC_SID09_FIELD_NUMBER: _ClassVar[int]
    DFC_SID10_FIELD_NUMBER: _ClassVar[int]
    DFC_SID11_FIELD_NUMBER: _ClassVar[int]
    DFC_SID12_FIELD_NUMBER: _ClassVar[int]
    DFC_SID13_FIELD_NUMBER: _ClassVar[int]
    DFC_SID14_FIELD_NUMBER: _ClassVar[int]
    DFC_SID15_FIELD_NUMBER: _ClassVar[int]
    DFC_SID16_FIELD_NUMBER: _ClassVar[int]
    DFC_SID17_FIELD_NUMBER: _ClassVar[int]
    DFC_SID18_FIELD_NUMBER: _ClassVar[int]
    DFC_SID19_FIELD_NUMBER: _ClassVar[int]
    DFC_SID20_FIELD_NUMBER: _ClassVar[int]
    DFC_SID21_FIELD_NUMBER: _ClassVar[int]
    DFC_SID22_FIELD_NUMBER: _ClassVar[int]
    DFC_SID23_FIELD_NUMBER: _ClassVar[int]
    DFC_SID24_FIELD_NUMBER: _ClassVar[int]
    DFC_SID25_FIELD_NUMBER: _ClassVar[int]
    DFC_SID26_FIELD_NUMBER: _ClassVar[int]
    DFC_SID27_FIELD_NUMBER: _ClassVar[int]
    DFC_SID28_FIELD_NUMBER: _ClassVar[int]
    DFC_SID29_FIELD_NUMBER: _ClassVar[int]
    DFC_SID30_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH01_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH02_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH03_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH04_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH05_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH06_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH07_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH08_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH09_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH10_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH11_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH12_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH13_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH14_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH15_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH16_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH17_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH18_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH19_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH20_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH21_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH22_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH23_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH24_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH25_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH26_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH27_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH28_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH29_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH30_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIRST_ROW_FIELD_NUMBER: _ClassVar[int]
    contact_import_template_sid: int
    name: str
    description: str
    delimiter: _wrappers_pb2.StringValue
    quote: _wrappers_pb2.StringValue
    is_fixed_width: bool
    dfc_sid01: _wrappers_pb2.Int32Value
    dfc_sid02: _wrappers_pb2.Int32Value
    dfc_sid03: _wrappers_pb2.Int32Value
    dfc_sid04: _wrappers_pb2.Int32Value
    dfc_sid05: _wrappers_pb2.Int32Value
    dfc_sid06: _wrappers_pb2.Int32Value
    dfc_sid07: _wrappers_pb2.Int32Value
    dfc_sid08: _wrappers_pb2.Int32Value
    dfc_sid09: _wrappers_pb2.Int32Value
    dfc_sid10: _wrappers_pb2.Int32Value
    dfc_sid11: _wrappers_pb2.Int32Value
    dfc_sid12: _wrappers_pb2.Int32Value
    dfc_sid13: _wrappers_pb2.Int32Value
    dfc_sid14: _wrappers_pb2.Int32Value
    dfc_sid15: _wrappers_pb2.Int32Value
    dfc_sid16: _wrappers_pb2.Int32Value
    dfc_sid17: _wrappers_pb2.Int32Value
    dfc_sid18: _wrappers_pb2.Int32Value
    dfc_sid19: _wrappers_pb2.Int32Value
    dfc_sid20: _wrappers_pb2.Int32Value
    dfc_sid21: _wrappers_pb2.Int32Value
    dfc_sid22: _wrappers_pb2.Int32Value
    dfc_sid23: _wrappers_pb2.Int32Value
    dfc_sid24: _wrappers_pb2.Int32Value
    dfc_sid25: _wrappers_pb2.Int32Value
    dfc_sid26: _wrappers_pb2.Int32Value
    dfc_sid27: _wrappers_pb2.Int32Value
    dfc_sid28: _wrappers_pb2.Int32Value
    dfc_sid29: _wrappers_pb2.Int32Value
    dfc_sid30: _wrappers_pb2.Int32Value
    field_length01: _wrappers_pb2.Int32Value
    field_length02: _wrappers_pb2.Int32Value
    field_length03: _wrappers_pb2.Int32Value
    field_length04: _wrappers_pb2.Int32Value
    field_length05: _wrappers_pb2.Int32Value
    field_length06: _wrappers_pb2.Int32Value
    field_length07: _wrappers_pb2.Int32Value
    field_length08: _wrappers_pb2.Int32Value
    field_length09: _wrappers_pb2.Int32Value
    field_length10: _wrappers_pb2.Int32Value
    field_length11: _wrappers_pb2.Int32Value
    field_length12: _wrappers_pb2.Int32Value
    field_length13: _wrappers_pb2.Int32Value
    field_length14: _wrappers_pb2.Int32Value
    field_length15: _wrappers_pb2.Int32Value
    field_length16: _wrappers_pb2.Int32Value
    field_length17: _wrappers_pb2.Int32Value
    field_length18: _wrappers_pb2.Int32Value
    field_length19: _wrappers_pb2.Int32Value
    field_length20: _wrappers_pb2.Int32Value
    field_length21: _wrappers_pb2.Int32Value
    field_length22: _wrappers_pb2.Int32Value
    field_length23: _wrappers_pb2.Int32Value
    field_length24: _wrappers_pb2.Int32Value
    field_length25: _wrappers_pb2.Int32Value
    field_length26: _wrappers_pb2.Int32Value
    field_length27: _wrappers_pb2.Int32Value
    field_length28: _wrappers_pb2.Int32Value
    field_length29: _wrappers_pb2.Int32Value
    field_length30: _wrappers_pb2.Int32Value
    template_number: int
    exclude_first_row: _wrappers_pb2.BoolValue
    def __init__(self, contact_import_template_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., delimiter: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., quote: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., is_fixed_width: bool = ..., dfc_sid01: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid02: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid03: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid04: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid05: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid06: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid07: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid08: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid09: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid10: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid11: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid12: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid13: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid14: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid15: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid16: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid17: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid18: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid19: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid20: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid21: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid22: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid23: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid24: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid25: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid26: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid27: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid28: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid29: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., dfc_sid30: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length01: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length02: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length03: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length04: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length05: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length06: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length07: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length08: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length09: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length10: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length11: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length12: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length13: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length14: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length15: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length16: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length17: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length18: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length19: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length20: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length21: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length22: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length23: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length24: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length25: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length26: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length27: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length28: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length29: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., field_length30: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., template_number: _Optional[int] = ..., exclude_first_row: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ListContactImportTemplatesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListContactImportTemplatesRes(_message.Message):
    __slots__ = ["contact_import_template"]
    CONTACT_IMPORT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    contact_import_template: _containers.RepeatedCompositeFieldContainer[ContactImportTemplate]
    def __init__(self, contact_import_template: _Optional[_Iterable[_Union[ContactImportTemplate, _Mapping]]] = ...) -> None: ...

class UpdatePreviewRecordToFinishedReq(_message.Message):
    __slots__ = ["agent_session_sid", "task_sid"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    task_sid: int
    def __init__(self, agent_session_sid: _Optional[int] = ..., task_sid: _Optional[int] = ...) -> None: ...

class UpdatePreviewRecordToFinishedRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAgentHuntGroupReq(_message.Message):
    __slots__ = ["hunt_group_sid", "user_id"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    user_id: str
    def __init__(self, hunt_group_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateAgentHuntGroupRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MultiAgentHuntGroupAssignmentReq(_message.Message):
    __slots__ = ["user_ids", "hunt_group_sid"]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    hunt_group_sid: int
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class MultiAgentHuntGroupAssignmentRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAgentProfileReq(_message.Message):
    __slots__ = ["agent_sid"]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    def __init__(self, agent_sid: _Optional[int] = ...) -> None: ...

class AgentProfile(_message.Message):
    __slots__ = ["first_name", "last_name"]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...

class RecalculateBillingReq(_message.Message):
    __slots__ = ["month", "types", "org_id"]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    month: _p3api_pb2.RecalculateBillingMonth
    types: _containers.RepeatedScalarFieldContainer[_p3api_pb2.RecalculateBillingType]
    org_id: str
    def __init__(self, month: _Optional[_Union[_p3api_pb2.RecalculateBillingMonth, str]] = ..., types: _Optional[_Iterable[_Union[_p3api_pb2.RecalculateBillingType, str]]] = ..., org_id: _Optional[str] = ...) -> None: ...

class RecalculateBillingRes(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["type", "updated", "error_message"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        type: _p3api_pb2.RecalculateBillingType
        updated: int
        error_message: str
        def __init__(self, type: _Optional[_Union[_p3api_pb2.RecalculateBillingType, str]] = ..., updated: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[RecalculateBillingRes.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[RecalculateBillingRes.Result, _Mapping]]] = ...) -> None: ...

class ListOutboundBroadcastTemplateDataReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOutboundBroadcastTemplateDataRes(_message.Message):
    __slots__ = ["templates"]
    class Data(_message.Message):
        __slots__ = ["template_number", "template_name", "template_type", "modify_date"]
        TEMPLATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MODIFY_DATE_FIELD_NUMBER: _ClassVar[int]
        template_number: int
        template_name: str
        template_type: _broadcasts_pb2.TemplateType.Enum
        modify_date: _timestamp_pb2.Timestamp
        def __init__(self, template_number: _Optional[int] = ..., template_name: _Optional[str] = ..., template_type: _Optional[_Union[_broadcasts_pb2.TemplateType.Enum, str]] = ..., modify_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[ListOutboundBroadcastTemplateDataRes.Data]
    def __init__(self, templates: _Optional[_Iterable[_Union[ListOutboundBroadcastTemplateDataRes.Data, _Mapping]]] = ...) -> None: ...

class MultiAgentSkillAssignmentReq(_message.Message):
    __slots__ = ["user_ids", "skills"]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    skills: _containers.RepeatedCompositeFieldContainer[SkillUpdate]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., skills: _Optional[_Iterable[_Union[SkillUpdate, _Mapping]]] = ...) -> None: ...

class MultiAgentSkillAssignmentRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MultiAgentSkillUnassignmentReq(_message.Message):
    __slots__ = ["user_ids", "skill_sids"]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_SIDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    skill_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_ids: _Optional[_Iterable[str]] = ..., skill_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class MultiAgentSkillUnassignmentRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListMAMAgentHuntGroupsByClientSidReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListMAMAgentHuntGroupsByClientSidRes(_message.Message):
    __slots__ = ["hunt_group"]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    hunt_group: _containers.RepeatedCompositeFieldContainer[HuntGroup]
    def __init__(self, hunt_group: _Optional[_Iterable[_Union[HuntGroup, _Mapping]]] = ...) -> None: ...

class UpdateAgentSkillsReq(_message.Message):
    __slots__ = ["user_id", "skills"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    skills: _containers.RepeatedCompositeFieldContainer[SkillUpdate]
    def __init__(self, user_id: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[SkillUpdate, _Mapping]]] = ...) -> None: ...

class SkillUpdate(_message.Message):
    __slots__ = ["skill_sid", "level"]
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    skill_sid: int
    level: int
    def __init__(self, skill_sid: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...

class UpdateAgentSkillsRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListTtsVoicesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListTtsVoicesRes(_message.Message):
    __slots__ = ["voices"]
    VOICES_FIELD_NUMBER: _ClassVar[int]
    voices: _containers.RepeatedCompositeFieldContainer[TtsVoice]
    def __init__(self, voices: _Optional[_Iterable[_Union[TtsVoice, _Mapping]]] = ...) -> None: ...

class TtsVoice(_message.Message):
    __slots__ = ["tts_voice_sid", "display_name", "actual_name", "port"]
    TTS_VOICE_SID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    tts_voice_sid: int
    display_name: str
    actual_name: str
    port: int
    def __init__(self, tts_voice_sid: _Optional[int] = ..., display_name: _Optional[str] = ..., actual_name: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class CreateTtsVoiceReq(_message.Message):
    __slots__ = ["actual_name", "display_name", "port"]
    ACTUAL_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    actual_name: str
    display_name: str
    port: int
    def __init__(self, actual_name: _Optional[str] = ..., display_name: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class CreateTtsVoiceRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTtsVoiceReq(_message.Message):
    __slots__ = ["tts_voice_sid"]
    TTS_VOICE_SID_FIELD_NUMBER: _ClassVar[int]
    tts_voice_sid: int
    def __init__(self, tts_voice_sid: _Optional[int] = ...) -> None: ...

class DeleteTtsVoiceRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CustomDataKey(_message.Message):
    __slots__ = ["name", "value", "client_properties_sid"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PROPERTIES_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    client_properties_sid: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., client_properties_sid: _Optional[int] = ...) -> None: ...

class ListCustomDataKeysReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListCustomDataKeysRes(_message.Message):
    __slots__ = ["data_keys"]
    DATA_KEYS_FIELD_NUMBER: _ClassVar[int]
    data_keys: _containers.RepeatedCompositeFieldContainer[CustomDataKey]
    def __init__(self, data_keys: _Optional[_Iterable[_Union[CustomDataKey, _Mapping]]] = ...) -> None: ...

class CreateCustomDataKeyReq(_message.Message):
    __slots__ = ["data_key"]
    DATA_KEY_FIELD_NUMBER: _ClassVar[int]
    data_key: CustomDataKey
    def __init__(self, data_key: _Optional[_Union[CustomDataKey, _Mapping]] = ...) -> None: ...

class CreateCustomDataKeyRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteCustomDataKeyReq(_message.Message):
    __slots__ = ["client_properties_sid"]
    CLIENT_PROPERTIES_SID_FIELD_NUMBER: _ClassVar[int]
    client_properties_sid: int
    def __init__(self, client_properties_sid: _Optional[int] = ...) -> None: ...

class DeleteCustomDataKeyRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCustomDataKeyReq(_message.Message):
    __slots__ = ["dataKey"]
    DATAKEY_FIELD_NUMBER: _ClassVar[int]
    dataKey: CustomDataKey
    def __init__(self, dataKey: _Optional[_Union[CustomDataKey, _Mapping]] = ...) -> None: ...

class UpdateCustomDataKeyRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Extension(_message.Message):
    __slots__ = ["pbx_extension_sid", "extension_number", "agent", "hunt_group", "agent_access", "email", "greeting", "has_greeting", "unheard_messages", "total_messages"]
    class Agent(_message.Message):
        __slots__ = ["first_name", "last_name", "user_id"]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        user_id: str
        def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
    class HuntGroup(_message.Message):
        __slots__ = ["hunt_group_sid", "hunt_group_name"]
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    class Email(_message.Message):
        __slots__ = ["subject", "body", "addresses", "attach_vm"]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        ATTACH_VM_FIELD_NUMBER: _ClassVar[int]
        subject: str
        body: str
        addresses: _containers.RepeatedScalarFieldContainer[str]
        attach_vm: bool
        def __init__(self, subject: _Optional[str] = ..., body: _Optional[str] = ..., addresses: _Optional[_Iterable[str]] = ..., attach_vm: bool = ...) -> None: ...
    PBX_EXTENSION_SID_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    AGENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GREETING_FIELD_NUMBER: _ClassVar[int]
    HAS_GREETING_FIELD_NUMBER: _ClassVar[int]
    UNHEARD_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    pbx_extension_sid: int
    extension_number: str
    agent: Extension.Agent
    hunt_group: Extension.HuntGroup
    agent_access: bool
    email: Extension.Email
    greeting: str
    has_greeting: bool
    unheard_messages: int
    total_messages: int
    def __init__(self, pbx_extension_sid: _Optional[int] = ..., extension_number: _Optional[str] = ..., agent: _Optional[_Union[Extension.Agent, _Mapping]] = ..., hunt_group: _Optional[_Union[Extension.HuntGroup, _Mapping]] = ..., agent_access: bool = ..., email: _Optional[_Union[Extension.Email, _Mapping]] = ..., greeting: _Optional[str] = ..., has_greeting: bool = ..., unheard_messages: _Optional[int] = ..., total_messages: _Optional[int] = ...) -> None: ...

class ListAgentExtensionsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAgentExtensionsRes(_message.Message):
    __slots__ = ["extensions"]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    def __init__(self, extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...) -> None: ...

class ListHuntGroupExtensionsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListHuntGroupExtensionsRes(_message.Message):
    __slots__ = ["extensions"]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    def __init__(self, extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...) -> None: ...

class CreateExtensionReq(_message.Message):
    __slots__ = ["extension_message"]
    EXTENSION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    extension_message: Extension
    def __init__(self, extension_message: _Optional[_Union[Extension, _Mapping]] = ...) -> None: ...

class CreateExtensionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateExtensionReq(_message.Message):
    __slots__ = ["extension_message"]
    EXTENSION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    extension_message: Extension
    def __init__(self, extension_message: _Optional[_Union[Extension, _Mapping]] = ...) -> None: ...

class UpdateExtensionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteExtensionReq(_message.Message):
    __slots__ = ["pbx_extension_sid"]
    PBX_EXTENSION_SID_FIELD_NUMBER: _ClassVar[int]
    pbx_extension_sid: int
    def __init__(self, pbx_extension_sid: _Optional[int] = ...) -> None: ...

class DeleteExtensionRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetActivityLogHistoryReq(_message.Message):
    __slots__ = ["day_filter", "user_name", "org_id"]
    DAY_FILTER_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    day_filter: int
    user_name: str
    org_id: str
    def __init__(self, day_filter: _Optional[int] = ..., user_name: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetActivityLogHistoryRes(_message.Message):
    __slots__ = ["activity_logs"]
    ACTIVITY_LOGS_FIELD_NUMBER: _ClassVar[int]
    activity_logs: _containers.RepeatedCompositeFieldContainer[ActivityLog]
    def __init__(self, activity_logs: _Optional[_Iterable[_Union[ActivityLog, _Mapping]]] = ...) -> None: ...

class ActivityLog(_message.Message):
    __slots__ = ["user_name", "origination_ip", "action_date", "action", "notes"]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINATION_IP_FIELD_NUMBER: _ClassVar[int]
    ACTION_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    user_name: _wrappers_pb2.StringValue
    origination_ip: _wrappers_pb2.StringValue
    action_date: _wrappers_pb2.StringValue
    action: _wrappers_pb2.StringValue
    notes: _wrappers_pb2.StringValue
    def __init__(self, user_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., origination_ip: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., action_date: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., action: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., notes: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ListSkillsReq(_message.Message):
    __slots__ = ["type_filters"]
    TYPE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    type_filters: _containers.RepeatedScalarFieldContainer[_wfm_pb2.SkillType.Enum]
    def __init__(self, type_filters: _Optional[_Iterable[_Union[_wfm_pb2.SkillType.Enum, str]]] = ...) -> None: ...

class ListSkillsRes(_message.Message):
    __slots__ = ["skills"]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[P3Skill]
    def __init__(self, skills: _Optional[_Iterable[_Union[P3Skill, _Mapping]]] = ...) -> None: ...

class P3Skill(_message.Message):
    __slots__ = ["region", "p3_id", "name", "description", "type"]
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

class ListScheduleRulesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListScheduleRulesResult(_message.Message):
    __slots__ = ["schedule_rules"]
    SCHEDULE_RULES_FIELD_NUMBER: _ClassVar[int]
    schedule_rules: _containers.RepeatedCompositeFieldContainer[ScheduleRule]
    def __init__(self, schedule_rules: _Optional[_Iterable[_Union[ScheduleRule, _Mapping]]] = ...) -> None: ...

class ScheduleRule(_message.Message):
    __slots__ = ["schedule_rule_sid", "client_sid", "name", "rule_time_zone"]
    SCHEDULE_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    schedule_rule_sid: int
    client_sid: _wrappers_pb2.Int64Value
    name: _wrappers_pb2.StringValue
    rule_time_zone: _wrappers_pb2.StringValue
    def __init__(self, schedule_rule_sid: _Optional[int] = ..., client_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rule_time_zone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ListSmsNumbersReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListSmsNumbersRes(_message.Message):
    __slots__ = ["sms_numbers"]
    SMS_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    sms_numbers: _containers.RepeatedCompositeFieldContainer[_omnichannel_pb2.SmsNumber]
    def __init__(self, sms_numbers: _Optional[_Iterable[_Union[_omnichannel_pb2.SmsNumber, _Mapping]]] = ...) -> None: ...
