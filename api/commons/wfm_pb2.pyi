from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegressionForecasterModelTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RANDOM_FOREST: _ClassVar[RegressionForecasterModelTypes]
    ADABOOST: _ClassVar[RegressionForecasterModelTypes]
    GRADIENT_BOOSTING: _ClassVar[RegressionForecasterModelTypes]
    LINEAR_REGRESSION: _ClassVar[RegressionForecasterModelTypes]
    LINEAR_AVG: _ClassVar[RegressionForecasterModelTypes]
    SEGMENTED_LINEAR: _ClassVar[RegressionForecasterModelTypes]
    MLP: _ClassVar[RegressionForecasterModelTypes]
    AUTO: _ClassVar[RegressionForecasterModelTypes]

class RegressionForecasterAvgsProcessingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORECAST: _ClassVar[RegressionForecasterAvgsProcessingType]
    AVERAGES: _ClassVar[RegressionForecasterAvgsProcessingType]
    FIXED_AVERAGES: _ClassVar[RegressionForecasterAvgsProcessingType]

class ConstraintTimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MINUTES: _ClassVar[ConstraintTimeUnit]
    HOURS: _ClassVar[ConstraintTimeUnit]
    SHIFTS: _ClassVar[ConstraintTimeUnit]
    DAYS: _ClassVar[ConstraintTimeUnit]
    WEEKS: _ClassVar[ConstraintTimeUnit]
    MONTHS: _ClassVar[ConstraintTimeUnit]
    YEARS: _ClassVar[ConstraintTimeUnit]

class ConfigEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALL_CENTER_NODE: _ClassVar[ConfigEntityType]
    CLIENT_NODE: _ClassVar[ConfigEntityType]
    LOCATION_NODE: _ClassVar[ConfigEntityType]
    PROGRAM_NODE: _ClassVar[ConfigEntityType]
    AGENT_GROUP: _ClassVar[ConfigEntityType]
    SHIFT_TEMPLATE: _ClassVar[ConfigEntityType]
    WFM_AGENT: _ClassVar[ConfigEntityType]
    PLACEMENT_RULE: _ClassVar[ConfigEntityType]
    CONSTRAINT_RULE: _ClassVar[ConfigEntityType]
    NON_SKILL_ACTIVITY: _ClassVar[ConfigEntityType]
    AGENT_AVAILABILITY: _ClassVar[ConfigEntityType]
    OPEN_TIMES: _ClassVar[ConfigEntityType]
    SCHEDULING_ACTIVITY: _ClassVar[ConfigEntityType]
    SKILL_PROFICIENCY: _ClassVar[ConfigEntityType]
    SCHEDULE_SCENARIO: _ClassVar[ConfigEntityType]
    SKILL: _ClassVar[ConfigEntityType]
    TOUR_PATTERN: _ClassVar[ConfigEntityType]
    TOUR_WEEK_PATTERN: _ClassVar[ConfigEntityType]
    TOUR_SHIFT_INSTANCE_CONFIG: _ClassVar[ConfigEntityType]
    TOUR_SHIFT_SEGMENT_CONFIG: _ClassVar[ConfigEntityType]
    TOUR_AGENT_COLLECTION: _ClassVar[ConfigEntityType]

class ConstraintRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIN_CONSEC_ON: _ClassVar[ConstraintRuleType]
    MAX_CONSEC_ON: _ClassVar[ConstraintRuleType]
    MIN_CONSEC_OFF: _ClassVar[ConstraintRuleType]
    MAX_CONSEC_OFF: _ClassVar[ConstraintRuleType]
    MIN_TOTAL_ON: _ClassVar[ConstraintRuleType]
    MAX_TOTAL_ON: _ClassVar[ConstraintRuleType]
    MIN_TOTAL_OFF: _ClassVar[ConstraintRuleType]
    MAX_TOTAL_OFF: _ClassVar[ConstraintRuleType]
    MIN_SKILL_LEVEL: _ClassVar[ConstraintRuleType]

class DOWPlacementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MUST_NOT: _ClassVar[DOWPlacementType]
    MAY: _ClassVar[DOWPlacementType]
    MUST: _ClassVar[DOWPlacementType]

class OpenTimesOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOSED: _ClassVar[OpenTimesOption]
    OPEN: _ClassVar[OpenTimesOption]

class AvailabilityOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE: _ClassVar[AvailabilityOption]
    NOT_AVAILABLE: _ClassVar[AvailabilityOption]
    PREFER_NOT_AVAILABLE: _ClassVar[AvailabilityOption]

class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MON: _ClassVar[DayOfWeek]
    TUE: _ClassVar[DayOfWeek]
    WED: _ClassVar[DayOfWeek]
    THU: _ClassVar[DayOfWeek]
    FRI: _ClassVar[DayOfWeek]
    SAT: _ClassVar[DayOfWeek]
    SUN: _ClassVar[DayOfWeek]

class ConfigRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IS_ASSOCIATED_WITH: _ClassVar[ConfigRelationshipType]
    IS_NOT_ASSOCIATED_WITH: _ClassVar[ConfigRelationshipType]
    IS_MEMBER_OF: _ClassVar[ConfigRelationshipType]

class DiagnosticLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFORMATION: _ClassVar[DiagnosticLevel]
    SUGGESTION: _ClassVar[DiagnosticLevel]
    WARNING: _ClassVar[DiagnosticLevel]
    DIAGNOSTIC_ERROR: _ClassVar[DiagnosticLevel]
    INTERNAL_ERROR: _ClassVar[DiagnosticLevel]

class DiagnosticCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERAL: _ClassVar[DiagnosticCode]
    OK: _ClassVar[DiagnosticCode]
    NO_SKILLS_IN_DICTIONARY: _ClassVar[DiagnosticCode]
    AGENT_HAS_NO_SKILL_PROFICIENCIES: _ClassVar[DiagnosticCode]
    AGENT_HAS_NO_SKILLS: _ClassVar[DiagnosticCode]
    NO_SCHEDULING_ACTIVITIES_FOR_CONSTRAINT_RULES: _ClassVar[DiagnosticCode]
    SCHEDULING_ACTIVITY_FOR_CONSTRAINT_RULE_NOT_FOUND: _ClassVar[DiagnosticCode]
    SHIFT_TEMPLATE_CANNOT_BE_NONE: _ClassVar[DiagnosticCode]
    SHIFT_TEMPLATE_HAS_NO_PLACEMENT_RULES: _ClassVar[DiagnosticCode]
    NO_ONCALL_IN_SHIFT_TEMPLATE_PLACEMENT_RULES: _ClassVar[DiagnosticCode]
    MIN_GT_MAX_DURATION_IN_SHIFT_TEMPLATE_PLACEMENT_RULES: _ClassVar[DiagnosticCode]
    MIN_GT_MAX_AGENTS_IN_SHIFT_TEMPLATE: _ClassVar[DiagnosticCode]
    NO_PLACEMENT_RULES_FOR_SHIFT_TEMPLATE: _ClassVar[DiagnosticCode]
    ACTIVITIES_SHORTER_THAN_SHIFT: _ClassVar[DiagnosticCode]
    NOT_ENOUGH_AGENTS_FOR_SHIFT: _ClassVar[DiagnosticCode]
    PROGRAM_HAS_NO_AGENT_GROUPS: _ClassVar[DiagnosticCode]
    PROGRAM_HAS_NO_SHIFT_TEMPLATES: _ClassVar[DiagnosticCode]
    LOCATION_HAS_NO_PROGRAMS: _ClassVar[DiagnosticCode]
    CLIENT_HAS_NO_LOCATIONS: _ClassVar[DiagnosticCode]
    CALL_CENTER_HAS_NO_CLIENTS: _ClassVar[DiagnosticCode]
    PROGRAM_HAS_INVALID_PARENT_LOCATION: _ClassVar[DiagnosticCode]
    LOCATION_HAS_INVALID_PARENT_CLIENT: _ClassVar[DiagnosticCode]
    CLIENT_HAS_INVALID_PARENT_CALL_CENTER: _ClassVar[DiagnosticCode]
    AGENT_GROUP_HAS_INVALID_PARENT_NODE: _ClassVar[DiagnosticCode]
    SHIFT_TEMPLATE_HAS_INVALID_PARENT_PROGRAM: _ClassVar[DiagnosticCode]
    NO_SKILL_PROFICIENCY_FOR_MIN_SKILL_PROFICIENCY_CONSTRAINT_RULE: _ClassVar[DiagnosticCode]
    TOO_MANY_AGENTS_WITH_LOCKED_SHIFTS_FOR_MIN_AGENTS: _ClassVar[DiagnosticCode]
    AGENT_DOES_NOT_BELONG_TO_AN_AGENT_GROUP: _ClassVar[DiagnosticCode]
    INVALID_CONSTRAINT_VAL_UNITS: _ClassVar[DiagnosticCode]
    CONSTRAINT_GENERAL_FAILURE: _ClassVar[DiagnosticCode]
    CANDIDATE_SHIFT_COLLISION_DETECTED: _ClassVar[DiagnosticCode]
    CANDIDATE_SHIFT_AGENT_NOT_AVAILABLE: _ClassVar[DiagnosticCode]
    CANDIDATE_CLOSED: _ClassVar[DiagnosticCode]
    CONSTRAINT_ACTIVITY_NOT_FOUND: _ClassVar[DiagnosticCode]
    CONSTRAINT_AGENT_DOES_NOT_HAVE_PROFICIENCY: _ClassVar[DiagnosticCode]
    CONSTRAINT_AGENT_PROFICIENCY_TOO_LOW: _ClassVar[DiagnosticCode]
    CONSTRAINT_MAX_TOTAL_ON_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MIN_TOTAL_ON_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MAX_TOTAL_OFF_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MIN_TOTAL_OFF_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MAX_CONSEC_ON_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MIN_CONSEC_ON_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MAX_CONSEC_OFF_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_MIN_CONSEC_OFF_FAILURE: _ClassVar[DiagnosticCode]
    CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR_SHIFT__PER_SHIFT: _ClassVar[DiagnosticCode]
    CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR__PER_MINUTES_HOURS: _ClassVar[DiagnosticCode]
    CONSTRAINT_CONSECUTIVE_SHIFTS_RULE_NOT_ALLOWED: _ClassVar[DiagnosticCode]
    CONSTRAINT_WITH_LARGER_PERIOD_PER_SMALL_PERIOD_NOT_ALLOWED: _ClassVar[DiagnosticCode]
    CONSTRAINT_MIN_MAX_OFF_TIME_FOR_SHIFTS_NOT_ALLOWED: _ClassVar[DiagnosticCode]
    CONSTRAINT_CANNOT_HAVE_CONSECUTIVE_TIME_PER_MULTIPLE_SHIFTS: _ClassVar[DiagnosticCode]
    CANNOT_GENERATE_TOUR_PATTERNS_FOR_NON_TOUR_SHIFT_TEMPLATE: _ClassVar[DiagnosticCode]
    TOUR_PATTERNS_NEEDED_TO_SCHEDULE_TOUR: _ClassVar[DiagnosticCode]
    SHIFT_TEMPLATE_ACTIVITY_PLACEMENT_MIN_MAX_MUST_BE_MULTIPLE_OF_5_MINUTES: _ClassVar[DiagnosticCode]
    NO_SHIFT_TEMPLATE_ACTIVITY_PLACEMENT_SEQUENCES_MATCH_SHIFT_MIN_MAX_WIDTH: _ClassVar[DiagnosticCode]
    INVALID_TOUR_PATTERN: _ClassVar[DiagnosticCode]
    INVALID_TOUR_AGENT_COLLECTION: _ClassVar[DiagnosticCode]
    INVALID_TOUR_SHIFT_INSTANCE_CONFIG: _ClassVar[DiagnosticCode]
    INVALID_TOUR_SHIFT_SEGMENT_CONFIG: _ClassVar[DiagnosticCode]
    TOUR_SHIFT_SEGMENT_CONFIG_OVERLAP: _ClassVar[DiagnosticCode]
    TOUR_SHIFT_SEGMENT_CONFIG_DOES_NOT_FIT: _ClassVar[DiagnosticCode]
    TOUR_SHIFT_INSTANCE_CONFIG_OVERLAP: _ClassVar[DiagnosticCode]
    WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_WEEK_PATTERNS: _ClassVar[DiagnosticCode]
    WFM_AGENT_SIDS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS: _ClassVar[DiagnosticCode]
    FIST_WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS: _ClassVar[DiagnosticCode]
    FIRST_WEEK_PATTERN_NUMBERS_NOT_FOUND_IN_TOUR_WEEK_PATTERNS: _ClassVar[DiagnosticCode]
    SHIFT_TEMPLATE_HAS_NO_ASSOCIATED_SCHEDULING_AGENT_GROUPS: _ClassVar[DiagnosticCode]
    ATTEMPT_TO_BUILD_SCHEDULES_FOR_INVALID_PARENT_NODE: _ClassVar[DiagnosticCode]
    SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MINIMUM: _ClassVar[DiagnosticCode]
    SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MAXIMUM: _ClassVar[DiagnosticCode]
    NO_OPEN_TIMES_SET_OR_INHERITED_BY_PROGRAM: _ClassVar[DiagnosticCode]
    TOUR_AGENT_COLLECTIONS_NEEDED_TO_SCHEDULE_TOUR: _ClassVar[DiagnosticCode]

class PerformanceMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FTE_REQUIRED_VS_ACHIEVED_SIMPLE: _ClassVar[PerformanceMetricType]
    FTE_REQUIRED_VS_ACHIEVED_EXTENDED: _ClassVar[PerformanceMetricType]
    SERVICE_LEVEL_ANALYSIS: _ClassVar[PerformanceMetricType]
    SERVICE_LEVEL_MATRIX: _ClassVar[PerformanceMetricType]
    CONTACT_HANDLING_METRICS: _ClassVar[PerformanceMetricType]
    LOAD_FORECAST: _ClassVar[PerformanceMetricType]

