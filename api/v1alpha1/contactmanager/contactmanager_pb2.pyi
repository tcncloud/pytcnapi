from api.commons.audit import audit_pb2 as _audit_pb2
from api.commons import classifier_pb2 as _classifier_pb2
from api.commons import contactmanager_pb2 as _contactmanager_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    __slots__ = ("contact_manager_list_id", "org_id", "project_id", "page_size", "page_token")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    org_id: str
    project_id: str
    page_size: int
    page_token: str
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListContactEntryListResponse(_message.Message):
    __slots__ = ("contact_manager_entry", "next_page_token", "cm_entry")
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CM_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    next_page_token: str
    cm_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., cm_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("contact_manager_entry_id", "contact_manager_entry_list_id", "key", "value", "type", "date_created", "status", "date_modified", "ttl", "file_name", "field", "expiry_date")
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    contact_manager_entry_list_id: int
    key: str
    value: str
    type: str
    date_created: _timestamp_pb2.Timestamp
    status: _contactmanager_pb2.ContactEntryStatus
    date_modified: _timestamp_pb2.Timestamp
    ttl: int
    file_name: _containers.RepeatedScalarFieldContainer[str]
    field: _containers.RepeatedCompositeFieldContainer[ContactField]
    expiry_date: _timestamp_pb2.Timestamp
    def __init__(self, contact_manager_entry_id: _Optional[int] = ..., contact_manager_entry_list_id: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_contactmanager_pb2.ContactEntryStatus, str]] = ..., date_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttl: _Optional[int] = ..., file_name: _Optional[_Iterable[str]] = ..., field: _Optional[_Iterable[_Union[ContactField, _Mapping]]] = ..., expiry_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ContactManagerList(_message.Message):
    __slots__ = ("contact_manager_list_id", "org_id", "project_id", "file_name", "description", "list_details", "ttl", "date_created", "is_deleted", "status", "contact_manager_list_name")
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
    CONTACT_MANAGER_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
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
    contact_manager_list_name: str
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., org_id: _Optional[str] = ..., project_id: _Optional[int] = ..., file_name: _Optional[str] = ..., description: _Optional[str] = ..., list_details: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_deleted: bool = ..., status: _Optional[_Union[_contactmanager_pb2.ContactListStatus, str]] = ..., contact_manager_list_name: _Optional[str] = ...) -> None: ...

class ContactManagerEntryVal(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class AddContactEntryRequest(_message.Message):
    __slots__ = ("contact_manager_list_id", "entry", "project_sid", "field")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    entry: _containers.RepeatedCompositeFieldContainer[Entry]
    project_sid: int
    field: _containers.RepeatedCompositeFieldContainer[ContactField]
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., entry: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ..., project_sid: _Optional[int] = ..., field: _Optional[_Iterable[_Union[ContactField, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("contact_manager_list_id", "contact_manager_entry_id", "edited_entry", "field")
    CONTACT_MANAGER_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_ENTRY_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    contact_manager_list_id: int
    contact_manager_entry_id: int
    edited_entry: _containers.RepeatedCompositeFieldContainer[EditedEntry]
    field: _containers.RepeatedCompositeFieldContainer[ContactField]
    def __init__(self, contact_manager_list_id: _Optional[int] = ..., contact_manager_entry_id: _Optional[int] = ..., edited_entry: _Optional[_Iterable[_Union[EditedEntry, _Mapping]]] = ..., field: _Optional[_Iterable[_Union[ContactField, _Mapping]]] = ...) -> None: ...

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

class ContactField(_message.Message):
    __slots__ = ("name", "value", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    type: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class EditContactEntryResponse(_message.Message):
    __slots__ = ("field",)
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: _containers.RepeatedCompositeFieldContainer[ContactField]
    def __init__(self, field: _Optional[_Iterable[_Union[ContactField, _Mapping]]] = ...) -> None: ...

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

class ListContactActivityLogRequest(_message.Message):
    __slots__ = ("org_id", "project_id", "contact_manager_entry_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    project_id: str
    contact_manager_entry_id: int
    def __init__(self, org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., contact_manager_entry_id: _Optional[int] = ...) -> None: ...

class ListContactActivityLogResponse(_message.Message):
    __slots__ = ("contact_activity_log",)
    CONTACT_ACTIVITY_LOG_FIELD_NUMBER: _ClassVar[int]
    contact_activity_log: _containers.RepeatedCompositeFieldContainer[ContactActivityLog]
    def __init__(self, contact_activity_log: _Optional[_Iterable[_Union[ContactActivityLog, _Mapping]]] = ...) -> None: ...

class ContactActivityLog(_message.Message):
    __slots__ = ("org_id", "project_id", "contact_manager_entry_id", "event_user", "event")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_USER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    project_id: str
    contact_manager_entry_id: int
    event_user: str
    event: _audit_pb2.AuditEvent
    def __init__(self, org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., contact_manager_entry_id: _Optional[int] = ..., event_user: _Optional[str] = ..., event: _Optional[_Union[_audit_pb2.AuditEvent, _Mapping]] = ...) -> None: ...
