from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["ticket_sid", "project_sid", "project_title", "ticket_code", "title", "description", "org_id", "created_by_id", "created_by_name", "created_by_date", "due_date", "assignee_list", "metadata", "ticket_skills", "status", "ticket_sla", "assignee"]
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
    def __init__(self, ticket_sid: _Optional[int] = ..., project_sid: _Optional[int] = ..., project_title: _Optional[str] = ..., ticket_code: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., org_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_by_name: _Optional[str] = ..., created_by_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignee_list: _Optional[str] = ..., metadata: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ..., ticket_skills: _Optional[_Iterable[_Union[Skills, _Mapping]]] = ..., status: _Optional[int] = ..., ticket_sla: _Optional[_Iterable[_Union[Sla, _Mapping]]] = ..., assignee: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Skills(_message.Message):
    __slots__ = ["skill_id", "is_preferred"]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PREFERRED_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    is_preferred: bool
    def __init__(self, skill_id: _Optional[str] = ..., is_preferred: bool = ...) -> None: ...

class Sla(_message.Message):
    __slots__ = ["condition_sid", "sla_sid", "sla_min"]
    CONDITION_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_MIN_FIELD_NUMBER: _ClassVar[int]
    condition_sid: int
    sla_sid: int
    sla_min: int
    def __init__(self, condition_sid: _Optional[int] = ..., sla_sid: _Optional[int] = ..., sla_min: _Optional[int] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ["comment_sid", "ticket_sid", "comment", "created_by_id", "created_by_name", "created_by_date"]
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
    __slots__ = ["ticket_sid", "status", "comment", "from_status", "created_by_id"]
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
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class TicketProject(_message.Message):
    __slots__ = ["ticket_project_id", "org_id", "project_sid", "project_code", "project_title", "is_active"]
    TICKET_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ticket_project_id: int
    org_id: str
    project_sid: int
    project_code: str
    project_title: str
    is_active: bool
    def __init__(self, ticket_project_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_sid: _Optional[int] = ..., project_code: _Optional[str] = ..., project_title: _Optional[str] = ..., is_active: bool = ...) -> None: ...

class TicketSla(_message.Message):
    __slots__ = ["sla_sid", "name", "description", "interval", "is_active"]
    SLA_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    sla_sid: int
    name: str
    description: str
    interval: int
    is_active: int
    def __init__(self, sla_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., interval: _Optional[int] = ..., is_active: _Optional[int] = ...) -> None: ...

class SlaConditions(_message.Message):
    __slots__ = ["sla_condition_sid", "sla_condition_name"]
    SLA_CONDITION_SID_FIELD_NUMBER: _ClassVar[int]
    SLA_CONDITION_NAME_FIELD_NUMBER: _ClassVar[int]
    sla_condition_sid: int
    sla_condition_name: str
    def __init__(self, sla_condition_sid: _Optional[int] = ..., sla_condition_name: _Optional[str] = ...) -> None: ...

class ReplyComment(_message.Message):
    __slots__ = ["comment_sid", "ticket_sid", "reply", "created_by_id", "created_by_date"]
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
    __slots__ = ["is_created"]
    IS_CREATED_FIELD_NUMBER: _ClassVar[int]
    is_created: bool
    def __init__(self, is_created: bool = ...) -> None: ...

class TicketAuditLog(_message.Message):
    __slots__ = ["ticket_audit_event_log_id", "org_id", "event", "ticket_sid", "event_type", "created_by_id", "created_by_date"]
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
    __slots__ = ["ticket_sid", "edit_value"]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    EDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    edit_value: EditAttribute
    def __init__(self, ticket_sid: _Optional[int] = ..., edit_value: _Optional[_Union[EditAttribute, _Mapping]] = ...) -> None: ...

class EditAttribute(_message.Message):
    __slots__ = ["col_desc", "from_val", "to_val", "is_edited"]
    COL_DESC_FIELD_NUMBER: _ClassVar[int]
    FROM_VAL_FIELD_NUMBER: _ClassVar[int]
    TO_VAL_FIELD_NUMBER: _ClassVar[int]
    IS_EDITED_FIELD_NUMBER: _ClassVar[int]
    col_desc: int
    from_val: str
    to_val: str
    is_edited: bool
    def __init__(self, col_desc: _Optional[int] = ..., from_val: _Optional[str] = ..., to_val: _Optional[str] = ..., is_edited: bool = ...) -> None: ...
