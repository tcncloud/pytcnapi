from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegressionForecasterModelTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RANDOM_FOREST: _ClassVar[RegressionForecasterModelTypes]
    ADABOOST: _ClassVar[RegressionForecasterModelTypes]
    GRADIENT_BOOSTING: _ClassVar[RegressionForecasterModelTypes]
    LINEAR_REGRESSION: _ClassVar[RegressionForecasterModelTypes]
    LINEAR_AVG: _ClassVar[RegressionForecasterModelTypes]
    SEGMENTED_LINEAR: _ClassVar[RegressionForecasterModelTypes]
    MLP: _ClassVar[RegressionForecasterModelTypes]
    AUTO: _ClassVar[RegressionForecasterModelTypes]

class RegressionForecasterAvgsProcessingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FORECAST: _ClassVar[RegressionForecasterAvgsProcessingType]
    AVERAGES: _ClassVar[RegressionForecasterAvgsProcessingType]
    FIXED_AVERAGES: _ClassVar[RegressionForecasterAvgsProcessingType]

class ConstraintTimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MINUTES: _ClassVar[ConstraintTimeUnit]
    HOURS: _ClassVar[ConstraintTimeUnit]
    SHIFTS: _ClassVar[ConstraintTimeUnit]
    DAYS: _ClassVar[ConstraintTimeUnit]
    WEEKS: _ClassVar[ConstraintTimeUnit]
    MONTHS: _ClassVar[ConstraintTimeUnit]
    YEARS: _ClassVar[ConstraintTimeUnit]

class ConfigEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
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

class ConstraintRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
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
    __slots__ = []
    MUST_NOT: _ClassVar[DOWPlacementType]
    MAY: _ClassVar[DOWPlacementType]
    MUST: _ClassVar[DOWPlacementType]

class OpenTimesOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CLOSED: _ClassVar[OpenTimesOption]
    OPEN: _ClassVar[OpenTimesOption]

class AvailabilityOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AVAILABLE: _ClassVar[AvailabilityOption]
    NOT_AVAILABLE: _ClassVar[AvailabilityOption]
    PREFER_NOT_AVAILABLE: _ClassVar[AvailabilityOption]

class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MON: _ClassVar[DayOfWeek]
    TUE: _ClassVar[DayOfWeek]
    WED: _ClassVar[DayOfWeek]
    THU: _ClassVar[DayOfWeek]
    FRI: _ClassVar[DayOfWeek]
    SAT: _ClassVar[DayOfWeek]
    SUN: _ClassVar[DayOfWeek]

class ConfigRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IS_ASSOCIATED_WITH: _ClassVar[ConfigRelationshipType]
    IS_NOT_ASSOCIATED_WITH: _ClassVar[ConfigRelationshipType]
    IS_MEMBER_OF: _ClassVar[ConfigRelationshipType]

class DiagnosticLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INFORMATION: _ClassVar[DiagnosticLevel]
    SUGGESTION: _ClassVar[DiagnosticLevel]
    WARNING: _ClassVar[DiagnosticLevel]
    DIAGNOSTIC_ERROR: _ClassVar[DiagnosticLevel]
    INTERNAL_ERROR: _ClassVar[DiagnosticLevel]

class DiagnosticCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
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

class PerformanceMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FTE_REQUIRED_VS_ACHIEVED_SIMPLE: _ClassVar[PerformanceMetricType]
    FTE_REQUIRED_VS_ACHIEVED_EXTENDED: _ClassVar[PerformanceMetricType]
    SERVICE_LEVEL_ANALYSIS: _ClassVar[PerformanceMetricType]
    SERVICE_LEVEL_MATRIX: _ClassVar[PerformanceMetricType]
    CONTACT_HANDLING_METRICS: _ClassVar[PerformanceMetricType]
    LOAD_FORECAST: _ClassVar[PerformanceMetricType]

