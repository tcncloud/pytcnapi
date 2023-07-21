from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AnaTimeZone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ANA_TIME_ZONE_UNKNOWN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_ANCHORAGE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_CHICAGO: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_DENVER: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_INDIANAPOLIS: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_LOS_ANGELES: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_MEXICO_CITY: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_NEW_YORK: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_PHOENIX: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AMERICA_PUERTO_RICO: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_ASIA_CALCUTTA: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_ASIA_COLOMBO: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_ASIA_MANILA: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_ADELAIDE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_BRISBANE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_DARWIN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_MELBOURNE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_PERTH: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_AUSTRALIA_SYDNEY: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_BRAZIL_ACRE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_BRAZIL_DENORONHA: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_BRAZIL_EAST: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_BRAZIL_WEST: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_ATLANTIC: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_CENTRAL: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_EAST_SASKATCHEWAN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_EASTERN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_MOUNTAIN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_NEWFOUNDLAND: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_PACIFIC: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_SASKATCHEWAN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_CANADA_YUKON: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_EUROPE_BERLIN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_EUROPE_BUCHAREST: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_EUROPE_LONDON: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_EUROPE_MADRID: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_JAPAN: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_MEXICO_BAJANORTE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_MEXICO_BAJASUR: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_PACIFIC_AUCKLAND: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_PACIFIC_CHATHAM: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_PACIFIC_HONOLULU: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_SINGAPORE: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_ETC_UNIVERSAL: _ClassVar[AnaTimeZone]
    ANA_TIME_ZONE_ETC_GREENWICH: _ClassVar[AnaTimeZone]

class TimeFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TIME_FILTER_TYPE_UNDEFINED: _ClassVar[TimeFilterType]
    TIME_FILTER_TYPE_QUICK: _ClassVar[TimeFilterType]
    TIME_FILTER_TYPE_ABSOLUTE: _ClassVar[TimeFilterType]
    TIME_FILTER_TYPE_RELATIVE: _ClassVar[TimeFilterType]

class DashPageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DASH_PAGE_TYPE_UNDEFINED: _ClassVar[DashPageType]
    DASH_PAGE_TYPE_DASHBOARD: _ClassVar[DashPageType]
    DASH_PAGE_TYPE_VISUALIZATION_LEGACY: _ClassVar[DashPageType]
    DASH_PAGE_TYPE_CHART: _ClassVar[DashPageType]

class FilterBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FILTER_BY_UNDEFINED: _ClassVar[FilterBy]
    FILTER_BY_MINUTES: _ClassVar[FilterBy]
    FILTER_BY_HOURS: _ClassVar[FilterBy]
    FILTER_BY_DAYS: _ClassVar[FilterBy]
    FILTER_BY_WEEKS: _ClassVar[FilterBy]
    FILTER_BY_MONTHS: _ClassVar[FilterBy]
    FILTER_BY_YEARS: _ClassVar[FilterBy]

class WallaceDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    WALLACE_DATA_TYPE_UNDEFINED: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_KEYWORD: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_LONG: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_DOUBLE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_BOOLEAN: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_DATE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_STRING: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_NESTED: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_OBJECT: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_FLATTENED: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_INTEGER_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_FLOAT_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_LONG_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_DOUBLE_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_DATE_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_IP_RANGE: _ClassVar[WallaceDataType]
    WALLACE_DATA_TYPE_DOUBLE_KEYWORD: _ClassVar[WallaceDataType]

class TimeScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ONE_DAY: _ClassVar[TimeScope]
    ONE_WEEK: _ClassVar[TimeScope]
    ONE_MONTH: _ClassVar[TimeScope]
    ONE_YEAR: _ClassVar[TimeScope]
    ONE_MINUTE: _ClassVar[TimeScope]
    FIVE_MINUTES: _ClassVar[TimeScope]
    TEN_MINUTES: _ClassVar[TimeScope]
    TWENTY_MINUTES: _ClassVar[TimeScope]
    THIRTY_MINUTES: _ClassVar[TimeScope]
    ONE_HOUR: _ClassVar[TimeScope]
    TWO_HOURS: _ClassVar[TimeScope]
    THREE_HOURS: _ClassVar[TimeScope]
    FOUR_HOURS: _ClassVar[TimeScope]

