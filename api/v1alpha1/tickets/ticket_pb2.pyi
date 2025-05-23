from api.commons import tickets_pb2 as _tickets_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NA: _ClassVar[ActionTypes]
    Callback: _ClassVar[ActionTypes]
    Emailback: _ClassVar[ActionTypes]
    Smsback: _ClassVar[ActionTypes]

class SLAConditions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[SLAConditions]
    Respond: _ClassVar[SLAConditions]
    Resolve: _ClassVar[SLAConditions]
NA: ActionTypes
Callback: ActionTypes
Emailback: ActionTypes
Smsback: ActionTypes
None: SLAConditions
Respond: SLAConditions
Resolve: SLAConditions

class PingReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTicketReq(_message.Message):
    __slots__ = ("title", "description", "project_sid", "due_date", "metadata", "ticket_skills", "status", "ticket_sla", "assign_self", "assign_other", "ticket_action", "ticket_assignee", "contact_entry_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TICKET_SKILLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TICKET_SLA_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_SELF_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_OTHER_FIELD_NUMBER: _ClassVar[int]
    TICKET_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKET_ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    project_sid: int
    due_date: _timestamp_pb2.Timestamp
    metadata: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Metadata]
    ticket_skills: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Skills]
    status: int
    ticket_sla: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Sla]
    assign_self: bool
    assign_other: str
    ticket_action: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.TicketAction]
    ticket_assignee: _containers.RepeatedScalarFieldContainer[str]
    contact_entry_id: int
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., project_sid: _Optional[int] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Iterable[_Union[_tickets_pb2.Metadata, _Mapping]]] = ..., ticket_skills: _Optional[_Iterable[_Union[_tickets_pb2.Skills, _Mapping]]] = ..., status: _Optional[int] = ..., ticket_sla: _Optional[_Iterable[_Union[_tickets_pb2.Sla, _Mapping]]] = ..., assign_self: bool = ..., assign_other: _Optional[str] = ..., ticket_action: _Optional[_Iterable[_Union[_tickets_pb2.TicketAction, _Mapping]]] = ..., ticket_assignee: _Optional[_Iterable[str]] = ..., contact_entry_id: _Optional[int] = ...) -> None: ...

class CreateTicketTemplateRequest(_message.Message):
    __slots__ = ("ticket_template",)
    TICKET_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ticket_template: _tickets_pb2.TicketTemplate
    def __init__(self, ticket_template: _Optional[_Union[_tickets_pb2.TicketTemplate, _Mapping]] = ...) -> None: ...

class CreateTicketTemplateResponse(_message.Message):
    __slots__ = ("ticket_template",)
    TICKET_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ticket_template: _tickets_pb2.TicketTemplate
    def __init__(self, ticket_template: _Optional[_Union[_tickets_pb2.TicketTemplate, _Mapping]] = ...) -> None: ...

class EditTicketTemplateRequest(_message.Message):
    __slots__ = ("ticket_template_id", "edit_value", "edited_fields_mask")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELDS_MASK_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: int
    edit_value: _tickets_pb2.TicketTemplate
    edited_fields_mask: _field_mask_pb2.FieldMask
    def __init__(self, ticket_template_id: _Optional[int] = ..., edit_value: _Optional[_Union[_tickets_pb2.TicketTemplate, _Mapping]] = ..., edited_fields_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class EditTicketTemplateResponse(_message.Message):
    __slots__ = ("is_edited",)
    IS_EDITED_FIELD_NUMBER: _ClassVar[int]
    is_edited: bool
    def __init__(self, is_edited: bool = ...) -> None: ...

class ListTicketTemplateRequest(_message.Message):
    __slots__ = ("ticket_template_id", "project_id", "request_mask", "template_id", "template_project_id")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MASK_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: int
    project_id: int
    request_mask: _field_mask_pb2.FieldMask
    template_id: int
    template_project_id: int
    def __init__(self, ticket_template_id: _Optional[int] = ..., project_id: _Optional[int] = ..., request_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., template_id: _Optional[int] = ..., template_project_id: _Optional[int] = ...) -> None: ...

class ListTicketTemplateResponse(_message.Message):
    __slots__ = ("enabled_templates", "ticket_project_template")
    ENABLED_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    TICKET_PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    enabled_templates: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.ListTemplate]
    ticket_project_template: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.TicketProjectTemplate]
    def __init__(self, enabled_templates: _Optional[_Iterable[_Union[_tickets_pb2.ListTemplate, _Mapping]]] = ..., ticket_project_template: _Optional[_Iterable[_Union[_tickets_pb2.TicketProjectTemplate, _Mapping]]] = ...) -> None: ...

