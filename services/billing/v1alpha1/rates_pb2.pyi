from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.entities.v1alpha1 import rates_pb2 as _rates_pb2
from services.billing.v1alpha1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id", "rate_definition")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class CreateDefaultRateDefinitionResponse(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class CreateRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id", "rate_definition")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class CreateRateDefinitionResponse(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteDefaultRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class DeleteRateDefinitionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id",)
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ...) -> None: ...

class GetRateDefinitionResponse(_message.Message):
    __slots__ = ("rate_definition",)
    RATE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    rate_definition: _rates_pb2.RateDefinition
    def __init__(self, rate_definition: _Optional[_Union[_rates_pb2.RateDefinition, _Mapping]] = ...) -> None: ...

class ListRateDefinitionsRequest(_message.Message):
    __slots__ = ("rate_definition_id", "filter", "fields", "sort", "page")
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
    __slots__ = ("rate_definitions", "token")
    RATE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    rate_definitions: _containers.RepeatedCompositeFieldContainer[_rates_pb2.RateDefinition]
    token: str
    def __init__(self, rate_definitions: _Optional[_Iterable[_Union[_rates_pb2.RateDefinition, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateDefaultRateDefinitionRequest(_message.Message):
    __slots__ = ("rate_definition_id", "rate_definition", "update_fields")
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
    __slots__ = ("rate_definition_id", "rate_definition", "update_fields")
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
