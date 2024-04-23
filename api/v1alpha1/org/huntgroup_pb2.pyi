from api.commons import broadcasts_pb2 as _broadcasts_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons.org import huntgroup_pb2 as _huntgroup_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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

class CreateHuntGroupRequest(_message.Message):
    __slots__ = ("name", "description", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: _huntgroup_pb2.HuntGroupType
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_huntgroup_pb2.HuntGroupType, str]] = ...) -> None: ...

class CreateHuntGroupResponse(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class UpdateHuntGroupGeneralDetailsRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "name", "description", "type")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    name: str
    description: str
    type: _huntgroup_pb2.HuntGroupType
    def __init__(self, hunt_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_huntgroup_pb2.HuntGroupType, str]] = ...) -> None: ...

class UpdateHuntGroupGeneralDetailsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteHuntGroupRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class DeleteHuntGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetHuntGroupDetailsRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetHuntGroupDetailsResponse(_message.Message):
    __slots__ = ("hunt_group_details",)
    HUNT_GROUP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_details: _huntgroup_pb2.HuntGroupDetails
    def __init__(self, hunt_group_details: _Optional[_Union[_huntgroup_pb2.HuntGroupDetails, _Mapping]] = ...) -> None: ...

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

class ListBroadcastTemplateGeneralDetailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBroadcastTemplateGeneralDetailsResponse(_message.Message):
    __slots__ = ("templates",)
    class Data(_message.Message):
        __slots__ = ("template_sid", "name", "broadcast_type", "last_scheduled_date")
        TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BROADCAST_TYPE_FIELD_NUMBER: _ClassVar[int]
        LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
        template_sid: int
        name: str
        broadcast_type: _broadcasts_pb2.BroadcastType
        last_scheduled_date: _timestamp_pb2.Timestamp
        def __init__(self, template_sid: _Optional[int] = ..., name: _Optional[str] = ..., broadcast_type: _Optional[_Union[_broadcasts_pb2.BroadcastType, str]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[ListBroadcastTemplateGeneralDetailsResponse.Data]
    def __init__(self, templates: _Optional[_Iterable[_Union[ListBroadcastTemplateGeneralDetailsResponse.Data, _Mapping]]] = ...) -> None: ...

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

class GetHuntGroupClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetHuntGroupClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateHuntGroupClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "template")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, hunt_group_sid: _Optional[int] = ..., template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateHuntGroupClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("template_sid",)
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    def __init__(self, template_sid: _Optional[int] = ...) -> None: ...

class UpdateHuntGroupClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "template")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, hunt_group_sid: _Optional[int] = ..., template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class UpdateHuntGroupClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteHuntGroupClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "template_sid")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    template_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., template_sid: _Optional[int] = ...) -> None: ...

class DeleteHuntGroupClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyHuntGroupClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("to_hunt_group_sid", "template")
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    to_hunt_group_sid: int
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, to_hunt_group_sid: _Optional[int] = ..., template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CopyHuntGroupClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCampaignClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateCampaignClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("template_sid",)
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    def __init__(self, template_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupsWithClientInfoTemplateDataRequest(_message.Message):
    __slots__ = ("filter",)
    class Filter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTER_UNSPECIFIED: _ClassVar[ListHuntGroupsWithClientInfoTemplateDataRequest.Filter]
        FILTER_ALL: _ClassVar[ListHuntGroupsWithClientInfoTemplateDataRequest.Filter]
        FILTER_HUNT_GROUPS_WITH_TEMPLATE: _ClassVar[ListHuntGroupsWithClientInfoTemplateDataRequest.Filter]
        FILTER_HUNT_GROUPS_WITHOUT_TEMPLATE: _ClassVar[ListHuntGroupsWithClientInfoTemplateDataRequest.Filter]
    FILTER_UNSPECIFIED: ListHuntGroupsWithClientInfoTemplateDataRequest.Filter
    FILTER_ALL: ListHuntGroupsWithClientInfoTemplateDataRequest.Filter
    FILTER_HUNT_GROUPS_WITH_TEMPLATE: ListHuntGroupsWithClientInfoTemplateDataRequest.Filter
    FILTER_HUNT_GROUPS_WITHOUT_TEMPLATE: ListHuntGroupsWithClientInfoTemplateDataRequest.Filter
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: ListHuntGroupsWithClientInfoTemplateDataRequest.Filter
    def __init__(self, filter: _Optional[_Union[ListHuntGroupsWithClientInfoTemplateDataRequest.Filter, str]] = ...) -> None: ...

class ListHuntGroupsWithClientInfoTemplateDataResponse(_message.Message):
    __slots__ = ("hunt_groups_with_template_data",)
    HUNT_GROUPS_WITH_TEMPLATE_DATA_FIELD_NUMBER: _ClassVar[int]
    hunt_groups_with_template_data: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.HuntGroupWithClientInfoTemplateData]
    def __init__(self, hunt_groups_with_template_data: _Optional[_Iterable[_Union[_huntgroup_pb2.HuntGroupWithClientInfoTemplateData, _Mapping]]] = ...) -> None: ...

class ListHuntGroupWebLinksRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupWebLinksResponse(_message.Message):
    __slots__ = ("web_links",)
    WEB_LINKS_FIELD_NUMBER: _ClassVar[int]
    web_links: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.WebLink]
    def __init__(self, web_links: _Optional[_Iterable[_Union[_huntgroup_pb2.WebLink, _Mapping]]] = ...) -> None: ...

class CopyHuntGroupWebLinkRequest(_message.Message):
    __slots__ = ("from_hunt_group_sid", "to_hunt_group_sid", "web_link")
    FROM_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    WEB_LINK_FIELD_NUMBER: _ClassVar[int]
    from_hunt_group_sid: int
    to_hunt_group_sid: int
    web_link: _huntgroup_pb2.WebLink
    def __init__(self, from_hunt_group_sid: _Optional[int] = ..., to_hunt_group_sid: _Optional[int] = ..., web_link: _Optional[_Union[_huntgroup_pb2.WebLink, _Mapping]] = ...) -> None: ...

class CopyHuntGroupWebLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHuntGroupWebLinksRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "web_links")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    WEB_LINKS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    web_links: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.WebLink]
    def __init__(self, hunt_group_sid: _Optional[int] = ..., web_links: _Optional[_Iterable[_Union[_huntgroup_pb2.WebLink, _Mapping]]] = ...) -> None: ...

class UpdateHuntGroupWebLinksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHuntGroupIntegrationLinksRequest(_message.Message):
    __slots__ = ("org_id", "hunt_group_sid")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    hunt_group_sid: int
    def __init__(self, org_id: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupIntegrationLinksResponse(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.IntegrationLink]
    def __init__(self, links: _Optional[_Iterable[_Union[_huntgroup_pb2.IntegrationLink, _Mapping]]] = ...) -> None: ...

class CopyHuntGroupIntegrationLinkRequest(_message.Message):
    __slots__ = ("to_hunt_group_sid", "link")
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    to_hunt_group_sid: int
    link: _huntgroup_pb2.IntegrationLink
    def __init__(self, to_hunt_group_sid: _Optional[int] = ..., link: _Optional[_Union[_huntgroup_pb2.IntegrationLink, _Mapping]] = ...) -> None: ...

class CopyHuntGroupIntegrationLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHuntGroupIntegrationLinksRequest(_message.Message):
    __slots__ = ("links", "hunt_group_sid")
    LINKS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.IntegrationLink]
    hunt_group_sid: int
    def __init__(self, links: _Optional[_Iterable[_Union[_huntgroup_pb2.IntegrationLink, _Mapping]]] = ..., hunt_group_sid: _Optional[int] = ...) -> None: ...

class UpdateHuntGroupIntegrationLinksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentTriggersRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListAgentTriggersResponse(_message.Message):
    __slots__ = ("agent_triggers",)
    AGENT_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    agent_triggers: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.AgentTrigger]
    def __init__(self, agent_triggers: _Optional[_Iterable[_Union[_huntgroup_pb2.AgentTrigger, _Mapping]]] = ...) -> None: ...

class CopyAgentTriggerRequest(_message.Message):
    __slots__ = ("from_hunt_group_sid", "to_hunt_group_sid", "agent_trigger")
    FROM_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    from_hunt_group_sid: int
    to_hunt_group_sid: int
    agent_trigger: _huntgroup_pb2.AgentTrigger
    def __init__(self, from_hunt_group_sid: _Optional[int] = ..., to_hunt_group_sid: _Optional[int] = ..., agent_trigger: _Optional[_Union[_huntgroup_pb2.AgentTrigger, _Mapping]] = ...) -> None: ...

class CopyAgentTriggerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentTriggersRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "agent_triggers")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    agent_triggers: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.AgentTrigger]
    def __init__(self, hunt_group_sid: _Optional[int] = ..., agent_triggers: _Optional[_Iterable[_Union[_huntgroup_pb2.AgentTrigger, _Mapping]]] = ...) -> None: ...

class UpdateAgentTriggersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetHuntGroupScriptRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class GetHuntGroupScriptResponse(_message.Message):
    __slots__ = ("hunt_group_script",)
    HUNT_GROUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    hunt_group_script: _huntgroup_pb2.HuntGroupScript
    def __init__(self, hunt_group_script: _Optional[_Union[_huntgroup_pb2.HuntGroupScript, _Mapping]] = ...) -> None: ...

class CreateHuntGroupScriptRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "hunt_group_script")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    hunt_group_script: _huntgroup_pb2.HuntGroupScript
    def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_script: _Optional[_Union[_huntgroup_pb2.HuntGroupScript, _Mapping]] = ...) -> None: ...

class CreateHuntGroupScriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHuntGroupScriptRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "hunt_group_script")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    hunt_group_script: _huntgroup_pb2.HuntGroupScript
    def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_script: _Optional[_Union[_huntgroup_pb2.HuntGroupScript, _Mapping]] = ...) -> None: ...

class UpdateHuntGroupScriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteHuntGroupScriptRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "script_sid")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    script_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ..., script_sid: _Optional[int] = ...) -> None: ...

class DeleteHuntGroupScriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
