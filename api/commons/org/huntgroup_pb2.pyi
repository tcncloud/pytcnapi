from api.commons import country_pb2 as _country_pb2
from api.commons import org_pb2 as _org_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HuntGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUNT_GROUP_TYPE_UNSPECIFIED: _ClassVar[HuntGroupType]
    HUNT_GROUP_TYPE_CONNECTED: _ClassVar[HuntGroupType]
    HUNT_GROUP_TYPE_SOFTPHONE: _ClassVar[HuntGroupType]

class TemplateCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_CATEGORY_UNSPECIFIED: _ClassVar[TemplateCategory]
    TEMPLATE_CATEGORY_HUNT_GROUP: _ClassVar[TemplateCategory]
    TEMPLATE_CATEGORY_CAMPAIGN: _ClassVar[TemplateCategory]

class WebLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_LINK_TYPE_UNSPECIFIED: _ClassVar[WebLinkType]
    WEB_LINK_STANDARD: _ClassVar[WebLinkType]
    WEB_LINK_JAVASCRIPT: _ClassVar[WebLinkType]

class WebLinkComponentKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_LINK_COMPONENT_KEY_TYPE_UNSPECIFIED: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_STATIC_TEXT: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_TTS_FIELD: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_AGENT_INFO: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_DATA_DIP: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_IVR_DATA: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_DATA_COLLECT: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_PHONE_METADATA: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_ZIP_POSTAL_METADATA: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_CUSTOM_ACCOUNT_DATA_KEY: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_SIP_HEADER_DATA: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_INTEGRATION_DATA: _ClassVar[WebLinkComponentKeyType]
    WEB_LINK_COMPONENT_KEY_TYPE_JOURNEY_DATA: _ClassVar[WebLinkComponentKeyType]

class ParameterSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARAMETER_SOURCE_TYPE_UNSPECIFIED: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_STATIC_TEXT: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_CFD_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_AGENT_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_AGENT_FIRST_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_AGENT_LAST_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_AGENT_USERNAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PARTNER_AGENT_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_HG_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_HG_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_HG_TYPE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_CONSUMER_PHONE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_CALLER_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_CALL_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_GROUP_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_AGENT_SESSION_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_DATA_DIP: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_IVR_DATA: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_DATA_COLLECT: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_AREA_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_CARRIER: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_CENTRAL_OFFICE_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_CITY: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_COUNTRY_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_SUBSCRIBER_NUMBER: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_ISO_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_INTERNATIONAL_PREFIX: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_LANGUAGE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_LATITUDE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_LONGITUDE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_MAXIMUM_BLOCK_NUMBER: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_MINIMUM_BLOCK_NUMBER: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_NATIONAL_DESTINATION: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_NATIONAL_PREFIX: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_NUMBER_BLOCK_ID: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_NUMBER_TYPE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_USES_NDC: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_DAYLIGHT_SAVINGS: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_PREFIX: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_REGION_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_REGION_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_1: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_2: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_3: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_4: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_TIME_ZONE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_PHONE_METADATA_UTC_OFFSET: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_1: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_2: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_3: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_1: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_2: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_3: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_AREA_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_CITY_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_CITY_TYPE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_ISO_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_FPS_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_LATITUDE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSITION_ACCURACY: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_LONGITUDE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_METROPOLITAN_AREA: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_DAYLIGHT_SAVINGS: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_PLACE_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_CODE_KEY: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_TYPE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_PROVICE_ABBREVIATION: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_PROVINCE_NAME: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_STATE_FPS_CODE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_TIME_ZONE: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_ZIP_METADATA_UTC_OFFSET: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_CUSTOM_ACCOUNT_DATA: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_SIP_HEADER_DATA: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_INTEGRATION_DATA: _ClassVar[ParameterSourceType]
    PARAMETER_SOURCE_TYPE_JOURNEY_DATA: _ClassVar[ParameterSourceType]

class AgentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_STATUS_UNSPECIFIED: _ClassVar[AgentStatus]
    AGENT_STATUS_LOGGED_IN: _ClassVar[AgentStatus]
    AGENT_STATUS_WAITING: _ClassVar[AgentStatus]
    AGENT_STATUS_PAUSED: _ClassVar[AgentStatus]
    AGENT_STATUS_ON_CALL: _ClassVar[AgentStatus]
    AGENT_STATUS_TRANSFER_CALL: _ClassVar[AgentStatus]
    AGENT_STATUS_TRANSFER_LOST: _ClassVar[AgentStatus]
    AGENT_STATUS_TRANSFER_TARGET_LOST: _ClassVar[AgentStatus]
    AGENT_STATUS_PREVIEW_CALL: _ClassVar[AgentStatus]
    AGENT_STATUS_MANUAL_DIAL_CALL: _ClassVar[AgentStatus]
    AGENT_STATUS_WRAP_UP: _ClassVar[AgentStatus]

class SystemPauseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYSTEM_PAUSE_CODE_UNSPECIFIED: _ClassVar[SystemPauseCode]
    SYSTEM_PAUSE_CODE_AGENT_TRIGGER_ADVANCE_TO_PAUSED: _ClassVar[SystemPauseCode]
    SYSTEM_PAUSE_CODE_CHANGE_PASSWORD: _ClassVar[SystemPauseCode]
    SYSTEM_PAUSE_CODE_CHECK_VOICE_MAIL: _ClassVar[SystemPauseCode]
    SYSTEM_PAUSE_CODE_MANUALLY_APPROVE_CALLS: _ClassVar[SystemPauseCode]

class TriggerAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_ACTION_UNSPECIFIED: _ClassVar[TriggerAction]
    TRIGGER_ACTION_ADVANCE_TO_STATUS: _ClassVar[TriggerAction]
    TRIGGER_ACTION_DISPLAY_MESSAGE: _ClassVar[TriggerAction]
    TRIGGER_ACTION_EJECT_AGENT: _ClassVar[TriggerAction]
    TRIGGER_ACTION_EXECUTE_WEB_LINK: _ClassVar[TriggerAction]
    TRIGGER_ACTION_EXECUTE_INTEGRATION_LINK: _ClassVar[TriggerAction]

class ScriptCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCRIPT_CATEGORY_UNSPECIFIED: _ClassVar[ScriptCategory]
    SCRIPT_CATEGORY_HUNT_GROUP: _ClassVar[ScriptCategory]
    SCRIPT_CATEGORY_CAMPAIGN: _ClassVar[ScriptCategory]

class ScriptResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCRIPT_RESPONSE_TYPE_UNSPECIFIED: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_DROP_DOWN_SELECT_MENU: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_MULTIPLE_SELECT_MENU: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_CHECK_BOXES: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_RADIO_BUTTONS: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_TEXT_BOX: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_TEXT_BOX_ALPHANUMERIC: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_TEXT_BOX_NUMERICAL: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_TEXT_VERIFICATION_FIELD: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_TEXT_AREA: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_REGULAR_EXPRESSION_FIELD: _ClassVar[ScriptResponseType]
    SCRIPT_RESPONSE_TYPE_REGULAR_EXPRESSION_AREA: _ClassVar[ScriptResponseType]

class CompareOperatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPARE_OPERATOR_TYPE_UNSPECIFIED: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_EQUALS: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_NOT_EQUALS: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_GREATER_THAN: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_LESS_THAN: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_GREATER_THAN_OR_EQUAL_TO: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_LESS_THAN_OR_EQUAL_TO: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_CONTAINS: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_DOES_NOT_CONTAIN: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_BLANK: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_NOT_BALNK: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_STARTS_WITH: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_DOES_NOT_START_WITH: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_ENDS_WITH: _ClassVar[CompareOperatorType]
    COMPARE_OPERATOR_TYPE_DOES_NOT_END_WITH: _ClassVar[CompareOperatorType]
