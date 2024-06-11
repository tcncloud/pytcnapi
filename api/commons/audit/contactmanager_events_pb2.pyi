from api.v1alpha1.contactmanager import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContactManagerEntryAddEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerEntryGetEncEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerDeleteEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContactManagerEntryEvent(_message.Message):
    __slots__ = ("ContactManagerListId", "ContactManagerEntryId", "ContactManagerEntryListIds")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYID_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYLISTIDS_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    ContactManagerEntryId: int
    ContactManagerEntryListIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ContactManagerListId: _Optional[int] = ..., ContactManagerEntryId: _Optional[int] = ..., ContactManagerEntryListIds: _Optional[_Iterable[int]] = ...) -> None: ...

class ContactManagerListUploadEvent(_message.Message):
    __slots__ = ("ContactManagerListId", "NumberOfContactsUploaded")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFCONTACTSUPLOADED_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    NumberOfContactsUploaded: int
    def __init__(self, ContactManagerListId: _Optional[int] = ..., NumberOfContactsUploaded: _Optional[int] = ...) -> None: ...

class ContactManagerKycEvent(_message.Message):
    __slots__ = ("ContactManagerListId", "ContactManagerEntryId", "types", "ContactManagerEntryListIds")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYID_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYLISTIDS_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    ContactManagerEntryId: int
    types: _containers.RepeatedScalarFieldContainer[str]
    ContactManagerEntryListIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ContactManagerListId: _Optional[int] = ..., ContactManagerEntryId: _Optional[int] = ..., types: _Optional[_Iterable[str]] = ..., ContactManagerEntryListIds: _Optional[_Iterable[int]] = ...) -> None: ...
