from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoomType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ROOM_TYPE_DIRECT: _ClassVar[RoomType]
    ROOM_TYPE_MULTI: _ClassVar[RoomType]
    ROOM_TYPE_SYSTEM: _ClassVar[RoomType]

class MessageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MESSAGE_STATUS_ACTIVE: _ClassVar[MessageStatus]
    MESSAGE_STATUS_EDITED: _ClassVar[MessageStatus]
    MESSAGE_STATUS_ARCHIVED: _ClassVar[MessageStatus]

class RoomStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ROOM_STATUS_ACTIVE: _ClassVar[RoomStatus]
    ROOM_STATUS_ARCHIVED: _ClassVar[RoomStatus]
    ROOM_STATUS_DELETED: _ClassVar[RoomStatus]
ROOM_TYPE_DIRECT: RoomType
ROOM_TYPE_MULTI: RoomType
ROOM_TYPE_SYSTEM: RoomType
MESSAGE_STATUS_ACTIVE: MessageStatus
MESSAGE_STATUS_EDITED: MessageStatus
MESSAGE_STATUS_ARCHIVED: MessageStatus
ROOM_STATUS_ACTIVE: RoomStatus
ROOM_STATUS_ARCHIVED: RoomStatus
ROOM_STATUS_DELETED: RoomStatus

class UserSid(_message.Message):
    __slots__ = ["user_id", "full_name", "display_name"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    full_name: str
    display_name: str
    def __init__(self, user_id: _Optional[str] = ..., full_name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ["user_sid", "added_by", "added_at", "room_id", "admin"]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    ADDED_BY_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    user_sid: UserSid
    added_by: UserSid
    added_at: _timestamp_pb2.Timestamp
    room_id: str
    admin: bool
    def __init__(self, user_sid: _Optional[_Union[UserSid, _Mapping]] = ..., added_by: _Optional[_Union[UserSid, _Mapping]] = ..., added_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., room_id: _Optional[str] = ..., admin: bool = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ["org_id", "room_id", "type", "created_at", "updated_at", "status", "id", "display_name"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    room_id: str
    type: RoomType
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    status: RoomStatus
    id: str
    display_name: str
    def __init__(self, org_id: _Optional[str] = ..., room_id: _Optional[str] = ..., type: _Optional[_Union[RoomType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[RoomStatus, str]] = ..., id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["org_id", "message_id", "room_id", "from_user", "status", "received_at", "updated_at", "payload", "unread", "nonce"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_USER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UNREAD_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    message_id: str
    room_id: str
    from_user: UserSid
    status: MessageStatus
    received_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    payload: str
    unread: bool
    nonce: str
    def __init__(self, org_id: _Optional[str] = ..., message_id: _Optional[str] = ..., room_id: _Optional[str] = ..., from_user: _Optional[_Union[UserSid, _Mapping]] = ..., status: _Optional[_Union[MessageStatus, str]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payload: _Optional[str] = ..., unread: bool = ..., nonce: _Optional[str] = ...) -> None: ...

class MessageStat(_message.Message):
    __slots__ = ["room_id", "unread_messages"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    UNREAD_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    unread_messages: int
    def __init__(self, room_id: _Optional[str] = ..., unread_messages: _Optional[int] = ...) -> None: ...
