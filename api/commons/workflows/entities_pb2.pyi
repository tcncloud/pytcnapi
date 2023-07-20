from api.commons.workflows import nodes_pb2 as _nodes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlowDefinition(_message.Message):
    __slots__ = ["id", "name", "description", "entry_node_id", "org_id", "nodes", "error_node_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    ERROR_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    entry_node_id: str
    org_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[_nodes_pb2.NodeDefinition]
    error_node_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., entry_node_id: _Optional[str] = ..., org_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[_nodes_pb2.NodeDefinition, _Mapping]]] = ..., error_node_id: _Optional[str] = ...) -> None: ...

class FlowState(_message.Message):
    __slots__ = ["envelope", "state", "payload"]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    envelope: Envelope
    state: State
    payload: Payload
    def __init__(self, envelope: _Optional[_Union[Envelope, _Mapping]] = ..., state: _Optional[_Union[State, _Mapping]] = ..., payload: _Optional[_Union[Payload, _Mapping]] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ["id", "org_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ["flow_done", "flow_id", "current_node", "error"]
    FLOW_DONE_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    flow_done: bool
    flow_id: str
    current_node: str
    error: str
    def __init__(self, flow_done: bool = ..., flow_id: _Optional[str] = ..., current_node: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ["data", "error"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: str
    error: str
    def __init__(self, data: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
