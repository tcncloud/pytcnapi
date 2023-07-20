from api.commons import country_pb2 as _country_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons.org import organization_pb2 as _organization_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrganizationRequest(_message.Message):
    __slots__ = ["name", "crm_id", "time_zone", "is_manual_only_account", "backoffice_theme", "allowed_countries", "p3_parent_account"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRM_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_ONLY_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKOFFICE_THEME_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    P3_PARENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    crm_id: str
    time_zone: _org_pb2.TimeZone
    is_manual_only_account: bool
    backoffice_theme: _org_pb2.ClientSkin
    allowed_countries: _containers.RepeatedScalarFieldContainer[_country_pb2.Country]
    p3_parent_account: str
    def __init__(self, name: _Optional[str] = ..., crm_id: _Optional[str] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., is_manual_only_account: bool = ..., backoffice_theme: _Optional[_Union[_org_pb2.ClientSkin, str]] = ..., allowed_countries: _Optional[_Iterable[_Union[_country_pb2.Country, str]]] = ..., p3_parent_account: _Optional[str] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ["organization"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    def __init__(self, organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ...) -> None: ...

class GetOrganizationByIdRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetOrganizationByIdResponse(_message.Message):
    __slots__ = ["organization"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    def __init__(self, organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ...) -> None: ...

class ListOrganizationsRequest(_message.Message):
    __slots__ = ["region_id", "archived"]
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    archived: bool
    def __init__(self, region_id: _Optional[str] = ..., archived: bool = ..., **kwargs) -> None: ...

class ListOrganizationsResponse(_message.Message):
    __slots__ = ["organization_details"]
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization_details: _containers.RepeatedCompositeFieldContainer[OrganizationDetails]
    def __init__(self, organization_details: _Optional[_Iterable[_Union[OrganizationDetails, _Mapping]]] = ...) -> None: ...

class OrganizationDetails(_message.Message):
    __slots__ = ["organization", "last_scheduled_date"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    last_scheduled_date: _timestamp_pb2.Timestamp
    def __init__(self, organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConvertOrgToManualRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ConvertOrgToManualResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOwnedOrgsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOwnedOrgsResponse(_message.Message):
    __slots__ = ["organization_details"]
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization_details: _containers.RepeatedCompositeFieldContainer[OrganizationDetails]
    def __init__(self, organization_details: _Optional[_Iterable[_Union[OrganizationDetails, _Mapping]]] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ["org_id", "time_zone", "billing_id", "name", "p3_owner_id", "archived", "field_mask"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    BILLING_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    P3_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    time_zone: _org_pb2.TimeZone
    billing_id: str
    name: str
    p3_owner_id: str
    archived: bool
    field_mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., time_zone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., billing_id: _Optional[str] = ..., name: _Optional[str] = ..., p3_owner_id: _Optional[str] = ..., archived: bool = ..., field_mask: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ["organization"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    def __init__(self, organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ...) -> None: ...

class ArchiveOrganizationRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class ArchiveOrganizationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnArchiveOrganizationRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class UnArchiveOrganizationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAllOrganizationsGloballyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAllOrganizationsGloballyResponse(_message.Message):
    __slots__ = ["organization_details"]
    class OrganizationDetails(_message.Message):
        __slots__ = ["org_id", "name", "client_sid", "billing_id", "region_id", "add_date", "last_scheduled_date", "archived"]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
        BILLING_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        ADD_DATE_FIELD_NUMBER: _ClassVar[int]
        LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
        ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        org_id: str
        name: str
        client_sid: int
        billing_id: str
        region_id: str
        add_date: _timestamp_pb2.Timestamp
        last_scheduled_date: _timestamp_pb2.Timestamp
        archived: bool
        def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., client_sid: _Optional[int] = ..., billing_id: _Optional[str] = ..., region_id: _Optional[str] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., archived: bool = ...) -> None: ...
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization_details: _containers.RepeatedCompositeFieldContainer[ListAllOrganizationsGloballyResponse.OrganizationDetails]
    def __init__(self, organization_details: _Optional[_Iterable[_Union[ListAllOrganizationsGloballyResponse.OrganizationDetails, _Mapping]]] = ...) -> None: ...

class ListOrganizationsByRegionRequest(_message.Message):
    __slots__ = ["region_id"]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    def __init__(self, region_id: _Optional[str] = ...) -> None: ...

class ListOrganizationsByRegionResponse(_message.Message):
    __slots__ = ["organization_details"]
    class OrganizationDetails(_message.Message):
        __slots__ = ["org_id", "name", "client_sid", "billing_id", "region_id", "add_date", "last_scheduled_date"]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
        BILLING_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        ADD_DATE_FIELD_NUMBER: _ClassVar[int]
        LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
        org_id: str
        name: str
        client_sid: int
        billing_id: str
        region_id: str
        add_date: _timestamp_pb2.Timestamp
        last_scheduled_date: _timestamp_pb2.Timestamp
        def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., client_sid: _Optional[int] = ..., billing_id: _Optional[str] = ..., region_id: _Optional[str] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization_details: _containers.RepeatedCompositeFieldContainer[ListOrganizationsByRegionResponse.OrganizationDetails]
    def __init__(self, organization_details: _Optional[_Iterable[_Union[ListOrganizationsByRegionResponse.OrganizationDetails, _Mapping]]] = ...) -> None: ...

class ListArchivedOrganizationsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListArchivedOrganizationsResponse(_message.Message):
    __slots__ = ["organization_details"]
    class OrganizationDetails(_message.Message):
        __slots__ = ["org_id", "name", "billing_id", "add_date", "last_scheduled_date"]
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BILLING_ID_FIELD_NUMBER: _ClassVar[int]
        ADD_DATE_FIELD_NUMBER: _ClassVar[int]
        LAST_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
        org_id: str
        name: str
        billing_id: str
        add_date: _timestamp_pb2.Timestamp
        last_scheduled_date: _timestamp_pb2.Timestamp
        def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., billing_id: _Optional[str] = ..., add_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization_details: _containers.RepeatedCompositeFieldContainer[ListArchivedOrganizationsResponse.OrganizationDetails]
    def __init__(self, organization_details: _Optional[_Iterable[_Union[ListArchivedOrganizationsResponse.OrganizationDetails, _Mapping]]] = ...) -> None: ...
