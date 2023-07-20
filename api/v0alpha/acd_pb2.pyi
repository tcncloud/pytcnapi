from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentGetStatusRequest(_message.Message):
    __slots__ = ["session_sid", "perform_keep_alive"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    perform_keep_alive: bool
    def __init__(self, session_sid: _Optional[int] = ..., perform_keep_alive: bool = ...) -> None: ...

class AgentGetStatusReply(_message.Message):
    __slots__ = ["status", "status_desc", "paused", "queue", "current_session_id", "last_status_change", "monitoring", "calls_count", "last_sip_code", "agent_peer_is_lost_call", "disabled", "keep_alive_succeeded", "transfer_members", "agent_is_muted"]
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
    KEEP_ALIVE_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    AGENT_IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    status: int
    status_desc: _acd_pb2.AgentStatus.Enum
    paused: bool
    queue: str
    current_session_id: int
    last_status_change: int
    monitoring: bool
    calls_count: int
    last_sip_code: int
    agent_peer_is_lost_call: bool
    disabled: bool
    keep_alive_succeeded: bool
    transfer_members: _containers.RepeatedCompositeFieldContainer[_acd_pb2.TransferMember]
    agent_is_muted: bool
    def __init__(self, status: _Optional[int] = ..., status_desc: _Optional[_Union[_acd_pb2.AgentStatus.Enum, str]] = ..., paused: bool = ..., queue: _Optional[str] = ..., current_session_id: _Optional[int] = ..., last_status_change: _Optional[int] = ..., monitoring: bool = ..., calls_count: _Optional[int] = ..., last_sip_code: _Optional[int] = ..., agent_peer_is_lost_call: bool = ..., disabled: bool = ..., keep_alive_succeeded: bool = ..., transfer_members: _Optional[_Iterable[_Union[_acd_pb2.TransferMember, _Mapping]]] = ..., agent_is_muted: bool = ...) -> None: ...

class AgentGetConnectedPartyRequest(_message.Message):
    __slots__ = ["session_sid", "user_id"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    user_id: str
    def __init__(self, session_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class AgentGetConnectedPartyReply(_message.Message):
    __slots__ = ["call_id", "call_type"]
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class ManagerAgentGetConnectedPartyRequest(_message.Message):
    __slots__ = ["session_sid", "user_id"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    user_id: str
    def __init__(self, session_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class ManagerAgentGetConnectedPartyReply(_message.Message):
    __slots__ = ["call_id", "call_type"]
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class AgentIntercomRequest(_message.Message):
    __slots__ = ["target_agent_id", "session_sid"]
    TARGET_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    target_agent_id: int
    session_sid: int
    def __init__(self, target_agent_id: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentIntercomAcceptRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomAcceptReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentIntercomRejectRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomRejectReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentIntercomCancelRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomCancelReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DialManualPrepareRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialManualPrepareReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DialManualCancelRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialManualCancelReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DialPreviewPrepareRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialPreviewPrepareReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentPauseRequest(_message.Message):
    __slots__ = ["session_sid", "reason"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class AgentPauseReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentSetReadyRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentSetReadyReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentGUIBusyRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentGUIBusyReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentDisconnectRequest(_message.Message):
    __slots__ = ["reason", "session_sid"]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    reason: str
    session_sid: int
    def __init__(self, reason: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentDisconnectReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentSessionEventReq(_message.Message):
    __slots__ = ["agent_session_sid", "action_key", "action_value"]
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    action_key: _acd_pb2.AgentSessionLogActionKey.Enum
    action_value: str
    def __init__(self, agent_session_sid: _Optional[int] = ..., action_key: _Optional[_Union[_acd_pb2.AgentSessionLogActionKey.Enum, str]] = ..., action_value: _Optional[str] = ...) -> None: ...

class AgentSessionEventRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CallerRequeueRequest(_message.Message):
    __slots__ = ["new_config_folder", "skills", "replace_skills", "replace_config", "session_sid", "voicemail_box"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    NEW_CONFIG_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_SKILLS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VOICEMAIL_BOX_FIELD_NUMBER: _ClassVar[int]
    new_config_folder: str
    skills: _containers.ScalarMap[str, bool]
    replace_skills: bool
    replace_config: _acd_pb2.ReplaceConfig.Enum
    session_sid: int
    voicemail_box: str
    def __init__(self, new_config_folder: _Optional[str] = ..., skills: _Optional[_Mapping[str, bool]] = ..., replace_skills: bool = ..., replace_config: _Optional[_Union[_acd_pb2.ReplaceConfig.Enum, str]] = ..., session_sid: _Optional[int] = ..., voicemail_box: _Optional[str] = ...) -> None: ...

class CallerRequeueReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToAgentCancelRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToAgentCancelReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToOutboundCancelRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToOutboundCancelReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToAgentApproveRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToAgentApproveReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToOutboundApproveRequest(_message.Message):
    __slots__ = ["session_sid", "member_identifiers"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifiers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_sid: _Optional[int] = ..., member_identifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class TransferWarmToOutboundApproveReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CallerSendToVoicemailRequest(_message.Message):
    __slots__ = ["mailbox", "session_sid"]
    MAILBOX_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    mailbox: str
    session_sid: int
    def __init__(self, mailbox: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class CallerSendToVoicemailReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentInviteTransferCallerToConferenceRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentInviteTransferCallerToConferenceReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentMonitorCallsRequest(_message.Message):
    __slots__ = ["monitor", "session_sid"]
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    monitor: bool
    session_sid: int
    def __init__(self, monitor: bool = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentMonitorCallsReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferColdToOutboundRequest(_message.Message):
    __slots__ = ["caller_id", "destination", "reserved_carriers", "session_sid"]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CARRIERS_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    destination: str
    reserved_carriers: _containers.RepeatedScalarFieldContainer[str]
    session_sid: int
    def __init__(self, caller_id: _Optional[str] = ..., destination: _Optional[str] = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class TransferColdToOutboundReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferColdToAgentRequest(_message.Message):
    __slots__ = ["destination_agent_id", "session_sid"]
    DESTINATION_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    destination_agent_id: int
    session_sid: int
    def __init__(self, destination_agent_id: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class TransferColdToAgentReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToOutboundStartRequest(_message.Message):
    __slots__ = ["caller_id", "destination", "reserved_carriers", "caller_hold", "session_sid"]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CARRIERS_FIELD_NUMBER: _ClassVar[int]
    CALLER_HOLD_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    destination: str
    reserved_carriers: _containers.RepeatedScalarFieldContainer[str]
    caller_hold: bool
    session_sid: int
    def __init__(self, caller_id: _Optional[str] = ..., destination: _Optional[str] = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., caller_hold: bool = ..., session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToOutboundStartReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateWarmOutboundTransferMemberRequest(_message.Message):
    __slots__ = ["caller_id", "destination", "reserved_carriers", "session_sid"]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    RESERVED_CARRIERS_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    destination: str
    reserved_carriers: _containers.RepeatedScalarFieldContainer[str]
    session_sid: int
    def __init__(self, caller_id: _Optional[str] = ..., destination: _Optional[str] = ..., reserved_carriers: _Optional[_Iterable[str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class CreateWarmOutboundTransferMemberReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveTransferMemberRequest(_message.Message):
    __slots__ = ["member_identifier", "session_sid"]
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    member_identifier: str
    session_sid: int
    def __init__(self, member_identifier: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class RemoveTransferMemberReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransferWarmToAgentStartRequest(_message.Message):
    __slots__ = ["destination_agent_id", "caller_hold", "session_sid", "skills"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    DESTINATION_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_HOLD_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    destination_agent_id: int
    caller_hold: bool
    session_sid: int
    skills: _containers.ScalarMap[str, bool]
    def __init__(self, destination_agent_id: _Optional[int] = ..., caller_hold: bool = ..., session_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class TransferWarmToAgentStartReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentGetCallFromHoldRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentGetCallFromHoldReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentGetSpecificCallFromHoldRequest(_message.Message):
    __slots__ = ["call_id", "call_type", "session_sid"]
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    session_sid: int
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentGetSpecificCallFromHoldReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentPutCallOnHoldRequest(_message.Message):
    __slots__ = ["hold_type", "session_sid"]
    HOLD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    hold_type: _acd_pb2.HoldType
    session_sid: int
    def __init__(self, hold_type: _Optional[_Union[_acd_pb2.HoldType, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentPutCallOnHoldReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ACDGetAllAgentsStatusesRequest(_message.Message):
    __slots__ = ["skills", "all_skills_required"]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ALL_SKILLS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedScalarFieldContainer[str]
    all_skills_required: bool
    def __init__(self, skills: _Optional[_Iterable[str]] = ..., all_skills_required: bool = ...) -> None: ...

class AgentStatusDetails(_message.Message):
    __slots__ = ["sid", "current_session_id", "status", "status_desc", "user_id"]
    SID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DESC_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    sid: int
    current_session_id: int
    status: int
    status_desc: _acd_pb2.AgentStatus.Enum
    user_id: str
    def __init__(self, sid: _Optional[int] = ..., current_session_id: _Optional[int] = ..., status: _Optional[int] = ..., status_desc: _Optional[_Union[_acd_pb2.AgentStatus.Enum, str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class ACDGetAllAgentsStatusesReply(_message.Message):
    __slots__ = ["agent_status_details"]
    AGENT_STATUS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    agent_status_details: _containers.RepeatedCompositeFieldContainer[AgentStatusDetails]
    def __init__(self, agent_status_details: _Optional[_Iterable[_Union[AgentStatusDetails, _Mapping]]] = ...) -> None: ...

class AgentReceiveMessageRequest(_message.Message):
    __slots__ = ["minimum_timestamp", "session_sid"]
    MINIMUM_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    minimum_timestamp: int
    session_sid: int
    def __init__(self, minimum_timestamp: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentReceiveMessageReply(_message.Message):
    __slots__ = ["message", "timestamp"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: int
    def __init__(self, message: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AgentPBXRejectCallRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentPBXRejectCallReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentPBXApproveCallRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentPBXApproveCallReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCallerLostPeerRequest(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class GetCallerLostPeerReply(_message.Message):
    __slots__ = ["hunt_group_sid"]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class CallerGetRawEventRequest(_message.Message):
    __slots__ = ["call_sid", "call_type"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class CallerGetRawEventReply(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: CallerEvent
    def __init__(self, event: _Optional[_Union[CallerEvent, _Mapping]] = ...) -> None: ...

class CallerEvent(_message.Message):
    __slots__ = ["skills", "allSkills"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class AllSkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ALLSKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.ScalarMap[str, bool]
    allSkills: _containers.ScalarMap[str, bool]
    def __init__(self, skills: _Optional[_Mapping[str, bool]] = ..., allSkills: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class PeerAgentWithCallerRequest(_message.Message):
    __slots__ = ["call_sid", "call_type", "session_sid"]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    session_sid: int
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class PeerAgentWithCallerReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HoldTransferMemberReq(_message.Message):
    __slots__ = ["session_sid", "member_identifier"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifier: str
    def __init__(self, session_sid: _Optional[int] = ..., member_identifier: _Optional[str] = ...) -> None: ...

class HoldTransferMemberRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnholdTransferMemberReq(_message.Message):
    __slots__ = ["session_sid", "member_identifier"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifier: str
    def __init__(self, session_sid: _Optional[int] = ..., member_identifier: _Optional[str] = ...) -> None: ...

class UnholdTransferMemberRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAgentCallCountsReq(_message.Message):
    __slots__ = ["agent_skills", "agent_pbx_extensions"]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    agent_skills: _containers.RepeatedScalarFieldContainer[str]
    agent_pbx_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_skills: _Optional[_Iterable[str]] = ..., agent_pbx_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAgentCallCountsRes(_message.Message):
    __slots__ = ["agent_calls", "skill_calls", "on_hold_calls"]
    AGENT_CALLS_FIELD_NUMBER: _ClassVar[int]
    SKILL_CALLS_FIELD_NUMBER: _ClassVar[int]
    ON_HOLD_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_calls: int
    skill_calls: int
    on_hold_calls: int
    def __init__(self, agent_calls: _Optional[int] = ..., skill_calls: _Optional[int] = ..., on_hold_calls: _Optional[int] = ...) -> None: ...

class WarmCallerTransferStartReq(_message.Message):
    __slots__ = ["session_sid", "call_sid", "call_type", "caller_hold"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLER_HOLD_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    caller_hold: bool
    def __init__(self, session_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., caller_hold: bool = ...) -> None: ...

class WarmCallerTransferStartRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WarmCallerTransferCancelReq(_message.Message):
    __slots__ = ["session_sid", "reason"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class WarmCallerTransferCancelRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WarmCallerTransferApproveReq(_message.Message):
    __slots__ = ["session_sid", "reason"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class WarmCallerTransferApproveRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlaySoundboardEntityReq(_message.Message):
    __slots__ = ["session_sid", "soundboard_entity_id"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SOUNDBOARD_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    soundboard_entity_id: int
    def __init__(self, session_sid: _Optional[int] = ..., soundboard_entity_id: _Optional[int] = ...) -> None: ...

class PlaySoundboardEntityRes(_message.Message):
    __slots__ = ["sound_instance_id"]
    SOUND_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    sound_instance_id: str
    def __init__(self, sound_instance_id: _Optional[str] = ...) -> None: ...

class StopSoundboardEntityReq(_message.Message):
    __slots__ = ["session_sid", "sound_instance_id"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SOUND_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    sound_instance_id: str
    def __init__(self, session_sid: _Optional[int] = ..., sound_instance_id: _Optional[str] = ...) -> None: ...

class StopSoundboardEntityRes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAgentSkillsRequest(_message.Message):
    __slots__ = ["session_sid", "skills", "replace_skills"]
    class SkillsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_SKILLS_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    skills: _containers.ScalarMap[str, int]
    replace_skills: bool
    def __init__(self, session_sid: _Optional[int] = ..., skills: _Optional[_Mapping[str, int]] = ..., replace_skills: bool = ...) -> None: ...

class UpdateAgentSkillsReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlayDTMFRequest(_message.Message):
    __slots__ = ["session_sid", "dtmf_digits"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    DTMF_DIGITS_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    dtmf_digits: _containers.RepeatedScalarFieldContainer[_acd_pb2.DTMFDigit]
    def __init__(self, session_sid: _Optional[int] = ..., dtmf_digits: _Optional[_Iterable[_Union[_acd_pb2.DTMFDigit, str]]] = ...) -> None: ...

class PlayDTMFReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentMuteRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentMuteReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AgentUnmuteRequest(_message.Message):
    __slots__ = ["session_sid"]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentUnmuteReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