class ScheduleShouldInclude(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONLY_SHIFT_INSTANCES: _ClassVar[ScheduleShouldInclude]
    ONLY_PERFORMANCE_METRICS: _ClassVar[ScheduleShouldInclude]
    SHIFT_INSTANCES_AND_PERFORMANCE_METRICS: _ClassVar[ScheduleShouldInclude]

class ScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DRAFT: _ClassVar[ScheduleType]
    PUBLISHED: _ClassVar[ScheduleType]

class SchedulingTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COVERAGE: _ClassVar[SchedulingTargetType]
    SERVICE_LEVEL: _ClassVar[SchedulingTargetType]

class BitmapType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLETE: _ClassVar[BitmapType]
    ONLY_WEEKMAPS: _ClassVar[BitmapType]
    ONLY_CALENDAR_ITEMS: _ClassVar[BitmapType]

class HistoryCacheState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_LOADED: _ClassVar[HistoryCacheState]
    LOADING: _ClassVar[HistoryCacheState]
    LOADING_COMPLETE: _ClassVar[HistoryCacheState]
    LOADING_FAILED: _ClassVar[HistoryCacheState]

class InitialSetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_SETUP: _ClassVar[InitialSetupState]
    SETTING_UP: _ClassVar[InitialSetupState]
    SETUP_COMPLETE: _ClassVar[InitialSetupState]
    FAILURE: _ClassVar[InitialSetupState]

class RealTimeManagementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[RealTimeManagementState]
    LOGGED_IN: _ClassVar[RealTimeManagementState]
    CALL_ON_HOLD: _ClassVar[RealTimeManagementState]
    OUTBOUND_CALL: _ClassVar[RealTimeManagementState]
    TRANSFER: _ClassVar[RealTimeManagementState]
    CONFERENCE: _ClassVar[RealTimeManagementState]
    READY: _ClassVar[RealTimeManagementState]
    NOT_READY: _ClassVar[RealTimeManagementState]
    WRAP_UP: _ClassVar[RealTimeManagementState]
    LOGGED_OUT: _ClassVar[RealTimeManagementState]

class AgentLeavePetitionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED_PETITION_STATUS: _ClassVar[AgentLeavePetitionStatus]
    PENDING_PETITION: _ClassVar[AgentLeavePetitionStatus]
    APPROVED_PETITION: _ClassVar[AgentLeavePetitionStatus]
    DENIED_PETITION: _ClassVar[AgentLeavePetitionStatus]
    CANCELLED_PETITION: _ClassVar[AgentLeavePetitionStatus]

class SchedulingActivityClassification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STANDARD_SCHEDULING_ACTIVITY: _ClassVar[SchedulingActivityClassification]
    ON_CALL_ACTIVITY: _ClassVar[SchedulingActivityClassification]
    TIME_OFF_ACTIVITY: _ClassVar[SchedulingActivityClassification]

class AdherenceRuleNotificationMedium(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_RULE_NOTIFICATION_MEDIUM_IN_PRODUCT: _ClassVar[AdherenceRuleNotificationMedium]
    ADHERENCE_RULE_NOTIFICATION_MEDIUM_EMAIL: _ClassVar[AdherenceRuleNotificationMedium]

class AdherenceRuleRequirementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_RULE_REQUIREMENT_TYPE_NOT_USED: _ClassVar[AdherenceRuleRequirementType]
    ADHERENCE_RULE_REQUIREMENT_TYPE_OPTIONAL: _ClassVar[AdherenceRuleRequirementType]
    ADHERENCE_RULE_REQUIREMENT_TYPE_MANDATORY: _ClassVar[AdherenceRuleRequirementType]

class AdherenceRuleRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_RULE_RANGE_START_OF_DAY: _ClassVar[AdherenceRuleRange]
    ADHERENCE_RULE_RANGE_START_OF_WEEK: _ClassVar[AdherenceRuleRange]
    ADHERENCE_RULE_RANGE_START_OF_MONTH: _ClassVar[AdherenceRuleRange]
    ADHERENCE_RULE_RANGE_REST_OF_DAY: _ClassVar[AdherenceRuleRange]
    ADHERENCE_RULE_RANGE_CUSTOM_DATE_RANGE: _ClassVar[AdherenceRuleRange]

class AdherenceDepartmentalRuleActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_DEPARTMENTAL_RULE_ACTION_TYPE_CALLS_ANSWERED: _ClassVar[AdherenceDepartmentalRuleActionType]

class AdherenceRuleCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_RULE_CONDITION_GREATER_THAN: _ClassVar[AdherenceRuleCondition]
    ADHERENCE_RULE_CONDITION_GREATER_THAN_EQUAL: _ClassVar[AdherenceRuleCondition]
    ADHERENCE_RULE_CONDITION_LESS_THAN: _ClassVar[AdherenceRuleCondition]
    ADHERENCE_RULE_CONDITION_LESS_THAN_EQUAL: _ClassVar[AdherenceRuleCondition]

class AdherenceRuleUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_RULE_UNIT_SECONDS: _ClassVar[AdherenceRuleUnit]
    ADHERENCE_RULE_UNIT_MINUTES: _ClassVar[AdherenceRuleUnit]
    ADHERENCE_RULE_UNIT_CALLS: _ClassVar[AdherenceRuleUnit]
    ADHERENCE_RULE_UNIT_PERCENTAGE: _ClassVar[AdherenceRuleUnit]

class AdherenceAgentRuleActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADHERENCE_AGENT_RULE_ACTION_TYPE_WRAP_UP: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_WAITING: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_MANUAL_DIAL: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_PREVIEW_DIAL: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_ANSWER_CALLS: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_CALL: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_HOLD: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START_LATE: _ClassVar[AdherenceAgentRuleActionType]
    ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_END_EARLY: _ClassVar[AdherenceAgentRuleActionType]
RANDOM_FOREST: RegressionForecasterModelTypes
ADABOOST: RegressionForecasterModelTypes
GRADIENT_BOOSTING: RegressionForecasterModelTypes
LINEAR_REGRESSION: RegressionForecasterModelTypes
LINEAR_AVG: RegressionForecasterModelTypes
SEGMENTED_LINEAR: RegressionForecasterModelTypes
MLP: RegressionForecasterModelTypes
AUTO: RegressionForecasterModelTypes
FORECAST: RegressionForecasterAvgsProcessingType
AVERAGES: RegressionForecasterAvgsProcessingType
FIXED_AVERAGES: RegressionForecasterAvgsProcessingType
MINUTES: ConstraintTimeUnit
HOURS: ConstraintTimeUnit
SHIFTS: ConstraintTimeUnit
DAYS: ConstraintTimeUnit
WEEKS: ConstraintTimeUnit
MONTHS: ConstraintTimeUnit
YEARS: ConstraintTimeUnit
CALL_CENTER_NODE: ConfigEntityType
CLIENT_NODE: ConfigEntityType
LOCATION_NODE: ConfigEntityType
PROGRAM_NODE: ConfigEntityType
AGENT_GROUP: ConfigEntityType
SHIFT_TEMPLATE: ConfigEntityType
WFM_AGENT: ConfigEntityType
PLACEMENT_RULE: ConfigEntityType
CONSTRAINT_RULE: ConfigEntityType
NON_SKILL_ACTIVITY: ConfigEntityType
AGENT_AVAILABILITY: ConfigEntityType
OPEN_TIMES: ConfigEntityType
SCHEDULING_ACTIVITY: ConfigEntityType
SKILL_PROFICIENCY: ConfigEntityType
SCHEDULE_SCENARIO: ConfigEntityType
SKILL: ConfigEntityType
TOUR_PATTERN: ConfigEntityType
TOUR_WEEK_PATTERN: ConfigEntityType
TOUR_SHIFT_INSTANCE_CONFIG: ConfigEntityType
TOUR_SHIFT_SEGMENT_CONFIG: ConfigEntityType
TOUR_AGENT_COLLECTION: ConfigEntityType
MIN_CONSEC_ON: ConstraintRuleType
MAX_CONSEC_ON: ConstraintRuleType
MIN_CONSEC_OFF: ConstraintRuleType
MAX_CONSEC_OFF: ConstraintRuleType
MIN_TOTAL_ON: ConstraintRuleType
MAX_TOTAL_ON: ConstraintRuleType
MIN_TOTAL_OFF: ConstraintRuleType
MAX_TOTAL_OFF: ConstraintRuleType
MIN_SKILL_LEVEL: ConstraintRuleType
MUST_NOT: DOWPlacementType
MAY: DOWPlacementType
MUST: DOWPlacementType
CLOSED: OpenTimesOption
OPEN: OpenTimesOption
AVAILABLE: AvailabilityOption
NOT_AVAILABLE: AvailabilityOption
PREFER_NOT_AVAILABLE: AvailabilityOption
MON: DayOfWeek
TUE: DayOfWeek
WED: DayOfWeek
THU: DayOfWeek
FRI: DayOfWeek
SAT: DayOfWeek
SUN: DayOfWeek
IS_ASSOCIATED_WITH: ConfigRelationshipType
IS_NOT_ASSOCIATED_WITH: ConfigRelationshipType
IS_MEMBER_OF: ConfigRelationshipType
INFORMATION: DiagnosticLevel
SUGGESTION: DiagnosticLevel
WARNING: DiagnosticLevel
DIAGNOSTIC_ERROR: DiagnosticLevel
INTERNAL_ERROR: DiagnosticLevel
GENERAL: DiagnosticCode
OK: DiagnosticCode
NO_SKILLS_IN_DICTIONARY: DiagnosticCode
AGENT_HAS_NO_SKILL_PROFICIENCIES: DiagnosticCode
AGENT_HAS_NO_SKILLS: DiagnosticCode
NO_SCHEDULING_ACTIVITIES_FOR_CONSTRAINT_RULES: DiagnosticCode
SCHEDULING_ACTIVITY_FOR_CONSTRAINT_RULE_NOT_FOUND: DiagnosticCode
SHIFT_TEMPLATE_CANNOT_BE_NONE: DiagnosticCode
SHIFT_TEMPLATE_HAS_NO_PLACEMENT_RULES: DiagnosticCode
NO_ONCALL_IN_SHIFT_TEMPLATE_PLACEMENT_RULES: DiagnosticCode
MIN_GT_MAX_DURATION_IN_SHIFT_TEMPLATE_PLACEMENT_RULES: DiagnosticCode
MIN_GT_MAX_AGENTS_IN_SHIFT_TEMPLATE: DiagnosticCode
NO_PLACEMENT_RULES_FOR_SHIFT_TEMPLATE: DiagnosticCode
ACTIVITIES_SHORTER_THAN_SHIFT: DiagnosticCode
NOT_ENOUGH_AGENTS_FOR_SHIFT: DiagnosticCode
PROGRAM_HAS_NO_AGENT_GROUPS: DiagnosticCode
PROGRAM_HAS_NO_SHIFT_TEMPLATES: DiagnosticCode
LOCATION_HAS_NO_PROGRAMS: DiagnosticCode
CLIENT_HAS_NO_LOCATIONS: DiagnosticCode
CALL_CENTER_HAS_NO_CLIENTS: DiagnosticCode
PROGRAM_HAS_INVALID_PARENT_LOCATION: DiagnosticCode
LOCATION_HAS_INVALID_PARENT_CLIENT: DiagnosticCode
CLIENT_HAS_INVALID_PARENT_CALL_CENTER: DiagnosticCode
AGENT_GROUP_HAS_INVALID_PARENT_NODE: DiagnosticCode
SHIFT_TEMPLATE_HAS_INVALID_PARENT_PROGRAM: DiagnosticCode
NO_SKILL_PROFICIENCY_FOR_MIN_SKILL_PROFICIENCY_CONSTRAINT_RULE: DiagnosticCode
TOO_MANY_AGENTS_WITH_LOCKED_SHIFTS_FOR_MIN_AGENTS: DiagnosticCode
AGENT_DOES_NOT_BELONG_TO_AN_AGENT_GROUP: DiagnosticCode
INVALID_CONSTRAINT_VAL_UNITS: DiagnosticCode
CONSTRAINT_GENERAL_FAILURE: DiagnosticCode
CANDIDATE_SHIFT_COLLISION_DETECTED: DiagnosticCode
CANDIDATE_SHIFT_AGENT_NOT_AVAILABLE: DiagnosticCode
CANDIDATE_CLOSED: DiagnosticCode
CONSTRAINT_ACTIVITY_NOT_FOUND: DiagnosticCode
CONSTRAINT_AGENT_DOES_NOT_HAVE_PROFICIENCY: DiagnosticCode
CONSTRAINT_AGENT_PROFICIENCY_TOO_LOW: DiagnosticCode
CONSTRAINT_MAX_TOTAL_ON_FAILURE: DiagnosticCode
CONSTRAINT_MIN_TOTAL_ON_FAILURE: DiagnosticCode
CONSTRAINT_MAX_TOTAL_OFF_FAILURE: DiagnosticCode
CONSTRAINT_MIN_TOTAL_OFF_FAILURE: DiagnosticCode
CONSTRAINT_MAX_CONSEC_ON_FAILURE: DiagnosticCode
CONSTRAINT_MIN_CONSEC_ON_FAILURE: DiagnosticCode
CONSTRAINT_MAX_CONSEC_OFF_FAILURE: DiagnosticCode
CONSTRAINT_MIN_CONSEC_OFF_FAILURE: DiagnosticCode
CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR_SHIFT__PER_SHIFT: DiagnosticCode
CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR__PER_MINUTES_HOURS: DiagnosticCode
CONSTRAINT_CONSECUTIVE_SHIFTS_RULE_NOT_ALLOWED: DiagnosticCode
CONSTRAINT_WITH_LARGER_PERIOD_PER_SMALL_PERIOD_NOT_ALLOWED: DiagnosticCode
CONSTRAINT_MIN_MAX_OFF_TIME_FOR_SHIFTS_NOT_ALLOWED: DiagnosticCode
CONSTRAINT_CANNOT_HAVE_CONSECUTIVE_TIME_PER_MULTIPLE_SHIFTS: DiagnosticCode
CANNOT_GENERATE_TOUR_PATTERNS_FOR_NON_TOUR_SHIFT_TEMPLATE: DiagnosticCode
TOUR_PATTERNS_NEEDED_TO_SCHEDULE_TOUR: DiagnosticCode
SHIFT_TEMPLATE_ACTIVITY_PLACEMENT_MIN_MAX_MUST_BE_MULTIPLE_OF_5_MINUTES: DiagnosticCode
NO_SHIFT_TEMPLATE_ACTIVITY_PLACEMENT_SEQUENCES_MATCH_SHIFT_MIN_MAX_WIDTH: DiagnosticCode
INVALID_TOUR_PATTERN: DiagnosticCode
INVALID_TOUR_AGENT_COLLECTION: DiagnosticCode
INVALID_TOUR_SHIFT_INSTANCE_CONFIG: DiagnosticCode
INVALID_TOUR_SHIFT_SEGMENT_CONFIG: DiagnosticCode
TOUR_SHIFT_SEGMENT_CONFIG_OVERLAP: DiagnosticCode
TOUR_SHIFT_SEGMENT_CONFIG_DOES_NOT_FIT: DiagnosticCode
TOUR_SHIFT_INSTANCE_CONFIG_OVERLAP: DiagnosticCode
WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_WEEK_PATTERNS: DiagnosticCode
WFM_AGENT_SIDS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS: DiagnosticCode
FIST_WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS: DiagnosticCode
FIRST_WEEK_PATTERN_NUMBERS_NOT_FOUND_IN_TOUR_WEEK_PATTERNS: DiagnosticCode
SHIFT_TEMPLATE_HAS_NO_ASSOCIATED_SCHEDULING_AGENT_GROUPS: DiagnosticCode
ATTEMPT_TO_BUILD_SCHEDULES_FOR_INVALID_PARENT_NODE: DiagnosticCode
SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MINIMUM: DiagnosticCode
SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MAXIMUM: DiagnosticCode
NO_OPEN_TIMES_SET_OR_INHERITED_BY_PROGRAM: DiagnosticCode
TOUR_AGENT_COLLECTIONS_NEEDED_TO_SCHEDULE_TOUR: DiagnosticCode
FTE_REQUIRED_VS_ACHIEVED_SIMPLE: PerformanceMetricType
FTE_REQUIRED_VS_ACHIEVED_EXTENDED: PerformanceMetricType
SERVICE_LEVEL_ANALYSIS: PerformanceMetricType
SERVICE_LEVEL_MATRIX: PerformanceMetricType
CONTACT_HANDLING_METRICS: PerformanceMetricType
LOAD_FORECAST: PerformanceMetricType
ONLY_SHIFT_INSTANCES: ScheduleShouldInclude
ONLY_PERFORMANCE_METRICS: ScheduleShouldInclude
SHIFT_INSTANCES_AND_PERFORMANCE_METRICS: ScheduleShouldInclude
DRAFT: ScheduleType
PUBLISHED: ScheduleType
COVERAGE: SchedulingTargetType
SERVICE_LEVEL: SchedulingTargetType
COMPLETE: BitmapType
ONLY_WEEKMAPS: BitmapType
ONLY_CALENDAR_ITEMS: BitmapType
NOT_LOADED: HistoryCacheState
LOADING: HistoryCacheState
LOADING_COMPLETE: HistoryCacheState
LOADING_FAILED: HistoryCacheState
NOT_SETUP: InitialSetupState
SETTING_UP: InitialSetupState
SETUP_COMPLETE: InitialSetupState
FAILURE: InitialSetupState
UNSPECIFIED: RealTimeManagementState
LOGGED_IN: RealTimeManagementState
CALL_ON_HOLD: RealTimeManagementState
OUTBOUND_CALL: RealTimeManagementState
TRANSFER: RealTimeManagementState
CONFERENCE: RealTimeManagementState
READY: RealTimeManagementState
NOT_READY: RealTimeManagementState
WRAP_UP: RealTimeManagementState
LOGGED_OUT: RealTimeManagementState
UNSPECIFIED_PETITION_STATUS: AgentLeavePetitionStatus
PENDING_PETITION: AgentLeavePetitionStatus
APPROVED_PETITION: AgentLeavePetitionStatus
DENIED_PETITION: AgentLeavePetitionStatus
CANCELLED_PETITION: AgentLeavePetitionStatus
STANDARD_SCHEDULING_ACTIVITY: SchedulingActivityClassification
ON_CALL_ACTIVITY: SchedulingActivityClassification
TIME_OFF_ACTIVITY: SchedulingActivityClassification
ADHERENCE_RULE_NOTIFICATION_MEDIUM_IN_PRODUCT: AdherenceRuleNotificationMedium
ADHERENCE_RULE_NOTIFICATION_MEDIUM_EMAIL: AdherenceRuleNotificationMedium
ADHERENCE_RULE_REQUIREMENT_TYPE_NOT_USED: AdherenceRuleRequirementType
ADHERENCE_RULE_REQUIREMENT_TYPE_OPTIONAL: AdherenceRuleRequirementType
ADHERENCE_RULE_REQUIREMENT_TYPE_MANDATORY: AdherenceRuleRequirementType
ADHERENCE_RULE_RANGE_START_OF_DAY: AdherenceRuleRange
ADHERENCE_RULE_RANGE_START_OF_WEEK: AdherenceRuleRange
ADHERENCE_RULE_RANGE_START_OF_MONTH: AdherenceRuleRange
ADHERENCE_RULE_RANGE_REST_OF_DAY: AdherenceRuleRange
ADHERENCE_RULE_RANGE_CUSTOM_DATE_RANGE: AdherenceRuleRange
ADHERENCE_DEPARTMENTAL_RULE_ACTION_TYPE_CALLS_ANSWERED: AdherenceDepartmentalRuleActionType
ADHERENCE_RULE_CONDITION_GREATER_THAN: AdherenceRuleCondition
ADHERENCE_RULE_CONDITION_GREATER_THAN_EQUAL: AdherenceRuleCondition
ADHERENCE_RULE_CONDITION_LESS_THAN: AdherenceRuleCondition
ADHERENCE_RULE_CONDITION_LESS_THAN_EQUAL: AdherenceRuleCondition
ADHERENCE_RULE_UNIT_SECONDS: AdherenceRuleUnit
ADHERENCE_RULE_UNIT_MINUTES: AdherenceRuleUnit
ADHERENCE_RULE_UNIT_CALLS: AdherenceRuleUnit
ADHERENCE_RULE_UNIT_PERCENTAGE: AdherenceRuleUnit
ADHERENCE_AGENT_RULE_ACTION_TYPE_WRAP_UP: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_WAITING: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_MANUAL_DIAL: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_PREVIEW_DIAL: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_ANSWER_CALLS: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_CALL: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_HOLD: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START_LATE: AdherenceAgentRuleActionType
ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_END_EARLY: AdherenceAgentRuleActionType

class SkillType(_message.Message):
    __slots__ = ()
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGENT_SKILL: _ClassVar[SkillType.Enum]
        HUNT_GROUP: _ClassVar[SkillType.Enum]
        AGENT_PBX: _ClassVar[SkillType.Enum]
        HUNT_GROUP_PBX: _ClassVar[SkillType.Enum]
        PBX: _ClassVar[SkillType.Enum]
        AGENT: _ClassVar[SkillType.Enum]
    AGENT_SKILL: SkillType.Enum
    HUNT_GROUP: SkillType.Enum
    AGENT_PBX: SkillType.Enum
    HUNT_GROUP_PBX: SkillType.Enum
    PBX: SkillType.Enum
    AGENT: SkillType.Enum
    def __init__(self) -> None: ...

class DatetimeRange(_message.Message):
    __slots__ = ("start_datetime", "end_datetime")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    END_DATETIME_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    end_datetime: _timestamp_pb2.Timestamp
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ForecastingParameters(_message.Message):
    __slots__ = ("interval_width_in_minutes", "historical_data_range_in_months", "historical_data_range_start_datetime", "forecast_test_range_in_weeks", "forecast_range_in_weeks", "forecast_datetime_range", "training_data_range_in_months", "training_data_datetime_range", "averages_calculation_range_in_months")
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_DATA_RANGE_IN_MONTHS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_DATA_RANGE_START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    FORECAST_TEST_RANGE_IN_WEEKS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_RANGE_IN_WEEKS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATA_RANGE_IN_MONTHS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATA_DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    AVERAGES_CALCULATION_RANGE_IN_MONTHS_FIELD_NUMBER: _ClassVar[int]
    interval_width_in_minutes: int
    historical_data_range_in_months: int
    historical_data_range_start_datetime: _timestamp_pb2.Timestamp
    forecast_test_range_in_weeks: int
    forecast_range_in_weeks: int
    forecast_datetime_range: DatetimeRange
    training_data_range_in_months: int
    training_data_datetime_range: DatetimeRange
    averages_calculation_range_in_months: int
    def __init__(self, interval_width_in_minutes: _Optional[int] = ..., historical_data_range_in_months: _Optional[int] = ..., historical_data_range_start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., forecast_test_range_in_weeks: _Optional[int] = ..., forecast_range_in_weeks: _Optional[int] = ..., forecast_datetime_range: _Optional[_Union[DatetimeRange, _Mapping]] = ..., training_data_range_in_months: _Optional[int] = ..., training_data_datetime_range: _Optional[_Union[DatetimeRange, _Mapping]] = ..., averages_calculation_range_in_months: _Optional[int] = ...) -> None: ...

class ProfileTOD(_message.Message):
    __slots__ = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    SUNDAY_FIELD_NUMBER: _ClassVar[int]
    MONDAY_FIELD_NUMBER: _ClassVar[int]
    TUESDAY_FIELD_NUMBER: _ClassVar[int]
    WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    THURSDAY_FIELD_NUMBER: _ClassVar[int]
    FRIDAY_FIELD_NUMBER: _ClassVar[int]
    SATURDAY_FIELD_NUMBER: _ClassVar[int]
    sunday: _containers.RepeatedScalarFieldContainer[float]
    monday: _containers.RepeatedScalarFieldContainer[float]
    tuesday: _containers.RepeatedScalarFieldContainer[float]
    wednesday: _containers.RepeatedScalarFieldContainer[float]
    thursday: _containers.RepeatedScalarFieldContainer[float]
    friday: _containers.RepeatedScalarFieldContainer[float]
    saturday: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, sunday: _Optional[_Iterable[float]] = ..., monday: _Optional[_Iterable[float]] = ..., tuesday: _Optional[_Iterable[float]] = ..., wednesday: _Optional[_Iterable[float]] = ..., thursday: _Optional[_Iterable[float]] = ..., friday: _Optional[_Iterable[float]] = ..., saturday: _Optional[_Iterable[float]] = ...) -> None: ...

class ProfileWOMS(_message.Message):
    __slots__ = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    JANUARY_FIELD_NUMBER: _ClassVar[int]
    FEBRUARY_FIELD_NUMBER: _ClassVar[int]
    MARCH_FIELD_NUMBER: _ClassVar[int]
    APRIL_FIELD_NUMBER: _ClassVar[int]
    MAY_FIELD_NUMBER: _ClassVar[int]
    JUNE_FIELD_NUMBER: _ClassVar[int]
    JULY_FIELD_NUMBER: _ClassVar[int]
    AUGUST_FIELD_NUMBER: _ClassVar[int]
    SEPTEMBER_FIELD_NUMBER: _ClassVar[int]
    OCTOBER_FIELD_NUMBER: _ClassVar[int]
    NOVEMBER_FIELD_NUMBER: _ClassVar[int]
    DECEMBER_FIELD_NUMBER: _ClassVar[int]
    january: _containers.RepeatedScalarFieldContainer[float]
    february: _containers.RepeatedScalarFieldContainer[float]
    march: _containers.RepeatedScalarFieldContainer[float]
    april: _containers.RepeatedScalarFieldContainer[float]
    may: _containers.RepeatedScalarFieldContainer[float]
    june: _containers.RepeatedScalarFieldContainer[float]
    july: _containers.RepeatedScalarFieldContainer[float]
    august: _containers.RepeatedScalarFieldContainer[float]
    september: _containers.RepeatedScalarFieldContainer[float]
    october: _containers.RepeatedScalarFieldContainer[float]
    november: _containers.RepeatedScalarFieldContainer[float]
    december: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, january: _Optional[_Iterable[float]] = ..., february: _Optional[_Iterable[float]] = ..., march: _Optional[_Iterable[float]] = ..., april: _Optional[_Iterable[float]] = ..., may: _Optional[_Iterable[float]] = ..., june: _Optional[_Iterable[float]] = ..., july: _Optional[_Iterable[float]] = ..., august: _Optional[_Iterable[float]] = ..., september: _Optional[_Iterable[float]] = ..., october: _Optional[_Iterable[float]] = ..., november: _Optional[_Iterable[float]] = ..., december: _Optional[_Iterable[float]] = ...) -> None: ...

