from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BroadcastTemplateOrdering(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BY_NAME_ASC: _ClassVar[BroadcastTemplateOrdering]
    BY_NAME_DESC: _ClassVar[BroadcastTemplateOrdering]
    BY_TEMPLATE_NUMBER_ASC: _ClassVar[BroadcastTemplateOrdering]
    BY_TEMPLATE_NUMBER_DESC: _ClassVar[BroadcastTemplateOrdering]
    BY_MODIFIED_DATE_ASC: _ClassVar[BroadcastTemplateOrdering]
    BY_MODIFIED_DATE_DESC: _ClassVar[BroadcastTemplateOrdering]

class ScheduleByTimeZoneScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOTH: _ClassVar[ScheduleByTimeZoneScope]
    STOP_DATE: _ClassVar[ScheduleByTimeZoneScope]
    START_DATE: _ClassVar[ScheduleByTimeZoneScope]

class AnsweringMachineDetection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTIMIZE_MACHINE_DETECTION: _ClassVar[AnsweringMachineDetection]
    OPTIMIZE_MACHINE_DETECTION_SLOW_LIVE: _ClassVar[AnsweringMachineDetection]
    OPTIMIZE_MACHINE_DELIVERY: _ClassVar[AnsweringMachineDetection]
    BALANCED_DETECTION_AND_DELIVERY: _ClassVar[AnsweringMachineDetection]

class DialListPenetrationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPTH_FIRST: _ClassVar[DialListPenetrationStrategy]
    BREADTH_FIRST: _ClassVar[DialListPenetrationStrategy]

class StandardReportFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PREFERENCE: _ClassVar[StandardReportFilter]
    FILTER_BY_ANSWERED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_ANSWERED_HANGUPS: _ClassVar[StandardReportFilter]
    FILTER_BY_ANSWERED_LINKCALL: _ClassVar[StandardReportFilter]
    FILTER_BY_ANY_KEY_PRESSED: _ClassVar[StandardReportFilter]
    FILTER_BY_BUSY: _ClassVar[StandardReportFilter]
    FILTER_BY_CANCELED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_CONFIRM_KEYS_3_THROUGH_6: _ClassVar[StandardReportFilter]
    FILTER_BY_CONNECTED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_DNCL_CANCELED: _ClassVar[StandardReportFilter]
    FILTER_BY_FAILED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_INVALID_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_LINKCALL_ABANDONED: _ClassVar[StandardReportFilter]
    FILTER_BY_MACHINE_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_MACHINE_DELIVERY: _ClassVar[StandardReportFilter]
    FILTER_BY_MACHINE_HANGUP: _ClassVar[StandardReportFilter]
    FILTER_BY_MACHINE_AND_ANY_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_NO_ANSWER: _ClassVar[StandardReportFilter]
    FILTER_BY_NO_KEYS_PRESSED: _ClassVar[StandardReportFilter]
    FILTER_BY_NOT_CANCELED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_UNCONNECTED_CALLS: _ClassVar[StandardReportFilter]
    FILTER_BY_UNCONNECTED_EXCLUDE_INVALID: _ClassVar[StandardReportFilter]
    FILTER_BY_0_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_1_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_2_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_3_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_4_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_5_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_6_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_7_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_8_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_9_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_STAR_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_POUND_KEY: _ClassVar[StandardReportFilter]
    FILTER_BY_MACHINE_HANGUP_AND_UNCONNECTED: _ClassVar[StandardReportFilter]
    FILTER_BY_EXCLUDING_CANCELED_AND_INVALID: _ClassVar[StandardReportFilter]
BY_NAME_ASC: BroadcastTemplateOrdering
BY_NAME_DESC: BroadcastTemplateOrdering
BY_TEMPLATE_NUMBER_ASC: BroadcastTemplateOrdering
BY_TEMPLATE_NUMBER_DESC: BroadcastTemplateOrdering
BY_MODIFIED_DATE_ASC: BroadcastTemplateOrdering
BY_MODIFIED_DATE_DESC: BroadcastTemplateOrdering
BOTH: ScheduleByTimeZoneScope
STOP_DATE: ScheduleByTimeZoneScope
START_DATE: ScheduleByTimeZoneScope
OPTIMIZE_MACHINE_DETECTION: AnsweringMachineDetection
OPTIMIZE_MACHINE_DETECTION_SLOW_LIVE: AnsweringMachineDetection
OPTIMIZE_MACHINE_DELIVERY: AnsweringMachineDetection
BALANCED_DETECTION_AND_DELIVERY: AnsweringMachineDetection
DEPTH_FIRST: DialListPenetrationStrategy
BREADTH_FIRST: DialListPenetrationStrategy
NO_PREFERENCE: StandardReportFilter
FILTER_BY_ANSWERED_CALLS: StandardReportFilter
FILTER_BY_ANSWERED_HANGUPS: StandardReportFilter
FILTER_BY_ANSWERED_LINKCALL: StandardReportFilter
FILTER_BY_ANY_KEY_PRESSED: StandardReportFilter
FILTER_BY_BUSY: StandardReportFilter
FILTER_BY_CANCELED_CALLS: StandardReportFilter
FILTER_BY_CONFIRM_KEYS_3_THROUGH_6: StandardReportFilter
FILTER_BY_CONNECTED_CALLS: StandardReportFilter
FILTER_BY_DNCL_CANCELED: StandardReportFilter
FILTER_BY_FAILED_CALLS: StandardReportFilter
FILTER_BY_INVALID_CALLS: StandardReportFilter
FILTER_BY_LINKCALL_ABANDONED: StandardReportFilter
FILTER_BY_MACHINE_CALLS: StandardReportFilter
FILTER_BY_MACHINE_DELIVERY: StandardReportFilter
FILTER_BY_MACHINE_HANGUP: StandardReportFilter
FILTER_BY_MACHINE_AND_ANY_KEY: StandardReportFilter
FILTER_BY_NO_ANSWER: StandardReportFilter
FILTER_BY_NO_KEYS_PRESSED: StandardReportFilter
FILTER_BY_NOT_CANCELED_CALLS: StandardReportFilter
FILTER_BY_UNCONNECTED_CALLS: StandardReportFilter
FILTER_BY_UNCONNECTED_EXCLUDE_INVALID: StandardReportFilter
FILTER_BY_0_KEY: StandardReportFilter
FILTER_BY_1_KEY: StandardReportFilter
FILTER_BY_2_KEY: StandardReportFilter
FILTER_BY_3_KEY: StandardReportFilter
FILTER_BY_4_KEY: StandardReportFilter
FILTER_BY_5_KEY: StandardReportFilter
FILTER_BY_6_KEY: StandardReportFilter
FILTER_BY_7_KEY: StandardReportFilter
FILTER_BY_8_KEY: StandardReportFilter
FILTER_BY_9_KEY: StandardReportFilter
FILTER_BY_STAR_KEY: StandardReportFilter
FILTER_BY_POUND_KEY: StandardReportFilter
FILTER_BY_MACHINE_HANGUP_AND_UNCONNECTED: StandardReportFilter
FILTER_BY_EXCLUDING_CANCELED_AND_INVALID: StandardReportFilter
