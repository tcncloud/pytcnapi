from api.commons import org_pb2 as _org_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ["org_id", "enabled_regions", "region_id", "billing_id", "client_sid", "name", "add_date", "is_manual_only_account", "backoffice_theme", "archived", "crm_id", "time_zone", "callbacks_service_id", "p3_owner_id"]
    class EnabledRegionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_ONLY_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKOFFICE_THEME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CRM_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CALLBACKS_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    P3_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    enabled_regions: _containers.ScalarMap[str, int]
    region_id: str
    billing_id: str
    client_sid: int
    name: str
    add_date: _timestamp_pb2.Timestamp
    is_manual_only_account: bool
    backoffice_theme: _org_pb2.ClientSkin
    archived: bool
    crm_id: str
    time_zone: _org_pb2.TimeZone
    callbacks_service_id: str
    p3_owner_id: str
    def __init__(self, org_id: _Optional[str] = ..., enabled_regions: _Optional[_Mapping[str, int]] = ..., region_id: _Optional[str] = ..., billing_id: _Optional[str] = ..., client_sid: _Optional[int] = ..., name: _Optional[str] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_manual_only_account: bool = ..., backoffice_theme: _Optional[_Union[_org_pb2.ClientSkin, str]] = ..., archived: bool = ..., crm_id: _Optional[str] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., callbacks_service_id: _Optional[str] = ..., p3_owner_id: _Optional[str] = ...) -> None: ...

class OrganizationDetails(_message.Message):
    __slots__ = ["organization", "last_scheduled_date"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    last_scheduled_date: _timestamp_pb2.Timestamp
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