class ProfileDOW(_message.Message):
    __slots__ = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    SUNDAY_FIELD_NUMBER: _ClassVar[int]
    MONDAY_FIELD_NUMBER: _ClassVar[int]
    TUESDAY_FIELD_NUMBER: _ClassVar[int]
    WEDNESDAY_FIELD_NUMBER: _ClassVar[int]
    THURSDAY_FIELD_NUMBER: _ClassVar[int]
    FRIDAY_FIELD_NUMBER: _ClassVar[int]
    SATURDAY_FIELD_NUMBER: _ClassVar[int]
    sunday: float
    monday: float
    tuesday: float
    wednesday: float
    thursday: float
    friday: float
    saturday: float
    def __init__(self, sunday: _Optional[float] = ..., monday: _Optional[float] = ..., tuesday: _Optional[float] = ..., wednesday: _Optional[float] = ..., thursday: _Optional[float] = ..., friday: _Optional[float] = ..., saturday: _Optional[float] = ...) -> None: ...

class ProfileMOY(_message.Message):
    __slots__ = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    JANUARY_FIELD_NUMBER: _ClassVar[int]
    FEBRUARY_FIELD_NUMBER: _ClassVar[int]
    MARCH_FIELD_NUMBER: _ClassVar[int]
    APRIL_FIELD_NUMBER: _ClassVar[int]
    MAY_FIELD_NUMBER: _ClassVar[int]
    JUNE_FIELD_NUMBER: _ClassVar[int]
    JULY_FIELD_NUMBER: _ClassVar[int]
    AUGUST_FIELD_NUMBER: _ClassVar[int]
    SEPTEMBER_FIELD_NUMBER: _ClassVar[int]
    OCTOBER_FIELD_NUMBER: _ClassVar[int]
    NOVEMBER_FIELD_NUMBER: _ClassVar[int]
    DECEMBER_FIELD_NUMBER: _ClassVar[int]
    january: float
    february: float
    march: float
    april: float
    may: float
    june: float
    july: float
    august: float
    september: float
    october: float
    november: float
    december: float
    def __init__(self, january: _Optional[float] = ..., february: _Optional[float] = ..., march: _Optional[float] = ..., april: _Optional[float] = ..., may: _Optional[float] = ..., june: _Optional[float] = ..., july: _Optional[float] = ..., august: _Optional[float] = ..., september: _Optional[float] = ..., october: _Optional[float] = ..., november: _Optional[float] = ..., december: _Optional[float] = ...) -> None: ...