class ScheduleShouldInclude(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ONLY_SHIFT_INSTANCES: _ClassVar[ScheduleShouldInclude]
    ONLY_PERFORMANCE_METRICS: _ClassVar[ScheduleShouldInclude]
    SHIFT_INSTANCES_AND_PERFORMANCE_METRICS: _ClassVar[ScheduleShouldInclude]

class ScheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DRAFT: _ClassVar[ScheduleType]
    PUBLISHED: _ClassVar[ScheduleType]

class SchedulingTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COVERAGE: _ClassVar[SchedulingTargetType]
    SERVICE_LEVEL: _ClassVar[SchedulingTargetType]

class BitmapType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPLETE: _ClassVar[BitmapType]
    ONLY_WEEKMAPS: _ClassVar[BitmapType]
    ONLY_CALENDAR_ITEMS: _ClassVar[BitmapType]
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

class SkillType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
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
    __slots__ = ["start_datetime", "end_datetime"]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    END_DATETIME_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    end_datetime: _timestamp_pb2.Timestamp
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ForecastingParameters(_message.Message):
    __slots__ = ["interval_width_in_minutes", "historical_data_range_in_months", "historical_data_range_start_datetime", "forecast_test_range_in_weeks", "forecast_range_in_weeks", "forecast_datetime_range", "training_data_range_in_months", "training_data_datetime_range", "averages_calculation_range_in_months"]
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
    __slots__ = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
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
    __slots__ = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
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
    __slots__ = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
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
    __slots__ = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
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
    __slots__ = ["profile_tod", "profile_woms", "profile_dow", "profile_moy"]
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
    __slots__ = ["total_calls", "distribution_profile"]
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    total_calls: int
    distribution_profile: DistributionProfile
    def __init__(self, total_calls: _Optional[int] = ..., distribution_profile: _Optional[_Union[DistributionProfile, _Mapping]] = ...) -> None: ...

class CallProfileGroupAvgs(_message.Message):
    __slots__ = ["min_average", "max_average", "distribution_profile"]
    MIN_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    min_average: float
    max_average: float
    distribution_profile: DistributionProfile
    def __init__(self, min_average: _Optional[float] = ..., max_average: _Optional[float] = ..., distribution_profile: _Optional[_Union[DistributionProfile, _Mapping]] = ...) -> None: ...

class OptionTypes(_message.Message):
    __slots__ = ["open_times_option", "availability_option"]
    OPEN_TIMES_OPTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_OPTION_FIELD_NUMBER: _ClassVar[int]
    open_times_option: OpenTimesOption
    availability_option: AvailabilityOption
    def __init__(self, open_times_option: _Optional[_Union[OpenTimesOption, str]] = ..., availability_option: _Optional[_Union[AvailabilityOption, str]] = ...) -> None: ...

class ScheduleSelector(_message.Message):
    __slots__ = ["schedule_sid", "schedule_type"]
    SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    schedule_sid: int
    schedule_type: ScheduleType
    def __init__(self, schedule_sid: _Optional[int] = ..., schedule_type: _Optional[_Union[ScheduleType, str]] = ...) -> None: ...

class SkillProfileCategory(_message.Message):
    __slots__ = ["skill_profile_category_sid", "skill_profile_category_type"]
    class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        SINGLE_SKILL_PROFILE: _ClassVar[SkillProfileCategory.CategoryType]
        SKILL_PROFILE_GROUP: _ClassVar[SkillProfileCategory.CategoryType]
    SINGLE_SKILL_PROFILE: SkillProfileCategory.CategoryType
    SKILL_PROFILE_GROUP: SkillProfileCategory.CategoryType
    SKILL_PROFILE_CATEGORY_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_category_sid: int
    skill_profile_category_type: SkillProfileCategory.CategoryType
    def __init__(self, skill_profile_category_sid: _Optional[int] = ..., skill_profile_category_type: _Optional[_Union[SkillProfileCategory.CategoryType, str]] = ...) -> None: ...
