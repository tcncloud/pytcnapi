from api.v1alpha1.contactmanager import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContactManagerEntryAddEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerEntryGetEncEvent(_message.Message):
    __slots__ = ("contact_manager_list_id", "contact_manager_entry_id", "created_by_id")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    contact_manager_entry_id: int
    created_by_id: str
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., contact_manager_entry_id: _Optional[int] = ..., created_by_id: _Optional[str] = ...) -> None: ...

class ContactManagerDeleteEvent(_message.Message):
    __slots__ = ("contact_manager_list_id", "deleted_by")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    deleted_by: str
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., deleted_by: _Optional[str] = ...) -> None: ...

class ContactManagerKycEvent(_message.Message):
    __slots__ = ("contact_manager_list_id", "kyc_details", "project_id", "created_by_id", "is_encrypted")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    KYC_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    kyc_details: _containers.RepeatedCompositeFieldContainer[_contactmanager_pb2.ContactManagerEntryVal]
    project_id: str
    created_by_id: str
    is_encrypted: bool
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., kyc_details: _Optional[_Iterable[_Union[_contactmanager_pb2.ContactManagerEntryVal, _Mapping]]] = ..., project_id: _Optional[str] = ..., created_by_id: _Optional[str] = ..., is_encrypted: bool = ...) -> None: ...
