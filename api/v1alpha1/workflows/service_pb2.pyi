from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersistedFlowDefinition(_message.Message):
    __slots__ = ["flow_definition_id", "org_id", "application", "name", "description", "definition", "create_time", "update_time", "extra"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    org_id: str
    application: str
    name: str
    description: str
    definition: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    extra: str
    def __init__(self, flow_definition_id: _Optional[str] = ..., org_id: _Optional[str] = ..., application: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., definition: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., extra: _Optional[str] = ...) -> None: ...

class CreateFlowDefinitionRequest(_message.Message):
    __slots__ = ["definition"]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    definition: PersistedFlowDefinition
    def __init__(self, definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class CreateFlowDefinitionResponse(_message.Message):
    __slots__ = ["flow_definition_id"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    def __init__(self, flow_definition_id: _Optional[str] = ...) -> None: ...

class GetFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition_id"]
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    def __init__(self, flow_definition_id: _Optional[str] = ...) -> None: ...

class GetFlowDefinitionResponse(_message.Message):
    __slots__ = ["definition"]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    definition: PersistedFlowDefinition
    def __init__(self, definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class ListFlowDefinitionsRequest(_message.Message):
    __slots__ = ["org_id", "application"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    application: str
    def __init__(self, org_id: _Optional[str] = ..., application: _Optional[str] = ...) -> None: ...

class ListFlowDefinitionsResponse(_message.Message):
    __slots__ = ["flow_definition"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition: PersistedFlowDefinition
    def __init__(self, flow_definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class UpdateFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition: PersistedFlowDefinition
    def __init__(self, flow_definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class UpdateFlowDefinitionResponse(_message.Message):
    __slots__ = ["flow_definition"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition: PersistedFlowDefinition
    def __init__(self, flow_definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class ValidateFlowDefinitionRequest(_message.Message):
    __slots__ = ["flow_definition"]
    FLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    flow_definition: PersistedFlowDefinition
    def __init__(self, flow_definition: _Optional[_Union[PersistedFlowDefinition, _Mapping]] = ...) -> None: ...

class ValidateFlowDefinitionResponse(_message.Message):
    __slots__ = ["valid", "error"]
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    error: str
    def __init__(self, valid: bool = ..., error: _Optional[str] = ...) -> None: ...
