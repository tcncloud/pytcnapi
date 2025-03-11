from api.commons.org import huntgroup_pb2 as _huntgroup_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    TRIGGER_ACTION_EXECUTE_EXILE_LINK: _ClassVar[TriggerAction]
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
TRIGGER_ACTION_EXECUTE_EXILE_LINK: TriggerAction

class ExileLink(_message.Message):
    __slots__ = ("parameter_sid", "hunt_group_sid", "name", "description", "order", "inbound_data", "outbound_data")
    PARAMETER_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    INBOUND_DATA_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_DATA_FIELD_NUMBER: _ClassVar[int]
    parameter_sid: int
    hunt_group_sid: int
    name: str
    description: str
    order: int
    inbound_data: ExileLinkData
    outbound_data: ExileLinkData
    def __init__(self, parameter_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., order: _Optional[int] = ..., inbound_data: _Optional[_Union[ExileLinkData, _Mapping]] = ..., outbound_data: _Optional[_Union[ExileLinkData, _Mapping]] = ...) -> None: ...

class ExileLinkData(_message.Message):
    __slots__ = ("record_id", "alternate_id")
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_ID_FIELD_NUMBER: _ClassVar[int]
    record_id: ExileLinkParameter
    alternate_id: ExileLinkParameter
    def __init__(self, record_id: _Optional[_Union[ExileLinkParameter, _Mapping]] = ..., alternate_id: _Optional[_Union[ExileLinkParameter, _Mapping]] = ...) -> None: ...

class ExileLinkParameter(_message.Message):
    __slots__ = ("contact_field_sid", "helper_value", "parameter_source_type")
    CONTACT_FIELD_SID_FIELD_NUMBER: _ClassVar[int]
    HELPER_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contact_field_sid: int
    helper_value: str
    parameter_source_type: _huntgroup_pb2.ParameterSourceType
    def __init__(self, contact_field_sid: _Optional[int] = ..., helper_value: _Optional[str] = ..., parameter_source_type: _Optional[_Union[_huntgroup_pb2.ParameterSourceType, str]] = ...) -> None: ...

class ListHuntGroupExileLinksRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupExileLinksResponse(_message.Message):
    __slots__ = ("exile_links",)
    EXILE_LINKS_FIELD_NUMBER: _ClassVar[int]
    exile_links: _containers.RepeatedCompositeFieldContainer[ExileLink]
    def __init__(self, exile_links: _Optional[_Iterable[_Union[ExileLink, _Mapping]]] = ...) -> None: ...

class CopyHuntGroupExileLinkRequest(_message.Message):
    __slots__ = ("to_hunt_group_sid", "exile_link")
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    EXILE_LINK_FIELD_NUMBER: _ClassVar[int]
    to_hunt_group_sid: int
    exile_link: ExileLink
    def __init__(self, to_hunt_group_sid: _Optional[int] = ..., exile_link: _Optional[_Union[ExileLink, _Mapping]] = ...) -> None: ...

class CopyHuntGroupExileLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHuntGroupExileLinksRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "exile_links")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    EXILE_LINKS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    exile_links: _containers.RepeatedCompositeFieldContainer[ExileLink]
    def __init__(self, hunt_group_sid: _Optional[int] = ..., exile_links: _Optional[_Iterable[_Union[ExileLink, _Mapping]]] = ...) -> None: ...

class UpdateHuntGroupExileLinksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

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
    __slots__ = ("action", "display_message", "advance_to_status", "web_link_sid", "integration_link_sid", "exile_link_sid", "pause_code")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_TO_STATUS_FIELD_NUMBER: _ClassVar[int]
    WEB_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    EXILE_LINK_SID_FIELD_NUMBER: _ClassVar[int]
    PAUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    action: TriggerAction
    display_message: str
    advance_to_status: AgentStatus
    web_link_sid: int
    integration_link_sid: int
    exile_link_sid: int
    pause_code: TriggerPauseCode
    def __init__(self, action: _Optional[_Union[TriggerAction, str]] = ..., display_message: _Optional[str] = ..., advance_to_status: _Optional[_Union[AgentStatus, str]] = ..., web_link_sid: _Optional[int] = ..., integration_link_sid: _Optional[int] = ..., exile_link_sid: _Optional[int] = ..., pause_code: _Optional[_Union[TriggerPauseCode, _Mapping]] = ...) -> None: ...

