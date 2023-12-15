from api.commons import org_pb2 as _org_pb2
from api.commons.org import huntgroup_pb2 as _huntgroup_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHuntGroupSettingsRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "field_mask")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, hunt_group_sid: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetHuntGroupSettingsResponse(_message.Message):
    __slots__ = ("general_settings", "communication_settings", "callback_settings", "preview_dial_settings", "manual_dial_settings", "transfer_call_settings", "number_history_settings")
    GENERAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CALL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_HISTORY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    general_settings: _huntgroup_pb2.GeneralSettings
    communication_settings: _huntgroup_pb2.CommunicationSettings
    callback_settings: _huntgroup_pb2.CallbackSettings
    preview_dial_settings: _huntgroup_pb2.PreviewDialSettings
    manual_dial_settings: _huntgroup_pb2.ManualDialSettings
    transfer_call_settings: _huntgroup_pb2.TransferCallSettings
    number_history_settings: _huntgroup_pb2.NumberHistorySettings
    def __init__(self, general_settings: _Optional[_Union[_huntgroup_pb2.GeneralSettings, _Mapping]] = ..., communication_settings: _Optional[_Union[_huntgroup_pb2.CommunicationSettings, _Mapping]] = ..., callback_settings: _Optional[_Union[_huntgroup_pb2.CallbackSettings, _Mapping]] = ..., preview_dial_settings: _Optional[_Union[_huntgroup_pb2.PreviewDialSettings, _Mapping]] = ..., manual_dial_settings: _Optional[_Union[_huntgroup_pb2.ManualDialSettings, _Mapping]] = ..., transfer_call_settings: _Optional[_Union[_huntgroup_pb2.TransferCallSettings, _Mapping]] = ..., number_history_settings: _Optional[_Union[_huntgroup_pb2.NumberHistorySettings, _Mapping]] = ...) -> None: ...

class UpdateHuntGroupSettingsRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "general_settings", "communication_settings", "callback_settings", "preview_dial_settings", "manual_dial_settings", "transfer_call_settings", "number_history_settings", "field_mask")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    GENERAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CALL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_HISTORY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    general_settings: _huntgroup_pb2.GeneralSettings
    communication_settings: _huntgroup_pb2.CommunicationSettings
    callback_settings: _huntgroup_pb2.CallbackSettings
    preview_dial_settings: _huntgroup_pb2.PreviewDialSettings
    manual_dial_settings: _huntgroup_pb2.ManualDialSettings
    transfer_call_settings: _huntgroup_pb2.TransferCallSettings
    number_history_settings: _huntgroup_pb2.NumberHistorySettings
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, hunt_group_sid: _Optional[int] = ..., general_settings: _Optional[_Union[_huntgroup_pb2.GeneralSettings, _Mapping]] = ..., communication_settings: _Optional[_Union[_huntgroup_pb2.CommunicationSettings, _Mapping]] = ..., callback_settings: _Optional[_Union[_huntgroup_pb2.CallbackSettings, _Mapping]] = ..., preview_dial_settings: _Optional[_Union[_huntgroup_pb2.PreviewDialSettings, _Mapping]] = ..., manual_dial_settings: _Optional[_Union[_huntgroup_pb2.ManualDialSettings, _Mapping]] = ..., transfer_call_settings: _Optional[_Union[_huntgroup_pb2.TransferCallSettings, _Mapping]] = ..., number_history_settings: _Optional[_Union[_huntgroup_pb2.NumberHistorySettings, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateHuntGroupSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCallerIdBucketsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCallerIdBucketsResponse(_message.Message):
    __slots__ = ("caller_id_bucket_data",)
    CALLER_ID_BUCKET_DATA_FIELD_NUMBER: _ClassVar[int]
    caller_id_bucket_data: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.CallerIdBucketData]
    def __init__(self, caller_id_bucket_data: _Optional[_Iterable[_Union[_huntgroup_pb2.CallerIdBucketData, _Mapping]]] = ...) -> None: ...

class GetDataDipTemplateRequest(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class GetDataDipTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.DataDipConfig
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.DataDipConfig, _Mapping]] = ...) -> None: ...

class ListDataDipTemplatesRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _org_pb2.DataDipTemplateFilterType
    def __init__(self, filter: _Optional[_Union[_org_pb2.DataDipTemplateFilterType, str]] = ...) -> None: ...

class ListDataDipTemplatesResponse(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.DataDipConfig]
    def __init__(self, templates: _Optional[_Iterable[_Union[_huntgroup_pb2.DataDipConfig, _Mapping]]] = ...) -> None: ...

class CreateDataDipTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.DataDipConfig
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.DataDipConfig, _Mapping]] = ...) -> None: ...

class CreateDataDipTemplateResponse(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class UpdateDataDipTemplateRequest(_message.Message):
    __slots__ = ("org_id", "template")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    template: _huntgroup_pb2.DataDipConfig
    def __init__(self, org_id: _Optional[str] = ..., template: _Optional[_Union[_huntgroup_pb2.DataDipConfig, _Mapping]] = ...) -> None: ...

class UpdateDataDipTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDataDipTemplateRequest(_message.Message):
    __slots__ = ("org_id", "xml_client_property_sid")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    xml_client_property_sid: int
    def __init__(self, org_id: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ...) -> None: ...

class DeleteDataDipTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyDataDipTemplateRequest(_message.Message):
    __slots__ = ("org_id", "xml_client_property_sid", "config_name")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    xml_client_property_sid: int
    config_name: str
    def __init__(self, org_id: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ..., config_name: _Optional[str] = ...) -> None: ...

class CopyDataDipTemplateResponse(_message.Message):
    __slots__ = ("xml_client_property_sid",)
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    xml_client_property_sid: int
    def __init__(self, xml_client_property_sid: _Optional[int] = ...) -> None: ...

class CopyDataDipTemplateToOrganizationRequest(_message.Message):
    __slots__ = ("org_id", "xml_client_property_sid", "config_name", "destination_org_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    XML_CLIENT_PROPERTY_SID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    xml_client_property_sid: int
    config_name: str
    destination_org_id: str
    def __init__(self, org_id: _Optional[str] = ..., xml_client_property_sid: _Optional[int] = ..., config_name: _Optional[str] = ..., destination_org_id: _Optional[str] = ...) -> None: ...

class CopyDataDipTemplateToOrganizationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentResponseAutoRulesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentResponseAutoRulesResponse(_message.Message):
    __slots__ = ("rulesets",)
    RULESETS_FIELD_NUMBER: _ClassVar[int]
    rulesets: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.AgentResponseAutoRuleSet]
    def __init__(self, rulesets: _Optional[_Iterable[_Union[_huntgroup_pb2.AgentResponseAutoRuleSet, _Mapping]]] = ...) -> None: ...

class CreateAgentResponseAutoRulesRequest(_message.Message):
    __slots__ = ("ruleset",)
    RULESET_FIELD_NUMBER: _ClassVar[int]
    ruleset: _huntgroup_pb2.AgentResponseAutoRuleSet
    def __init__(self, ruleset: _Optional[_Union[_huntgroup_pb2.AgentResponseAutoRuleSet, _Mapping]] = ...) -> None: ...

class CreateAgentResponseAutoRulesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentResponseAutoRulesRequest(_message.Message):
    __slots__ = ("rulesetSid", "ruleset")
    RULESETSID_FIELD_NUMBER: _ClassVar[int]
    RULESET_FIELD_NUMBER: _ClassVar[int]
    rulesetSid: int
    ruleset: _huntgroup_pb2.AgentResponseAutoRuleSet
    def __init__(self, rulesetSid: _Optional[int] = ..., ruleset: _Optional[_Union[_huntgroup_pb2.AgentResponseAutoRuleSet, _Mapping]] = ...) -> None: ...

class UpdateAgentResponseAutoRulesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAgentResponseAutoRulesRequest(_message.Message):
    __slots__ = ("rulesetSid",)
    RULESETSID_FIELD_NUMBER: _ClassVar[int]
    rulesetSid: int
    def __init__(self, rulesetSid: _Optional[int] = ...) -> None: ...

class DeleteAgentResponseAutoRulesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
