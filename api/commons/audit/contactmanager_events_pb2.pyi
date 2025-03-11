from api.commons import classifier_pb2 as _classifier_pb2
from api.commons import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    __slots__ = ("deleteEvent",)
    DELETEEVENT_FIELD_NUMBER: _ClassVar[int]
    deleteEvent: ContactManagerEntryEvent
    def __init__(self, deleteEvent: _Optional[_Union[ContactManagerEntryEvent, _Mapping]] = ...) -> None: ...

class ContactManagerEntryEvent(_message.Message):
    __slots__ = ("ContactManagerListId", "ContactManagerEntryId", "ContactManagerEntryListIds", "FieldChanges", "ContactUpdateTaskId")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYID_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERENTRYLISTIDS_FIELD_NUMBER: _ClassVar[int]
    FIELDCHANGES_FIELD_NUMBER: _ClassVar[int]
    CONTACTUPDATETASKID_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    ContactManagerEntryId: int
    ContactManagerEntryListIds: _containers.RepeatedScalarFieldContainer[int]
    FieldChanges: _containers.RepeatedCompositeFieldContainer[ContactFieldChanges]
    ContactUpdateTaskId: int
    def __init__(self, ContactManagerListId: _Optional[int] = ..., ContactManagerEntryId: _Optional[int] = ..., ContactManagerEntryListIds: _Optional[_Iterable[int]] = ..., FieldChanges: _Optional[_Iterable[_Union[ContactFieldChanges, _Mapping]]] = ..., ContactUpdateTaskId: _Optional[int] = ...) -> None: ...

class ContactFieldChanges(_message.Message):
    __slots__ = ("from_value", "to_value")
    FROM_VALUE_FIELD_NUMBER: _ClassVar[int]
    TO_VALUE_FIELD_NUMBER: _ClassVar[int]
    from_value: AuditedContactField
    to_value: AuditedContactField
    def __init__(self, from_value: _Optional[_Union[AuditedContactField, _Mapping]] = ..., to_value: _Optional[_Union[AuditedContactField, _Mapping]] = ...) -> None: ...

class AuditedContactField(_message.Message):
    __slots__ = ("contact_field_id", "name", "type", "value")
    CONTACT_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    contact_field_id: int
    name: str
    type: str
    value: str
    def __init__(self, contact_field_id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ContactManagerListUploadEvent(_message.Message):
    __slots__ = ("ContactManagerListId", "NumberOfContactsUploaded", "NumberOfSuccessfulContactsUploaded", "NumberOfFailedContacts", "NumberOfNewContacts", "NumberOfDuplicateContacts", "DeDupFieldType", "DeDupMergeStrategy", "ContactManagerListName", "FileName", "UpdateTaskId", "Ttl")
    CONTACTMANAGERLISTID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFCONTACTSUPLOADED_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSUCCESSFULCONTACTSUPLOADED_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFFAILEDCONTACTS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFNEWCONTACTS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDUPLICATECONTACTS_FIELD_NUMBER: _ClassVar[int]
    DEDUPFIELDTYPE_FIELD_NUMBER: _ClassVar[int]
    DEDUPMERGESTRATEGY_FIELD_NUMBER: _ClassVar[int]
    CONTACTMANAGERLISTNAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    UPDATETASKID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ContactManagerListId: int
    NumberOfContactsUploaded: int
    NumberOfSuccessfulContactsUploaded: int
    NumberOfFailedContacts: int
    NumberOfNewContacts: int
    NumberOfDuplicateContacts: int
    DeDupFieldType: _classifier_pb2.ClassifierEntityType
    DeDupMergeStrategy: _contactmanager_pb2.DeDuplicationMergeStrategy
    ContactManagerListName: str
    FileName: str
    UpdateTaskId: int
    Ttl: int
    def __init__(self, ContactManagerListId: _Optional[int] = ..., NumberOfContactsUploaded: _Optional[int] = ..., NumberOfSuccessfulContactsUploaded: _Optional[int] = ..., NumberOfFailedContacts: _Optional[int] = ..., NumberOfNewContacts: _Optional[int] = ..., NumberOfDuplicateContacts: _Optional[int] = ..., DeDupFieldType: _Optional[_Union[_classifier_pb2.ClassifierEntityType, str]] = ..., DeDupMergeStrategy: _Optional[_Union[_contactmanager_pb2.DeDuplicationMergeStrategy, str]] = ..., ContactManagerListName: _Optional[str] = ..., FileName: _Optional[str] = ..., UpdateTaskId: _Optional[int] = ..., Ttl: _Optional[int] = ...) -> None: ...

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

class ContactManagerEntityAssociationEvent(_message.Message):
    __slots__ = ("contact_manager_entry_id", "entity_id", "deleted", "is_active")
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    entity_id: str
    deleted: bool
    is_active: bool
    def __init__(self, contact_manager_entry_id: _Optional[int] = ..., entity_id: _Optional[str] = ..., deleted: bool = ..., is_active: bool = ...) -> None: ...
