from api.commons import communication_pb2 as _communication_pb2
from api.commons import enums_pb2 as _enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verb(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    V_UNKNOWN: _ClassVar[Verb]
    V_ALLOW: _ClassVar[Verb]
    V_DENY: _ClassVar[Verb]
    V_SCRUB: _ClassVar[Verb]
    V_OVERRIDE: _ClassVar[Verb]

class Entity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    E_UNKNOWN: _ClassVar[Entity]
    E_CALL: _ClassVar[Entity]
    E_EMAIL: _ClassVar[Entity]
    E_SMS: _ClassVar[Entity]

class SubEntity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SE_ALL: _ClassVar[SubEntity]
    SE_INBOUND: _ClassVar[SubEntity]
    SE_OUTBOUND: _ClassVar[SubEntity]
    SE_MANUAL: _ClassVar[SubEntity]
    SE_PREVIEW: _ClassVar[SubEntity]
    SE_MAC: _ClassVar[SubEntity]
    SE_BROADCAST: _ClassVar[SubEntity]

class PhoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CELL: _ClassVar[PhoneType]
    LAND: _ClassVar[PhoneType]
    TOLL_FREE: _ClassVar[PhoneType]

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CT_PHONE_NUMBER: _ClassVar[ContentType]
    CT_EMAIL: _ClassVar[ContentType]
    CT_SMS: _ClassVar[ContentType]
    CT_OTHER: _ClassVar[ContentType]
    CT_ACCOUNT_NUMBER: _ClassVar[ContentType]

class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CHANNEL_CALL: _ClassVar[Channel]
    CHANNEL_EMAIL: _ClassVar[Channel]
    CHANNEL_SMS: _ClassVar[Channel]

class PluginType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_PLUGIN: _ClassVar[PluginType]
    GRYPHON: _ClassVar[PluginType]
    TCN_CONSENT: _ClassVar[PluginType]
    RND: _ClassVar[PluginType]

class Environment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INVALID_ENV: _ClassVar[Environment]
    TEST: _ClassVar[Environment]
    PRODUCTION: _ClassVar[Environment]

class ConsentAbsentAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONSENT_ABSENT_ACTION_ALLOW: _ClassVar[ConsentAbsentAction]
    CONSENT_ABSENT_ACTION_DENY: _ClassVar[ConsentAbsentAction]
V_UNKNOWN: Verb
V_ALLOW: Verb
V_DENY: Verb
V_SCRUB: Verb
V_OVERRIDE: Verb
E_UNKNOWN: Entity
E_CALL: Entity
E_EMAIL: Entity
E_SMS: Entity
SE_ALL: SubEntity
SE_INBOUND: SubEntity
SE_OUTBOUND: SubEntity
SE_MANUAL: SubEntity
SE_PREVIEW: SubEntity
SE_MAC: SubEntity
SE_BROADCAST: SubEntity
CELL: PhoneType
LAND: PhoneType
TOLL_FREE: PhoneType
CT_PHONE_NUMBER: ContentType
CT_EMAIL: ContentType
CT_SMS: ContentType
CT_OTHER: ContentType
CT_ACCOUNT_NUMBER: ContentType
CHANNEL_CALL: Channel
CHANNEL_EMAIL: Channel
CHANNEL_SMS: Channel
UNKNOWN_PLUGIN: PluginType
GRYPHON: PluginType
TCN_CONSENT: PluginType
RND: PluginType
INVALID_ENV: Environment
TEST: Environment
PRODUCTION: Environment
CONSENT_ABSENT_ACTION_ALLOW: ConsentAbsentAction
CONSENT_ABSENT_ACTION_DENY: ConsentAbsentAction

class Rule(_message.Message):
    __slots__ = ["verb", "entity", "sub_entity", "selectors", "rule_text"]
    VERB_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    SUB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SELECTORS_FIELD_NUMBER: _ClassVar[int]
    RULE_TEXT_FIELD_NUMBER: _ClassVar[int]
    verb: Verb
    entity: Entity
    sub_entity: SubEntity
    selectors: _containers.RepeatedCompositeFieldContainer[Selector]
    rule_text: str
    def __init__(self, verb: _Optional[_Union[Verb, str]] = ..., entity: _Optional[_Union[Entity, str]] = ..., sub_entity: _Optional[_Union[SubEntity, str]] = ..., selectors: _Optional[_Iterable[_Union[Selector, _Mapping]]] = ..., rule_text: _Optional[str] = ...) -> None: ...

class Selector(_message.Message):
    __slots__ = ["time", "week", "dncl", "frequency", "location", "phone_type", "month", "date", "holiday", "meta", "plugin"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    DNCL_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PHONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    HOLIDAY_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    time: TimeExp
    week: WeekdayExp
    dncl: DnclExp
    frequency: FrequencyExp
    location: LocationExp
    phone_type: PhoneTypeExp
    month: MonthExp
    date: DateExp
    holiday: HolidayExp
    meta: MetaFieldExp
    plugin: PluginExp
    def __init__(self, time: _Optional[_Union[TimeExp, _Mapping]] = ..., week: _Optional[_Union[WeekdayExp, _Mapping]] = ..., dncl: _Optional[_Union[DnclExp, _Mapping]] = ..., frequency: _Optional[_Union[FrequencyExp, _Mapping]] = ..., location: _Optional[_Union[LocationExp, _Mapping]] = ..., phone_type: _Optional[_Union[PhoneTypeExp, _Mapping]] = ..., month: _Optional[_Union[MonthExp, _Mapping]] = ..., date: _Optional[_Union[DateExp, _Mapping]] = ..., holiday: _Optional[_Union[HolidayExp, _Mapping]] = ..., meta: _Optional[_Union[MetaFieldExp, _Mapping]] = ..., plugin: _Optional[_Union[PluginExp, _Mapping]] = ...) -> None: ...

class TimeExp(_message.Message):
    __slots__ = ["start_hour", "end_hour"]
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    start_hour: str
    end_hour: str
    def __init__(self, start_hour: _Optional[str] = ..., end_hour: _Optional[str] = ...) -> None: ...

class WeekdayExp(_message.Message):
    __slots__ = ["day", "text"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Weekday.Enum
    text: str
    def __init__(self, day: _Optional[_Union[_enums_pb2.Weekday.Enum, str]] = ..., text: _Optional[str] = ...) -> None: ...

class DnclExp(_message.Message):
    __slots__ = ["list_name", "field_names"]
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    list_name: str
    field_names: FieldNamesMod
    def __init__(self, list_name: _Optional[str] = ..., field_names: _Optional[_Union[FieldNamesMod, _Mapping]] = ...) -> None: ...

class FrequencyExp(_message.Message):
    __slots__ = ["count", "duration", "results", "dispositions", "field_names", "checking_entities", "matching"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    CHECKING_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    MATCHING_FIELD_NUMBER: _ClassVar[int]
    count: int
    duration: int
    results: ResultsMod
    dispositions: DispositionMod
    field_names: FieldNamesMod
    checking_entities: _containers.RepeatedCompositeFieldContainer[EntityExp]
    matching: MatchingMod
    def __init__(self, count: _Optional[int] = ..., duration: _Optional[int] = ..., results: _Optional[_Union[ResultsMod, _Mapping]] = ..., dispositions: _Optional[_Union[DispositionMod, _Mapping]] = ..., field_names: _Optional[_Union[FieldNamesMod, _Mapping]] = ..., checking_entities: _Optional[_Iterable[_Union[EntityExp, _Mapping]]] = ..., matching: _Optional[_Union[MatchingMod, _Mapping]] = ...) -> None: ...

class MatchingMod(_message.Message):
    __slots__ = ["mod"]
    AND_FIELD_NUMBER: _ClassVar[int]
    OR_FIELD_NUMBER: _ClassVar[int]
    MOD_FIELD_NUMBER: _ClassVar[int]
    mod: MatchingEntity
    def __init__(self, mod: _Optional[_Union[MatchingEntity, _Mapping]] = ..., **kwargs) -> None: ...

class MatchingEntity(_message.Message):
    __slots__ = ["results", "dispositions"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    results: ResultsMod
    dispositions: DispositionMod
    def __init__(self, results: _Optional[_Union[ResultsMod, _Mapping]] = ..., dispositions: _Optional[_Union[DispositionMod, _Mapping]] = ...) -> None: ...

class LocationExp(_message.Message):
    __slots__ = ["country", "state", "county", "city", "province", "postal_codes", "area_codes"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODES_FIELD_NUMBER: _ClassVar[int]
    AREA_CODES_FIELD_NUMBER: _ClassVar[int]
    country: str
    state: str
    county: str
    city: str
    province: str
    postal_codes: _containers.RepeatedScalarFieldContainer[str]
    area_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, country: _Optional[str] = ..., state: _Optional[str] = ..., county: _Optional[str] = ..., city: _Optional[str] = ..., province: _Optional[str] = ..., postal_codes: _Optional[_Iterable[str]] = ..., area_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class PhoneTypeExp(_message.Message):
    __slots__ = ["phone_type"]
    PHONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    phone_type: PhoneType
    def __init__(self, phone_type: _Optional[_Union[PhoneType, str]] = ...) -> None: ...

class MonthExp(_message.Message):
    __slots__ = ["month", "text"]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    month: _enums_pb2.Month
    text: str
    def __init__(self, month: _Optional[_Union[_enums_pb2.Month, str]] = ..., text: _Optional[str] = ...) -> None: ...

class DateExp(_message.Message):
    __slots__ = ["month", "day", "year"]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    month: _enums_pb2.Month
    day: int
    year: int
    def __init__(self, month: _Optional[_Union[_enums_pb2.Month, str]] = ..., day: _Optional[int] = ..., year: _Optional[int] = ...) -> None: ...

class HolidayExp(_message.Message):
    __slots__ = ["name", "country", "type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    country: str
    type: str
    def __init__(self, name: _Optional[str] = ..., country: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class MetaFieldExp(_message.Message):
    __slots__ = ["field"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: str
    def __init__(self, field: _Optional[str] = ...) -> None: ...

class PluginExp(_message.Message):
    __slots__ = ["type", "tcn_strict", "license_id", "reference_key", "from_number", "env", "profile_name", "content_field", "topic", "absent_action", "date_last_contact"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TCN_STRICT_FIELD_NUMBER: _ClassVar[int]
    LICENSE_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_KEY_FIELD_NUMBER: _ClassVar[int]
    FROM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    ABSENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    DATE_LAST_CONTACT_FIELD_NUMBER: _ClassVar[int]
    type: PluginType
    tcn_strict: bool
    license_id: str
    reference_key: str
    from_number: str
    env: Environment
    profile_name: str
    content_field: str
    topic: str
    absent_action: ConsentAbsentAction
    date_last_contact: str
    def __init__(self, type: _Optional[_Union[PluginType, str]] = ..., tcn_strict: bool = ..., license_id: _Optional[str] = ..., reference_key: _Optional[str] = ..., from_number: _Optional[str] = ..., env: _Optional[_Union[Environment, str]] = ..., profile_name: _Optional[str] = ..., content_field: _Optional[str] = ..., topic: _Optional[str] = ..., absent_action: _Optional[_Union[ConsentAbsentAction, str]] = ..., date_last_contact: _Optional[str] = ...) -> None: ...

class EntityExp(_message.Message):
    __slots__ = ["sub_entity", "entity"]
    SUB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    sub_entity: SubEntity
    entity: Entity
    def __init__(self, sub_entity: _Optional[_Union[SubEntity, str]] = ..., entity: _Optional[_Union[Entity, str]] = ...) -> None: ...

class FieldNamesMod(_message.Message):
    __slots__ = ["field_names"]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    field_names: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, field_names: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class ResultsMod(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, results: _Optional[_Iterable[str]] = ...) -> None: ...

class DispositionMod(_message.Message):
    __slots__ = ["dispositions"]
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    dispositions: _containers.RepeatedCompositeFieldContainer[DispositionField]
    def __init__(self, dispositions: _Optional[_Iterable[_Union[DispositionField, _Mapping]]] = ...) -> None: ...

class DispositionField(_message.Message):
    __slots__ = ["key", "value", "pairs"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    pairs: _containers.RepeatedCompositeFieldContainer[DispositionPair]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., pairs: _Optional[_Iterable[_Union[DispositionPair, _Mapping]]] = ...) -> None: ...

class DispositionPair(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ["Field", "Content"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    Field: str
    Content: str
    def __init__(self, Field: _Optional[str] = ..., Content: _Optional[str] = ...) -> None: ...

class ConsentCondition(_message.Message):
    __slots__ = ["consent_condition_id", "consent_id", "days_of_the_week", "time_of_day_from", "time_of_day_to", "from_date", "to_date"]
    CONSENT_CONDITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    TO_DATE_FIELD_NUMBER: _ClassVar[int]
    consent_condition_id: int
    consent_id: int
    days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    time_of_day_from: str
    time_of_day_to: str
    from_date: _timestamp_pb2.Timestamp
    to_date: _timestamp_pb2.Timestamp
    def __init__(self, consent_condition_id: _Optional[int] = ..., consent_id: _Optional[int] = ..., days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., time_of_day_from: _Optional[str] = ..., time_of_day_to: _Optional[str] = ..., from_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScenarioData(_message.Message):
    __slots__ = ["comm_type", "phone_number", "country_code", "email", "call_metadata", "time_of_call", "frequency_count", "frequency_duration", "dncl_blocks", "country", "state", "county", "city", "province", "phone_type", "time_zone", "holidays", "country_code_data"]
    class CallMetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CALL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_CALL_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_COUNT_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_DURATION_FIELD_NUMBER: _ClassVar[int]
    DNCL_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    PHONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_DATA_FIELD_NUMBER: _ClassVar[int]
    comm_type: _communication_pb2.CommType
    phone_number: str
    country_code: str
    email: str
    call_metadata: _containers.ScalarMap[str, str]
    time_of_call: _timestamp_pb2.Timestamp
    frequency_count: int
    frequency_duration: int
    dncl_blocks: bool
    country: str
    state: str
    county: str
    city: str
    province: str
    phone_type: PhoneType
    time_zone: str
    holidays: _containers.RepeatedScalarFieldContainer[str]
    country_code_data: CountryCode
    def __init__(self, comm_type: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., phone_number: _Optional[str] = ..., country_code: _Optional[str] = ..., email: _Optional[str] = ..., call_metadata: _Optional[_Mapping[str, str]] = ..., time_of_call: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., frequency_count: _Optional[int] = ..., frequency_duration: _Optional[int] = ..., dncl_blocks: bool = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., county: _Optional[str] = ..., city: _Optional[str] = ..., province: _Optional[str] = ..., phone_type: _Optional[_Union[PhoneType, str]] = ..., time_zone: _Optional[str] = ..., holidays: _Optional[_Iterable[str]] = ..., country_code_data: _Optional[_Union[CountryCode, _Mapping]] = ...) -> None: ...

class CountryCode(_message.Message):
    __slots__ = ["country_code", "country_name", "country_id"]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    country_code: int
    country_name: str
    country_id: str
    def __init__(self, country_code: _Optional[int] = ..., country_name: _Optional[str] = ..., country_id: _Optional[str] = ...) -> None: ...

class ScenarioResult(_message.Message):
    __slots__ = ["passed_value", "should_allow_responses", "should_deny_responses", "scenario_name"]
    PASSED_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ALLOW_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DENY_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    passed_value: bool
    should_allow_responses: _containers.RepeatedCompositeFieldContainer[ScenarioRuleResponse]
    should_deny_responses: _containers.RepeatedCompositeFieldContainer[ScenarioRuleResponse]
    scenario_name: str
    def __init__(self, passed_value: bool = ..., should_allow_responses: _Optional[_Iterable[_Union[ScenarioRuleResponse, _Mapping]]] = ..., should_deny_responses: _Optional[_Iterable[_Union[ScenarioRuleResponse, _Mapping]]] = ..., scenario_name: _Optional[str] = ...) -> None: ...

class ScenarioRuleResponse(_message.Message):
    __slots__ = ["rule_text", "permit_value"]
    RULE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    rule_text: str
    permit_value: bool
    def __init__(self, rule_text: _Optional[str] = ..., permit_value: bool = ...) -> None: ...

class ScrubEntryDetails(_message.Message):
    __slots__ = ["content", "expiration_date", "notes"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    content: str
    expiration_date: _timestamp_pb2.Timestamp
    notes: _wrappers_pb2.StringValue
    def __init__(self, content: _Optional[str] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RuleResponse(_message.Message):
    __slots__ = ["rule_text", "permit", "plugin_response"]
    RULE_TEXT_FIELD_NUMBER: _ClassVar[int]
    PERMIT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    rule_text: str
    permit: bool
    plugin_response: str
    def __init__(self, rule_text: _Optional[str] = ..., permit: bool = ..., plugin_response: _Optional[str] = ...) -> None: ...
