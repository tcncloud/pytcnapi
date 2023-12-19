from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeScale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_SCALE_MINUTE: _ClassVar[TimeScale]
    TIME_SCALE_HOUR: _ClassVar[TimeScale]
    TIME_SCALE_DAY: _ClassVar[TimeScale]
    TIME_SCALE_WEEK: _ClassVar[TimeScale]
    TIME_SCALE_MONTH: _ClassVar[TimeScale]
    TIME_SCALE_YEAR: _ClassVar[TimeScale]

class TicketStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TICKET_STATUS_NEW: _ClassVar[TicketStatus]
    TICKET_STATUS_OPEN: _ClassVar[TicketStatus]
    TICKET_STATUS_CLOSE: _ClassVar[TicketStatus]

class PhoneNumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOBILE: _ClassVar[PhoneNumberType]
    OTHER: _ClassVar[PhoneNumberType]
    INVALID_ERROR: _ClassVar[PhoneNumberType]
TIME_SCALE_MINUTE: TimeScale
TIME_SCALE_HOUR: TimeScale
TIME_SCALE_DAY: TimeScale
TIME_SCALE_WEEK: TimeScale
TIME_SCALE_MONTH: TimeScale
TIME_SCALE_YEAR: TimeScale
TICKET_STATUS_NEW: TicketStatus
TICKET_STATUS_OPEN: TicketStatus
TICKET_STATUS_CLOSE: TicketStatus
MOBILE: PhoneNumberType
OTHER: PhoneNumberType
INVALID_ERROR: PhoneNumberType

class Ticket(_message.Message):
    __slots__ = ("ticket_sid", "project_sid", "project_title", "ticket_code", "title", "description", "org_id", "created_by_id", "created_by_name", "created_by_date", "due_date", "assignee_list", "metadata", "ticket_skills", "status", "ticket_sla", "assignee", "ticket_action", "ticket_status", "ticket_assignee", "ticket_participant")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    TICKET_CODE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_DATE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_LIST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TICKET_SKILLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TICKET_SLA_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    TICKET_ACTION_FIELD_NUMBER: _ClassVar[int]
    TICKET_STATUS_FIELD_NUMBER: _ClassVar[int]
    TICKET_ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    TICKET_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    project_sid: int
    project_title: str
    ticket_code: str
    title: str
    description: str
    org_id: str
    created_by_id: str
    created_by_name: str
    created_by_date: _timestamp_pb2.Timestamp
    due_date: _timestamp_pb2.Timestamp
    assignee_list: str
    metadata: _containers.RepeatedCompositeFieldContainer[Metadata]
    ticket_skills: _containers.RepeatedCompositeFieldContainer[Skills]
    status: int
    ticket_sla: _containers.RepeatedCompositeFieldContainer[Sla]
    assignee: str
    ticket_action: _containers.RepeatedCompositeFieldContainer[TicketAction]
    ticket_status: TicketStatus
    ticket_assignee: _containers.RepeatedScalarFieldContainer[str]
    ticket_participant: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ticket_sid: _Optional[int] = ..., project_sid: _Optional[int] = ..., project_title: _Optional[str] = ..., ticket_code: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., org_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_by_name: _Optional[str] = ..., created_by_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignee_list: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ..., ticket_skills: _Optional[_Iterable[_Union[Skills, _Mapping]]] = ..., status: _Optional[int] = ..., ticket_sla: _Optional[_Iterable[_Union[Sla, _Mapping]]] = ..., assignee: _Optional[str] = ..., ticket_action: _Optional[_Iterable[_Union[TicketAction, _Mapping]]] = ..., ticket_status: _Optional[_Union[TicketStatus, str]] = ..., ticket_assignee: _Optional[_Iterable[str]] = ..., ticket_participant: _Optional[_Iterable[str]] = ...) -> None: ...

