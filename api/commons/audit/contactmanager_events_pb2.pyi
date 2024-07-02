from api.v1alpha1.contactmanager import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContactManagerEntryAddEvent(_message.Message):
    __slots__ = ("addEvent",)
    ADDEVENT_FIELD_NUMBER: _ClassVar[int]
    addEvent: ContactManagerEntryEvent
    def __init__(self, addEvent: _Optional[_Union[ContactManagerEntryEvent, _Mapping]] = ...) -> None: ...

class ContactManagerEntryGetEncEvent(_message.Message):
    __slots__ = ("viewEvent",)
    VIEWEVENT_FIELD_NUMBER: _ClassVar[int]
    viewEvent: ContactManagerEntryEvent
    def __init__(self, viewEvent: _Optional[_Union[ContactManagerEntryEvent, _Mapping]] = ...) -> None: ...

class ContactManagerEntryEditEvent(_message.Message):
    __slots__ = ("editEvent",)
    EDITEVENT_FIELD_NUMBER: _ClassVar[int]
    editEvent: ContactManagerEntryEvent
    def __init__(self, editEvent: _Optional[_Union[ContactManagerEntryEvent, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("ContactManagerListId", "NumberOfContactsUploaded", "NumberOfSuccessfulContactsUploaded", "NumberOfFailedContacts")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFCONTACTSUPLOADED_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSUCCESSFULCONTACTSUPLOADED_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFFAILEDCONTACTS_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    NumberOfContactsUploaded: int
    NumberOfSuccessfulContactsUploaded: int
    NumberOfFailedContacts: int
    def __init__(self, ContactManagerListId: _Optional[int] = ..., NumberOfContactsUploaded: _Optional[int] = ..., NumberOfSuccessfulContactsUploaded: _Optional[int] = ..., NumberOfFailedContacts: _Optional[int] = ...) -> None: ...

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
