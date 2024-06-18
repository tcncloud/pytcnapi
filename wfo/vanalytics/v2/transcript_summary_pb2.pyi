from api.commons import vanalytics_pb2 as _vanalytics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTranscriptSummaryRequest(_message.Message):
    __slots__ = ("transcript_sid",)
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    def __init__(self, transcript_sid: _Optional[int] = ...) -> None: ...

class GetTranscriptSummaryResponse(_message.Message):
    __slots__ = ("transcript_summary",)
    TRANSCRIPT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    transcript_summary: TranscriptSummary
    def __init__(self, transcript_summary: _Optional[_Union[TranscriptSummary, _Mapping]] = ...) -> None: ...

class TranscriptSummary(_message.Message):
    __slots__ = ("bullet_points", "status")
    BULLET_POINTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bullet_points: _containers.RepeatedScalarFieldContainer[str]
    status: _vanalytics_pb2.TranscriptSummaryStatus
    def __init__(self, bullet_points: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[_vanalytics_pb2.TranscriptSummaryStatus, str]] = ...) -> None: ...