class TicketTemplate(_message.Message):
    __slots__ = ("ticket_template_id", "org_id", "template", "template_entity_version", "template_name", "created_by_id", "modified_by", "created_date", "modified_date", "is_active", "template_id")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ENTITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: int
    org_id: str
    template: str
    template_entity_version: str
    template_name: str
    created_by_id: str
    modified_by: str
    created_date: _timestamp_pb2.Timestamp
    modified_date: _timestamp_pb2.Timestamp
    is_active: bool
    template_id: int
    def __init__(self, ticket_template_id: _Optional[int] = ..., org_id: _Optional[str] = ..., template: _Optional[str] = ..., template_entity_version: _Optional[str] = ..., template_name: _Optional[str] = ..., created_by_id: _Optional[str] = ..., modified_by: _Optional[str] = ..., created_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modified_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: bool = ..., template_id: _Optional[int] = ...) -> None: ...

class TicketProjectTemplate(_message.Message):
    __slots__ = ("ticket_template", "project_description")
    TICKET_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ticket_template: TicketTemplate
    project_description: _containers.RepeatedCompositeFieldContainer[ProjectDescription]
    def __init__(self, ticket_template: _Optional[_Union[TicketTemplate, _Mapping]] = ..., project_description: _Optional[_Iterable[_Union[ProjectDescription, _Mapping]]] = ...) -> None: ...

class ProjectDescription(_message.Message):
    __slots__ = ("project_id", "project_title")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    project_title: str
    def __init__(self, project_id: _Optional[int] = ..., project_title: _Optional[str] = ...) -> None: ...

class ListTemplate(_message.Message):
    __slots__ = ("ticket_template_id", "template_name", "project_id", "template", "template_entity_version", "is_active", "created_by_id", "created_date", "project_title", "assigned_project")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ENTITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: int
    template_name: str
    project_id: int
    template: str
    template_entity_version: str
    is_active: bool
    created_by_id: str
    created_date: _timestamp_pb2.Timestamp
    project_title: str
    assigned_project: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ticket_template_id: _Optional[int] = ..., template_name: _Optional[str] = ..., project_id: _Optional[int] = ..., template: _Optional[str] = ..., template_entity_version: _Optional[str] = ..., is_active: bool = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., project_title: _Optional[str] = ..., assigned_project: _Optional[_Iterable[int]] = ...) -> None: ...

class AssignProjectTemplate(_message.Message):
    __slots__ = ("ticket_template_id", "project_id")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: _containers.RepeatedScalarFieldContainer[int]
    project_id: int
    def __init__(self, ticket_template_id: _Optional[_Iterable[int]] = ..., project_id: _Optional[int] = ...) -> None: ...

class Duration(_message.Message):
    __slots__ = ("value", "scale")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    value: int
    scale: TimeScale
    def __init__(self, value: _Optional[int] = ..., scale: _Optional[_Union[TimeScale, str]] = ...) -> None: ...

class TicketAction(_message.Message):
    __slots__ = ("ticket_action_id", "action_id", "callback_context", "ticket_id", "start_ts", "expiry_ts", "state", "action_skills", "action_sla_id", "work_done_by", "voice_context", "sms_context", "email_context", "action_type")
    TICKET_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    START_TS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_SKILLS_FIELD_NUMBER: _ClassVar[int]
    ACTION_SLA_ID_FIELD_NUMBER: _ClassVar[int]
    WORK_DONE_BY_FIELD_NUMBER: _ClassVar[int]
    VOICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SMS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ticket_action_id: int
    action_id: int
    callback_context: CallbackContext
    ticket_id: int
    start_ts: _timestamp_pb2.Timestamp
    expiry_ts: _timestamp_pb2.Timestamp
    state: int
    action_skills: _containers.RepeatedScalarFieldContainer[str]
    action_sla_id: _containers.RepeatedCompositeFieldContainer[Sla]
    work_done_by: str
    voice_context: CallbackContext
    sms_context: SmsbackContext
    email_context: EmailbackContext
    action_type: ActionType
    def __init__(self, ticket_action_id: _Optional[int] = ..., action_id: _Optional[int] = ..., callback_context: _Optional[_Union[CallbackContext, _Mapping]] = ..., ticket_id: _Optional[int] = ..., start_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiry_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[int] = ..., action_skills: _Optional[_Iterable[str]] = ..., action_sla_id: _Optional[_Iterable[_Union[Sla, _Mapping]]] = ..., work_done_by: _Optional[str] = ..., voice_context: _Optional[_Union[CallbackContext, _Mapping]] = ..., sms_context: _Optional[_Union[SmsbackContext, _Mapping]] = ..., email_context: _Optional[_Union[EmailbackContext, _Mapping]] = ..., action_type: _Optional[_Union[ActionType, _Mapping]] = ...) -> None: ...