class Tag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TAG_ALL: _ClassVar[Tag]
    TAG_CUSTOM: _ClassVar[Tag]
    TAG_LEGACY: _ClassVar[Tag]
    TAG_DYNAMIC: _ClassVar[Tag]
    P3_RJ_RECORDS_INBOUND_CALL: _ClassVar[Tag]
    P3_RJ_RECORDS_MANUAL_CALL: _ClassVar[Tag]
    P3_RJ_RECORDS_OUTBOUND_CALL: _ClassVar[Tag]
    P3_RJ_RECORDS_OUTBOUND_TASK: _ClassVar[Tag]
    P3_RJ_RECORDS_AGENT_CALL_OUTBOUND: _ClassVar[Tag]
    P3_RJ_RECORDS_AGENT_CALL_INBOUND: _ClassVar[Tag]
    P3_RJ_RECORDS_AGENT_CALL_MANUAL: _ClassVar[Tag]
    P3_RJ_RECORDS_SMS: _ClassVar[Tag]
    P3_RJ_RECORDS_EMAIL: _ClassVar[Tag]
    P3_RJ_AGGREGATE_INBOUND: _ClassVar[Tag]
    P3_RJ_AGGREGATE_OUTBOUND: _ClassVar[Tag]
    P3_RJ_AGGREGATE_MANUAL: _ClassVar[Tag]
    P3_RJ_AGGREGATE_AGENT_CALL: _ClassVar[Tag]
    P3_RJ_AGGREGATE_HUNT_GROUP: _ClassVar[Tag]
    P3_RJ_AGGREGATE_AGENT_SESSION: _ClassVar[Tag]
    P3_RJ_AGGREGATE_SKILLS: _ClassVar[Tag]
    P3_RJ_COLLATED_INBOUND: _ClassVar[Tag]
    P3_RJ_COLLATED_OUTBOUND: _ClassVar[Tag]
    P3_RJ_COLLATED_MANUAL: _ClassVar[Tag]
    P3_RJ_COLLATED_AGENT_CALL: _ClassVar[Tag]
    P3_RJ_COLLATED_HUNT_GROUP: _ClassVar[Tag]
    P3_RJ_COLLATED_AGENT_SESSION: _ClassVar[Tag]
    P3_RJ_MISC_SCHEDULED_CALLBACK: _ClassVar[Tag]

class CsvQuoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NO_QUOTE_TYPE: _ClassVar[CsvQuoteType]
    SINGLE: _ClassVar[CsvQuoteType]
    DOUBLE: _ClassVar[CsvQuoteType]

class StringComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STRING_EQ: _ClassVar[StringComparison]
    STRING_NEQ: _ClassVar[StringComparison]
    STRING_STARTS_WITH: _ClassVar[StringComparison]
    STRING_NOT_STARTS_WITH: _ClassVar[StringComparison]
    STRING_CONTAINS: _ClassVar[StringComparison]
    STRING_NOT_CONTAINS: _ClassVar[StringComparison]
    STRING_ENDS_WITH: _ClassVar[StringComparison]
    STRING_NOT_ENDS_WITH: _ClassVar[StringComparison]
    STRING_BLANK: _ClassVar[StringComparison]
    STRING_NOT_BLANK: _ClassVar[StringComparison]

class FloatComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FLOAT_EQ: _ClassVar[FloatComparison]
    FLOAT_NEQ: _ClassVar[FloatComparison]
    LT: _ClassVar[FloatComparison]
    LTE: _ClassVar[FloatComparison]
    GT: _ClassVar[FloatComparison]
    GTE: _ClassVar[FloatComparison]
    FLOAT_BLANK: _ClassVar[FloatComparison]
    FLOAT_NOT_BLANK: _ClassVar[FloatComparison]

class BoolComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BOOL_EQ: _ClassVar[BoolComparison]
    BOOL_NEQ: _ClassVar[BoolComparison]

class DateComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATE_COMPARISON_EQ: _ClassVar[DateComparison]
    DATE_COMPARISON_NEQ: _ClassVar[DateComparison]
    DATE_COMPARISON_LT: _ClassVar[DateComparison]
    DATE_COMPARISON_LTE: _ClassVar[DateComparison]
    DATE_COMPARISON_GT: _ClassVar[DateComparison]
    DATE_COMPARISON_GTE: _ClassVar[DateComparison]

class CompoundFilterJoin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AND: _ClassVar[CompoundFilterJoin]
    OR: _ClassVar[CompoundFilterJoin]

class AnaExportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ANA_EXPORT_TYPE_EMAIL: _ClassVar[AnaExportType]
    ANA_EXPORT_TYPE_SFTP: _ClassVar[AnaExportType]
    ANA_EXPORT_TYPE_HTTPS: _ClassVar[AnaExportType]

class ExporterDataSelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CHART_ID_SELECTION_TYPE: _ClassVar[ExporterDataSelectionType]
    CUSTOM_SELECTION_TYPE: _ClassVar[ExporterDataSelectionType]

class NumericAggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FLOAT_AGGREGATION_TOP_HITS: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_AVERAGE: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_SUM: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_MIN: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_MAX: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_TERMS: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_PERCENTILE: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_COUNT: _ClassVar[NumericAggregation]
    FLOAT_AGGREGATION_NONE: _ClassVar[NumericAggregation]

class NonNumericAggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STRING_AGGREGATION_TOP_HITS: _ClassVar[NonNumericAggregation]
    STRING_AGGREGATION_TERMS: _ClassVar[NonNumericAggregation]
    STRING_AGGREGATION_COUNT: _ClassVar[NonNumericAggregation]
    STRING_AGGREGATION_NONE: _ClassVar[NonNumericAggregation]

class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OPERATION_ADD: _ClassVar[Operation]
    OPERATION_SUBTRACT_LEFT: _ClassVar[Operation]
    OPERATION_SUBTRACT_RIGHT: _ClassVar[Operation]
    OPERATION_MULTIPLY: _ClassVar[Operation]
    OPERATION_DIVIDE_LEFT: _ClassVar[Operation]
    OPERATION_DIVIDE_RIGHT: _ClassVar[Operation]

