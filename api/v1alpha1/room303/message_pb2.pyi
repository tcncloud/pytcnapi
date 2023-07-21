from api.commons import room303_pb2 as _room303_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMessageRequest(_message.Message):
    __slots__ = ["room_id", "payload", "nonce"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    payload: str
    nonce: str
    def __init__(self, room_id: _Optional[str] = ..., payload: _Optional[str] = ..., nonce: _Optional[str] = ...) -> None: ...

class CreateMessageResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _room303_pb2.Message
    def __init__(self, message: _Optional[_Union[_room303_pb2.Message, _Mapping]] = ...) -> None: ...

class EditMessageRequest(_message.Message):
    __slots__ = ["message_id", "payload", "room_id", "nonce"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    payload: str
    room_id: str
    nonce: str
    def __init__(self, message_id: _Optional[str] = ..., payload: _Optional[str] = ..., room_id: _Optional[str] = ..., nonce: _Optional[str] = ...) -> None: ...

class EditMessageResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _room303_pb2.Message
    def __init__(self, message: _Optional[_Union[_room303_pb2.Message, _Mapping]] = ...) -> None: ...

class GetMessagesRequest(_message.Message):
    __slots__ = ["room_id", "offset"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    offset: _timestamp_pb2.Timestamp
    def __init__(self, room_id: _Optional[str] = ..., offset: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetMessagesResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_room303_pb2.Message]
    def __init__(self, messages: _Optional[_Iterable[_Union[_room303_pb2.Message, _Mapping]]] = ...) -> None: ...

class StreamMessageUpdatesRequest(_message.Message):
    __slots__ = ["room_id", "member_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    member_id: str
    def __init__(self, room_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class StreamMessageUpdatesResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _room303_pb2.Message
    def __init__(self, message: _Optional[_Union[_room303_pb2.Message, _Mapping]] = ...) -> None: ...

class MarkMessageReadRequest(_message.Message):
    __slots__ = ["message_id", "member_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    member_id: str
    def __init__(self, message_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class MarkMessageReadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MarkAllMessagesReadRequest(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    def __init__(self, room_id: _Optional[str] = ...) -> None: ...

class MarkAllMessagesReadResponse(_message.Message):
    __slots__ = ["rows_updated"]
    ROWS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    rows_updated: _containers.RepeatedCompositeFieldContainer[_room303_pb2.Message]
    def __init__(self, rows_updated: _Optional[_Iterable[_Union[_room303_pb2.Message, _Mapping]]] = ...) -> None: ...

class GetUnreadStatsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUnreadStatsResponse(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_room303_pb2.MessageStat]
    def __init__(self, stats: _Optional[_Iterable[_Union[_room303_pb2.MessageStat, _Mapping]]] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ["message_id", "room_id", "nonce"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    room_id: str
    nonce: str
    def __init__(self, message_id: _Optional[str] = ..., room_id: _Optional[str] = ..., nonce: _Optional[str] = ...) -> None: ...

class DeleteMessageResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _room303_pb2.Message
    def __init__(self, message: _Optional[_Union[_room303_pb2.Message, _Mapping]] = ...) -> None: ...

class BulkMarkMessageReadRequest(_message.Message):
    __slots__ = ["room_id", "message_ids"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, room_id: _Optional[str] = ..., message_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BulkMarkMessageReadResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_room303_pb2.Message]
    def __init__(self, messages: _Optional[_Iterable[_Union[_room303_pb2.Message, _Mapping]]] = ...) -> None: ...
