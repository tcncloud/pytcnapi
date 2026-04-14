from api.commons import asm_pb2 as _asm_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AsmAgentLoginEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class AsmOpenVoiceEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid", "voice_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    voice_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ..., voice_session_sid: _Optional[int] = ...) -> None: ...

class AsmOpenOmniAgentEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class AsmActivateConversationEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid", "conversation")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class AsmDeactivateConversationEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid", "conversation")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class AsmAgentStateChangedEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid", "new_status", "old_status", "old_status_duration_milliseconds")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    OLD_STATUS_FIELD_NUMBER: _ClassVar[int]
    OLD_STATUS_DURATION_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    new_status: _asm_pb2.StatusState
    old_status: _asm_pb2.StatusState
    old_status_duration_milliseconds: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ..., new_status: _Optional[_Union[_asm_pb2.StatusState, str]] = ..., old_status: _Optional[_Union[_asm_pb2.StatusState, str]] = ..., old_status_duration_milliseconds: _Optional[int] = ...) -> None: ...

class AsmAgentLogoutEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid", "reason")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    reason: str
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class AsmPauseEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class AsmResumeEvent(_message.Message):
    __slots__ = ("user_id", "asm_session_sid")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    asm_session_sid: int
    def __init__(self, user_id: _Optional[str] = ..., asm_session_sid: _Optional[int] = ...) -> None: ...

class AsmConversationPulledEvent(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...
