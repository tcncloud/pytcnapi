from api.commons.org import agent_profile_group_pb2 as _agent_profile_group_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAgentProfileGroupRequest(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class GetAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class UpdateAgentProfileGroupRequest(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class UpdateAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentProfileGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAgentProfileGroupsResponse(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    agent_profile_groups: _containers.RepeatedCompositeFieldContainer[_agent_profile_group_pb2.AgentProfileGroup]
    def __init__(self, agent_profile_groups: _Optional[_Iterable[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]]] = ...) -> None: ...

class CreateAgentProfileGroupRequest(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group: _agent_profile_group_pb2.AgentProfileGroup
    def __init__(self, agent_profile_group: _Optional[_Union[_agent_profile_group_pb2.AgentProfileGroup, _Mapping]] = ...) -> None: ...

class CreateAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class DeleteAgentProfileGroupRequest(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    def __init__(self, agent_profile_group_id: _Optional[str] = ...) -> None: ...

class DeleteAgentProfileGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignAgentProfileGroupsRequest(_message.Message):
    __slots__ = ()
    AGENT_PROFILE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    agent_profile_group_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_profile_group_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignAgentProfileGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