class DistributionProfile(_message.Message):
    __slots__ = ("profile_tod", "profile_woms", "profile_dow", "profile_moy")
    PROFILE_TOD_FIELD_NUMBER: _ClassVar[int]
    PROFILE_WOMS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_DOW_FIELD_NUMBER: _ClassVar[int]
    PROFILE_MOY_FIELD_NUMBER: _ClassVar[int]
    profile_tod: ProfileTOD
    profile_woms: ProfileWOMS
    profile_dow: ProfileDOW
    profile_moy: ProfileMOY
    def __init__(self, profile_tod: _Optional[_Union[ProfileTOD, _Mapping]] = ..., profile_woms: _Optional[_Union[ProfileWOMS, _Mapping]] = ..., profile_dow: _Optional[_Union[ProfileDOW, _Mapping]] = ..., profile_moy: _Optional[_Union[ProfileMOY, _Mapping]] = ...) -> None: ...

class CallProfileGroupCalls(_message.Message):
    __slots__ = ("total_calls", "distribution_profile")
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    total_calls: int
    distribution_profile: DistributionProfile
    def __init__(self, total_calls: _Optional[int] = ..., distribution_profile: _Optional[_Union[DistributionProfile, _Mapping]] = ...) -> None: ...

class CallProfileGroupAvgs(_message.Message):
    __slots__ = ("min_average", "max_average", "distribution_profile")
    MIN_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    min_average: float
    max_average: float
    distribution_profile: DistributionProfile
    def __init__(self, min_average: _Optional[float] = ..., max_average: _Optional[float] = ..., distribution_profile: _Optional[_Union[DistributionProfile, _Mapping]] = ...) -> None: ...