class ListHuntGroupAgentTriggersRequest(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class ListHuntGroupAgentTriggersResponse(_message.Message):
    __slots__ = ("agent_triggers",)
    AGENT_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    agent_triggers: _containers.RepeatedCompositeFieldContainer[AgentTrigger]
    def __init__(self, agent_triggers: _Optional[_Iterable[_Union[AgentTrigger, _Mapping]]] = ...) -> None: ...

class CopyHuntGroupAgentTriggerRequest(_message.Message):
    __slots__ = ("from_hunt_group_sid", "to_hunt_group_sid", "agent_trigger")
    FROM_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    TO_HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    from_hunt_group_sid: int
    to_hunt_group_sid: int
    agent_trigger: AgentTrigger
    def __init__(self, from_hunt_group_sid: _Optional[int] = ..., to_hunt_group_sid: _Optional[int] = ..., agent_trigger: _Optional[_Union[AgentTrigger, _Mapping]] = ...) -> None: ...

class CopyHuntGroupAgentTriggerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateHuntGroupAgentTriggersRequest(_message.Message):
    __slots__ = ("hunt_group_sid", "agent_triggers")
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    agent_triggers: _containers.RepeatedCompositeFieldContainer[AgentTrigger]
    def __init__(self, hunt_group_sid: _Optional[int] = ..., agent_triggers: _Optional[_Iterable[_Union[AgentTrigger, _Mapping]]] = ...) -> None: ...

class UpdateHuntGroupAgentTriggersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyHuntGroupToOrganizationRequest(_message.Message):
    __slots__ = ("to_organization_id", "hunt_group_sid", "new_hunt_group_name")
    TO_ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NEW_HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    to_organization_id: str
    hunt_group_sid: int
    new_hunt_group_name: str
    def __init__(self, to_organization_id: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., new_hunt_group_name: _Optional[str] = ...) -> None: ...

class CopyHuntGroupToOrganizationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminCopyHuntGroupToOrganizationRequest(_message.Message):
    __slots__ = ("from_organization_id", "to_organization_id", "hunt_group_sid", "new_hunt_group_name")
    FROM_ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NEW_HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    from_organization_id: str
    to_organization_id: str
    hunt_group_sid: int
    new_hunt_group_name: str
    def __init__(self, from_organization_id: _Optional[str] = ..., to_organization_id: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., new_hunt_group_name: _Optional[str] = ...) -> None: ...

class AdminCopyHuntGroupToOrganizationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminListHuntGroupsRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class AdminListHuntGroupsResponse(_message.Message):
    __slots__ = ("hunt_groups",)
    class HuntGroup(_message.Message):
        __slots__ = ("hunt_group_sid", "hunt_group_name")
        HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        hunt_group_sid: int
        hunt_group_name: str
        def __init__(self, hunt_group_sid: _Optional[int] = ..., hunt_group_name: _Optional[str] = ...) -> None: ...
    HUNT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    hunt_groups: _containers.RepeatedCompositeFieldContainer[AdminListHuntGroupsResponse.HuntGroup]
    def __init__(self, hunt_groups: _Optional[_Iterable[_Union[AdminListHuntGroupsResponse.HuntGroup, _Mapping]]] = ...) -> None: ...

class ListAgentScriptsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentScriptsResponse(_message.Message):
    __slots__ = ("scripts",)
    class Script(_message.Message):
        __slots__ = ("script", "hunt_group_sids", "outbound_broadcast_template_sids", "inbound_broadcast_template_sids")
        SCRIPT_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_BROADCAST_TEMPLATE_SIDS_FIELD_NUMBER: _ClassVar[int]
        INBOUND_BROADCAST_TEMPLATE_SIDS_FIELD_NUMBER: _ClassVar[int]
        script: _huntgroup_pb2.HuntGroupScript
        hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
        outbound_broadcast_template_sids: _containers.RepeatedScalarFieldContainer[int]
        inbound_broadcast_template_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, script: _Optional[_Union[_huntgroup_pb2.HuntGroupScript, _Mapping]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ..., outbound_broadcast_template_sids: _Optional[_Iterable[int]] = ..., inbound_broadcast_template_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    scripts: _containers.RepeatedCompositeFieldContainer[ListAgentScriptsResponse.Script]
    def __init__(self, scripts: _Optional[_Iterable[_Union[ListAgentScriptsResponse.Script, _Mapping]]] = ...) -> None: ...

class CreateAgentClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class CreateAgentClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("template_sid",)
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    def __init__(self, template_sid: _Optional[int] = ...) -> None: ...

class UpdateAgentClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class UpdateAgentClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("template_sid",)
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    def __init__(self, template_sid: _Optional[int] = ...) -> None: ...

class GetAgentClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _huntgroup_pb2.ClientInfoDisplayTemplate
    def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ...) -> None: ...

class ListAgentClientInfoDisplayTemplatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentClientInfoDisplayTemplatesResponse(_message.Message):
    __slots__ = ("templates", "display_templates")
    class TemplateInfo(_message.Message):
        __slots__ = ("template", "hunt_group_sids", "outbound_broadcast_template_sids", "inbound_broadcast_template_sids")
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_BROADCAST_TEMPLATE_SIDS_FIELD_NUMBER: _ClassVar[int]
        INBOUND_BROADCAST_TEMPLATE_SIDS_FIELD_NUMBER: _ClassVar[int]
        template: _huntgroup_pb2.ClientInfoDisplayTemplate
        hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
        outbound_broadcast_template_sids: _containers.RepeatedScalarFieldContainer[int]
        inbound_broadcast_template_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, template: _Optional[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ..., outbound_broadcast_template_sids: _Optional[_Iterable[int]] = ..., inbound_broadcast_template_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[_huntgroup_pb2.ClientInfoDisplayTemplate]
    display_templates: _containers.RepeatedCompositeFieldContainer[ListAgentClientInfoDisplayTemplatesResponse.TemplateInfo]
    def __init__(self, templates: _Optional[_Iterable[_Union[_huntgroup_pb2.ClientInfoDisplayTemplate, _Mapping]]] = ..., display_templates: _Optional[_Iterable[_Union[ListAgentClientInfoDisplayTemplatesResponse.TemplateInfo, _Mapping]]] = ...) -> None: ...

class DeleteAgentClientInfoDisplayTemplateRequest(_message.Message):
    __slots__ = ("template_sid",)
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    def __init__(self, template_sid: _Optional[int] = ...) -> None: ...

class DeleteAgentClientInfoDisplayTemplateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignAgentClientInfoDisplayTemplateToHuntGroupsRequest(_message.Message):
    __slots__ = ("template_sid", "hunt_group_sids")
    TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    template_sid: int
    hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, template_sid: _Optional[int] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class AssignAgentClientInfoDisplayTemplateToHuntGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnassignAgentClientInfoDisplayTemplateFromHuntGroupsRequest(_message.Message):
    __slots__ = ("hunt_group_sids",)
    HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hunt_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class UnassignAgentClientInfoDisplayTemplateFromHuntGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
