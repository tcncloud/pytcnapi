from api.commons import acd_pb2 as _acd_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentCallLog(_message.Message):
    __slots__ = ("actions",)
    class Action(_message.Message):
        __slots__ = ("call_skills_initial", "call_ended")
        CALL_SKILLS_INITIAL_FIELD_NUMBER: _ClassVar[int]
        CALL_ENDED_FIELD_NUMBER: _ClassVar[int]
        call_skills_initial: AgentCallLog.CallSkillsInitial
        call_ended: str
        def __init__(self, call_skills_initial: _Optional[_Union[AgentCallLog.CallSkillsInitial, _Mapping]] = ..., call_ended: _Optional[str] = ...) -> None: ...
    class CallSkillsInitial(_message.Message):
        __slots__ = ("need", "want")
        NEED_FIELD_NUMBER: _ClassVar[int]
        WANT_FIELD_NUMBER: _ClassVar[int]
        need: _containers.RepeatedScalarFieldContainer[str]
        want: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, need: _Optional[_Iterable[str]] = ..., want: _Optional[_Iterable[str]] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[AgentCallLog.Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[AgentCallLog.Action, _Mapping]]] = ...) -> None: ...

class AgentCallLogQuery(_message.Message):
    __slots__ = ("call_skills_initial", "call_ended")
    class CallSkillsInitial(_message.Message):
        __slots__ = ("need", "want")
        class Need(_message.Message):
            __slots__ = ("values", "all")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            ALL_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]
            all: bool
            def __init__(self, values: _Optional[_Iterable[str]] = ..., all: bool = ...) -> None: ...
        class Want(_message.Message):
            __slots__ = ("values", "all")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            ALL_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]
            all: bool
            def __init__(self, values: _Optional[_Iterable[str]] = ..., all: bool = ...) -> None: ...
        NEED_FIELD_NUMBER: _ClassVar[int]
        WANT_FIELD_NUMBER: _ClassVar[int]
        need: AgentCallLogQuery.CallSkillsInitial.Need
        want: AgentCallLogQuery.CallSkillsInitial.Want
        def __init__(self, need: _Optional[_Union[AgentCallLogQuery.CallSkillsInitial.Need, _Mapping]] = ..., want: _Optional[_Union[AgentCallLogQuery.CallSkillsInitial.Want, _Mapping]] = ...) -> None: ...
    class CallEnded(_message.Message):
        __slots__ = ("reasons",)
        REASONS_FIELD_NUMBER: _ClassVar[int]
        reasons: _containers.RepeatedScalarFieldContainer[_acd_pb2.AgentCallLogCallEnded]
        def __init__(self, reasons: _Optional[_Iterable[_Union[_acd_pb2.AgentCallLogCallEnded, str]]] = ...) -> None: ...
    CALL_SKILLS_INITIAL_FIELD_NUMBER: _ClassVar[int]
    CALL_ENDED_FIELD_NUMBER: _ClassVar[int]
    call_skills_initial: AgentCallLogQuery.CallSkillsInitial
    call_ended: AgentCallLogQuery.CallEnded
    def __init__(self, call_skills_initial: _Optional[_Union[AgentCallLogQuery.CallSkillsInitial, _Mapping]] = ..., call_ended: _Optional[_Union[AgentCallLogQuery.CallEnded, _Mapping]] = ...) -> None: ...