class OptionTypes(_message.Message):
    __slots__ = ("open_times_option", "availability_option")
    OPEN_TIMES_OPTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_OPTION_FIELD_NUMBER: _ClassVar[int]
    open_times_option: OpenTimesOption
    availability_option: AvailabilityOption
    def __init__(self, open_times_option: _Optional[_Union[OpenTimesOption, str]] = ..., availability_option: _Optional[_Union[AvailabilityOption, str]] = ...) -> None: ...

class ScheduleSelector(_message.Message):
    __slots__ = ("schedule_sid", "schedule_type")
    SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    schedule_sid: int
    schedule_type: ScheduleType
    def __init__(self, schedule_sid: _Optional[int] = ..., schedule_type: _Optional[_Union[ScheduleType, str]] = ...) -> None: ...

class SkillProfileCategory(_message.Message):
    __slots__ = ("skill_profile_category_sid", "skill_profile_category_type")
    class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SINGLE_SKILL_PROFILE: _ClassVar[SkillProfileCategory.CategoryType]
        SKILL_PROFILE_GROUP: _ClassVar[SkillProfileCategory.CategoryType]
    SINGLE_SKILL_PROFILE: SkillProfileCategory.CategoryType
    SKILL_PROFILE_GROUP: SkillProfileCategory.CategoryType
    SKILL_PROFILE_CATEGORY_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_category_sid: int
    skill_profile_category_type: SkillProfileCategory.CategoryType
    def __init__(self, skill_profile_category_sid: _Optional[int] = ..., skill_profile_category_type: _Optional[_Union[SkillProfileCategory.CategoryType, str]] = ...) -> None: ...

