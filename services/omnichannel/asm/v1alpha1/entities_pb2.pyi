from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSessionRes(_message.Message):
    __slots__ = ("asm_session",)
    ASM_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session: AsmSession
    def __init__(self, asm_session: _Optional[_Union[AsmSession, _Mapping]] = ...) -> None: ...

class VoiceRegistration(_message.Message):
    __slots__ = ("username", "password", "dial_url", "pstn_phone", "default_time_zone", "expiration_timestamp")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DIAL_URL_FIELD_NUMBER: _ClassVar[int]
    PSTN_PHONE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    dial_url: str
    pstn_phone: str
    default_time_zone: str
    expiration_timestamp: int
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., dial_url: _Optional[str] = ..., pstn_phone: _Optional[str] = ..., default_time_zone: _Optional[str] = ..., expiration_timestamp: _Optional[int] = ...) -> None: ...

class VoiceSession(_message.Message):
    __slots__ = ("voice_session_sid", "voice_session_start", "voice_session_end")
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_START_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_END_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    voice_session_start: _timestamp_pb2.Timestamp
    voice_session_end: _timestamp_pb2.Timestamp
    def __init__(self, voice_session_sid: _Optional[int] = ..., voice_session_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., voice_session_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EndSessionReq(_message.Message):
    __slots__ = ("asm_session_sid", "reason")
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    reason: str
    def __init__(self, asm_session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class EndSessionRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentSessionRes(_message.Message):
    __slots__ = ("asm_session",)
    ASM_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session: AsmSession
    def __init__(self, asm_session: _Optional[_Union[AsmSession, _Mapping]] = ...) -> None: ...

class AsmSession(_message.Message):
    __slots__ = ("asm_session_sid", "asm_session_start", "asm_session_end", "voice_session")
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_START_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_END_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    asm_session_start: _timestamp_pb2.Timestamp
    asm_session_end: _timestamp_pb2.Timestamp
    voice_session: VoiceSession
    def __init__(self, asm_session_sid: _Optional[int] = ..., asm_session_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., asm_session_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., voice_session: _Optional[_Union[VoiceSession, _Mapping]] = ...) -> None: ...

class EnableVoiceReq(_message.Message):
    __slots__ = ("asm_session_sid", "hunt_group_sid", "skills")
    class SkillsEntry(_message.Message):
        __slots__ = ("key", "value")
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

class EnableVoiceRes(_message.Message):
    __slots__ = ("voice_session", "voice_registration")
    VOICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    VOICE_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    voice_session: VoiceSession
    voice_registration: VoiceRegistration
    def __init__(self, voice_session: _Optional[_Union[VoiceSession, _Mapping]] = ..., voice_registration: _Optional[_Union[VoiceRegistration, _Mapping]] = ...) -> None: ...

class DisableVoiceReq(_message.Message):
    __slots__ = ("asm_session_sid",)
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    asm_session_sid: int
    def __init__(self, asm_session_sid: _Optional[int] = ...) -> None: ...

class DisableVoiceRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAsmUserDetailsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAsmUserDetailsRes(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[ListAsmUserDetails]
    def __init__(self, sessions: _Optional[_Iterable[_Union[ListAsmUserDetails, _Mapping]]] = ...) -> None: ...

class ListAsmUserDetails(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
