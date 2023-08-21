from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OmniNodePrompt(_message.Message):
    __slots__ = ["prompt", "store_to", "options"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    STORE_TO_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    store_to: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, prompt: _Optional[str] = ..., store_to: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class OmniNodeSendMessage(_message.Message):
    __slots__ = ["prompt", "options"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, prompt: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class OmniNodeUserInput(_message.Message):
    __slots__ = ["store_id"]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class OmniNodeBranching(_message.Message):
    __slots__ = ["store_id", "options"]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_id: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class OmniNodeSetSkill(_message.Message):
    __slots__ = ["skill", "skills"]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skill: str
    skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, skill: _Optional[str] = ..., skills: _Optional[_Iterable[str]] = ...) -> None: ...

class OmniNodeToAgent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OmniNodeToMatcher(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OmniNodeError(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...