class SchedulingResultMetricForSkillCollection(_message.Message):
    __slots__ = ("total_internal_intervals", "total_intervals_with_fte_required", "total_intervals_with_ftes_remaining", "coverage", "root_mean_square", "has_result", "skill_collection")
    TOTAL_INTERNAL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INTERVALS_WITH_FTE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INTERVALS_WITH_FTES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_MEAN_SQUARE_FIELD_NUMBER: _ClassVar[int]
    HAS_RESULT_FIELD_NUMBER: _ClassVar[int]
    SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    total_internal_intervals: int
    total_intervals_with_fte_required: int
    total_intervals_with_ftes_remaining: int
    coverage: float
    root_mean_square: float
    has_result: bool
    skill_collection: SkillProfileCategory
    def __init__(self, total_internal_intervals: _Optional[int] = ..., total_intervals_with_fte_required: _Optional[int] = ..., total_intervals_with_ftes_remaining: _Optional[int] = ..., coverage: _Optional[float] = ..., root_mean_square: _Optional[float] = ..., has_result: bool = ..., skill_collection: _Optional[_Union[SkillProfileCategory, _Mapping]] = ...) -> None: ...

class SchedulingResultMetric(_message.Message):
    __slots__ = ("total_internal_intervals", "total_intervals_with_fte_required", "total_intervals_with_ftes_remaining", "coverage", "root_mean_square", "has_result", "metrics_by_skill_collection")
    TOTAL_INTERNAL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INTERVALS_WITH_FTE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INTERVALS_WITH_FTES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    ROOT_MEAN_SQUARE_FIELD_NUMBER: _ClassVar[int]
    HAS_RESULT_FIELD_NUMBER: _ClassVar[int]
    METRICS_BY_SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    total_internal_intervals: int
    total_intervals_with_fte_required: int
    total_intervals_with_ftes_remaining: int
    coverage: float
    root_mean_square: float
    has_result: bool
    metrics_by_skill_collection: _containers.RepeatedCompositeFieldContainer[SchedulingResultMetricForSkillCollection]
    def __init__(self, total_internal_intervals: _Optional[int] = ..., total_intervals_with_fte_required: _Optional[int] = ..., total_intervals_with_ftes_remaining: _Optional[int] = ..., coverage: _Optional[float] = ..., root_mean_square: _Optional[float] = ..., has_result: bool = ..., metrics_by_skill_collection: _Optional[_Iterable[_Union[SchedulingResultMetricForSkillCollection, _Mapping]]] = ...) -> None: ...

class ClientHistoryCacheInfo(_message.Message):
    __slots__ = ("state", "progress_percentage")
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    state: HistoryCacheState
    progress_percentage: int
    def __init__(self, state: _Optional[_Union[HistoryCacheState, str]] = ..., progress_percentage: _Optional[int] = ...) -> None: ...

class ErrorTrace(_message.Message):
    __slots__ = ("grpc_trace_bin",)
    GRPC_TRACE_BIN_FIELD_NUMBER: _ClassVar[int]
    grpc_trace_bin: str
    def __init__(self, grpc_trace_bin: _Optional[str] = ...) -> None: ...

