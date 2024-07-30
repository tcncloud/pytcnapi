from annotations import authz_pb2 as _authz_pb2
from api.commons import org_pb2 as _org_pb2
from api.commons import wfm_pb2 as _wfm_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerformInitialClientSetupRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PerformInitialClientSetupResponse(_message.Message):
    __slots__ = ("setup_status",)
    SETUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    setup_status: _wfm_pb2.InitialSetupStatus
    def __init__(self, setup_status: _Optional[_Union[_wfm_pb2.InitialSetupStatus, _Mapping]] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("skill_sid", "client_skill_type", "name", "delete_date", "client_skill_sid", "proficiency")
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SKILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_DATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
    skill_sid: int
    client_skill_type: _wfm_pb2.SkillType.Enum
    name: str
    delete_date: _timestamp_pb2.Timestamp
    client_skill_sid: int
    proficiency: int
    def __init__(self, skill_sid: _Optional[int] = ..., client_skill_type: _Optional[_Union[_wfm_pb2.SkillType.Enum, str]] = ..., name: _Optional[str] = ..., delete_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., client_skill_sid: _Optional[int] = ..., proficiency: _Optional[int] = ...) -> None: ...

class SkillProfile(_message.Message):
    __slots__ = ("skill_profile_sid", "name", "description", "create_date", "unnamed", "inactive_as_of_date", "skills", "skills_count", "occurrence", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "are_averages_manual")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    UNNAMED_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SKILLS_COUNT_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ARE_AVERAGES_MANUAL_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    name: str
    description: str
    create_date: _timestamp_pb2.Timestamp
    unnamed: bool
    inactive_as_of_date: _timestamp_pb2.Timestamp
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    skills_count: int
    occurrence: float
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    are_averages_manual: bool
    def __init__(self, skill_profile_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., create_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., unnamed: bool = ..., inactive_as_of_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., skills_count: _Optional[int] = ..., occurrence: _Optional[float] = ..., average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., are_averages_manual: bool = ...) -> None: ...

class SkillProfileGroup(_message.Message):
    __slots__ = ("skill_profile_group_sid", "name", "description", "create_time", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "are_averages_manual", "skill_profile_sids", "datetime_set_to_inactive")
    SKILL_PROFILE_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ARE_AVERAGES_MANUAL_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group_sid: int
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    are_averages_manual: bool
    skill_profile_sids: _containers.RepeatedScalarFieldContainer[int]
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    def __init__(self, skill_profile_group_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., are_averages_manual: bool = ..., skill_profile_sids: _Optional[_Iterable[int]] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSkillProfilesReq(_message.Message):
    __slots__ = ("active_only", "with_skills")
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    WITH_SKILLS_FIELD_NUMBER: _ClassVar[int]
    active_only: bool
    with_skills: bool
    def __init__(self, active_only: bool = ..., with_skills: bool = ...) -> None: ...

class ListSkillProfilesRes(_message.Message):
    __slots__ = ("skill_profiles",)
    SKILL_PROFILES_FIELD_NUMBER: _ClassVar[int]
    skill_profiles: _containers.RepeatedCompositeFieldContainer[SkillProfile]
    def __init__(self, skill_profiles: _Optional[_Iterable[_Union[SkillProfile, _Mapping]]] = ...) -> None: ...

class UpdateSkillProfileReq(_message.Message):
    __slots__ = ("skill_profile_sid", "name", "description", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "are_averages_manual")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ARE_AVERAGES_MANUAL_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    name: str
    description: str
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    are_averages_manual: bool
    def __init__(self, skill_profile_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., are_averages_manual: bool = ...) -> None: ...

class UpdateSkillProfileRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSkillProfileProficienciesReq(_message.Message):
    __slots__ = ("proficiencies",)
    class Proficiency(_message.Message):
        __slots__ = ("skill_profile_sid", "skill_sid", "proficiency")
        SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
        SKILL_SID_FIELD_NUMBER: _ClassVar[int]
        PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
        skill_profile_sid: int
        skill_sid: int
        proficiency: int
        def __init__(self, skill_profile_sid: _Optional[int] = ..., skill_sid: _Optional[int] = ..., proficiency: _Optional[int] = ...) -> None: ...
    PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    proficiencies: _containers.RepeatedCompositeFieldContainer[UpdateSkillProfileProficienciesReq.Proficiency]
    def __init__(self, proficiencies: _Optional[_Iterable[_Union[UpdateSkillProfileProficienciesReq.Proficiency, _Mapping]]] = ...) -> None: ...

class UpdateSkillProfileProficienciesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSkillProfileReq(_message.Message):
    __slots__ = ("skill_profile_sid",)
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    def __init__(self, skill_profile_sid: _Optional[int] = ...) -> None: ...

class GetSkillProfileRes(_message.Message):
    __slots__ = ("skill_profile", "mappings")
    class Mapping(_message.Message):
        __slots__ = ("skill_profile_sid", "name")
        SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        skill_profile_sid: int
        name: str
        def __init__(self, skill_profile_sid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    SKILL_PROFILE_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    skill_profile: SkillProfile
    mappings: _containers.RepeatedCompositeFieldContainer[GetSkillProfileRes.Mapping]
    def __init__(self, skill_profile: _Optional[_Union[SkillProfile, _Mapping]] = ..., mappings: _Optional[_Iterable[_Union[GetSkillProfileRes.Mapping, _Mapping]]] = ...) -> None: ...

class ResyncSkillProfilesReq(_message.Message):
    __slots__ = ("from_historical_range_start_date",)
    FROM_HISTORICAL_RANGE_START_DATE_FIELD_NUMBER: _ClassVar[int]
    from_historical_range_start_date: bool
    def __init__(self, from_historical_range_start_date: bool = ...) -> None: ...

class ResyncSkillProfilesRes(_message.Message):
    __slots__ = ("created_skill_profile_sids",)
    CREATED_SKILL_PROFILE_SIDS_FIELD_NUMBER: _ClassVar[int]
    created_skill_profile_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, created_skill_profile_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetLastSkillProfileResyncDateReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLastSkillProfileResyncDateRes(_message.Message):
    __slots__ = ("resync_date",)
    RESYNC_DATE_FIELD_NUMBER: _ClassVar[int]
    resync_date: _timestamp_pb2.Timestamp
    def __init__(self, resync_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpsertForecastingParametersReq(_message.Message):
    __slots__ = ("forecasting_parameters",)
    FORECASTING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    forecasting_parameters: _wfm_pb2.ForecastingParameters
    def __init__(self, forecasting_parameters: _Optional[_Union[_wfm_pb2.ForecastingParameters, _Mapping]] = ...) -> None: ...

class UpsertForecastingParametersRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetForecastingParametersReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetForecastingParametersRes(_message.Message):
    __slots__ = ("forecasting_parameters",)
    FORECASTING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    forecasting_parameters: _wfm_pb2.ForecastingParameters
    def __init__(self, forecasting_parameters: _Optional[_Union[_wfm_pb2.ForecastingParameters, _Mapping]] = ...) -> None: ...

class HistoricalDataInterval(_message.Message):
    __slots__ = ("start_datetime", "skill_profile_sid", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "total_calls", "total_abandoned_calls", "is_delta", "original_average_speed_of_answer_in_seconds", "original_average_handle_time_in_seconds", "original_average_after_call_work_in_seconds", "original_average_time_to_abort_in_seconds", "original_total_calls", "original_total_abandoned_calls", "skill_profile_category")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ABANDONED_CALLS_FIELD_NUMBER: _ClassVar[int]
    IS_DELTA_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TOTAL_ABANDONED_CALLS_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    skill_profile_sid: int
    average_speed_of_answer_in_seconds: _wrappers_pb2.FloatValue
    average_handle_time_in_seconds: _wrappers_pb2.FloatValue
    average_after_call_work_in_seconds: _wrappers_pb2.FloatValue
    average_time_to_abort_in_seconds: _wrappers_pb2.FloatValue
    total_calls: int
    total_abandoned_calls: int
    is_delta: bool
    original_average_speed_of_answer_in_seconds: _wrappers_pb2.FloatValue
    original_average_handle_time_in_seconds: _wrappers_pb2.FloatValue
    original_average_after_call_work_in_seconds: _wrappers_pb2.FloatValue
    original_average_time_to_abort_in_seconds: _wrappers_pb2.FloatValue
    original_total_calls: int
    original_total_abandoned_calls: int
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skill_profile_sid: _Optional[int] = ..., average_speed_of_answer_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., average_handle_time_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., average_after_call_work_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., average_time_to_abort_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., total_calls: _Optional[int] = ..., total_abandoned_calls: _Optional[int] = ..., is_delta: bool = ..., original_average_speed_of_answer_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., original_average_handle_time_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., original_average_after_call_work_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., original_average_time_to_abort_in_seconds: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., original_total_calls: _Optional[int] = ..., original_total_abandoned_calls: _Optional[int] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class GetClientHistoryCacheInfoReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClientHistoryCacheInfoRes(_message.Message):
    __slots__ = ("cache_info",)
    CACHE_INFO_FIELD_NUMBER: _ClassVar[int]
    cache_info: _wfm_pb2.ClientHistoryCacheInfo
    def __init__(self, cache_info: _Optional[_Union[_wfm_pb2.ClientHistoryCacheInfo, _Mapping]] = ...) -> None: ...

class ListHistoricalDataReq(_message.Message):
    __slots__ = ("skill_profile_sid", "skill_profile_category")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, skill_profile_sid: _Optional[int] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class ListHistoricalDataRes(_message.Message):
    __slots__ = ("historical_data_intervals",)
    HISTORICAL_DATA_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    historical_data_intervals: _containers.RepeatedCompositeFieldContainer[HistoricalDataInterval]
    def __init__(self, historical_data_intervals: _Optional[_Iterable[_Union[HistoricalDataInterval, _Mapping]]] = ...) -> None: ...

class UpsertHistoricalDataDeltaReq(_message.Message):
    __slots__ = ("delta",)
    DELTA_FIELD_NUMBER: _ClassVar[int]
    delta: HistoricalDataInterval
    def __init__(self, delta: _Optional[_Union[HistoricalDataInterval, _Mapping]] = ...) -> None: ...

class UpsertHistoricalDataDeltaRes(_message.Message):
    __slots__ = ("delta",)
    DELTA_FIELD_NUMBER: _ClassVar[int]
    delta: HistoricalDataInterval
    def __init__(self, delta: _Optional[_Union[HistoricalDataInterval, _Mapping]] = ...) -> None: ...

class UpsertHistoricalDataDeltasReq(_message.Message):
    __slots__ = ("deltas",)
    DELTAS_FIELD_NUMBER: _ClassVar[int]
    deltas: _containers.RepeatedCompositeFieldContainer[HistoricalDataInterval]
    def __init__(self, deltas: _Optional[_Iterable[_Union[HistoricalDataInterval, _Mapping]]] = ...) -> None: ...

class UpsertHistoricalDataDeltasRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillsRes(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    def __init__(self, skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ...) -> None: ...

class CallProfileTemplate(_message.Message):
    __slots__ = ("call_profile_template_sid", "name", "total_calls_profile", "total_abandoned_calls_profile", "average_speed_of_answer_profile", "average_handle_time_profile", "average_after_call_work_profile", "average_time_to_abort_profile", "fixed_average_speed_of_answer", "fixed_average_handle_time", "fixed_average_after_call_work", "fixed_average_time_to_abort", "default_to_fixed_averages_forecast", "time_zone")
    CALL_PROFILE_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_PROFILE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ABANDONED_CALLS_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGE_SPEED_OF_ANSWER_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGE_HANDLE_TIME_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGE_AFTER_CALL_WORK_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGE_TIME_TO_ABORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TO_FIXED_AVERAGES_FORECAST_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    call_profile_template_sid: int
    name: str
    total_calls_profile: _wfm_pb2.CallProfileGroupCalls
    total_abandoned_calls_profile: _wfm_pb2.CallProfileGroupCalls
    average_speed_of_answer_profile: _wfm_pb2.CallProfileGroupAvgs
    average_handle_time_profile: _wfm_pb2.CallProfileGroupAvgs
    average_after_call_work_profile: _wfm_pb2.CallProfileGroupAvgs
    average_time_to_abort_profile: _wfm_pb2.CallProfileGroupAvgs
    fixed_average_speed_of_answer: float
    fixed_average_handle_time: float
    fixed_average_after_call_work: float
    fixed_average_time_to_abort: float
    default_to_fixed_averages_forecast: bool
    time_zone: str
    def __init__(self, call_profile_template_sid: _Optional[int] = ..., name: _Optional[str] = ..., total_calls_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupCalls, _Mapping]] = ..., total_abandoned_calls_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupCalls, _Mapping]] = ..., average_speed_of_answer_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupAvgs, _Mapping]] = ..., average_handle_time_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupAvgs, _Mapping]] = ..., average_after_call_work_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupAvgs, _Mapping]] = ..., average_time_to_abort_profile: _Optional[_Union[_wfm_pb2.CallProfileGroupAvgs, _Mapping]] = ..., fixed_average_speed_of_answer: _Optional[float] = ..., fixed_average_handle_time: _Optional[float] = ..., fixed_average_after_call_work: _Optional[float] = ..., fixed_average_time_to_abort: _Optional[float] = ..., default_to_fixed_averages_forecast: bool = ..., time_zone: _Optional[str] = ...) -> None: ...

class BuildCallProfileTemplateForSkillProfileReq(_message.Message):
    __slots__ = ("skill_profile_sid", "time_zone")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    time_zone: str
    def __init__(self, skill_profile_sid: _Optional[int] = ..., time_zone: _Optional[str] = ...) -> None: ...

class BuildCallProfileTemplateForSkillProfileRes(_message.Message):
    __slots__ = ("call_profile_template",)
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    call_profile_template: CallProfileTemplate
    def __init__(self, call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ...) -> None: ...

class BuildCallProfileTemplateReq(_message.Message):
    __slots__ = ("skill_profile_category", "time_zone")
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    time_zone: str
    def __init__(self, skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ..., time_zone: _Optional[str] = ...) -> None: ...

class BuildCallProfileTemplateRes(_message.Message):
    __slots__ = ("call_profile_template",)
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    call_profile_template: CallProfileTemplate
    def __init__(self, call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ...) -> None: ...

class CreateInactiveSkillProfileMappingReq(_message.Message):
    __slots__ = ("inactive_skill_profile_sid", "active_skill_profile_sid")
    INACTIVE_SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    inactive_skill_profile_sid: int
    active_skill_profile_sid: int
    def __init__(self, inactive_skill_profile_sid: _Optional[int] = ..., active_skill_profile_sid: _Optional[int] = ...) -> None: ...

class CreateInactiveSkillProfileMappingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAvailableRegressionForecasterModelTypesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAvailableRegressionForecasterModelTypesRes(_message.Message):
    __slots__ = ("model_types",)
    MODEL_TYPES_FIELD_NUMBER: _ClassVar[int]
    model_types: _containers.RepeatedScalarFieldContainer[_wfm_pb2.RegressionForecasterModelTypes]
    def __init__(self, model_types: _Optional[_Iterable[_Union[_wfm_pb2.RegressionForecasterModelTypes, str]]] = ...) -> None: ...

class DisconnectInactiveSkillProfileMappingReq(_message.Message):
    __slots__ = ("inactive_skill_profile_sid",)
    INACTIVE_SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    inactive_skill_profile_sid: int
    def __init__(self, inactive_skill_profile_sid: _Optional[int] = ...) -> None: ...

class DisconnectInactiveSkillProfileMappingRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSkillProfileGroupReq(_message.Message):
    __slots__ = ("skill_profile_group",)
    SKILL_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group: SkillProfileGroup
    def __init__(self, skill_profile_group: _Optional[_Union[SkillProfileGroup, _Mapping]] = ...) -> None: ...

class CreateSkillProfileGroupRes(_message.Message):
    __slots__ = ("skill_profile_group_sid",)
    SKILL_PROFILE_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group_sid: int
    def __init__(self, skill_profile_group_sid: _Optional[int] = ...) -> None: ...

class UpdateSkillProfileGroupReq(_message.Message):
    __slots__ = ("skill_profile_group",)
    SKILL_PROFILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group: SkillProfileGroup
    def __init__(self, skill_profile_group: _Optional[_Union[SkillProfileGroup, _Mapping]] = ...) -> None: ...

class UpdateSkillProfileGroupRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSkillProfileGroupsReq(_message.Message):
    __slots__ = ("skill_profile_group_sids", "include_inactive")
    SKILL_PROFILE_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group_sids: _containers.RepeatedScalarFieldContainer[int]
    include_inactive: bool
    def __init__(self, skill_profile_group_sids: _Optional[_Iterable[int]] = ..., include_inactive: bool = ...) -> None: ...

class ListSkillProfileGroupsRes(_message.Message):
    __slots__ = ("skill_profile_groups",)
    SKILL_PROFILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    skill_profile_groups: _containers.RepeatedCompositeFieldContainer[SkillProfileGroup]
    def __init__(self, skill_profile_groups: _Optional[_Iterable[_Union[SkillProfileGroup, _Mapping]]] = ...) -> None: ...

class UpdateSkillProfileGroupAssociationsReq(_message.Message):
    __slots__ = ("skill_profile_group_sid", "skill_profile_sids_to_associate", "skill_profile_sids_to_disassociate")
    SKILL_PROFILE_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_TO_ASSOCIATE_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_TO_DISASSOCIATE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_group_sid: int
    skill_profile_sids_to_associate: _containers.RepeatedScalarFieldContainer[int]
    skill_profile_sids_to_disassociate: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skill_profile_group_sid: _Optional[int] = ..., skill_profile_sids_to_associate: _Optional[_Iterable[int]] = ..., skill_profile_sids_to_disassociate: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateSkillProfileGroupAssociationsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteHistoricalDataDeltasReq(_message.Message):
    __slots__ = ("skill_profile_sid", "start_datetimes")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIMES_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    start_datetimes: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, skill_profile_sid: _Optional[int] = ..., start_datetimes: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class DeleteHistoricalDataDeltasRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTopSkillProfilesReq(_message.Message):
    __slots__ = ("max_number_of_profiles",)
    MAX_NUMBER_OF_PROFILES_FIELD_NUMBER: _ClassVar[int]
    max_number_of_profiles: int
    def __init__(self, max_number_of_profiles: _Optional[int] = ...) -> None: ...

class ListTopSkillProfilesRes(_message.Message):
    __slots__ = ("skill_profiles",)
    SKILL_PROFILES_FIELD_NUMBER: _ClassVar[int]
    skill_profiles: _containers.RepeatedCompositeFieldContainer[SkillProfile]
    def __init__(self, skill_profiles: _Optional[_Iterable[_Union[SkillProfile, _Mapping]]] = ...) -> None: ...

class GetSkillProfilesCountReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSkillProfilesCountRes(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class BuildProfileForecastByIntervalReq(_message.Message):
    __slots__ = ("call_profile_template", "fixed_averages_forecast", "skill_profile_sid", "skill_profile_category")
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGES_FORECAST_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    call_profile_template: CallProfileTemplate
    fixed_averages_forecast: bool
    skill_profile_sid: int
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ..., fixed_averages_forecast: bool = ..., skill_profile_sid: _Optional[int] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class CallDataByInterval(_message.Message):
    __slots__ = ("start_datetime", "skill_profile_sid", "total_calls", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "total_abandoned_calls", "is_delta", "forecast_data_interval_sid", "interval_width_in_minutes", "skill_profile_category")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ABANDONED_CALLS_FIELD_NUMBER: _ClassVar[int]
    IS_DELTA_FIELD_NUMBER: _ClassVar[int]
    FORECAST_DATA_INTERVAL_SID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    skill_profile_sid: int
    total_calls: int
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    total_abandoned_calls: int
    is_delta: bool
    forecast_data_interval_sid: int
    interval_width_in_minutes: int
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skill_profile_sid: _Optional[int] = ..., total_calls: _Optional[int] = ..., average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., total_abandoned_calls: _Optional[int] = ..., is_delta: bool = ..., forecast_data_interval_sid: _Optional[int] = ..., interval_width_in_minutes: _Optional[int] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class BuildProfileForecastByIntervalWithStatsReq(_message.Message):
    __slots__ = ("call_profile_template", "fixed_averages_forecast", "skill_profile_sid", "skill_profile_category")
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGES_FORECAST_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    call_profile_template: CallProfileTemplate
    fixed_averages_forecast: bool
    skill_profile_sid: int
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ..., fixed_averages_forecast: bool = ..., skill_profile_sid: _Optional[int] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class BuildProfileForecastByIntervalWithStatsRes(_message.Message):
    __slots__ = ("call_data", "forecast_stats")
    CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    FORECAST_STATS_FIELD_NUMBER: _ClassVar[int]
    call_data: CallDataByInterval
    forecast_stats: GetForecastStatisticsRes
    def __init__(self, call_data: _Optional[_Union[CallDataByInterval, _Mapping]] = ..., forecast_stats: _Optional[_Union[GetForecastStatisticsRes, _Mapping]] = ...) -> None: ...

class UpsertProfileForecastReq(_message.Message):
    __slots__ = ("skill_profile_sid", "call_profile_template", "fixed_averages_forecast", "skill_profile_category")
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FIXED_AVERAGES_FORECAST_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    call_profile_template: CallProfileTemplate
    fixed_averages_forecast: bool
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, skill_profile_sid: _Optional[int] = ..., call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ..., fixed_averages_forecast: bool = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class UpsertProfileForecastRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCallProfileTemplateReq(_message.Message):
    __slots__ = ("call_profile_template",)
    CALL_PROFILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    call_profile_template: CallProfileTemplate
    def __init__(self, call_profile_template: _Optional[_Union[CallProfileTemplate, _Mapping]] = ...) -> None: ...

class CreateCallProfileTemplateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCallProfileTemplateReq(_message.Message):
    __slots__ = ("call_profile_template_sid",)
    CALL_PROFILE_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    call_profile_template_sid: int
    def __init__(self, call_profile_template_sid: _Optional[int] = ...) -> None: ...

class DeleteCallProfileTemplateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegressionTemplate(_message.Message):
    __slots__ = ("regression_template_sid", "name", "model_type", "exclude_call_data_for_n_weeks", "num_weeks_ago_to_emphasize", "max_deviation", "trend_sensitivity", "exclude_intervals_with_no_calls", "avgs_processing_type", "include_seasonality", "include_trend")
    REGRESSION_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CALL_DATA_FOR_N_WEEKS_FIELD_NUMBER: _ClassVar[int]
    NUM_WEEKS_AGO_TO_EMPHASIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    TREND_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_INTERVALS_WITH_NO_CALLS_FIELD_NUMBER: _ClassVar[int]
    AVGS_PROCESSING_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SEASONALITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TREND_FIELD_NUMBER: _ClassVar[int]
    regression_template_sid: int
    name: str
    model_type: _wfm_pb2.RegressionForecasterModelTypes
    exclude_call_data_for_n_weeks: int
    num_weeks_ago_to_emphasize: int
    max_deviation: float
    trend_sensitivity: float
    exclude_intervals_with_no_calls: bool
    avgs_processing_type: _wfm_pb2.RegressionForecasterAvgsProcessingType
    include_seasonality: bool
    include_trend: bool
    def __init__(self, regression_template_sid: _Optional[int] = ..., name: _Optional[str] = ..., model_type: _Optional[_Union[_wfm_pb2.RegressionForecasterModelTypes, str]] = ..., exclude_call_data_for_n_weeks: _Optional[int] = ..., num_weeks_ago_to_emphasize: _Optional[int] = ..., max_deviation: _Optional[float] = ..., trend_sensitivity: _Optional[float] = ..., exclude_intervals_with_no_calls: bool = ..., avgs_processing_type: _Optional[_Union[_wfm_pb2.RegressionForecasterAvgsProcessingType, str]] = ..., include_seasonality: bool = ..., include_trend: bool = ...) -> None: ...

class CreateRegressionTemplateReq(_message.Message):
    __slots__ = ("regression_template",)
    REGRESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    regression_template: RegressionTemplate
    def __init__(self, regression_template: _Optional[_Union[RegressionTemplate, _Mapping]] = ...) -> None: ...

class CreateRegressionTemplateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRegressionTemplateReq(_message.Message):
    __slots__ = ("regression_template_sid",)
    REGRESSION_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    regression_template_sid: int
    def __init__(self, regression_template_sid: _Optional[int] = ...) -> None: ...

class DeleteRegressionTemplateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRegressionTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRegressionTemplatesRes(_message.Message):
    __slots__ = ("regression_templates",)
    REGRESSION_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    regression_templates: _containers.RepeatedCompositeFieldContainer[RegressionTemplate]
    def __init__(self, regression_templates: _Optional[_Iterable[_Union[RegressionTemplate, _Mapping]]] = ...) -> None: ...

class BuildRegressionForecastByIntervalReq(_message.Message):
    __slots__ = ("average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "regression_template", "skill_profile_sids_to_forecast")
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REGRESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_TO_FORECAST_FIELD_NUMBER: _ClassVar[int]
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    regression_template: RegressionTemplate
    skill_profile_sids_to_forecast: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., regression_template: _Optional[_Union[RegressionTemplate, _Mapping]] = ..., skill_profile_sids_to_forecast: _Optional[_Iterable[int]] = ...) -> None: ...

class BuildRegressionForecastByIntervalWithStatsReq(_message.Message):
    __slots__ = ("average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "regression_template", "skill_profile_sids_to_forecast")
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REGRESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_TO_FORECAST_FIELD_NUMBER: _ClassVar[int]
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    regression_template: RegressionTemplate
    skill_profile_sids_to_forecast: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., regression_template: _Optional[_Union[RegressionTemplate, _Mapping]] = ..., skill_profile_sids_to_forecast: _Optional[_Iterable[int]] = ...) -> None: ...

class GetForecastStatisticsRes(_message.Message):
    __slots__ = ("num_intervals_measured", "total_calls_historical", "total_calls_predicted", "percent_calls_over_under", "rms_error_calls", "rms_error_ATAB", "rms_error_ASA", "rms_error_ACW", "rms_error_AHT", "are_stats_invalid", "invalid_reason")
    NUM_INTERVALS_MEASURED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_HISTORICAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_PREDICTED_FIELD_NUMBER: _ClassVar[int]
    PERCENT_CALLS_OVER_UNDER_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_CALLS_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_ATAB_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_ASA_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_ACW_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_AHT_FIELD_NUMBER: _ClassVar[int]
    ARE_STATS_INVALID_FIELD_NUMBER: _ClassVar[int]
    INVALID_REASON_FIELD_NUMBER: _ClassVar[int]
    num_intervals_measured: int
    total_calls_historical: int
    total_calls_predicted: int
    percent_calls_over_under: float
    rms_error_calls: float
    rms_error_ATAB: float
    rms_error_ASA: float
    rms_error_ACW: float
    rms_error_AHT: float
    are_stats_invalid: bool
    invalid_reason: str
    def __init__(self, num_intervals_measured: _Optional[int] = ..., total_calls_historical: _Optional[int] = ..., total_calls_predicted: _Optional[int] = ..., percent_calls_over_under: _Optional[float] = ..., rms_error_calls: _Optional[float] = ..., rms_error_ATAB: _Optional[float] = ..., rms_error_ASA: _Optional[float] = ..., rms_error_ACW: _Optional[float] = ..., rms_error_AHT: _Optional[float] = ..., are_stats_invalid: bool = ..., invalid_reason: _Optional[str] = ...) -> None: ...

class BuildRegressionForecastByIntervalWithStatsRes(_message.Message):
    __slots__ = ("call_data", "forecast_stats")
    CALL_DATA_FIELD_NUMBER: _ClassVar[int]
    FORECAST_STATS_FIELD_NUMBER: _ClassVar[int]
    call_data: CallDataByInterval
    forecast_stats: GetForecastStatisticsRes
    def __init__(self, call_data: _Optional[_Union[CallDataByInterval, _Mapping]] = ..., forecast_stats: _Optional[_Union[GetForecastStatisticsRes, _Mapping]] = ...) -> None: ...

class ListCallProfileTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCallProfileTemplatesRes(_message.Message):
    __slots__ = ("call_profile_templates",)
    CALL_PROFILE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    call_profile_templates: _containers.RepeatedCompositeFieldContainer[CallProfileTemplate]
    def __init__(self, call_profile_templates: _Optional[_Iterable[_Union[CallProfileTemplate, _Mapping]]] = ...) -> None: ...

class ListForecastIntervalsForSkillProfileReq(_message.Message):
    __slots__ = ("skill_profile_sid",)
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    def __init__(self, skill_profile_sid: _Optional[int] = ...) -> None: ...

class ListForecastIntervalsReq(_message.Message):
    __slots__ = ("skill_profile_category",)
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class UpsertRegressionForecastReq(_message.Message):
    __slots__ = ("regression_template", "average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds", "skill_profile_sids_to_forecast")
    REGRESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_SIDS_TO_FORECAST_FIELD_NUMBER: _ClassVar[int]
    regression_template: RegressionTemplate
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    skill_profile_sids_to_forecast: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, regression_template: _Optional[_Union[RegressionTemplate, _Mapping]] = ..., average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ..., skill_profile_sids_to_forecast: _Optional[_Iterable[int]] = ...) -> None: ...

class UpsertRegressionForecastRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpsertForecastDataDeltaReq(_message.Message):
    __slots__ = ("delta",)
    DELTA_FIELD_NUMBER: _ClassVar[int]
    delta: CallDataByInterval
    def __init__(self, delta: _Optional[_Union[CallDataByInterval, _Mapping]] = ...) -> None: ...

class UpsertForecastDataDeltaRes(_message.Message):
    __slots__ = ("delta",)
    DELTA_FIELD_NUMBER: _ClassVar[int]
    delta: CallDataByInterval
    def __init__(self, delta: _Optional[_Union[CallDataByInterval, _Mapping]] = ...) -> None: ...

class UpsertForecastDataDeltasReq(_message.Message):
    __slots__ = ("deltas",)
    DELTAS_FIELD_NUMBER: _ClassVar[int]
    deltas: _containers.RepeatedCompositeFieldContainer[CallDataByInterval]
    def __init__(self, deltas: _Optional[_Iterable[_Union[CallDataByInterval, _Mapping]]] = ...) -> None: ...

class UpsertForecastDataDeltasRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteForecastIntervalsReq(_message.Message):
    __slots__ = ("skill_profile_sid", "forecast_interval_sids", "skill_profile_category", "forecast_interval_delete_type")
    class ForecastIntervalDeleteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERVALS_AND_DELTAS: _ClassVar[DeleteForecastIntervalsReq.ForecastIntervalDeleteType]
        DELTAS: _ClassVar[DeleteForecastIntervalsReq.ForecastIntervalDeleteType]
    INTERVALS_AND_DELTAS: DeleteForecastIntervalsReq.ForecastIntervalDeleteType
    DELTAS: DeleteForecastIntervalsReq.ForecastIntervalDeleteType
    class IntervalSids(_message.Message):
        __slots__ = ("sids",)
        SIDS_FIELD_NUMBER: _ClassVar[int]
        sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, sids: _Optional[_Iterable[int]] = ...) -> None: ...
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    FORECAST_INTERVAL_SIDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FORECAST_INTERVAL_DELETE_TYPE_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    forecast_interval_sids: DeleteForecastIntervalsReq.IntervalSids
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    forecast_interval_delete_type: DeleteForecastIntervalsReq.ForecastIntervalDeleteType
    def __init__(self, skill_profile_sid: _Optional[int] = ..., forecast_interval_sids: _Optional[_Union[DeleteForecastIntervalsReq.IntervalSids, _Mapping]] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ..., forecast_interval_delete_type: _Optional[_Union[DeleteForecastIntervalsReq.ForecastIntervalDeleteType, str]] = ...) -> None: ...

class DeleteForecastIntervalsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHistoricalDataForAllSkillProfilesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListHistoricalDataForAllSkillProfilesRes(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[HistoricalDataInterval]
    def __init__(self, history: _Optional[_Iterable[_Union[HistoricalDataInterval, _Mapping]]] = ...) -> None: ...

class BuildDOWAndMOYProfilesReq(_message.Message):
    __slots__ = ("profile_tod", "profile_woms", "is_average_profile")
    PROFILE_TOD_FIELD_NUMBER: _ClassVar[int]
    PROFILE_WOMS_FIELD_NUMBER: _ClassVar[int]
    IS_AVERAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile_tod: _wfm_pb2.ProfileTOD
    profile_woms: _wfm_pb2.ProfileWOMS
    is_average_profile: bool
    def __init__(self, profile_tod: _Optional[_Union[_wfm_pb2.ProfileTOD, _Mapping]] = ..., profile_woms: _Optional[_Union[_wfm_pb2.ProfileWOMS, _Mapping]] = ..., is_average_profile: bool = ...) -> None: ...

class BuildDOWAndMOYProfilesRes(_message.Message):
    __slots__ = ("profile_dow", "profile_moy")
    PROFILE_DOW_FIELD_NUMBER: _ClassVar[int]
    PROFILE_MOY_FIELD_NUMBER: _ClassVar[int]
    profile_dow: _wfm_pb2.ProfileDOW
    profile_moy: _wfm_pb2.ProfileMOY
    def __init__(self, profile_dow: _Optional[_Union[_wfm_pb2.ProfileDOW, _Mapping]] = ..., profile_moy: _Optional[_Union[_wfm_pb2.ProfileMOY, _Mapping]] = ...) -> None: ...

class CalculateTrainingDataAveragesForSkillProfileReq(_message.Message):
    __slots__ = ("skill_profile_sid",)
    SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sid: int
    def __init__(self, skill_profile_sid: _Optional[int] = ...) -> None: ...

class CalculateTrainingDataAveragesForSkillProfileRes(_message.Message):
    __slots__ = ("average_speed_of_answer_in_seconds", "average_handle_time_in_seconds", "average_after_call_work_in_seconds", "average_time_to_abort_in_seconds")
    AVERAGE_SPEED_OF_ANSWER_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_HANDLE_TIME_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AFTER_CALL_WORK_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TIME_TO_ABORT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    average_speed_of_answer_in_seconds: float
    average_handle_time_in_seconds: float
    average_after_call_work_in_seconds: float
    average_time_to_abort_in_seconds: float
    def __init__(self, average_speed_of_answer_in_seconds: _Optional[float] = ..., average_handle_time_in_seconds: _Optional[float] = ..., average_after_call_work_in_seconds: _Optional[float] = ..., average_time_to_abort_in_seconds: _Optional[float] = ...) -> None: ...

class UpdateSkillProfileAveragesUsingHistoricalDataReq(_message.Message):
    __slots__ = ("skill_profile_sids", "datetime_range", "exclude_skill_profiles_with_manual_averages", "skill_profile_group_sids")
    SKILL_PROFILE_SIDS_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SKILL_PROFILES_WITH_MANUAL_AVERAGES_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    skill_profile_sids: _containers.RepeatedScalarFieldContainer[int]
    datetime_range: _wfm_pb2.DatetimeRange
    exclude_skill_profiles_with_manual_averages: bool
    skill_profile_group_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, skill_profile_sids: _Optional[_Iterable[int]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., exclude_skill_profiles_with_manual_averages: bool = ..., skill_profile_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateSkillProfileAveragesUsingHistoricalDataRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserCapability(_message.Message):
    __slots__ = ("can_display", "can_edit", "is_move_target", "can_move", "can_delete", "can_undelete", "can_add_child")
    CAN_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    CAN_EDIT_FIELD_NUMBER: _ClassVar[int]
    IS_MOVE_TARGET_FIELD_NUMBER: _ClassVar[int]
    CAN_MOVE_FIELD_NUMBER: _ClassVar[int]
    CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
    CAN_UNDELETE_FIELD_NUMBER: _ClassVar[int]
    CAN_ADD_CHILD_FIELD_NUMBER: _ClassVar[int]
    can_display: bool
    can_edit: bool
    is_move_target: bool
    can_move: bool
    can_delete: bool
    can_undelete: bool
    can_add_child: bool
    def __init__(self, can_display: bool = ..., can_edit: bool = ..., is_move_target: bool = ..., can_move: bool = ..., can_delete: bool = ..., can_undelete: bool = ..., can_add_child: bool = ...) -> None: ...

class CallCenterNode(_message.Message):
    __slots__ = ("call_center_node_sid", "name", "description", "datetime_set_to_inactive", "time_zone_val", "schedule_scenario_sid", "member_client_nodes", "member_non_skill_activities", "member_open_times_patterns", "member_agent_availability_patterns", "member_constraint_rules", "member_agent_groups", "origin_sid", "shrinkage")
    CALL_CENTER_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_VAL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CLIENT_NODES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OPEN_TIMES_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SID_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_FIELD_NUMBER: _ClassVar[int]
    call_center_node_sid: int
    name: str
    description: str
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    time_zone_val: _org_pb2.TimeZone
    schedule_scenario_sid: int
    member_client_nodes: _containers.RepeatedCompositeFieldContainer[ClientNode]
    member_non_skill_activities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
    member_open_times_patterns: _containers.RepeatedCompositeFieldContainer[OpenTimesPattern]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    origin_sid: _wrappers_pb2.Int64Value
    shrinkage: _wrappers_pb2.FloatValue
    def __init__(self, call_center_node_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_zone_val: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., schedule_scenario_sid: _Optional[int] = ..., member_client_nodes: _Optional[_Iterable[_Union[ClientNode, _Mapping]]] = ..., member_non_skill_activities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ..., member_open_times_patterns: _Optional[_Iterable[_Union[OpenTimesPattern, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ..., origin_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shrinkage: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class UpdateCallCenterNodeReq(_message.Message):
    __slots__ = ("node",)
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: CallCenterNode
    def __init__(self, node: _Optional[_Union[CallCenterNode, _Mapping]] = ...) -> None: ...

class UpdateCallCenterNodeRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClientNode(_message.Message):
    __slots__ = ("client_node_sid", "name", "description", "parent_sid", "datetime_set_to_inactive", "time_zone_val", "schedule_scenario_sid", "member_location_nodes", "member_non_skill_activities", "member_open_times_patterns", "member_agent_availability_patterns", "member_constraint_rules", "member_agent_groups", "origin_sid", "shrinkage")
    CLIENT_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARENT_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_VAL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_LOCATION_NODES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OPEN_TIMES_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SID_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_FIELD_NUMBER: _ClassVar[int]
    client_node_sid: int
    name: str
    description: str
    parent_sid: int
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    time_zone_val: _org_pb2.TimeZone
    schedule_scenario_sid: int
    member_location_nodes: _containers.RepeatedCompositeFieldContainer[LocationNode]
    member_non_skill_activities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
    member_open_times_patterns: _containers.RepeatedCompositeFieldContainer[OpenTimesPattern]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    origin_sid: _wrappers_pb2.Int64Value
    shrinkage: _wrappers_pb2.FloatValue
    def __init__(self, client_node_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., parent_sid: _Optional[int] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_zone_val: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., schedule_scenario_sid: _Optional[int] = ..., member_location_nodes: _Optional[_Iterable[_Union[LocationNode, _Mapping]]] = ..., member_non_skill_activities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ..., member_open_times_patterns: _Optional[_Iterable[_Union[OpenTimesPattern, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ..., origin_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shrinkage: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class CreateClientNodeReq(_message.Message):
    __slots__ = ("node",)
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: ClientNode
    def __init__(self, node: _Optional[_Union[ClientNode, _Mapping]] = ...) -> None: ...

class CreateClientNodeRes(_message.Message):
    __slots__ = ("client_node_sid",)
    CLIENT_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    client_node_sid: int
    def __init__(self, client_node_sid: _Optional[int] = ...) -> None: ...

class UpdateClientNodeReq(_message.Message):
    __slots__ = ("node",)
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: ClientNode
    def __init__(self, node: _Optional[_Union[ClientNode, _Mapping]] = ...) -> None: ...

class UpdateClientNodeRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocationNode(_message.Message):
    __slots__ = ("location_node_sid", "name", "description", "client_node_sid", "datetime_set_to_inactive", "time_zone_val", "shrinkage_is_percentage", "shrinkage_value", "schedule_scenario_sid", "member_program_nodes", "member_non_skill_activities", "member_open_times_patterns", "member_agent_availability_patterns", "member_constraint_rules", "member_agent_groups", "origin_sid", "shrinkage")
    LOCATION_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_VAL_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_IS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PROGRAM_NODES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OPEN_TIMES_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SID_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_FIELD_NUMBER: _ClassVar[int]
    location_node_sid: int
    name: str
    description: str
    client_node_sid: int
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    time_zone_val: _org_pb2.TimeZone
    shrinkage_is_percentage: bool
    shrinkage_value: int
    schedule_scenario_sid: int
    member_program_nodes: _containers.RepeatedCompositeFieldContainer[ProgramNode]
    member_non_skill_activities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
    member_open_times_patterns: _containers.RepeatedCompositeFieldContainer[OpenTimesPattern]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    origin_sid: _wrappers_pb2.Int64Value
    shrinkage: _wrappers_pb2.FloatValue
    def __init__(self, location_node_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., client_node_sid: _Optional[int] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., time_zone_val: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., shrinkage_is_percentage: bool = ..., shrinkage_value: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., member_program_nodes: _Optional[_Iterable[_Union[ProgramNode, _Mapping]]] = ..., member_non_skill_activities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ..., member_open_times_patterns: _Optional[_Iterable[_Union[OpenTimesPattern, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ..., origin_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shrinkage: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class CreateLocationNodeReq(_message.Message):
    __slots__ = ("node",)
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: LocationNode
    def __init__(self, node: _Optional[_Union[LocationNode, _Mapping]] = ...) -> None: ...

class CreateLocationNodeRes(_message.Message):
    __slots__ = ("location_node_sid",)
    LOCATION_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    location_node_sid: int
    def __init__(self, location_node_sid: _Optional[int] = ...) -> None: ...

class UpdateLocationNodeReq(_message.Message):
    __slots__ = ("location_node",)
    LOCATION_NODE_FIELD_NUMBER: _ClassVar[int]
    location_node: LocationNode
    def __init__(self, location_node: _Optional[_Union[LocationNode, _Mapping]] = ...) -> None: ...

class UpdateLocationNodeRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProgramNode(_message.Message):
    __slots__ = ("program_node_sid", "name", "description", "location_node_sid", "datetime_set_to_inactive", "shrinkage_is_percentage", "shrinkage_value", "schedule_scenario_sid", "member_shift_templates", "member_non_skill_activities", "member_open_times_patterns", "member_agent_availability_patterns", "member_constraint_rules", "member_agent_groups", "member_skill_proficiencies", "origin_sid", "skill_profile_category", "shrinkage")
    PROGRAM_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_IS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SHIFT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_OPEN_TIMES_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SHRINKAGE_FIELD_NUMBER: _ClassVar[int]
    program_node_sid: int
    name: str
    description: str
    location_node_sid: int
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    shrinkage_is_percentage: bool
    shrinkage_value: int
    schedule_scenario_sid: int
    member_shift_templates: _containers.RepeatedCompositeFieldContainer[ShiftTemplate]
    member_non_skill_activities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
    member_open_times_patterns: _containers.RepeatedCompositeFieldContainer[OpenTimesPattern]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    member_skill_proficiencies: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
    origin_sid: _wrappers_pb2.Int64Value
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    shrinkage: _wrappers_pb2.FloatValue
    def __init__(self, program_node_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., location_node_sid: _Optional[int] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shrinkage_is_percentage: bool = ..., shrinkage_value: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., member_shift_templates: _Optional[_Iterable[_Union[ShiftTemplate, _Mapping]]] = ..., member_non_skill_activities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ..., member_open_times_patterns: _Optional[_Iterable[_Union[OpenTimesPattern, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ..., member_skill_proficiencies: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ..., origin_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ..., shrinkage: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class CreateProgramNodeReq(_message.Message):
    __slots__ = ("node",)
    NODE_FIELD_NUMBER: _ClassVar[int]
    node: ProgramNode
    def __init__(self, node: _Optional[_Union[ProgramNode, _Mapping]] = ...) -> None: ...

class CreateProgramNodeRes(_message.Message):
    __slots__ = ("program_node_sid",)
    PROGRAM_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    program_node_sid: int
    def __init__(self, program_node_sid: _Optional[int] = ...) -> None: ...

class UpdateProgramNodeReq(_message.Message):
    __slots__ = ("program_node",)
    PROGRAM_NODE_FIELD_NUMBER: _ClassVar[int]
    program_node: ProgramNode
    def __init__(self, program_node: _Optional[_Union[ProgramNode, _Mapping]] = ...) -> None: ...

class UpdateProgramNodeRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProgramNodesBySidReq(_message.Message):
    __slots__ = ("program_node_sids",)
    PROGRAM_NODE_SIDS_FIELD_NUMBER: _ClassVar[int]
    program_node_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, program_node_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListProgramNodesBySidRes(_message.Message):
    __slots__ = ("program_nodes",)
    PROGRAM_NODES_FIELD_NUMBER: _ClassVar[int]
    program_nodes: _containers.RepeatedCompositeFieldContainer[ProgramNode]
    def __init__(self, program_nodes: _Optional[_Iterable[_Union[ProgramNode, _Mapping]]] = ...) -> None: ...

class ParentEntity(_message.Message):
    __slots__ = ("parent_sid", "parent_type")
    PARENT_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent_sid: int
    parent_type: _wfm_pb2.ConfigEntityType
    def __init__(self, parent_sid: _Optional[int] = ..., parent_type: _Optional[_Union[_wfm_pb2.ConfigEntityType, str]] = ...) -> None: ...

class ConstraintRule(_message.Message):
    __slots__ = ("constraint_rule_sid", "parent_entity", "name", "description", "val_count", "val_unit", "per_count", "per_unit", "priority", "is_priority_infinite", "rule_type", "target_sid", "schedule_scenario_sid", "scheduling_activity", "skill_proficiency")
    CONSTRAINT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    VAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    PER_COUNT_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IS_PRIORITY_INFINITE_FIELD_NUMBER: _ClassVar[int]
    RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFICIENCY_FIELD_NUMBER: _ClassVar[int]
    constraint_rule_sid: int
    parent_entity: ParentEntity
    name: str
    description: str
    val_count: int
    val_unit: _wfm_pb2.ConstraintTimeUnit
    per_count: int
    per_unit: _wfm_pb2.ConstraintTimeUnit
    priority: int
    is_priority_infinite: bool
    rule_type: _wfm_pb2.ConstraintRuleType
    target_sid: int
    schedule_scenario_sid: int
    scheduling_activity: SchedulingActivity
    skill_proficiency: SkillProficiency
    def __init__(self, constraint_rule_sid: _Optional[int] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., val_count: _Optional[int] = ..., val_unit: _Optional[_Union[_wfm_pb2.ConstraintTimeUnit, str]] = ..., per_count: _Optional[int] = ..., per_unit: _Optional[_Union[_wfm_pb2.ConstraintTimeUnit, str]] = ..., priority: _Optional[int] = ..., is_priority_infinite: bool = ..., rule_type: _Optional[_Union[_wfm_pb2.ConstraintRuleType, str]] = ..., target_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., scheduling_activity: _Optional[_Union[SchedulingActivity, _Mapping]] = ..., skill_proficiency: _Optional[_Union[SkillProficiency, _Mapping]] = ...) -> None: ...

class CreateConstraintRuleReq(_message.Message):
    __slots__ = ("constraint_rule",)
    CONSTRAINT_RULE_FIELD_NUMBER: _ClassVar[int]
    constraint_rule: ConstraintRule
    def __init__(self, constraint_rule: _Optional[_Union[ConstraintRule, _Mapping]] = ...) -> None: ...

class CreateConstraintRuleRes(_message.Message):
    __slots__ = ("constraint_rule_sid", "skill_proficiency_sid")
    CONSTRAINT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFICIENCY_SID_FIELD_NUMBER: _ClassVar[int]
    constraint_rule_sid: int
    skill_proficiency_sid: int
    def __init__(self, constraint_rule_sid: _Optional[int] = ..., skill_proficiency_sid: _Optional[int] = ...) -> None: ...

class UpdateConstraintRuleReq(_message.Message):
    __slots__ = ("constraint_rule",)
    CONSTRAINT_RULE_FIELD_NUMBER: _ClassVar[int]
    constraint_rule: ConstraintRule
    def __init__(self, constraint_rule: _Optional[_Union[ConstraintRule, _Mapping]] = ...) -> None: ...

class UpdateConstraintRuleRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteConstraintRuleReq(_message.Message):
    __slots__ = ("constraint_rule_sid",)
    CONSTRAINT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    constraint_rule_sid: int
    def __init__(self, constraint_rule_sid: _Optional[int] = ...) -> None: ...

class DeleteConstraintRuleRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NonSkillActivity(_message.Message):
    __slots__ = ("non_skill_activity_sid", "name", "description", "datetime_set_to_inactive", "red", "green", "blue", "transparency", "inherited_from_entity")
    NON_SKILL_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENCY_FIELD_NUMBER: _ClassVar[int]
    INHERITED_FROM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity_sid: int
    name: str
    description: str
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    red: int
    green: int
    blue: int
    transparency: float
    inherited_from_entity: ParentEntity
    def __init__(self, non_skill_activity_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ..., transparency: _Optional[float] = ..., inherited_from_entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class CreateNonSkillActivityReq(_message.Message):
    __slots__ = ("non_skill_activity",)
    NON_SKILL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity: NonSkillActivity
    def __init__(self, non_skill_activity: _Optional[_Union[NonSkillActivity, _Mapping]] = ...) -> None: ...

class CreateNonSkillActivityRes(_message.Message):
    __slots__ = ("non_skill_activity_sid", "scheduling_activity_sid")
    NON_SKILL_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity_sid: int
    scheduling_activity_sid: int
    def __init__(self, non_skill_activity_sid: _Optional[int] = ..., scheduling_activity_sid: _Optional[int] = ...) -> None: ...

class UpdateNonSkillActivityReq(_message.Message):
    __slots__ = ("non_skill_activity",)
    NON_SKILL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity: NonSkillActivity
    def __init__(self, non_skill_activity: _Optional[_Union[NonSkillActivity, _Mapping]] = ...) -> None: ...

class UpdateNonSkillActivityRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListNonSkillActivitiesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListNonSkillActivitiesRes(_message.Message):
    __slots__ = ("non_skill_activities",)
    NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    non_skill_activities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
    def __init__(self, non_skill_activities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ...) -> None: ...

class ListNonSkillActivityAssociationsReq(_message.Message):
    __slots__ = ("associated_entity", "relationship_type")
    ASSOCIATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    associated_entity: ParentEntity
    relationship_type: _wfm_pb2.ConfigRelationshipType
    def __init__(self, associated_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., relationship_type: _Optional[_Union[_wfm_pb2.ConfigRelationshipType, str]] = ...) -> None: ...

class ListNonSkillActivityAssociationsRes(_message.Message):
    __slots__ = ("non_skill_activity_sids",)
    NON_SKILL_ACTIVITY_SIDS_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, non_skill_activity_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class SchedulingActivity(_message.Message):
    __slots__ = ("scheduling_activity_sid", "is_skill_activity", "activity_sid", "member_non_skill_activity", "activity_classification")
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    IS_SKILL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NON_SKILL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    scheduling_activity_sid: int
    is_skill_activity: bool
    activity_sid: _wrappers_pb2.Int64Value
    member_non_skill_activity: NonSkillActivity
    activity_classification: _wfm_pb2.SchedulingActivityClassification
    def __init__(self, scheduling_activity_sid: _Optional[int] = ..., is_skill_activity: bool = ..., activity_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., member_non_skill_activity: _Optional[_Union[NonSkillActivity, _Mapping]] = ..., activity_classification: _Optional[_Union[_wfm_pb2.SchedulingActivityClassification, str]] = ...) -> None: ...

class ListCandidateSchedulingActivitiesReq(_message.Message):
    __slots__ = ("parent_of_rule", "schedule_scenario_sid")
    PARENT_OF_RULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    parent_of_rule: ParentEntity
    schedule_scenario_sid: int
    def __init__(self, parent_of_rule: _Optional[_Union[ParentEntity, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class ListCandidateSchedulingActivitiesRes(_message.Message):
    __slots__ = ("scheduling_activities",)
    SCHEDULING_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    scheduling_activities: _containers.RepeatedCompositeFieldContainer[SchedulingActivity]
    def __init__(self, scheduling_activities: _Optional[_Iterable[_Union[SchedulingActivity, _Mapping]]] = ...) -> None: ...

class GetOnCallSchedulingActivityReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOnCallSchedulingActivityRes(_message.Message):
    __slots__ = ("on_call_scheduling_activity",)
    ON_CALL_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    on_call_scheduling_activity: SchedulingActivity
    def __init__(self, on_call_scheduling_activity: _Optional[_Union[SchedulingActivity, _Mapping]] = ...) -> None: ...

class AgentGroup(_message.Message):
    __slots__ = ("agent_group_sid", "parent_entity", "name", "description", "datetime_set_to_inactive", "schedule_scenario_sid", "member_constraint_rules", "member_wfm_agents", "member_skill_proficiencies", "member_agent_availability_patterns")
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    agent_group_sid: int
    parent_entity: ParentEntity
    name: str
    description: str
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    schedule_scenario_sid: int
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_wfm_agents: _containers.RepeatedCompositeFieldContainer[WFMAgent]
    member_skill_proficiencies: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    def __init__(self, agent_group_sid: _Optional[int] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_wfm_agents: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ..., member_skill_proficiencies: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ...) -> None: ...

class CreateAgentGroupReq(_message.Message):
    __slots__ = ("agent_group",)
    AGENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_group: AgentGroup
    def __init__(self, agent_group: _Optional[_Union[AgentGroup, _Mapping]] = ...) -> None: ...

class CreateAgentGroupRes(_message.Message):
    __slots__ = ("agent_group_sid",)
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    agent_group_sid: int
    def __init__(self, agent_group_sid: _Optional[int] = ...) -> None: ...

class ListAgentScheduleGroupsRequest(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: ParentEntity
    def __init__(self, entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class ListAgentScheduleGroupsResponse(_message.Message):
    __slots__ = ("agent_groups",)
    AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    def __init__(self, agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ...) -> None: ...

class UpdateAgentGroupReq(_message.Message):
    __slots__ = ("agent_group",)
    AGENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    agent_group: AgentGroup
    def __init__(self, agent_group: _Optional[_Union[AgentGroup, _Mapping]] = ...) -> None: ...

class UpdateAgentGroupRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WFMAgent(_message.Message):
    __slots__ = ("wfm_agent_sid", "tcn_agent_sid", "name", "datetime_set_to_inactive", "member_constraint_rules", "member_skill_proficiencies", "member_agent_availability_patterns", "created_at", "tcn_agent_is_enabled")
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    TCN_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TCN_AGENT_IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid: int
    tcn_agent_sid: _wrappers_pb2.Int64Value
    name: str
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    member_constraint_rules: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
    member_skill_proficiencies: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
    member_agent_availability_patterns: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
    created_at: _timestamp_pb2.Timestamp
    tcn_agent_is_enabled: bool
    def __init__(self, wfm_agent_sid: _Optional[int] = ..., tcn_agent_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., name: _Optional[str] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., member_constraint_rules: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ..., member_skill_proficiencies: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ..., member_agent_availability_patterns: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tcn_agent_is_enabled: bool = ...) -> None: ...

class CreateUnassignedWFMAgentRequest(_message.Message):
    __slots__ = ("wfm_agent_sid_to_copy_agent_group_associations", "name")
    WFM_AGENT_SID_TO_COPY_AGENT_GROUP_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid_to_copy_agent_group_associations: _wrappers_pb2.Int64Value
    name: str
    def __init__(self, wfm_agent_sid_to_copy_agent_group_associations: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class CreateUnassignedWFMAgentResponse(_message.Message):
    __slots__ = ("wfm_agent_sid",)
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid: int
    def __init__(self, wfm_agent_sid: _Optional[int] = ...) -> None: ...

class UpdateWFMAgentReq(_message.Message):
    __slots__ = ("wfm_agent",)
    WFM_AGENT_FIELD_NUMBER: _ClassVar[int]
    wfm_agent: WFMAgent
    def __init__(self, wfm_agent: _Optional[_Union[WFMAgent, _Mapping]] = ...) -> None: ...

class UpdateWFMAgentRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAllWFMAgentsReq(_message.Message):
    __slots__ = ("include_inactive", "include_skill_proficiencies", "include_agent_groups", "agent_group_schedule_scenario_sid")
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUP_SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    include_inactive: bool
    include_skill_proficiencies: bool
    include_agent_groups: bool
    agent_group_schedule_scenario_sid: int
    def __init__(self, include_inactive: bool = ..., include_skill_proficiencies: bool = ..., include_agent_groups: bool = ..., agent_group_schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class ListAllWFMAgentsRes(_message.Message):
    __slots__ = ("wfm_agents", "agent_groups_by_agent")
    class AgentGroupsByAgent(_message.Message):
        __slots__ = ("agent_groups",)
        AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
        def __init__(self, agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ...) -> None: ...
    WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUPS_BY_AGENT_FIELD_NUMBER: _ClassVar[int]
    wfm_agents: _containers.RepeatedCompositeFieldContainer[WFMAgent]
    agent_groups_by_agent: _containers.RepeatedCompositeFieldContainer[ListAllWFMAgentsRes.AgentGroupsByAgent]
    def __init__(self, wfm_agents: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ..., agent_groups_by_agent: _Optional[_Iterable[_Union[ListAllWFMAgentsRes.AgentGroupsByAgent, _Mapping]]] = ...) -> None: ...

class ListCandidateWFMAgentsReq(_message.Message):
    __slots__ = ("agent_group_sid",)
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    agent_group_sid: int
    def __init__(self, agent_group_sid: _Optional[int] = ...) -> None: ...

class ListCandidateWFMAgentsRes(_message.Message):
    __slots__ = ("wfm_agents",)
    WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    wfm_agents: _containers.RepeatedCompositeFieldContainer[WFMAgent]
    def __init__(self, wfm_agents: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ...) -> None: ...

class ListUngroupedWFMAgentsReq(_message.Message):
    __slots__ = ("schedule_scenario_sid", "created_after_datetime", "include_skill_proficiencies")
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_DATETIME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    created_after_datetime: _timestamp_pb2.Timestamp
    include_skill_proficiencies: bool
    def __init__(self, schedule_scenario_sid: _Optional[int] = ..., created_after_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., include_skill_proficiencies: bool = ...) -> None: ...

class ListUngroupedWFMAgentsRes(_message.Message):
    __slots__ = ("wfm_agents",)
    WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    wfm_agents: _containers.RepeatedCompositeFieldContainer[WFMAgent]
    def __init__(self, wfm_agents: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ...) -> None: ...

class ListWFMAgentSidsReq(_message.Message):
    __slots__ = ("tcn_agent_sids",)
    TCN_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    tcn_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tcn_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListWFMAgentSidsRes(_message.Message):
    __slots__ = ("sids",)
    class SidsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SIDS_FIELD_NUMBER: _ClassVar[int]
    sids: _containers.ScalarMap[int, int]
    def __init__(self, sids: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ListUnassignedWFMAgentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUnassignedWFMAgentsResponse(_message.Message):
    __slots__ = ("wfm_agents",)
    WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    wfm_agents: _containers.RepeatedCompositeFieldContainer[WFMAgent]
    def __init__(self, wfm_agents: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ...) -> None: ...

class ListWFMAgentsAssociatedWithAgentGroupReq(_message.Message):
    __slots__ = ("agent_group_sid",)
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    agent_group_sid: int
    def __init__(self, agent_group_sid: _Optional[int] = ...) -> None: ...

class ListWFMAgentsAssociatedWithAgentGroupRes(_message.Message):
    __slots__ = ("wfm_agent_sids",)
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class BuildAgentDiagnosticsReq(_message.Message):
    __slots__ = ("wfm_agent_sid", "schedule_scenario_sid", "agent_group_sid")
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid: int
    schedule_scenario_sid: int
    agent_group_sid: int
    def __init__(self, wfm_agent_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., agent_group_sid: _Optional[int] = ...) -> None: ...

class BuildAgentDiagnosticsRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostics]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostics, _Mapping]]] = ...) -> None: ...

class CreateWFMAgentMembershipsReq(_message.Message):
    __slots__ = ("wfm_agent_sids", "agent_group_sid", "schedule_scenario_sid")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    agent_group_sid: int
    schedule_scenario_sid: int
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., agent_group_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class CreateWFMAgentMembershipsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyWFMAgentMembershipsRequest(_message.Message):
    __slots__ = ("originating_wfm_agent_sid", "target_wfm_agent_sid")
    ORIGINATING_WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    TARGET_WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    originating_wfm_agent_sid: int
    target_wfm_agent_sid: int
    def __init__(self, originating_wfm_agent_sid: _Optional[int] = ..., target_wfm_agent_sid: _Optional[int] = ...) -> None: ...

class CopyWFMAgentMembershipsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWFMAgentMembershipsReq(_message.Message):
    __slots__ = ("wfm_agent_sids", "agent_group_sid")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    agent_group_sid: int
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., agent_group_sid: _Optional[int] = ...) -> None: ...

class DeleteWFMAgentMembershipsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWFMAgentsMembershipsReq(_message.Message):
    __slots__ = ("wfm_agent_sids", "agent_group_sids")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    agent_group_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., agent_group_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteWFMAgentsMembershipsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveAgentFromFutureShiftsRequest(_message.Message):
    __slots__ = ("wfm_agent_sid_to_remove", "replace_with_new_unassigned_agent")
    WFM_AGENT_SID_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_WITH_NEW_UNASSIGNED_AGENT_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid_to_remove: int
    replace_with_new_unassigned_agent: bool
    def __init__(self, wfm_agent_sid_to_remove: _Optional[int] = ..., replace_with_new_unassigned_agent: bool = ...) -> None: ...

class RemoveAgentFromFutureShiftsResponse(_message.Message):
    __slots__ = ("unassigned_agent_sid",)
    UNASSIGNED_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    unassigned_agent_sid: _wrappers_pb2.Int64Value
    def __init__(self, unassigned_agent_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class DOWPlacement(_message.Message):
    __slots__ = ("start_minute", "end_minute", "placement_type", "day_of_week", "week_number")
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    WEEK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    start_minute: int
    end_minute: int
    placement_type: _wfm_pb2.DOWPlacementType
    day_of_week: _wfm_pb2.DayOfWeek
    week_number: int
    def __init__(self, start_minute: _Optional[int] = ..., end_minute: _Optional[int] = ..., placement_type: _Optional[_Union[_wfm_pb2.DOWPlacementType, str]] = ..., day_of_week: _Optional[_Union[_wfm_pb2.DayOfWeek, str]] = ..., week_number: _Optional[int] = ...) -> None: ...

class ShiftTemplate(_message.Message):
    __slots__ = ("shift_template_sid", "program_node_sid", "name", "description", "datetime_set_to_inactive", "is_tourshift", "min_shift_width", "max_shift_width", "min_agents", "max_agents", "shift_start_boundary_minutes", "same_time_each_DOW", "same_length_per_agent", "schedule_scenario_sid", "member_placement_rules", "DOW_placements", "member_agent_groups")
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_TOURSHIFT_FIELD_NUMBER: _ClassVar[int]
    MIN_SHIFT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_SHIFT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MIN_AGENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_AGENTS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_START_BOUNDARY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SAME_TIME_EACH_DOW_FIELD_NUMBER: _ClassVar[int]
    SAME_LENGTH_PER_AGENT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PLACEMENT_RULES_FIELD_NUMBER: _ClassVar[int]
    DOW_PLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    program_node_sid: int
    name: str
    description: str
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    is_tourshift: bool
    min_shift_width: int
    max_shift_width: int
    min_agents: int
    max_agents: int
    shift_start_boundary_minutes: int
    same_time_each_DOW: bool
    same_length_per_agent: bool
    schedule_scenario_sid: int
    member_placement_rules: _containers.RepeatedCompositeFieldContainer[PlacementRule]
    DOW_placements: _containers.RepeatedCompositeFieldContainer[DOWPlacement]
    member_agent_groups: _containers.RepeatedCompositeFieldContainer[AgentGroup]
    def __init__(self, shift_template_sid: _Optional[int] = ..., program_node_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_tourshift: bool = ..., min_shift_width: _Optional[int] = ..., max_shift_width: _Optional[int] = ..., min_agents: _Optional[int] = ..., max_agents: _Optional[int] = ..., shift_start_boundary_minutes: _Optional[int] = ..., same_time_each_DOW: bool = ..., same_length_per_agent: bool = ..., schedule_scenario_sid: _Optional[int] = ..., member_placement_rules: _Optional[_Iterable[_Union[PlacementRule, _Mapping]]] = ..., DOW_placements: _Optional[_Iterable[_Union[DOWPlacement, _Mapping]]] = ..., member_agent_groups: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ...) -> None: ...

class CreateShiftTemplateReq(_message.Message):
    __slots__ = ("shift_template",)
    SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    shift_template: ShiftTemplate
    def __init__(self, shift_template: _Optional[_Union[ShiftTemplate, _Mapping]] = ...) -> None: ...

class CreateShiftTemplateRes(_message.Message):
    __slots__ = ("shift_template_sid",)
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    def __init__(self, shift_template_sid: _Optional[int] = ...) -> None: ...

class UpdateShiftTemplateReq(_message.Message):
    __slots__ = ("shift_template",)
    SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    shift_template: ShiftTemplate
    def __init__(self, shift_template: _Optional[_Union[ShiftTemplate, _Mapping]] = ...) -> None: ...

class UpdateShiftTemplateRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListShiftTemplatesBySidsReq(_message.Message):
    __slots__ = ("shift_template_sids", "include_placement_rules")
    SHIFT_TEMPLATE_SIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PLACEMENT_RULES_FIELD_NUMBER: _ClassVar[int]
    shift_template_sids: _containers.RepeatedScalarFieldContainer[int]
    include_placement_rules: bool
    def __init__(self, shift_template_sids: _Optional[_Iterable[int]] = ..., include_placement_rules: bool = ...) -> None: ...

class ListShiftTemplatesBySidsRes(_message.Message):
    __slots__ = ("shift_templates",)
    SHIFT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    shift_templates: _containers.RepeatedCompositeFieldContainer[ShiftTemplate]
    def __init__(self, shift_templates: _Optional[_Iterable[_Union[ShiftTemplate, _Mapping]]] = ...) -> None: ...

class BuildShiftTemplateDiagnosticsReq(_message.Message):
    __slots__ = ("shift_template_sid", "schedule_scenario_sid")
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    schedule_scenario_sid: int
    def __init__(self, shift_template_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class BuildShiftTemplateDiagnosticsRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class PlacementRule(_message.Message):
    __slots__ = ("placement_rule_sid", "shift_template_sid", "activity_order", "min_duration_minutes", "max_duration_minutes", "scheduling_activity_sid", "schedule_scenario_sid", "member_scheduling_activity")
    PLACEMENT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ORDER_FIELD_NUMBER: _ClassVar[int]
    MIN_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    placement_rule_sid: int
    shift_template_sid: int
    activity_order: int
    min_duration_minutes: int
    max_duration_minutes: int
    scheduling_activity_sid: int
    schedule_scenario_sid: int
    member_scheduling_activity: SchedulingActivity
    def __init__(self, placement_rule_sid: _Optional[int] = ..., shift_template_sid: _Optional[int] = ..., activity_order: _Optional[int] = ..., min_duration_minutes: _Optional[int] = ..., max_duration_minutes: _Optional[int] = ..., scheduling_activity_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., member_scheduling_activity: _Optional[_Union[SchedulingActivity, _Mapping]] = ...) -> None: ...

class CreatePlacementRuleReq(_message.Message):
    __slots__ = ("placement_rule",)
    PLACEMENT_RULE_FIELD_NUMBER: _ClassVar[int]
    placement_rule: PlacementRule
    def __init__(self, placement_rule: _Optional[_Union[PlacementRule, _Mapping]] = ...) -> None: ...

class CreatePlacementRuleRes(_message.Message):
    __slots__ = ("placement_rule_sid",)
    PLACEMENT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    placement_rule_sid: int
    def __init__(self, placement_rule_sid: _Optional[int] = ...) -> None: ...

class UpdatePlacementRuleReq(_message.Message):
    __slots__ = ("placement_rule",)
    PLACEMENT_RULE_FIELD_NUMBER: _ClassVar[int]
    placement_rule: PlacementRule
    def __init__(self, placement_rule: _Optional[_Union[PlacementRule, _Mapping]] = ...) -> None: ...

class UpdatePlacementRuleRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePlacementRuleReq(_message.Message):
    __slots__ = ("placement_rule_sid",)
    PLACEMENT_RULE_SID_FIELD_NUMBER: _ClassVar[int]
    placement_rule_sid: int
    def __init__(self, placement_rule_sid: _Optional[int] = ...) -> None: ...

class DeletePlacementRuleRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DatetimePattern(_message.Message):
    __slots__ = ("week_maps", "calendar_items")
    class WeekMap(_message.Message):
        __slots__ = ("datetime_range", "day_maps")
        class WeekMapDOW(_message.Message):
            __slots__ = ("day_of_week", "start_minute_in_day", "end_minute_in_day", "value")
            DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
            START_MINUTE_IN_DAY_FIELD_NUMBER: _ClassVar[int]
            END_MINUTE_IN_DAY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            day_of_week: _wfm_pb2.DayOfWeek
            start_minute_in_day: int
            end_minute_in_day: int
            value: _wfm_pb2.OptionTypes
            def __init__(self, day_of_week: _Optional[_Union[_wfm_pb2.DayOfWeek, str]] = ..., start_minute_in_day: _Optional[int] = ..., end_minute_in_day: _Optional[int] = ..., value: _Optional[_Union[_wfm_pb2.OptionTypes, _Mapping]] = ...) -> None: ...
        DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        DAY_MAPS_FIELD_NUMBER: _ClassVar[int]
        datetime_range: _wfm_pb2.DatetimeRange
        day_maps: _containers.RepeatedCompositeFieldContainer[DatetimePattern.WeekMap.WeekMapDOW]
        def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., day_maps: _Optional[_Iterable[_Union[DatetimePattern.WeekMap.WeekMapDOW, _Mapping]]] = ...) -> None: ...
    class CalendarItem(_message.Message):
        __slots__ = ("datetime_range", "value")
        DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        datetime_range: _wfm_pb2.DatetimeRange
        value: _wfm_pb2.OptionTypes
        def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., value: _Optional[_Union[_wfm_pb2.OptionTypes, _Mapping]] = ...) -> None: ...
    WEEK_MAPS_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_ITEMS_FIELD_NUMBER: _ClassVar[int]
    week_maps: _containers.RepeatedCompositeFieldContainer[DatetimePattern.WeekMap]
    calendar_items: _containers.RepeatedCompositeFieldContainer[DatetimePattern.CalendarItem]
    def __init__(self, week_maps: _Optional[_Iterable[_Union[DatetimePattern.WeekMap, _Mapping]]] = ..., calendar_items: _Optional[_Iterable[_Union[DatetimePattern.CalendarItem, _Mapping]]] = ...) -> None: ...

class OpenTimesPattern(_message.Message):
    __slots__ = ("open_times_pattern_sid", "parent_entity", "datetime_pattern", "schedule_scenario_sid", "scheduling_activity_sid")
    OPEN_TIMES_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    open_times_pattern_sid: int
    parent_entity: ParentEntity
    datetime_pattern: DatetimePattern
    schedule_scenario_sid: int
    scheduling_activity_sid: _wrappers_pb2.Int64Value
    def __init__(self, open_times_pattern_sid: _Optional[int] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_pattern: _Optional[_Union[DatetimePattern, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ..., scheduling_activity_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class CreateOpenTimesPatternReq(_message.Message):
    __slots__ = ("open_times_pattern",)
    OPEN_TIMES_PATTERN_FIELD_NUMBER: _ClassVar[int]
    open_times_pattern: OpenTimesPattern
    def __init__(self, open_times_pattern: _Optional[_Union[OpenTimesPattern, _Mapping]] = ...) -> None: ...

class CreateOpenTimesPatternRes(_message.Message):
    __slots__ = ("open_times_pattern_sid",)
    OPEN_TIMES_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    open_times_pattern_sid: int
    def __init__(self, open_times_pattern_sid: _Optional[int] = ...) -> None: ...

class UpdateOpenTimesPatternReq(_message.Message):
    __slots__ = ("open_times_pattern",)
    OPEN_TIMES_PATTERN_FIELD_NUMBER: _ClassVar[int]
    open_times_pattern: OpenTimesPattern
    def __init__(self, open_times_pattern: _Optional[_Union[OpenTimesPattern, _Mapping]] = ...) -> None: ...

class UpdateOpenTimesPatternRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteOpenTimesPatternReq(_message.Message):
    __slots__ = ("open_times_pattern_sid",)
    OPEN_TIMES_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    open_times_pattern_sid: int
    def __init__(self, open_times_pattern_sid: _Optional[int] = ...) -> None: ...

class DeleteOpenTimesPatternRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOpenTimesBitmapsReq(_message.Message):
    __slots__ = ("node_to_check", "schedule_scenario_sid", "include_inactive", "datetime_range", "bitmap_type")
    NODE_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    BITMAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_to_check: ParentEntity
    schedule_scenario_sid: int
    include_inactive: bool
    datetime_range: _wfm_pb2.DatetimeRange
    bitmap_type: _wfm_pb2.BitmapType
    def __init__(self, node_to_check: _Optional[_Union[ParentEntity, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ..., include_inactive: bool = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., bitmap_type: _Optional[_Union[_wfm_pb2.BitmapType, str]] = ...) -> None: ...

class GetOpenTimesBitmapsRes(_message.Message):
    __slots__ = ("inherited_bitmap", "own_bitmap", "resulting_bitmap")
    INHERITED_BITMAP_FIELD_NUMBER: _ClassVar[int]
    OWN_BITMAP_FIELD_NUMBER: _ClassVar[int]
    RESULTING_BITMAP_FIELD_NUMBER: _ClassVar[int]
    inherited_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.OpenTimesOption]
    own_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.OpenTimesOption]
    resulting_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.OpenTimesOption]
    def __init__(self, inherited_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.OpenTimesOption, str]]] = ..., own_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.OpenTimesOption, str]]] = ..., resulting_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.OpenTimesOption, str]]] = ...) -> None: ...

class ListOpenDateRangesForNodeOpenTimesBitmapsRequest(_message.Message):
    __slots__ = ("datetime_range", "node_selector", "schedule_scenario_sid")
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    datetime_range: _wfm_pb2.DatetimeRange
    node_selector: ParentEntity
    schedule_scenario_sid: int
    def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class ListOpenDateRangesForNodeOpenTimesBitmapsResponse(_message.Message):
    __slots__ = ("open_close_ranges",)
    OPEN_CLOSE_RANGES_FIELD_NUMBER: _ClassVar[int]
    open_close_ranges: _containers.RepeatedCompositeFieldContainer[_wfm_pb2.DatetimeRange]
    def __init__(self, open_close_ranges: _Optional[_Iterable[_Union[_wfm_pb2.DatetimeRange, _Mapping]]] = ...) -> None: ...

class AgentAvailabilityPattern(_message.Message):
    __slots__ = ("agent_availability_pattern_sid", "parent_entity", "datetime_pattern", "schedule_scenario_sid", "scheduling_activity_sid")
    AGENT_AVAILABILITY_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    agent_availability_pattern_sid: int
    parent_entity: ParentEntity
    datetime_pattern: DatetimePattern
    schedule_scenario_sid: int
    scheduling_activity_sid: _wrappers_pb2.Int64Value
    def __init__(self, agent_availability_pattern_sid: _Optional[int] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_pattern: _Optional[_Union[DatetimePattern, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ..., scheduling_activity_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class CreateAgentAvailabilityPatternReq(_message.Message):
    __slots__ = ("agent_availability_pattern",)
    AGENT_AVAILABILITY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    agent_availability_pattern: AgentAvailabilityPattern
    def __init__(self, agent_availability_pattern: _Optional[_Union[AgentAvailabilityPattern, _Mapping]] = ...) -> None: ...

class CreateAgentAvailabilityPatternRes(_message.Message):
    __slots__ = ("agent_availability_pattern_sid",)
    AGENT_AVAILABILITY_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    agent_availability_pattern_sid: int
    def __init__(self, agent_availability_pattern_sid: _Optional[int] = ...) -> None: ...

class UpdateAgentAvailabilityPatternReq(_message.Message):
    __slots__ = ("agent_availability_pattern",)
    AGENT_AVAILABILITY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    agent_availability_pattern: AgentAvailabilityPattern
    def __init__(self, agent_availability_pattern: _Optional[_Union[AgentAvailabilityPattern, _Mapping]] = ...) -> None: ...

class UpdateAgentAvailabilityPatternRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAgentAvailabilityPatternReq(_message.Message):
    __slots__ = ("agent_availability_pattern_sid",)
    AGENT_AVAILABILITY_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    agent_availability_pattern_sid: int
    def __init__(self, agent_availability_pattern_sid: _Optional[int] = ...) -> None: ...

class DeleteAgentAvailabilityPatternRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AvailabilityBitmapSet(_message.Message):
    __slots__ = ("own_bitmap", "inherited_bitmap", "resulting_bitmap", "parent_entity")
    OWN_BITMAP_FIELD_NUMBER: _ClassVar[int]
    INHERITED_BITMAP_FIELD_NUMBER: _ClassVar[int]
    RESULTING_BITMAP_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    own_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.AvailabilityOption]
    inherited_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.AvailabilityOption]
    resulting_bitmap: _containers.RepeatedScalarFieldContainer[_wfm_pb2.AvailabilityOption]
    parent_entity: ParentEntity
    def __init__(self, own_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.AvailabilityOption, str]]] = ..., inherited_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.AvailabilityOption, str]]] = ..., resulting_bitmap: _Optional[_Iterable[_Union[_wfm_pb2.AvailabilityOption, str]]] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class GetAvailabilityBitmapsReq(_message.Message):
    __slots__ = ("entities_to_check", "schedule_scenario_sid", "include_inactive", "datetime_range", "bitmap_type")
    ENTITIES_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    BITMAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    entities_to_check: _containers.RepeatedCompositeFieldContainer[ParentEntity]
    schedule_scenario_sid: int
    include_inactive: bool
    datetime_range: _wfm_pb2.DatetimeRange
    bitmap_type: _wfm_pb2.BitmapType
    def __init__(self, entities_to_check: _Optional[_Iterable[_Union[ParentEntity, _Mapping]]] = ..., schedule_scenario_sid: _Optional[int] = ..., include_inactive: bool = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., bitmap_type: _Optional[_Union[_wfm_pb2.BitmapType, str]] = ...) -> None: ...

class GetAvailabilityBitmapsRes(_message.Message):
    __slots__ = ("bitmaps",)
    BITMAPS_FIELD_NUMBER: _ClassVar[int]
    bitmaps: _containers.RepeatedCompositeFieldContainer[AvailabilityBitmapSet]
    def __init__(self, bitmaps: _Optional[_Iterable[_Union[AvailabilityBitmapSet, _Mapping]]] = ...) -> None: ...

class UpsertNonSkillActivityAssociationReq(_message.Message):
    __slots__ = ("non_skill_activity_sid", "node", "association_type", "schedule_scenario_sid")
    NON_SKILL_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    non_skill_activity_sid: int
    node: ParentEntity
    association_type: _wfm_pb2.ConfigRelationshipType
    schedule_scenario_sid: int
    def __init__(self, non_skill_activity_sid: _Optional[int] = ..., node: _Optional[_Union[ParentEntity, _Mapping]] = ..., association_type: _Optional[_Union[_wfm_pb2.ConfigRelationshipType, str]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class UpsertNonSkillActivityAssociationRes(_message.Message):
    __slots__ = ("upsert_succeeded", "nodes_affected", "rules_using_activity")
    class EntityMapping(_message.Message):
        __slots__ = ("left_entity", "right_entity")
        LEFT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        RIGHT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        left_entity: ParentEntity
        right_entity: ParentEntity
        def __init__(self, left_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., right_entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...
    UPSERT_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    NODES_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    RULES_USING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    upsert_succeeded: bool
    nodes_affected: _containers.RepeatedCompositeFieldContainer[ParentEntity]
    rules_using_activity: _containers.RepeatedCompositeFieldContainer[UpsertNonSkillActivityAssociationRes.EntityMapping]
    def __init__(self, upsert_succeeded: bool = ..., nodes_affected: _Optional[_Iterable[_Union[ParentEntity, _Mapping]]] = ..., rules_using_activity: _Optional[_Iterable[_Union[UpsertNonSkillActivityAssociationRes.EntityMapping, _Mapping]]] = ...) -> None: ...

class SkillProficiency(_message.Message):
    __slots__ = ("skill_proficiency_sid", "skill_sid", "preferred_skill_profile_sid", "manual_proficiency_value", "parent_entity", "skill_name", "skill_profile_name", "skill_profile_proficiency_value")
    SKILL_PROFICIENCY_SID_FIELD_NUMBER: _ClassVar[int]
    SKILL_SID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SKILL_PROFILE_SID_FIELD_NUMBER: _ClassVar[int]
    MANUAL_PROFICIENCY_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SKILL_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_PROFICIENCY_VALUE_FIELD_NUMBER: _ClassVar[int]
    skill_proficiency_sid: int
    skill_sid: int
    preferred_skill_profile_sid: _wrappers_pb2.Int64Value
    manual_proficiency_value: int
    parent_entity: ParentEntity
    skill_name: str
    skill_profile_name: str
    skill_profile_proficiency_value: int
    def __init__(self, skill_proficiency_sid: _Optional[int] = ..., skill_sid: _Optional[int] = ..., preferred_skill_profile_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., manual_proficiency_value: _Optional[int] = ..., parent_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., skill_name: _Optional[str] = ..., skill_profile_name: _Optional[str] = ..., skill_profile_proficiency_value: _Optional[int] = ...) -> None: ...

class CreateSkillProficienciesReq(_message.Message):
    __slots__ = ("proficiencies", "schedule_scenario_sid")
    PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    proficiencies: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
    schedule_scenario_sid: int
    def __init__(self, proficiencies: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class CreateSkillProficienciesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSkillProficienciesReq(_message.Message):
    __slots__ = ("skill_proficiencies",)
    SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    skill_proficiencies: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
    def __init__(self, skill_proficiencies: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ...) -> None: ...

class UpdateSkillProficienciesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSkillProficiencyReq(_message.Message):
    __slots__ = ("skill_proficiency_sid",)
    SKILL_PROFICIENCY_SID_FIELD_NUMBER: _ClassVar[int]
    skill_proficiency_sid: int
    def __init__(self, skill_proficiency_sid: _Optional[int] = ...) -> None: ...

class DeleteSkillProficiencyRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScheduleScenario(_message.Message):
    __slots__ = ("schedule_scenario_sid", "name", "description", "creation_datetime", "created_by_user_id", "is_default", "copied_from_scenario_sid", "schedule_range", "datetime_set_to_inactive", "is_active")
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATETIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    COPIED_FROM_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_SET_TO_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    name: str
    description: str
    creation_datetime: _timestamp_pb2.Timestamp
    created_by_user_id: str
    is_default: bool
    copied_from_scenario_sid: _wrappers_pb2.Int64Value
    schedule_range: _wfm_pb2.DatetimeRange
    datetime_set_to_inactive: _timestamp_pb2.Timestamp
    is_active: bool
    def __init__(self, schedule_scenario_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., creation_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., is_default: bool = ..., copied_from_scenario_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., schedule_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., datetime_set_to_inactive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: bool = ...) -> None: ...

class CopyScenarioReq(_message.Message):
    __slots__ = ("scenario_sid_to_copy", "include_inactive", "name", "description", "schedule_range")
    SCENARIO_SID_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RANGE_FIELD_NUMBER: _ClassVar[int]
    scenario_sid_to_copy: int
    include_inactive: bool
    name: str
    description: str
    schedule_range: _wfm_pb2.DatetimeRange
    def __init__(self, scenario_sid_to_copy: _Optional[int] = ..., include_inactive: bool = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., schedule_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ...) -> None: ...

class CopyScenarioRes(_message.Message):
    __slots__ = ("schedule_scenario_sid",)
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    def __init__(self, schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class CreateScheduleScenarioWithNodesReq(_message.Message):
    __slots__ = ("schedule_scenario", "call_center_node_name", "call_center_node_description", "client_node_name", "client_node_description", "location_node_name", "location_node_description", "program_node_name", "program_node_description", "time_zone_val", "skill_profile_category")
    SCHEDULE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    CALL_CENTER_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_CENTER_NODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_NODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_VAL_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario: ScheduleScenario
    call_center_node_name: str
    call_center_node_description: str
    client_node_name: str
    client_node_description: str
    location_node_name: str
    location_node_description: str
    program_node_name: str
    program_node_description: str
    time_zone_val: _org_pb2.TimeZone
    skill_profile_category: _wfm_pb2.SkillProfileCategory
    def __init__(self, schedule_scenario: _Optional[_Union[ScheduleScenario, _Mapping]] = ..., call_center_node_name: _Optional[str] = ..., call_center_node_description: _Optional[str] = ..., client_node_name: _Optional[str] = ..., client_node_description: _Optional[str] = ..., location_node_name: _Optional[str] = ..., location_node_description: _Optional[str] = ..., program_node_name: _Optional[str] = ..., program_node_description: _Optional[str] = ..., time_zone_val: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., skill_profile_category: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class CreateScheduleScenarioWithNodesRes(_message.Message):
    __slots__ = ("schedule_scenario_sid",)
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    def __init__(self, schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class UpdateScheduleScenarioReq(_message.Message):
    __slots__ = ("scheduleScenario",)
    SCHEDULESCENARIO_FIELD_NUMBER: _ClassVar[int]
    scheduleScenario: ScheduleScenario
    def __init__(self, scheduleScenario: _Optional[_Union[ScheduleScenario, _Mapping]] = ...) -> None: ...

class UpdateScheduleScenarioRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConfigEntitiesReq(_message.Message):
    __slots__ = ("entity_type", "belongs_to_entity", "include_inactive", "member_depth", "schedule_scenario_sid")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    BELONGS_TO_ENTITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_DEPTH_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    entity_type: _wfm_pb2.ConfigEntityType
    belongs_to_entity: ParentEntity
    include_inactive: bool
    member_depth: int
    schedule_scenario_sid: int
    def __init__(self, entity_type: _Optional[_Union[_wfm_pb2.ConfigEntityType, str]] = ..., belongs_to_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., include_inactive: bool = ..., member_depth: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class ListConfigEntitiesRes(_message.Message):
    __slots__ = ("call_center_node", "client_nodes", "location_nodes", "program_nodes", "agent_groups", "shift_templates", "wfm_agents", "placement_rules", "constraint_rules", "non_skill_activities", "agent_availability_patterns", "open_times_patterns", "scheduling_activity", "skill_proficiencies", "schedule_scenarios")
    class ClientNodeEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[ClientNode]
        def __init__(self, entities: _Optional[_Iterable[_Union[ClientNode, _Mapping]]] = ...) -> None: ...
    class LocationNodeEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[LocationNode]
        def __init__(self, entities: _Optional[_Iterable[_Union[LocationNode, _Mapping]]] = ...) -> None: ...
    class ProgramNodeEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[ProgramNode]
        def __init__(self, entities: _Optional[_Iterable[_Union[ProgramNode, _Mapping]]] = ...) -> None: ...
    class AgentGroupEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[AgentGroup]
        def __init__(self, entities: _Optional[_Iterable[_Union[AgentGroup, _Mapping]]] = ...) -> None: ...
    class ShiftTemplateEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[ShiftTemplate]
        def __init__(self, entities: _Optional[_Iterable[_Union[ShiftTemplate, _Mapping]]] = ...) -> None: ...
    class WFMAgentEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[WFMAgent]
        def __init__(self, entities: _Optional[_Iterable[_Union[WFMAgent, _Mapping]]] = ...) -> None: ...
    class PlacementRuleEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[PlacementRule]
        def __init__(self, entities: _Optional[_Iterable[_Union[PlacementRule, _Mapping]]] = ...) -> None: ...
    class ConstraintRuleEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[ConstraintRule]
        def __init__(self, entities: _Optional[_Iterable[_Union[ConstraintRule, _Mapping]]] = ...) -> None: ...
    class NonSkillActivityEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[NonSkillActivity]
        def __init__(self, entities: _Optional[_Iterable[_Union[NonSkillActivity, _Mapping]]] = ...) -> None: ...
    class AgentAvailabilityPatternEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[AgentAvailabilityPattern]
        def __init__(self, entities: _Optional[_Iterable[_Union[AgentAvailabilityPattern, _Mapping]]] = ...) -> None: ...
    class OpenTimesPatternEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[OpenTimesPattern]
        def __init__(self, entities: _Optional[_Iterable[_Union[OpenTimesPattern, _Mapping]]] = ...) -> None: ...
    class SkillProficiencyEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[SkillProficiency]
        def __init__(self, entities: _Optional[_Iterable[_Union[SkillProficiency, _Mapping]]] = ...) -> None: ...
    class ScheduleScenarioEntities(_message.Message):
        __slots__ = ("entities",)
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        entities: _containers.RepeatedCompositeFieldContainer[ScheduleScenario]
        def __init__(self, entities: _Optional[_Iterable[_Union[ScheduleScenario, _Mapping]]] = ...) -> None: ...
    CALL_CENTER_NODE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NODES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NODES_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_NODES_FIELD_NUMBER: _ClassVar[int]
    AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENTS_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_RULES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_RULES_FIELD_NUMBER: _ClassVar[int]
    NON_SKILL_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    AGENT_AVAILABILITY_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    OPEN_TIMES_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFICIENCIES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    call_center_node: CallCenterNode
    client_nodes: ListConfigEntitiesRes.ClientNodeEntities
    location_nodes: ListConfigEntitiesRes.LocationNodeEntities
    program_nodes: ListConfigEntitiesRes.ProgramNodeEntities
    agent_groups: ListConfigEntitiesRes.AgentGroupEntities
    shift_templates: ListConfigEntitiesRes.ShiftTemplateEntities
    wfm_agents: ListConfigEntitiesRes.WFMAgentEntities
    placement_rules: ListConfigEntitiesRes.PlacementRuleEntities
    constraint_rules: ListConfigEntitiesRes.ConstraintRuleEntities
    non_skill_activities: ListConfigEntitiesRes.NonSkillActivityEntities
    agent_availability_patterns: ListConfigEntitiesRes.AgentAvailabilityPatternEntities
    open_times_patterns: ListConfigEntitiesRes.OpenTimesPatternEntities
    scheduling_activity: SchedulingActivity
    skill_proficiencies: ListConfigEntitiesRes.SkillProficiencyEntities
    schedule_scenarios: ListConfigEntitiesRes.ScheduleScenarioEntities
    def __init__(self, call_center_node: _Optional[_Union[CallCenterNode, _Mapping]] = ..., client_nodes: _Optional[_Union[ListConfigEntitiesRes.ClientNodeEntities, _Mapping]] = ..., location_nodes: _Optional[_Union[ListConfigEntitiesRes.LocationNodeEntities, _Mapping]] = ..., program_nodes: _Optional[_Union[ListConfigEntitiesRes.ProgramNodeEntities, _Mapping]] = ..., agent_groups: _Optional[_Union[ListConfigEntitiesRes.AgentGroupEntities, _Mapping]] = ..., shift_templates: _Optional[_Union[ListConfigEntitiesRes.ShiftTemplateEntities, _Mapping]] = ..., wfm_agents: _Optional[_Union[ListConfigEntitiesRes.WFMAgentEntities, _Mapping]] = ..., placement_rules: _Optional[_Union[ListConfigEntitiesRes.PlacementRuleEntities, _Mapping]] = ..., constraint_rules: _Optional[_Union[ListConfigEntitiesRes.ConstraintRuleEntities, _Mapping]] = ..., non_skill_activities: _Optional[_Union[ListConfigEntitiesRes.NonSkillActivityEntities, _Mapping]] = ..., agent_availability_patterns: _Optional[_Union[ListConfigEntitiesRes.AgentAvailabilityPatternEntities, _Mapping]] = ..., open_times_patterns: _Optional[_Union[ListConfigEntitiesRes.OpenTimesPatternEntities, _Mapping]] = ..., scheduling_activity: _Optional[_Union[SchedulingActivity, _Mapping]] = ..., skill_proficiencies: _Optional[_Union[ListConfigEntitiesRes.SkillProficiencyEntities, _Mapping]] = ..., schedule_scenarios: _Optional[_Union[ListConfigEntitiesRes.ScheduleScenarioEntities, _Mapping]] = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ("level", "code", "message", "source_entity")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    level: _wfm_pb2.DiagnosticLevel
    code: _wfm_pb2.DiagnosticCode
    message: str
    source_entity: ParentEntity
    def __init__(self, level: _Optional[_Union[_wfm_pb2.DiagnosticLevel, str]] = ..., code: _Optional[_Union[_wfm_pb2.DiagnosticCode, str]] = ..., message: _Optional[str] = ..., source_entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class Diagnostics(_message.Message):
    __slots__ = ("source_entity", "diagnostics")
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    source_entity: ParentEntity
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, source_entity: _Optional[_Union[ParentEntity, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class DeleteShiftInstancesReq(_message.Message):
    __slots__ = ("shift_instance_sids",)
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, shift_instance_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteShiftInstancesRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BuildNodeDiagnosticsReq(_message.Message):
    __slots__ = ("node_to_check", "schedule_scenario_sid")
    NODE_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    node_to_check: ParentEntity
    schedule_scenario_sid: int
    def __init__(self, node_to_check: _Optional[_Union[ParentEntity, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class BuildNodeDiagnosticsRes(_message.Message):
    __slots__ = ("diagnostics", "nodes_checked")
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    NODES_CHECKED_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    nodes_checked: _containers.RepeatedCompositeFieldContainer[ParentEntity]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ..., nodes_checked: _Optional[_Iterable[_Union[ParentEntity, _Mapping]]] = ...) -> None: ...

class BuildGlobalDiagnosticsReq(_message.Message):
    __slots__ = ("schedule_scenario_sid",)
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    def __init__(self, schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class BuildGlobalDiagnosticsRes(_message.Message):
    __slots__ = ("diagnostics", "nodes_checked")
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    NODES_CHECKED_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    nodes_checked: _containers.RepeatedCompositeFieldContainer[ParentEntity]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ..., nodes_checked: _Optional[_Iterable[_Union[ParentEntity, _Mapping]]] = ...) -> None: ...

class PublishedSchedule(_message.Message):
    __slots__ = ("published_schedule_sid", "created_at", "last_updated_at", "shift_instances", "performance_metrics", "performance_metrics_v2")
    PUBLISHED_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_V2_FIELD_NUMBER: _ClassVar[int]
    published_schedule_sid: int
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    performance_metrics: _containers.RepeatedCompositeFieldContainer[PerformanceMetric]
    performance_metrics_v2: _containers.RepeatedCompositeFieldContainer[PerformanceMetricV2]
    def __init__(self, published_schedule_sid: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., performance_metrics: _Optional[_Iterable[_Union[PerformanceMetric, _Mapping]]] = ..., performance_metrics_v2: _Optional[_Iterable[_Union[PerformanceMetricV2, _Mapping]]] = ...) -> None: ...

class DraftSchedule(_message.Message):
    __slots__ = ("draft_schedule_sid", "created_at", "last_updated_at", "name", "description", "datetime_range", "created_by_user_id", "shift_instances", "performance_metrics", "schedule_scenario_sid", "performance_metrics_v2")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_V2_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    created_at: _timestamp_pb2.Timestamp
    last_updated_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    datetime_range: _wfm_pb2.DatetimeRange
    created_by_user_id: str
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    performance_metrics: _containers.RepeatedCompositeFieldContainer[PerformanceMetric]
    schedule_scenario_sid: int
    performance_metrics_v2: _containers.RepeatedCompositeFieldContainer[PerformanceMetricV2]
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., performance_metrics: _Optional[_Iterable[_Union[PerformanceMetric, _Mapping]]] = ..., schedule_scenario_sid: _Optional[int] = ..., performance_metrics_v2: _Optional[_Iterable[_Union[PerformanceMetricV2, _Mapping]]] = ...) -> None: ...

class PerformanceMetricForSkillCollection(_message.Message):
    __slots__ = ("date_range", "total_calls_required", "total_ftes_achieved", "num_intervals_with_required_calls", "num_intervals_with_ftes_but_no_schedules", "num_intervals_with_ftes_but_no_forecasted_calls", "total_unscheduled_calls", "total_unnecessary_ftes", "interval_width_in_minutes", "metric_type", "fte_intervals", "service_level_intervals", "skill_collection")
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTES_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_REQUIRED_CALLS_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_FTES_BUT_NO_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_FTES_BUT_NO_FORECASTED_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNSCHEDULED_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNNECESSARY_FTES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    FTE_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    date_range: _wfm_pb2.DatetimeRange
    total_calls_required: int
    total_ftes_achieved: int
    num_intervals_with_required_calls: int
    num_intervals_with_ftes_but_no_schedules: int
    num_intervals_with_ftes_but_no_forecasted_calls: int
    total_unscheduled_calls: int
    total_unnecessary_ftes: int
    interval_width_in_minutes: int
    metric_type: _wfm_pb2.PerformanceMetricType
    fte_intervals: _containers.RepeatedCompositeFieldContainer[FTERequiredVsAchievedInterval]
    service_level_intervals: _containers.RepeatedCompositeFieldContainer[ServiceLevelInterval]
    skill_collection: _wfm_pb2.SkillProfileCategory
    def __init__(self, date_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., total_calls_required: _Optional[int] = ..., total_ftes_achieved: _Optional[int] = ..., num_intervals_with_required_calls: _Optional[int] = ..., num_intervals_with_ftes_but_no_schedules: _Optional[int] = ..., num_intervals_with_ftes_but_no_forecasted_calls: _Optional[int] = ..., total_unscheduled_calls: _Optional[int] = ..., total_unnecessary_ftes: _Optional[int] = ..., interval_width_in_minutes: _Optional[int] = ..., metric_type: _Optional[_Union[_wfm_pb2.PerformanceMetricType, str]] = ..., fte_intervals: _Optional[_Iterable[_Union[FTERequiredVsAchievedInterval, _Mapping]]] = ..., service_level_intervals: _Optional[_Iterable[_Union[ServiceLevelInterval, _Mapping]]] = ..., skill_collection: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class PerformanceMetric(_message.Message):
    __slots__ = ("date_range", "total_calls_required", "total_ftes_achieved", "num_intervals_with_required_calls", "num_intervals_with_ftes_but_no_schedules", "num_intervals_with_ftes_but_no_forecasted_calls", "total_unscheduled_calls", "total_unnecessary_ftes", "interval_width_in_minutes", "metric_type", "fte_intervals", "service_level_intervals", "metrics_by_skill_collection")
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CALLS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTES_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_REQUIRED_CALLS_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_FTES_BUT_NO_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_FTES_BUT_NO_FORECASTED_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNSCHEDULED_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNNECESSARY_FTES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    FTE_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    METRICS_BY_SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    date_range: _wfm_pb2.DatetimeRange
    total_calls_required: int
    total_ftes_achieved: int
    num_intervals_with_required_calls: int
    num_intervals_with_ftes_but_no_schedules: int
    num_intervals_with_ftes_but_no_forecasted_calls: int
    total_unscheduled_calls: int
    total_unnecessary_ftes: int
    interval_width_in_minutes: int
    metric_type: _wfm_pb2.PerformanceMetricType
    fte_intervals: _containers.RepeatedCompositeFieldContainer[FTERequiredVsAchievedInterval]
    service_level_intervals: _containers.RepeatedCompositeFieldContainer[ServiceLevelInterval]
    metrics_by_skill_collection: _containers.RepeatedCompositeFieldContainer[PerformanceMetricForSkillCollection]
    def __init__(self, date_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., total_calls_required: _Optional[int] = ..., total_ftes_achieved: _Optional[int] = ..., num_intervals_with_required_calls: _Optional[int] = ..., num_intervals_with_ftes_but_no_schedules: _Optional[int] = ..., num_intervals_with_ftes_but_no_forecasted_calls: _Optional[int] = ..., total_unscheduled_calls: _Optional[int] = ..., total_unnecessary_ftes: _Optional[int] = ..., interval_width_in_minutes: _Optional[int] = ..., metric_type: _Optional[_Union[_wfm_pb2.PerformanceMetricType, str]] = ..., fte_intervals: _Optional[_Iterable[_Union[FTERequiredVsAchievedInterval, _Mapping]]] = ..., service_level_intervals: _Optional[_Iterable[_Union[ServiceLevelInterval, _Mapping]]] = ..., metrics_by_skill_collection: _Optional[_Iterable[_Union[PerformanceMetricForSkillCollection, _Mapping]]] = ...) -> None: ...

class PerformanceMetricForSkillCollectionV2(_message.Message):
    __slots__ = ("date_range", "total_fte_intervals_required", "total_fte_intervals_achieved", "num_intervals_with_call_ftes", "num_intervals_with_shift_ftes", "num_intervals_with_call_ftes_but_no_shifts", "num_intervals_with_shifts_but_no_call_ftes", "total_underscheduled_call_ftes", "total_overscheduled_call_ftes", "interval_width_in_minutes", "metric_type", "fte_occupancy_intervals", "service_level_intervals", "skill_collection", "total_required_fte", "total_achieved_fte", "total_productive_fte")
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTE_INTERVALS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTE_INTERVALS_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_SHIFT_FTES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_CALL_FTES_BUT_NO_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_SHIFTS_BUT_NO_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNDERSCHEDULED_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OVERSCHEDULED_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    FTE_OCCUPANCY_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REQUIRED_FTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACHIEVED_FTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRODUCTIVE_FTE_FIELD_NUMBER: _ClassVar[int]
    date_range: _wfm_pb2.DatetimeRange
    total_fte_intervals_required: float
    total_fte_intervals_achieved: float
    num_intervals_with_call_ftes: int
    num_intervals_with_shift_ftes: int
    num_intervals_with_call_ftes_but_no_shifts: int
    num_intervals_with_shifts_but_no_call_ftes: int
    total_underscheduled_call_ftes: float
    total_overscheduled_call_ftes: float
    interval_width_in_minutes: int
    metric_type: _wfm_pb2.PerformanceMetricType
    fte_occupancy_intervals: _containers.RepeatedCompositeFieldContainer[FTERequiredVsAchievedOccupancyInterval]
    service_level_intervals: _containers.RepeatedCompositeFieldContainer[ServiceLevelInterval]
    skill_collection: _wfm_pb2.SkillProfileCategory
    total_required_fte: float
    total_achieved_fte: float
    total_productive_fte: float
    def __init__(self, date_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., total_fte_intervals_required: _Optional[float] = ..., total_fte_intervals_achieved: _Optional[float] = ..., num_intervals_with_call_ftes: _Optional[int] = ..., num_intervals_with_shift_ftes: _Optional[int] = ..., num_intervals_with_call_ftes_but_no_shifts: _Optional[int] = ..., num_intervals_with_shifts_but_no_call_ftes: _Optional[int] = ..., total_underscheduled_call_ftes: _Optional[float] = ..., total_overscheduled_call_ftes: _Optional[float] = ..., interval_width_in_minutes: _Optional[int] = ..., metric_type: _Optional[_Union[_wfm_pb2.PerformanceMetricType, str]] = ..., fte_occupancy_intervals: _Optional[_Iterable[_Union[FTERequiredVsAchievedOccupancyInterval, _Mapping]]] = ..., service_level_intervals: _Optional[_Iterable[_Union[ServiceLevelInterval, _Mapping]]] = ..., skill_collection: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ..., total_required_fte: _Optional[float] = ..., total_achieved_fte: _Optional[float] = ..., total_productive_fte: _Optional[float] = ...) -> None: ...

class PerformanceMetricV2(_message.Message):
    __slots__ = ("date_range", "total_fte_intervals_required", "total_fte_intervals_achieved", "num_intervals_with_call_ftes", "num_intervals_with_shift_ftes", "num_intervals_with_call_ftes_but_no_shifts", "num_intervals_with_shifts_but_no_call_ftes", "total_underscheduled_call_ftes", "total_overscheduled_call_ftes", "interval_width_in_minutes", "metric_type", "fte_occupancy_intervals", "service_level_intervals", "metrics_by_skill_collection", "total_required_fte", "total_achieved_fte", "total_productive_fte")
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTE_INTERVALS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTE_INTERVALS_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_SHIFT_FTES_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_CALL_FTES_BUT_NO_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    NUM_INTERVALS_WITH_SHIFTS_BUT_NO_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UNDERSCHEDULED_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OVERSCHEDULED_CALL_FTES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    FTE_OCCUPANCY_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    METRICS_BY_SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REQUIRED_FTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACHIEVED_FTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRODUCTIVE_FTE_FIELD_NUMBER: _ClassVar[int]
    date_range: _wfm_pb2.DatetimeRange
    total_fte_intervals_required: float
    total_fte_intervals_achieved: float
    num_intervals_with_call_ftes: int
    num_intervals_with_shift_ftes: int
    num_intervals_with_call_ftes_but_no_shifts: int
    num_intervals_with_shifts_but_no_call_ftes: int
    total_underscheduled_call_ftes: float
    total_overscheduled_call_ftes: float
    interval_width_in_minutes: int
    metric_type: _wfm_pb2.PerformanceMetricType
    fte_occupancy_intervals: _containers.RepeatedCompositeFieldContainer[FTERequiredVsAchievedOccupancyInterval]
    service_level_intervals: _containers.RepeatedCompositeFieldContainer[ServiceLevelInterval]
    metrics_by_skill_collection: _containers.RepeatedCompositeFieldContainer[PerformanceMetricForSkillCollectionV2]
    total_required_fte: float
    total_achieved_fte: float
    total_productive_fte: float
    def __init__(self, date_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., total_fte_intervals_required: _Optional[float] = ..., total_fte_intervals_achieved: _Optional[float] = ..., num_intervals_with_call_ftes: _Optional[int] = ..., num_intervals_with_shift_ftes: _Optional[int] = ..., num_intervals_with_call_ftes_but_no_shifts: _Optional[int] = ..., num_intervals_with_shifts_but_no_call_ftes: _Optional[int] = ..., total_underscheduled_call_ftes: _Optional[float] = ..., total_overscheduled_call_ftes: _Optional[float] = ..., interval_width_in_minutes: _Optional[int] = ..., metric_type: _Optional[_Union[_wfm_pb2.PerformanceMetricType, str]] = ..., fte_occupancy_intervals: _Optional[_Iterable[_Union[FTERequiredVsAchievedOccupancyInterval, _Mapping]]] = ..., service_level_intervals: _Optional[_Iterable[_Union[ServiceLevelInterval, _Mapping]]] = ..., metrics_by_skill_collection: _Optional[_Iterable[_Union[PerformanceMetricForSkillCollectionV2, _Mapping]]] = ..., total_required_fte: _Optional[float] = ..., total_achieved_fte: _Optional[float] = ..., total_productive_fte: _Optional[float] = ...) -> None: ...

class ServiceLevelInterval(_message.Message):
    __slots__ = ("start_datetime", "service_level_achieved")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    service_level_achieved: float
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., service_level_achieved: _Optional[float] = ...) -> None: ...

class FTERequiredVsAchievedInterval(_message.Message):
    __slots__ = ("start_datetime", "required_calls", "achieved_ftes")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CALLS_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_FTES_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    required_calls: int
    achieved_ftes: int
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., required_calls: _Optional[int] = ..., achieved_ftes: _Optional[int] = ...) -> None: ...

class FTERequiredVsAchievedOccupancyInterval(_message.Message):
    __slots__ = ("start_datetime", "required_fte_occupancy", "achieved_fte_occupancy", "required_fte", "achieved_fte", "productive_fte")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FTE_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_FTE_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FTE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_FTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIVE_FTE_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    required_fte_occupancy: float
    achieved_fte_occupancy: float
    required_fte: float
    achieved_fte: float
    productive_fte: float
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., required_fte_occupancy: _Optional[float] = ..., achieved_fte_occupancy: _Optional[float] = ..., required_fte: _Optional[float] = ..., achieved_fte: _Optional[float] = ..., productive_fte: _Optional[float] = ...) -> None: ...

class RequiredCallsInterval(_message.Message):
    __slots__ = ("start_datetime", "required_calls")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CALLS_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    required_calls: int
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., required_calls: _Optional[int] = ...) -> None: ...

class ShiftInstance(_message.Message):
    __slots__ = ("shift_instance_sid", "start_datetime", "is_locked", "width_in_minutes", "shift_template_sid", "originating_program_node_sid", "schedule_sid", "wfm_agent_sid", "schedule_type", "shift_segments", "shift_template", "planned_shrinkage_percent")
    SHIFT_INSTANCE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    ORIGINATING_PROGRAM_NODE_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PLANNED_SHRINKAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    is_locked: bool
    width_in_minutes: int
    shift_template_sid: int
    originating_program_node_sid: int
    schedule_sid: int
    wfm_agent_sid: int
    schedule_type: _wfm_pb2.ScheduleType
    shift_segments: _containers.RepeatedCompositeFieldContainer[ShiftSegment]
    shift_template: ShiftTemplate
    planned_shrinkage_percent: float
    def __init__(self, shift_instance_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_locked: bool = ..., width_in_minutes: _Optional[int] = ..., shift_template_sid: _Optional[int] = ..., originating_program_node_sid: _Optional[int] = ..., schedule_sid: _Optional[int] = ..., wfm_agent_sid: _Optional[int] = ..., schedule_type: _Optional[_Union[_wfm_pb2.ScheduleType, str]] = ..., shift_segments: _Optional[_Iterable[_Union[ShiftSegment, _Mapping]]] = ..., shift_template: _Optional[_Union[ShiftTemplate, _Mapping]] = ..., planned_shrinkage_percent: _Optional[float] = ...) -> None: ...

class ShiftSegmentCallStat(_message.Message):
    __slots__ = ("num_calls", "percent_fit", "skill_collection")
    NUM_CALLS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIT_FIELD_NUMBER: _ClassVar[int]
    SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    num_calls: float
    percent_fit: float
    skill_collection: _wfm_pb2.SkillProfileCategory
    def __init__(self, num_calls: _Optional[float] = ..., percent_fit: _Optional[float] = ..., skill_collection: _Optional[_Union[_wfm_pb2.SkillProfileCategory, _Mapping]] = ...) -> None: ...

class ShiftSegment(_message.Message):
    __slots__ = ("shift_segment_sid", "shift_instance_sid", "order_in_shift_instance", "width_in_minutes", "start_minute_in_shift", "scheduling_activity_sid", "scheduling_activity", "call_stats_by_skill_collection")
    SHIFT_SEGMENT_SID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_INSTANCE_SID_FIELD_NUMBER: _ClassVar[int]
    ORDER_IN_SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_IN_SHIFT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    CALL_STATS_BY_SKILL_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    shift_segment_sid: int
    shift_instance_sid: int
    order_in_shift_instance: int
    width_in_minutes: int
    start_minute_in_shift: int
    scheduling_activity_sid: int
    scheduling_activity: SchedulingActivity
    call_stats_by_skill_collection: _containers.RepeatedCompositeFieldContainer[ShiftSegmentCallStat]
    def __init__(self, shift_segment_sid: _Optional[int] = ..., shift_instance_sid: _Optional[int] = ..., order_in_shift_instance: _Optional[int] = ..., width_in_minutes: _Optional[int] = ..., start_minute_in_shift: _Optional[int] = ..., scheduling_activity_sid: _Optional[int] = ..., scheduling_activity: _Optional[_Union[SchedulingActivity, _Mapping]] = ..., call_stats_by_skill_collection: _Optional[_Iterable[_Union[ShiftSegmentCallStat, _Mapping]]] = ...) -> None: ...

class GetPublishedScheduleReq(_message.Message):
    __slots__ = ("datetime_range", "include_shift_instances", "include_shift_template", "include_shift_segments", "include_scheduling_activity", "include_activity", "node_selector")
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    datetime_range: _wfm_pb2.DatetimeRange
    include_shift_instances: bool
    include_shift_template: bool
    include_shift_segments: bool
    include_scheduling_activity: bool
    include_activity: bool
    node_selector: ParentEntity
    def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., include_shift_instances: bool = ..., include_shift_template: bool = ..., include_shift_segments: bool = ..., include_scheduling_activity: bool = ..., include_activity: bool = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class GetPublishedScheduleRes(_message.Message):
    __slots__ = ("published_schedule",)
    PUBLISHED_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    published_schedule: PublishedSchedule
    def __init__(self, published_schedule: _Optional[_Union[PublishedSchedule, _Mapping]] = ...) -> None: ...

class GetPublishedScheduleRequiredCallsReq(_message.Message):
    __slots__ = ("viewing_range", "interval_width_in_minutes")
    VIEWING_RANGE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    viewing_range: _wfm_pb2.DatetimeRange
    interval_width_in_minutes: int
    def __init__(self, viewing_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., interval_width_in_minutes: _Optional[int] = ...) -> None: ...

class GetPublishedScheduleRequiredCallsRes(_message.Message):
    __slots__ = ("interval_width_in_minutes", "required_calls_intervals")
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CALLS_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    interval_width_in_minutes: int
    required_calls_intervals: _containers.RepeatedCompositeFieldContainer[RequiredCallsInterval]
    def __init__(self, interval_width_in_minutes: _Optional[int] = ..., required_calls_intervals: _Optional[_Iterable[_Union[RequiredCallsInterval, _Mapping]]] = ...) -> None: ...

class GetDraftScheduleRequiredCallsReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "viewing_range", "interval_width_in_minutes")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    VIEWING_RANGE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    viewing_range: _wfm_pb2.DatetimeRange
    interval_width_in_minutes: int
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., viewing_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., interval_width_in_minutes: _Optional[int] = ...) -> None: ...

class GetDraftScheduleRequiredCallsRes(_message.Message):
    __slots__ = ("interval_width_in_minutes", "required_calls_intervals")
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CALLS_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    interval_width_in_minutes: int
    required_calls_intervals: _containers.RepeatedCompositeFieldContainer[RequiredCallsInterval]
    def __init__(self, interval_width_in_minutes: _Optional[int] = ..., required_calls_intervals: _Optional[_Iterable[_Union[RequiredCallsInterval, _Mapping]]] = ...) -> None: ...

class CreateDraftScheduleReq(_message.Message):
    __slots__ = ("name", "description", "scheduling_range", "schedule_scenario_sid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_RANGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    scheduling_range: _wfm_pb2.DatetimeRange
    schedule_scenario_sid: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., scheduling_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class CreateDraftScheduleRes(_message.Message):
    __slots__ = ("draft_schedule_sid",)
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    def __init__(self, draft_schedule_sid: _Optional[int] = ...) -> None: ...

class UpdateDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "name", "description", "datetime_range", "delete_shifts_not_in_range", "copy_shifts_into_new_range", "get_updated_shifts")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_SHIFTS_NOT_IN_RANGE_FIELD_NUMBER: _ClassVar[int]
    COPY_SHIFTS_INTO_NEW_RANGE_FIELD_NUMBER: _ClassVar[int]
    GET_UPDATED_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    name: str
    description: str
    datetime_range: _wfm_pb2.DatetimeRange
    delete_shifts_not_in_range: bool
    copy_shifts_into_new_range: bool
    get_updated_shifts: bool
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., delete_shifts_not_in_range: bool = ..., copy_shifts_into_new_range: bool = ..., get_updated_shifts: bool = ...) -> None: ...

class UpdateDraftScheduleRes(_message.Message):
    __slots__ = ("draft_schedule",)
    DRAFT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    draft_schedule: DraftSchedule
    def __init__(self, draft_schedule: _Optional[_Union[DraftSchedule, _Mapping]] = ...) -> None: ...

class BuildDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "schedule_scenario_sid", "schedule_scenario_scheduling_range", "node_selector", "include_shift_instances", "include_shift_template", "include_shift_segments", "include_scheduling_activity", "include_activity", "auto_generate_agents")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SCHEDULING_RANGE_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    AUTO_GENERATE_AGENTS_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    schedule_scenario_sid: int
    schedule_scenario_scheduling_range: _wfm_pb2.DatetimeRange
    node_selector: ParentEntity
    include_shift_instances: bool
    include_shift_template: bool
    include_shift_segments: bool
    include_scheduling_activity: bool
    include_activity: bool
    auto_generate_agents: bool
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ..., schedule_scenario_scheduling_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., include_shift_instances: bool = ..., include_shift_template: bool = ..., include_shift_segments: bool = ..., include_scheduling_activity: bool = ..., include_activity: bool = ..., auto_generate_agents: bool = ...) -> None: ...

class BuildDraftScheduleRes(_message.Message):
    __slots__ = ("draft_schedule", "diagnostics", "scheduling_result_metric")
    DRAFT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_RESULT_METRIC_FIELD_NUMBER: _ClassVar[int]
    draft_schedule: DraftSchedule
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    scheduling_result_metric: _wfm_pb2.SchedulingResultMetric
    def __init__(self, draft_schedule: _Optional[_Union[DraftSchedule, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ..., scheduling_result_metric: _Optional[_Union[_wfm_pb2.SchedulingResultMetric, _Mapping]] = ...) -> None: ...

class PublishDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "node_selector", "datetime_range", "include_shift_instances", "include_shift_template", "include_shift_segments", "include_scheduling_activity", "include_activity", "ignore_diagnostics_errors")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DIAGNOSTICS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    node_selector: ParentEntity
    datetime_range: _wfm_pb2.DatetimeRange
    include_shift_instances: bool
    include_shift_template: bool
    include_shift_segments: bool
    include_scheduling_activity: bool
    include_activity: bool
    ignore_diagnostics_errors: bool
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., include_shift_instances: bool = ..., include_shift_template: bool = ..., include_shift_segments: bool = ..., include_scheduling_activity: bool = ..., include_activity: bool = ..., ignore_diagnostics_errors: bool = ...) -> None: ...

class PublishDraftScheduleRes(_message.Message):
    __slots__ = ("published_schedule", "diagnostics")
    PUBLISHED_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    published_schedule: PublishedSchedule
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, published_schedule: _Optional[_Union[PublishedSchedule, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class ResetDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "datetime_range", "unlocked_only")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_ONLY_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    datetime_range: _wfm_pb2.DatetimeRange
    unlocked_only: bool
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., unlocked_only: bool = ...) -> None: ...

class ResetDraftScheduleRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class GetDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "datetime_range", "include_shift_instances", "include_shift_template", "include_shift_segments", "include_scheduling_activity", "include_activity", "node_selector")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    datetime_range: _wfm_pb2.DatetimeRange
    include_shift_instances: bool
    include_shift_template: bool
    include_shift_segments: bool
    include_scheduling_activity: bool
    include_activity: bool
    node_selector: ParentEntity
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., include_shift_instances: bool = ..., include_shift_template: bool = ..., include_shift_segments: bool = ..., include_scheduling_activity: bool = ..., include_activity: bool = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class GetDraftScheduleRes(_message.Message):
    __slots__ = ("draft_schedule",)
    DRAFT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    draft_schedule: DraftSchedule
    def __init__(self, draft_schedule: _Optional[_Union[DraftSchedule, _Mapping]] = ...) -> None: ...

class ListDraftSchedulesReq(_message.Message):
    __slots__ = ("datetime_range",)
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    datetime_range: _wfm_pb2.DatetimeRange
    def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ...) -> None: ...

class ListDraftSchedulesRes(_message.Message):
    __slots__ = ("draft_schedules",)
    DRAFT_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    draft_schedules: _containers.RepeatedCompositeFieldContainer[DraftSchedule]
    def __init__(self, draft_schedules: _Optional[_Iterable[_Union[DraftSchedule, _Mapping]]] = ...) -> None: ...

class ClearScheduleReq(_message.Message):
    __slots__ = ("schedule_selector", "node_selector", "datetime_range", "invert_datetime_range", "start_datetimes_only", "delete_locked")
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INVERT_DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    START_DATETIMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOCKED_FIELD_NUMBER: _ClassVar[int]
    schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    datetime_range: _wfm_pb2.DatetimeRange
    invert_datetime_range: bool
    start_datetimes_only: bool
    delete_locked: bool
    def __init__(self, schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., invert_datetime_range: bool = ..., start_datetimes_only: bool = ..., delete_locked: bool = ...) -> None: ...

class ClearScheduleRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class DeleteDraftScheduleReq(_message.Message):
    __slots__ = ("draft_schedule_sid",)
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    def __init__(self, draft_schedule_sid: _Optional[int] = ...) -> None: ...

class DeleteDraftScheduleRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListShiftInstancesBySidReq(_message.Message):
    __slots__ = ("shift_instance_sids", "include_shift_segments", "include_shift_template", "include_scheduling_activity", "include_activity")
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SHIFT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    include_shift_segments: bool
    include_shift_template: bool
    include_scheduling_activity: bool
    include_activity: bool
    def __init__(self, shift_instance_sids: _Optional[_Iterable[int]] = ..., include_shift_segments: bool = ..., include_shift_template: bool = ..., include_scheduling_activity: bool = ..., include_activity: bool = ...) -> None: ...

class ListShiftInstancesBySidRes(_message.Message):
    __slots__ = ("shift_instances",)
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    def __init__(self, shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ...) -> None: ...

class CopyScheduleToScheduleReq(_message.Message):
    __slots__ = ("source_schedule_selector", "destination_schedule_selector", "node_selector", "datetime_range", "start_datetimes_only", "overlap_as_warning")
    SOURCE_SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    START_DATETIMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    OVERLAP_AS_WARNING_FIELD_NUMBER: _ClassVar[int]
    source_schedule_selector: _wfm_pb2.ScheduleSelector
    destination_schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    datetime_range: _wfm_pb2.DatetimeRange
    start_datetimes_only: bool
    overlap_as_warning: bool
    def __init__(self, source_schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., destination_schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., start_datetimes_only: bool = ..., overlap_as_warning: bool = ...) -> None: ...

class CopyScheduleToScheduleRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class CreateShiftInstanceReq(_message.Message):
    __slots__ = ("draft_schedule_sid", "shift_template_sid", "start_datetime", "width_in_minutes", "is_locked", "wfm_agent_sid", "metric_types")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    shift_template_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    width_in_minutes: int
    is_locked: bool
    wfm_agent_sid: _wrappers_pb2.Int64Value
    metric_types: _containers.RepeatedScalarFieldContainer[_wfm_pb2.PerformanceMetricType]
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., shift_template_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., width_in_minutes: _Optional[int] = ..., is_locked: bool = ..., wfm_agent_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., metric_types: _Optional[_Iterable[_Union[_wfm_pb2.PerformanceMetricType, str]]] = ...) -> None: ...

class CreateShiftInstanceRes(_message.Message):
    __slots__ = ("shift_instance", "performance_metrics", "performance_metrics_v2")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_V2_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    performance_metrics: _containers.RepeatedCompositeFieldContainer[PerformanceMetric]
    performance_metrics_v2: _containers.RepeatedCompositeFieldContainer[PerformanceMetricV2]
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., performance_metrics: _Optional[_Iterable[_Union[PerformanceMetric, _Mapping]]] = ..., performance_metrics_v2: _Optional[_Iterable[_Union[PerformanceMetricV2, _Mapping]]] = ...) -> None: ...

class CreateShiftInstanceV2Req(_message.Message):
    __slots__ = ("draft_schedule_sid", "shift_template_sid", "start_datetime", "is_locked", "wfm_agent_sids")
    DRAFT_SCHEDULE_SID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    draft_schedule_sid: int
    shift_template_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    is_locked: bool
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, draft_schedule_sid: _Optional[int] = ..., shift_template_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_locked: bool = ..., wfm_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateShiftInstanceV2Res(_message.Message):
    __slots__ = ("shift_instances", "diagnostics")
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class CreateShiftInstanceWithSegmentsRequest(_message.Message):
    __slots__ = ("shift_instance", "ignore_diagnostics_errors")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DIAGNOSTICS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    ignore_diagnostics_errors: bool
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., ignore_diagnostics_errors: bool = ...) -> None: ...

class CreateShiftInstanceWithSegmentsResponse(_message.Message):
    __slots__ = ("shift_instance", "diagnostics")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class SplitShiftInstanceReq(_message.Message):
    __slots__ = ("shift_instance_sid", "time_to_split")
    SHIFT_INSTANCE_SID_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_SPLIT_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sid: int
    time_to_split: _timestamp_pb2.Timestamp
    def __init__(self, shift_instance_sid: _Optional[int] = ..., time_to_split: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SplitShiftInstanceRes(_message.Message):
    __slots__ = ("shift_instances", "diagnostics")
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class SwapShiftInstancesReq(_message.Message):
    __slots__ = ("wfm_agent_sid1", "wfm_agent_sid2", "shift_instance_sids")
    WFM_AGENT_SID1_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID2_FIELD_NUMBER: _ClassVar[int]
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sid1: int
    wfm_agent_sid2: int
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, wfm_agent_sid1: _Optional[int] = ..., wfm_agent_sid2: _Optional[int] = ..., shift_instance_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class SwapShiftInstancesRes(_message.Message):
    __slots__ = ("shift_instances", "diagnostics")
    SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class UpdateShiftInstanceReq(_message.Message):
    __slots__ = ("shift_instance_sid", "start_datetime", "is_locked", "width_in_minutes", "wfm_agent_sid", "metric_types")
    SHIFT_INSTANCE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    is_locked: bool
    width_in_minutes: int
    wfm_agent_sid: _wrappers_pb2.Int64Value
    metric_types: _containers.RepeatedScalarFieldContainer[_wfm_pb2.PerformanceMetricType]
    def __init__(self, shift_instance_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_locked: bool = ..., width_in_minutes: _Optional[int] = ..., wfm_agent_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., metric_types: _Optional[_Iterable[_Union[_wfm_pb2.PerformanceMetricType, str]]] = ...) -> None: ...

class UpdateShiftInstanceRes(_message.Message):
    __slots__ = ("shift_instance", "performance_metrics", "performance_metrics_v2")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_V2_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    performance_metrics: _containers.RepeatedCompositeFieldContainer[PerformanceMetric]
    performance_metrics_v2: _containers.RepeatedCompositeFieldContainer[PerformanceMetricV2]
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., performance_metrics: _Optional[_Iterable[_Union[PerformanceMetric, _Mapping]]] = ..., performance_metrics_v2: _Optional[_Iterable[_Union[PerformanceMetricV2, _Mapping]]] = ...) -> None: ...

class UpdateShiftInstanceV2Req(_message.Message):
    __slots__ = ("shift_instance_sid", "start_datetime", "width_in_minutes", "wfm_agent_sid", "is_locked", "planned_shrinkage_percent")
    SHIFT_INSTANCE_SID_FIELD_NUMBER: _ClassVar[int]
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    PLANNED_SHRINKAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sid: int
    start_datetime: _timestamp_pb2.Timestamp
    width_in_minutes: int
    wfm_agent_sid: int
    is_locked: bool
    planned_shrinkage_percent: float
    def __init__(self, shift_instance_sid: _Optional[int] = ..., start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., width_in_minutes: _Optional[int] = ..., wfm_agent_sid: _Optional[int] = ..., is_locked: bool = ..., planned_shrinkage_percent: _Optional[float] = ...) -> None: ...

class UpdateShiftInstanceV2Res(_message.Message):
    __slots__ = ("shift_instance", "diagnostics")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class UpdateShiftInstanceWithSegmentsRequest(_message.Message):
    __slots__ = ("shift_instance", "ignore_diagnostics_errors")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DIAGNOSTICS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    ignore_diagnostics_errors: bool
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., ignore_diagnostics_errors: bool = ...) -> None: ...

class UpdateShiftInstanceWithSegmentsResponse(_message.Message):
    __slots__ = ("shift_instance", "diagnostics")
    SHIFT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    shift_instance: ShiftInstance
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, shift_instance: _Optional[_Union[ShiftInstance, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class CopyShiftInstancesToScheduleReq(_message.Message):
    __slots__ = ("destination_schedule", "shift_instance_sids", "overlap_as_warning")
    DESTINATION_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    OVERLAP_AS_WARNING_FIELD_NUMBER: _ClassVar[int]
    destination_schedule: _wfm_pb2.ScheduleSelector
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    overlap_as_warning: bool
    def __init__(self, destination_schedule: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., shift_instance_sids: _Optional[_Iterable[int]] = ..., overlap_as_warning: bool = ...) -> None: ...

class CopyShiftInstancesToScheduleRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class ListShiftInstanceSidsForAgentReq(_message.Message):
    __slots__ = ("schedule_selector", "datetime_range", "wfm_agent_sid")
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    schedule_selector: _wfm_pb2.ScheduleSelector
    datetime_range: _wfm_pb2.DatetimeRange
    wfm_agent_sid: int
    def __init__(self, schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., wfm_agent_sid: _Optional[int] = ...) -> None: ...

class ListShiftInstanceSidsForAgentRes(_message.Message):
    __slots__ = ("shift_instance_sids",)
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, shift_instance_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListShiftSegmentsByShiftInstanceSidsReq(_message.Message):
    __slots__ = ("shift_instance_sids", "include_scheduling_activity", "include_activity")
    SHIFT_INSTANCE_SIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCHEDULING_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    shift_instance_sids: _containers.RepeatedScalarFieldContainer[int]
    include_scheduling_activity: bool
    include_activity: bool
    def __init__(self, shift_instance_sids: _Optional[_Iterable[int]] = ..., include_scheduling_activity: bool = ..., include_activity: bool = ...) -> None: ...

class ListShiftSegmentsByShiftInstanceSidsRes(_message.Message):
    __slots__ = ("shift_segments",)
    SHIFT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    shift_segments: _containers.RepeatedCompositeFieldContainer[ShiftSegment]
    def __init__(self, shift_segments: _Optional[_Iterable[_Union[ShiftSegment, _Mapping]]] = ...) -> None: ...

class PerformanceMetricParameter(_message.Message):
    __slots__ = ("metric_type", "service_level_target_duration_seconds")
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_TARGET_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    metric_type: _wfm_pb2.PerformanceMetricType
    service_level_target_duration_seconds: _wrappers_pb2.Int64Value
    def __init__(self, metric_type: _Optional[_Union[_wfm_pb2.PerformanceMetricType, str]] = ..., service_level_target_duration_seconds: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class GetPerformanceMetricsReq(_message.Message):
    __slots__ = ("schedule_selector", "node_selector", "datetime_range", "metric_params", "interval_width_in_minutes", "resync_call_stats")
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    METRIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    RESYNC_CALL_STATS_FIELD_NUMBER: _ClassVar[int]
    schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    datetime_range: _wfm_pb2.DatetimeRange
    metric_params: _containers.RepeatedCompositeFieldContainer[PerformanceMetricParameter]
    interval_width_in_minutes: int
    resync_call_stats: bool
    def __init__(self, schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., metric_params: _Optional[_Iterable[_Union[PerformanceMetricParameter, _Mapping]]] = ..., interval_width_in_minutes: _Optional[int] = ..., resync_call_stats: bool = ...) -> None: ...

class GetPerformanceMetricsRes(_message.Message):
    __slots__ = ("performance_metrics", "performance_metrics_v2")
    PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_METRICS_V2_FIELD_NUMBER: _ClassVar[int]
    performance_metrics: _containers.RepeatedCompositeFieldContainer[PerformanceMetric]
    performance_metrics_v2: _containers.RepeatedCompositeFieldContainer[PerformanceMetricV2]
    def __init__(self, performance_metrics: _Optional[_Iterable[_Union[PerformanceMetric, _Mapping]]] = ..., performance_metrics_v2: _Optional[_Iterable[_Union[PerformanceMetricV2, _Mapping]]] = ...) -> None: ...

class SchedulingTarget(_message.Message):
    __slots__ = ("scheduling_target_sid", "scheduling_target_type", "scheduling_target_percentage", "service_level_target_duration_seconds", "node_entity")
    SCHEDULING_TARGET_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_TARGET_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_TARGET_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NODE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    scheduling_target_sid: int
    scheduling_target_type: _wfm_pb2.SchedulingTargetType
    scheduling_target_percentage: float
    service_level_target_duration_seconds: _wrappers_pb2.Int64Value
    node_entity: ParentEntity
    def __init__(self, scheduling_target_sid: _Optional[int] = ..., scheduling_target_type: _Optional[_Union[_wfm_pb2.SchedulingTargetType, str]] = ..., scheduling_target_percentage: _Optional[float] = ..., service_level_target_duration_seconds: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., node_entity: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class SetSchedulingTargetReq(_message.Message):
    __slots__ = ("scheduling_target", "schedule_scenario_sid")
    SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    scheduling_target: SchedulingTarget
    schedule_scenario_sid: int
    def __init__(self, scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class SetSchedulingTargetRes(_message.Message):
    __slots__ = ("scheduling_target_sid",)
    SCHEDULING_TARGET_SID_FIELD_NUMBER: _ClassVar[int]
    scheduling_target_sid: int
    def __init__(self, scheduling_target_sid: _Optional[int] = ...) -> None: ...

class GetSchedulingTargetReq(_message.Message):
    __slots__ = ("node_selector",)
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    node_selector: ParentEntity
    def __init__(self, node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class GetSchedulingTargetRes(_message.Message):
    __slots__ = ("inherited_scheduling_target", "own_scheduling_target", "resulting_scheduling_target")
    INHERITED_SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    OWN_SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    inherited_scheduling_target: SchedulingTarget
    own_scheduling_target: SchedulingTarget
    resulting_scheduling_target: SchedulingTarget
    def __init__(self, inherited_scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ..., own_scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ..., resulting_scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ...) -> None: ...

class DeleteSchedulingTargetReq(_message.Message):
    __slots__ = ("node_selector",)
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    node_selector: ParentEntity
    def __init__(self, node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ...) -> None: ...

class DeleteSchedulingTargetRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultSchedulingTargetReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultSchedulingTargetRes(_message.Message):
    __slots__ = ("scheduling_target",)
    SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    scheduling_target: SchedulingTarget
    def __init__(self, scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ...) -> None: ...

class SetDefaultSchedulingTargetReq(_message.Message):
    __slots__ = ("scheduling_target",)
    SCHEDULING_TARGET_FIELD_NUMBER: _ClassVar[int]
    scheduling_target: SchedulingTarget
    def __init__(self, scheduling_target: _Optional[_Union[SchedulingTarget, _Mapping]] = ...) -> None: ...

class SetDefaultSchedulingTargetRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRequiredCallsIntervalsReq(_message.Message):
    __slots__ = ("node_selector", "datetime_range", "interval_width_in_minutes")
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    node_selector: ParentEntity
    datetime_range: _wfm_pb2.DatetimeRange
    interval_width_in_minutes: int
    def __init__(self, node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., interval_width_in_minutes: _Optional[int] = ...) -> None: ...

class ListRequiredCallsIntervalsRes(_message.Message):
    __slots__ = ("interval_width_in_minutes", "required_calls_intervals")
    INTERVAL_WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CALLS_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    interval_width_in_minutes: int
    required_calls_intervals: _containers.RepeatedCompositeFieldContainer[RequiredCallsInterval]
    def __init__(self, interval_width_in_minutes: _Optional[int] = ..., required_calls_intervals: _Optional[_Iterable[_Union[RequiredCallsInterval, _Mapping]]] = ...) -> None: ...

class TourShiftSegmentConfig(_message.Message):
    __slots__ = ("tour_shift_segment_config_sid", "tour_shift_instance_config_sid", "start_minute_in_shift", "width_in_minutes", "scheduling_activity_sid")
    TOUR_SHIFT_SEGMENT_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    TOUR_SHIFT_INSTANCE_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_IN_SHIFT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_ACTIVITY_SID_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_config_sid: int
    tour_shift_instance_config_sid: int
    start_minute_in_shift: int
    width_in_minutes: int
    scheduling_activity_sid: int
    def __init__(self, tour_shift_segment_config_sid: _Optional[int] = ..., tour_shift_instance_config_sid: _Optional[int] = ..., start_minute_in_shift: _Optional[int] = ..., width_in_minutes: _Optional[int] = ..., scheduling_activity_sid: _Optional[int] = ...) -> None: ...

class TourShiftInstanceConfig(_message.Message):
    __slots__ = ("tour_shift_instance_config_sid", "tour_week_pattern_sid", "start_minute_in_week", "width_in_minutes", "member_tour_shift_segment_configs")
    TOUR_SHIFT_INSTANCE_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    TOUR_WEEK_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    START_MINUTE_IN_WEEK_FIELD_NUMBER: _ClassVar[int]
    WIDTH_IN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TOUR_SHIFT_SEGMENT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config_sid: int
    tour_week_pattern_sid: int
    start_minute_in_week: int
    width_in_minutes: int
    member_tour_shift_segment_configs: _containers.RepeatedCompositeFieldContainer[TourShiftSegmentConfig]
    def __init__(self, tour_shift_instance_config_sid: _Optional[int] = ..., tour_week_pattern_sid: _Optional[int] = ..., start_minute_in_week: _Optional[int] = ..., width_in_minutes: _Optional[int] = ..., member_tour_shift_segment_configs: _Optional[_Iterable[_Union[TourShiftSegmentConfig, _Mapping]]] = ...) -> None: ...

class TourWeekPattern(_message.Message):
    __slots__ = ("tour_week_pattern_sid", "tour_pattern_sid", "week_pattern_number", "member_tour_shift_instance_configs")
    TOUR_WEEK_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    WEEK_PATTERN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TOUR_SHIFT_INSTANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    tour_week_pattern_sid: int
    tour_pattern_sid: int
    week_pattern_number: int
    member_tour_shift_instance_configs: _containers.RepeatedCompositeFieldContainer[TourShiftInstanceConfig]
    def __init__(self, tour_week_pattern_sid: _Optional[int] = ..., tour_pattern_sid: _Optional[int] = ..., week_pattern_number: _Optional[int] = ..., member_tour_shift_instance_configs: _Optional[_Iterable[_Union[TourShiftInstanceConfig, _Mapping]]] = ...) -> None: ...

class TourAgentCollection(_message.Message):
    __slots__ = ("tour_agent_collection_sid", "tour_pattern_sid", "min_agents_to_schedule", "max_agents_to_schedule", "first_week_pattern_number", "name", "wfm_agent_sids")
    TOUR_AGENT_COLLECTION_SID_FIELD_NUMBER: _ClassVar[int]
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    MIN_AGENTS_TO_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MAX_AGENTS_TO_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    FIRST_WEEK_PATTERN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection_sid: int
    tour_pattern_sid: int
    min_agents_to_schedule: int
    max_agents_to_schedule: int
    first_week_pattern_number: int
    name: str
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_agent_collection_sid: _Optional[int] = ..., tour_pattern_sid: _Optional[int] = ..., min_agents_to_schedule: _Optional[int] = ..., max_agents_to_schedule: _Optional[int] = ..., first_week_pattern_number: _Optional[int] = ..., name: _Optional[str] = ..., wfm_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class TourPattern(_message.Message):
    __slots__ = ("tour_pattern_sid", "shift_template_sid", "member_tour_week_patterns", "member_tour_agent_collections")
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TOUR_WEEK_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TOUR_AGENT_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    shift_template_sid: int
    member_tour_week_patterns: _containers.RepeatedCompositeFieldContainer[TourWeekPattern]
    member_tour_agent_collections: _containers.RepeatedCompositeFieldContainer[TourAgentCollection]
    def __init__(self, tour_pattern_sid: _Optional[int] = ..., shift_template_sid: _Optional[int] = ..., member_tour_week_patterns: _Optional[_Iterable[_Union[TourWeekPattern, _Mapping]]] = ..., member_tour_agent_collections: _Optional[_Iterable[_Union[TourAgentCollection, _Mapping]]] = ...) -> None: ...

class CreateTourPatternReq(_message.Message):
    __slots__ = ("shift_template_sid",)
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    def __init__(self, shift_template_sid: _Optional[int] = ...) -> None: ...

class CreateTourPatternRes(_message.Message):
    __slots__ = ("tour_pattern_sid",)
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    def __init__(self, tour_pattern_sid: _Optional[int] = ...) -> None: ...

class GetTourPatternDiagnosticsReq(_message.Message):
    __slots__ = ("tour_pattern",)
    TOUR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    tour_pattern: TourPattern
    def __init__(self, tour_pattern: _Optional[_Union[TourPattern, _Mapping]] = ...) -> None: ...

class GetTourPatternDiagnosticsRes(_message.Message):
    __slots__ = ("diagnostics",)
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class UpsertTourPatternWithMembersReq(_message.Message):
    __slots__ = ("tour_pattern",)
    TOUR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    tour_pattern: TourPattern
    def __init__(self, tour_pattern: _Optional[_Union[TourPattern, _Mapping]] = ...) -> None: ...

class UpsertTourPatternWithMembersRes(_message.Message):
    __slots__ = ("tour_pattern", "diagnostics")
    TOUR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    tour_pattern: TourPattern
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, tour_pattern: _Optional[_Union[TourPattern, _Mapping]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class GetTourPatternReq(_message.Message):
    __slots__ = ("shift_template_sid",)
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    def __init__(self, shift_template_sid: _Optional[int] = ...) -> None: ...

class GetTourPatternRes(_message.Message):
    __slots__ = ("tour_pattern",)
    TOUR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    tour_pattern: TourPattern
    def __init__(self, tour_pattern: _Optional[_Union[TourPattern, _Mapping]] = ...) -> None: ...

class GetTourPatternWithMembersReq(_message.Message):
    __slots__ = ("shift_template_sid",)
    SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    shift_template_sid: int
    def __init__(self, shift_template_sid: _Optional[int] = ...) -> None: ...

class GetTourPatternWithMembersRes(_message.Message):
    __slots__ = ("tour_pattern",)
    TOUR_PATTERN_FIELD_NUMBER: _ClassVar[int]
    tour_pattern: TourPattern
    def __init__(self, tour_pattern: _Optional[_Union[TourPattern, _Mapping]] = ...) -> None: ...

class DeleteTourPatternReq(_message.Message):
    __slots__ = ("tour_pattern_sid",)
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    def __init__(self, tour_pattern_sid: _Optional[int] = ...) -> None: ...

class DeleteTourPatternRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTourWeekPatternReq(_message.Message):
    __slots__ = ("tour_pattern_sid",)
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    def __init__(self, tour_pattern_sid: _Optional[int] = ...) -> None: ...

class CreateTourWeekPatternRes(_message.Message):
    __slots__ = ("tour_week_pattern_sid",)
    TOUR_WEEK_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_week_pattern_sid: int
    def __init__(self, tour_week_pattern_sid: _Optional[int] = ...) -> None: ...

class ListTourWeekPatternsReq(_message.Message):
    __slots__ = ("tour_pattern_sid",)
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    def __init__(self, tour_pattern_sid: _Optional[int] = ...) -> None: ...

class ListTourWeekPatternsRes(_message.Message):
    __slots__ = ("tour_week_patterns",)
    TOUR_WEEK_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    tour_week_patterns: _containers.RepeatedCompositeFieldContainer[TourWeekPattern]
    def __init__(self, tour_week_patterns: _Optional[_Iterable[_Union[TourWeekPattern, _Mapping]]] = ...) -> None: ...

class DeleteTourWeekPatternsReq(_message.Message):
    __slots__ = ("tour_week_pattern_sids",)
    TOUR_WEEK_PATTERN_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_week_pattern_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_week_pattern_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteTourWeekPatternsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTourShiftInstanceConfigReq(_message.Message):
    __slots__ = ("tour_shift_instance_config",)
    TOUR_SHIFT_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config: TourShiftInstanceConfig
    def __init__(self, tour_shift_instance_config: _Optional[_Union[TourShiftInstanceConfig, _Mapping]] = ...) -> None: ...

class CreateTourShiftInstanceConfigRes(_message.Message):
    __slots__ = ("tour_shift_instance_config_sid",)
    TOUR_SHIFT_INSTANCE_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config_sid: int
    def __init__(self, tour_shift_instance_config_sid: _Optional[int] = ...) -> None: ...

class UpdateTourShiftInstanceConfigReq(_message.Message):
    __slots__ = ("tour_shift_instance_config",)
    TOUR_SHIFT_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config: TourShiftInstanceConfig
    def __init__(self, tour_shift_instance_config: _Optional[_Union[TourShiftInstanceConfig, _Mapping]] = ...) -> None: ...

class UpdateTourShiftInstanceConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTourShiftInstanceConfigsReq(_message.Message):
    __slots__ = ("tour_week_pattern_sids",)
    TOUR_WEEK_PATTERN_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_week_pattern_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_week_pattern_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListTourShiftInstanceConfigsRes(_message.Message):
    __slots__ = ("tour_shift_instance_configs",)
    TOUR_SHIFT_INSTANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_configs: _containers.RepeatedCompositeFieldContainer[TourShiftInstanceConfig]
    def __init__(self, tour_shift_instance_configs: _Optional[_Iterable[_Union[TourShiftInstanceConfig, _Mapping]]] = ...) -> None: ...

class DeleteTourShiftInstanceConfigsReq(_message.Message):
    __slots__ = ("tour_shift_instance_config_sids",)
    TOUR_SHIFT_INSTANCE_CONFIG_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_shift_instance_config_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteTourShiftInstanceConfigsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTourShiftSegmentConfigReq(_message.Message):
    __slots__ = ("tour_shift_segment_config",)
    TOUR_SHIFT_SEGMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_config: TourShiftSegmentConfig
    def __init__(self, tour_shift_segment_config: _Optional[_Union[TourShiftSegmentConfig, _Mapping]] = ...) -> None: ...

class CreateTourShiftSegmentConfigRes(_message.Message):
    __slots__ = ("tour_shift_segment_config_sid",)
    TOUR_SHIFT_SEGMENT_CONFIG_SID_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_config_sid: int
    def __init__(self, tour_shift_segment_config_sid: _Optional[int] = ...) -> None: ...

class UpdateTourShiftSegmentConfigReq(_message.Message):
    __slots__ = ("tour_shift_segment_config",)
    TOUR_SHIFT_SEGMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_config: TourShiftSegmentConfig
    def __init__(self, tour_shift_segment_config: _Optional[_Union[TourShiftSegmentConfig, _Mapping]] = ...) -> None: ...

class UpdateTourShiftSegmentConfigRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTourShiftSegmentConfigsReq(_message.Message):
    __slots__ = ("tour_shift_instance_config_sids",)
    TOUR_SHIFT_INSTANCE_CONFIG_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_instance_config_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_shift_instance_config_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListTourShiftSegmentConfigsRes(_message.Message):
    __slots__ = ("tour_shift_segment_configs",)
    TOUR_SHIFT_SEGMENT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_configs: _containers.RepeatedCompositeFieldContainer[TourShiftSegmentConfig]
    def __init__(self, tour_shift_segment_configs: _Optional[_Iterable[_Union[TourShiftSegmentConfig, _Mapping]]] = ...) -> None: ...

class DeleteTourShiftSegmentConfigsReq(_message.Message):
    __slots__ = ("tour_shift_segment_config_sids",)
    TOUR_SHIFT_SEGMENT_CONFIG_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_shift_segment_config_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_shift_segment_config_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteTourShiftSegmentConfigsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTourAgentCollectionReq(_message.Message):
    __slots__ = ("tour_agent_collection",)
    TOUR_AGENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection: TourAgentCollection
    def __init__(self, tour_agent_collection: _Optional[_Union[TourAgentCollection, _Mapping]] = ...) -> None: ...

class CreateTourAgentCollectionRes(_message.Message):
    __slots__ = ("tour_agent_collection_sid",)
    TOUR_AGENT_COLLECTION_SID_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection_sid: int
    def __init__(self, tour_agent_collection_sid: _Optional[int] = ...) -> None: ...

class UpdateTourAgentCollectionReq(_message.Message):
    __slots__ = ("tour_agent_collection",)
    TOUR_AGENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection: TourAgentCollection
    def __init__(self, tour_agent_collection: _Optional[_Union[TourAgentCollection, _Mapping]] = ...) -> None: ...

class UpdateTourAgentCollectionRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTourAgentCollectionsReq(_message.Message):
    __slots__ = ("tour_pattern_sid",)
    TOUR_PATTERN_SID_FIELD_NUMBER: _ClassVar[int]
    tour_pattern_sid: int
    def __init__(self, tour_pattern_sid: _Optional[int] = ...) -> None: ...

class ListTourAgentCollectionsRes(_message.Message):
    __slots__ = ("tour_agent_collections",)
    TOUR_AGENT_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collections: _containers.RepeatedCompositeFieldContainer[TourAgentCollection]
    def __init__(self, tour_agent_collections: _Optional[_Iterable[_Union[TourAgentCollection, _Mapping]]] = ...) -> None: ...

class DeleteTourAgentCollectionsReq(_message.Message):
    __slots__ = ("tour_agent_collection_sids",)
    TOUR_AGENT_COLLECTION_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_agent_collection_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteTourAgentCollectionsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTourAgentCollectionWFMAgentsReq(_message.Message):
    __slots__ = ("wfm_agent_sids", "tour_agent_collection_sid")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    TOUR_AGENT_COLLECTION_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    tour_agent_collection_sid: int
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., tour_agent_collection_sid: _Optional[int] = ...) -> None: ...

class CreateTourAgentCollectionWFMAgentsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTourAgentCollectionWFMAgentsReq(_message.Message):
    __slots__ = ("tour_agent_collection_sids",)
    TOUR_AGENT_COLLECTION_SIDS_FIELD_NUMBER: _ClassVar[int]
    tour_agent_collection_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tour_agent_collection_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ListTourAgentCollectionWFMAgentsRes(_message.Message):
    __slots__ = ("wfm_agent_pairings",)
    class SidMapping(_message.Message):
        __slots__ = ("agent_collection_sid", "wfm_agent_sids")
        AGENT_COLLECTION_SID_FIELD_NUMBER: _ClassVar[int]
        WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
        agent_collection_sid: int
        wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, agent_collection_sid: _Optional[int] = ..., wfm_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    WFM_AGENT_PAIRINGS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_pairings: _containers.RepeatedCompositeFieldContainer[ListTourAgentCollectionWFMAgentsRes.SidMapping]
    def __init__(self, wfm_agent_pairings: _Optional[_Iterable[_Union[ListTourAgentCollectionWFMAgentsRes.SidMapping, _Mapping]]] = ...) -> None: ...

class DeleteTourAgentCollectionWFMAgentsReq(_message.Message):
    __slots__ = ("wfm_agent_sids", "tour_agent_collection_sid")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    TOUR_AGENT_COLLECTION_SID_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    tour_agent_collection_sid: int
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., tour_agent_collection_sid: _Optional[int] = ...) -> None: ...

class DeleteTourAgentCollectionWFMAgentsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateTourWeekPatternsReq(_message.Message):
    __slots__ = ("target_shift_template_sid", "num_weeks_in_tour", "schedule_scenario_sid")
    TARGET_SHIFT_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    NUM_WEEKS_IN_TOUR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    target_shift_template_sid: int
    num_weeks_in_tour: int
    schedule_scenario_sid: int
    def __init__(self, target_shift_template_sid: _Optional[int] = ..., num_weeks_in_tour: _Optional[int] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class GenerateTourWeekPatternsRes(_message.Message):
    __slots__ = ("tour_week_patterns", "diagnostics")
    TOUR_WEEK_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    tour_week_patterns: _containers.RepeatedCompositeFieldContainer[TourWeekPattern]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, tour_week_patterns: _Optional[_Iterable[_Union[TourWeekPattern, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class RemoveAgentFromScheduleRequest(_message.Message):
    __slots__ = ("datetime_range", "wfm_agent_sid", "schedule_selector", "node_selector", "schedule_scenario_sid")
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    datetime_range: _wfm_pb2.DatetimeRange
    wfm_agent_sid: int
    schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    schedule_scenario_sid: int
    def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., wfm_agent_sid: _Optional[int] = ..., schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., schedule_scenario_sid: _Optional[int] = ...) -> None: ...

class RemoveAgentFromScheduleResponse(_message.Message):
    __slots__ = ("unassigned_wfm_agent_sid", "updated_shifts")
    UNASSIGNED_WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    unassigned_wfm_agent_sid: int
    updated_shifts: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    def __init__(self, unassigned_wfm_agent_sid: _Optional[int] = ..., updated_shifts: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ...) -> None: ...

class ListValidAgentsForReplacementReq(_message.Message):
    __slots__ = ("schedule_scenario_sid", "datetime_range", "schedule_selector", "node_selector", "wfm_agent_sid_to_replace", "skip_skill_proficiency_sort", "include_skill_mismatches", "skip_force_same_agent_groups")
    SCHEDULE_SCENARIO_SID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_TO_REPLACE_FIELD_NUMBER: _ClassVar[int]
    SKIP_SKILL_PROFICIENCY_SORT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SKILL_MISMATCHES_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORCE_SAME_AGENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    schedule_scenario_sid: int
    datetime_range: _wfm_pb2.DatetimeRange
    schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    wfm_agent_sid_to_replace: int
    skip_skill_proficiency_sort: bool
    include_skill_mismatches: bool
    skip_force_same_agent_groups: bool
    def __init__(self, schedule_scenario_sid: _Optional[int] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., wfm_agent_sid_to_replace: _Optional[int] = ..., skip_skill_proficiency_sort: bool = ..., include_skill_mismatches: bool = ..., skip_force_same_agent_groups: bool = ...) -> None: ...

class ListValidAgentsForReplacementRes(_message.Message):
    __slots__ = ("wfm_agent_sids",)
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ...) -> None: ...

class ReplaceAgentOnScheduleReq(_message.Message):
    __slots__ = ("datetime_range", "schedule_selector", "node_selector", "wfm_agent_sid_to_remove", "wfm_agent_sid_to_add", "skip_overlapping_shifts")
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    SKIP_OVERLAPPING_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    datetime_range: _wfm_pb2.DatetimeRange
    schedule_selector: _wfm_pb2.ScheduleSelector
    node_selector: ParentEntity
    wfm_agent_sid_to_remove: int
    wfm_agent_sid_to_add: int
    skip_overlapping_shifts: bool
    def __init__(self, datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., schedule_selector: _Optional[_Union[_wfm_pb2.ScheduleSelector, _Mapping]] = ..., node_selector: _Optional[_Union[ParentEntity, _Mapping]] = ..., wfm_agent_sid_to_remove: _Optional[int] = ..., wfm_agent_sid_to_add: _Optional[int] = ..., skip_overlapping_shifts: bool = ...) -> None: ...

class ReplaceAgentOnScheduleRes(_message.Message):
    __slots__ = ("updated_shift_instances", "diagnostics")
    UPDATED_SHIFT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    updated_shift_instances: _containers.RepeatedCompositeFieldContainer[ShiftInstance]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, updated_shift_instances: _Optional[_Iterable[_Union[ShiftInstance, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class RgbaColor(_message.Message):
    __slots__ = ("red", "green", "blue", "alpha", "name")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    red: float
    green: float
    blue: float
    alpha: float
    name: str
    def __init__(self, red: _Optional[float] = ..., green: _Optional[float] = ..., blue: _Optional[float] = ..., alpha: _Optional[float] = ..., name: _Optional[str] = ...) -> None: ...

class HelloWorldWFMAdherenceRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HelloWorldWFMAdherenceResponse(_message.Message):
    __slots__ = ("hello_message",)
    HELLO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    hello_message: str
    def __init__(self, hello_message: _Optional[str] = ...) -> None: ...

class ListAgentStatesForDayRequest(_message.Message):
    __slots__ = ("start_datetime", "end_datetime")
    START_DATETIME_FIELD_NUMBER: _ClassVar[int]
    END_DATETIME_FIELD_NUMBER: _ClassVar[int]
    start_datetime: _timestamp_pb2.Timestamp
    end_datetime: _timestamp_pb2.Timestamp
    def __init__(self, start_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAgentStatesForDayResponse(_message.Message):
    __slots__ = ("agent_states",)
    AGENT_STATES_FIELD_NUMBER: _ClassVar[int]
    agent_states: _containers.RepeatedCompositeFieldContainer[_wfm_pb2.AgentStateSequence]
    def __init__(self, agent_states: _Optional[_Iterable[_Union[_wfm_pb2.AgentStateSequence, _Mapping]]] = ...) -> None: ...

class ListRealTimeManagementStatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRealTimeManagementStatesResponse(_message.Message):
    __slots__ = ("states",)
    STATES_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedScalarFieldContainer[_wfm_pb2.RealTimeManagementState]
    def __init__(self, states: _Optional[_Iterable[_Union[_wfm_pb2.RealTimeManagementState, str]]] = ...) -> None: ...

class RealTimeManagementStateColor(_message.Message):
    __slots__ = ("state", "color")
    STATE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    state: _wfm_pb2.RealTimeManagementState
    color: RgbaColor
    def __init__(self, state: _Optional[_Union[_wfm_pb2.RealTimeManagementState, str]] = ..., color: _Optional[_Union[RgbaColor, _Mapping]] = ...) -> None: ...

class UpsertRealTimeManagementStateColorRequest(_message.Message):
    __slots__ = ("state", "rgba_color_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    RGBA_COLOR_ID_FIELD_NUMBER: _ClassVar[int]
    state: _wfm_pb2.RealTimeManagementState
    rgba_color_id: int
    def __init__(self, state: _Optional[_Union[_wfm_pb2.RealTimeManagementState, str]] = ..., rgba_color_id: _Optional[int] = ...) -> None: ...

class UpsertRealTimeManagementStateColorResponse(_message.Message):
    __slots__ = ("state_color",)
    STATE_COLOR_FIELD_NUMBER: _ClassVar[int]
    state_color: RealTimeManagementStateColor
    def __init__(self, state_color: _Optional[_Union[RealTimeManagementStateColor, _Mapping]] = ...) -> None: ...

class ListRealTimeManagementStateColorsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRealTimeManagementStateColorsResponse(_message.Message):
    __slots__ = ("state_colors",)
    STATE_COLORS_FIELD_NUMBER: _ClassVar[int]
    state_colors: _containers.RepeatedCompositeFieldContainer[RealTimeManagementStateColor]
    def __init__(self, state_colors: _Optional[_Iterable[_Union[RealTimeManagementStateColor, _Mapping]]] = ...) -> None: ...

class DeleteRealTimeManagementStateColorRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _wfm_pb2.RealTimeManagementState
    def __init__(self, state: _Optional[_Union[_wfm_pb2.RealTimeManagementState, str]] = ...) -> None: ...

class DeleteRealTimeManagementStateColorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateAgentLeavePetitionRequest(_message.Message):
    __slots__ = ("requested_datetime_ranges", "petition_comment", "wfm_agent_sid", "requested_hours_off")
    REQUESTED_DATETIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    PETITION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    WFM_AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_HOURS_OFF_FIELD_NUMBER: _ClassVar[int]
    requested_datetime_ranges: _containers.RepeatedCompositeFieldContainer[_wfm_pb2.DatetimeRange]
    petition_comment: str
    wfm_agent_sid: int
    requested_hours_off: float
    def __init__(self, requested_datetime_ranges: _Optional[_Iterable[_Union[_wfm_pb2.DatetimeRange, _Mapping]]] = ..., petition_comment: _Optional[str] = ..., wfm_agent_sid: _Optional[int] = ..., requested_hours_off: _Optional[float] = ...) -> None: ...

class CreateAgentLeavePetitionResponse(_message.Message):
    __slots__ = ("agent_leave_petition",)
    AGENT_LEAVE_PETITION_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition: _wfm_pb2.AgentLeavePetition
    def __init__(self, agent_leave_petition: _Optional[_Union[_wfm_pb2.AgentLeavePetition, _Mapping]] = ...) -> None: ...

class ListAgentLeavePetitionsRequest(_message.Message):
    __slots__ = ("wfm_agent_sids", "datetime_range", "include_archived")
    WFM_AGENT_SIDS_FIELD_NUMBER: _ClassVar[int]
    DATETIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    wfm_agent_sids: _containers.RepeatedScalarFieldContainer[int]
    datetime_range: _wfm_pb2.DatetimeRange
    include_archived: bool
    def __init__(self, wfm_agent_sids: _Optional[_Iterable[int]] = ..., datetime_range: _Optional[_Union[_wfm_pb2.DatetimeRange, _Mapping]] = ..., include_archived: bool = ...) -> None: ...

class ListAgentLeavePetitionsResponse(_message.Message):
    __slots__ = ("agent_leave_petitions",)
    AGENT_LEAVE_PETITIONS_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petitions: _containers.RepeatedCompositeFieldContainer[_wfm_pb2.AgentLeavePetition]
    def __init__(self, agent_leave_petitions: _Optional[_Iterable[_Union[_wfm_pb2.AgentLeavePetition, _Mapping]]] = ...) -> None: ...

class ArchiveAgentLeavePetitionRequest(_message.Message):
    __slots__ = ("agent_leave_petition_id",)
    AGENT_LEAVE_PETITION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition_id: int
    def __init__(self, agent_leave_petition_id: _Optional[int] = ...) -> None: ...

class ArchiveAgentLeavePetitionResponse(_message.Message):
    __slots__ = ("agent_leave_petition",)
    AGENT_LEAVE_PETITION_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition: _wfm_pb2.AgentLeavePetition
    def __init__(self, agent_leave_petition: _Optional[_Union[_wfm_pb2.AgentLeavePetition, _Mapping]] = ...) -> None: ...

class ResolveAgentLeavePetitionRequest(_message.Message):
    __slots__ = ("agent_leave_petition_id", "petition_status", "response_comment", "retain_partial_shifts", "replace_with_unassigned_agent")
    AGENT_LEAVE_PETITION_ID_FIELD_NUMBER: _ClassVar[int]
    PETITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    RETAIN_PARTIAL_SHIFTS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_WITH_UNASSIGNED_AGENT_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition_id: int
    petition_status: _wfm_pb2.AgentLeavePetitionStatus
    response_comment: str
    retain_partial_shifts: bool
    replace_with_unassigned_agent: bool
    def __init__(self, agent_leave_petition_id: _Optional[int] = ..., petition_status: _Optional[_Union[_wfm_pb2.AgentLeavePetitionStatus, str]] = ..., response_comment: _Optional[str] = ..., retain_partial_shifts: bool = ..., replace_with_unassigned_agent: bool = ...) -> None: ...

class ResolveAgentLeavePetitionResponse(_message.Message):
    __slots__ = ("agent_leave_petition",)
    AGENT_LEAVE_PETITION_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition: _wfm_pb2.AgentLeavePetition
    def __init__(self, agent_leave_petition: _Optional[_Union[_wfm_pb2.AgentLeavePetition, _Mapping]] = ...) -> None: ...

class CancelAgentLeavePetitionRequest(_message.Message):
    __slots__ = ("agent_leave_petition_id",)
    AGENT_LEAVE_PETITION_ID_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition_id: int
    def __init__(self, agent_leave_petition_id: _Optional[int] = ...) -> None: ...

class CancelAgentLeavePetitionResponse(_message.Message):
    __slots__ = ("agent_leave_petition",)
    AGENT_LEAVE_PETITION_FIELD_NUMBER: _ClassVar[int]
    agent_leave_petition: _wfm_pb2.AgentLeavePetition
    def __init__(self, agent_leave_petition: _Optional[_Union[_wfm_pb2.AgentLeavePetition, _Mapping]] = ...) -> None: ...

class CreateRgbaColorRequest(_message.Message):
    __slots__ = ("color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    color: RgbaColor
    def __init__(self, color: _Optional[_Union[RgbaColor, _Mapping]] = ...) -> None: ...

class CreateRgbaColorResponse(_message.Message):
    __slots__ = ("rgba_color_id",)
    RGBA_COLOR_ID_FIELD_NUMBER: _ClassVar[int]
    rgba_color_id: int
    def __init__(self, rgba_color_id: _Optional[int] = ...) -> None: ...

class ListRgbaColorsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRgbaColorsResponse(_message.Message):
    __slots__ = ("colors",)
    COLORS_FIELD_NUMBER: _ClassVar[int]
    colors: _containers.RepeatedCompositeFieldContainer[RgbaColor]
    def __init__(self, colors: _Optional[_Iterable[_Union[RgbaColor, _Mapping]]] = ...) -> None: ...

class UpdateRgbaColorRequest(_message.Message):
    __slots__ = ("color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    color: RgbaColor
    def __init__(self, color: _Optional[_Union[RgbaColor, _Mapping]] = ...) -> None: ...

class UpdateRgbaColorResponse(_message.Message):
    __slots__ = ("color",)
    COLOR_FIELD_NUMBER: _ClassVar[int]
    color: RgbaColor
    def __init__(self, color: _Optional[_Union[RgbaColor, _Mapping]] = ...) -> None: ...

class DeleteRgbaColorRequest(_message.Message):
    __slots__ = ("rgba_color_id",)
    RGBA_COLOR_ID_FIELD_NUMBER: _ClassVar[int]
    rgba_color_id: int
    def __init__(self, rgba_color_id: _Optional[int] = ...) -> None: ...

class DeleteRgbaColorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