class CallbackContext(_message.Message):
    __slots__ = ("caller_id", "phone_no", "country_code", "caller_name", "caller_country_code")
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NO_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CALLER_NAME_FIELD_NUMBER: _ClassVar[int]
    CALLER_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    phone_no: str
    country_code: str
    caller_name: str
    caller_country_code: str
    def __init__(self, caller_id: _Optional[str] = ..., phone_no: _Optional[str] = ..., country_code: _Optional[str] = ..., caller_name: _Optional[str] = ..., caller_country_code: _Optional[str] = ...) -> None: ...

class SmsbackContext(_message.Message):
    __slots__ = ("contact_name", "to_sms", "from_sms", "to_country_code", "from_country_code")
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_SMS_FIELD_NUMBER: _ClassVar[int]
    FROM_SMS_FIELD_NUMBER: _ClassVar[int]
    TO_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    FROM_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    contact_name: str
    to_sms: str
    from_sms: str
    to_country_code: str
    from_country_code: str
    def __init__(self, contact_name: _Optional[str] = ..., to_sms: _Optional[str] = ..., from_sms: _Optional[str] = ..., to_country_code: _Optional[str] = ..., from_country_code: _Optional[str] = ...) -> None: ...

class ActionType(_message.Message):
    __slots__ = ("action_type_id", "action_name")
    ACTION_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    action_type_id: int
    action_name: str
    def __init__(self, action_type_id: _Optional[int] = ..., action_name: _Optional[str] = ...) -> None: ...

