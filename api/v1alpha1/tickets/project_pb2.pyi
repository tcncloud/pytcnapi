from api.commons.audit import audit_pb2 as _audit_pb2
from api.commons import tickets_pb2 as _tickets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnableProjectReq(_message.Message):
    __slots__ = ["project_sid", "project_code", "project_title", "is_active"]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    project_sid: int
    project_code: str
    project_title: str
    is_active: bool
    def __init__(self, project_sid: _Optional[int] = ..., project_code: _Optional[str] = ..., project_title: _Optional[str] = ..., is_active: bool = ...) -> None: ...

class EnableProjectRes(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListEnabledProjectsReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListEnabledProjectsRes(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_tickets_pb2.TicketProject]
    def __init__(self, projects: _Optional[_Iterable[_Union[_tickets_pb2.TicketProject, _Mapping]]] = ...) -> None: ...

class ListTicketAuditLogReq(_message.Message):
    __slots__ = ["ticket_sid"]
    TICKET_SID_FIELD_NUMBER: _ClassVar[int]
    ticket_sid: int
    def __init__(self, ticket_sid: _Optional[int] = ...) -> None: ...

class ListTicketAuditLogRes(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_audit_pb2.AuditEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_audit_pb2.AuditEvent, _Mapping]]] = ...) -> None: ...
