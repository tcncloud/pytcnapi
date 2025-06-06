from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons.integrations import integrations_pb2 as _integrations_pb2
from api.v1alpha1.integrations import service_pb2 as _service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentGetStatusRequest(_message.Message):
    __slots__ = ("session_sid", "perform_keep_alive")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    PERFORM_KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    perform_keep_alive: bool
    def __init__(self, session_sid: _Optional[int] = ..., perform_keep_alive: bool = ...) -> None: ...

class AgentGetStatusReply(_message.Message):
    __slots__ = ("status", "status_desc", "paused", "queue", "current_session_id", "last_status_change", "monitoring", "calls_count", "last_sip_code", "agent_peer_is_lost_call", "disabled", "keep_alive_succeeded", "transfer_members", "agent_is_muted")
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
    __slots__ = ("session_sid", "user_id")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    user_id: str
    def __init__(self, session_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class AgentGetConnectedPartyReply(_message.Message):
    __slots__ = ("call_id", "call_type")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class ManagerAgentGetConnectedPartyRequest(_message.Message):
    __slots__ = ("session_sid", "user_id")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    user_id: str
    def __init__(self, session_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class ManagerAgentGetConnectedPartyReply(_message.Message):
    __slots__ = ("call_id", "call_type")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class AgentIntercomRequest(_message.Message):
    __slots__ = ("target_agent_id", "session_sid")
    TARGET_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    target_agent_id: int
    session_sid: int
    def __init__(self, target_agent_id: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentIntercomAcceptRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomAcceptReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentIntercomRejectRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomRejectReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentIntercomCancelRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentIntercomCancelReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DialManualPrepareRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialManualPrepareReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DialManualCancelRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialManualCancelReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DialPreviewPrepareRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class DialPreviewPrepareReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentPauseRequest(_message.Message):
    __slots__ = ("session_sid", "reason")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class AgentPauseReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentSetReadyRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentSetReadyReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentGUIBusyRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentGUIBusyReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentDisconnectRequest(_message.Message):
    __slots__ = ("reason", "session_sid")
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    reason: str
    session_sid: int
    def __init__(self, reason: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentDisconnectReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentSessionEventReq(_message.Message):
    __slots__ = ("agent_session_sid", "action_key", "action_value")
    AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ACTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    agent_session_sid: int
    action_key: _acd_pb2.AgentSessionLogActionKey.Enum
    action_value: str
    def __init__(self, agent_session_sid: _Optional[int] = ..., action_key: _Optional[_Union[_acd_pb2.AgentSessionLogActionKey.Enum, str]] = ..., action_value: _Optional[str] = ...) -> None: ...

class AgentSessionEventRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallerRequeueRequest(_message.Message):
    __slots__ = ("new_config_folder", "skills", "replace_skills", "replace_config", "session_sid", "voicemail_box")
    class SkillsEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToAgentCancelRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToAgentCancelReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToOutboundCancelRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToOutboundCancelReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToAgentApproveRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class TransferWarmToAgentApproveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToOutboundApproveRequest(_message.Message):
    __slots__ = ("session_sid", "member_identifiers")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifiers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_sid: _Optional[int] = ..., member_identifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class TransferWarmToOutboundApproveReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallerSendToVoicemailRequest(_message.Message):
    __slots__ = ("mailbox", "session_sid")
    MAILBOX_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    mailbox: str
    session_sid: int
    def __init__(self, mailbox: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class CallerSendToVoicemailReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentInviteTransferCallerToConferenceRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentInviteTransferCallerToConferenceReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentMonitorCallsRequest(_message.Message):
    __slots__ = ("monitor", "session_sid")
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    monitor: bool
    session_sid: int
    def __init__(self, monitor: bool = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentMonitorCallsReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferColdToOutboundRequest(_message.Message):
    __slots__ = ("caller_id", "destination", "reserved_carriers", "session_sid")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferColdToAgentRequest(_message.Message):
    __slots__ = ("destination_agent_id", "session_sid")
    DESTINATION_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    destination_agent_id: int
    session_sid: int
    def __init__(self, destination_agent_id: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class TransferColdToAgentReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToOutboundStartRequest(_message.Message):
    __slots__ = ("caller_id", "destination", "reserved_carriers", "caller_hold", "session_sid")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateWarmOutboundTransferMemberRequest(_message.Message):
    __slots__ = ("caller_id", "destination", "reserved_carriers", "session_sid")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveTransferMemberRequest(_message.Message):
    __slots__ = ("member_identifier", "session_sid")
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    member_identifier: str
    session_sid: int
    def __init__(self, member_identifier: _Optional[str] = ..., session_sid: _Optional[int] = ...) -> None: ...

class RemoveTransferMemberReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferWarmToAgentStartRequest(_message.Message):
    __slots__ = ("destination_agent_id", "caller_hold", "session_sid", "skills")
    class SkillsEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentGetCallFromHoldRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentGetCallFromHoldReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentGetSpecificCallFromHoldRequest(_message.Message):
    __slots__ = ("call_id", "call_type", "session_sid")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    call_id: int
    call_type: _acd_pb2.CallType.Enum
    session_sid: int
    def __init__(self, call_id: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentGetSpecificCallFromHoldReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentPutCallOnHoldRequest(_message.Message):
    __slots__ = ("hold_type", "session_sid")
    HOLD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    hold_type: _acd_pb2.HoldType
    session_sid: int
    def __init__(self, hold_type: _Optional[_Union[_acd_pb2.HoldType, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentPutCallOnHoldReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ACDGetAllAgentsStatusesRequest(_message.Message):
    __slots__ = ("skills", "all_skills_required")
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ALL_SKILLS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedScalarFieldContainer[str]
    all_skills_required: bool
    def __init__(self, skills: _Optional[_Iterable[str]] = ..., all_skills_required: bool = ...) -> None: ...

class AgentStatusDetails(_message.Message):
    __slots__ = ("sid", "current_session_id", "status", "status_desc", "user_id")
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
    __slots__ = ("agent_status_details",)
    AGENT_STATUS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    agent_status_details: _containers.RepeatedCompositeFieldContainer[AgentStatusDetails]
    def __init__(self, agent_status_details: _Optional[_Iterable[_Union[AgentStatusDetails, _Mapping]]] = ...) -> None: ...

class AgentReceiveMessageRequest(_message.Message):
    __slots__ = ("minimum_timestamp", "session_sid")
    MINIMUM_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    minimum_timestamp: int
    session_sid: int
    def __init__(self, minimum_timestamp: _Optional[int] = ..., session_sid: _Optional[int] = ...) -> None: ...

class AgentReceiveMessageReply(_message.Message):
    __slots__ = ("message", "timestamp")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: int
    def __init__(self, message: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class AgentPBXRejectCallRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentPBXRejectCallReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentPBXApproveCallRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentPBXApproveCallReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCallerLostPeerRequest(_message.Message):
    __slots__ = ("call_sid", "call_type")
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class GetCallerLostPeerReply(_message.Message):
    __slots__ = ("hunt_group_sid",)
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    hunt_group_sid: int
    def __init__(self, hunt_group_sid: _Optional[int] = ...) -> None: ...

class CallerGetRawEventRequest(_message.Message):
    __slots__ = ("call_sid", "call_type")
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...

class CallerGetRawEventReply(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: CallerEvent
    def __init__(self, event: _Optional[_Union[CallerEvent, _Mapping]] = ...) -> None: ...

class CallerEvent(_message.Message):
    __slots__ = ("skills", "allSkills")
    class SkillsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class AllSkillsEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ("call_sid", "call_type", "session_sid")
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    session_sid: int
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., session_sid: _Optional[int] = ...) -> None: ...

class PeerAgentWithCallerReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldTransferMemberReq(_message.Message):
    __slots__ = ("session_sid", "member_identifier")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifier: str
    def __init__(self, session_sid: _Optional[int] = ..., member_identifier: _Optional[str] = ...) -> None: ...

class HoldTransferMemberRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnholdTransferMemberReq(_message.Message):
    __slots__ = ("session_sid", "member_identifier")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    member_identifier: str
    def __init__(self, session_sid: _Optional[int] = ..., member_identifier: _Optional[str] = ...) -> None: ...

class UnholdTransferMemberRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAgentCallCountsReq(_message.Message):
    __slots__ = ("agent_skills", "agent_pbx_extensions")
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    agent_skills: _containers.RepeatedScalarFieldContainer[str]
    agent_pbx_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_skills: _Optional[_Iterable[str]] = ..., agent_pbx_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAgentCallCountsRes(_message.Message):
    __slots__ = ("agent_calls", "skill_calls", "on_hold_calls")
    AGENT_CALLS_FIELD_NUMBER: _ClassVar[int]
    SKILL_CALLS_FIELD_NUMBER: _ClassVar[int]
    ON_HOLD_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_calls: int
    skill_calls: int
    on_hold_calls: int
    def __init__(self, agent_calls: _Optional[int] = ..., skill_calls: _Optional[int] = ..., on_hold_calls: _Optional[int] = ...) -> None: ...

class WarmCallerTransferStartReq(_message.Message):
    __slots__ = ("session_sid", "call_sid", "call_type", "caller_hold")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class WarmCallerTransferCancelReq(_message.Message):
    __slots__ = ("session_sid", "reason")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class WarmCallerTransferCancelRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WarmCallerTransferApproveReq(_message.Message):
    __slots__ = ("session_sid", "reason")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    reason: str
    def __init__(self, session_sid: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class WarmCallerTransferApproveRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PlaySoundboardEntityReq(_message.Message):
    __slots__ = ("session_sid", "soundboard_entity_id")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SOUNDBOARD_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    soundboard_entity_id: int
    def __init__(self, session_sid: _Optional[int] = ..., soundboard_entity_id: _Optional[int] = ...) -> None: ...

class PlaySoundboardEntityRes(_message.Message):
    __slots__ = ("sound_instance_id",)
    SOUND_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    sound_instance_id: str
    def __init__(self, sound_instance_id: _Optional[str] = ...) -> None: ...

class StopSoundboardEntityReq(_message.Message):
    __slots__ = ("session_sid", "sound_instance_id")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    SOUND_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    sound_instance_id: str
    def __init__(self, session_sid: _Optional[int] = ..., sound_instance_id: _Optional[str] = ...) -> None: ...

class StopSoundboardEntityRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAgentSkillsRequest(_message.Message):
    __slots__ = ("session_sid", "skills", "replace_skills")
    class SkillsEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ()
    def __init__(self) -> None: ...

class PlayDTMFRequest(_message.Message):
    __slots__ = ("session_sid", "dtmf_digits")
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    DTMF_DIGITS_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    dtmf_digits: _containers.RepeatedScalarFieldContainer[_acd_pb2.DTMFDigit]
    def __init__(self, session_sid: _Optional[int] = ..., dtmf_digits: _Optional[_Iterable[_Union[_acd_pb2.DTMFDigit, str]]] = ...) -> None: ...

class PlayDTMFReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentMuteRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentMuteReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentUnmuteRequest(_message.Message):
    __slots__ = ("session_sid",)
    SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    session_sid: int
    def __init__(self, session_sid: _Optional[int] = ...) -> None: ...

class AgentUnmuteReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartSecureFormReq(_message.Message):
    __slots__ = ("portal_id", "voice_session_sid")
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    portal_id: str
    voice_session_sid: int
    def __init__(self, portal_id: _Optional[str] = ..., voice_session_sid: _Optional[int] = ...) -> None: ...

class StartSecureFormRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CollectSecureFormFieldReq(_message.Message):
    __slots__ = ("field_name", "voice_session_sid")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    voice_session_sid: int
    def __init__(self, field_name: _Optional[str] = ..., voice_session_sid: _Optional[int] = ...) -> None: ...

class CollectSecureFormFieldRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetSecureFormFieldReq(_message.Message):
    __slots__ = ("voice_session_sid",)
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    def __init__(self, voice_session_sid: _Optional[int] = ...) -> None: ...

class ResetSecureFormFieldRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptSecureFormFieldReq(_message.Message):
    __slots__ = ("voice_session_sid",)
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    def __init__(self, voice_session_sid: _Optional[int] = ...) -> None: ...

class AcceptSecureFormFieldRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessSecureFormReq(_message.Message):
    __slots__ = ("values", "portal_id", "segment", "choice", "voice_session_sid")
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _service_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_service_pb2.Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, _service_pb2.Value]
    portal_id: str
    segment: int
    choice: int
    voice_session_sid: int
    def __init__(self, values: _Optional[_Mapping[str, _service_pb2.Value]] = ..., portal_id: _Optional[str] = ..., segment: _Optional[int] = ..., choice: _Optional[int] = ..., voice_session_sid: _Optional[int] = ...) -> None: ...

class ProcessSecureFormRes(_message.Message):
    __slots__ = ("success", "data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _service_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_service_pb2.Value, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: _containers.MessageMap[str, _service_pb2.Value]
    def __init__(self, success: bool = ..., data: _Optional[_Mapping[str, _service_pb2.Value]] = ...) -> None: ...

class FinishSecureFormHandlingReq(_message.Message):
    __slots__ = ("reason", "data", "voice_session_sid")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _service_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_service_pb2.Value, _Mapping]] = ...) -> None: ...
    REASON_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    reason: str
    data: _containers.MessageMap[str, _service_pb2.Value]
    voice_session_sid: int
    def __init__(self, reason: _Optional[str] = ..., data: _Optional[_Mapping[str, _service_pb2.Value]] = ..., voice_session_sid: _Optional[int] = ...) -> None: ...

class FinishSecureFormHandlingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PopulateWorkflowFieldsReq(_message.Message):
    __slots__ = ("client_sid", "agent_sid", "call_sid", "call_type", "scheduled_callback_id", "field_definitions")
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    agent_sid: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    scheduled_callback_id: str
    field_definitions: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.FieldDefinition]
    def __init__(self, client_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., scheduled_callback_id: _Optional[str] = ..., field_definitions: _Optional[_Iterable[_Union[_integrations_pb2.FieldDefinition, _Mapping]]] = ...) -> None: ...

class PopulateWorkflowFieldsRes(_message.Message):
    __slots__ = ("values",)
    class ValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _service_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_service_pb2.Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, _service_pb2.Value]
    def __init__(self, values: _Optional[_Mapping[str, _service_pb2.Value]] = ...) -> None: ...

class ValidateFieldReq(_message.Message):
    __slots__ = ("voice_session_sid", "validation_type", "field_name")
    VOICE_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    voice_session_sid: int
    validation_type: _integrations_pb2.Validation
    field_name: str
    def __init__(self, voice_session_sid: _Optional[int] = ..., validation_type: _Optional[_Union[_integrations_pb2.Validation, str]] = ..., field_name: _Optional[str] = ...) -> None: ...

class ValidateFieldRes(_message.Message):
    __slots__ = ("valid", "reason")
    VALID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    reason: str
    def __init__(self, valid: bool = ..., reason: _Optional[str] = ...) -> None: ...

class ListAgentsVoiceStatusesRequest(_message.Message):
    __slots__ = ("skills", "all_skills_required", "page_token")
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    ALL_SKILLS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedScalarFieldContainer[str]
    all_skills_required: bool
    page_token: str
    def __init__(self, skills: _Optional[_Iterable[str]] = ..., all_skills_required: bool = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAgentsVoiceStatusesReply(_message.Message):
    __slots__ = ("agent_details", "next_page_token")
    AGENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    agent_details: _containers.RepeatedCompositeFieldContainer[AgentVoiceStatusDetails]
    next_page_token: str
    def __init__(self, agent_details: _Optional[_Iterable[_Union[AgentVoiceStatusDetails, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AgentVoiceStatusDetails(_message.Message):
    __slots__ = ("agent_sid", "hunt_group_sid", "current_session_sid", "first_name", "last_name", "status", "status_desc", "skills", "pbx_extensions")
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_DESC_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    PBX_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    agent_sid: int
    hunt_group_sid: int
    current_session_sid: int
    first_name: str
    last_name: str
    status: int
    status_desc: _acd_pb2.AgentStatus.Enum
    skills: _containers.RepeatedScalarFieldContainer[str]
    pbx_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_sid: _Optional[int] = ..., hunt_group_sid: _Optional[int] = ..., current_session_sid: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., status: _Optional[int] = ..., status_desc: _Optional[_Union[_acd_pb2.AgentStatus.Enum, str]] = ..., skills: _Optional[_Iterable[str]] = ..., pbx_extensions: _Optional[_Iterable[str]] = ...) -> None: ...
