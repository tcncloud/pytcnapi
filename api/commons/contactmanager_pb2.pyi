from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeDuplicationMergeStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEEP_EXISTING_LIST: _ClassVar[DeDuplicationMergeStrategy]
    REPLACE_EXISTING_LIST: _ClassVar[DeDuplicationMergeStrategy]
KEEP_EXISTING_LIST: DeDuplicationMergeStrategy
REPLACE_EXISTING_LIST: DeDuplicationMergeStrategy

class ContactManagerEntry(_message.Message):
    __slots__ = ("contact_manager_entry_id", "contact_manager_entry_list_id", "key", "value", "type", "date_created")
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    contact_manager_entry_list_id: int
    key: str
    value: str
    type: str
    date_created: _timestamp_pb2.Timestamp
    def __init__(self, contact_manager_entry_id: _Optional[int] = ..., contact_manager_entry_list_id: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ContactManagerList(_message.Message):
    __slots__ = ("contact_manager_list_id", "org_id", "project_id", "file_name", "description", "list_details", "ttl", "date_created")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LIST_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    org_id: str
    project_id: int
    file_name: str
    description: str
    list_details: _containers.RepeatedScalarFieldContainer[str]
    ttl: int
    date_created: _timestamp_pb2.Timestamp
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_id: _Optional[int] = ..., file_name: _Optional[str] = ..., description: _Optional[str] = ..., list_details: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ContactManagerEntryVal(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
