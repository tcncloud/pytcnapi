from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentCallLog(_message.Message):
    __slots__ = ["actions"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ["call_skills_initial", "call_ended"]
    CALL_SKILLS_INITIAL_FIELD_NUMBER: _ClassVar[int]
    CALL_ENDED_FIELD_NUMBER: _ClassVar[int]
    call_skills_initial: CallSkillsInitial
    call_ended: str
    def __init__(self, call_skills_initial: _Optional[_Union[CallSkillsInitial, _Mapping]] = ..., call_ended: _Optional[str] = ...) -> None: ...

class CallSkillsInitial(_message.Message):
    __slots__ = ["need", "want"]
    NEED_FIELD_NUMBER: _ClassVar[int]
    WANT_FIELD_NUMBER: _ClassVar[int]
    need: _containers.RepeatedScalarFieldContainer[str]
    want: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, need: _Optional[_Iterable[str]] = ..., want: _Optional[_Iterable[str]] = ...) -> None: ...
