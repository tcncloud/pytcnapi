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
    __slots__ = ("contact_list", "contact_manager_list")
    CONTACT_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_LIST_FIELD_NUMBER: _ClassVar[int]
    contact_list: _containers.RepeatedCompositeFieldContainer[_contactmanager_pb2.ContactManagerList]
    contact_manager_list: _containers.RepeatedCompositeFieldContainer[ContactManagerList]
    def __init__(self, contact_list: _Optional[_Iterable[_Union[_contactmanager_pb2.ContactManagerList, _Mapping]]] = ..., contact_manager_list: _Optional[_Iterable[_Union[ContactManagerList, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("contact_entry", "contact_manager_entry")
    CONTACT_ENTRY_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_entry: _containers.RepeatedCompositeFieldContainer[_contactmanager_pb2.ContactManagerEntry]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_entry: _Optional[_Iterable[_Union[_contactmanager_pb2.ContactManagerEntry, _Mapping]]] = ..., contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetEncContactEntryRequest(_message.Message):
    __slots__ = ("contact_manager_entry_id",)
    CONTACT_MANAGER_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    contact_manager_entry_id: int
    def __init__(self, contact_manager_entry_id: _Optional[int] = ...) -> None: ...

class GetEncContactEntryResponse(_message.Message):
    __slots__ = ("contact_entry", "contact_manager_entry")
    CONTACT_ENTRY_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_ENTRY_FIELD_NUMBER: _ClassVar[int]
    contact_entry: _containers.RepeatedCompositeFieldContainer[_contactmanager_pb2.ContactManagerEntry]
    contact_manager_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, contact_entry: _Optional[_Iterable[_Union[_contactmanager_pb2.ContactManagerEntry, _Mapping]]] = ..., contact_manager_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetKYCEncContactEntryRequest(_message.Message):
    __slots__ = ("project_id", "entry_val", "min_kyc_limit", "kyc_response")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_VAL_FIELD_NUMBER: _ClassVar[int]
    MIN_KYC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    KYC_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    entry_val: _containers.RepeatedCompositeFieldContainer[_contactmanager_pb2.ContactManagerEntryVal]
    min_kyc_limit: int
    kyc_response: _containers.RepeatedCompositeFieldContainer[ContactManagerEntryVal]
    def __init__(self, project_id: _Optional[int] = ..., entry_val: _Optional[_Iterable[_Union[_contactmanager_pb2.ContactManagerEntryVal, _Mapping]]] = ..., min_kyc_limit: _Optional[int] = ..., kyc_response: _Optional[_Iterable[_Union[ContactManagerEntryVal, _Mapping]]] = ...) -> None: ...

class GetKYCEncContactEntryResponse(_message.Message):
    __slots__ = ("verified", "contact_entry")
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ENTRY_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    contact_entry: _containers.RepeatedCompositeFieldContainer[ContactManagerEntry]
    def __init__(self, verified: bool = ..., contact_entry: _Optional[_Iterable[_Union[ContactManagerEntry, _Mapping]]] = ...) -> None: ...

class GetKYCKeysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetKYCKeysResponse(_message.Message):
    __slots__ = ("entry_type", "kyc_limit")
    ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KYC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    entry_type: _containers.RepeatedScalarFieldContainer[str]
    kyc_limit: int
    def __init__(self, entry_type: _Optional[_Iterable[str]] = ..., kyc_limit: _Optional[int] = ...) -> None: ...

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
