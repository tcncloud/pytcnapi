from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_CALL: _ClassVar[Channel]
    CHANNEL_SMS: _ClassVar[Channel]

class ReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVIEW_STATUS_TODO: _ClassVar[ReviewStatus]
    REVIEW_STATUS_DONE: _ClassVar[ReviewStatus]
    REVIEW_STATUS_NONE: _ClassVar[ReviewStatus]
CHANNEL_CALL: Channel
CHANNEL_SMS: Channel
REVIEW_STATUS_TODO: ReviewStatus
REVIEW_STATUS_DONE: ReviewStatus
REVIEW_STATUS_NONE: ReviewStatus

class Transcript(_message.Message):
    __slots__ = ("call", "sms", "channel", "start_time", "delete_time", "flag_summary", "transcript_sid")
    CALL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    call: Call
    sms: Sms
    channel: Channel
    start_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    flag_summary: FlagSummary
    transcript_sid: int
    def __init__(self, call: _Optional[_Union[Call, _Mapping]] = ..., sms: _Optional[_Union[Sms, _Mapping]] = ..., channel: _Optional[_Union[Channel, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flag_summary: _Optional[_Union[FlagSummary, _Mapping]] = ..., transcript_sid: _Optional[int] = ...) -> None: ...

class FlagSummary(_message.Message):
    __slots__ = ("count", "priority_sum", "priority_max", "need_review", "flags", "review_status")
    class NeedReview(_message.Message):
        __slots__ = ("priority_sum", "priority_max", "count", "flag_sids")
        PRIORITY_SUM_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_MAX_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
        priority_sum: int
        priority_max: int
        count: int
        flag_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, priority_sum: _Optional[int] = ..., priority_max: _Optional[int] = ..., count: _Optional[int] = ..., flag_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    class Flag(_message.Message):
        __slots__ = ("flag_sid", "name", "priority", "version", "filters", "must_review", "must_notify", "reviews")
        FLAG_SID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        MUST_REVIEW_FIELD_NUMBER: _ClassVar[int]
        MUST_NOTIFY_FIELD_NUMBER: _ClassVar[int]
        REVIEWS_FIELD_NUMBER: _ClassVar[int]
        flag_sid: int
        name: str
        priority: int
        version: int
        filters: _containers.RepeatedCompositeFieldContainer[FlagSummary.Filter]
        must_review: bool
        must_notify: bool
        reviews: _containers.RepeatedCompositeFieldContainer[FlagSummary.Review]
        def __init__(self, flag_sid: _Optional[int] = ..., name: _Optional[str] = ..., priority: _Optional[int] = ..., version: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[FlagSummary.Filter, _Mapping]]] = ..., must_review: bool = ..., must_notify: bool = ..., reviews: _Optional[_Iterable[_Union[FlagSummary.Review, _Mapping]]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("join_key", "flag_sid", "filter_sid", "version", "name")
        JOIN_KEY_FIELD_NUMBER: _ClassVar[int]
        FLAG_SID_FIELD_NUMBER: _ClassVar[int]
        FILTER_SID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        join_key: str
        flag_sid: int
        filter_sid: int
        version: int
        name: str
        def __init__(self, join_key: _Optional[str] = ..., flag_sid: _Optional[int] = ..., filter_sid: _Optional[int] = ..., version: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class Review(_message.Message):
        __slots__ = ("join_key", "flag_sid", "user_id")
        JOIN_KEY_FIELD_NUMBER: _ClassVar[int]
        FLAG_SID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        join_key: str
        flag_sid: int
        user_id: str
        def __init__(self, join_key: _Optional[str] = ..., flag_sid: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_SUM_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_MAX_FIELD_NUMBER: _ClassVar[int]
    NEED_REVIEW_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    count: int
    priority_sum: int
    priority_max: int
    need_review: FlagSummary.NeedReview
    flags: _containers.RepeatedCompositeFieldContainer[FlagSummary.Flag]
    review_status: ReviewStatus
    def __init__(self, count: _Optional[int] = ..., priority_sum: _Optional[int] = ..., priority_max: _Optional[int] = ..., need_review: _Optional[_Union[FlagSummary.NeedReview, _Mapping]] = ..., flags: _Optional[_Iterable[_Union[FlagSummary.Flag, _Mapping]]] = ..., review_status: _Optional[_Union[ReviewStatus, str]] = ...) -> None: ...

class Sms(_message.Message):
    __slots__ = ("conversation_sid", "threads")
    class Thread(_message.Message):
        __slots__ = ("id", "segments")
        ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        id: int
        segments: _containers.RepeatedCompositeFieldContainer[Sms.Segment]
        def __init__(self, id: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Sms.Segment, _Mapping]]] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    threads: _containers.RepeatedCompositeFieldContainer[Sms.Thread]
    def __init__(self, conversation_sid: _Optional[int] = ..., threads: _Optional[_Iterable[_Union[Sms.Thread, _Mapping]]] = ...) -> None: ...

class Call(_message.Message):
    __slots__ = ("call_sid", "call_type", "audio_time", "threads")
    class Thread(_message.Message):
        __slots__ = ("id", "segments")
        ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        id: int
        segments: _containers.RepeatedCompositeFieldContainer[Call.Segment]
        def __init__(self, id: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Call.Segment, _Mapping]]] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    audio_time: int
    threads: _containers.RepeatedCompositeFieldContainer[Call.Thread]
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., audio_time: _Optional[int] = ..., threads: _Optional[_Iterable[_Union[Call.Thread, _Mapping]]] = ...) -> None: ...