HUNT_GROUP_TYPE_UNSPECIFIED: HuntGroupType
HUNT_GROUP_TYPE_CONNECTED: HuntGroupType
HUNT_GROUP_TYPE_SOFTPHONE: HuntGroupType
TEMPLATE_CATEGORY_UNSPECIFIED: TemplateCategory
TEMPLATE_CATEGORY_HUNT_GROUP: TemplateCategory
TEMPLATE_CATEGORY_CAMPAIGN: TemplateCategory
WEB_LINK_TYPE_UNSPECIFIED: WebLinkType
WEB_LINK_STANDARD: WebLinkType
WEB_LINK_JAVASCRIPT: WebLinkType
WEB_LINK_COMPONENT_KEY_TYPE_UNSPECIFIED: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_STATIC_TEXT: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_TTS_FIELD: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_AGENT_INFO: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_DATA_DIP: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_IVR_DATA: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_DATA_COLLECT: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_PHONE_METADATA: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_ZIP_POSTAL_METADATA: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_CUSTOM_ACCOUNT_DATA_KEY: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_SIP_HEADER_DATA: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_INTEGRATION_DATA: WebLinkComponentKeyType
WEB_LINK_COMPONENT_KEY_TYPE_JOURNEY_DATA: WebLinkComponentKeyType
PARAMETER_SOURCE_TYPE_UNSPECIFIED: ParameterSourceType
PARAMETER_SOURCE_TYPE_STATIC_TEXT: ParameterSourceType
PARAMETER_SOURCE_TYPE_CFD_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_AGENT_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_AGENT_FIRST_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_AGENT_LAST_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_AGENT_USERNAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_PARTNER_AGENT_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_HG_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_HG_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_HG_TYPE: ParameterSourceType
PARAMETER_SOURCE_TYPE_CONSUMER_PHONE: ParameterSourceType
PARAMETER_SOURCE_TYPE_CALLER_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_CALL_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_GROUP_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_AGENT_SESSION_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_DATA_DIP: ParameterSourceType
PARAMETER_SOURCE_TYPE_IVR_DATA: ParameterSourceType
PARAMETER_SOURCE_TYPE_DATA_COLLECT: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_AREA_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_CARRIER: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_CENTRAL_OFFICE_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_CITY: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_COUNTRY_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_SUBSCRIBER_NUMBER: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_ISO_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_INTERNATIONAL_PREFIX: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_LANGUAGE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_LATITUDE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_LONGITUDE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_MAXIMUM_BLOCK_NUMBER: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_MINIMUM_BLOCK_NUMBER: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_NATIONAL_DESTINATION: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_NATIONAL_PREFIX: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_NUMBER_BLOCK_ID: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_NUMBER_TYPE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_USES_NDC: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_DAYLIGHT_SAVINGS: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_PREFIX: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_REGION_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_REGION_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_1: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_2: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_3: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_SPECIAL_SERVICE_CODE_4: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_TIME_ZONE: ParameterSourceType
PARAMETER_SOURCE_TYPE_PHONE_METADATA_UTC_OFFSET: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_1: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_2: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_CODE_3: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_1: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_2: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ADMIN_NAME_3: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_AREA_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_CITY_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_CITY_TYPE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_ISO_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_COUNTRY_FPS_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_LATITUDE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSITION_ACCURACY: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_LONGITUDE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_METROPOLITAN_AREA: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_DAYLIGHT_SAVINGS: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_PLACE_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_CODE_KEY: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_POSTAL_TYPE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_PROVICE_ABBREVIATION: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_PROVINCE_NAME: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_STATE_FPS_CODE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_TIME_ZONE: ParameterSourceType
PARAMETER_SOURCE_TYPE_ZIP_METADATA_UTC_OFFSET: ParameterSourceType
PARAMETER_SOURCE_TYPE_CUSTOM_ACCOUNT_DATA: ParameterSourceType
PARAMETER_SOURCE_TYPE_SIP_HEADER_DATA: ParameterSourceType
PARAMETER_SOURCE_TYPE_INTEGRATION_DATA: ParameterSourceType
PARAMETER_SOURCE_TYPE_JOURNEY_DATA: ParameterSourceType
AGENT_STATUS_UNSPECIFIED: AgentStatus
AGENT_STATUS_LOGGED_IN: AgentStatus
AGENT_STATUS_WAITING: AgentStatus
AGENT_STATUS_PAUSED: AgentStatus
AGENT_STATUS_ON_CALL: AgentStatus
AGENT_STATUS_TRANSFER_CALL: AgentStatus
AGENT_STATUS_TRANSFER_LOST: AgentStatus
AGENT_STATUS_TRANSFER_TARGET_LOST: AgentStatus
AGENT_STATUS_PREVIEW_CALL: AgentStatus
AGENT_STATUS_MANUAL_DIAL_CALL: AgentStatus
AGENT_STATUS_WRAP_UP: AgentStatus
SYSTEM_PAUSE_CODE_UNSPECIFIED: SystemPauseCode
SYSTEM_PAUSE_CODE_AGENT_TRIGGER_ADVANCE_TO_PAUSED: SystemPauseCode
SYSTEM_PAUSE_CODE_CHANGE_PASSWORD: SystemPauseCode
SYSTEM_PAUSE_CODE_CHECK_VOICE_MAIL: SystemPauseCode
SYSTEM_PAUSE_CODE_MANUALLY_APPROVE_CALLS: SystemPauseCode
TRIGGER_ACTION_UNSPECIFIED: TriggerAction
TRIGGER_ACTION_ADVANCE_TO_STATUS: TriggerAction
TRIGGER_ACTION_DISPLAY_MESSAGE: TriggerAction
TRIGGER_ACTION_EJECT_AGENT: TriggerAction
TRIGGER_ACTION_EXECUTE_WEB_LINK: TriggerAction
TRIGGER_ACTION_EXECUTE_INTEGRATION_LINK: TriggerAction
SCRIPT_CATEGORY_UNSPECIFIED: ScriptCategory
SCRIPT_CATEGORY_HUNT_GROUP: ScriptCategory
SCRIPT_CATEGORY_CAMPAIGN: ScriptCategory
SCRIPT_RESPONSE_TYPE_UNSPECIFIED: ScriptResponseType
SCRIPT_RESPONSE_TYPE_DROP_DOWN_SELECT_MENU: ScriptResponseType
SCRIPT_RESPONSE_TYPE_MULTIPLE_SELECT_MENU: ScriptResponseType
SCRIPT_RESPONSE_TYPE_CHECK_BOXES: ScriptResponseType
SCRIPT_RESPONSE_TYPE_RADIO_BUTTONS: ScriptResponseType
SCRIPT_RESPONSE_TYPE_TEXT_BOX: ScriptResponseType
SCRIPT_RESPONSE_TYPE_TEXT_BOX_ALPHANUMERIC: ScriptResponseType
SCRIPT_RESPONSE_TYPE_TEXT_BOX_NUMERICAL: ScriptResponseType
SCRIPT_RESPONSE_TYPE_TEXT_VERIFICATION_FIELD: ScriptResponseType
SCRIPT_RESPONSE_TYPE_TEXT_AREA: ScriptResponseType
SCRIPT_RESPONSE_TYPE_REGULAR_EXPRESSION_FIELD: ScriptResponseType
SCRIPT_RESPONSE_TYPE_REGULAR_EXPRESSION_AREA: ScriptResponseType
COMPARE_OPERATOR_TYPE_UNSPECIFIED: CompareOperatorType
COMPARE_OPERATOR_TYPE_EQUALS: CompareOperatorType
COMPARE_OPERATOR_TYPE_NOT_EQUALS: CompareOperatorType
COMPARE_OPERATOR_TYPE_GREATER_THAN: CompareOperatorType
COMPARE_OPERATOR_TYPE_LESS_THAN: CompareOperatorType
COMPARE_OPERATOR_TYPE_GREATER_THAN_OR_EQUAL_TO: CompareOperatorType
COMPARE_OPERATOR_TYPE_LESS_THAN_OR_EQUAL_TO: CompareOperatorType
COMPARE_OPERATOR_TYPE_CONTAINS: CompareOperatorType
COMPARE_OPERATOR_TYPE_DOES_NOT_CONTAIN: CompareOperatorType
COMPARE_OPERATOR_TYPE_BLANK: CompareOperatorType
COMPARE_OPERATOR_TYPE_NOT_BALNK: CompareOperatorType
COMPARE_OPERATOR_TYPE_STARTS_WITH: CompareOperatorType
COMPARE_OPERATOR_TYPE_DOES_NOT_START_WITH: CompareOperatorType
COMPARE_OPERATOR_TYPE_ENDS_WITH: CompareOperatorType
COMPARE_OPERATOR_TYPE_DOES_NOT_END_WITH: CompareOperatorType

class HuntGroupSettings(_message.Message):
    __slots__ = ("general_settings", "communication_settings", "callback_settings", "preview_dial_settings", "manual_dial_settings", "transfer_call_settings", "number_history_settings")
    GENERAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CALL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_HISTORY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    general_settings: GeneralSettings
    communication_settings: CommunicationSettings
    callback_settings: CallbackSettings
    preview_dial_settings: PreviewDialSettings
    manual_dial_settings: ManualDialSettings
    transfer_call_settings: TransferCallSettings
    number_history_settings: NumberHistorySettings
    def __init__(self, general_settings: _Optional[_Union[GeneralSettings, _Mapping]] = ..., communication_settings: _Optional[_Union[CommunicationSettings, _Mapping]] = ..., callback_settings: _Optional[_Union[CallbackSettings, _Mapping]] = ..., preview_dial_settings: _Optional[_Union[PreviewDialSettings, _Mapping]] = ..., manual_dial_settings: _Optional[_Union[ManualDialSettings, _Mapping]] = ..., transfer_call_settings: _Optional[_Union[TransferCallSettings, _Mapping]] = ..., number_history_settings: _Optional[_Union[NumberHistorySettings, _Mapping]] = ...) -> None: ...

