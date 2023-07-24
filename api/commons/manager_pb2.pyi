from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AgentInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AGENT_INFO_ACTIVE_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_IN_CONFERENCE_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_MANUAL_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_PAUSED_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_PREVIEW_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_READY_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_TOTAL_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_TRANSFER_AGENTS: _ClassVar[AgentInfo]
    AGENT_INFO_WRAP_UP_AGENTS: _ClassVar[AgentInfo]

class SkillStats(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SKILL_STATS_AGENT_PEERED_CALLS: _ClassVar[SkillStats]
    SKILL_STATS_AVERAGE_LENGTH: _ClassVar[SkillStats]
    SKILL_STATS_CALL_COUNT: _ClassVar[SkillStats]
    SKILL_STATS_CALL_SKILL_MAP: _ClassVar[SkillStats]
    SKILL_STATS_CALL_TYPE: _ClassVar[SkillStats]
    SKILL_STATS_CALLS_LIST: _ClassVar[SkillStats]
    SKILL_STATS_DAILY_BY_SKILLS_KEY: _ClassVar[SkillStats]
    SKILL_STATS_LONGEST_IN_QUEUE: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_MD: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_PC: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_LI: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_OC: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_P: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_W: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_WU: _ClassVar[SkillStats]
    SKILL_STATS_MATCHING_AGENTS_TC: _ClassVar[SkillStats]
    SKILL_STATS_MAXIMUM_LENGTH: _ClassVar[SkillStats]
    SKILL_STATS_MINIMUM_LENGTH: _ClassVar[SkillStats]
    SKILL_STATS_PBX_EXTENSION: _ClassVar[SkillStats]
    SKILL_STATS_QUEUED_NOTIFICATION_TYPE: _ClassVar[SkillStats]
    SKILL_STATS_SKILL_SET: _ClassVar[SkillStats]
    SKILL_STATS_TOTAL_LENGTH_FOR_AVERAGE: _ClassVar[SkillStats]

class SkillQueues(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SKILL_QUEUES_ACD_QUEUE: _ClassVar[SkillQueues]
    SKILL_QUEUES_MULTI_HOLD: _ClassVar[SkillQueues]
    SKILL_QUEUES_SIMPLE_HOLD: _ClassVar[SkillQueues]
    SKILL_QUEUES_TRANSFER: _ClassVar[SkillQueues]
    SKILL_QUEUES_SUSPENDED_CALLBACK: _ClassVar[SkillQueues]
    SKILL_QUEUES_GRAND_TOTALS: _ClassVar[SkillQueues]

class AgentStats(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AGENT_STATS_AGENT_NAME: _ClassVar[AgentStats]
    AGENT_STATS_AGENT_STATUS: _ClassVar[AgentStats]
    AGENT_STATS_DURATION_IN_STATUS: _ClassVar[AgentStats]
    AGENT_STATS_LOGIN_DATE_TIME: _ClassVar[AgentStats]
    AGENT_STATS_LOGIN_DURATION: _ClassVar[AgentStats]
    AGENT_STATS_AGENT_SKILLS: _ClassVar[AgentStats]
    AGENT_STATS_AGENT_SID: _ClassVar[AgentStats]
    AGENT_STATS_SESSION_ID: _ClassVar[AgentStats]
    AGENT_STATS_HUNT_GROUP_NAME: _ClassVar[AgentStats]
    AGENT_STATS_CALL_COUNT: _ClassVar[AgentStats]
    AGENT_STATS_PAUSE_CODE: _ClassVar[AgentStats]
    AGENT_STATS_RECORDING_STATUS: _ClassVar[AgentStats]
    AGENT_STATS_MULTI_HOLD_COUNT: _ClassVar[AgentStats]
    AGENT_STATS_SIMPLE_HOLD_COUNT: _ClassVar[AgentStats]
    AGENT_STATS_TOTAL_HOLD_COUNT: _ClassVar[AgentStats]

class ManagerBargeInMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MONITOR: _ClassVar[ManagerBargeInMode]
    FULL_CONFERENCE: _ClassVar[ManagerBargeInMode]
    AGENT_WHISPER: _ClassVar[ManagerBargeInMode]
AGENT_INFO_ACTIVE_AGENTS: AgentInfo
AGENT_INFO_IN_CONFERENCE_AGENTS: AgentInfo
AGENT_INFO_MANUAL_AGENTS: AgentInfo
AGENT_INFO_PAUSED_AGENTS: AgentInfo
AGENT_INFO_PREVIEW_AGENTS: AgentInfo
AGENT_INFO_READY_AGENTS: AgentInfo
AGENT_INFO_TOTAL_AGENTS: AgentInfo
AGENT_INFO_TRANSFER_AGENTS: AgentInfo
AGENT_INFO_WRAP_UP_AGENTS: AgentInfo
SKILL_STATS_AGENT_PEERED_CALLS: SkillStats
SKILL_STATS_AVERAGE_LENGTH: SkillStats
SKILL_STATS_CALL_COUNT: SkillStats
SKILL_STATS_CALL_SKILL_MAP: SkillStats
SKILL_STATS_CALL_TYPE: SkillStats
SKILL_STATS_CALLS_LIST: SkillStats
SKILL_STATS_DAILY_BY_SKILLS_KEY: SkillStats
SKILL_STATS_LONGEST_IN_QUEUE: SkillStats
SKILL_STATS_MATCHING_AGENTS_MD: SkillStats
SKILL_STATS_MATCHING_AGENTS_PC: SkillStats
SKILL_STATS_MATCHING_AGENTS_LI: SkillStats
SKILL_STATS_MATCHING_AGENTS_OC: SkillStats
SKILL_STATS_MATCHING_AGENTS_P: SkillStats
SKILL_STATS_MATCHING_AGENTS_W: SkillStats
SKILL_STATS_MATCHING_AGENTS_WU: SkillStats
SKILL_STATS_MATCHING_AGENTS_TC: SkillStats
SKILL_STATS_MAXIMUM_LENGTH: SkillStats
SKILL_STATS_MINIMUM_LENGTH: SkillStats
SKILL_STATS_PBX_EXTENSION: SkillStats
SKILL_STATS_QUEUED_NOTIFICATION_TYPE: SkillStats
SKILL_STATS_SKILL_SET: SkillStats
SKILL_STATS_TOTAL_LENGTH_FOR_AVERAGE: SkillStats
SKILL_QUEUES_ACD_QUEUE: SkillQueues
SKILL_QUEUES_MULTI_HOLD: SkillQueues
SKILL_QUEUES_SIMPLE_HOLD: SkillQueues
SKILL_QUEUES_TRANSFER: SkillQueues
SKILL_QUEUES_SUSPENDED_CALLBACK: SkillQueues
SKILL_QUEUES_GRAND_TOTALS: SkillQueues
AGENT_STATS_AGENT_NAME: AgentStats
AGENT_STATS_AGENT_STATUS: AgentStats
AGENT_STATS_DURATION_IN_STATUS: AgentStats
AGENT_STATS_LOGIN_DATE_TIME: AgentStats
AGENT_STATS_LOGIN_DURATION: AgentStats
AGENT_STATS_AGENT_SKILLS: AgentStats
AGENT_STATS_AGENT_SID: AgentStats
AGENT_STATS_SESSION_ID: AgentStats
AGENT_STATS_HUNT_GROUP_NAME: AgentStats
AGENT_STATS_CALL_COUNT: AgentStats
AGENT_STATS_PAUSE_CODE: AgentStats
AGENT_STATS_RECORDING_STATUS: AgentStats
AGENT_STATS_MULTI_HOLD_COUNT: AgentStats
AGENT_STATS_SIMPLE_HOLD_COUNT: AgentStats
AGENT_STATS_TOTAL_HOLD_COUNT: AgentStats
MONITOR: ManagerBargeInMode
FULL_CONFERENCE: ManagerBargeInMode
AGENT_WHISPER: ManagerBargeInMode