class InitialSetupStatus(_message.Message):
    __slots__ = ("state", "progress_percentage", "message")
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    state: InitialSetupState
    progress_percentage: int
    message: str
    def __init__(self, state: _Optional[_Union[InitialSetupState, str]] = ..., progress_percentage: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class AgentStateSegment(_message.Message):
    __slots__ = ("order_in_rts", "states", "width_in_minutes", "width_in_seconds")
    ORDER_IN_RTS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    order_in_rts: int
    states: _containers.RepeatedScalarFieldContainer[RealTimeManagementState]
    width_in_minutes: int
    width_in_seconds: int
    def __init__(self, order_in_rts: _Optional[int] = ..., states: _Optional[_Iterable[_Union[RealTimeManagementState, str]]] = ..., width_in_minutes: _Optional[int] = ..., width_in_seconds: _Optional[int] = ...) -> None: ...

class AgentStateSequence(_message.Message):
    __slots__ = ("wfm_agent_sid", "start_datetime", "state_segments")
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    STATE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    state_segments: _containers.RepeatedCompositeFieldContainer[AgentStateSegment]
    def __init__(self, wfm_agent_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state_segments: _Optional[_Iterable[_Union[AgentStateSegment, _Mapping]]] = ...) -> None: ...

class AgentLeavePetition(_message.Message):
    __slots__ = ("agent_leave_petition_id", "wfm_agent_sid", "petition_status", "petition_comment", "response_comment", "requested_datetime_ranges", "created_time", "archived_time", "resolved_time", "resolved_by_user_id", "requested_hours_off")
    AGENT_LEAVE_PETITION_ID_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    PETITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    PETITION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_DATETIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_HOURS_OFF_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition_id: int
    wfm_agent_sid: int
    petition_status: AgentLeavePetitionStatus
    petition_comment: str
    response_comment: str
    requested_datetime_ranges: _containers.RepeatedCompositeFieldContainer[DatetimeRange]
    created_time: _timestamp_pb2.Timestamp
    archived_time: _timestamp_pb2.Timestamp
    resolved_time: _timestamp_pb2.Timestamp
    resolved_by_user_id: str
    requested_hours_off: float
    def __init__(self, agent_leave_petition_id: _Optional[int] = ..., wfm_agent_sid: _Optional[int] = ..., petition_status: _Optional[_Union[AgentLeavePetitionStatus, str]] = ..., petition_comment: _Optional[str] = ..., response_comment: _Optional[str] = ..., requested_datetime_ranges: _Optional[_Iterable[_Union[DatetimeRange, _Mapping]]] = ..., created_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., archived_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_by_user_id: _Optional[str] = ..., requested_hours_off: _Optional[float] = ...) -> None: ...

class ConfigEntity(_message.Message):
    __slots__ = ("entity_sid", "entity_type")
    ENTITY_SID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    entity_sid: int
    entity_type: ConfigEntityType
    def __init__(self, entity_sid: _Optional[int] = ..., entity_type: _Optional[_Union[ConfigEntityType, str]] = ...) -> None: ...

class AdherenceRuleNotificationConfig(_message.Message):
    __slots__ = ("adherence_rule_notification_config_id", "name")
    ADHERENCE_RULE_NOTIFICATION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    adherence_rule_notification_config_id: int
    name: str
    def __init__(self, adherence_rule_notification_config_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class AdherenceRuleNotificationConfigEntry(_message.Message):
    __slots__ = ("adherence_rule_notification_config_entry_id", "adherence_rule_notification_config_id", "recipient_user_id", "notification_medium", "seconds_to_wait_for_no_response")
    ADHERENCE_RULE_NOTIFICATION_CONFIG_ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ADHERENCE_RULE_NOTIFICATION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_MEDIUM_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TO_WAIT_FOR_NO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    adherence_rule_notification_config_entry_id: int
    adherence_rule_notification_config_id: int
    recipient_user_id: str
    notification_medium: AdherenceRuleNotificationMedium
    seconds_to_wait_for_no_response: int
    def __init__(self, adherence_rule_notification_config_entry_id: _Optional[int] = ..., adherence_rule_notification_config_id: _Optional[int] = ..., recipient_user_id: _Optional[str] = ..., notification_medium: _Optional[_Union[AdherenceRuleNotificationMedium, str]] = ..., seconds_to_wait_for_no_response: _Optional[int] = ...) -> None: ...

class AdherenceDepartmentalRuleAction(_message.Message):
    __slots__ = ("action_type",)
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    action_type: AdherenceDepartmentalRuleActionType
    def __init__(self, action_type: _Optional[_Union[AdherenceDepartmentalRuleActionType, str]] = ...) -> None: ...

class AdherenceDepartmentalRule(_message.Message):
    __slots__ = ("adherence_departmental_rule_id", "name", "selected_entity", "rule_requirement_type", "adherence_rule_notification_config_id", "rule_range", "custom_range")
    ADHERENCE_DEPARTMENTAL_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RULE_REQUIREMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADHERENCE_RULE_NOTIFICATION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_RANGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RANGE_FIELD_NUMBER: _ClassVar[int]
    adherence_departmental_rule_id: int
    name: str
    selected_entity: ConfigEntity
    rule_requirement_type: AdherenceRuleRequirementType
    adherence_rule_notification_config_id: int
    rule_range: AdherenceRuleRange
    custom_range: DatetimeRange
    def __init__(self, adherence_departmental_rule_id: _Optional[int] = ..., name: _Optional[str] = ..., selected_entity: _Optional[_Union[ConfigEntity, _Mapping]] = ..., rule_requirement_type: _Optional[_Union[AdherenceRuleRequirementType, str]] = ..., adherence_rule_notification_config_id: _Optional[int] = ..., rule_range: _Optional[_Union[AdherenceRuleRange, str]] = ..., custom_range: _Optional[_Union[DatetimeRange, _Mapping]] = ...) -> None: ...

class AdherenceDepartmentalRuleClause(_message.Message):
    __slots__ = ("adherence_departmental_rule_clause_id", "adherence_departmental_rule_id", "action", "condition", "amount", "unit", "per_amount", "per_unit")
    ADHERENCE_DEPARTMENTAL_RULE_CLAUSE_ID_FIELD_NUMBER: _ClassVar[int]
    ADHERENCE_DEPARTMENTAL_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    PER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    adherence_departmental_rule_clause_id: int
    adherence_departmental_rule_id: int
    action: AdherenceDepartmentalRuleAction
    condition: AdherenceRuleCondition
    amount: int
    unit: AdherenceRuleUnit
    per_amount: _wrappers_pb2.Int32Value
    per_unit: AdherenceRuleUnit
    def __init__(self, adherence_departmental_rule_clause_id: _Optional[int] = ..., adherence_departmental_rule_id: _Optional[int] = ..., action: _Optional[_Union[AdherenceDepartmentalRuleAction, _Mapping]] = ..., condition: _Optional[_Union[AdherenceRuleCondition, str]] = ..., amount: _Optional[int] = ..., unit: _Optional[_Union[AdherenceRuleUnit, str]] = ..., per_amount: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., per_unit: _Optional[_Union[AdherenceRuleUnit, str]] = ...) -> None: ...

class AdherenceAgentRule(_message.Message):
    __slots__ = ("adherence_agent_rule_id", "name", "selected_entity", "rule_requirement_type", "adherence_rule_notification_config_id")
    ADHERENCE_AGENT_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RULE_REQUIREMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADHERENCE_RULE_NOTIFICATION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    adherence_agent_rule_id: int
    name: str
    selected_entity: ConfigEntity
    rule_requirement_type: AdherenceRuleRequirementType
    adherence_rule_notification_config_id: int
    def __init__(self, adherence_agent_rule_id: _Optional[int] = ..., name: _Optional[str] = ..., selected_entity: _Optional[_Union[ConfigEntity, _Mapping]] = ..., rule_requirement_type: _Optional[_Union[AdherenceRuleRequirementType, str]] = ..., adherence_rule_notification_config_id: _Optional[int] = ...) -> None: ...

class AdherenceAgentRuleAction(_message.Message):
    __slots__ = ("action_type",)
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    action_type: AdherenceAgentRuleActionType
    def __init__(self, action_type: _Optional[_Union[AdherenceAgentRuleActionType, str]] = ...) -> None: ...

class AdherenceAgentRuleClause(_message.Message):
    __slots__ = ("adherence_agent_rule_clause_id", "adherence_agent_rule_id", "action", "condition", "amount", "unit")
    ADHERENCE_AGENT_RULE_CLAUSE_ID_FIELD_NUMBER: _ClassVar[int]
    ADHERENCE_AGENT_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    adherence_agent_rule_clause_id: int
    adherence_agent_rule_id: int
    action: AdherenceAgentRuleAction
    condition: AdherenceRuleCondition
    amount: int
    unit: AdherenceRuleUnit
    def __init__(self, adherence_agent_rule_clause_id: _Optional[int] = ..., adherence_agent_rule_id: _Optional[int] = ..., action: _Optional[_Union[AdherenceAgentRuleAction, _Mapping]] = ..., condition: _Optional[_Union[AdherenceRuleCondition, str]] = ..., amount: _Optional[int] = ..., unit: _Optional[_Union[AdherenceRuleUnit, str]] = ...) -> None: ...