class SearchTranscriptsRequest(_message.Message):
    __slots__ = ("page_size", "order_by", "read_mask", "bool_query", "page_token", "highlight")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    BOOL_QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    bool_query: TranscriptBoolQuery
    page_token: str
    highlight: Highlight
    def __init__(self, page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., bool_query: _Optional[_Union[TranscriptBoolQuery, _Mapping]] = ..., page_token: _Optional[str] = ..., highlight: _Optional[_Union[Highlight, _Mapping]] = ...) -> None: ...

class Highlight(_message.Message):
    __slots__ = ("prefix", "suffix")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    suffix: str
    def __init__(self, prefix: _Optional[str] = ..., suffix: _Optional[str] = ...) -> None: ...

class SearchTranscriptsResponse(_message.Message):
    __slots__ = ("hits", "next_page_token")
    class Hit(_message.Message):
        __slots__ = ("transcript",)
        TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
        transcript: Transcript
        def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...
    HITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[SearchTranscriptsResponse.Hit]
    next_page_token: str
    def __init__(self, hits: _Optional[_Iterable[_Union[SearchTranscriptsResponse.Hit, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class TranscriptBoolQuery(_message.Message):
    __slots__ = ("transcript",)
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    transcript: TranscriptQuery
    def __init__(self, transcript: _Optional[_Union[TranscriptQuery, _Mapping]] = ...) -> None: ...

class TranscriptQuery(_message.Message):
    __slots__ = ("transcript_sid", "channel", "metadata", "threads")
    class TranscriptSid(_message.Message):
        __slots__ = ("any",)
        ANY_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
    class Channel(_message.Message):
        __slots__ = ("any",)
        ANY_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[Channel]
        def __init__(self, any: _Optional[_Iterable[_Union[Channel, str]]] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("call", "sms")
        CALL_FIELD_NUMBER: _ClassVar[int]
        SMS_FIELD_NUMBER: _ClassVar[int]
        call: TranscriptQuery.Call
        sms: TranscriptQuery.Sms
        def __init__(self, call: _Optional[_Union[TranscriptQuery.Call, _Mapping]] = ..., sms: _Optional[_Union[TranscriptQuery.Sms, _Mapping]] = ...) -> None: ...
    class Call(_message.Message):
        __slots__ = ("call_sid", "audio_time", "call_type")
        class CallType(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
            def __init__(self, any: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ...) -> None: ...
        class CallSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class AudioTime(_message.Message):
            __slots__ = ("gte", "lte", "gt", "lt")
            GTE_FIELD_NUMBER: _ClassVar[int]
            LTE_FIELD_NUMBER: _ClassVar[int]
            GT_FIELD_NUMBER: _ClassVar[int]
            LT_FIELD_NUMBER: _ClassVar[int]
            gte: _wrappers_pb2.Int32Value
            lte: _wrappers_pb2.Int32Value
            gt: _wrappers_pb2.Int32Value
            lt: _wrappers_pb2.Int32Value
            def __init__(self, gte: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: TranscriptQuery.Call.CallSid
        audio_time: TranscriptQuery.Call.AudioTime
        call_type: TranscriptQuery.Call.CallType
        def __init__(self, call_sid: _Optional[_Union[TranscriptQuery.Call.CallSid, _Mapping]] = ..., audio_time: _Optional[_Union[TranscriptQuery.Call.AudioTime, _Mapping]] = ..., call_type: _Optional[_Union[TranscriptQuery.Call.CallType, _Mapping]] = ...) -> None: ...
    class Sms(_message.Message):
        __slots__ = ("conversation_sid",)
        class ConversationSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: TranscriptQuery.Sms.ConversationSid
        def __init__(self, conversation_sid: _Optional[_Union[TranscriptQuery.Sms.ConversationSid, _Mapping]] = ...) -> None: ...
    class Threads(_message.Message):
        __slots__ = ("id", "text")
        class Id(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class Text(_message.Message):
            __slots__ = ("match", "span_near")
            MATCH_FIELD_NUMBER: _ClassVar[int]
            SPAN_NEAR_FIELD_NUMBER: _ClassVar[int]
            match: Match
            span_near: SpanNear
            def __init__(self, match: _Optional[_Union[Match, _Mapping]] = ..., span_near: _Optional[_Union[SpanNear, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        id: TranscriptQuery.Threads.Id
        text: TranscriptQuery.Threads.Text
        def __init__(self, id: _Optional[_Union[TranscriptQuery.Threads.Id, _Mapping]] = ..., text: _Optional[_Union[TranscriptQuery.Threads.Text, _Mapping]] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: TranscriptQuery.TranscriptSid
    channel: TranscriptQuery.Channel
    metadata: TranscriptQuery.Metadata
    threads: TranscriptQuery.Threads
    def __init__(self, transcript_sid: _Optional[_Union[TranscriptQuery.TranscriptSid, _Mapping]] = ..., channel: _Optional[_Union[TranscriptQuery.Channel, _Mapping]] = ..., metadata: _Optional[_Union[TranscriptQuery.Metadata, _Mapping]] = ..., threads: _Optional[_Union[TranscriptQuery.Threads, _Mapping]] = ...) -> None: ...

class FuzzinessAuto(_message.Message):
    __slots__ = ("low", "high")
    LOW_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    low: int
    high: int
    def __init__(self, low: _Optional[int] = ..., high: _Optional[int] = ...) -> None: ...

class Match(_message.Message):
    __slots__ = ("text", "operator", "fuzziness_auto", "fuzziness_value")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    FUZZINESS_AUTO_FIELD_NUMBER: _ClassVar[int]
    FUZZINESS_VALUE_FIELD_NUMBER: _ClassVar[int]
    text: str
    operator: str
    fuzziness_auto: FuzzinessAuto
    fuzziness_value: int
    def __init__(self, text: _Optional[str] = ..., operator: _Optional[str] = ..., fuzziness_auto: _Optional[_Union[FuzzinessAuto, _Mapping]] = ..., fuzziness_value: _Optional[int] = ...) -> None: ...

class SpanNear(_message.Message):
    __slots__ = ("slop", "in_order", "clauses")
    class Clause(_message.Message):
        __slots__ = ("span_near", "span_fuzzy", "span_term")
        SPAN_NEAR_FIELD_NUMBER: _ClassVar[int]
        SPAN_FUZZY_FIELD_NUMBER: _ClassVar[int]
        SPAN_TERM_FIELD_NUMBER: _ClassVar[int]
        span_near: SpanNear
        span_fuzzy: SpanFuzzy
        span_term: SpanTerm
        def __init__(self, span_near: _Optional[_Union[SpanNear, _Mapping]] = ..., span_fuzzy: _Optional[_Union[SpanFuzzy, _Mapping]] = ..., span_term: _Optional[_Union[SpanTerm, _Mapping]] = ...) -> None: ...
    SLOP_FIELD_NUMBER: _ClassVar[int]
    IN_ORDER_FIELD_NUMBER: _ClassVar[int]
    CLAUSES_FIELD_NUMBER: _ClassVar[int]
    slop: int
    in_order: bool
    clauses: _containers.RepeatedCompositeFieldContainer[SpanNear.Clause]
    def __init__(self, slop: _Optional[int] = ..., in_order: bool = ..., clauses: _Optional[_Iterable[_Union[SpanNear.Clause, _Mapping]]] = ...) -> None: ...

class SpanTerm(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class SpanFuzzy(_message.Message):
    __slots__ = ("value", "fuzziness_auto", "fuzziness_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FUZZINESS_AUTO_FIELD_NUMBER: _ClassVar[int]
    FUZZINESS_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    fuzziness_auto: FuzzinessAuto
    fuzziness_value: int
    def __init__(self, value: _Optional[str] = ..., fuzziness_auto: _Optional[_Union[FuzzinessAuto, _Mapping]] = ..., fuzziness_value: _Optional[int] = ...) -> None: ...
