from api.commons import asm_pb2 as _asm_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ()
    STATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_CONVERSATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
    SEND_STATUS_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_EVENT_FIELD_NUMBER: _ClassVar[int]
    RESUME_EVENT_FIELD_NUMBER: _ClassVar[int]
    state: _asm_pb2.StatusState
    event_time: int
    activated_conversation_event: ActivatedConversationEvent
    deactivated_conversation_event: DeactivatedConversationEvent
    sent_message_event: SentMessageEvent
    send_status_event: SendStatusEvent
    pause_event: PauseEvent
    resume_event: ResumeEvent
    def __init__(self, state: _Optional[_Union[_asm_pb2.StatusState, str]] = ..., event_time: _Optional[int] = ..., activated_conversation_event: _Optional[_Union[ActivatedConversationEvent, _Mapping]] = ..., deactivated_conversation_event: _Optional[_Union[DeactivatedConversationEvent, _Mapping]] = ..., sent_message_event: _Optional[_Union[SentMessageEvent, _Mapping]] = ..., send_status_event: _Optional[_Union[SendStatusEvent, _Mapping]] = ..., pause_event: _Optional[_Union[PauseEvent, _Mapping]] = ..., resume_event: _Optional[_Union[ResumeEvent, _Mapping]] = ...) -> None: ...

class ActivatedConversationEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class DeactivatedConversationEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class SentMessageEvent(_message.Message):
    __slots__ = ()
    RESPONSE_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IS_INITIAL_AGENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    response_time_seconds: int
    is_initial_agent_message: bool
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, response_time_seconds: _Optional[int] = ..., is_initial_agent_message: _Optional[bool] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class SendStatusEvent(_message.Message):
    __slots__ = ()
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _asm_pb2.StatusState
    def __init__(self, status: _Optional[_Union[_asm_pb2.StatusState, str]] = ...) -> None: ...

class AsmEvent(_message.Message):
    __slots__ = ()
    STATE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_CONVERSATION_ASM_EVENT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_CONVERSATION_ASM_EVENT_FIELD_NUMBER: _ClassVar[int]
    SENT_MESSAGE_ASM_EVENT_FIELD_NUMBER: _ClassVar[int]
    SEND_STATUS_ASM_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_EVENT_FIELD_NUMBER: _ClassVar[int]
    RESUME_EVENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PULLED_EVENT_FIELD_NUMBER: _ClassVar[int]
    state: _asm_pb2.StatusState
    event_time: int
    activated_conversation_asm_event: ActivatedConversationAsmEvent
    deactivated_conversation_asm_event: DeactivatedConversationAsmEvent
    sent_message_asm_event: SentMessageAsmEvent
    send_status_asm_event: SendStatusAsmEvent
    pause_event: PauseEvent
    resume_event: ResumeEvent
    conversation_pulled_event: ConversationPulledEvent
    def __init__(self, state: _Optional[_Union[_asm_pb2.StatusState, str]] = ..., event_time: _Optional[int] = ..., activated_conversation_asm_event: _Optional[_Union[ActivatedConversationAsmEvent, _Mapping]] = ..., deactivated_conversation_asm_event: _Optional[_Union[DeactivatedConversationAsmEvent, _Mapping]] = ..., sent_message_asm_event: _Optional[_Union[SentMessageAsmEvent, _Mapping]] = ..., send_status_asm_event: _Optional[_Union[SendStatusAsmEvent, _Mapping]] = ..., pause_event: _Optional[_Union[PauseEvent, _Mapping]] = ..., resume_event: _Optional[_Union[ResumeEvent, _Mapping]] = ..., conversation_pulled_event: _Optional[_Union[ConversationPulledEvent, _Mapping]] = ...) -> None: ...

class ActivatedConversationAsmEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class DeactivatedConversationAsmEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class SentMessageAsmEvent(_message.Message):
    __slots__ = ()
    RESPONSE_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IS_INITIAL_AGENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    response_time_seconds: int
    is_initial_agent_message: bool
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, response_time_seconds: _Optional[int] = ..., is_initial_agent_message: _Optional[bool] = ..., conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...

class SendStatusAsmEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResumeEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConversationPulledEvent(_message.Message):
    __slots__ = ()
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: _omnichannel_pb2.OmniConversation
    def __init__(self, conversation: _Optional[_Union[_omnichannel_pb2.OmniConversation, _Mapping]] = ...) -> None: ...
