from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CronType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CRON_TYPE_LMS: _ClassVar[CronType]
    CRON_TYPE_JOURNEY: _ClassVar[CronType]

class EnrichmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ENRICHMENT_TYPE_OR: _ClassVar[EnrichmentType]
    ENRICHMENT_TYPE_XOR: _ClassVar[EnrichmentType]
    ENRICHMENT_TYPE_AND: _ClassVar[EnrichmentType]
    ENRICHMENT_TYPE_JOIN: _ClassVar[EnrichmentType]
    ENRICHMENT_TYPE_NOT: _ClassVar[EnrichmentType]

class PrimarySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PRIMARY_SOURCE_LMS: _ClassVar[PrimarySource]
    PRIMARY_SOURCE_CJS: _ClassVar[PrimarySource]

class DedupKeyPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    KEEP_FIRST: _ClassVar[DedupKeyPolicy]
    KEEP_LAST: _ClassVar[DedupKeyPolicy]
    KEEP_ALL: _ClassVar[DedupKeyPolicy]

class RunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RUN_TYPE_ENABLED: _ClassVar[RunType]
    RUN_TYPE_DISABLED: _ClassVar[RunType]
    RUN_TYPE_TEST: _ClassVar[RunType]

class ConsentActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONSENT_ACTION_TYPE_ADD: _ClassVar[ConsentActionType]
    CONSENT_ACTION_TYPE_REVOKE: _ClassVar[ConsentActionType]

class RecordType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RECORD_TYPE_ALL: _ClassVar[RecordType]
    RECORD_TYPE_STRING: _ClassVar[RecordType]
    RECORD_TYPE_NUMBER: _ClassVar[RecordType]
    RECORD_TYPE_BOOL: _ClassVar[RecordType]
    RECORD_TYPE_PHONE: _ClassVar[RecordType]
    RECORD_TYPE_CURRENCY: _ClassVar[RecordType]
    RECORD_TYPE_ENRICHED_PHONE: _ClassVar[RecordType]
    RECORD_TYPE_ENRICHED_ZIP: _ClassVar[RecordType]
    RECORD_TYPE_POSTAL_CODE: _ClassVar[RecordType]
    RECORD_TYPE_EMAIL: _ClassVar[RecordType]
    RECORD_TYPE_DATETIME_NOW: _ClassVar[RecordType]
    RECORD_TYPE_DATETIME_TIMESTAMP: _ClassVar[RecordType]
    RECORD_TYPE_DATETIME_DATE: _ClassVar[RecordType]
    RECORD_TYPE_DATETIME_MONTH_AND_DAY: _ClassVar[RecordType]
    RECORD_TYPE_DATETIME_TIME_OF_DAY: _ClassVar[RecordType]
    RECORD_TYPE_REPEATED_RECORDS: _ClassVar[RecordType]
    RECORD_TYPE_RECORD_MAP: _ClassVar[RecordType]
    RECORD_TYPE_ERROR: _ClassVar[RecordType]
    RECORD_TYPE_SOCIAL: _ClassVar[RecordType]
    RECORD_TYPE_DATE_OF_BIRTH: _ClassVar[RecordType]
    RECORD_TYPE_FULL_NAME: _ClassVar[RecordType]
    RECORD_TYPE_ACCOUNT_NUMBER: _ClassVar[RecordType]
    RECORD_TYPE_STRUCT_VALUE: _ClassVar[RecordType]
    RECORD_TYPE_EHR_DETAILS: _ClassVar[RecordType]