class GeneralSettings(_message.Message):
    __slots__ = ("enable_agent_gateway_title_bar", "default_agent_dial_in", "require_end_call_confirmation", "enable_authorization_by_ip", "authorized_ip_addresses", "initial_agent_status", "enable_agent_pause", "agent_pause_option_set", "default_agent_pause_option", "enable_pause_option_reset", "triggered_pause_status_pause_code_waiting", "triggered_pause_status_pause_code_wrapup", "display_recording_indicator", "enable_call_recording_pause", "call_recording_pause_confirmation", "call_recording_delay", "enable_pause_recording_on_hold", "enable_envision_screen_recording", "agent_screen_recording", "enable_agent_simple_hold", "enable_agent_multi_accept", "pause_agent_after_multi_accept", "hold_queue_monitoring", "display_machine_deliver", "display_linkback_hunt_group", "display_sip_header_data", "display_ivr_navigation_keys", "display_data_collect_data", "display_data_dipped_data", "integration_data_display", "journey_data_display", "agent_call_history_scope", "agent_login_gui_statistics_display", "phone_zip_metadata_display", "display_skills", "display_web_links", "enable_agent_hunt_group_reassignment", "disallowed_hunt_groups", "enable_manual_approval_of_calls", "require_manual_approval_number", "enable_manual_approval_of_sms", "require_manual_approval_number_sms", "disable_reject_option_for_approvers", "alphanumeric_keypad", "enable_call_desktop_notifications", "inbound_compliance_metadata", "enable_agent_intercom", "prepare_state_call_delivery")
    class PauseOptionSet(_message.Message):
        __slots__ = ("enabled", "set_sid")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        SET_SID_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        set_sid: int
        def __init__(self, enabled: bool = ..., set_sid: _Optional[int] = ...) -> None: ...
    class HoldQueueMonitoring(_message.Message):
        __slots__ = ("enabled", "agent_routing", "required_hunt_group_routing", "preferred_hunt_group_routing")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        AGENT_ROUTING_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_HUNT_GROUP_ROUTING_FIELD_NUMBER: _ClassVar[int]
        PREFERRED_HUNT_GROUP_ROUTING_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        agent_routing: _org_pb2.AgentRouting
        required_hunt_group_routing: int
        preferred_hunt_group_routing: int
        def __init__(self, enabled: bool = ..., agent_routing: _Optional[_Union[_org_pb2.AgentRouting, str]] = ..., required_hunt_group_routing: _Optional[int] = ..., preferred_hunt_group_routing: _Optional[int] = ...) -> None: ...
    class DataDipDataDisplay(_message.Message):
        __slots__ = ("display_data_dip_data", "data_dip_display_keys")
        DISPLAY_DATA_DIP_DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_DIP_DISPLAY_KEYS_FIELD_NUMBER: _ClassVar[int]
        display_data_dip_data: bool
        data_dip_display_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, display_data_dip_data: bool = ..., data_dip_display_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class IntegrationDataDisplay(_message.Message):
        __slots__ = ("display_integration_data", "integration_display_keys")
        DISPLAY_INTEGRATION_DATA_FIELD_NUMBER: _ClassVar[int]
        INTEGRATION_DISPLAY_KEYS_FIELD_NUMBER: _ClassVar[int]
        display_integration_data: bool
        integration_display_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, display_integration_data: bool = ..., integration_display_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class JourneyDataDisplay(_message.Message):
        __slots__ = ("display_journey_data", "journey_display_keys")
        DISPLAY_JOURNEY_DATA_FIELD_NUMBER: _ClassVar[int]
        JOURNEY_DISPLAY_KEYS_FIELD_NUMBER: _ClassVar[int]
        display_journey_data: bool
        journey_display_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, display_journey_data: bool = ..., journey_display_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class AgentLoginGuiStatisticsDisplay(_message.Message):
        __slots__ = ("display_agent_login_gui_statistics", "agent_login_gui_statistics_template")
        DISPLAY_AGENT_LOGIN_GUI_STATISTICS_FIELD_NUMBER: _ClassVar[int]
        AGENT_LOGIN_GUI_STATISTICS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        display_agent_login_gui_statistics: bool
        agent_login_gui_statistics_template: int
        def __init__(self, display_agent_login_gui_statistics: bool = ..., agent_login_gui_statistics_template: _Optional[int] = ...) -> None: ...
    class PhoneZipMetadataDisplay(_message.Message):
        __slots__ = ("display_phone_zip_metadata", "phone_zip_metadata_keys")
        DISPLAY_PHONE_ZIP_METADATA_FIELD_NUMBER: _ClassVar[int]
        PHONE_ZIP_METADATA_KEYS_FIELD_NUMBER: _ClassVar[int]
        display_phone_zip_metadata: bool
        phone_zip_metadata_keys: _containers.RepeatedScalarFieldContainer[_org_pb2.PhonePostalDisplayOptions]
        def __init__(self, display_phone_zip_metadata: bool = ..., phone_zip_metadata_keys: _Optional[_Iterable[_Union[_org_pb2.PhonePostalDisplayOptions, str]]] = ...) -> None: ...
    class DisallowedHuntGroups(_message.Message):
        __slots__ = ("enabled", "hunt_groups")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        hunt_groups: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, enabled: bool = ..., hunt_groups: _Optional[_Iterable[int]] = ...) -> None: ...
    class AlphanumericKeypad(_message.Message):
        __slots__ = ("enabled", "delimiter")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        delimiter: _org_pb2.AlphanumericKeypadDelimiter
        def __init__(self, enabled: bool = ..., delimiter: _Optional[_Union[_org_pb2.AlphanumericKeypadDelimiter, str]] = ...) -> None: ...
    class InboundComplianceMetadata(_message.Message):
        __slots__ = ("enabled", "optional_data", "required_data")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_DATA_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        optional_data: _containers.RepeatedScalarFieldContainer[int]
        required_data: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, enabled: bool = ..., optional_data: _Optional[_Iterable[int]] = ..., required_data: _Optional[_Iterable[int]] = ...) -> None: ...
    class PrepareStateCallDelivery(_message.Message):
        __slots__ = ("manual_dial", "preview_dial")
        MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_DIAL_FIELD_NUMBER: _ClassVar[int]
        manual_dial: bool
        preview_dial: bool
        def __init__(self, manual_dial: bool = ..., preview_dial: bool = ...) -> None: ...
    ENABLE_AGENT_GATEWAY_TITLE_BAR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_DIAL_IN_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_END_CALL_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTHORIZATION_BY_IP_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_PAUSE_FIELD_NUMBER: _ClassVar[int]
    AGENT_PAUSE_OPTION_SET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_PAUSE_OPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PAUSE_OPTION_RESET_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_PAUSE_STATUS_PAUSE_CODE_WAITING_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_PAUSE_STATUS_PAUSE_CODE_WRAPUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_RECORDING_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALL_RECORDING_PAUSE_FIELD_NUMBER: _ClassVar[int]
    CALL_RECORDING_PAUSE_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    CALL_RECORDING_DELAY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PAUSE_RECORDING_ON_HOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ENVISION_SCREEN_RECORDING_FIELD_NUMBER: _ClassVar[int]
    AGENT_SCREEN_RECORDING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_SIMPLE_HOLD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_MULTI_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_AGENT_AFTER_MULTI_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    HOLD_QUEUE_MONITORING_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MACHINE_DELIVER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LINKBACK_HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SIP_HEADER_DATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IVR_NAVIGATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_COLLECT_DATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATA_DIPPED_DATA_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_DATA_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_DATA_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_HISTORY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_LOGIN_GUI_STATISTICS_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    PHONE_ZIP_METADATA_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_SKILLS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_WEB_LINKS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_HUNT_GROUP_REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    DISALLOWED_HUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MANUAL_APPROVAL_OF_CALLS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_MANUAL_APPROVAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MANUAL_APPROVAL_OF_SMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_MANUAL_APPROVAL_NUMBER_SMS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_REJECT_OPTION_FOR_APPROVERS_FIELD_NUMBER: _ClassVar[int]
    ALPHANUMERIC_KEYPAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALL_DESKTOP_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    INBOUND_COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_INTERCOM_FIELD_NUMBER: _ClassVar[int]
    PREPARE_STATE_CALL_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    enable_agent_gateway_title_bar: bool
    default_agent_dial_in: str
    require_end_call_confirmation: bool
    enable_authorization_by_ip: bool
    authorized_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    initial_agent_status: _org_pb2.InitialAgentStatus
    enable_agent_pause: bool
    agent_pause_option_set: GeneralSettings.PauseOptionSet
    default_agent_pause_option: str
    enable_pause_option_reset: bool
    triggered_pause_status_pause_code_waiting: str
    triggered_pause_status_pause_code_wrapup: str
    display_recording_indicator: bool
    enable_call_recording_pause: bool
    call_recording_pause_confirmation: bool
    call_recording_delay: int
    enable_pause_recording_on_hold: bool
    enable_envision_screen_recording: bool
    agent_screen_recording: bool
    enable_agent_simple_hold: bool
    enable_agent_multi_accept: bool
    pause_agent_after_multi_accept: bool
    hold_queue_monitoring: GeneralSettings.HoldQueueMonitoring
    display_machine_deliver: bool
    display_linkback_hunt_group: bool
    display_sip_header_data: bool
    display_ivr_navigation_keys: bool
    display_data_collect_data: bool
    display_data_dipped_data: GeneralSettings.DataDipDataDisplay
    integration_data_display: GeneralSettings.IntegrationDataDisplay
    journey_data_display: GeneralSettings.JourneyDataDisplay
    agent_call_history_scope: _org_pb2.AgentCallHistoryScope
    agent_login_gui_statistics_display: GeneralSettings.AgentLoginGuiStatisticsDisplay
    phone_zip_metadata_display: GeneralSettings.PhoneZipMetadataDisplay
    display_skills: bool
    display_web_links: bool
    enable_agent_hunt_group_reassignment: bool
    disallowed_hunt_groups: GeneralSettings.DisallowedHuntGroups
    enable_manual_approval_of_calls: bool
    require_manual_approval_number: bool
    enable_manual_approval_of_sms: bool
    require_manual_approval_number_sms: bool
    disable_reject_option_for_approvers: bool
    alphanumeric_keypad: GeneralSettings.AlphanumericKeypad
    enable_call_desktop_notifications: bool
    inbound_compliance_metadata: GeneralSettings.InboundComplianceMetadata
    enable_agent_intercom: bool
    prepare_state_call_delivery: GeneralSettings.PrepareStateCallDelivery
    def __init__(self, enable_agent_gateway_title_bar: bool = ..., default_agent_dial_in: _Optional[str] = ..., require_end_call_confirmation: bool = ..., enable_authorization_by_ip: bool = ..., authorized_ip_addresses: _Optional[_Iterable[str]] = ..., initial_agent_status: _Optional[_Union[_org_pb2.InitialAgentStatus, str]] = ..., enable_agent_pause: bool = ..., agent_pause_option_set: _Optional[_Union[GeneralSettings.PauseOptionSet, _Mapping]] = ..., default_agent_pause_option: _Optional[str] = ..., enable_pause_option_reset: bool = ..., triggered_pause_status_pause_code_waiting: _Optional[str] = ..., triggered_pause_status_pause_code_wrapup: _Optional[str] = ..., display_recording_indicator: bool = ..., enable_call_recording_pause: bool = ..., call_recording_pause_confirmation: bool = ..., call_recording_delay: _Optional[int] = ..., enable_pause_recording_on_hold: bool = ..., enable_envision_screen_recording: bool = ..., agent_screen_recording: bool = ..., enable_agent_simple_hold: bool = ..., enable_agent_multi_accept: bool = ..., pause_agent_after_multi_accept: bool = ..., hold_queue_monitoring: _Optional[_Union[GeneralSettings.HoldQueueMonitoring, _Mapping]] = ..., display_machine_deliver: bool = ..., display_linkback_hunt_group: bool = ..., display_sip_header_data: bool = ..., display_ivr_navigation_keys: bool = ..., display_data_collect_data: bool = ..., display_data_dipped_data: _Optional[_Union[GeneralSettings.DataDipDataDisplay, _Mapping]] = ..., integration_data_display: _Optional[_Union[GeneralSettings.IntegrationDataDisplay, _Mapping]] = ..., journey_data_display: _Optional[_Union[GeneralSettings.JourneyDataDisplay, _Mapping]] = ..., agent_call_history_scope: _Optional[_Union[_org_pb2.AgentCallHistoryScope, str]] = ..., agent_login_gui_statistics_display: _Optional[_Union[GeneralSettings.AgentLoginGuiStatisticsDisplay, _Mapping]] = ..., phone_zip_metadata_display: _Optional[_Union[GeneralSettings.PhoneZipMetadataDisplay, _Mapping]] = ..., display_skills: bool = ..., display_web_links: bool = ..., enable_agent_hunt_group_reassignment: bool = ..., disallowed_hunt_groups: _Optional[_Union[GeneralSettings.DisallowedHuntGroups, _Mapping]] = ..., enable_manual_approval_of_calls: bool = ..., require_manual_approval_number: bool = ..., enable_manual_approval_of_sms: bool = ..., require_manual_approval_number_sms: bool = ..., disable_reject_option_for_approvers: bool = ..., alphanumeric_keypad: _Optional[_Union[GeneralSettings.AlphanumericKeypad, _Mapping]] = ..., enable_call_desktop_notifications: bool = ..., inbound_compliance_metadata: _Optional[_Union[GeneralSettings.InboundComplianceMetadata, _Mapping]] = ..., enable_agent_intercom: bool = ..., prepare_state_call_delivery: _Optional[_Union[GeneralSettings.PrepareStateCallDelivery, _Mapping]] = ...) -> None: ...