class AssignProjectTemplateRequest(_message.Message):
    __slots__ = ("project_template", "project_id", "template_description")
    PROJECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    project_template: _tickets_pb2.AssignProjectTemplate
    project_id: int
    template_description: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.TemplateDescription]
    def __init__(self, project_template: _Optional[_Union[_tickets_pb2.AssignProjectTemplate, _Mapping]] = ..., project_id: _Optional[int] = ..., template_description: _Optional[_Iterable[_Union[_tickets_pb2.TemplateDescription, _Mapping]]] = ...) -> None: ...

class AssignProjectTemplateResponse(_message.Message):
    __slots__ = ("is_assigned",)
    IS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    is_assigned: bool
    def __init__(self, is_assigned: bool = ...) -> None: ...

class CreateTicketRes(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _tickets_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_tickets_pb2.Ticket, _Mapping]] = ...) -> None: ...

class GetActionTypeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActionTypeResponse(_message.Message):
    __slots__ = ("action_type",)
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    action_type: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.ActionType]
    def __init__(self, action_type: _Optional[_Iterable[_Union[_tickets_pb2.ActionType, _Mapping]]] = ...) -> None: ...

class GetPhoneNumberTypeRequest(_message.Message):
    __slots__ = ("phone_number",)
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    def __init__(self, phone_number: _Optional[str] = ...) -> None: ...

class GetPhoneNumberTypeResponse(_message.Message):
    __slots__ = ("phone_type",)
    PHONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    phone_type: _tickets_pb2.PhoneNumberType
    def __init__(self, phone_type: _Optional[_Union[_tickets_pb2.PhoneNumberType, str]] = ...) -> None: ...

class EditTicketReq(_message.Message):
    __slots__ = ("ticket_sid", "edit_value")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    edit_value: _tickets_pb2.EditAttribute
    def __init__(self, ticket_sid: _Optional[int] = ..., edit_value: _Optional[_Union[_tickets_pb2.EditAttribute, _Mapping]] = ...) -> None: ...

class EditMaskTicketReq(_message.Message):
    __slots__ = ("ticket_sid", "edit_value", "edited_fields_mask", "ticket_code", "contact_entry_id")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELDS_MASK_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    edit_value: _tickets_pb2.Ticket
    edited_fields_mask: _containers.RepeatedCompositeFieldContainer[_field_mask_pb2.FieldMask]
    ticket_code: str
    contact_entry_id: int
    def __init__(self, ticket_sid: _Optional[int] = ..., edit_value: _Optional[_Union[_tickets_pb2.Ticket, _Mapping]] = ..., edited_fields_mask: _Optional[_Iterable[_Union[_field_mask_pb2.FieldMask, _Mapping]]] = ..., ticket_code: _Optional[str] = ..., contact_entry_id: _Optional[int] = ...) -> None: ...

class EditMaskTicketRes(_message.Message):
    __slots__ = ("is_edited",)
    IS_EDITED_FIELD_NUMBER: _ClassVar[int]
    is_edited: bool
    def __init__(self, is_edited: bool = ...) -> None: ...

class ListAllocatedTicketRes(_message.Message):
    __slots__ = ("ticket_sid",)
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ticket_sid: _Optional[_Iterable[int]] = ...) -> None: ...

class ListAllocatedTicketReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentTicketsResponse(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Ticket]
    def __init__(self, ticket: _Optional[_Iterable[_Union[_tickets_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class ListAgentTicketsRequest(_message.Message):
    __slots__ = ("select_field_mask", "filter_mask")
    SELECT_FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    FILTER_MASK_FIELD_NUMBER: _ClassVar[int]
    select_field_mask: _field_mask_pb2.FieldMask
    filter_mask: _field_mask_pb2.FieldMask
    def __init__(self, select_field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., filter_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListAvailableAgentTicketsResponse(_message.Message):
    __slots__ = ("ticket_sid", "ticket")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: _containers.RepeatedScalarFieldContainer[int]
    ticket: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Ticket]
    def __init__(self, ticket_sid: _Optional[_Iterable[int]] = ..., ticket: _Optional[_Iterable[_Union[_tickets_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class ListAvailableAgentTicketsRequest(_message.Message):
    __slots__ = ("select_field_mask", "available_filter", "agent_view_limit")
    SELECT_FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    AGENT_VIEW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    select_field_mask: _field_mask_pb2.FieldMask
    available_filter: AvailableTicketsFilter
    agent_view_limit: int
    def __init__(self, select_field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., available_filter: _Optional[_Union[AvailableTicketsFilter, _Mapping]] = ..., agent_view_limit: _Optional[int] = ...) -> None: ...

class AvailableTicketsFilter(_message.Message):
    __slots__ = ("agent_skill_id",)
    AGENT_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    agent_skill_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_skill_id: _Optional[_Iterable[str]] = ...) -> None: ...

class EditTicketRes(_message.Message):
    __slots__ = ("is_edited",)
    IS_EDITED_FIELD_NUMBER: _ClassVar[int]
    is_edited: bool
    def __init__(self, is_edited: bool = ...) -> None: ...

class ListTicketsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTicketsRes(_message.Message):
    __slots__ = ("tickets",)
    TICKETS_FIELD_NUMBER: _ClassVar[int]
    tickets: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Ticket]
    def __init__(self, tickets: _Optional[_Iterable[_Union[_tickets_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class AssignTicketReq(_message.Message):
    __slots__ = ("ticket_sid", "assignee_list", "assigned_id")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_LIST_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    assignee_list: str
    assigned_id: str
    def __init__(self, ticket_sid: _Optional[int] = ..., assignee_list: _Optional[str] = ..., assigned_id: _Optional[str] = ...) -> None: ...

class AssignTicketRes(_message.Message):
    __slots__ = ("ticket_sid", "assignee_list", "assigned_id")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_LIST_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    assignee_list: str
    assigned_id: str
    def __init__(self, ticket_sid: _Optional[int] = ..., assignee_list: _Optional[str] = ..., assigned_id: _Optional[str] = ...) -> None: ...

class ViewTicketReq(_message.Message):
    __slots__ = ("ticket_sid", "ticket_code")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    ticket_code: str
    def __init__(self, ticket_sid: _Optional[int] = ..., ticket_code: _Optional[str] = ...) -> None: ...

class ViewTicketRes(_message.Message):
    __slots__ = ("ticket", "comments", "reply_comment")
    TICKET_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    REPLY_COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket: _tickets_pb2.Ticket
    comments: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Comment]
    reply_comment: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.ReplyComment]
    def __init__(self, ticket: _Optional[_Union[_tickets_pb2.Ticket, _Mapping]] = ..., comments: _Optional[_Iterable[_Union[_tickets_pb2.Comment, _Mapping]]] = ..., reply_comment: _Optional[_Iterable[_Union[_tickets_pb2.ReplyComment, _Mapping]]] = ...) -> None: ...

class CreateCommentReq(_message.Message):
    __slots__ = ("ticket_sid", "comment", "ticket_code")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    comment: str
    ticket_code: str
    def __init__(self, ticket_sid: _Optional[int] = ..., comment: _Optional[str] = ..., ticket_code: _Optional[str] = ...) -> None: ...

class CreateCommentRes(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _tickets_pb2.Comment
    def __init__(self, comment: _Optional[_Union[_tickets_pb2.Comment, _Mapping]] = ...) -> None: ...

class CloseTicketReq(_message.Message):
    __slots__ = ("ticket_sid", "comment", "from_status", "ticket_code")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FROM_STATUS_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    comment: str
    from_status: int
    ticket_code: str
    def __init__(self, ticket_sid: _Optional[int] = ..., comment: _Optional[str] = ..., from_status: _Optional[int] = ..., ticket_code: _Optional[str] = ...) -> None: ...

class CloseTicketRes(_message.Message):
    __slots__ = ("is_status",)
    IS_STATUS_FIELD_NUMBER: _ClassVar[int]
    is_status: bool
    def __init__(self, is_status: bool = ...) -> None: ...

class CreateSlaReq(_message.Message):
    __slots__ = ("sla_sid", "name", "description", "interval", "duration")
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    sla_sid: int
    name: str
    description: str
    interval: int
    duration: _tickets_pb2.Duration
    def __init__(self, sla_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., interval: _Optional[int] = ..., duration: _Optional[_Union[_tickets_pb2.Duration, _Mapping]] = ...) -> None: ...

class CreateSlaRes(_message.Message):
    __slots__ = ("sla",)
    SLA_FIELD_NUMBER: _ClassVar[int]
    sla: _tickets_pb2.TicketSla
    def __init__(self, sla: _Optional[_Union[_tickets_pb2.TicketSla, _Mapping]] = ...) -> None: ...

class ListSlaReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSlaRes(_message.Message):
    __slots__ = ("ticketsSla",)
    TICKETSSLA_FIELD_NUMBER: _ClassVar[int]
    ticketsSla: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.TicketSla]
    def __init__(self, ticketsSla: _Optional[_Iterable[_Union[_tickets_pb2.TicketSla, _Mapping]]] = ...) -> None: ...

class UpdateSlaReq(_message.Message):
    __slots__ = ("sla_sid", "is_active")
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    sla_sid: int
    is_active: int
    def __init__(self, sla_sid: _Optional[int] = ..., is_active: _Optional[int] = ...) -> None: ...

class UpdateSlaRes(_message.Message):
    __slots__ = ("ticketsSla",)
    TICKETSSLA_FIELD_NUMBER: _ClassVar[int]
    ticketsSla: _tickets_pb2.TicketSla
    def __init__(self, ticketsSla: _Optional[_Union[_tickets_pb2.TicketSla, _Mapping]] = ...) -> None: ...

class ListSlaConditionReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSlaConditionRes(_message.Message):
    __slots__ = ("slaCondition",)
    SLACONDITION_FIELD_NUMBER: _ClassVar[int]
    slaCondition: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.SlaConditions]
    def __init__(self, slaCondition: _Optional[_Iterable[_Union[_tickets_pb2.SlaConditions, _Mapping]]] = ...) -> None: ...

class ReplyCommentReq(_message.Message):
    __slots__ = ("comment_sid", "ticket_sid", "reply", "created_by_id", "ticket_code")
    COMMENT_SID_FIELD_NUMBER: _ClassVar[int]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    comment_sid: int
    ticket_sid: int
    reply: str
    created_by_id: str
    ticket_code: str
    def __init__(self, comment_sid: _Optional[int] = ..., ticket_sid: _Optional[int] = ..., reply: _Optional[str] = ..., created_by_id: _Optional[str] = ..., ticket_code: _Optional[str] = ...) -> None: ...

class ReplyCommentRes(_message.Message):
    __slots__ = ("is_created",)
    IS_CREATED_FIELD_NUMBER: _ClassVar[int]
    is_created: _tickets_pb2.ConfirmReplyComment
    def __init__(self, is_created: _Optional[_Union[_tickets_pb2.ConfirmReplyComment, _Mapping]] = ...) -> None: ...

class CreateSelfAssignReq(_message.Message):
    __slots__ = ("ticket_sid",)
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    def __init__(self, ticket_sid: _Optional[int] = ...) -> None: ...

class CreateSelfAssignRes(_message.Message):
    __slots__ = ("is_assigned",)
    IS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    is_assigned: bool
    def __init__(self, is_assigned: bool = ...) -> None: ...

class ListSkillsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillsResponse(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    def __init__(self, skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("skill_id", "name")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    name: str
    def __init__(self, skill_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("user_id", "first_name", "last_name", "is_active")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    first_name: str
    last_name: str
    is_active: bool
    def __init__(self, user_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., is_active: bool = ...) -> None: ...

class CreateTicketActionRequest(_message.Message):
    __slots__ = ("ticket_action",)
    TICKET_ACTION_FIELD_NUMBER: _ClassVar[int]
    ticket_action: _tickets_pb2.TicketAction
    def __init__(self, ticket_action: _Optional[_Union[_tickets_pb2.TicketAction, _Mapping]] = ...) -> None: ...

class CreateTicketActionResponse(_message.Message):
    __slots__ = ("ticket_action",)
    TICKET_ACTION_FIELD_NUMBER: _ClassVar[int]
    ticket_action: _tickets_pb2.TicketAction
    def __init__(self, ticket_action: _Optional[_Union[_tickets_pb2.TicketAction, _Mapping]] = ...) -> None: ...

class CloseTicketActionRequest(_message.Message):
    __slots__ = ("ticket_action_id", "ticket_id", "comment", "ticket_code")
    TICKET_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    ticket_action_id: int
    ticket_id: int
    comment: str
    ticket_code: str
    def __init__(self, ticket_action_id: _Optional[int] = ..., ticket_id: _Optional[int] = ..., comment: _Optional[str] = ..., ticket_code: _Optional[str] = ...) -> None: ...

class CloseTicketActionResponse(_message.Message):
    __slots__ = ("is_closed",)
    IS_CLOSED_FIELD_NUMBER: _ClassVar[int]
    is_closed: bool
    def __init__(self, is_closed: bool = ...) -> None: ...

class AssignTicketActionRequest(_message.Message):
    __slots__ = ("ticket_action_id",)
    TICKET_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_action_id: int
    def __init__(self, ticket_action_id: _Optional[int] = ...) -> None: ...

class AssignTicketActionResponse(_message.Message):
    __slots__ = ("is_assigned",)
    IS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    is_assigned: bool
    def __init__(self, is_assigned: bool = ...) -> None: ...

class ChangeTicketStatusRequest(_message.Message):
    __slots__ = ("ticket_id", "status_id", "ticket_status")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_STATUS_FIELD_NUMBER: _ClassVar[int]
    ticket_id: int
    status_id: int
    ticket_status: _tickets_pb2.TicketStatus
    def __init__(self, ticket_id: _Optional[int] = ..., status_id: _Optional[int] = ..., ticket_status: _Optional[_Union[_tickets_pb2.TicketStatus, str]] = ...) -> None: ...

class ChangeTicketStatusResponse(_message.Message):
    __slots__ = ("is_status_edited",)
    IS_STATUS_EDITED_FIELD_NUMBER: _ClassVar[int]
    is_status_edited: bool
    def __init__(self, is_status_edited: bool = ...) -> None: ...

class AddEntityRefRequest(_message.Message):
    __slots__ = ("entity_ref",)
    ENTITY_REF_FIELD_NUMBER: _ClassVar[int]
    entity_ref: EntityRef
    def __init__(self, entity_ref: _Optional[_Union[EntityRef, _Mapping]] = ...) -> None: ...

class AddEntityRefResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEntityRefsByTicketRequest(_message.Message):
    __slots__ = ("ticket_code",)
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    def __init__(self, ticket_code: _Optional[str] = ...) -> None: ...

class ListEntityRefsByTicketResponse(_message.Message):
    __slots__ = ("entity_ref",)
    ENTITY_REF_FIELD_NUMBER: _ClassVar[int]
    entity_ref: _containers.RepeatedCompositeFieldContainer[EntityRef]
    def __init__(self, entity_ref: _Optional[_Iterable[_Union[EntityRef, _Mapping]]] = ...) -> None: ...

class ListTicketsByEntityRefRequest(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class ListTicketsByEntityRefResponse(_message.Message):
    __slots__ = ("tickets",)
    TICKETS_FIELD_NUMBER: _ClassVar[int]
    tickets: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.Ticket]
    def __init__(self, tickets: _Optional[_Iterable[_Union[_tickets_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class CreateCustomFieldRequest(_message.Message):
    __slots__ = ("ticket_code", "project_id", "custom_field")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    custom_field: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.CustomField]
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ..., custom_field: _Optional[_Iterable[_Union[_tickets_pb2.CustomField, _Mapping]]] = ...) -> None: ...

class CreateCustomFieldResponse(_message.Message):
    __slots__ = ("ticket_code", "project_id", "custom_field")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    custom_field: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.CustomField]
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ..., custom_field: _Optional[_Iterable[_Union[_tickets_pb2.CustomField, _Mapping]]] = ...) -> None: ...

class EditCustomFieldRequest(_message.Message):
    __slots__ = ("ticket_code", "project_id", "edit_value")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    edit_value: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.CustomField]
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ..., edit_value: _Optional[_Iterable[_Union[_tickets_pb2.CustomField, _Mapping]]] = ...) -> None: ...

class EditCustomFieldResponse(_message.Message):
    __slots__ = ("ticket_code", "project_id", "edited_custom_field")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    edited_custom_field: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.CustomField]
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ..., edited_custom_field: _Optional[_Iterable[_Union[_tickets_pb2.CustomField, _Mapping]]] = ...) -> None: ...

class ListCustomFieldsRequest(_message.Message):
    __slots__ = ("ticket_code", "project_id")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ...) -> None: ...

class ListCustomFieldsResponse(_message.Message):
    __slots__ = ("ticket_code", "project_id", "custom_fields")
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ticket_code: str
    project_id: int
    custom_fields: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.CustomField]
    def __init__(self, ticket_code: _Optional[str] = ..., project_id: _Optional[int] = ..., custom_fields: _Optional[_Iterable[_Union[_tickets_pb2.CustomField, _Mapping]]] = ...) -> None: ...

class EntityRef(_message.Message):
    __slots__ = ("org_id", "region_id", "ticket_code", "uri")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region_id: str
    ticket_code: str
    uri: str
    def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., ticket_code: _Optional[str] = ..., uri: _Optional[str] = ...) -> None: ...
