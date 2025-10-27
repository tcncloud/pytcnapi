import datetime

from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha2 import rates_pb2 as _rates_pb2
from services.billing.v1alpha2 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class CreateDefaultRateDefinitionResponse(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class CreateDefaultRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[CreateDefaultRateDefinitionRequest]
    def __init__(self, rates: _Optional[_Iterable[_Union[CreateDefaultRateDefinitionRequest, _Mapping]]] = ...) -> None: ...

class CreateDefaultRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[CreateDefaultRateDefinitionResponse]
    def __init__(self, rates: _Optional[_Iterable[_Union[CreateDefaultRateDefinitionResponse, _Mapping]]] = ...) -> None: ...

class CreateRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    default_rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., default_rate_definition_id: _Optional[str] = ...) -> None: ...

class CreateRateDefinitionResponse(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class CreateRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[CreateRateDefinitionRequest]
    def __init__(self, rates: _Optional[_Iterable[_Union[CreateRateDefinitionRequest, _Mapping]]] = ...) -> None: ...

class CreateRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[CreateRateDefinitionResponse]
    def __init__(self, rates: _Optional[_Iterable[_Union[CreateRateDefinitionResponse, _Mapping]]] = ...) -> None: ...

class DeleteDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteDefaultRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDefaultRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    rate_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rate_definition_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteDefaultRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_IDS_FIELD_NUMBER: _ClassVar[int]
    rate_definition_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rate_definition_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class GetRateDefinitionResponse(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class GetRateHistoryRequest(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, org_id: _Optional[str] = ..., group_ids: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetRateHistoryResponse(_message.Message):
    __slots__ = ()
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateSnapshot]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[_rates_pb2.RateSnapshot, _Mapping]]] = ...) -> None: ...

class ListActiveRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, rate_definition_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListActiveRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    RATE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    rate_definitions: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    token: str
    def __init__(self, rate_definitions: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class ListRateDefinitionsRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, rate_definition_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListRateDefinitionsResponse(_message.Message):
    __slots__ = ()
    RATE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    rate_definitions: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    token: str
    def __init__(self, rate_definitions: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDefaultRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateRateDefinitionRequest(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    update_fields: _field_mask_pb2.FieldMask
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ..., update_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
