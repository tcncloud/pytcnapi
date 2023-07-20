from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BarChartOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BAR_CHART_ORIENTATION_BAR: _ClassVar[BarChartOrientation]
    BAR_CHART_ORIENTATION_COLUMN: _ClassVar[BarChartOrientation]

class ChartOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CHART_ORIENTATION_HORIZONTAL: _ClassVar[ChartOrientation]
    CHART_ORIENTATION_VERTICAL: _ClassVar[ChartOrientation]

class AreaChartChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AREA_CHART_CHOICE_AREA: _ClassVar[AreaChartChoice]
    AREA_CHART_CHOICE_AREASPLINE: _ClassVar[AreaChartChoice]

class LineChartStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LINE_CHART_STEP_LEFT: _ClassVar[LineChartStep]
    LINE_CHART_STEP_CENTER: _ClassVar[LineChartStep]
    LINE_CHART_STEP_RIGHT: _ClassVar[LineChartStep]
    LINE_CHART_STEP_NOLINE: _ClassVar[LineChartStep]

class ChartDisplayLabels(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CHART_DISPLAY_LABELS_NEVER: _ClassVar[ChartDisplayLabels]
    CHART_DISPLAY_LABELS_ALWAYS: _ClassVar[ChartDisplayLabels]

class ThresholdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    THRESHOLD_TYPE_STATIC: _ClassVar[ThresholdType]
    THRESHOLD_TYPE_DATA_POINT: _ClassVar[ThresholdType]
    THRESHOLD_TYPE_NOT_SET: _ClassVar[ThresholdType]

class PackedBubbleChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PACKED_BUBBLE_CHOICE_PACKED: _ClassVar[PackedBubbleChoice]
    PACKED_BUBBLE_CHOICE_SPLIT: _ClassVar[PackedBubbleChoice]

class SuffixChoices(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SUFFIX_CHOICES_NOSUFFIX: _ClassVar[SuffixChoices]
    SUFFIX_CHOICES_DOLLARS: _ClassVar[SuffixChoices]
    SUFFIX_CHOICES_PERCENTAGE: _ClassVar[SuffixChoices]
BAR_CHART_ORIENTATION_BAR: BarChartOrientation
BAR_CHART_ORIENTATION_COLUMN: BarChartOrientation
CHART_ORIENTATION_HORIZONTAL: ChartOrientation
CHART_ORIENTATION_VERTICAL: ChartOrientation
AREA_CHART_CHOICE_AREA: AreaChartChoice
AREA_CHART_CHOICE_AREASPLINE: AreaChartChoice
LINE_CHART_STEP_LEFT: LineChartStep
LINE_CHART_STEP_CENTER: LineChartStep
LINE_CHART_STEP_RIGHT: LineChartStep
LINE_CHART_STEP_NOLINE: LineChartStep
CHART_DISPLAY_LABELS_NEVER: ChartDisplayLabels
CHART_DISPLAY_LABELS_ALWAYS: ChartDisplayLabels
THRESHOLD_TYPE_STATIC: ThresholdType
THRESHOLD_TYPE_DATA_POINT: ThresholdType
THRESHOLD_TYPE_NOT_SET: ThresholdType
PACKED_BUBBLE_CHOICE_PACKED: PackedBubbleChoice
PACKED_BUBBLE_CHOICE_SPLIT: PackedBubbleChoice
SUFFIX_CHOICES_NOSUFFIX: SuffixChoices
SUFFIX_CHOICES_DOLLARS: SuffixChoices
SUFFIX_CHOICES_PERCENTAGE: SuffixChoices