class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FIELD_TYPE_STRING: _ClassVar[FieldType]
    FIELD_TYPE_NUMBER: _ClassVar[FieldType]
    FIELD_TYPE_BOOLEAN: _ClassVar[FieldType]
    FIELD_TYPE_PHONE: _ClassVar[FieldType]
    FIELD_TYPE_CURRENCY: _ClassVar[FieldType]
    FIELD_TYPE_EMAIL: _ClassVar[FieldType]
    FIELD_TYPE_DATETIME_NOW: _ClassVar[FieldType]
    FIELD_TYPE_DATETIME_TIMESTAMP: _ClassVar[FieldType]
    FIELD_TYPE_DATETIME_DATE: _ClassVar[FieldType]
    FIELD_TYPE_DATETIME_MONTH_AND_DAY: _ClassVar[FieldType]
    FIELD_TYPE_DATETIME_TIME_OF_DAY: _ClassVar[FieldType]
    FIELD_TYPE_POSTAL_CODE: _ClassVar[FieldType]
    FIELD_TYPE_ENRICHED_PHONE: _ClassVar[FieldType]
    FIELD_TYPE_ENRICHED_ZIP: _ClassVar[FieldType]
    FIELD_TYPE_SOCIAL: _ClassVar[FieldType]
    FIELD_TYPE_DATE_OF_BIRTH: _ClassVar[FieldType]
    FIELD_TYPE_FULL_NAME: _ClassVar[FieldType]
    FIELD_TYPE_ACCOUNT_NUMBER: _ClassVar[FieldType]
    FIELD_TYPE_ERROR: _ClassVar[FieldType]
    FIELD_TYPE_STRUCT_VALUE: _ClassVar[FieldType]
    FIELD_TYPE_EHR_DETAILS: _ClassVar[FieldType]

class FileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FILE_FORMAT_CSV: _ClassVar[FileFormat]
    FILE_FORMAT_CUSTOM_DELIM: _ClassVar[FileFormat]
    FILE_FORMAT_FIXED_FORMAT: _ClassVar[FileFormat]
    FILE_FORMAT_TAB: _ClassVar[FileFormat]
    FILE_FORMAT_JSON: _ClassVar[FileFormat]

class PipelineElementStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PIPELINE_ELEMENT_STATUS_TYPE_INITIALIZED: _ClassVar[PipelineElementStatusType]
    PIPELINE_ELEMENT_STATUS_TYPE_RUNNING: _ClassVar[PipelineElementStatusType]
    PIPELINE_ELEMENT_STATUS_TYPE_STOPPED: _ClassVar[PipelineElementStatusType]
    PIPELINE_ELEMENT_STATUS_TYPE_FAILED: _ClassVar[PipelineElementStatusType]

class EntrypointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ENTRYPOINT_TYPE_NON: _ClassVar[EntrypointType]
    ENTRYPOINT_TYPE_API: _ClassVar[EntrypointType]
    ENTRYPOINT_TYPE_SFTP: _ClassVar[EntrypointType]

class DuplicatePolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DUPLICATE_POLICY_TYPE_KEEP_RECORD_DISCARD_NUMBER: _ClassVar[DuplicatePolicyType]
    DUPLICATE_POLICY_TYPE_ALLOW_RECORD_KEEP_NUMBER: _ClassVar[DuplicatePolicyType]
    DUPLICATE_POLICY_TYPE_DISCARD_RECORD: _ClassVar[DuplicatePolicyType]
    DUPLICATE_POLICY_TYPE_DUPLICATE_LIST: _ClassVar[DuplicatePolicyType]

class AbsentPolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ABSENT_POLICY_TYPE_KEEP: _ClassVar[AbsentPolicyType]
    ABSENT_POLICY_TYPE_DISCARD: _ClassVar[AbsentPolicyType]

class DialOrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DIAL_ORDER_TYPE_FIRST: _ClassVar[DialOrderType]
    DIAL_ORDER_TYPE_NATURAL: _ClassVar[DialOrderType]
    DIAL_ORDER_TYPE_CUSTOM: _ClassVar[DialOrderType]

class ExportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EXPORT_TYPE_FILENAME: _ClassVar[ExportType]
    EXPORT_TYPE_SFTP: _ClassVar[ExportType]

class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SORT_ORDER_ASCENDING: _ClassVar[SortOrder]
    SORT_ORDER_DESCENDING: _ClassVar[SortOrder]

class CompareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPARE_TYPE_STRING: _ClassVar[CompareType]
    COMPARE_TYPE_NUMBER: _ClassVar[CompareType]
    COMPARE_TYPE_BOOL: _ClassVar[CompareType]

class CompareOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPARE_OPERATOR_EQUAL_TO: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_GREATER: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_GREATER_EQUAL: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_LESS: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_LESS_EQUAL: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_STARTS_WITH: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_ENDS_WITH: _ClassVar[CompareOperator]
    COMPARE_OPERATOR_CONTAINS: _ClassVar[CompareOperator]

class ChainOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CHAIN_OPERATOR_AND: _ClassVar[ChainOperator]
    CHAIN_OPERATOR_OR: _ClassVar[ChainOperator]

class DeDupActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DE_DUP_ACTIONS_KEEP_FIRST: _ClassVar[DeDupActions]
    DE_DUP_ACTIONS_KEEP_BOTH: _ClassVar[DeDupActions]
    DE_DUP_ACTIONS_KEEP_LAST: _ClassVar[DeDupActions]
    DE_DUP_ACTIONS_KEEP_NEITHER: _ClassVar[DeDupActions]

class DatePosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATE_POSITION_FIRST: _ClassVar[DatePosition]
    DATE_POSITION_BEFORE_FILENAME: _ClassVar[DatePosition]
    DATE_POSITION_AFTER_FILENAME: _ClassVar[DatePosition]
    DATE_POSITION_LAST: _ClassVar[DatePosition]

class RelativeDay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RELATIVE_DAY_TODAY: _ClassVar[RelativeDay]
    RELATIVE_DAY_YESTERDAY: _ClassVar[RelativeDay]
    RELATIVE_DAY_LAST_FRIDAY: _ClassVar[RelativeDay]

class FilePatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FILE_PATTERN_TYPE_GLOB: _ClassVar[FilePatternType]
    FILE_PATTERN_TYPE_CONSTRUCTED: _ClassVar[FilePatternType]
    FILE_PATTERN_TYPE_ORIGINAL: _ClassVar[FilePatternType]

class DateTimePrecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATETIME_PRECISION_NOW: _ClassVar[DateTimePrecision]
    DATETIME_PRECISION_TIMESTAMP: _ClassVar[DateTimePrecision]
    DATETIME_PRECISION_DATE: _ClassVar[DateTimePrecision]
    DATETIME_PRECISION_MONTH_AND_DAY: _ClassVar[DateTimePrecision]
    DATETIME_PRECISION_TIME_OF_DAY: _ClassVar[DateTimePrecision]

