from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Interval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TODAY: _ClassVar[Interval]
    YESTERDAY: _ClassVar[Interval]
    THIS_WEEK: _ClassVar[Interval]
    LAST_7_DAYS: _ClassVar[Interval]
    LAST_WEEK: _ClassVar[Interval]
    LAST_14_DAYS: _ClassVar[Interval]
    THIS_MONTH: _ClassVar[Interval]
    LAST_30_DAYS: _ClassVar[Interval]
    LAST_60_DAYS: _ClassVar[Interval]
    LAST_90_DAYS: _ClassVar[Interval]
    LAST_180_DAYS: _ClassVar[Interval]

class TranscriptSummaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSCRIPT_SUMMARY_STATUS_QUEUED: _ClassVar[TranscriptSummaryStatus]
    TRANSCRIPT_SUMMARY_STATUS_QUEUED_ERRORED: _ClassVar[TranscriptSummaryStatus]
    TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED: _ClassVar[TranscriptSummaryStatus]
    TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED_ERRORED: _ClassVar[TranscriptSummaryStatus]
    TRANSCRIPT_SUMMARY_STATUS_VISIBLE: _ClassVar[TranscriptSummaryStatus]

class TranscriptSentimentTone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSCRIPT_SENTIMENT_TONE_UNKNOWN: _ClassVar[TranscriptSentimentTone]
    TRANSCRIPT_SENTIMENT_TONE_NEGATIVE: _ClassVar[TranscriptSentimentTone]
    TRANSCRIPT_SENTIMENT_TONE_NEUTRAL: _ClassVar[TranscriptSentimentTone]
    TRANSCRIPT_SENTIMENT_TONE_POSITIVE: _ClassVar[TranscriptSentimentTone]

class RecordingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECORDING_TYPE_TCN: _ClassVar[RecordingType]
    RECORDING_TYPE_EXTERNAL: _ClassVar[RecordingType]
    RECORDING_TYPE_VOICEMAIL: _ClassVar[RecordingType]
TODAY: Interval
YESTERDAY: Interval
THIS_WEEK: Interval
LAST_7_DAYS: Interval
LAST_WEEK: Interval
LAST_14_DAYS: Interval
THIS_MONTH: Interval
LAST_30_DAYS: Interval
LAST_60_DAYS: Interval
LAST_90_DAYS: Interval
LAST_180_DAYS: Interval
TRANSCRIPT_SUMMARY_STATUS_QUEUED: TranscriptSummaryStatus
TRANSCRIPT_SUMMARY_STATUS_QUEUED_ERRORED: TranscriptSummaryStatus
TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED: TranscriptSummaryStatus
TRANSCRIPT_SUMMARY_STATUS_SUMMARIZED_ERRORED: TranscriptSummaryStatus
TRANSCRIPT_SUMMARY_STATUS_VISIBLE: TranscriptSummaryStatus
TRANSCRIPT_SENTIMENT_TONE_UNKNOWN: TranscriptSentimentTone
TRANSCRIPT_SENTIMENT_TONE_NEGATIVE: TranscriptSentimentTone
TRANSCRIPT_SENTIMENT_TONE_NEUTRAL: TranscriptSentimentTone
TRANSCRIPT_SENTIMENT_TONE_POSITIVE: TranscriptSentimentTone
RECORDING_TYPE_TCN: RecordingType
RECORDING_TYPE_EXTERNAL: RecordingType
RECORDING_TYPE_VOICEMAIL: RecordingType
