from api.commons import room303_pb2 as _room303_pb2
from api.commons import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRoomRequest(_message.Message):
    __slots__ = ["name", "type", "members"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _room303_pb2.RoomType
    members: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_room303_pb2.RoomType, str]] = ..., members: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRoomRequest(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    def __init__(self, room_id: _Optional[str] = ...) -> None: ...

class ListAllRoomsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListRoomsForMemberRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListRoomsResponse(_message.Message):
    __slots__ = ["rooms"]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    rooms: _containers.RepeatedCompositeFieldContainer[_room303_pb2.Room]
    def __init__(self, rooms: _Optional[_Iterable[_Union[_room303_pb2.Room, _Mapping]]] = ...) -> None: ...

class ArchiveRoomRequest(_message.Message):
    __slots__ = ["room_id"]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    def __init__(self, room_id: _Optional[str] = ...) -> None: ...

class ListUsersNamesRequest(_message.Message):
    __slots__ = ["org_id", "agent", "archived_filter"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    agent: bool
    archived_filter: _user_pb2.UserArchivedStateFilter
    def __init__(self, org_id: _Optional[str] = ..., agent: bool = ..., archived_filter: _Optional[_Union[_user_pb2.UserArchivedStateFilter, str]] = ...) -> None: ...

class ListUsersNamesResponse(_message.Message):
    __slots__ = ["user_details"]
    USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    user_details: _containers.RepeatedCompositeFieldContainer[UserDetails]
    def __init__(self, user_details: _Optional[_Iterable[_Union[UserDetails, _Mapping]]] = ...) -> None: ...

class UserDetails(_message.Message):
    __slots__ = ["user_id", "user_name", "first_name", "last_name"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_name: str
    first_name: str
    last_name: str
    def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ...) -> None: ...
