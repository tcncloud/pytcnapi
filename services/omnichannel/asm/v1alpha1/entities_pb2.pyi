from api.commons import event_pb2 as _event_pb2
from services.omnichannel.asm.entities.v1alpha1 import session_pb2 as _session_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ()
    ASM_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session: _session_pb2.AsmSession
    def __init__(self, asm_session: _Optional[_Union[_session_pb2.AsmSession, _Mapping]] = ...) -> None: ...

class EndSessionRequest(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    reason: str
    def __init__(self, asm_session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class EndSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionResponse(_message.Message):
    __slots__ = ()
    ASM_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session: _session_pb2.AsmSession
    def __init__(self, asm_session: _Optional[_Union[_session_pb2.AsmSession, _Mapping]] = ...) -> None: ...

class EnableVoiceRequest(_message.Message):
    __slots__ = ()
    class SkillsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    hunt_group_sid: int
    skills: _containers.ScalarMap[str, int]
    def __init__(self, asm_session_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EnableVoiceResponse(_message.Message):
    __slots__ = ()
    VOICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    VOICE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    voice_session: _session_pb2.VoiceSession
    voice_registration: _session_pb2.VoiceRegistration
    def __init__(self, voice_session: _Optional[_Union[_session_pb2.VoiceSession, _Mapping]] = ..., voice_registration: _Optional[_Union[_session_pb2.VoiceRegistration, _Mapping]] = ...) -> None: ...

class DisableVoiceRequest(_message.Message):
    __slots__ = ()
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    def __init__(self, asm_session_sid: _Optional[int] = ...) -> None: ...

class DisableVoiceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAsmUserDetailsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAsmUserDetailsResponse(_message.Message):
    __slots__ = ()
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ASM_USER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.AsmUserDetails]
    asm_user_details: _containers.RepeatedCompositeFieldContainer[_session_pb2.AsmUserDetails]
    def __init__(self, sessions: _Optional[_Iterable[_Union[_session_pb2.AsmUserDetails, _Mapping]]] = ..., asm_user_details: _Optional[_Iterable[_Union[_session_pb2.AsmUserDetails, _Mapping]]] = ...) -> None: ...

class PushEventsRequest(_message.Message):
    __slots__ = ()
    AMS_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ASM_EVENTS_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ams_session_sid: int
    asm_events: _containers.RepeatedCompositeFieldContainer[_event_pb2.AsmEvent]
    asm_session_sid: int
    def __init__(self, ams_session_sid: _Optional[int] = ..., asm_events: _Optional[_Iterable[_Union[_event_pb2.AsmEvent, _Mapping]]] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class PushEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
