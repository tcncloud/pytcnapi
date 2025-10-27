import datetime

from annotations import authz_pb2 as _authz_pb2
from api.v1alpha1.vanalytics import correction_pb2 as _correction_pb2
from api.v1alpha1.vanalytics import filter_pb2 as _filter_pb2
from api.v1alpha1.vanalytics import flag_pb2 as _flag_pb2
from api.v1alpha1.vanalytics import flag_filter_pb2 as _flag_filter_pb2
from api.v1alpha1.vanalytics import flag_review_pb2 as _flag_review_pb2
from api.v1alpha1.vanalytics import flag_snapshot_pb2 as _flag_snapshot_pb2
from api.v1alpha1.vanalytics import flag_transcript_pb2 as _flag_transcript_pb2
from api.v1alpha1.vanalytics import flag_transcript_filter_pb2 as _flag_transcript_filter_pb2
from api.v1alpha1.vanalytics import transcript_pb2 as _transcript_pb2
from api.v1alpha1.vanalytics import transcript_summary_pb2 as _transcript_summary_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditRequest(_message.Message):
    __slots__ = ()
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AuditResponse(_message.Message):
    __slots__ = ()
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLED_AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_USAGE_FIELD_NUMBER: _ClassVar[int]
    BILLED_TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    audio_time: float
    billed_audio_time: float
    last_usage: _timestamp_pb2.Timestamp
    billed_transcripts: int
    def __init__(self, audio_time: _Optional[float] = ..., billed_audio_time: _Optional[float] = ..., last_usage: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billed_transcripts: _Optional[int] = ...) -> None: ...

class GetRecordingUrlRequest(_message.Message):
    __slots__ = ()
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    kind: str
    def __init__(self, transcript_sid: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class GetRecordingUrlResponse(_message.Message):
    __slots__ = ()
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class ListBillingSpanRequest(_message.Message):
    __slots__ = ()
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListBillingSpanResponse(_message.Message):
    __slots__ = ()
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    spans: _containers.RepeatedCompositeFieldContainer[BillingSpan]
    def __init__(self, next_page_token: _Optional[str] = ..., spans: _Optional[_Iterable[_Union[BillingSpan, _Mapping]]] = ...) -> None: ...

class BillingSpan(_message.Message):
    __slots__ = ()
    CALLS_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    calls: int
    hours: int
    cost: float
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, calls: _Optional[int] = ..., hours: _Optional[int] = ..., cost: _Optional[float] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