class CustomDataSeleciton(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CUSTOM_DATA_SELECTION_UKNOWN: _ClassVar[CustomDataSeleciton]

class DataPointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATA_POINT_TYPE_NUMBER: _ClassVar[DataPointType]
    DATA_POINT_TYPE_STRING: _ClassVar[DataPointType]
    DATA_POINT_TYPE_BOOLEAN: _ClassVar[DataPointType]
    DATA_POINT_TYPE_DATE: _ClassVar[DataPointType]

class ExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NOT_SENT: _ClassVar[ExportStatus]
    SENT: _ClassVar[ExportStatus]
ANA_TIME_ZONE_UNKNOWN: AnaTimeZone
ANA_TIME_ZONE_AMERICA_ANCHORAGE: AnaTimeZone
ANA_TIME_ZONE_AMERICA_CHICAGO: AnaTimeZone
ANA_TIME_ZONE_AMERICA_DENVER: AnaTimeZone
ANA_TIME_ZONE_AMERICA_INDIANAPOLIS: AnaTimeZone
ANA_TIME_ZONE_AMERICA_LOS_ANGELES: AnaTimeZone
ANA_TIME_ZONE_AMERICA_MEXICO_CITY: AnaTimeZone
ANA_TIME_ZONE_AMERICA_NEW_YORK: AnaTimeZone
ANA_TIME_ZONE_AMERICA_PHOENIX: AnaTimeZone
ANA_TIME_ZONE_AMERICA_PUERTO_RICO: AnaTimeZone
ANA_TIME_ZONE_ASIA_CALCUTTA: AnaTimeZone
ANA_TIME_ZONE_ASIA_COLOMBO: AnaTimeZone
ANA_TIME_ZONE_ASIA_MANILA: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_ADELAIDE: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_BRISBANE: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_DARWIN: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_MELBOURNE: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_PERTH: AnaTimeZone
ANA_TIME_ZONE_AUSTRALIA_SYDNEY: AnaTimeZone
ANA_TIME_ZONE_BRAZIL_ACRE: AnaTimeZone
ANA_TIME_ZONE_BRAZIL_DENORONHA: AnaTimeZone
ANA_TIME_ZONE_BRAZIL_EAST: AnaTimeZone
ANA_TIME_ZONE_BRAZIL_WEST: AnaTimeZone
ANA_TIME_ZONE_CANADA_ATLANTIC: AnaTimeZone
ANA_TIME_ZONE_CANADA_CENTRAL: AnaTimeZone
ANA_TIME_ZONE_CANADA_EAST_SASKATCHEWAN: AnaTimeZone
ANA_TIME_ZONE_CANADA_EASTERN: AnaTimeZone
ANA_TIME_ZONE_CANADA_MOUNTAIN: AnaTimeZone
ANA_TIME_ZONE_CANADA_NEWFOUNDLAND: AnaTimeZone
ANA_TIME_ZONE_CANADA_PACIFIC: AnaTimeZone
ANA_TIME_ZONE_CANADA_SASKATCHEWAN: AnaTimeZone
ANA_TIME_ZONE_CANADA_YUKON: AnaTimeZone
ANA_TIME_ZONE_EUROPE_BERLIN: AnaTimeZone
ANA_TIME_ZONE_EUROPE_BUCHAREST: AnaTimeZone
ANA_TIME_ZONE_EUROPE_LONDON: AnaTimeZone
ANA_TIME_ZONE_EUROPE_MADRID: AnaTimeZone
ANA_TIME_ZONE_JAPAN: AnaTimeZone
ANA_TIME_ZONE_MEXICO_BAJANORTE: AnaTimeZone
ANA_TIME_ZONE_MEXICO_BAJASUR: AnaTimeZone
ANA_TIME_ZONE_PACIFIC_AUCKLAND: AnaTimeZone
ANA_TIME_ZONE_PACIFIC_CHATHAM: AnaTimeZone
ANA_TIME_ZONE_PACIFIC_HONOLULU: AnaTimeZone
ANA_TIME_ZONE_SINGAPORE: AnaTimeZone
ANA_TIME_ZONE_ETC_UNIVERSAL: AnaTimeZone
ANA_TIME_ZONE_ETC_GREENWICH: AnaTimeZone
TIME_FILTER_TYPE_UNDEFINED: TimeFilterType
TIME_FILTER_TYPE_QUICK: TimeFilterType
TIME_FILTER_TYPE_ABSOLUTE: TimeFilterType
TIME_FILTER_TYPE_RELATIVE: TimeFilterType
DASH_PAGE_TYPE_UNDEFINED: DashPageType
DASH_PAGE_TYPE_DASHBOARD: DashPageType
DASH_PAGE_TYPE_VISUALIZATION_LEGACY: DashPageType
DASH_PAGE_TYPE_CHART: DashPageType
FILTER_BY_UNDEFINED: FilterBy
FILTER_BY_MINUTES: FilterBy
FILTER_BY_HOURS: FilterBy
FILTER_BY_DAYS: FilterBy
FILTER_BY_WEEKS: FilterBy
FILTER_BY_MONTHS: FilterBy
FILTER_BY_YEARS: FilterBy
WALLACE_DATA_TYPE_UNDEFINED: WallaceDataType
WALLACE_DATA_TYPE_KEYWORD: WallaceDataType
WALLACE_DATA_TYPE_LONG: WallaceDataType
WALLACE_DATA_TYPE_DOUBLE: WallaceDataType
WALLACE_DATA_TYPE_BOOLEAN: WallaceDataType
WALLACE_DATA_TYPE_DATE: WallaceDataType
WALLACE_DATA_TYPE_STRING: WallaceDataType
WALLACE_DATA_TYPE_NESTED: WallaceDataType
WALLACE_DATA_TYPE_OBJECT: WallaceDataType
WALLACE_DATA_TYPE_FLATTENED: WallaceDataType
WALLACE_DATA_TYPE_INTEGER_RANGE: WallaceDataType
WALLACE_DATA_TYPE_FLOAT_RANGE: WallaceDataType
WALLACE_DATA_TYPE_LONG_RANGE: WallaceDataType
WALLACE_DATA_TYPE_DOUBLE_RANGE: WallaceDataType
WALLACE_DATA_TYPE_DATE_RANGE: WallaceDataType
WALLACE_DATA_TYPE_IP_RANGE: WallaceDataType
WALLACE_DATA_TYPE_DOUBLE_KEYWORD: WallaceDataType
ONE_DAY: TimeScope
ONE_WEEK: TimeScope
ONE_MONTH: TimeScope
ONE_YEAR: TimeScope
ONE_MINUTE: TimeScope
FIVE_MINUTES: TimeScope
TEN_MINUTES: TimeScope
TWENTY_MINUTES: TimeScope
THIRTY_MINUTES: TimeScope
ONE_HOUR: TimeScope
TWO_HOURS: TimeScope
THREE_HOURS: TimeScope
FOUR_HOURS: TimeScope
TAG_ALL: Tag
TAG_CUSTOM: Tag
TAG_LEGACY: Tag
TAG_DYNAMIC: Tag
P3_RJ_RECORDS_INBOUND_CALL: Tag
P3_RJ_RECORDS_MANUAL_CALL: Tag
P3_RJ_RECORDS_OUTBOUND_CALL: Tag
P3_RJ_RECORDS_OUTBOUND_TASK: Tag
P3_RJ_RECORDS_AGENT_CALL_OUTBOUND: Tag
P3_RJ_RECORDS_AGENT_CALL_INBOUND: Tag
P3_RJ_RECORDS_AGENT_CALL_MANUAL: Tag
P3_RJ_RECORDS_SMS: Tag
P3_RJ_RECORDS_EMAIL: Tag
P3_RJ_AGGREGATE_INBOUND: Tag
P3_RJ_AGGREGATE_OUTBOUND: Tag
P3_RJ_AGGREGATE_MANUAL: Tag
P3_RJ_AGGREGATE_AGENT_CALL: Tag
P3_RJ_AGGREGATE_HUNT_GROUP: Tag
P3_RJ_AGGREGATE_AGENT_SESSION: Tag
P3_RJ_AGGREGATE_SKILLS: Tag
P3_RJ_COLLATED_INBOUND: Tag
P3_RJ_COLLATED_OUTBOUND: Tag
P3_RJ_COLLATED_MANUAL: Tag
P3_RJ_COLLATED_AGENT_CALL: Tag
P3_RJ_COLLATED_HUNT_GROUP: Tag
P3_RJ_COLLATED_AGENT_SESSION: Tag
P3_RJ_MISC_SCHEDULED_CALLBACK: Tag
NO_QUOTE_TYPE: CsvQuoteType
SINGLE: CsvQuoteType
DOUBLE: CsvQuoteType
STRING_EQ: StringComparison
STRING_NEQ: StringComparison
STRING_STARTS_WITH: StringComparison
STRING_NOT_STARTS_WITH: StringComparison
STRING_CONTAINS: StringComparison
STRING_NOT_CONTAINS: StringComparison
STRING_ENDS_WITH: StringComparison
STRING_NOT_ENDS_WITH: StringComparison
STRING_BLANK: StringComparison
STRING_NOT_BLANK: StringComparison
FLOAT_EQ: FloatComparison
FLOAT_NEQ: FloatComparison
LT: FloatComparison
LTE: FloatComparison
GT: FloatComparison
GTE: FloatComparison
FLOAT_BLANK: FloatComparison
FLOAT_NOT_BLANK: FloatComparison
BOOL_EQ: BoolComparison
BOOL_NEQ: BoolComparison
DATE_COMPARISON_EQ: DateComparison
DATE_COMPARISON_NEQ: DateComparison
DATE_COMPARISON_LT: DateComparison
DATE_COMPARISON_LTE: DateComparison
DATE_COMPARISON_GT: DateComparison
DATE_COMPARISON_GTE: DateComparison
AND: CompoundFilterJoin
OR: CompoundFilterJoin
ANA_EXPORT_TYPE_EMAIL: AnaExportType
ANA_EXPORT_TYPE_SFTP: AnaExportType
ANA_EXPORT_TYPE_HTTPS: AnaExportType
CHART_ID_SELECTION_TYPE: ExporterDataSelectionType
CUSTOM_SELECTION_TYPE: ExporterDataSelectionType
FLOAT_AGGREGATION_TOP_HITS: NumericAggregation
FLOAT_AGGREGATION_AVERAGE: NumericAggregation
FLOAT_AGGREGATION_SUM: NumericAggregation
FLOAT_AGGREGATION_MIN: NumericAggregation
FLOAT_AGGREGATION_MAX: NumericAggregation
FLOAT_AGGREGATION_TERMS: NumericAggregation
FLOAT_AGGREGATION_PERCENTILE: NumericAggregation
FLOAT_AGGREGATION_COUNT: NumericAggregation
FLOAT_AGGREGATION_NONE: NumericAggregation
STRING_AGGREGATION_TOP_HITS: NonNumericAggregation
STRING_AGGREGATION_TERMS: NonNumericAggregation
STRING_AGGREGATION_COUNT: NonNumericAggregation
STRING_AGGREGATION_NONE: NonNumericAggregation
OPERATION_ADD: Operation
OPERATION_SUBTRACT_LEFT: Operation
OPERATION_SUBTRACT_RIGHT: Operation
OPERATION_MULTIPLY: Operation
OPERATION_DIVIDE_LEFT: Operation
OPERATION_DIVIDE_RIGHT: Operation
CUSTOM_DATA_SELECTION_UKNOWN: CustomDataSeleciton
DATA_POINT_TYPE_NUMBER: DataPointType
DATA_POINT_TYPE_STRING: DataPointType
DATA_POINT_TYPE_BOOLEAN: DataPointType
DATA_POINT_TYPE_DATE: DataPointType
NOT_SENT: ExportStatus
SENT: ExportStatus
