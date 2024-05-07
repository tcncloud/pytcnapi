from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ACDStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACD_UNKNOWN: _ClassVar[ACDStatus]
    AGENT_SESSION_LOGGING_IN: _ClassVar[ACDStatus]
    AGENT_SESSION_LOGGED_IN: _ClassVar[ACDStatus]
    AGENT_SESSION_COMPLETED: _ClassVar[ACDStatus]
    AGENT_SESSION_SUMMED: _ClassVar[ACDStatus]
    AGENT_SESSION_ACCOUNTINGEXPORT: _ClassVar[ACDStatus]

class AgentCallLogCallEnded(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_CANCELLED: _ClassVar[AgentCallLogCallEnded]
    CALLER_DISCONNECTED: _ClassVar[AgentCallLogCallEnded]
    NOT_CONNECTED: _ClassVar[AgentCallLogCallEnded]
    AGENT_LOST: _ClassVar[AgentCallLogCallEnded]
    AGENT_HANGUP: _ClassVar[AgentCallLogCallEnded]
    CALLER_HANGUP: _ClassVar[AgentCallLogCallEnded]
    CALL_END_ESTIMATE: _ClassVar[AgentCallLogCallEnded]

class HoldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[HoldType]
    SIMPLE: _ClassVar[HoldType]
    MULTI: _ClassVar[HoldType]

class QueuedNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QueuedNotificationType_GENERAL_INITIAL: _ClassVar[QueuedNotificationType]
    QueuedNotificationType_PBX_INITIAL: _ClassVar[QueuedNotificationType]
    QueuedNotificationType_AGENT_BOUND_INITIAL: _ClassVar[QueuedNotificationType]
    QueuedNotificationType_GENERAL_REQUEUED: _ClassVar[QueuedNotificationType]
    QueuedNotificationType_AGENT_BOUND_REQUEUED: _ClassVar[QueuedNotificationType]

class TransferMemberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TransferMemberType_AGENT: _ClassVar[TransferMemberType]
    TransferMemberType_CALLER: _ClassVar[TransferMemberType]
    TransferMemberType_OUTBOUND: _ClassVar[TransferMemberType]

class DTMFDigit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DTMFDigit_0: _ClassVar[DTMFDigit]
    DTMFDigit_1: _ClassVar[DTMFDigit]
    DTMFDigit_2: _ClassVar[DTMFDigit]
    DTMFDigit_3: _ClassVar[DTMFDigit]
    DTMFDigit_4: _ClassVar[DTMFDigit]
    DTMFDigit_5: _ClassVar[DTMFDigit]
    DTMFDigit_6: _ClassVar[DTMFDigit]
    DTMFDigit_7: _ClassVar[DTMFDigit]
    DTMFDigit_8: _ClassVar[DTMFDigit]
    DTMFDigit_9: _ClassVar[DTMFDigit]
    DTMFDigit_A: _ClassVar[DTMFDigit]
    DTMFDigit_B: _ClassVar[DTMFDigit]
    DTMFDigit_C: _ClassVar[DTMFDigit]
    DTMFDigit_D: _ClassVar[DTMFDigit]
    DTMFDigit_STAR: _ClassVar[DTMFDigit]
    DTMFDigit_POUND: _ClassVar[DTMFDigit]
ACD_UNKNOWN: ACDStatus
AGENT_SESSION_LOGGING_IN: ACDStatus
AGENT_SESSION_LOGGED_IN: ACDStatus
AGENT_SESSION_COMPLETED: ACDStatus
AGENT_SESSION_SUMMED: ACDStatus
AGENT_SESSION_ACCOUNTINGEXPORT: ACDStatus
AGENT_CANCELLED: AgentCallLogCallEnded
CALLER_DISCONNECTED: AgentCallLogCallEnded
NOT_CONNECTED: AgentCallLogCallEnded
AGENT_LOST: AgentCallLogCallEnded
AGENT_HANGUP: AgentCallLogCallEnded
CALLER_HANGUP: AgentCallLogCallEnded
CALL_END_ESTIMATE: AgentCallLogCallEnded
UNKNOWN: HoldType
SIMPLE: HoldType
MULTI: HoldType
QueuedNotificationType_GENERAL_INITIAL: QueuedNotificationType
QueuedNotificationType_PBX_INITIAL: QueuedNotificationType
QueuedNotificationType_AGENT_BOUND_INITIAL: QueuedNotificationType
QueuedNotificationType_GENERAL_REQUEUED: QueuedNotificationType
QueuedNotificationType_AGENT_BOUND_REQUEUED: QueuedNotificationType
TransferMemberType_AGENT: TransferMemberType
TransferMemberType_CALLER: TransferMemberType
TransferMemberType_OUTBOUND: TransferMemberType
DTMFDigit_0: DTMFDigit
DTMFDigit_1: DTMFDigit
DTMFDigit_2: DTMFDigit
DTMFDigit_3: DTMFDigit
DTMFDigit_4: DTMFDigit
DTMFDigit_5: DTMFDigit
DTMFDigit_6: DTMFDigit
DTMFDigit_7: DTMFDigit
DTMFDigit_8: DTMFDigit
DTMFDigit_9: DTMFDigit
DTMFDigit_A: DTMFDigit
DTMFDigit_B: DTMFDigit
DTMFDigit_C: DTMFDigit
DTMFDigit_D: DTMFDigit
DTMFDigit_STAR: DTMFDigit
DTMFDigit_POUND: DTMFDigit

class AgentSession(_message.Message):
    __slots__ = ("agent_sid", "tenant_sid", "session_sid", "asm_session_sid", "org_id", "region_id", "user_id")
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    TENANT_SID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    tenant_sid: int
    session_sid: int
    asm_session_sid: int
    org_id: str
    region_id: str
    user_id: str
    def __init__(self, agent_sid: _Optional[int] = ..., tenant_sid: _Optional[int] = ..., session_sid: _Optional[int] = ..., asm_session_sid: _Optional[int] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class CallerSid(_message.Message):
    __slots__ = ("caller_sid", "type", "tenant_sid", "org_id")
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_SID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    caller_sid: int
    type: CallType.Enum
    tenant_sid: int
    org_id: str
    def __init__(self, caller_sid: _Optional[int] = ..., type: _Optional[_Union[CallType.Enum, str]] = ..., tenant_sid: _Optional[int] = ..., org_id: _Optional[str] = ...) -> None: ...

class AgentStatus(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNAVALIABLE: _ClassVar[AgentStatus.Enum]
        IDLE: _ClassVar[AgentStatus.Enum]
        READY: _ClassVar[AgentStatus.Enum]
        HUNGUP: _ClassVar[AgentStatus.Enum]
        DESTROYED: _ClassVar[AgentStatus.Enum]
        PEERED: _ClassVar[AgentStatus.Enum]
        PAUSED: _ClassVar[AgentStatus.Enum]
        WRAPUP: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_IDLE: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_WRAPUP: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_PAUSE: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_DIAL_CANCEL: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_PBX_REJECT: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_PBX_HANGUP: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_PBX_WAS_TAKEN: _ClassVar[AgentStatus.Enum]
        PREPARING_AFTER_GUI_BUSY: _ClassVar[AgentStatus.Enum]
        MANUAL_DIAL_PREPARED: _ClassVar[AgentStatus.Enum]
        PREVIEW_DIAL_PREPARED: _ClassVar[AgentStatus.Enum]
        MANUAL_DIAL_STARTED: _ClassVar[AgentStatus.Enum]
        PREVIEW_DIAL_STARTED: _ClassVar[AgentStatus.Enum]
        OUTBOUND_LOCKED: _ClassVar[AgentStatus.Enum]
        WARM_AGENT_TRANSFER_STARTED_SOURCE: _ClassVar[AgentStatus.Enum]
        WARM_AGENT_TRANSFER_STARTED_DESTINATION: _ClassVar[AgentStatus.Enum]
        WARM_OUTBOUND_TRANSFER_STARTED: _ClassVar[AgentStatus.Enum]
        WARM_OUTBOUND_TRANSFER_PEER_LOST: _ClassVar[AgentStatus.Enum]
        PBX_POPUP_LOCKED: _ClassVar[AgentStatus.Enum]
        PEERED_WITH_CALL_ON_HOLD: _ClassVar[AgentStatus.Enum]
        CALLBACK_RESUMING: _ClassVar[AgentStatus.Enum]
        GUI_BUSY: _ClassVar[AgentStatus.Enum]
        INTERCOM: _ClassVar[AgentStatus.Enum]
        INTERCOM_RINGING_SOURCE: _ClassVar[AgentStatus.Enum]
        INTERCOM_RINGING_DESTINATION: _ClassVar[AgentStatus.Enum]
        WARM_OUTBOUND_TRANSFER_OUTBOUND_LOST: _ClassVar[AgentStatus.Enum]
        PREPARED_TO_PEER: _ClassVar[AgentStatus.Enum]
        WARM_SKILL_TRANSFER_SOURCE_PENDING: _ClassVar[AgentStatus.Enum]
        CALLER_TRANSFER_STARTED: _ClassVar[AgentStatus.Enum]
        CALLER_TRANSFER_LOST_PEER: _ClassVar[AgentStatus.Enum]
        CALLER_TRANSFER_LOST_MERGED_CALLER: _ClassVar[AgentStatus.Enum]
        COLD_OUTBOUND_TRANSFER_STARTED: _ClassVar[AgentStatus.Enum]
        COLD_AGENT_TRANSFER_STARTED: _ClassVar[AgentStatus.Enum]
    UNAVALIABLE: AgentStatus.Enum
    IDLE: AgentStatus.Enum
    READY: AgentStatus.Enum
    HUNGUP: AgentStatus.Enum
    DESTROYED: AgentStatus.Enum
    PEERED: AgentStatus.Enum
    PAUSED: AgentStatus.Enum
    WRAPUP: AgentStatus.Enum
    PREPARING_AFTER_IDLE: AgentStatus.Enum
    PREPARING_AFTER_WRAPUP: AgentStatus.Enum
    PREPARING_AFTER_PAUSE: AgentStatus.Enum
    PREPARING_AFTER_DIAL_CANCEL: AgentStatus.Enum
    PREPARING_AFTER_PBX_REJECT: AgentStatus.Enum
    PREPARING_AFTER_PBX_HANGUP: AgentStatus.Enum
    PREPARING_AFTER_PBX_WAS_TAKEN: AgentStatus.Enum
    PREPARING_AFTER_GUI_BUSY: AgentStatus.Enum
    MANUAL_DIAL_PREPARED: AgentStatus.Enum
    PREVIEW_DIAL_PREPARED: AgentStatus.Enum
    MANUAL_DIAL_STARTED: AgentStatus.Enum
    PREVIEW_DIAL_STARTED: AgentStatus.Enum
    OUTBOUND_LOCKED: AgentStatus.Enum
    WARM_AGENT_TRANSFER_STARTED_SOURCE: AgentStatus.Enum
    WARM_AGENT_TRANSFER_STARTED_DESTINATION: AgentStatus.Enum
    WARM_OUTBOUND_TRANSFER_STARTED: AgentStatus.Enum
    WARM_OUTBOUND_TRANSFER_PEER_LOST: AgentStatus.Enum
    PBX_POPUP_LOCKED: AgentStatus.Enum
    PEERED_WITH_CALL_ON_HOLD: AgentStatus.Enum
    CALLBACK_RESUMING: AgentStatus.Enum
    GUI_BUSY: AgentStatus.Enum
    INTERCOM: AgentStatus.Enum
    INTERCOM_RINGING_SOURCE: AgentStatus.Enum
    INTERCOM_RINGING_DESTINATION: AgentStatus.Enum
    WARM_OUTBOUND_TRANSFER_OUTBOUND_LOST: AgentStatus.Enum
    PREPARED_TO_PEER: AgentStatus.Enum
    WARM_SKILL_TRANSFER_SOURCE_PENDING: AgentStatus.Enum
    CALLER_TRANSFER_STARTED: AgentStatus.Enum
    CALLER_TRANSFER_LOST_PEER: AgentStatus.Enum
    CALLER_TRANSFER_LOST_MERGED_CALLER: AgentStatus.Enum
    COLD_OUTBOUND_TRANSFER_STARTED: AgentStatus.Enum
    COLD_AGENT_TRANSFER_STARTED: AgentStatus.Enum
    def __init__(self) -> None: ...

class CallerStatus(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNAVALIABLE: _ClassVar[CallerStatus.Enum]
        IDLE: _ClassVar[CallerStatus.Enum]
        READY: _ClassVar[CallerStatus.Enum]
        HUNGUP: _ClassVar[CallerStatus.Enum]
        DESTROYED: _ClassVar[CallerStatus.Enum]
        PEERED: _ClassVar[CallerStatus.Enum]
        OUTBOUND_LOCKED: _ClassVar[CallerStatus.Enum]
        OUTBOUND_PEERED: _ClassVar[CallerStatus.Enum]
        PBX_POPUP_LOCKED: _ClassVar[CallerStatus.Enum]
        VOICEMAIL: _ClassVar[CallerStatus.Enum]
        PEERED_WITH_CALL_ON_HOLD: _ClassVar[CallerStatus.Enum]
        CALLBACK_SUSPENDED: _ClassVar[CallerStatus.Enum]
        WARM_AGENT_TRANSFER_STARTED: _ClassVar[CallerStatus.Enum]
        WARM_OUTBOUND_TRANSFER_STARTED: _ClassVar[CallerStatus.Enum]
        OUTBOUND_DIAL_TRANSFER_STARTED: _ClassVar[CallerStatus.Enum]
        PREPARED_TO_PEER: _ClassVar[CallerStatus.Enum]
        WARM_SKILL_TRANSFER_PENDING: _ClassVar[CallerStatus.Enum]
        CALLER_TRANSFER_PEER: _ClassVar[CallerStatus.Enum]
        CALLER_TRANSFER_MERGED_CALLER: _ClassVar[CallerStatus.Enum]
        CALLER_PEERED: _ClassVar[CallerStatus.Enum]
    UNAVALIABLE: CallerStatus.Enum
    IDLE: CallerStatus.Enum
    READY: CallerStatus.Enum
    HUNGUP: CallerStatus.Enum
    DESTROYED: CallerStatus.Enum
    PEERED: CallerStatus.Enum
    OUTBOUND_LOCKED: CallerStatus.Enum
    OUTBOUND_PEERED: CallerStatus.Enum
    PBX_POPUP_LOCKED: CallerStatus.Enum
    VOICEMAIL: CallerStatus.Enum
    PEERED_WITH_CALL_ON_HOLD: CallerStatus.Enum
    CALLBACK_SUSPENDED: CallerStatus.Enum
    WARM_AGENT_TRANSFER_STARTED: CallerStatus.Enum
    WARM_OUTBOUND_TRANSFER_STARTED: CallerStatus.Enum
    OUTBOUND_DIAL_TRANSFER_STARTED: CallerStatus.Enum
    PREPARED_TO_PEER: CallerStatus.Enum
    WARM_SKILL_TRANSFER_PENDING: CallerStatus.Enum
    CALLER_TRANSFER_PEER: CallerStatus.Enum
    CALLER_TRANSFER_MERGED_CALLER: CallerStatus.Enum
    CALLER_PEERED: CallerStatus.Enum
    def __init__(self) -> None: ...

class CallType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INBOUND: _ClassVar[CallType.Enum]
        OUTBOUND: _ClassVar[CallType.Enum]
        PREVIEW: _ClassVar[CallType.Enum]
        MANUAL: _ClassVar[CallType.Enum]
        MAC: _ClassVar[CallType.Enum]
    INBOUND: CallType.Enum
    OUTBOUND: CallType.Enum
    PREVIEW: CallType.Enum
    MANUAL: CallType.Enum
    MAC: CallType.Enum
    def __init__(self) -> None: ...

class AgentDialIn(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOLL_FREE: _ClassVar[AgentDialIn.Enum]
        SOFTPHONE: _ClassVar[AgentDialIn.Enum]
        LOCAL: _ClassVar[AgentDialIn.Enum]
    TOLL_FREE: AgentDialIn.Enum
    SOFTPHONE: AgentDialIn.Enum
    LOCAL: AgentDialIn.Enum
    def __init__(self) -> None: ...

class HuntGroupType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNCONNECTED: _ClassVar[HuntGroupType.Enum]
        CONNECTED: _ClassVar[HuntGroupType.Enum]
        SOFTPHONE: _ClassVar[HuntGroupType.Enum]
    UNCONNECTED: HuntGroupType.Enum
    CONNECTED: HuntGroupType.Enum
    SOFTPHONE: HuntGroupType.Enum
    def __init__(self) -> None: ...

class AgentSessionLogActionKey(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGENT_PAUSE_START: _ClassVar[AgentSessionLogActionKey.Enum]
        AGENT_PAUSE_STOP: _ClassVar[AgentSessionLogActionKey.Enum]
        AGENT_SKILLS_INITIAL: _ClassVar[AgentSessionLogActionKey.Enum]
        AGENT_LOGOUT: _ClassVar[AgentSessionLogActionKey.Enum]
        EXECUTED_AGENT_TRIGGER: _ClassVar[AgentSessionLogActionKey.Enum]
        DURATION_SINCE_LAST_LOGON: _ClassVar[AgentSessionLogActionKey.Enum]
        AGENT_LOGIN_IP: _ClassVar[AgentSessionLogActionKey.Enum]
        MAC_DECISION: _ClassVar[AgentSessionLogActionKey.Enum]
        MAC_10_KEY_DECISION: _ClassVar[AgentSessionLogActionKey.Enum]
        MAC_10_KEY_CONFIRM: _ClassVar[AgentSessionLogActionKey.Enum]
        HUNT_GROUP_REASSIGNMENT: _ClassVar[AgentSessionLogActionKey.Enum]
        PBX_ACCEPT: _ClassVar[AgentSessionLogActionKey.Enum]
        PBX_HANGUP: _ClassVar[AgentSessionLogActionKey.Enum]
        PBX_LOST: _ClassVar[AgentSessionLogActionKey.Enum]
        PBX_REJECT: _ClassVar[AgentSessionLogActionKey.Enum]
        PBX_TIMEOUT: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_INVITE_CALLER: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_START_SOURCE: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_END_SOURCE: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_START_DESTINATION: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_AGENT_END_DESTINATION: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_INVITE_CALLER: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_START: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_END: _ClassVar[AgentSessionLogActionKey.Enum]
        COLD_TRANSFER_OUTBOUND_START: _ClassVar[AgentSessionLogActionKey.Enum]
        COLD_TRANSFER_AGENT_START_SOURCE: _ClassVar[AgentSessionLogActionKey.Enum]
        COLD_TRANSFER_AGENT_END_SOURCE: _ClassVar[AgentSessionLogActionKey.Enum]
        COLD_TRANSFER_AGENT_START_DESTINATION: _ClassVar[AgentSessionLogActionKey.Enum]
        COLD_TRANSFER_AGENT_END_DESTINATION: _ClassVar[AgentSessionLogActionKey.Enum]
        HOLD_START: _ClassVar[AgentSessionLogActionKey.Enum]
        HOLD_END: _ClassVar[AgentSessionLogActionKey.Enum]
        REQUEUE: _ClassVar[AgentSessionLogActionKey.Enum]
        CALLER_SENT_TO_VOICEMAIL: _ClassVar[AgentSessionLogActionKey.Enum]
        RECORDING_START: _ClassVar[AgentSessionLogActionKey.Enum]
        RECORDING_STOP: _ClassVar[AgentSessionLogActionKey.Enum]
        PBR_STARTED_RECORD: _ClassVar[AgentSessionLogActionKey.Enum]
        PBR_FINISHED_RECORD: _ClassVar[AgentSessionLogActionKey.Enum]
        ACD_LOGOUT: _ClassVar[AgentSessionLogActionKey.Enum]
        ACD_REGISTER: _ClassVar[AgentSessionLogActionKey.Enum]
        EXECUTED_AGENT_WEBLINK: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_HOLD_CALLER: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_UNHOLD_CALLER: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_HOLD_AGENT: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_UNHOLD_AGENT: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_HOLD: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_UNHOLD: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_HOLD_OUTBOUND: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_UNHOLD_OUTBOUND: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_ADD_OUTBOUND: _ClassVar[AgentSessionLogActionKey.Enum]
        TRANSFER_REMOVE_OUTBOUND: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_CALLER_TRANSFER_START: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_CALLER_TRANSFER_INVITE_CALLER: _ClassVar[AgentSessionLogActionKey.Enum]
        WARM_CALLER_TRANSFER_END: _ClassVar[AgentSessionLogActionKey.Enum]
        BARGE_IN_START: _ClassVar[AgentSessionLogActionKey.Enum]
        BARGE_IN_STOP: _ClassVar[AgentSessionLogActionKey.Enum]
        BargeInCallJoined: _ClassVar[AgentSessionLogActionKey.Enum]
        BargeInCallLeft: _ClassVar[AgentSessionLogActionKey.Enum]
    AGENT_PAUSE_START: AgentSessionLogActionKey.Enum
    AGENT_PAUSE_STOP: AgentSessionLogActionKey.Enum
    AGENT_SKILLS_INITIAL: AgentSessionLogActionKey.Enum
    AGENT_LOGOUT: AgentSessionLogActionKey.Enum
    EXECUTED_AGENT_TRIGGER: AgentSessionLogActionKey.Enum
    DURATION_SINCE_LAST_LOGON: AgentSessionLogActionKey.Enum
    AGENT_LOGIN_IP: AgentSessionLogActionKey.Enum
    MAC_DECISION: AgentSessionLogActionKey.Enum
    MAC_10_KEY_DECISION: AgentSessionLogActionKey.Enum
    MAC_10_KEY_CONFIRM: AgentSessionLogActionKey.Enum
    HUNT_GROUP_REASSIGNMENT: AgentSessionLogActionKey.Enum
    PBX_ACCEPT: AgentSessionLogActionKey.Enum
    PBX_HANGUP: AgentSessionLogActionKey.Enum
    PBX_LOST: AgentSessionLogActionKey.Enum
    PBX_REJECT: AgentSessionLogActionKey.Enum
    PBX_TIMEOUT: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_INVITE_CALLER: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_START_SOURCE: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_END_SOURCE: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_START_DESTINATION: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_AGENT_END_DESTINATION: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_INVITE_CALLER: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_START: AgentSessionLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_END: AgentSessionLogActionKey.Enum
    COLD_TRANSFER_OUTBOUND_START: AgentSessionLogActionKey.Enum
    COLD_TRANSFER_AGENT_START_SOURCE: AgentSessionLogActionKey.Enum
    COLD_TRANSFER_AGENT_END_SOURCE: AgentSessionLogActionKey.Enum
    COLD_TRANSFER_AGENT_START_DESTINATION: AgentSessionLogActionKey.Enum
    COLD_TRANSFER_AGENT_END_DESTINATION: AgentSessionLogActionKey.Enum
    HOLD_START: AgentSessionLogActionKey.Enum
    HOLD_END: AgentSessionLogActionKey.Enum
    REQUEUE: AgentSessionLogActionKey.Enum
    CALLER_SENT_TO_VOICEMAIL: AgentSessionLogActionKey.Enum
    RECORDING_START: AgentSessionLogActionKey.Enum
    RECORDING_STOP: AgentSessionLogActionKey.Enum
    PBR_STARTED_RECORD: AgentSessionLogActionKey.Enum
    PBR_FINISHED_RECORD: AgentSessionLogActionKey.Enum
    ACD_LOGOUT: AgentSessionLogActionKey.Enum
    ACD_REGISTER: AgentSessionLogActionKey.Enum
    EXECUTED_AGENT_WEBLINK: AgentSessionLogActionKey.Enum
    TRANSFER_HOLD_CALLER: AgentSessionLogActionKey.Enum
    TRANSFER_UNHOLD_CALLER: AgentSessionLogActionKey.Enum
    TRANSFER_HOLD_AGENT: AgentSessionLogActionKey.Enum
    TRANSFER_UNHOLD_AGENT: AgentSessionLogActionKey.Enum
    TRANSFER_HOLD: AgentSessionLogActionKey.Enum
    TRANSFER_UNHOLD: AgentSessionLogActionKey.Enum
    TRANSFER_HOLD_OUTBOUND: AgentSessionLogActionKey.Enum
    TRANSFER_UNHOLD_OUTBOUND: AgentSessionLogActionKey.Enum
    TRANSFER_ADD_OUTBOUND: AgentSessionLogActionKey.Enum
    TRANSFER_REMOVE_OUTBOUND: AgentSessionLogActionKey.Enum
    WARM_CALLER_TRANSFER_START: AgentSessionLogActionKey.Enum
    WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL: AgentSessionLogActionKey.Enum
    WARM_CALLER_TRANSFER_INVITE_CALLER: AgentSessionLogActionKey.Enum
    WARM_CALLER_TRANSFER_END: AgentSessionLogActionKey.Enum
    BARGE_IN_START: AgentSessionLogActionKey.Enum
    BARGE_IN_STOP: AgentSessionLogActionKey.Enum
    BargeInCallJoined: AgentSessionLogActionKey.Enum
    BargeInCallLeft: AgentSessionLogActionKey.Enum
    def __init__(self) -> None: ...

class AgentCallLogActionKey(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DNCL_ADD: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_ENDED: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_DISCONNECT: _ClassVar[AgentCallLogActionKey.Enum]
        CALLER_HUNGUP: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_AGENT_INVITE_CALLER: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_AGENT_START: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_AGENT_END: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_INVITE_CALLER: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_START: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_TRANSFER_OUTBOUND_END: _ClassVar[AgentCallLogActionKey.Enum]
        COLD_TRANSFER_AGENT_START: _ClassVar[AgentCallLogActionKey.Enum]
        COLD_TRANSFER_AGENT_END: _ClassVar[AgentCallLogActionKey.Enum]
        COLD_TRANSFER_OUTBOUND_START: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_SUSPEND_START: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_RESUMING: _ClassVar[AgentCallLogActionKey.Enum]
        VOICEMAIL_END: _ClassVar[AgentCallLogActionKey.Enum]
        CALLER_SENT_TO_VOICEMAIL: _ClassVar[AgentCallLogActionKey.Enum]
        HOLD_START: _ClassVar[AgentCallLogActionKey.Enum]
        HOLD_END: _ClassVar[AgentCallLogActionKey.Enum]
        RECORDING_START: _ClassVar[AgentCallLogActionKey.Enum]
        RECORDING_STOP: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_SKILLS_SCORE: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_SKILLS_MATCHED: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_SKILLS_CURRENT: _ClassVar[AgentCallLogActionKey.Enum]
        CALL_SKILLS_INITIAL: _ClassVar[AgentCallLogActionKey.Enum]
        SKILLS_CHANGED_DROPSKILLS: _ClassVar[AgentCallLogActionKey.Enum]
        SKILLS_CHANGED_ADDSKILLS: _ClassVar[AgentCallLogActionKey.Enum]
        REQUEUE: _ClassVar[AgentCallLogActionKey.Enum]
        SKILLS_CHANGED_REQUEUE: _ClassVar[AgentCallLogActionKey.Enum]
        SCRUB_OVERRIDE: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_RESUMING_WITH_MANUAL_CALL_START: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_RESUMING_WITH_MANUAL_CALL_FINISH: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_RESUMING_WITH_MANUAL_CALL_TIMEDOUT: _ClassVar[AgentCallLogActionKey.Enum]
        CALLBACK_RESUMING_WITH_MANUAL_CALL_REPLACED: _ClassVar[AgentCallLogActionKey.Enum]
        TRANSFER_HOLD: _ClassVar[AgentCallLogActionKey.Enum]
        TRANSFER_UNHOLD: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_CALLER_TRANSFER_SOURCE_START: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_CALLER_TRANSFER_DESTINATION_START: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_CALLER_TRANSFER_INVITE_CALLER: _ClassVar[AgentCallLogActionKey.Enum]
        WARM_CALLER_TRANSFER_END: _ClassVar[AgentCallLogActionKey.Enum]
        BARGE_IN_START: _ClassVar[AgentCallLogActionKey.Enum]
        BARGE_IN_STOP: _ClassVar[AgentCallLogActionKey.Enum]
    DNCL_ADD: AgentCallLogActionKey.Enum
    CALL_ENDED: AgentCallLogActionKey.Enum
    CALL_DISCONNECT: AgentCallLogActionKey.Enum
    CALLER_HUNGUP: AgentCallLogActionKey.Enum
    WARM_TRANSFER_AGENT_INVITE_CALLER_INITIAL: AgentCallLogActionKey.Enum
    WARM_TRANSFER_AGENT_INVITE_CALLER: AgentCallLogActionKey.Enum
    WARM_TRANSFER_AGENT_START: AgentCallLogActionKey.Enum
    WARM_TRANSFER_AGENT_END: AgentCallLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_INVITE_CALLER: AgentCallLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_INVITE_CALLER_INITIAL: AgentCallLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_START: AgentCallLogActionKey.Enum
    WARM_TRANSFER_OUTBOUND_END: AgentCallLogActionKey.Enum
    COLD_TRANSFER_AGENT_START: AgentCallLogActionKey.Enum
    COLD_TRANSFER_AGENT_END: AgentCallLogActionKey.Enum
    COLD_TRANSFER_OUTBOUND_START: AgentCallLogActionKey.Enum
    CALLBACK_SUSPEND_START: AgentCallLogActionKey.Enum
    CALLBACK_RESUMING: AgentCallLogActionKey.Enum
    VOICEMAIL_END: AgentCallLogActionKey.Enum
    CALLER_SENT_TO_VOICEMAIL: AgentCallLogActionKey.Enum
    HOLD_START: AgentCallLogActionKey.Enum
    HOLD_END: AgentCallLogActionKey.Enum
    RECORDING_START: AgentCallLogActionKey.Enum
    RECORDING_STOP: AgentCallLogActionKey.Enum
    CALL_SKILLS_SCORE: AgentCallLogActionKey.Enum
    CALL_SKILLS_MATCHED: AgentCallLogActionKey.Enum
    CALL_SKILLS_CURRENT: AgentCallLogActionKey.Enum
    CALL_SKILLS_INITIAL: AgentCallLogActionKey.Enum
    SKILLS_CHANGED_DROPSKILLS: AgentCallLogActionKey.Enum
    SKILLS_CHANGED_ADDSKILLS: AgentCallLogActionKey.Enum
    REQUEUE: AgentCallLogActionKey.Enum
    SKILLS_CHANGED_REQUEUE: AgentCallLogActionKey.Enum
    SCRUB_OVERRIDE: AgentCallLogActionKey.Enum
    CALLBACK_RESUMING_WITH_MANUAL_CALL_START: AgentCallLogActionKey.Enum
    CALLBACK_RESUMING_WITH_MANUAL_CALL_FINISH: AgentCallLogActionKey.Enum
    CALLBACK_RESUMING_WITH_MANUAL_CALL_TIMEDOUT: AgentCallLogActionKey.Enum
    CALLBACK_RESUMING_WITH_MANUAL_CALL_REPLACED: AgentCallLogActionKey.Enum
    TRANSFER_HOLD: AgentCallLogActionKey.Enum
    TRANSFER_UNHOLD: AgentCallLogActionKey.Enum
    WARM_CALLER_TRANSFER_SOURCE_START: AgentCallLogActionKey.Enum
    WARM_CALLER_TRANSFER_DESTINATION_START: AgentCallLogActionKey.Enum
    WARM_CALLER_TRANSFER_INVITE_CALLER_INITIAL: AgentCallLogActionKey.Enum
    WARM_CALLER_TRANSFER_INVITE_CALLER: AgentCallLogActionKey.Enum
    WARM_CALLER_TRANSFER_END: AgentCallLogActionKey.Enum
    BARGE_IN_START: AgentCallLogActionKey.Enum
    BARGE_IN_STOP: AgentCallLogActionKey.Enum
    def __init__(self) -> None: ...

class AgentCallLogActionValue(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AgentCallLogActionValue.Enum]
        DNCL_RESULT_FAILED: _ClassVar[AgentCallLogActionValue.Enum]
        CALL_ENDED_CALLER_DISCONNECTED: _ClassVar[AgentCallLogActionValue.Enum]
    UNSPECIFIED: AgentCallLogActionValue.Enum
    DNCL_RESULT_FAILED: AgentCallLogActionValue.Enum
    CALL_ENDED_CALLER_DISCONNECTED: AgentCallLogActionValue.Enum
    def __init__(self) -> None: ...

class HuntGroupParamKey(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGENT_DIAL_IN_NUMBER: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_LOGIN_GUI_STATISTICS_TEMPLATE: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_PASSWORD_REQUIRES_LETTER: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_PASSWORD_REQUIRES_NUMBER: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_PASSWORD_REQUIRES_SYMBOL: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_PASSWORD_REQUIRES_UPPER_LOWER: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_SKILLS_REASSIGNMENT: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_STATS_CALL_HISTORY: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_TRIGGER: _ClassVar[HuntGroupParamKey.Enum]
        AGENT_DISPOSITION_CONDITIONAL_DNCL: _ClassVar[HuntGroupParamKey.Enum]
        ALLOWED_IPS: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_AGENT_HOLD: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_AGENT_INTERCOM: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_AGENT_PASSWORD_RESET: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_AGENT_PAUSE_CODE_RESET: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_AGENT_TO_PAUSE: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_CALLBACK_SCHEDULING: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_EXPORT_PHONE_NUMBER_ACTIVITY: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_MANUAL_APPROVAL_OF_CALLS: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_MANUAL_DIALING: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_PHONE_NUMBER_ACTIVITY: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_PREVIEW_DIAL_CANCEL: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_SCHEDULED_CALLBACK_CALLING: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_TRANSFER_CALLS: _ClassVar[HuntGroupParamKey.Enum]
        ALPHANUMERIC_KEYPAD: _ClassVar[HuntGroupParamKey.Enum]
        AUTO_PAUSE_ON_MULTI_HOLD: _ClassVar[HuntGroupParamKey.Enum]
        AUTO_PAUSE_ON_PREVIEW_CANCEL: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_AGENT_PAUSE_CODE: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_AGENT_TRANSFERS_FILTERING: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_DNCL_COUNTRY: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_DNCL_EXPIRATION: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_INBOUND_CALL_DNCL_EXPIRATION: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_MANUAL_CALL_DNCL_EXPIRATION: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_OUTBOUND_CALL_DNCL_EXPIRATION: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_PREVIEW_CALL_DNCL_EXPIRATION: _ClassVar[HuntGroupParamKey.Enum]
        DEFAULT_SCHEDULED_CALLBACK_ROUTING: _ClassVar[HuntGroupParamKey.Enum]
        DISCONNECT_CALL_CONFIRMATION: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_AGENT_TRANSFERS_FILTERING: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_DATA_COLLECT_DATA: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_DATA_DIPPED_DATA: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_IVR_KEYS_PRESSED: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_PHONE_ZIP_METADATA: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_RECORDING_INDICATOR: _ClassVar[HuntGroupParamKey.Enum]
        DO_ALLOW_ADD_DNCL: _ClassVar[HuntGroupParamKey.Enum]
        ENABLE_RECORDING_PAUSE: _ClassVar[HuntGroupParamKey.Enum]
        HOLD_QUEUE_MONITORING: _ClassVar[HuntGroupParamKey.Enum]
        HOLD_QUEUE_MONITORING_AGENT_ROUTING: _ClassVar[HuntGroupParamKey.Enum]
        HOLD_QUEUE_MONITORING_PREFERRED_HUNT_GROUP_ROUTING: _ClassVar[HuntGroupParamKey.Enum]
        HOLD_QUEUE_MONITORING_REQUIRED_HUNT_GROUP_ROUTING: _ClassVar[HuntGroupParamKey.Enum]
        HUNT_GROUP_CLIENT_INFO_DISPLAY_TEMPLATE: _ClassVar[HuntGroupParamKey.Enum]
        HUNT_GROUP_SCRIPT: _ClassVar[HuntGroupParamKey.Enum]
        HUNT_GROUP_WEB_LINK: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_APPROVAL_NUMBER_CONFIRMATION: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_AUTO_DNCL_ADD: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DEFAULT_CALLER_ID: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DEFAULT_COUNTRY: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DISPLAY_COUNTRY_SELECT_MENU: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DEFAULT_CALLER_ID_COUNTRY: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DISPLAY_CALLER_ID_COUNTRY_SELECT_MENU: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DISPLAY_OUTBOUND_NUMBER_PHONE_BOOK: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_DISPLAY_PHONE_BOOK: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_NUMBER_WHITE_LIST: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_OVERRIDE_CELL_SCRUB: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_OVERRIDE_RECORDING_SETTINGS: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_SCRUB_OVERRIDE: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_TIMEZONE_OVERRIDE: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_DIAL_USER_EDITABLE_CALLER_ID: _ClassVar[HuntGroupParamKey.Enum]
        MANUAL_QUEUE_CONFIGURATION_NAME: _ClassVar[HuntGroupParamKey.Enum]
        MINIMUM_AGENT_PASSWORD_LENGTH: _ClassVar[HuntGroupParamKey.Enum]
        PHONE_NUMBER_ACTIVITY_EDIT_RESPONSES: _ClassVar[HuntGroupParamKey.Enum]
        PHONE_NUMBER_ACTIVITY_RECORDINGS_DOWNLOAD: _ClassVar[HuntGroupParamKey.Enum]
        PREVIEW_DIAL_AUTO_DNCL_ADD: _ClassVar[HuntGroupParamKey.Enum]
        PREVIEW_DIAL_CALL_TIMEOUT: _ClassVar[HuntGroupParamKey.Enum]
        PREVIEW_DIAL_CONFIRMATION: _ClassVar[HuntGroupParamKey.Enum]
        PREVIEW_QUEUE_CONFIGURATION_NAME: _ClassVar[HuntGroupParamKey.Enum]
        RECORDING_DELAY: _ClassVar[HuntGroupParamKey.Enum]
        REQUEUE_TRANSFER_QUEUE_CONFIGURATION_NAME: _ClassVar[HuntGroupParamKey.Enum]
        SCHEDULED_CALLBACKS_RETRIEVAL_MODE: _ClassVar[HuntGroupParamKey.Enum]
        SCHEDULED_CALLBACK_ROUTING_DISALLOWED: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DEFAULT_CALLER_ID: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DEFAULT_COUNTRY: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DEFAULT_TRANSFER_NUMBER: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DISPLAY_CALLER_ID_PHONE_BOOK: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DISPLAY_COUNTRY_SELECT_MENU: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_DISPLAY_TRANSFER_NUMBER_PHONE_BOOK: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_HAND_OFF_TYPE: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_TRANSFER_TYPE: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_USER_EDITABLE_CALLER_ID: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_CALLS_USER_EDITABLE_TRANSFER_NUMBER: _ClassVar[HuntGroupParamKey.Enum]
        TRANSFER_RECORDING_STATUS: _ClassVar[HuntGroupParamKey.Enum]
        USE_ADVANCED_GATEWAY_TITLE: _ClassVar[HuntGroupParamKey.Enum]
        USE_AGENT_PAUSE_CODES: _ClassVar[HuntGroupParamKey.Enum]
        USE_IP_BASED_AUTH: _ClassVar[HuntGroupParamKey.Enum]
        HUNT_GROUP_REASSIGNMENT_DISALLOWED: _ClassVar[HuntGroupParamKey.Enum]
        REQUEUE_TRANSFER_DISALLOWED_SKILLS: _ClassVar[HuntGroupParamKey.Enum]
        ALLOW_MANUAL_APPROVAL_FOR_MESSAGING: _ClassVar[HuntGroupParamKey.Enum]
        DISPLAY_SKILLS: _ClassVar[HuntGroupParamKey.Enum]
        PBX_TRANSFER_DISALLOWED_EXTENSIONS: _ClassVar[HuntGroupParamKey.Enum]
    AGENT_DIAL_IN_NUMBER: HuntGroupParamKey.Enum
    AGENT_LOGIN_GUI_STATISTICS_TEMPLATE: HuntGroupParamKey.Enum
    AGENT_PASSWORD_REQUIRES_LETTER: HuntGroupParamKey.Enum
    AGENT_PASSWORD_REQUIRES_NUMBER: HuntGroupParamKey.Enum
    AGENT_PASSWORD_REQUIRES_SYMBOL: HuntGroupParamKey.Enum
    AGENT_PASSWORD_REQUIRES_UPPER_LOWER: HuntGroupParamKey.Enum
    AGENT_SKILLS_REASSIGNMENT: HuntGroupParamKey.Enum
    AGENT_STATS_CALL_HISTORY: HuntGroupParamKey.Enum
    AGENT_TRIGGER: HuntGroupParamKey.Enum
    AGENT_DISPOSITION_CONDITIONAL_DNCL: HuntGroupParamKey.Enum
    ALLOWED_IPS: HuntGroupParamKey.Enum
    ALLOW_AGENT_HOLD: HuntGroupParamKey.Enum
    ALLOW_AGENT_INTERCOM: HuntGroupParamKey.Enum
    ALLOW_AGENT_PASSWORD_RESET: HuntGroupParamKey.Enum
    ALLOW_AGENT_PAUSE_CODE_RESET: HuntGroupParamKey.Enum
    ALLOW_AGENT_TO_PAUSE: HuntGroupParamKey.Enum
    ALLOW_CALLBACK_SCHEDULING: HuntGroupParamKey.Enum
    ALLOW_EXPORT_PHONE_NUMBER_ACTIVITY: HuntGroupParamKey.Enum
    ALLOW_MANUAL_APPROVAL_OF_CALLS: HuntGroupParamKey.Enum
    ALLOW_MANUAL_DIALING: HuntGroupParamKey.Enum
    ALLOW_PHONE_NUMBER_ACTIVITY: HuntGroupParamKey.Enum
    ALLOW_PREVIEW_DIAL_CANCEL: HuntGroupParamKey.Enum
    ALLOW_SCHEDULED_CALLBACK_CALLING: HuntGroupParamKey.Enum
    ALLOW_TRANSFER_CALLS: HuntGroupParamKey.Enum
    ALPHANUMERIC_KEYPAD: HuntGroupParamKey.Enum
    AUTO_PAUSE_ON_MULTI_HOLD: HuntGroupParamKey.Enum
    AUTO_PAUSE_ON_PREVIEW_CANCEL: HuntGroupParamKey.Enum
    DEFAULT_AGENT_PAUSE_CODE: HuntGroupParamKey.Enum
    DEFAULT_AGENT_TRANSFERS_FILTERING: HuntGroupParamKey.Enum
    DEFAULT_DNCL_COUNTRY: HuntGroupParamKey.Enum
    DEFAULT_DNCL_EXPIRATION: HuntGroupParamKey.Enum
    DEFAULT_INBOUND_CALL_DNCL_EXPIRATION: HuntGroupParamKey.Enum
    DEFAULT_MANUAL_CALL_DNCL_EXPIRATION: HuntGroupParamKey.Enum
    DEFAULT_OUTBOUND_CALL_DNCL_EXPIRATION: HuntGroupParamKey.Enum
    DEFAULT_PREVIEW_CALL_DNCL_EXPIRATION: HuntGroupParamKey.Enum
    DEFAULT_SCHEDULED_CALLBACK_ROUTING: HuntGroupParamKey.Enum
    DISCONNECT_CALL_CONFIRMATION: HuntGroupParamKey.Enum
    DISPLAY_AGENT_TRANSFERS_FILTERING: HuntGroupParamKey.Enum
    DISPLAY_DATA_COLLECT_DATA: HuntGroupParamKey.Enum
    DISPLAY_DATA_DIPPED_DATA: HuntGroupParamKey.Enum
    DISPLAY_IVR_KEYS_PRESSED: HuntGroupParamKey.Enum
    DISPLAY_PHONE_ZIP_METADATA: HuntGroupParamKey.Enum
    DISPLAY_RECORDING_INDICATOR: HuntGroupParamKey.Enum
    DO_ALLOW_ADD_DNCL: HuntGroupParamKey.Enum
    ENABLE_RECORDING_PAUSE: HuntGroupParamKey.Enum
    HOLD_QUEUE_MONITORING: HuntGroupParamKey.Enum
    HOLD_QUEUE_MONITORING_AGENT_ROUTING: HuntGroupParamKey.Enum
    HOLD_QUEUE_MONITORING_PREFERRED_HUNT_GROUP_ROUTING: HuntGroupParamKey.Enum
    HOLD_QUEUE_MONITORING_REQUIRED_HUNT_GROUP_ROUTING: HuntGroupParamKey.Enum
    HUNT_GROUP_CLIENT_INFO_DISPLAY_TEMPLATE: HuntGroupParamKey.Enum
    HUNT_GROUP_SCRIPT: HuntGroupParamKey.Enum
    HUNT_GROUP_WEB_LINK: HuntGroupParamKey.Enum
    MANUAL_APPROVAL_NUMBER_CONFIRMATION: HuntGroupParamKey.Enum
    MANUAL_DIAL_AUTO_DNCL_ADD: HuntGroupParamKey.Enum
    MANUAL_DIAL_DEFAULT_CALLER_ID: HuntGroupParamKey.Enum
    MANUAL_DIAL_DEFAULT_COUNTRY: HuntGroupParamKey.Enum
    MANUAL_DIAL_DISPLAY_COUNTRY_SELECT_MENU: HuntGroupParamKey.Enum
    MANUAL_DIAL_DEFAULT_CALLER_ID_COUNTRY: HuntGroupParamKey.Enum
    MANUAL_DIAL_DISPLAY_CALLER_ID_COUNTRY_SELECT_MENU: HuntGroupParamKey.Enum
    MANUAL_DIAL_DISPLAY_OUTBOUND_NUMBER_PHONE_BOOK: HuntGroupParamKey.Enum
    MANUAL_DIAL_DISPLAY_PHONE_BOOK: HuntGroupParamKey.Enum
    MANUAL_DIAL_NUMBER_WHITE_LIST: HuntGroupParamKey.Enum
    MANUAL_DIAL_OVERRIDE_CELL_SCRUB: HuntGroupParamKey.Enum
    MANUAL_DIAL_OVERRIDE_RECORDING_SETTINGS: HuntGroupParamKey.Enum
    MANUAL_DIAL_SCRUB_OVERRIDE: HuntGroupParamKey.Enum
    MANUAL_DIAL_TIMEZONE_OVERRIDE: HuntGroupParamKey.Enum
    MANUAL_DIAL_USER_EDITABLE_CALLER_ID: HuntGroupParamKey.Enum
    MANUAL_QUEUE_CONFIGURATION_NAME: HuntGroupParamKey.Enum
    MINIMUM_AGENT_PASSWORD_LENGTH: HuntGroupParamKey.Enum
    PHONE_NUMBER_ACTIVITY_EDIT_RESPONSES: HuntGroupParamKey.Enum
    PHONE_NUMBER_ACTIVITY_RECORDINGS_DOWNLOAD: HuntGroupParamKey.Enum
    PREVIEW_DIAL_AUTO_DNCL_ADD: HuntGroupParamKey.Enum
    PREVIEW_DIAL_CALL_TIMEOUT: HuntGroupParamKey.Enum
    PREVIEW_DIAL_CONFIRMATION: HuntGroupParamKey.Enum
    PREVIEW_QUEUE_CONFIGURATION_NAME: HuntGroupParamKey.Enum
    RECORDING_DELAY: HuntGroupParamKey.Enum
    REQUEUE_TRANSFER_QUEUE_CONFIGURATION_NAME: HuntGroupParamKey.Enum
    SCHEDULED_CALLBACKS_RETRIEVAL_MODE: HuntGroupParamKey.Enum
    SCHEDULED_CALLBACK_ROUTING_DISALLOWED: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DEFAULT_CALLER_ID: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DEFAULT_COUNTRY: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DEFAULT_TRANSFER_NUMBER: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DISPLAY_CALLER_ID_PHONE_BOOK: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DISPLAY_COUNTRY_SELECT_MENU: HuntGroupParamKey.Enum
    TRANSFER_CALLS_DISPLAY_TRANSFER_NUMBER_PHONE_BOOK: HuntGroupParamKey.Enum
    TRANSFER_CALLS_HAND_OFF_TYPE: HuntGroupParamKey.Enum
    TRANSFER_CALLS_TRANSFER_TYPE: HuntGroupParamKey.Enum
    TRANSFER_CALLS_USER_EDITABLE_CALLER_ID: HuntGroupParamKey.Enum
    TRANSFER_CALLS_USER_EDITABLE_TRANSFER_NUMBER: HuntGroupParamKey.Enum
    TRANSFER_RECORDING_STATUS: HuntGroupParamKey.Enum
    USE_ADVANCED_GATEWAY_TITLE: HuntGroupParamKey.Enum
    USE_AGENT_PAUSE_CODES: HuntGroupParamKey.Enum
    USE_IP_BASED_AUTH: HuntGroupParamKey.Enum
    HUNT_GROUP_REASSIGNMENT_DISALLOWED: HuntGroupParamKey.Enum
    REQUEUE_TRANSFER_DISALLOWED_SKILLS: HuntGroupParamKey.Enum
    ALLOW_MANUAL_APPROVAL_FOR_MESSAGING: HuntGroupParamKey.Enum
    DISPLAY_SKILLS: HuntGroupParamKey.Enum
    PBX_TRANSFER_DISALLOWED_EXTENSIONS: HuntGroupParamKey.Enum
    def __init__(self) -> None: ...

class ReplaceConfig(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHANGE: _ClassVar[ReplaceConfig.Enum]
        TENANT: _ClassVar[ReplaceConfig.Enum]
        REPLACE: _ClassVar[ReplaceConfig.Enum]
    NO_CHANGE: ReplaceConfig.Enum
    TENANT: ReplaceConfig.Enum
    REPLACE: ReplaceConfig.Enum
    def __init__(self) -> None: ...

class TransferMember(_message.Message):
    __slots__ = ("identifier", "display_label", "member_type", "agent_session", "caller_sid", "outbound_id")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_ID_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    display_label: str
    member_type: TransferMemberType
    agent_session: AgentSession
    caller_sid: CallerSid
    outbound_id: str
    def __init__(self, identifier: _Optional[str] = ..., display_label: _Optional[str] = ..., member_type: _Optional[_Union[TransferMemberType, str]] = ..., agent_session: _Optional[_Union[AgentSession, _Mapping]] = ..., caller_sid: _Optional[_Union[CallerSid, _Mapping]] = ..., outbound_id: _Optional[str] = ...) -> None: ...

class AgentAlert(_message.Message):
    __slots__ = ("backoffice_message", "directed_call_ringing", "directed_call_hangup")
    BACKOFFICE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_CALL_RINGING_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_CALL_HANGUP_FIELD_NUMBER: _ClassVar[int]
    backoffice_message: AgentBackofficeMessageAlert
    directed_call_ringing: AgentDirectedCallRingingAlert
    directed_call_hangup: AgentDirectedCallHangupAlert
    def __init__(self, backoffice_message: _Optional[_Union[AgentBackofficeMessageAlert, _Mapping]] = ..., directed_call_ringing: _Optional[_Union[AgentDirectedCallRingingAlert, _Mapping]] = ..., directed_call_hangup: _Optional[_Union[AgentDirectedCallHangupAlert, _Mapping]] = ...) -> None: ...

class AgentBackofficeMessageAlert(_message.Message):
    __slots__ = ("expire_duration", "timestamp", "target_agent_session", "message", "id")
    EXPIRE_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    expire_duration: int
    timestamp: _timestamp_pb2.Timestamp
    target_agent_session: AgentSession
    message: str
    id: str
    def __init__(self, expire_duration: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target_agent_session: _Optional[_Union[AgentSession, _Mapping]] = ..., message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AgentDirectedCallRingingAlert(_message.Message):
    __slots__ = ("expire_duration", "timestamp", "target_agent_session", "caller_sid", "caller_id", "destination_number", "id")
    EXPIRE_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    expire_duration: int
    timestamp: _timestamp_pb2.Timestamp
    target_agent_session: AgentSession
    caller_sid: CallerSid
    caller_id: str
    destination_number: str
    id: str
    def __init__(self, expire_duration: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target_agent_session: _Optional[_Union[AgentSession, _Mapping]] = ..., caller_sid: _Optional[_Union[CallerSid, _Mapping]] = ..., caller_id: _Optional[str] = ..., destination_number: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AgentDirectedCallHangupAlert(_message.Message):
    __slots__ = ("expire_duration", "timestamp", "target_agent_session", "caller_sid", "id")
    EXPIRE_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    CALLER_SID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    expire_duration: int
    timestamp: _timestamp_pb2.Timestamp
    target_agent_session: AgentSession
    caller_sid: CallerSid
    id: str
    def __init__(self, expire_duration: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target_agent_session: _Optional[_Union[AgentSession, _Mapping]] = ..., caller_sid: _Optional[_Union[CallerSid, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class AgentState(_message.Message):
    __slots__ = ("status", "status_desc", "paused", "queue", "current_session_id", "last_status_change", "monitoring", "calls_count", "last_sip_code", "agent_peer_is_lost_call", "disabled", "caller_was_suspended", "transfer_members", "agent_peer_is_direct_to_agent", "user_id", "agent_sid", "asm_session_sid", "agent_is_muted", "uuid")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DESC_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    CALLS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_SIP_CODE_FIELD_NUMBER: _ClassVar[int]
    AGENT_PEER_IS_LOST_CALL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CALLER_WAS_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PEER_IS_DIRECT_TO_AGENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    ASM_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    status: int
    status_desc: AgentStatus.Enum
    paused: bool
    queue: str
    current_session_id: int
    last_status_change: int
    monitoring: bool
    calls_count: int
    last_sip_code: int
    agent_peer_is_lost_call: bool
    disabled: bool
    caller_was_suspended: bool
    transfer_members: _containers.RepeatedCompositeFieldContainer[TransferMember]
    agent_peer_is_direct_to_agent: bool
    user_id: str
    agent_sid: int
    asm_session_sid: int
    agent_is_muted: bool
    uuid: str
    def __init__(self, status: _Optional[int] = ..., status_desc: _Optional[_Union[AgentStatus.Enum, str]] = ..., paused: bool = ..., queue: _Optional[str] = ..., current_session_id: _Optional[int] = ..., last_status_change: _Optional[int] = ..., monitoring: bool = ..., calls_count: _Optional[int] = ..., last_sip_code: _Optional[int] = ..., agent_peer_is_lost_call: bool = ..., disabled: bool = ..., caller_was_suspended: bool = ..., transfer_members: _Optional[_Iterable[_Union[TransferMember, _Mapping]]] = ..., agent_peer_is_direct_to_agent: bool = ..., user_id: _Optional[str] = ..., agent_sid: _Optional[int] = ..., asm_session_sid: _Optional[int] = ..., agent_is_muted: bool = ..., uuid: _Optional[str] = ...) -> None: ...
