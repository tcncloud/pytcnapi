from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.org.exile_certificate_manager.v1alpha1 import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateExileConfigurationRequest(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: _entities_pb2.ExileConfigurationType
    parameters: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[_entities_pb2.ExileConfigurationType, str]] = ..., parameters: _Optional[str] = ...) -> None: ...

class CreateExileConfigurationResponse(_message.Message):
    __slots__ = ()
    EXILE_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXILE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    exile_configuration_id: str
    exile_configuration: _entities_pb2.ExileConfiguration
    def __init__(self, exile_configuration_id: _Optional[str] = ..., exile_configuration: _Optional[_Union[_entities_pb2.ExileConfiguration, _Mapping]] = ...) -> None: ...

class UpdateExileConfigurationRequest(_message.Message):
    __slots__ = ()
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    configuration: _entities_pb2.ExileConfiguration
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, configuration: _Optional[_Union[_entities_pb2.ExileConfiguration, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateExileConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteExileConfigurationRequest(_message.Message):
    __slots__ = ()
    EXILE_CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    exile_configuration_id: str
    def __init__(self, exile_configuration_id: _Optional[str] = ...) -> None: ...

class DeleteExileConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListExileConfigurationsRequest(_message.Message):
    __slots__ = ()
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListExileConfigurationsResponse(_message.Message):
    __slots__ = ()
    EXILE_CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    exile_configurations: _containers.RepeatedCompositeFieldContainer[_entities_pb2.ExileConfiguration]
    def __init__(self, exile_configurations: _Optional[_Iterable[_Union[_entities_pb2.ExileConfiguration, _Mapping]]] = ...) -> None: ...
