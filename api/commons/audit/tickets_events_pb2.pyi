from api.commons import tickets_pb2 as _tickets_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TicketEvent(_message.Message):
    __slots__ = ["editticket", "created_by_id"]
    EDITTICKET_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    editticket: _tickets_pb2.EditTicket
    created_by_id: str
    def __init__(self, editticket: _Optional[_Union[_tickets_pb2.EditTicket, _Mapping]] = ..., created_by_id: _Optional[str] = ...) -> None: ...