class EmailbackContext(_message.Message):
    __slots__ = ("contact_name", "to_email", "from_email")
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_EMAIL_FIELD_NUMBER: _ClassVar[int]
    FROM_EMAIL_FIELD_NUMBER: _ClassVar[int]
    contact_name: str
    to_email: str
    from_email: str
    def __init__(self, contact_name: _Optional[str] = ..., to_email: _Optional[str] = ..., from_email: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Skills(_message.Message):
    __slots__ = ("skill_id", "is_preferred")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PREFERRED_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    is_preferred: bool
    def __init__(self, skill_id: _Optional[str] = ..., is_preferred: bool = ...) -> None: ...

class Sla(_message.Message):
    __slots__ = ("condition_sid", "sla_sid", "sla_min", "sla_duration")
    CONDITION_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_MIN_FIELD_NUMBER: _ClassVar[int]
    SLA_DURATION_FIELD_NUMBER: _ClassVar[int]
    condition_sid: int
    sla_sid: int
    sla_min: int
    sla_duration: Duration
    def __init__(self, condition_sid: _Optional[int] = ..., sla_sid: _Optional[int] = ..., sla_min: _Optional[int] = ..., sla_duration: _Optional[_Union[Duration, _Mapping]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("comment_sid", "ticket_sid", "comment", "created_by_id", "created_by_name", "created_by_date")
    COMMENT_SID_FIELD_NUMBER: _ClassVar[int]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_DATE_FIELD_NUMBER: _ClassVar[int]
    comment_sid: int
    ticket_sid: int
    comment: str
    created_by_id: str
    created_by_name: str
    created_by_date: _timestamp_pb2.Timestamp
    def __init__(self, comment_sid: _Optional[int] = ..., ticket_sid: _Optional[int] = ..., comment: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_by_name: _Optional[str] = ..., created_by_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CloseTicket(_message.Message):
    __slots__ = ("ticket_sid", "status", "comment", "from_status", "created_by_id")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FROM_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    status: int
    comment: str
    from_status: int
    created_by_id: str
    def __init__(self, ticket_sid: _Optional[int] = ..., status: _Optional[int] = ..., comment: _Optional[str] = ..., from_status: _Optional[int] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class ConfirmClose(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class TicketProject(_message.Message):
    __slots__ = ("ticket_project_id", "org_id", "project_sid", "project_code", "project_title", "is_active", "template_desc")
    TICKET_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DESC_FIELD_NUMBER: _ClassVar[int]
    ticket_project_id: int
    org_id: str
    project_sid: int
    project_code: str
    project_title: str
    is_active: bool
    template_desc: _containers.RepeatedCompositeFieldContainer[TemplateDescription]
    def __init__(self, ticket_project_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_sid: _Optional[int] = ..., project_code: _Optional[str] = ..., project_title: _Optional[str] = ..., is_active: bool = ..., template_desc: _Optional[_Iterable[_Union[TemplateDescription, _Mapping]]] = ...) -> None: ...

class TemplateDescription(_message.Message):
    __slots__ = ("ticket_template_id", "template_name")
    TICKET_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    ticket_template_id: int
    template_name: str
    def __init__(self, ticket_template_id: _Optional[int] = ..., template_name: _Optional[str] = ...) -> None: ...

class TicketSla(_message.Message):
    __slots__ = ("sla_sid", "name", "description", "interval", "is_active", "ticket_sla_duration")
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TICKET_SLA_DURATION_FIELD_NUMBER: _ClassVar[int]
    sla_sid: int
    name: str
    description: str
    interval: int
    is_active: int
    ticket_sla_duration: Duration
    def __init__(self, sla_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., interval: _Optional[int] = ..., is_active: _Optional[int] = ..., ticket_sla_duration: _Optional[_Union[Duration, _Mapping]] = ...) -> None: ...

class SlaConditions(_message.Message):
    __slots__ = ("sla_condition_sid", "sla_condition_name")
    SLA_CONDITION_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_CONDITION_NAME_FIELD_NUMBER: _ClassVar[int]
    sla_condition_sid: int
    sla_condition_name: str
    def __init__(self, sla_condition_sid: _Optional[int] = ..., sla_condition_name: _Optional[str] = ...) -> None: ...

class ReplyComment(_message.Message):
    __slots__ = ("comment_sid", "ticket_sid", "reply", "created_by_id", "created_by_date")
    COMMENT_SID_FIELD_NUMBER: _ClassVar[int]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_DATE_FIELD_NUMBER: _ClassVar[int]
    comment_sid: int
    ticket_sid: int
    reply: str
    created_by_id: str
    created_by_date: _timestamp_pb2.Timestamp
    def __init__(self, comment_sid: _Optional[int] = ..., ticket_sid: _Optional[int] = ..., reply: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_by_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConfirmReplyComment(_message.Message):
    __slots__ = ("is_created",)
    IS_CREATED_FIELD_NUMBER: _ClassVar[int]
    is_created: bool
    def __init__(self, is_created: bool = ...) -> None: ...

class TicketAuditLog(_message.Message):
    __slots__ = ("ticket_audit_event_log_id", "org_id", "event", "ticket_sid", "event_type", "created_by_id", "created_by_date")
    TICKET_AUDIT_EVENT_LOG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_DATE_FIELD_NUMBER: _ClassVar[int]
    ticket_audit_event_log_id: str
    org_id: str
    event: str
    ticket_sid: int
    event_type: str
    created_by_id: str
    created_by_date: _timestamp_pb2.Timestamp
    def __init__(self, ticket_audit_event_log_id: _Optional[str] = ..., org_id: _Optional[str] = ..., event: _Optional[str] = ..., ticket_sid: _Optional[int] = ..., event_type: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_by_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EditTicket(_message.Message):
    __slots__ = ("ticket_sid", "edit_value")
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    edit_value: EditAttribute
    def __init__(self, ticket_sid: _Optional[int] = ..., edit_value: _Optional[_Union[EditAttribute, _Mapping]] = ...) -> None: ...

class EditAttribute(_message.Message):
    __slots__ = ("col_desc", "from_val", "to_val", "is_edited")
    COL_DESC_FIELD_NUMBER: _ClassVar[int]
    FROM_VAL_FIELD_NUMBER: _ClassVar[int]
    TO_VAL_FIELD_NUMBER: _ClassVar[int]
    IS_EDITED_FIELD_NUMBER: _ClassVar[int]
    col_desc: int
    from_val: str
    to_val: str
    is_edited: bool
    def __init__(self, col_desc: _Optional[int] = ..., from_val: _Optional[str] = ..., to_val: _Optional[str] = ..., is_edited: bool = ...) -> None: ...
