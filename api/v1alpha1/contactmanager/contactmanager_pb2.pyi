from api.commons import classifier_pb2 as _classifier_pb2
from api.commons import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetContactListRequest(_message.Message):
    __slots__ = ("request_mask", "org_id", "project_id")
    REQUEST_MASK_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    request_mask: _field_mask_pb2.FieldMask
    org_id: str
    project_id: int
    def __init__(self, request_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., org_id: _Optional[str] = ..., project_id: _Optional[int] = ...) -> None: ...

class GetContactListResponse(_message.Message):
    __slots__ = ("contact_manager_list",)
    CONTACT_MANAGER_LIST_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list: _containers.RepeatedCompositeFieldContainer[ContactManagerList]
    def __init__(self, contact_manager_list: _Optional[_Iterable[_Union[ContactManagerList, _Mapping]]] = ...) -> None: ...

class ListContactEntryListRequest(_message.Message):
    __slots__ = ("contact_manager_list_id", "org_id", "project_id")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    org_id: str
    project_id: str
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class ListContactEntryListResponse(_message.Message):
    __slots__ = ("contact_manager_entry",)
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetEncContactEntryRequest(_message.Message):
    __slots__ = ("contact_manager_entry_id",)
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    def __init__(self, contact_manager_entry_id: _Optional[int] = ...) -> None: ...

class GetEncContactEntryResponse(_message.Message):
    __slots__ = ("contact_manager_entry",)
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetKYCEncContactEntryRequest(_message.Message):
    __slots__ = ("project_id", "kyc_response")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    KYC_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    kyc_response: _containers.RepeatedCompositeFieldContainer[ContactManagerEntryVal]
    def __init__(self, project_id: _Optional[int] = ..., kyc_response: _Optional[_Iterable[_Union[ContactManagerEntryVal, _Mapping]]] = ...) -> None: ...

class GetKYCEncContactEntryResponse(_message.Message):
    __slots__ = ("verified", "contact_entry")
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRY_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    contact_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, verified: bool = ..., contact_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetKYCKeysRequest(_message.Message):
    __slots__ = ("project_sid",)
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    project_sid: int
    def __init__(self, project_sid: _Optional[int] = ...) -> None: ...

class GetKYCKeysResponse(_message.Message):
    __slots__ = ("entry_type",)
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    entry_type: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entry_type: _Optional[_Iterable[str]] = ...) -> None: ...

class ContactManagerEntry(_message.Message):
    __slots__ = ("contact_manager_entry_id", "contact_manager_entry_list_id", "key", "value", "type", "date_created", "status")
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    contact_manager_entry_list_id: int
    key: str
    value: str
    type: str
    date_created: _timestamp_pb2.Timestamp
    status: _contactmanager_pb2.ContactEntryStatus
    def __init__(self, contact_manager_entry_id: _Optional[int] = ..., contact_manager_entry_list_id: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_contactmanager_pb2.ContactEntryStatus, str]] = ...) -> None: ...

class ContactManagerList(_message.Message):
    __slots__ = ("contact_manager_list_id", "org_id", "project_id", "file_name", "description", "list_details", "ttl", "date_created", "is_deleted", "status")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LIST_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    org_id: str
    project_id: int
    file_name: str
    description: str
    list_details: _containers.RepeatedScalarFieldContainer[str]
    ttl: int
    date_created: _timestamp_pb2.Timestamp
    is_deleted: bool
    status: _contactmanager_pb2.ContactListStatus
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_id: _Optional[int] = ..., file_name: _Optional[str] = ..., description: _Optional[str] = ..., list_details: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., status: _Optional[_Union[_contactmanager_pb2.ContactListStatus, str]] = ...) -> None: ...

class ContactManagerEntryVal(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class AddContactEntryRequest(_message.Message):
    __slots__ = ("contact_manager_list_id", "entry")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    entry: _containers.RepeatedCompositeFieldContainer[Entry]
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., entry: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ("name", "value", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    type: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class AddContactEntryResponse(_message.Message):
    __slots__ = ("contact_id",)
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    contact_id: int
    def __init__(self, contact_id: _Optional[int] = ...) -> None: ...

class EditContactEntryRequest(_message.Message):
    __slots__ = ("contact_manager_list_id", "contact_manager_entry_id", "edited_entry")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    contact_manager_entry_id: int
    edited_entry: _containers.RepeatedCompositeFieldContainer[EditedEntry]
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., contact_manager_entry_id: _Optional[int] = ..., edited_entry: _Optional[_Iterable[_Union[EditedEntry, _Mapping]]] = ...) -> None: ...

class EditedEntry(_message.Message):
    __slots__ = ("contact_manager_entry_list_id", "name", "value", "type")
    CONTACT_MANAGER_ENTRY_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_list_id: int
    name: str
    value: str
    type: str
    def __init__(self, contact_manager_entry_list_id: _Optional[int] = ..., name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class EditContactEntryResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListContactsByEntityRequest(_message.Message):
    __slots__ = ("project_id", "entity_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    entity_id: str
    def __init__(self, project_id: _Optional[int] = ..., entity_id: _Optional[str] = ...) -> None: ...

class ListContactsByEntityResponse(_message.Message):
    __slots__ = ("contact_manager_entry",)
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetContactFieldTypeRequest(_message.Message):
    __slots__ = ("field_name", "field_value", "field_type")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    field_value: str
    field_type: _classifier_pb2.ClassifierEntityType
    def __init__(self, field_name: _Optional[str] = ..., field_value: _Optional[str] = ..., field_type: _Optional[_Union[_classifier_pb2.ClassifierEntityType, str]] = ...) -> None: ...

class GetContactFieldTypeResponse(_message.Message):
    __slots__ = ("field_type",)
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_type: _classifier_pb2.ClassifierEntityType
    def __init__(self, field_type: _Optional[_Union[_classifier_pb2.ClassifierEntityType, str]] = ...) -> None: ...