class HuntGroupDetails(_message.Message):
    __slots__ = ("general_details", "template_details", "web_link_details", "trigger_details", "integration_link_details", "script_details")
    class GeneralDetails(_message.Message):
        __slots__ = ("name", "description", "type", "modify_date", "agent_count")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MODIFY_DATE_FIELD_NUMBER: _ClassVar[int]
        AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        type: HuntGroupType
        modify_date: _timestamp_pb2.Timestamp
        agent_count: int
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[HuntGroupType, str]] = ..., modify_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_count: _Optional[int] = ...) -> None: ...
    class ClientInfoDisplayTemplateDetails(_message.Message):
        __slots__ = ("name", "description", "display_all_fields", "defined_field_count", "template_sid")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_ALL_FIELDS_FIELD_NUMBER: _ClassVar[int]
        DEFINED_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        display_all_fields: bool
        defined_field_count: int
        template_sid: int
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., display_all_fields: bool = ..., defined_field_count: _Optional[int] = ..., template_sid: _Optional[int] = ...) -> None: ...
    class WebLinkDetails(_message.Message):
        __slots__ = ("name", "description", "base_url", "parameter_count")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BASE_URL_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        base_url: str
        parameter_count: int
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., base_url: _Optional[str] = ..., parameter_count: _Optional[int] = ...) -> None: ...
    class TriggerDetails(_message.Message):
        __slots__ = ("description", "status", "duration", "action")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        status: AgentStatus
        duration: int
        action: TriggerAction
        def __init__(self, description: _Optional[str] = ..., status: _Optional[_Union[AgentStatus, str]] = ..., duration: _Optional[int] = ..., action: _Optional[_Union[TriggerAction, str]] = ...) -> None: ...
    class IntegrationLinkDetails(_message.Message):
        __slots__ = ("name", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class ScriptDetails(_message.Message):
        __slots__ = ("script_sid", "name", "description", "act_count", "disposition_count", "verbiage_count")
        SCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACT_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISPOSITION_COUNT_FIELD_NUMBER: _ClassVar[int]
        VERBIAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        script_sid: int
        name: str
        description: str
        act_count: int
        disposition_count: int
        verbiage_count: int
        def __init__(self, script_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., act_count: _Optional[int] = ..., disposition_count: _Optional[int] = ..., verbiage_count: _Optional[int] = ...) -> None: ...
    GENERAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    WEB_LINK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_LINK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    general_details: HuntGroupDetails.GeneralDetails
    template_details: HuntGroupDetails.ClientInfoDisplayTemplateDetails
    web_link_details: _containers.RepeatedCompositeFieldContainer[HuntGroupDetails.WebLinkDetails]
    trigger_details: _containers.RepeatedCompositeFieldContainer[HuntGroupDetails.TriggerDetails]
    integration_link_details: _containers.RepeatedCompositeFieldContainer[HuntGroupDetails.IntegrationLinkDetails]
    script_details: HuntGroupDetails.ScriptDetails
    def __init__(self, general_details: _Optional[_Union[HuntGroupDetails.GeneralDetails, _Mapping]] = ..., template_details: _Optional[_Union[HuntGroupDetails.ClientInfoDisplayTemplateDetails, _Mapping]] = ..., web_link_details: _Optional[_Iterable[_Union[HuntGroupDetails.WebLinkDetails, _Mapping]]] = ..., trigger_details: _Optional[_Iterable[_Union[HuntGroupDetails.TriggerDetails, _Mapping]]] = ..., integration_link_details: _Optional[_Iterable[_Union[HuntGroupDetails.IntegrationLinkDetails, _Mapping]]] = ..., script_details: _Optional[_Union[HuntGroupDetails.ScriptDetails, _Mapping]] = ...) -> None: ...

class CommunicationSettings(_message.Message):
    __slots__ = ("enable_scrub_list_adding", "scrub_lists", "enable_scrub_list_removal", "scrub_lists_removal_allowed", "compliance_default_country", "display_options_in_wrapup", "inbound_scrub_list_expiration", "manual_scrub_list_expiration", "outbound_scrub_list_expiration", "preview_scrub_list_expiration", "automate_manually_dialed_scrub_list", "automate_preview_dialed_scrub_list", "automate_response_rules", "automate_scrub_list_call_data")
    class ScrubListExpiration(_message.Message):
        __slots__ = ("default_expiration", "limit_expiration", "limited_expirations")
        DEFAULT_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        LIMITED_EXPIRATIONS_FIELD_NUMBER: _ClassVar[int]
        default_expiration: _org_pb2.CommunicationExpiration
        limit_expiration: bool
        limited_expirations: _containers.RepeatedScalarFieldContainer[_org_pb2.CommunicationExpiration]
        def __init__(self, default_expiration: _Optional[_Union[_org_pb2.CommunicationExpiration, str]] = ..., limit_expiration: bool = ..., limited_expirations: _Optional[_Iterable[_Union[_org_pb2.CommunicationExpiration, str]]] = ...) -> None: ...
    class AutomateResponseRules(_message.Message):
        __slots__ = ("enabled", "rule_sid")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        RULE_SID_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        rule_sid: int
        def __init__(self, enabled: bool = ..., rule_sid: _Optional[int] = ...) -> None: ...
    class AutomateScrubListCallData(_message.Message):
        __slots__ = ("enabled", "scrub_list_data_fields")
        class ScrubListDataField(_message.Message):
            __slots__ = ("scrub_list", "call_data_field")
            SCRUB_LIST_FIELD_NUMBER: _ClassVar[int]
            CALL_DATA_FIELD_FIELD_NUMBER: _ClassVar[int]
            scrub_list: str
            call_data_field: int
            def __init__(self, scrub_list: _Optional[str] = ..., call_data_field: _Optional[int] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        SCRUB_LIST_DATA_FIELDS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        scrub_list_data_fields: _containers.RepeatedCompositeFieldContainer[CommunicationSettings.AutomateScrubListCallData.ScrubListDataField]
        def __init__(self, enabled: bool = ..., scrub_list_data_fields: _Optional[_Iterable[_Union[CommunicationSettings.AutomateScrubListCallData.ScrubListDataField, _Mapping]]] = ...) -> None: ...
    ENABLE_SCRUB_LIST_ADDING_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LISTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SCRUB_LIST_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    SCRUB_LISTS_REMOVAL_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_DEFAULT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_OPTIONS_IN_WRAPUP_FIELD_NUMBER: _ClassVar[int]
    INBOUND_SCRUB_LIST_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    MANUAL_SCRUB_LIST_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_SCRUB_LIST_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_SCRUB_LIST_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATE_MANUALLY_DIALED_SCRUB_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTOMATE_PREVIEW_DIALED_SCRUB_LIST_FIELD_NUMBER: _ClassVar[int]
    AUTOMATE_RESPONSE_RULES_FIELD_NUMBER: _ClassVar[int]
    AUTOMATE_SCRUB_LIST_CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    enable_scrub_list_adding: bool
    scrub_lists: _containers.RepeatedScalarFieldContainer[str]
    enable_scrub_list_removal: bool
    scrub_lists_removal_allowed: _containers.RepeatedScalarFieldContainer[str]
    compliance_default_country: _country_pb2.Country
    display_options_in_wrapup: bool
    inbound_scrub_list_expiration: CommunicationSettings.ScrubListExpiration
    manual_scrub_list_expiration: CommunicationSettings.ScrubListExpiration
    outbound_scrub_list_expiration: CommunicationSettings.ScrubListExpiration
    preview_scrub_list_expiration: CommunicationSettings.ScrubListExpiration
    automate_manually_dialed_scrub_list: bool
    automate_preview_dialed_scrub_list: bool
    automate_response_rules: CommunicationSettings.AutomateResponseRules
    automate_scrub_list_call_data: CommunicationSettings.AutomateScrubListCallData
    def __init__(self, enable_scrub_list_adding: bool = ..., scrub_lists: _Optional[_Iterable[str]] = ..., enable_scrub_list_removal: bool = ..., scrub_lists_removal_allowed: _Optional[_Iterable[str]] = ..., compliance_default_country: _Optional[_Union[_country_pb2.Country, str]] = ..., display_options_in_wrapup: bool = ..., inbound_scrub_list_expiration: _Optional[_Union[CommunicationSettings.ScrubListExpiration, _Mapping]] = ..., manual_scrub_list_expiration: _Optional[_Union[CommunicationSettings.ScrubListExpiration, _Mapping]] = ..., outbound_scrub_list_expiration: _Optional[_Union[CommunicationSettings.ScrubListExpiration, _Mapping]] = ..., preview_scrub_list_expiration: _Optional[_Union[CommunicationSettings.ScrubListExpiration, _Mapping]] = ..., automate_manually_dialed_scrub_list: bool = ..., automate_preview_dialed_scrub_list: bool = ..., automate_response_rules: _Optional[_Union[CommunicationSettings.AutomateResponseRules, _Mapping]] = ..., automate_scrub_list_call_data: _Optional[_Union[CommunicationSettings.AutomateScrubListCallData, _Mapping]] = ...) -> None: ...

class CallbackSettings(_message.Message):
    __slots__ = ("enable_callback_scheduling", "default_callback_routing", "enable_callback_calling", "enable_automatic_retrieval", "callback_routing_disallowed", "enable_customizable_caller_id", "default_caller_id", "enable_callback_calendar")
    class DefaultRouting(_message.Message):
        __slots__ = ("routing_mode", "agent_sid", "agent_skillsets", "hunt_group_sids")
        ROUTING_MODE_FIELD_NUMBER: _ClassVar[int]
        AGENT_SID_FIELD_NUMBER: _ClassVar[int]
        AGENT_SKILLSETS_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        routing_mode: _org_pb2.DefaultCallbackRouting
        agent_sid: int
        agent_skillsets: _containers.RepeatedScalarFieldContainer[int]
        hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, routing_mode: _Optional[_Union[_org_pb2.DefaultCallbackRouting, str]] = ..., agent_sid: _Optional[int] = ..., agent_skillsets: _Optional[_Iterable[int]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    class CallbackRoutingDisallowed(_message.Message):
        __slots__ = ("use_routing_limiting", "agent_sids", "hunt_group_sids", "agent_skill_sids")
        USE_ROUTING_LIMITING_FIELD_NUMBER: _ClassVar[int]
        AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        AGENT_SKILL_SIDS_FIELD_NUMBER: _ClassVar[int]
        use_routing_limiting: bool
        agent_sids: _containers.RepeatedScalarFieldContainer[int]
        hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
        agent_skill_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, use_routing_limiting: bool = ..., agent_sids: _Optional[_Iterable[int]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ..., agent_skill_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    ENABLE_CALLBACK_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLBACK_ROUTING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALLBACK_CALLING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOMATIC_RETRIEVAL_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ROUTING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CUSTOMIZABLE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALLBACK_CALENDAR_FIELD_NUMBER: _ClassVar[int]
    enable_callback_scheduling: bool
    default_callback_routing: CallbackSettings.DefaultRouting
    enable_callback_calling: bool
    enable_automatic_retrieval: bool
    callback_routing_disallowed: CallbackSettings.CallbackRoutingDisallowed
    enable_customizable_caller_id: bool
    default_caller_id: str
    enable_callback_calendar: bool
    def __init__(self, enable_callback_scheduling: bool = ..., default_callback_routing: _Optional[_Union[CallbackSettings.DefaultRouting, _Mapping]] = ..., enable_callback_calling: bool = ..., enable_automatic_retrieval: bool = ..., callback_routing_disallowed: _Optional[_Union[CallbackSettings.CallbackRoutingDisallowed, _Mapping]] = ..., enable_customizable_caller_id: bool = ..., default_caller_id: _Optional[str] = ..., enable_callback_calendar: bool = ...) -> None: ...

class PreviewDialSettings(_message.Message):
    __slots__ = ("enable_preview_dial_cancel", "enable_auto_pause_on_cancel", "timeout_minutes", "require_number_confirmation", "preview_queue_config")
    ENABLE_PREVIEW_DIAL_CANCEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTO_PAUSE_ON_CANCEL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_NUMBER_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_QUEUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enable_preview_dial_cancel: bool
    enable_auto_pause_on_cancel: bool
    timeout_minutes: int
    require_number_confirmation: bool
    preview_queue_config: str
    def __init__(self, enable_preview_dial_cancel: bool = ..., enable_auto_pause_on_cancel: bool = ..., timeout_minutes: _Optional[int] = ..., require_number_confirmation: bool = ..., preview_queue_config: _Optional[str] = ...) -> None: ...

class ManualDialSettings(_message.Message):
    __slots__ = ("enable_manual_dial", "queue_configuration_name", "default_call_recording", "cell_phone_scrub", "time_zone_restriction", "time_zone_validation_postal_code", "natural_compliance_scrub", "scrub_override", "enable_whitelist", "default_outbound_country", "display_outbound_country_selection", "display_outbound_number_phone_book", "default_caller_id_country", "display_caller_id_country_selection", "display_caller_id_phone_book", "enable_customizable_caller_id", "default_caller_id", "enable_caller_id_bucket", "random_caller_id_bucket", "automate_random_caller_id", "enable_mask_caller_id", "enable_sip_address", "natural_language_compliance_metadata", "data_dip_scope", "data_dip_config_sid", "data_dip_result_handling", "data_dip_integration_mappings", "data_dip_integration_handling", "enable_reject_option_for_approvers")
    class ScrubOverride(_message.Message):
        __slots__ = ("enable_dncl_override", "enable_cell_scrub_override", "enable_time_zone_scrub_override", "natural_compliance_override")
        ENABLE_DNCL_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CELL_SCRUB_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_TIME_ZONE_SCRUB_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        NATURAL_COMPLIANCE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        enable_dncl_override: bool
        enable_cell_scrub_override: bool
        enable_time_zone_scrub_override: bool
        natural_compliance_override: bool
        def __init__(self, enable_dncl_override: bool = ..., enable_cell_scrub_override: bool = ..., enable_time_zone_scrub_override: bool = ..., natural_compliance_override: bool = ...) -> None: ...
    class DefaultCallerId(_message.Message):
        __slots__ = ("usage", "custom_caller_id")
        USAGE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        usage: _org_pb2.DefaultManualDialCallerId
        custom_caller_id: str
        def __init__(self, usage: _Optional[_Union[_org_pb2.DefaultManualDialCallerId, str]] = ..., custom_caller_id: _Optional[str] = ...) -> None: ...
    class DataDipIntegrationMapping(_message.Message):
        __slots__ = ("mapping_type", "data_dip_return_key", "contact_field_description_sid")
        MAPPING_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_DIP_RETURN_KEY_FIELD_NUMBER: _ClassVar[int]
        CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
        mapping_type: _org_pb2.ManualDialDataDipIntegration
        data_dip_return_key: str
        contact_field_description_sid: int
        def __init__(self, mapping_type: _Optional[_Union[_org_pb2.ManualDialDataDipIntegration, str]] = ..., data_dip_return_key: _Optional[str] = ..., contact_field_description_sid: _Optional[int] = ...) -> None: ...
    ENABLE_MANUAL_DIAL_FIELD_NUMBER: _ClassVar[int]
    QUEUE_CONFIGURATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALL_RECORDING_FIELD_NUMBER: _ClassVar[int]
    CELL_PHONE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_VALIDATION_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    NATURAL_COMPLIANCE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    SCRUB_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_OUTBOUND_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_OUTBOUND_COUNTRY_SELECTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_OUTBOUND_NUMBER_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CALLER_ID_COUNTRY_SELECTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CALLER_ID_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CUSTOMIZABLE_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALLER_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    RANDOM_CALLER_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    AUTOMATE_RANDOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MASK_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_RESULT_HANDLING_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_INTEGRATION_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    DATA_DIP_INTEGRATION_HANDLING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REJECT_OPTION_FOR_APPROVERS_FIELD_NUMBER: _ClassVar[int]
    enable_manual_dial: bool
    queue_configuration_name: str
    default_call_recording: _org_pb2.HuntGroupOrgDefaultCustom
    cell_phone_scrub: _org_pb2.HuntGroupOrgDefaultCustom
    time_zone_restriction: _org_pb2.HuntGroupOrgDefaultCustom
    time_zone_validation_postal_code: _org_pb2.ManualDialTimeZoneValidation
    natural_compliance_scrub: NaturalLanguageComplianceScrub
    scrub_override: ManualDialSettings.ScrubOverride
    enable_whitelist: bool
    default_outbound_country: _country_pb2.Country
    display_outbound_country_selection: bool
    display_outbound_number_phone_book: bool
    default_caller_id_country: _country_pb2.Country
    display_caller_id_country_selection: bool
    display_caller_id_phone_book: bool
    enable_customizable_caller_id: bool
    default_caller_id: ManualDialSettings.DefaultCallerId
    enable_caller_id_bucket: bool
    random_caller_id_bucket: int
    automate_random_caller_id: bool
    enable_mask_caller_id: bool
    enable_sip_address: bool
    natural_language_compliance_metadata: NaturalLanguageComplianceMetadata
    data_dip_scope: _org_pb2.ManualDialDataDipScope
    data_dip_config_sid: int
    data_dip_result_handling: _org_pb2.ManualDialDataDipHandling
    data_dip_integration_mappings: _containers.RepeatedCompositeFieldContainer[ManualDialSettings.DataDipIntegrationMapping]
    data_dip_integration_handling: _org_pb2.ManualDialDataDipHandling
    enable_reject_option_for_approvers: bool
    def __init__(self, enable_manual_dial: bool = ..., queue_configuration_name: _Optional[str] = ..., default_call_recording: _Optional[_Union[_org_pb2.HuntGroupOrgDefaultCustom, str]] = ..., cell_phone_scrub: _Optional[_Union[_org_pb2.HuntGroupOrgDefaultCustom, str]] = ..., time_zone_restriction: _Optional[_Union[_org_pb2.HuntGroupOrgDefaultCustom, str]] = ..., time_zone_validation_postal_code: _Optional[_Union[_org_pb2.ManualDialTimeZoneValidation, str]] = ..., natural_compliance_scrub: _Optional[_Union[NaturalLanguageComplianceScrub, _Mapping]] = ..., scrub_override: _Optional[_Union[ManualDialSettings.ScrubOverride, _Mapping]] = ..., enable_whitelist: bool = ..., default_outbound_country: _Optional[_Union[_country_pb2.Country, str]] = ..., display_outbound_country_selection: bool = ..., display_outbound_number_phone_book: bool = ..., default_caller_id_country: _Optional[_Union[_country_pb2.Country, str]] = ..., display_caller_id_country_selection: bool = ..., display_caller_id_phone_book: bool = ..., enable_customizable_caller_id: bool = ..., default_caller_id: _Optional[_Union[ManualDialSettings.DefaultCallerId, _Mapping]] = ..., enable_caller_id_bucket: bool = ..., random_caller_id_bucket: _Optional[int] = ..., automate_random_caller_id: bool = ..., enable_mask_caller_id: bool = ..., enable_sip_address: bool = ..., natural_language_compliance_metadata: _Optional[_Union[NaturalLanguageComplianceMetadata, _Mapping]] = ..., data_dip_scope: _Optional[_Union[_org_pb2.ManualDialDataDipScope, str]] = ..., data_dip_config_sid: _Optional[int] = ..., data_dip_result_handling: _Optional[_Union[_org_pb2.ManualDialDataDipHandling, str]] = ..., data_dip_integration_mappings: _Optional[_Iterable[_Union[ManualDialSettings.DataDipIntegrationMapping, _Mapping]]] = ..., data_dip_integration_handling: _Optional[_Union[_org_pb2.ManualDialDataDipHandling, str]] = ..., enable_reject_option_for_approvers: bool = ...) -> None: ...

class NaturalLanguageComplianceScrub(_message.Message):
    __slots__ = ("compliance_scrub", "rule_set_id")
    COMPLIANCE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    compliance_scrub: _org_pb2.HuntGroupOrgDefaultCustom
    rule_set_id: str
    def __init__(self, compliance_scrub: _Optional[_Union[_org_pb2.HuntGroupOrgDefaultCustom, str]] = ..., rule_set_id: _Optional[str] = ...) -> None: ...

class NaturalLanguageComplianceMetadata(_message.Message):
    __slots__ = ("enabled", "optional_data", "required_data")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_DATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    optional_data: _containers.RepeatedScalarFieldContainer[int]
    required_data: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, enabled: bool = ..., optional_data: _Optional[_Iterable[int]] = ..., required_data: _Optional[_Iterable[int]] = ...) -> None: ...

class CallerIdBucketData(_message.Message):
    __slots__ = ("xml_client_property_sid", "bucket_name")
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    bucket_name: str
    def __init__(self, xml_client_property_sid: _Optional[int] = ..., bucket_name: _Optional[str] = ...) -> None: ...

class TransferCallSettings(_message.Message):
    __slots__ = ("enable_transfer", "hand_off_types", "recording_status", "transfer_types", "display_transfer_number_phone_book", "enable_transfer_number_editing", "default_transfer_number", "start_recording_numbers", "stop_recording_numbers", "transfer_number_country", "display_transfer_country_selection", "display_caller_id_phone_book", "enable_caller_id_editing", "default_caller_id", "caller_id_country", "display_caller_id_country_selection", "display_agent_transfer_filtering", "default_agent_transfer_filtering", "enable_hunt_group_filtering", "requeue_queue_config", "requeue_transfer_disallowed", "pbx_transfer_disallowed", "enable_scrub_override", "enable_whitelist", "natural_compliance_scrub", "natural_language_compliance_metadata")
    class HandOffTypes(_message.Message):
        __slots__ = ("enable_conference", "enable_warm", "enable_cold")
        ENABLE_CONFERENCE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_WARM_FIELD_NUMBER: _ClassVar[int]
        ENABLE_COLD_FIELD_NUMBER: _ClassVar[int]
        enable_conference: bool
        enable_warm: bool
        enable_cold: bool
        def __init__(self, enable_conference: bool = ..., enable_warm: bool = ..., enable_cold: bool = ...) -> None: ...
    class TransferTypes(_message.Message):
        __slots__ = ("enable_agent_transfer", "enable_open_transfer", "enable_requeue_transfer", "enable_pbx_extension_transfer", "enable_voicemail_transfer")
        ENABLE_AGENT_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        ENABLE_OPEN_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        ENABLE_REQUEUE_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        ENABLE_PBX_EXTENSION_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        ENABLE_VOICEMAIL_TRANSFER_FIELD_NUMBER: _ClassVar[int]
        enable_agent_transfer: bool
        enable_open_transfer: bool
        enable_requeue_transfer: bool
        enable_pbx_extension_transfer: bool
        enable_voicemail_transfer: bool
        def __init__(self, enable_agent_transfer: bool = ..., enable_open_transfer: bool = ..., enable_requeue_transfer: bool = ..., enable_pbx_extension_transfer: bool = ..., enable_voicemail_transfer: bool = ...) -> None: ...
    class RequeueTransferDisallowed(_message.Message):
        __slots__ = ("enable", "agent_skill_sids", "hunt_group_sids")
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        AGENT_SKILL_SIDS_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        agent_skill_sids: _containers.RepeatedScalarFieldContainer[int]
        hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, enable: bool = ..., agent_skill_sids: _Optional[_Iterable[int]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    class PbxTransferDisallowed(_message.Message):
        __slots__ = ("enable", "extensions")
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        extensions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, enable: bool = ..., extensions: _Optional[_Iterable[str]] = ...) -> None: ...
    class RequeueQueueConfiguration(_message.Message):
        __slots__ = ("usage", "custom_name")
        USAGE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_NAME_FIELD_NUMBER: _ClassVar[int]
        usage: _org_pb2.RequeueTransferQueueConfig
        custom_name: str
        def __init__(self, usage: _Optional[_Union[_org_pb2.RequeueTransferQueueConfig, str]] = ..., custom_name: _Optional[str] = ...) -> None: ...
    class DefaultCallerId(_message.Message):
        __slots__ = ("usage", "custom_caller_id")
        USAGE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        usage: _org_pb2.DefaultTransferCallerId
        custom_caller_id: str
        def __init__(self, usage: _Optional[_Union[_org_pb2.DefaultTransferCallerId, str]] = ..., custom_caller_id: _Optional[str] = ...) -> None: ...
    ENABLE_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    HAND_OFF_TYPES_FIELD_NUMBER: _ClassVar[int]
    RECORDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TYPES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TRANSFER_NUMBER_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TRANSFER_NUMBER_EDITING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRANSFER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_RECORDING_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    STOP_RECORDING_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_NUMBER_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TRANSFER_COUNTRY_SELECTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CALLER_ID_PHONE_BOOK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CALLER_ID_EDITING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CALLER_ID_COUNTRY_SELECTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_AGENT_TRANSFER_FILTERING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AGENT_TRANSFER_FILTERING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HUNT_GROUP_FILTERING_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_QUEUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_TRANSFER_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    PBX_TRANSFER_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SCRUB_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    NATURAL_COMPLIANCE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_COMPLIANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    enable_transfer: bool
    hand_off_types: TransferCallSettings.HandOffTypes
    recording_status: _org_pb2.TransferRecordingStatus
    transfer_types: TransferCallSettings.TransferTypes
    display_transfer_number_phone_book: bool
    enable_transfer_number_editing: bool
    default_transfer_number: str
    start_recording_numbers: _containers.RepeatedScalarFieldContainer[str]
    stop_recording_numbers: _containers.RepeatedScalarFieldContainer[str]
    transfer_number_country: _country_pb2.Country
    display_transfer_country_selection: bool
    display_caller_id_phone_book: bool
    enable_caller_id_editing: bool
    default_caller_id: TransferCallSettings.DefaultCallerId
    caller_id_country: _country_pb2.Country
    display_caller_id_country_selection: bool
    display_agent_transfer_filtering: bool
    default_agent_transfer_filtering: bool
    enable_hunt_group_filtering: bool
    requeue_queue_config: TransferCallSettings.RequeueQueueConfiguration
    requeue_transfer_disallowed: TransferCallSettings.RequeueTransferDisallowed
    pbx_transfer_disallowed: TransferCallSettings.PbxTransferDisallowed
    enable_scrub_override: bool
    enable_whitelist: bool
    natural_compliance_scrub: NaturalLanguageComplianceScrub
    natural_language_compliance_metadata: NaturalLanguageComplianceMetadata
    def __init__(self, enable_transfer: bool = ..., hand_off_types: _Optional[_Union[TransferCallSettings.HandOffTypes, _Mapping]] = ..., recording_status: _Optional[_Union[_org_pb2.TransferRecordingStatus, str]] = ..., transfer_types: _Optional[_Union[TransferCallSettings.TransferTypes, _Mapping]] = ..., display_transfer_number_phone_book: bool = ..., enable_transfer_number_editing: bool = ..., default_transfer_number: _Optional[str] = ..., start_recording_numbers: _Optional[_Iterable[str]] = ..., stop_recording_numbers: _Optional[_Iterable[str]] = ..., transfer_number_country: _Optional[_Union[_country_pb2.Country, str]] = ..., display_transfer_country_selection: bool = ..., display_caller_id_phone_book: bool = ..., enable_caller_id_editing: bool = ..., default_caller_id: _Optional[_Union[TransferCallSettings.DefaultCallerId, _Mapping]] = ..., caller_id_country: _Optional[_Union[_country_pb2.Country, str]] = ..., display_caller_id_country_selection: bool = ..., display_agent_transfer_filtering: bool = ..., default_agent_transfer_filtering: bool = ..., enable_hunt_group_filtering: bool = ..., requeue_queue_config: _Optional[_Union[TransferCallSettings.RequeueQueueConfiguration, _Mapping]] = ..., requeue_transfer_disallowed: _Optional[_Union[TransferCallSettings.RequeueTransferDisallowed, _Mapping]] = ..., pbx_transfer_disallowed: _Optional[_Union[TransferCallSettings.PbxTransferDisallowed, _Mapping]] = ..., enable_scrub_override: bool = ..., enable_whitelist: bool = ..., natural_compliance_scrub: _Optional[_Union[NaturalLanguageComplianceScrub, _Mapping]] = ..., natural_language_compliance_metadata: _Optional[_Union[NaturalLanguageComplianceMetadata, _Mapping]] = ...) -> None: ...

class NumberHistorySettings(_message.Message):
    __slots__ = ("enable_search", "enable_report_download", "enable_recordings_download", "enable_agent_response_editing")
    ENABLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REPORT_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RECORDINGS_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_RESPONSE_EDITING_FIELD_NUMBER: _ClassVar[int]
    enable_search: bool
    enable_report_download: bool
    enable_recordings_download: bool
    enable_agent_response_editing: bool
    def __init__(self, enable_search: bool = ..., enable_report_download: bool = ..., enable_recordings_download: bool = ..., enable_agent_response_editing: bool = ...) -> None: ...

class AgentResponseAutoRuleSet(_message.Message):
    __slots__ = ("ruleset_sid", "name", "description", "country", "responses")
    RULESET_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    ruleset_sid: int
    name: str
    description: str
    country: _country_pb2.Country
    responses: _containers.RepeatedCompositeFieldContainer[AutoResponseChoice]
    def __init__(self, ruleset_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., country: _Optional[_Union[_country_pb2.Country, str]] = ..., responses: _Optional[_Iterable[_Union[AutoResponseChoice, _Mapping]]] = ...) -> None: ...

class AutoResponseChoice(_message.Message):
    __slots__ = ("agent_call_response", "comparitors")
    AGENT_CALL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COMPARITORS_FIELD_NUMBER: _ClassVar[int]
    agent_call_response: str
    comparitors: _containers.RepeatedCompositeFieldContainer[AgentResponseComparitors]
    def __init__(self, agent_call_response: _Optional[str] = ..., comparitors: _Optional[_Iterable[_Union[AgentResponseComparitors, _Mapping]]] = ...) -> None: ...

class AgentResponseComparitors(_message.Message):
    __slots__ = ("value", "expiration")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    value: str
    expiration: int
    def __init__(self, value: _Optional[str] = ..., expiration: _Optional[int] = ...) -> None: ...

class ClientInfoDisplayTemplate(_message.Message):
    __slots__ = ("template_sid", "name", "description", "display_all_fields", "dialed_number_field_style", "contact_field_styles", "template_category", "client_info_display_template_sid", "hunt_group_sid")
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ALL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DIALED_NUMBER_FIELD_STYLE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_STYLES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_DISPLAY_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: str
    name: str
    description: str
    display_all_fields: bool
    dialed_number_field_style: DialedNumberFieldStyle
    contact_field_styles: _containers.RepeatedCompositeFieldContainer[ContactFieldStyle]
    template_category: TemplateCategory
    client_info_display_template_sid: int
    hunt_group_sid: int
    def __init__(self, template_sid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., display_all_fields: bool = ..., dialed_number_field_style: _Optional[_Union[DialedNumberFieldStyle, _Mapping]] = ..., contact_field_styles: _Optional[_Iterable[_Union[ContactFieldStyle, _Mapping]]] = ..., template_category: _Optional[_Union[TemplateCategory, str]] = ..., client_info_display_template_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class FieldStyle(_message.Message):
    __slots__ = ("text_color", "background_color", "allow_agent_copy")
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AGENT_COPY_FIELD_NUMBER: _ClassVar[int]
    text_color: str
    background_color: str
    allow_agent_copy: bool
    def __init__(self, text_color: _Optional[str] = ..., background_color: _Optional[str] = ..., allow_agent_copy: bool = ...) -> None: ...

class ContactFieldStyle(_message.Message):
    __slots__ = ("description_id", "field_style")
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_STYLE_FIELD_NUMBER: _ClassVar[int]
    description_id: int
    field_style: FieldStyle
    def __init__(self, description_id: _Optional[int] = ..., field_style: _Optional[_Union[FieldStyle, _Mapping]] = ...) -> None: ...

class DialedNumberFieldStyle(_message.Message):
    __slots__ = ("field_style", "display_to_agent")
    FIELD_STYLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TO_AGENT_FIELD_NUMBER: _ClassVar[int]
    field_style: FieldStyle
    display_to_agent: bool
    def __init__(self, field_style: _Optional[_Union[FieldStyle, _Mapping]] = ..., display_to_agent: bool = ...) -> None: ...

class HuntGroupWithClientInfoTemplateData(_message.Message):
    __slots__ = ("hunt_group", "template")
    class HuntGroup(_message.Message):
        __slots__ = ("client_sid", "hunt_group_sid", "hunt_group_name")
        CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        client_sid: int
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, client_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    HUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    hunt_group: HuntGroupWithClientInfoTemplateData.HuntGroup
    template: ClientInfoDisplayTemplate
    def __init__(self, hunt_group: _Optional[_Union[HuntGroupWithClientInfoTemplateData.HuntGroup, _Mapping]] = ..., template: _Optional[_Union[ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class WebLink(_message.Message):
    __slots__ = ("web_link_sid", "name", "description", "link_type", "order", "base_url", "parameters")
    WEB_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    web_link_sid: int
    name: str
    description: str
    link_type: WebLinkType
    order: int
    base_url: _containers.RepeatedCompositeFieldContainer[WebLinkComponent]
    parameters: _containers.RepeatedCompositeFieldContainer[WebLinkParameter]
    def __init__(self, web_link_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., link_type: _Optional[_Union[WebLinkType, str]] = ..., order: _Optional[int] = ..., base_url: _Optional[_Iterable[_Union[WebLinkComponent, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[WebLinkParameter, _Mapping]]] = ...) -> None: ...

class WebLinkComponent(_message.Message):
    __slots__ = ("key_type", "value")
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key_type: WebLinkComponentKeyType
    value: str
    def __init__(self, key_type: _Optional[_Union[WebLinkComponentKeyType, str]] = ..., value: _Optional[str] = ...) -> None: ...

class WebLinkParameter(_message.Message):
    __slots__ = ("key", "components")
    KEY_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    key: str
    components: _containers.RepeatedCompositeFieldContainer[WebLinkComponent]
    def __init__(self, key: _Optional[str] = ..., components: _Optional[_Iterable[_Union[WebLinkComponent, _Mapping]]] = ...) -> None: ...

class DataDipConfig(_message.Message):
    __slots__ = ("config_name", "config_type", "remote_url", "param_type_value_tuples", "params", "data", "request_method", "xml_client_property_sid", "headers")
    class Param(_message.Message):
        __slots__ = ("name", "value", "param_type", "composite_value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        PARAM_TYPE_FIELD_NUMBER: _ClassVar[int]
        COMPOSITE_VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        param_type: str
        composite_value: _containers.RepeatedCompositeFieldContainer[DataDipConfig.ParamTypeValueTuple]
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., param_type: _Optional[str] = ..., composite_value: _Optional[_Iterable[_Union[DataDipConfig.ParamTypeValueTuple, _Mapping]]] = ...) -> None: ...
    class ParamTypeValueTuple(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ReturnData(_message.Message):
        __slots__ = ("name", "access_type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        access_type: str
        def __init__(self, name: _Optional[str] = ..., access_type: _Optional[str] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("name", "value", "header_type", "param_type_value_tuples")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        HEADER_TYPE_FIELD_NUMBER: _ClassVar[int]
        PARAM_TYPE_VALUE_TUPLES_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        header_type: str
        param_type_value_tuples: _containers.RepeatedCompositeFieldContainer[DataDipConfig.ParamTypeValueTuple]
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., header_type: _Optional[str] = ..., param_type_value_tuples: _Optional[_Iterable[_Union[DataDipConfig.ParamTypeValueTuple, _Mapping]]] = ...) -> None: ...
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    PARAM_TYPE_VALUE_TUPLES_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    config_type: str
    remote_url: str
    param_type_value_tuples: _containers.RepeatedCompositeFieldContainer[DataDipConfig.ParamTypeValueTuple]
    params: _containers.RepeatedCompositeFieldContainer[DataDipConfig.Param]
    data: _containers.RepeatedCompositeFieldContainer[DataDipConfig.ReturnData]
    request_method: str
    xml_client_property_sid: int
    headers: _containers.RepeatedCompositeFieldContainer[DataDipConfig.Header]
    def __init__(self, config_name: _Optional[str] = ..., config_type: _Optional[str] = ..., remote_url: _Optional[str] = ..., param_type_value_tuples: _Optional[_Iterable[_Union[DataDipConfig.ParamTypeValueTuple, _Mapping]]] = ..., params: _Optional[_Iterable[_Union[DataDipConfig.Param, _Mapping]]] = ..., data: _Optional[_Iterable[_Union[DataDipConfig.ReturnData, _Mapping]]] = ..., request_method: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[DataDipConfig.Header, _Mapping]]] = ...) -> None: ...

class IntegrationLink(_message.Message):
    __slots__ = ("integration_id", "parameter_sid", "name", "description", "method_id", "order", "parameters", "configuration_name", "hunt_group_sid")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    integration_id: int
    parameter_sid: int
    name: str
    description: str
    method_id: int
    order: int
    parameters: _containers.RepeatedCompositeFieldContainer[IntegrationLinkParameter]
    configuration_name: str
    hunt_group_sid: int
    def __init__(self, integration_id: _Optional[int] = ..., parameter_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., method_id: _Optional[int] = ..., order: _Optional[int] = ..., parameters: _Optional[_Iterable[_Union[IntegrationLinkParameter, _Mapping]]] = ..., configuration_name: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class IntegrationLinkParameter(_message.Message):
    __slots__ = ("key", "sub_parameters")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUB_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    key: str
    sub_parameters: _containers.RepeatedCompositeFieldContainer[IntegrationLinkSubParameter]
    def __init__(self, key: _Optional[str] = ..., sub_parameters: _Optional[_Iterable[_Union[IntegrationLinkSubParameter, _Mapping]]] = ...) -> None: ...

class IntegrationLinkSubParameter(_message.Message):
    __slots__ = ("key", "parts")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    key: str
    parts: _containers.RepeatedCompositeFieldContainer[IntegrationLinkSubParameterPart]
    def __init__(self, key: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[IntegrationLinkSubParameterPart, _Mapping]]] = ...) -> None: ...

class IntegrationLinkSubParameterPart(_message.Message):
    __slots__ = ("contact_field_sid", "helper_value", "parameter_source_type")
    CONTACT_FIELD_SID_FIELD_NUMBER: _ClassVar[int]
    HELPER_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contact_field_sid: int
    helper_value: str
    parameter_source_type: ParameterSourceType
    def __init__(self, contact_field_sid: _Optional[int] = ..., helper_value: _Optional[str] = ..., parameter_source_type: _Optional[_Union[ParameterSourceType, str]] = ...) -> None: ...

class AgentTrigger(_message.Message):
    __slots__ = ("agent_trigger_sid", "description", "agent_status_option", "trigger_action_option")
    AGENT_TRIGGER_SID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_OPTION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ACTION_OPTION_FIELD_NUMBER: _ClassVar[int]
    agent_trigger_sid: int
    description: str
    agent_status_option: AgentStatusOption
    trigger_action_option: TriggerActionOption
    def __init__(self, agent_trigger_sid: _Optional[int] = ..., description: _Optional[str] = ..., agent_status_option: _Optional[_Union[AgentStatusOption, _Mapping]] = ..., trigger_action_option: _Optional[_Union[TriggerActionOption, _Mapping]] = ...) -> None: ...

class AgentStatusOption(_message.Message):
    __slots__ = ("agent_status", "duration", "pause_code", "call_types", "scheduled_callback_present")
    AGENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_PRESENT_FIELD_NUMBER: _ClassVar[int]
    agent_status: AgentStatus
    duration: int
    pause_code: TriggerPauseCode
    call_types: TriggerCallTypes
    scheduled_callback_present: bool
    def __init__(self, agent_status: _Optional[_Union[AgentStatus, str]] = ..., duration: _Optional[int] = ..., pause_code: _Optional[_Union[TriggerPauseCode, _Mapping]] = ..., call_types: _Optional[_Union[TriggerCallTypes, _Mapping]] = ..., scheduled_callback_present: bool = ...) -> None: ...

class TriggerPauseCode(_message.Message):
    __slots__ = ("system_pause_code", "custom_pause_code")
    SYSTEM_PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    system_pause_code: SystemPauseCode
    custom_pause_code: str
    def __init__(self, system_pause_code: _Optional[_Union[SystemPauseCode, str]] = ..., custom_pause_code: _Optional[str] = ...) -> None: ...

class TriggerCallTypes(_message.Message):
    __slots__ = ("outbound", "inbound", "manual", "preview")
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    outbound: bool
    inbound: bool
    manual: bool
    preview: bool
    def __init__(self, outbound: bool = ..., inbound: bool = ..., manual: bool = ..., preview: bool = ...) -> None: ...

class TriggerActionOption(_message.Message):
    __slots__ = ("action", "display_message", "advance_to_status", "web_link_sid", "integration_link_sid")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_TO_STATUS_FIELD_NUMBER: _ClassVar[int]
    WEB_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    action: TriggerAction
    display_message: str
    advance_to_status: AgentStatus
    web_link_sid: int
    integration_link_sid: int
    def __init__(self, action: _Optional[_Union[TriggerAction, str]] = ..., display_message: _Optional[str] = ..., advance_to_status: _Optional[_Union[AgentStatus, str]] = ..., web_link_sid: _Optional[int] = ..., integration_link_sid: _Optional[int] = ...) -> None: ...

class HuntGroupScript(_message.Message):
    __slots__ = ("script_sid", "name", "description", "auto_script_progression", "script_category", "acts")
    SCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCRIPT_PROGRESSION_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ACTS_FIELD_NUMBER: _ClassVar[int]
    script_sid: int
    name: str
    description: str
    auto_script_progression: bool
    script_category: ScriptCategory
    acts: _containers.RepeatedCompositeFieldContainer[Act]
    def __init__(self, script_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., auto_script_progression: bool = ..., script_category: _Optional[_Union[ScriptCategory, str]] = ..., acts: _Optional[_Iterable[_Union[Act, _Mapping]]] = ...) -> None: ...

class Act(_message.Message):
    __slots__ = ("dispositions", "verbiages", "conditional_navigations", "default_conditional_navigation_target", "page_arrival_recording_control", "page_exit_recording_control")
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    VERBIAGES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_NAVIGATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONDITIONAL_NAVIGATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    PAGE_ARRIVAL_RECORDING_CONTROL_FIELD_NUMBER: _ClassVar[int]
    PAGE_EXIT_RECORDING_CONTROL_FIELD_NUMBER: _ClassVar[int]
    dispositions: _containers.RepeatedCompositeFieldContainer[Disposition]
    verbiages: _containers.RepeatedCompositeFieldContainer[Verbiage]
    conditional_navigations: _containers.RepeatedCompositeFieldContainer[ConditionalNavigation]
    default_conditional_navigation_target: int
    page_arrival_recording_control: int
    page_exit_recording_control: int
    def __init__(self, dispositions: _Optional[_Iterable[_Union[Disposition, _Mapping]]] = ..., verbiages: _Optional[_Iterable[_Union[Verbiage, _Mapping]]] = ..., conditional_navigations: _Optional[_Iterable[_Union[ConditionalNavigation, _Mapping]]] = ..., default_conditional_navigation_target: _Optional[int] = ..., page_arrival_recording_control: _Optional[int] = ..., page_exit_recording_control: _Optional[int] = ...) -> None: ...

class Disposition(_message.Message):
    __slots__ = ("response_options", "header", "prompt", "order", "required", "default_value", "bypass_auto_script_progression", "response_type", "response_evaluator")
    RESPONSE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_AUTO_SCRIPT_PROGRESSION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    response_options: _containers.RepeatedScalarFieldContainer[str]
    header: str
    prompt: str
    order: int
    required: bool
    default_value: str
    bypass_auto_script_progression: bool
    response_type: ScriptResponseType
    response_evaluator: int
    def __init__(self, response_options: _Optional[_Iterable[str]] = ..., header: _Optional[str] = ..., prompt: _Optional[str] = ..., order: _Optional[int] = ..., required: bool = ..., default_value: _Optional[str] = ..., bypass_auto_script_progression: bool = ..., response_type: _Optional[_Union[ScriptResponseType, str]] = ..., response_evaluator: _Optional[int] = ...) -> None: ...

class Verbiage(_message.Message):
    __slots__ = ("order", "header", "body")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    order: int
    header: str
    body: str
    def __init__(self, order: _Optional[int] = ..., header: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class ConditionalNavigation(_message.Message):
    __slots__ = ("target_act_index", "complex_boolean_expression_list")
    TARGET_ACT_INDEX_FIELD_NUMBER: _ClassVar[int]
    COMPLEX_BOOLEAN_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    target_act_index: int
    complex_boolean_expression_list: ComplexBooleanExpressionList
    def __init__(self, target_act_index: _Optional[int] = ..., complex_boolean_expression_list: _Optional[_Union[ComplexBooleanExpressionList, _Mapping]] = ...) -> None: ...

class ComplexBooleanExpressionList(_message.Message):
    __slots__ = ("complex_boolean_expressions",)
    COMPLEX_BOOLEAN_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    complex_boolean_expressions: _containers.RepeatedCompositeFieldContainer[ComplexBooleanExpression]
    def __init__(self, complex_boolean_expressions: _Optional[_Iterable[_Union[ComplexBooleanExpression, _Mapping]]] = ...) -> None: ...

class ComplexBooleanExpression(_message.Message):
    __slots__ = ("compare_expression_list",)
    COMPARE_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    compare_expression_list: CompareExpressionList
    def __init__(self, compare_expression_list: _Optional[_Union[CompareExpressionList, _Mapping]] = ...) -> None: ...

class CompareExpressionList(_message.Message):
    __slots__ = ("simple_compare_expression",)
    SIMPLE_COMPARE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    simple_compare_expression: _containers.RepeatedCompositeFieldContainer[SimpleCompareExpression]
    def __init__(self, simple_compare_expression: _Optional[_Iterable[_Union[SimpleCompareExpression, _Mapping]]] = ...) -> None: ...

class SimpleCompareExpression(_message.Message):
    __slots__ = ("operator_type", "act_index", "disposition_header", "compare_value")
    OPERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACT_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_HEADER_FIELD_NUMBER: _ClassVar[int]
    COMPARE_VALUE_FIELD_NUMBER: _ClassVar[int]
    operator_type: CompareOperatorType
    act_index: int
    disposition_header: str
    compare_value: str
    def __init__(self, operator_type: _Optional[_Union[CompareOperatorType, str]] = ..., act_index: _Optional[int] = ..., disposition_header: _Optional[str] = ..., compare_value: _Optional[str] = ...) -> None: ...

class ResponseEvaluator(_message.Message):
    __slots__ = ("response_evaluator_id", "org_id", "name", "description", "regular_expression")
    RESPONSE_EVALUATOR_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REGULAR_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    response_evaluator_id: str
    org_id: str
    name: str
    description: str
    regular_expression: str
    def __init__(self, response_evaluator_id: _Optional[str] = ..., org_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., regular_expression: _Optional[str] = ...) -> None: ...
