from api.commons import tickets_pb2 as _tickets_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TicketEvent(_message.Message):
    __slots__ = ()
    EDITTICKET_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    editticket: _tickets_pb2.EditTicket
    created_by_id: str
    def __init__(self, editticket: _Optional[_Union[_tickets_pb2.EditTicket, _Mapping]] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class TicketCustomFieldCreateEvent(_message.Message):
    __slots__ = ()
    TICKET_CUSTOM_FIELD_AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_custom_field_audit_log: _tickets_pb2.TicketCustomFieldAuditLog
    created_by_id: str
    def __init__(self, ticket_custom_field_audit_log: _Optional[_Union[_tickets_pb2.TicketCustomFieldAuditLog, _Mapping]] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class TicketCustomFieldEditEvent(_message.Message):
    __slots__ = ()
    TICKET_CUSTOM_FIELD_AUDIT_LOG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_custom_field_audit_log: _tickets_pb2.TicketCustomFieldAuditLog
    created_by_id: str
    def __init__(self, ticket_custom_field_audit_log: _Optional[_Union[_tickets_pb2.TicketCustomFieldAuditLog, _Mapping]] = ..., created_by_id: _Optional[str] = ...) -> None: ...
