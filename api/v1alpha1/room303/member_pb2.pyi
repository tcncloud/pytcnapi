from api.commons import room303_pb2 as _room303_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddRoomMemberRequest(_message.Message):
    __slots__ = ("room_id", "user_id", "admin")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    user_id: str
    admin: bool
    def __init__(self, room_id: _Optional[str] = ..., user_id: _Optional[str] = ..., admin: bool = ...) -> None: ...

class RemoveRoomMemberRequest(_message.Message):
    __slots__ = ("user_id", "room_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    room_id: str
    def __init__(self, user_id: _Optional[str] = ..., room_id: _Optional[str] = ...) -> None: ...

class RemoveRoomMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRoomMembersRequest(_message.Message):
    __slots__ = ("room_id",)
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    def __init__(self, room_id: _Optional[str] = ...) -> None: ...

class ListRoomMembersResponse(_message.Message):
    __slots__ = ("members",)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_room303_pb2.Member]
    def __init__(self, members: _Optional[_Iterable[_Union[_room303_pb2.Member, _Mapping]]] = ...) -> None: ...

class SetAdminForRoomMemberRequest(_message.Message):
    __slots__ = ("room_id", "user_id")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    user_id: str
    def __init__(self, room_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SetAdminForRoomMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinRoomRequest(_message.Message):
    __slots__ = ("room_id",)
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    def __init__(self, room_id: _Optional[str] = ...) -> None: ...

class GetRoomMemberRequest(_message.Message):
    __slots__ = ("room_id", "user_id")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    user_id: str
    def __init__(self, room_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
