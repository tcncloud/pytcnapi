from annotations import authz_pb2 as _authz_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersistedWorkflowDefinition(_message.Message):
    __slots__ = ("flow_definition_id", "org_id", "application", "name", "labels", "description", "definition", "create_time", "update_time", "extra")
    FLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    flow_definition_id: str
    org_id: str
    application: str
    name: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    description: str
    definition: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    extra: str
    def __init__(self, flow_definition_id: _Optional[str] = ..., org_id: _Optional[str] = ..., application: _Optional[str] = ..., name: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., definition: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., extra: _Optional[str] = ...) -> None: ...

class CreateWorkflowDefinitionRequest(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class CreateWorkflowDefinitionResponse(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class GetWorkflowDefinitionRequest(_message.Message):
    __slots__ = ("workflow_definition_id",)
    WORKFLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_definition_id: str
    def __init__(self, workflow_definition_id: _Optional[str] = ...) -> None: ...

class GetWorkflowDefinitionResponse(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class ListWorkflowDefinitionsRequest(_message.Message):
    __slots__ = ("org_id", "application", "labels")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    application: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., application: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...

class ListWorkflowDefinitionsResponse(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class UpdateWorkflowDefinitionRequest(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class UpdateWorkflowDefinitionResponse(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class DeleteWorkflowDefinitionRequest(_message.Message):
    __slots__ = ("workflow_definition_id",)
    WORKFLOW_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_definition_id: str
    def __init__(self, workflow_definition_id: _Optional[str] = ...) -> None: ...

class DeleteWorkflowDefinitionResponse(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class ValidateWorkflowDefinitionRequest(_message.Message):
    __slots__ = ("workflow_definition",)
    WORKFLOW_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    workflow_definition: PersistedWorkflowDefinition
    def __init__(self, workflow_definition: _Optional[_Union[PersistedWorkflowDefinition, _Mapping]] = ...) -> None: ...

class ValidateWorkflowDefinitionResponse(_message.Message):
    __slots__ = ("valid", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    error: str
    def __init__(self, valid: bool = ..., error: _Optional[str] = ...) -> None: ...
