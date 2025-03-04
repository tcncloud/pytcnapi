from api.commons import acd_pb2 as _acd_pb2
from api.commons import omnichannel_pb2 as _omnichannel_pb2
from api.commons import vanalytics_pb2 as _vanalytics_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from wfo.vanalytics.v2 import agent_call_log_pb2 as _agent_call_log_pb2
from wfo.vanalytics.v2 import transcript_summary_pb2 as _transcript_summary_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REVIEW_STATUS_TODO: _ClassVar[ReviewStatus]
    REVIEW_STATUS_DONE: _ClassVar[ReviewStatus]
    REVIEW_STATUS_NONE: _ClassVar[ReviewStatus]
REVIEW_STATUS_TODO: ReviewStatus
REVIEW_STATUS_DONE: ReviewStatus
REVIEW_STATUS_NONE: ReviewStatus

class Transcript(_message.Message):
    __slots__ = ("call", "sms", "chat", "channel", "start_time", "delete_time", "flag_summary", "transcript_sid", "summary")
    class Skills(_message.Message):
        __slots__ = ("need", "want")
        NEED_FIELD_NUMBER: _ClassVar[int]
        WANT_FIELD_NUMBER: _ClassVar[int]
        need: _containers.RepeatedScalarFieldContainer[str]
        want: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, need: _Optional[_Iterable[str]] = ..., want: _Optional[_Iterable[str]] = ...) -> None: ...
    CALL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    call: Call
    sms: Sms
    chat: Chat
    channel: _omnichannel_pb2.ChannelType
    start_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    flag_summary: FlagSummary
    transcript_sid: int
    summary: _transcript_summary_pb2.TranscriptSummary
    def __init__(self, call: _Optional[_Union[Call, _Mapping]] = ..., sms: _Optional[_Union[Sms, _Mapping]] = ..., chat: _Optional[_Union[Chat, _Mapping]] = ..., channel: _Optional[_Union[_omnichannel_pb2.ChannelType, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flag_summary: _Optional[_Union[FlagSummary, _Mapping]] = ..., transcript_sid: _Optional[int] = ..., summary: _Optional[_Union[_transcript_summary_pb2.TranscriptSummary, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("conversation_sid", "threads", "phone", "caller_id", "campaign_sid", "agent_response")
    class AgentResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Sms.AgentResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Sms.AgentResponse, _Mapping]] = ...) -> None: ...
    class Phone(_message.Message):
        __slots__ = ("raw",)
        RAW_FIELD_NUMBER: _ClassVar[int]
        raw: str
        def __init__(self, raw: _Optional[str] = ...) -> None: ...
    class AgentResponse(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class Thread(_message.Message):
        __slots__ = ("id", "segments", "user_id", "sentiment")
        ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        id: int
        segments: _containers.RepeatedCompositeFieldContainer[Sms.Segment]
        user_id: str
        sentiment: Sentiment
        def __init__(self, id: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Sms.Segment, _Mapping]]] = ..., user_id: _Optional[str] = ..., sentiment: _Optional[_Union[Sentiment, _Mapping]] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("text", "offset", "attachments")
        class Attachment(_message.Message):
            __slots__ = ("attachment_sid",)
            ATTACHMENT_SID_FIELD_NUMBER: _ClassVar[int]
            attachment_sid: int
            def __init__(self, attachment_sid: _Optional[int] = ...) -> None: ...
        TEXT_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
        text: str
        offset: _duration_pb2.Duration
        attachments: _containers.RepeatedCompositeFieldContainer[Sms.Segment.Attachment]
        def __init__(self, text: _Optional[str] = ..., offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., attachments: _Optional[_Iterable[_Union[Sms.Segment.Attachment, _Mapping]]] = ...) -> None: ...
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    threads: _containers.RepeatedCompositeFieldContainer[Sms.Thread]
    phone: Sms.Phone
    caller_id: str
    campaign_sid: int
    agent_response: _containers.MessageMap[str, Sms.AgentResponse]
    def __init__(self, conversation_sid: _Optional[int] = ..., threads: _Optional[_Iterable[_Union[Sms.Thread, _Mapping]]] = ..., phone: _Optional[_Union[Sms.Phone, _Mapping]] = ..., caller_id: _Optional[str] = ..., campaign_sid: _Optional[int] = ..., agent_response: _Optional[_Mapping[str, Sms.AgentResponse]] = ...) -> None: ...

class Call(_message.Message):
    __slots__ = ("call_sid", "call_type", "audio_time", "threads", "silence", "talk_over", "talk_time", "caller_id", "group_name", "agent_response", "hunt_group_sids", "number_format", "agent_call_log", "phone", "audio_bytes", "recording_type")
    class AgentResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Call.AgentResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Call.AgentResponse, _Mapping]] = ...) -> None: ...
    class Phone(_message.Message):
        __slots__ = ("raw",)
        RAW_FIELD_NUMBER: _ClassVar[int]
        raw: str
        def __init__(self, raw: _Optional[str] = ...) -> None: ...
    class AgentResponse(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    class Thread(_message.Message):
        __slots__ = ("id", "segments", "user_id", "sentiment")
        ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        id: int
        segments: _containers.RepeatedCompositeFieldContainer[Call.Segment]
        user_id: str
        sentiment: Sentiment
        def __init__(self, id: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Call.Segment, _Mapping]]] = ..., user_id: _Optional[str] = ..., sentiment: _Optional[_Union[Sentiment, _Mapping]] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("text", "offset", "duration")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        text: str
        offset: _duration_pb2.Duration
        duration: _duration_pb2.Duration
        def __init__(self, text: _Optional[str] = ..., offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class TalkOver(_message.Message):
        __slots__ = ("duration", "occurrence", "threshold")
        class Duration(_message.Message):
            __slots__ = ("total", "max", "percentage")
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            total: _duration_pb2.Duration
            max: _duration_pb2.Duration
            percentage: int
            def __init__(self, total: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., percentage: _Optional[int] = ...) -> None: ...
        class Occurrence(_message.Message):
            __slots__ = ("total",)
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            total: int
            def __init__(self, total: _Optional[int] = ...) -> None: ...
        DURATION_FIELD_NUMBER: _ClassVar[int]
        OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        duration: Call.TalkOver.Duration
        occurrence: Call.TalkOver.Occurrence
        threshold: int
        def __init__(self, duration: _Optional[_Union[Call.TalkOver.Duration, _Mapping]] = ..., occurrence: _Optional[_Union[Call.TalkOver.Occurrence, _Mapping]] = ..., threshold: _Optional[int] = ...) -> None: ...
    class Silence(_message.Message):
        __slots__ = ("duration", "occurrence", "threshold")
        class Duration(_message.Message):
            __slots__ = ("total", "max", "percentage")
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            total: _duration_pb2.Duration
            max: _duration_pb2.Duration
            percentage: int
            def __init__(self, total: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., percentage: _Optional[int] = ...) -> None: ...
        class Occurrence(_message.Message):
            __slots__ = ("total",)
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            total: int
            def __init__(self, total: _Optional[int] = ...) -> None: ...
        DURATION_FIELD_NUMBER: _ClassVar[int]
        OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        duration: Call.Silence.Duration
        occurrence: Call.Silence.Occurrence
        threshold: int
        def __init__(self, duration: _Optional[_Union[Call.Silence.Duration, _Mapping]] = ..., occurrence: _Optional[_Union[Call.Silence.Occurrence, _Mapping]] = ..., threshold: _Optional[int] = ...) -> None: ...
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_FIELD_NUMBER: _ClassVar[int]
    TALK_OVER_FIELD_NUMBER: _ClassVar[int]
    TALK_TIME_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_LOG_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BYTES_FIELD_NUMBER: _ClassVar[int]
    RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    audio_time: int
    threads: _containers.RepeatedCompositeFieldContainer[Call.Thread]
    silence: Call.Silence
    talk_over: Call.TalkOver
    talk_time: _duration_pb2.Duration
    caller_id: str
    group_name: str
    agent_response: _containers.MessageMap[str, Call.AgentResponse]
    hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
    number_format: str
    agent_call_log: _agent_call_log_pb2.AgentCallLog
    phone: Call.Phone
    audio_bytes: int
    recording_type: _vanalytics_pb2.RecordingType
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., audio_time: _Optional[int] = ..., threads: _Optional[_Iterable[_Union[Call.Thread, _Mapping]]] = ..., silence: _Optional[_Union[Call.Silence, _Mapping]] = ..., talk_over: _Optional[_Union[Call.TalkOver, _Mapping]] = ..., talk_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., caller_id: _Optional[str] = ..., group_name: _Optional[str] = ..., agent_response: _Optional[_Mapping[str, Call.AgentResponse]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ..., number_format: _Optional[str] = ..., agent_call_log: _Optional[_Union[_agent_call_log_pb2.AgentCallLog, _Mapping]] = ..., phone: _Optional[_Union[Call.Phone, _Mapping]] = ..., audio_bytes: _Optional[int] = ..., recording_type: _Optional[_Union[_vanalytics_pb2.RecordingType, str]] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ("conversation_sid", "threads", "phone", "customer_name", "campaign_sid", "email_address", "agent_response")
    class AgentResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Chat.AgentResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Chat.AgentResponse, _Mapping]] = ...) -> None: ...
    class Thread(_message.Message):
        __slots__ = ("id", "segments", "user_id", "sentiment")
        ID_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        id: int
        segments: _containers.RepeatedCompositeFieldContainer[Chat.Segment]
        user_id: str
        sentiment: Sentiment
        def __init__(self, id: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Chat.Segment, _Mapping]]] = ..., user_id: _Optional[str] = ..., sentiment: _Optional[_Union[Sentiment, _Mapping]] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("text", "offset")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        text: str
        offset: _duration_pb2.Duration
        def __init__(self, text: _Optional[str] = ..., offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Phone(_message.Message):
        __slots__ = ("raw",)
        RAW_FIELD_NUMBER: _ClassVar[int]
        raw: str
        def __init__(self, raw: _Optional[str] = ...) -> None: ...
    class AgentResponse(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
    CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    conversation_sid: int
    threads: _containers.RepeatedCompositeFieldContainer[Chat.Thread]
    phone: Chat.Phone
    customer_name: str
    campaign_sid: int
    email_address: str
    agent_response: _containers.MessageMap[str, Chat.AgentResponse]
    def __init__(self, conversation_sid: _Optional[int] = ..., threads: _Optional[_Iterable[_Union[Chat.Thread, _Mapping]]] = ..., phone: _Optional[_Union[Chat.Phone, _Mapping]] = ..., customer_name: _Optional[str] = ..., campaign_sid: _Optional[int] = ..., email_address: _Optional[str] = ..., agent_response: _Optional[_Mapping[str, Chat.AgentResponse]] = ...) -> None: ...

class Sentiment(_message.Message):
    __slots__ = ("overall", "worst", "dominant", "last", "samples")
    class Sample(_message.Message):
        __slots__ = ("estimate", "offset", "duration")
        ESTIMATE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        estimate: Sentiment.Estimate
        offset: _duration_pb2.Duration
        duration: _duration_pb2.Duration
        def __init__(self, estimate: _Optional[_Union[Sentiment.Estimate, _Mapping]] = ..., offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Estimate(_message.Message):
        __slots__ = ("positive", "neutral", "negative")
        POSITIVE_FIELD_NUMBER: _ClassVar[int]
        NEUTRAL_FIELD_NUMBER: _ClassVar[int]
        NEGATIVE_FIELD_NUMBER: _ClassVar[int]
        positive: float
        neutral: float
        negative: float
        def __init__(self, positive: _Optional[float] = ..., neutral: _Optional[float] = ..., negative: _Optional[float] = ...) -> None: ...
    OVERALL_FIELD_NUMBER: _ClassVar[int]
    WORST_FIELD_NUMBER: _ClassVar[int]
    DOMINANT_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    overall: Sentiment.Estimate
    worst: _vanalytics_pb2.TranscriptSentimentTone
    dominant: _vanalytics_pb2.TranscriptSentimentTone
    last: _vanalytics_pb2.TranscriptSentimentTone
    samples: _containers.RepeatedCompositeFieldContainer[Sentiment.Sample]
    def __init__(self, overall: _Optional[_Union[Sentiment.Estimate, _Mapping]] = ..., worst: _Optional[_Union[_vanalytics_pb2.TranscriptSentimentTone, str]] = ..., dominant: _Optional[_Union[_vanalytics_pb2.TranscriptSentimentTone, str]] = ..., last: _Optional[_Union[_vanalytics_pb2.TranscriptSentimentTone, str]] = ..., samples: _Optional[_Iterable[_Union[Sentiment.Sample, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("hits", "next_page_token", "total")
    class Hit(_message.Message):
        __slots__ = ("transcript",)
        TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
        transcript: Transcript
        def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...
    HITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[SearchTranscriptsResponse.Hit]
    next_page_token: str
    total: int
    def __init__(self, hits: _Optional[_Iterable[_Union[SearchTranscriptsResponse.Hit, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class TranscriptBoolQuery(_message.Message):
    __slots__ = ("transcript",)
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    transcript: TranscriptQuery
    def __init__(self, transcript: _Optional[_Union[TranscriptQuery, _Mapping]] = ...) -> None: ...

class TranscriptQuery(_message.Message):
    __slots__ = ("transcript_sid", "channel", "metadata", "threads", "flag_summary", "start_time", "delete_time", "phone", "channel_type", "skills", "agent_response")
    class SkillsQuery(_message.Message):
        __slots__ = ("need", "want")
        class Skills(_message.Message):
            __slots__ = ("any", "all")
            ANY_FIELD_NUMBER: _ClassVar[int]
            ALL_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            all: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ..., all: _Optional[_Iterable[str]] = ...) -> None: ...
        NEED_FIELD_NUMBER: _ClassVar[int]
        WANT_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        need: TranscriptQuery.SkillsQuery.Skills
        want: TranscriptQuery.SkillsQuery.Skills
        def __init__(self, need: _Optional[_Union[TranscriptQuery.SkillsQuery.Skills, _Mapping]] = ..., want: _Optional[_Union[TranscriptQuery.SkillsQuery.Skills, _Mapping]] = ..., **kwargs) -> None: ...
    class Phone(_message.Message):
        __slots__ = ("cc", "ndc", "prefix", "city", "iso2", "region_code", "region_name", "time_zone", "type", "utc", "location", "raw")
        class Cc(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Ndc(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Prefix(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class City(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Iso2(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class RegionCode(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class RegionName(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class TimeZone(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Type(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Utc(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, any: _Optional[_Iterable[float]] = ...) -> None: ...
        class Location(_message.Message):
            __slots__ = ("zip_code_proximity",)
            class ZipCodeProximity(_message.Message):
                __slots__ = ("country_code", "zip_code", "distance")
                COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
                ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
                DISTANCE_FIELD_NUMBER: _ClassVar[int]
                country_code: str
                zip_code: str
                distance: str
                def __init__(self, country_code: _Optional[str] = ..., zip_code: _Optional[str] = ..., distance: _Optional[str] = ...) -> None: ...
            ZIP_CODE_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
            zip_code_proximity: TranscriptQuery.Phone.Location.ZipCodeProximity
            def __init__(self, zip_code_proximity: _Optional[_Union[TranscriptQuery.Phone.Location.ZipCodeProximity, _Mapping]] = ...) -> None: ...
        class Raw(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        CC_FIELD_NUMBER: _ClassVar[int]
        NDC_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        ISO2_FIELD_NUMBER: _ClassVar[int]
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        REGION_NAME_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UTC_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        RAW_FIELD_NUMBER: _ClassVar[int]
        cc: TranscriptQuery.Phone.Cc
        ndc: TranscriptQuery.Phone.Ndc
        prefix: TranscriptQuery.Phone.Prefix
        city: TranscriptQuery.Phone.City
        iso2: TranscriptQuery.Phone.Iso2
        region_code: TranscriptQuery.Phone.RegionCode
        region_name: TranscriptQuery.Phone.RegionName
        time_zone: TranscriptQuery.Phone.TimeZone
        type: TranscriptQuery.Phone.Type
        utc: TranscriptQuery.Phone.Utc
        location: TranscriptQuery.Phone.Location
        raw: TranscriptQuery.Phone.Raw
        def __init__(self, cc: _Optional[_Union[TranscriptQuery.Phone.Cc, _Mapping]] = ..., ndc: _Optional[_Union[TranscriptQuery.Phone.Ndc, _Mapping]] = ..., prefix: _Optional[_Union[TranscriptQuery.Phone.Prefix, _Mapping]] = ..., city: _Optional[_Union[TranscriptQuery.Phone.City, _Mapping]] = ..., iso2: _Optional[_Union[TranscriptQuery.Phone.Iso2, _Mapping]] = ..., region_code: _Optional[_Union[TranscriptQuery.Phone.RegionCode, _Mapping]] = ..., region_name: _Optional[_Union[TranscriptQuery.Phone.RegionName, _Mapping]] = ..., time_zone: _Optional[_Union[TranscriptQuery.Phone.TimeZone, _Mapping]] = ..., type: _Optional[_Union[TranscriptQuery.Phone.Type, _Mapping]] = ..., utc: _Optional[_Union[TranscriptQuery.Phone.Utc, _Mapping]] = ..., location: _Optional[_Union[TranscriptQuery.Phone.Location, _Mapping]] = ..., raw: _Optional[_Union[TranscriptQuery.Phone.Raw, _Mapping]] = ...) -> None: ...
    class TranscriptSid(_message.Message):
        __slots__ = ("any",)
        ANY_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
    class Channel(_message.Message):
        __slots__ = ("any",)
        ANY_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[_omnichannel_pb2.ChannelType]
        def __init__(self, any: _Optional[_Iterable[_Union[_omnichannel_pb2.ChannelType, str]]] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("call", "sms", "chat")
        CALL_FIELD_NUMBER: _ClassVar[int]
        SMS_FIELD_NUMBER: _ClassVar[int]
        CHAT_FIELD_NUMBER: _ClassVar[int]
        call: TranscriptQuery.Call
        sms: TranscriptQuery.Sms
        chat: TranscriptQuery.Chat
        def __init__(self, call: _Optional[_Union[TranscriptQuery.Call, _Mapping]] = ..., sms: _Optional[_Union[TranscriptQuery.Sms, _Mapping]] = ..., chat: _Optional[_Union[TranscriptQuery.Chat, _Mapping]] = ...) -> None: ...
    class Call(_message.Message):
        __slots__ = ("call_sid", "audio_time", "call_type", "silence", "talk_over", "talk_time", "caller_id", "group_name", "agent_response", "hunt_group_sids", "agent_call_log", "audio_bytes", "recording_type")
        class RecordingType(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[_vanalytics_pb2.RecordingType]
            def __init__(self, any: _Optional[_Iterable[_Union[_vanalytics_pb2.RecordingType, str]]] = ...) -> None: ...
        class AudioBytes(_message.Message):
            __slots__ = ("gte", "lte", "gt", "lt")
            GTE_FIELD_NUMBER: _ClassVar[int]
            LTE_FIELD_NUMBER: _ClassVar[int]
            GT_FIELD_NUMBER: _ClassVar[int]
            LT_FIELD_NUMBER: _ClassVar[int]
            gte: _wrappers_pb2.Int64Value
            lte: _wrappers_pb2.Int64Value
            gt: _wrappers_pb2.Int64Value
            lt: _wrappers_pb2.Int64Value
            def __init__(self, gte: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
        class HuntGroupSids(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class AgentResponse(_message.Message):
            __slots__ = ("key", "values", "numbers")
            class Values(_message.Message):
                __slots__ = ("starts_with", "contains")
                IN_FIELD_NUMBER: _ClassVar[int]
                STARTS_WITH_FIELD_NUMBER: _ClassVar[int]
                CONTAINS_FIELD_NUMBER: _ClassVar[int]
                starts_with: str
                contains: str
                def __init__(self, starts_with: _Optional[str] = ..., contains: _Optional[str] = ..., **kwargs) -> None: ...
            class Numbers(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt", "eq")
                IN_FIELD_NUMBER: _ClassVar[int]
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                EQ_FIELD_NUMBER: _ClassVar[int]
                gte: _wrappers_pb2.DoubleValue
                lte: _wrappers_pb2.DoubleValue
                gt: _wrappers_pb2.DoubleValue
                lt: _wrappers_pb2.DoubleValue
                eq: _wrappers_pb2.DoubleValue
                def __init__(self, gte: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., eq: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., **kwargs) -> None: ...
            class Key(_message.Message):
                __slots__ = ("starts_with", "contains")
                IN_FIELD_NUMBER: _ClassVar[int]
                STARTS_WITH_FIELD_NUMBER: _ClassVar[int]
                CONTAINS_FIELD_NUMBER: _ClassVar[int]
                starts_with: str
                contains: str
                def __init__(self, starts_with: _Optional[str] = ..., contains: _Optional[str] = ..., **kwargs) -> None: ...
            AND_FIELD_NUMBER: _ClassVar[int]
            OR_FIELD_NUMBER: _ClassVar[int]
            NOT_FIELD_NUMBER: _ClassVar[int]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            NUMBERS_FIELD_NUMBER: _ClassVar[int]
            key: TranscriptQuery.Call.AgentResponse.Key
            values: TranscriptQuery.Call.AgentResponse.Values
            numbers: TranscriptQuery.Call.AgentResponse.Numbers
            def __init__(self, key: _Optional[_Union[TranscriptQuery.Call.AgentResponse.Key, _Mapping]] = ..., values: _Optional[_Union[TranscriptQuery.Call.AgentResponse.Values, _Mapping]] = ..., numbers: _Optional[_Union[TranscriptQuery.Call.AgentResponse.Numbers, _Mapping]] = ..., **kwargs) -> None: ...
        class CallType(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
            def __init__(self, any: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ...) -> None: ...
        class GroupName(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class CallSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class CallerId(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
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
        class TalkTime(_message.Message):
            __slots__ = ("gte", "lte", "gt", "lt")
            GTE_FIELD_NUMBER: _ClassVar[int]
            LTE_FIELD_NUMBER: _ClassVar[int]
            GT_FIELD_NUMBER: _ClassVar[int]
            LT_FIELD_NUMBER: _ClassVar[int]
            gte: _duration_pb2.Duration
            lte: _duration_pb2.Duration
            gt: _duration_pb2.Duration
            lt: _duration_pb2.Duration
            def __init__(self, gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class TalkOver(_message.Message):
            __slots__ = ("duration_total", "duration_max", "occurrence_total", "duration_percentage")
            class DurationTotal(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _duration_pb2.Duration
                lte: _duration_pb2.Duration
                gt: _duration_pb2.Duration
                lt: _duration_pb2.Duration
                def __init__(self, gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class DurationMax(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _duration_pb2.Duration
                lte: _duration_pb2.Duration
                gt: _duration_pb2.Duration
                lt: _duration_pb2.Duration
                def __init__(self, gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class OccurrenceTotal(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _wrappers_pb2.UInt32Value
                lte: _wrappers_pb2.UInt32Value
                gt: _wrappers_pb2.UInt32Value
                lt: _wrappers_pb2.UInt32Value
                def __init__(self, gte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
            class DurationPercentage(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _wrappers_pb2.UInt32Value
                lte: _wrappers_pb2.UInt32Value
                gt: _wrappers_pb2.UInt32Value
                lt: _wrappers_pb2.UInt32Value
                def __init__(self, gte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
            DURATION_TOTAL_FIELD_NUMBER: _ClassVar[int]
            DURATION_MAX_FIELD_NUMBER: _ClassVar[int]
            OCCURRENCE_TOTAL_FIELD_NUMBER: _ClassVar[int]
            DURATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            duration_total: TranscriptQuery.Call.TalkOver.DurationTotal
            duration_max: TranscriptQuery.Call.TalkOver.DurationMax
            occurrence_total: TranscriptQuery.Call.TalkOver.OccurrenceTotal
            duration_percentage: TranscriptQuery.Call.TalkOver.DurationPercentage
            def __init__(self, duration_total: _Optional[_Union[TranscriptQuery.Call.TalkOver.DurationTotal, _Mapping]] = ..., duration_max: _Optional[_Union[TranscriptQuery.Call.TalkOver.DurationMax, _Mapping]] = ..., occurrence_total: _Optional[_Union[TranscriptQuery.Call.TalkOver.OccurrenceTotal, _Mapping]] = ..., duration_percentage: _Optional[_Union[TranscriptQuery.Call.TalkOver.DurationPercentage, _Mapping]] = ...) -> None: ...
        class Silence(_message.Message):
            __slots__ = ("duration_total", "duration_max", "occurrence_total", "duration_percentage")
            class DurationTotal(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _duration_pb2.Duration
                lte: _duration_pb2.Duration
                gt: _duration_pb2.Duration
                lt: _duration_pb2.Duration
                def __init__(self, gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class DurationMax(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _duration_pb2.Duration
                lte: _duration_pb2.Duration
                gt: _duration_pb2.Duration
                lt: _duration_pb2.Duration
                def __init__(self, gte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lte: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., gt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            class OccurrenceTotal(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _wrappers_pb2.UInt32Value
                lte: _wrappers_pb2.UInt32Value
                gt: _wrappers_pb2.UInt32Value
                lt: _wrappers_pb2.UInt32Value
                def __init__(self, gte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
            class DurationPercentage(_message.Message):
                __slots__ = ("gte", "lte", "gt", "lt")
                GTE_FIELD_NUMBER: _ClassVar[int]
                LTE_FIELD_NUMBER: _ClassVar[int]
                GT_FIELD_NUMBER: _ClassVar[int]
                LT_FIELD_NUMBER: _ClassVar[int]
                gte: _wrappers_pb2.UInt32Value
                lte: _wrappers_pb2.UInt32Value
                gt: _wrappers_pb2.UInt32Value
                lt: _wrappers_pb2.UInt32Value
                def __init__(self, gte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
            DURATION_TOTAL_FIELD_NUMBER: _ClassVar[int]
            DURATION_MAX_FIELD_NUMBER: _ClassVar[int]
            OCCURRENCE_TOTAL_FIELD_NUMBER: _ClassVar[int]
            DURATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            duration_total: TranscriptQuery.Call.Silence.DurationTotal
            duration_max: TranscriptQuery.Call.Silence.DurationMax
            occurrence_total: TranscriptQuery.Call.Silence.OccurrenceTotal
            duration_percentage: TranscriptQuery.Call.Silence.DurationPercentage
            def __init__(self, duration_total: _Optional[_Union[TranscriptQuery.Call.Silence.DurationTotal, _Mapping]] = ..., duration_max: _Optional[_Union[TranscriptQuery.Call.Silence.DurationMax, _Mapping]] = ..., occurrence_total: _Optional[_Union[TranscriptQuery.Call.Silence.OccurrenceTotal, _Mapping]] = ..., duration_percentage: _Optional[_Union[TranscriptQuery.Call.Silence.DurationPercentage, _Mapping]] = ...) -> None: ...
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        SILENCE_FIELD_NUMBER: _ClassVar[int]
        TALK_OVER_FIELD_NUMBER: _ClassVar[int]
        TALK_TIME_FIELD_NUMBER: _ClassVar[int]
        CALLER_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
        AGENT_CALL_LOG_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BYTES_FIELD_NUMBER: _ClassVar[int]
        RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: TranscriptQuery.Call.CallSid
        audio_time: TranscriptQuery.Call.AudioTime
        call_type: TranscriptQuery.Call.CallType
        silence: TranscriptQuery.Call.Silence
        talk_over: TranscriptQuery.Call.TalkOver
        talk_time: TranscriptQuery.Call.TalkTime
        caller_id: TranscriptQuery.Call.CallerId
        group_name: TranscriptQuery.Call.GroupName
        agent_response: TranscriptQuery.Call.AgentResponse
        hunt_group_sids: TranscriptQuery.Call.HuntGroupSids
        agent_call_log: _agent_call_log_pb2.AgentCallLogQuery
        audio_bytes: TranscriptQuery.Call.AudioBytes
        recording_type: TranscriptQuery.Call.RecordingType
        def __init__(self, call_sid: _Optional[_Union[TranscriptQuery.Call.CallSid, _Mapping]] = ..., audio_time: _Optional[_Union[TranscriptQuery.Call.AudioTime, _Mapping]] = ..., call_type: _Optional[_Union[TranscriptQuery.Call.CallType, _Mapping]] = ..., silence: _Optional[_Union[TranscriptQuery.Call.Silence, _Mapping]] = ..., talk_over: _Optional[_Union[TranscriptQuery.Call.TalkOver, _Mapping]] = ..., talk_time: _Optional[_Union[TranscriptQuery.Call.TalkTime, _Mapping]] = ..., caller_id: _Optional[_Union[TranscriptQuery.Call.CallerId, _Mapping]] = ..., group_name: _Optional[_Union[TranscriptQuery.Call.GroupName, _Mapping]] = ..., agent_response: _Optional[_Union[TranscriptQuery.Call.AgentResponse, _Mapping]] = ..., hunt_group_sids: _Optional[_Union[TranscriptQuery.Call.HuntGroupSids, _Mapping]] = ..., agent_call_log: _Optional[_Union[_agent_call_log_pb2.AgentCallLogQuery, _Mapping]] = ..., audio_bytes: _Optional[_Union[TranscriptQuery.Call.AudioBytes, _Mapping]] = ..., recording_type: _Optional[_Union[TranscriptQuery.Call.RecordingType, _Mapping]] = ...) -> None: ...
    class Sms(_message.Message):
        __slots__ = ("conversation_sid", "campaign_sid")
        class ConversationSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class CampaignSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: TranscriptQuery.Sms.ConversationSid
        campaign_sid: TranscriptQuery.Sms.CampaignSid
        def __init__(self, conversation_sid: _Optional[_Union[TranscriptQuery.Sms.ConversationSid, _Mapping]] = ..., campaign_sid: _Optional[_Union[TranscriptQuery.Sms.CampaignSid, _Mapping]] = ...) -> None: ...
    class Chat(_message.Message):
        __slots__ = ("conversation_sid", "campaign_sid", "customer_name", "email_address")
        class ConversationSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class CampaignSid(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class CustomerName(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class EmailAddress(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_SID_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: TranscriptQuery.Chat.ConversationSid
        campaign_sid: TranscriptQuery.Chat.CampaignSid
        customer_name: TranscriptQuery.Chat.CustomerName
        email_address: TranscriptQuery.Chat.EmailAddress
        def __init__(self, conversation_sid: _Optional[_Union[TranscriptQuery.Chat.ConversationSid, _Mapping]] = ..., campaign_sid: _Optional[_Union[TranscriptQuery.Chat.CampaignSid, _Mapping]] = ..., customer_name: _Optional[_Union[TranscriptQuery.Chat.CustomerName, _Mapping]] = ..., email_address: _Optional[_Union[TranscriptQuery.Chat.EmailAddress, _Mapping]] = ...) -> None: ...
    class AgentResponse(_message.Message):
        __slots__ = ("key", "values", "numbers")
        class Values(_message.Message):
            __slots__ = ("starts_with", "contains")
            IN_FIELD_NUMBER: _ClassVar[int]
            STARTS_WITH_FIELD_NUMBER: _ClassVar[int]
            CONTAINS_FIELD_NUMBER: _ClassVar[int]
            starts_with: str
            contains: str
            def __init__(self, starts_with: _Optional[str] = ..., contains: _Optional[str] = ..., **kwargs) -> None: ...
        class Numbers(_message.Message):
            __slots__ = ("gte", "lte", "gt", "lt", "eq")
            IN_FIELD_NUMBER: _ClassVar[int]
            GTE_FIELD_NUMBER: _ClassVar[int]
            LTE_FIELD_NUMBER: _ClassVar[int]
            GT_FIELD_NUMBER: _ClassVar[int]
            LT_FIELD_NUMBER: _ClassVar[int]
            EQ_FIELD_NUMBER: _ClassVar[int]
            gte: _wrappers_pb2.DoubleValue
            lte: _wrappers_pb2.DoubleValue
            gt: _wrappers_pb2.DoubleValue
            lt: _wrappers_pb2.DoubleValue
            eq: _wrappers_pb2.DoubleValue
            def __init__(self, gte: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., eq: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., **kwargs) -> None: ...
        class Key(_message.Message):
            __slots__ = ("starts_with", "contains")
            IN_FIELD_NUMBER: _ClassVar[int]
            STARTS_WITH_FIELD_NUMBER: _ClassVar[int]
            CONTAINS_FIELD_NUMBER: _ClassVar[int]
            starts_with: str
            contains: str
            def __init__(self, starts_with: _Optional[str] = ..., contains: _Optional[str] = ..., **kwargs) -> None: ...
        AND_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        NUMBERS_FIELD_NUMBER: _ClassVar[int]
        key: TranscriptQuery.AgentResponse.Key
        values: TranscriptQuery.AgentResponse.Values
        numbers: TranscriptQuery.AgentResponse.Numbers
        def __init__(self, key: _Optional[_Union[TranscriptQuery.AgentResponse.Key, _Mapping]] = ..., values: _Optional[_Union[TranscriptQuery.AgentResponse.Values, _Mapping]] = ..., numbers: _Optional[_Union[TranscriptQuery.AgentResponse.Numbers, _Mapping]] = ..., **kwargs) -> None: ...
    class Threads(_message.Message):
        __slots__ = ("id", "text", "user_id")
        class UserId(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ...) -> None: ...
        class Id(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
        class Text(_message.Message):
            __slots__ = ("match", "span_near", "timespan")
            class Timespan(_message.Message):
                __slots__ = ("head", "tail")
                HEAD_FIELD_NUMBER: _ClassVar[int]
                TAIL_FIELD_NUMBER: _ClassVar[int]
                head: _duration_pb2.Duration
                tail: _duration_pb2.Duration
                def __init__(self, head: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tail: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
            MATCH_FIELD_NUMBER: _ClassVar[int]
            SPAN_NEAR_FIELD_NUMBER: _ClassVar[int]
            TIMESPAN_FIELD_NUMBER: _ClassVar[int]
            NOT_FIELD_NUMBER: _ClassVar[int]
            match: Match
            span_near: SpanNear
            timespan: TranscriptQuery.Threads.Text.Timespan
            def __init__(self, match: _Optional[_Union[Match, _Mapping]] = ..., span_near: _Optional[_Union[SpanNear, _Mapping]] = ..., timespan: _Optional[_Union[TranscriptQuery.Threads.Text.Timespan, _Mapping]] = ..., **kwargs) -> None: ...
        AND_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: TranscriptQuery.Threads.Id
        text: TranscriptQuery.Threads.Text
        user_id: TranscriptQuery.Threads.UserId
        def __init__(self, id: _Optional[_Union[TranscriptQuery.Threads.Id, _Mapping]] = ..., text: _Optional[_Union[TranscriptQuery.Threads.Text, _Mapping]] = ..., user_id: _Optional[_Union[TranscriptQuery.Threads.UserId, _Mapping]] = ..., **kwargs) -> None: ...
    class FlagSummary(_message.Message):
        __slots__ = ("need_review", "review_status", "flags", "count")
        class NeedReview(_message.Message):
            __slots__ = ("flag_sids",)
            class FlagSids(_message.Message):
                __slots__ = ("any",)
                ANY_FIELD_NUMBER: _ClassVar[int]
                any: _containers.RepeatedScalarFieldContainer[int]
                def __init__(self, any: _Optional[_Iterable[int]] = ...) -> None: ...
            FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
            flag_sids: TranscriptQuery.FlagSummary.NeedReview.FlagSids
            def __init__(self, flag_sids: _Optional[_Union[TranscriptQuery.FlagSummary.NeedReview.FlagSids, _Mapping]] = ...) -> None: ...
        class ReviewStatus(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[ReviewStatus]
            def __init__(self, any: _Optional[_Iterable[_Union[ReviewStatus, str]]] = ...) -> None: ...
        class Flags(_message.Message):
            __slots__ = ("flag_sid",)
            class FlagSid(_message.Message):
                __slots__ = ("any", "all")
                ANY_FIELD_NUMBER: _ClassVar[int]
                ALL_FIELD_NUMBER: _ClassVar[int]
                any: _containers.RepeatedScalarFieldContainer[int]
                all: _containers.RepeatedScalarFieldContainer[int]
                def __init__(self, any: _Optional[_Iterable[int]] = ..., all: _Optional[_Iterable[int]] = ...) -> None: ...
            FLAG_SID_FIELD_NUMBER: _ClassVar[int]
            flag_sid: TranscriptQuery.FlagSummary.Flags.FlagSid
            def __init__(self, flag_sid: _Optional[_Union[TranscriptQuery.FlagSummary.Flags.FlagSid, _Mapping]] = ...) -> None: ...
        class Count(_message.Message):
            __slots__ = ("gte", "lte", "gt", "lt", "eq")
            GTE_FIELD_NUMBER: _ClassVar[int]
            LTE_FIELD_NUMBER: _ClassVar[int]
            GT_FIELD_NUMBER: _ClassVar[int]
            LT_FIELD_NUMBER: _ClassVar[int]
            EQ_FIELD_NUMBER: _ClassVar[int]
            gte: _wrappers_pb2.Int32Value
            lte: _wrappers_pb2.Int32Value
            gt: _wrappers_pb2.Int32Value
            lt: _wrappers_pb2.Int32Value
            eq: _wrappers_pb2.Int32Value
            def __init__(self, gte: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., lte: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., gt: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., lt: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., eq: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        NEED_REVIEW_FIELD_NUMBER: _ClassVar[int]
        REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        need_review: TranscriptQuery.FlagSummary.NeedReview
        review_status: TranscriptQuery.FlagSummary.ReviewStatus
        flags: TranscriptQuery.FlagSummary.Flags
        count: TranscriptQuery.FlagSummary.Count
        def __init__(self, need_review: _Optional[_Union[TranscriptQuery.FlagSummary.NeedReview, _Mapping]] = ..., review_status: _Optional[_Union[TranscriptQuery.FlagSummary.ReviewStatus, _Mapping]] = ..., flags: _Optional[_Union[TranscriptQuery.FlagSummary.Flags, _Mapping]] = ..., count: _Optional[_Union[TranscriptQuery.FlagSummary.Count, _Mapping]] = ...) -> None: ...
    class StartTime(_message.Message):
        __slots__ = ("gte", "lte", "gt", "lt", "moment")
        GTE_FIELD_NUMBER: _ClassVar[int]
        LTE_FIELD_NUMBER: _ClassVar[int]
        GT_FIELD_NUMBER: _ClassVar[int]
        LT_FIELD_NUMBER: _ClassVar[int]
        MOMENT_FIELD_NUMBER: _ClassVar[int]
        gte: _timestamp_pb2.Timestamp
        lte: _timestamp_pb2.Timestamp
        gt: _timestamp_pb2.Timestamp
        lt: _timestamp_pb2.Timestamp
        moment: Moment
        def __init__(self, gte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., moment: _Optional[_Union[Moment, _Mapping]] = ...) -> None: ...
    class DeleteTime(_message.Message):
        __slots__ = ("gte", "lte", "gt", "lt")
        GTE_FIELD_NUMBER: _ClassVar[int]
        LTE_FIELD_NUMBER: _ClassVar[int]
        GT_FIELD_NUMBER: _ClassVar[int]
        LT_FIELD_NUMBER: _ClassVar[int]
        gte: _timestamp_pb2.Timestamp
        lte: _timestamp_pb2.Timestamp
        gt: _timestamp_pb2.Timestamp
        lt: _timestamp_pb2.Timestamp
        def __init__(self, gte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lte: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., gt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: TranscriptQuery.TranscriptSid
    channel: TranscriptQuery.Channel
    metadata: TranscriptQuery.Metadata
    threads: TranscriptQuery.Threads
    flag_summary: TranscriptQuery.FlagSummary
    start_time: TranscriptQuery.StartTime
    delete_time: TranscriptQuery.DeleteTime
    phone: TranscriptQuery.Phone
    channel_type: TranscriptQuery.Channel
    skills: TranscriptQuery.SkillsQuery
    agent_response: TranscriptQuery.AgentResponse
    def __init__(self, transcript_sid: _Optional[_Union[TranscriptQuery.TranscriptSid, _Mapping]] = ..., channel: _Optional[_Union[TranscriptQuery.Channel, _Mapping]] = ..., metadata: _Optional[_Union[TranscriptQuery.Metadata, _Mapping]] = ..., threads: _Optional[_Union[TranscriptQuery.Threads, _Mapping]] = ..., flag_summary: _Optional[_Union[TranscriptQuery.FlagSummary, _Mapping]] = ..., start_time: _Optional[_Union[TranscriptQuery.StartTime, _Mapping]] = ..., delete_time: _Optional[_Union[TranscriptQuery.DeleteTime, _Mapping]] = ..., phone: _Optional[_Union[TranscriptQuery.Phone, _Mapping]] = ..., channel_type: _Optional[_Union[TranscriptQuery.Channel, _Mapping]] = ..., skills: _Optional[_Union[TranscriptQuery.SkillsQuery, _Mapping]] = ..., agent_response: _Optional[_Union[TranscriptQuery.AgentResponse, _Mapping]] = ...) -> None: ...

class Moment(_message.Message):
    __slots__ = ("time_zone", "interval")
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    interval: _vanalytics_pb2.Interval
    def __init__(self, time_zone: _Optional[str] = ..., interval: _Optional[_Union[_vanalytics_pb2.Interval, str]] = ...) -> None: ...

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

class BulkDeleteTranscriptsRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: TranscriptQuery
    def __init__(self, query: _Optional[_Union[TranscriptQuery, _Mapping]] = ...) -> None: ...

class BulkDeleteTranscriptsResponse(_message.Message):
    __slots__ = ("total",)
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    total: int
    def __init__(self, total: _Optional[int] = ...) -> None: ...

class BulkRestoreTranscriptsRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: TranscriptQuery
    def __init__(self, query: _Optional[_Union[TranscriptQuery, _Mapping]] = ...) -> None: ...

class BulkRestoreTranscriptsResponse(_message.Message):
    __slots__ = ("total",)
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    total: int
    def __init__(self, total: _Optional[int] = ...) -> None: ...

class ListTranscriptGroupNamesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTranscriptGroupNamesResponse(_message.Message):
    __slots__ = ("group_names",)
    GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    group_names: _containers.RepeatedCompositeFieldContainer[TranscriptGroupName]
    def __init__(self, group_names: _Optional[_Iterable[_Union[TranscriptGroupName, _Mapping]]] = ...) -> None: ...

class TranscriptGroupName(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ListAgentResponseValuesRequest(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class ListAgentResponseValuesResponse(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