class HttpVerb(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    HTTP_VERB_GET: _ClassVar[HttpVerb]
    HTTP_VERB_POST: _ClassVar[HttpVerb]

class ComplianceListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPLIANCE_LIST_TYPE_SCRUB: _ClassVar[ComplianceListType]
    COMPLIANCE_LIST_TYPE_CONSENT: _ClassVar[ComplianceListType]

class EventState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EVENT_STATE_NONE: _ClassVar[EventState]
    EVENT_STATE_KICKOFF: _ClassVar[EventState]
    EVENT_STATE_CHECK: _ClassVar[EventState]
    EVENT_STATE_PROCESS: _ClassVar[EventState]
    EVENT_STATE_CLEANUP: _ClassVar[EventState]

class TimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT: _ClassVar[TimeUnit]
    TIME_WEEKS: _ClassVar[TimeUnit]
    TIME_DAYS: _ClassVar[TimeUnit]
    TIME_HOURS: _ClassVar[TimeUnit]
CRON_TYPE_LMS: CronType
CRON_TYPE_JOURNEY: CronType
ENRICHMENT_TYPE_OR: EnrichmentType
ENRICHMENT_TYPE_XOR: EnrichmentType
ENRICHMENT_TYPE_AND: EnrichmentType
ENRICHMENT_TYPE_JOIN: EnrichmentType
ENRICHMENT_TYPE_NOT: EnrichmentType
PRIMARY_SOURCE_LMS: PrimarySource
PRIMARY_SOURCE_CJS: PrimarySource
KEEP_FIRST: DedupKeyPolicy
KEEP_LAST: DedupKeyPolicy
KEEP_ALL: DedupKeyPolicy
RUN_TYPE_ENABLED: RunType
RUN_TYPE_DISABLED: RunType
RUN_TYPE_TEST: RunType
CONSENT_ACTION_TYPE_ADD: ConsentActionType
CONSENT_ACTION_TYPE_REVOKE: ConsentActionType
RECORD_TYPE_ALL: RecordType
RECORD_TYPE_STRING: RecordType
RECORD_TYPE_NUMBER: RecordType
RECORD_TYPE_BOOL: RecordType
RECORD_TYPE_PHONE: RecordType
RECORD_TYPE_CURRENCY: RecordType
RECORD_TYPE_ENRICHED_PHONE: RecordType
RECORD_TYPE_ENRICHED_ZIP: RecordType
RECORD_TYPE_POSTAL_CODE: RecordType
RECORD_TYPE_EMAIL: RecordType
RECORD_TYPE_DATETIME_NOW: RecordType
RECORD_TYPE_DATETIME_TIMESTAMP: RecordType
RECORD_TYPE_DATETIME_DATE: RecordType
RECORD_TYPE_DATETIME_MONTH_AND_DAY: RecordType
RECORD_TYPE_DATETIME_TIME_OF_DAY: RecordType
RECORD_TYPE_REPEATED_RECORDS: RecordType
RECORD_TYPE_RECORD_MAP: RecordType
RECORD_TYPE_ERROR: RecordType
RECORD_TYPE_SOCIAL: RecordType
RECORD_TYPE_DATE_OF_BIRTH: RecordType
RECORD_TYPE_FULL_NAME: RecordType
RECORD_TYPE_ACCOUNT_NUMBER: RecordType
RECORD_TYPE_STRUCT_VALUE: RecordType
RECORD_TYPE_EHR_DETAILS: RecordType
FIELD_TYPE_STRING: FieldType
FIELD_TYPE_NUMBER: FieldType
FIELD_TYPE_BOOLEAN: FieldType
FIELD_TYPE_PHONE: FieldType
FIELD_TYPE_CURRENCY: FieldType
FIELD_TYPE_EMAIL: FieldType
FIELD_TYPE_DATETIME_NOW: FieldType
FIELD_TYPE_DATETIME_TIMESTAMP: FieldType
FIELD_TYPE_DATETIME_DATE: FieldType
FIELD_TYPE_DATETIME_MONTH_AND_DAY: FieldType
FIELD_TYPE_DATETIME_TIME_OF_DAY: FieldType
FIELD_TYPE_POSTAL_CODE: FieldType
FIELD_TYPE_ENRICHED_PHONE: FieldType
FIELD_TYPE_ENRICHED_ZIP: FieldType
FIELD_TYPE_SOCIAL: FieldType
FIELD_TYPE_DATE_OF_BIRTH: FieldType
FIELD_TYPE_FULL_NAME: FieldType
FIELD_TYPE_ACCOUNT_NUMBER: FieldType
FIELD_TYPE_ERROR: FieldType
FIELD_TYPE_STRUCT_VALUE: FieldType
FIELD_TYPE_EHR_DETAILS: FieldType
FILE_FORMAT_CSV: FileFormat
FILE_FORMAT_CUSTOM_DELIM: FileFormat
FILE_FORMAT_FIXED_FORMAT: FileFormat
FILE_FORMAT_TAB: FileFormat
FILE_FORMAT_JSON: FileFormat
PIPELINE_ELEMENT_STATUS_TYPE_INITIALIZED: PipelineElementStatusType
PIPELINE_ELEMENT_STATUS_TYPE_RUNNING: PipelineElementStatusType
PIPELINE_ELEMENT_STATUS_TYPE_STOPPED: PipelineElementStatusType
PIPELINE_ELEMENT_STATUS_TYPE_FAILED: PipelineElementStatusType
ENTRYPOINT_TYPE_NON: EntrypointType
ENTRYPOINT_TYPE_API: EntrypointType
ENTRYPOINT_TYPE_SFTP: EntrypointType
DUPLICATE_POLICY_TYPE_KEEP_RECORD_DISCARD_NUMBER: DuplicatePolicyType
DUPLICATE_POLICY_TYPE_ALLOW_RECORD_KEEP_NUMBER: DuplicatePolicyType
DUPLICATE_POLICY_TYPE_DISCARD_RECORD: DuplicatePolicyType
DUPLICATE_POLICY_TYPE_DUPLICATE_LIST: DuplicatePolicyType
ABSENT_POLICY_TYPE_KEEP: AbsentPolicyType
ABSENT_POLICY_TYPE_DISCARD: AbsentPolicyType
DIAL_ORDER_TYPE_FIRST: DialOrderType
DIAL_ORDER_TYPE_NATURAL: DialOrderType
DIAL_ORDER_TYPE_CUSTOM: DialOrderType
EXPORT_TYPE_FILENAME: ExportType
EXPORT_TYPE_SFTP: ExportType
SORT_ORDER_ASCENDING: SortOrder
SORT_ORDER_DESCENDING: SortOrder
COMPARE_TYPE_STRING: CompareType
COMPARE_TYPE_NUMBER: CompareType
COMPARE_TYPE_BOOL: CompareType
COMPARE_OPERATOR_EQUAL_TO: CompareOperator
COMPARE_OPERATOR_GREATER: CompareOperator
COMPARE_OPERATOR_GREATER_EQUAL: CompareOperator
COMPARE_OPERATOR_LESS: CompareOperator
COMPARE_OPERATOR_LESS_EQUAL: CompareOperator
COMPARE_OPERATOR_STARTS_WITH: CompareOperator
COMPARE_OPERATOR_ENDS_WITH: CompareOperator
COMPARE_OPERATOR_CONTAINS: CompareOperator
CHAIN_OPERATOR_AND: ChainOperator
CHAIN_OPERATOR_OR: ChainOperator
DE_DUP_ACTIONS_KEEP_FIRST: DeDupActions
DE_DUP_ACTIONS_KEEP_BOTH: DeDupActions
DE_DUP_ACTIONS_KEEP_LAST: DeDupActions
DE_DUP_ACTIONS_KEEP_NEITHER: DeDupActions
DATE_POSITION_FIRST: DatePosition
DATE_POSITION_BEFORE_FILENAME: DatePosition
DATE_POSITION_AFTER_FILENAME: DatePosition
DATE_POSITION_LAST: DatePosition
RELATIVE_DAY_TODAY: RelativeDay
RELATIVE_DAY_YESTERDAY: RelativeDay
RELATIVE_DAY_LAST_FRIDAY: RelativeDay
FILE_PATTERN_TYPE_GLOB: FilePatternType
FILE_PATTERN_TYPE_CONSTRUCTED: FilePatternType
FILE_PATTERN_TYPE_ORIGINAL: FilePatternType
DATETIME_PRECISION_NOW: DateTimePrecision
DATETIME_PRECISION_TIMESTAMP: DateTimePrecision
DATETIME_PRECISION_DATE: DateTimePrecision
DATETIME_PRECISION_MONTH_AND_DAY: DateTimePrecision
DATETIME_PRECISION_TIME_OF_DAY: DateTimePrecision
HTTP_VERB_GET: HttpVerb
HTTP_VERB_POST: HttpVerb
COMPLIANCE_LIST_TYPE_SCRUB: ComplianceListType
COMPLIANCE_LIST_TYPE_CONSENT: ComplianceListType
EVENT_STATE_NONE: EventState
EVENT_STATE_KICKOFF: EventState
EVENT_STATE_CHECK: EventState
EVENT_STATE_PROCESS: EventState
EVENT_STATE_CLEANUP: EventState
DEFAULT: TimeUnit
TIME_WEEKS: TimeUnit
TIME_DAYS: TimeUnit
TIME_HOURS: TimeUnit

class RecordField(_message.Message):
    __slots__ = ["name", "type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: RecordType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[RecordType, str]] = ...) -> None: ...

class FilePattern(_message.Message):
    __slots__ = ["type", "directory", "filename", "prefixes", "date_format", "suffix", "file_extension", "date_prefix", "day_to_use"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DATE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DAY_TO_USE_FIELD_NUMBER: _ClassVar[int]
    type: FilePatternType
    directory: str
    filename: str
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    date_format: str
    suffix: str
    file_extension: str
    date_prefix: bool
    day_to_use: RelativeDay
    def __init__(self, type: _Optional[_Union[FilePatternType, str]] = ..., directory: _Optional[str] = ..., filename: _Optional[str] = ..., prefixes: _Optional[_Iterable[str]] = ..., date_format: _Optional[str] = ..., suffix: _Optional[str] = ..., file_extension: _Optional[str] = ..., date_prefix: bool = ..., day_to_use: _Optional[_Union[RelativeDay, str]] = ...) -> None: ...

class ConstructedFilename(_message.Message):
    __slots__ = ["override_filename", "prefix", "date_format", "suffix", "file_extension", "date_position", "day_to_use"]
    OVERRIDE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    DATE_POSITION_FIELD_NUMBER: _ClassVar[int]
    DAY_TO_USE_FIELD_NUMBER: _ClassVar[int]
    override_filename: _wrappers_pb2.StringValue
    prefix: str
    date_format: str
    suffix: str
    file_extension: str
    date_position: DatePosition
    day_to_use: RelativeDay
    def __init__(self, override_filename: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., prefix: _Optional[str] = ..., date_format: _Optional[str] = ..., suffix: _Optional[str] = ..., file_extension: _Optional[str] = ..., date_position: _Optional[_Union[DatePosition, str]] = ..., day_to_use: _Optional[_Union[RelativeDay, str]] = ...) -> None: ...

class PaginationTerminator(_message.Message):
    __slots__ = ["key", "negate", "exists_check", "num_greater_than", "num_less_than", "num_equals", "count_less_than", "str_equals", "str_contains", "bool_equals"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    EXISTS_CHECK_FIELD_NUMBER: _ClassVar[int]
    NUM_GREATER_THAN_FIELD_NUMBER: _ClassVar[int]
    NUM_LESS_THAN_FIELD_NUMBER: _ClassVar[int]
    NUM_EQUALS_FIELD_NUMBER: _ClassVar[int]
    COUNT_LESS_THAN_FIELD_NUMBER: _ClassVar[int]
    STR_EQUALS_FIELD_NUMBER: _ClassVar[int]
    STR_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    BOOL_EQUALS_FIELD_NUMBER: _ClassVar[int]
    key: str
    negate: bool
    exists_check: bool
    num_greater_than: float
    num_less_than: float
    num_equals: float
    count_less_than: int
    str_equals: str
    str_contains: str
    bool_equals: bool
    def __init__(self, key: _Optional[str] = ..., negate: bool = ..., exists_check: bool = ..., num_greater_than: _Optional[float] = ..., num_less_than: _Optional[float] = ..., num_equals: _Optional[float] = ..., count_less_than: _Optional[int] = ..., str_equals: _Optional[str] = ..., str_contains: _Optional[str] = ..., bool_equals: bool = ...) -> None: ...

class Expiration(_message.Message):
    __slots__ = ["units", "quantity"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    units: TimeUnit
    quantity: int
    def __init__(self, units: _Optional[_Union[TimeUnit, str]] = ..., quantity: _Optional[int] = ...) -> None: ...
