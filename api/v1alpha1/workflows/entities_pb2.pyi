from api.commons.workflows import entities_pb2 as _entities_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFlowDefinitionsRequest(_message.Message):
    __slots__ = ["filter"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    def __init__(self, filter: _Optional[str] = ...) -> None: ...

class ListFlowDefinitionsResponse(_message.Message):
    __slots__ = ["flow_definitions"]
    FLOW_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    flow_definitions: _containers.RepeatedCompositeFieldContainer[_entities_pb2.FlowDefinition]
    def __init__(self, flow_definitions: _Optional[_Iterable[_Union[_entities_pb2.FlowDefinition, _Mapping]]] = ...) -> None: ...

class SaveFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition", "update_mask"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    flow_definition: _entities_pb2.FlowDefinition
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, flow_definition: _Optional[_Union[_entities_pb2.FlowDefinition, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SaveFlowDefinitionResponse(_message.Message):
    __slots__ = ["flow_definition_id", "flow_definition"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    flow_definition: _entities_pb2.FlowDefinition
    def __init__(self, flow_definition_id: _Optional[str] = ..., flow_definition: _Optional[_Union[_entities_pb2.FlowDefinition, _Mapping]] = ...) -> None: ...

class GetFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition_id"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    def __init__(self, flow_definition_id: _Optional[str] = ...) -> None: ...

class GetFlowDefinitionResponse(_message.Message):
    __slots__ = ["flow_definition"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition: _entities_pb2.FlowDefinition
    def __init__(self, flow_definition: _Optional[_Union[_entities_pb2.FlowDefinition, _Mapping]] = ...) -> None: ...

class DeleteFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition_id"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    def __init__(self, flow_definition_id: _Optional[str] = ...) -> None: ...

class DeleteFlowDefinitionResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...
