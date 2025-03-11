from api.commons import acd_pb2 as _acd_pb2
from api.commons import vanalytics_pb2 as _vanalytics_pb2
from api.v1alpha1.vanalytics.aclpb import aclpb_pb2 as _aclpb_pb2
from api.v1alpha1.vanalytics import expr_pb2 as _expr_pb2
from api.v1alpha1.vanalytics import transcript_summary_pb2 as _transcript_summary_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TranscriptReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSCRIPT_REVIEW_STATUS_TODO: _ClassVar[TranscriptReviewStatus]
    TRANSCRIPT_REVIEW_STATUS_DONE: _ClassVar[TranscriptReviewStatus]
    TRANSCRIPT_REVIEW_STATUS_NONE: _ClassVar[TranscriptReviewStatus]
TRANSCRIPT_REVIEW_STATUS_TODO: TranscriptReviewStatus
TRANSCRIPT_REVIEW_STATUS_DONE: TranscriptReviewStatus
TRANSCRIPT_REVIEW_STATUS_NONE: TranscriptReviewStatus

class BulkDeleteTranscriptsRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: SearchRequest
    def __init__(self, query: _Optional[_Union[SearchRequest, _Mapping]] = ...) -> None: ...

class BulkDeleteTranscriptsResponse(_message.Message):
    __slots__ = ("total",)
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    total: int
    def __init__(self, total: _Optional[int] = ...) -> None: ...

class BulkRestoreTranscriptsRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: SearchRequest
    def __init__(self, query: _Optional[_Union[SearchRequest, _Mapping]] = ...) -> None: ...

class BulkRestoreTranscriptsResponse(_message.Message):
    __slots__ = ("total",)
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    total: int
    def __init__(self, total: _Optional[int] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("silence", "talk_time", "agent", "page_size", "sort", "create_time", "talk_over", "terms", "channel", "phrase", "transcript_mask", "transcript_sid", "phone_number", "caller_id", "transcript_sids", "call_start_time", "call_types", "call_sids", "hunt_group_sids", "group_names", "agent_call_log", "where", "time_frame")
    class Phrase(_message.Message):
        __slots__ = ("words", "slop", "in_order", "highlight", "agent", "channel", "position_offset")
        class Word(_message.Message):
            __slots__ = ("value", "fuzziness")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            FUZZINESS_FIELD_NUMBER: _ClassVar[int]
            value: str
            fuzziness: str
            def __init__(self, value: _Optional[str] = ..., fuzziness: _Optional[str] = ...) -> None: ...
        class Highlight(_message.Message):
            __slots__ = ("pre_tags", "post_tags")
            PRE_TAGS_FIELD_NUMBER: _ClassVar[int]
            POST_TAGS_FIELD_NUMBER: _ClassVar[int]
            pre_tags: _containers.RepeatedScalarFieldContainer[str]
            post_tags: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, pre_tags: _Optional[_Iterable[str]] = ..., post_tags: _Optional[_Iterable[str]] = ...) -> None: ...
        WORDS_FIELD_NUMBER: _ClassVar[int]
        SLOP_FIELD_NUMBER: _ClassVar[int]
        IN_ORDER_FIELD_NUMBER: _ClassVar[int]
        HIGHLIGHT_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        POSITION_OFFSET_FIELD_NUMBER: _ClassVar[int]
        words: _containers.RepeatedCompositeFieldContainer[SearchRequest.Phrase.Word]
        slop: int
        in_order: bool
        highlight: SearchRequest.Phrase.Highlight
        agent: SearchRequest.Agent
        channel: int
        position_offset: SearchRequest.PositionOffset
        def __init__(self, words: _Optional[_Iterable[_Union[SearchRequest.Phrase.Word, _Mapping]]] = ..., slop: _Optional[int] = ..., in_order: bool = ..., highlight: _Optional[_Union[SearchRequest.Phrase.Highlight, _Mapping]] = ..., agent: _Optional[_Union[SearchRequest.Agent, _Mapping]] = ..., channel: _Optional[int] = ..., position_offset: _Optional[_Union[SearchRequest.PositionOffset, _Mapping]] = ..., **kwargs) -> None: ...
    class PositionOffset(_message.Message):
        __slots__ = ("start", "stop")
        START_FIELD_NUMBER: _ClassVar[int]
        STOP_FIELD_NUMBER: _ClassVar[int]
        start: _duration_pb2.Duration
        stop: _duration_pb2.Duration
        def __init__(self, start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., stop: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Silence(_message.Message):
        __slots__ = ("duration_total", "duration_max", "occurrence_total", "duration_percentage")
        DURATION_TOTAL_FIELD_NUMBER: _ClassVar[int]
        DURATION_MAX_FIELD_NUMBER: _ClassVar[int]
        OCCURRENCE_TOTAL_FIELD_NUMBER: _ClassVar[int]
        DURATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        duration_total: _expr_pb2.Uint32Expr
        duration_max: _expr_pb2.Uint32Expr
        occurrence_total: _expr_pb2.Uint32Expr
        duration_percentage: _expr_pb2.Uint32Expr
        def __init__(self, duration_total: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., duration_max: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., occurrence_total: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., duration_percentage: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ...) -> None: ...
    class TalkOver(_message.Message):
        __slots__ = ("duration_total", "duration_max", "occurrence_total", "duration_percentage")
        DURATION_TOTAL_FIELD_NUMBER: _ClassVar[int]
        DURATION_MAX_FIELD_NUMBER: _ClassVar[int]
        OCCURRENCE_TOTAL_FIELD_NUMBER: _ClassVar[int]
        DURATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        duration_total: _expr_pb2.Uint32Expr
        duration_max: _expr_pb2.Uint32Expr
        occurrence_total: _expr_pb2.Uint32Expr
        duration_percentage: _expr_pb2.Uint32Expr
        def __init__(self, duration_total: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., duration_max: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., occurrence_total: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., duration_percentage: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ...) -> None: ...
    class Terms(_message.Message):
        __slots__ = ("any", "all", "agent", "channel", "position_offset")
        ANY_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        POSITION_OFFSET_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[str]
        all: _containers.RepeatedScalarFieldContainer[str]
        agent: SearchRequest.Agent
        channel: int
        position_offset: SearchRequest.PositionOffset
        def __init__(self, any: _Optional[_Iterable[str]] = ..., all: _Optional[_Iterable[str]] = ..., agent: _Optional[_Union[SearchRequest.Agent, _Mapping]] = ..., channel: _Optional[int] = ..., position_offset: _Optional[_Union[SearchRequest.PositionOffset, _Mapping]] = ..., **kwargs) -> None: ...
    class Agent(_message.Message):
        __slots__ = ("user_name",)
        class UserName(_message.Message):
            __slots__ = ("any", "all")
            ANY_FIELD_NUMBER: _ClassVar[int]
            ALL_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            all: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ..., all: _Optional[_Iterable[str]] = ...) -> None: ...
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        user_name: SearchRequest.Agent.UserName
        def __init__(self, user_name: _Optional[_Union[SearchRequest.Agent.UserName, _Mapping]] = ...) -> None: ...
    SILENCE_FIELD_NUMBER: _ClassVar[int]
    TALK_TIME_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TALK_OVER_FIELD_NUMBER: _ClassVar[int]
    TERMS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_MASK_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    CALL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    CALL_SIDS_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SIDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_LOG_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    TIME_FRAME_FIELD_NUMBER: _ClassVar[int]
    silence: SearchRequest.Silence
    talk_time: _expr_pb2.Uint32Expr
    agent: SearchRequest.Agent
    page_size: int
    sort: Sort
    create_time: _expr_pb2.TimestampExpr
    talk_over: SearchRequest.TalkOver
    terms: SearchRequest.Terms
    channel: int
    phrase: SearchRequest.Phrase
    transcript_mask: _field_mask_pb2.FieldMask
    transcript_sid: int
    phone_number: str
    caller_id: str
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    call_start_time: _expr_pb2.TimestampExpr
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    call_sids: _containers.RepeatedScalarFieldContainer[int]
    hunt_group_sids: _containers.RepeatedScalarFieldContainer[int]
    group_names: _containers.RepeatedScalarFieldContainer[str]
    agent_call_log: AgentCallLogQuery
    where: SearchQuery
    time_frame: _expr_pb2.Uint32Range
    def __init__(self, silence: _Optional[_Union[SearchRequest.Silence, _Mapping]] = ..., talk_time: _Optional[_Union[_expr_pb2.Uint32Expr, _Mapping]] = ..., agent: _Optional[_Union[SearchRequest.Agent, _Mapping]] = ..., page_size: _Optional[int] = ..., sort: _Optional[_Union[Sort, _Mapping]] = ..., create_time: _Optional[_Union[_expr_pb2.TimestampExpr, _Mapping]] = ..., talk_over: _Optional[_Union[SearchRequest.TalkOver, _Mapping]] = ..., terms: _Optional[_Union[SearchRequest.Terms, _Mapping]] = ..., channel: _Optional[int] = ..., phrase: _Optional[_Union[SearchRequest.Phrase, _Mapping]] = ..., transcript_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., transcript_sid: _Optional[int] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., transcript_sids: _Optional[_Iterable[int]] = ..., call_start_time: _Optional[_Union[_expr_pb2.TimestampExpr, _Mapping]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., call_sids: _Optional[_Iterable[int]] = ..., hunt_group_sids: _Optional[_Iterable[int]] = ..., group_names: _Optional[_Iterable[str]] = ..., agent_call_log: _Optional[_Union[AgentCallLogQuery, _Mapping]] = ..., where: _Optional[_Union[SearchQuery, _Mapping]] = ..., time_frame: _Optional[_Union[_expr_pb2.Uint32Range, _Mapping]] = ...) -> None: ...

class SearchQuery(_message.Message):
    __slots__ = ("transcript_sid", "flag_summary", "audio_time", "delete_time", "results", "agent_response", "agent_call_log", "phone")
    class Phone(_message.Message):
        __slots__ = ("cc", "ndc", "prefix", "city", "iso2", "region_code", "region_name", "time_zone", "type", "utc", "location")
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
        cc: SearchQuery.Cc
        ndc: SearchQuery.Ndc
        prefix: SearchQuery.Prefix
        city: SearchQuery.City
        iso2: SearchQuery.Iso2
        region_code: SearchQuery.RegionCode
        region_name: SearchQuery.RegionName
        time_zone: SearchQuery.TimeZone
        type: SearchQuery.Type
        utc: SearchQuery.Utc
        location: SearchQuery.Location
        def __init__(self, cc: _Optional[_Union[SearchQuery.Cc, _Mapping]] = ..., ndc: _Optional[_Union[SearchQuery.Ndc, _Mapping]] = ..., prefix: _Optional[_Union[SearchQuery.Prefix, _Mapping]] = ..., city: _Optional[_Union[SearchQuery.City, _Mapping]] = ..., iso2: _Optional[_Union[SearchQuery.Iso2, _Mapping]] = ..., region_code: _Optional[_Union[SearchQuery.RegionCode, _Mapping]] = ..., region_name: _Optional[_Union[SearchQuery.RegionName, _Mapping]] = ..., time_zone: _Optional[_Union[SearchQuery.TimeZone, _Mapping]] = ..., type: _Optional[_Union[SearchQuery.Type, _Mapping]] = ..., utc: _Optional[_Union[SearchQuery.Utc, _Mapping]] = ..., location: _Optional[_Union[SearchQuery.Location, _Mapping]] = ...) -> None: ...
    class Cc(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class Ndc(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class Prefix(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class City(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class Iso2(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class RegionCode(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class RegionName(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class TimeZone(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class Type(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class Utc(_message.Message):
        __slots__ = ()
        IN_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
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
        zip_code_proximity: SearchQuery.Location.ZipCodeProximity
        def __init__(self, zip_code_proximity: _Optional[_Union[SearchQuery.Location.ZipCodeProximity, _Mapping]] = ...) -> None: ...
    class AgentCallLog(_message.Message):
        __slots__ = ("call_skills_initial", "call_ended")
        CALL_SKILLS_INITIAL_FIELD_NUMBER: _ClassVar[int]
        CALL_ENDED_FIELD_NUMBER: _ClassVar[int]
        call_skills_initial: SearchQuery.CallSkillsInitial
        call_ended: SearchQuery.CallEnded
        def __init__(self, call_skills_initial: _Optional[_Union[SearchQuery.CallSkillsInitial, _Mapping]] = ..., call_ended: _Optional[_Union[SearchQuery.CallEnded, _Mapping]] = ...) -> None: ...
    class CallEnded(_message.Message):
        __slots__ = ("reasons",)
        REASONS_FIELD_NUMBER: _ClassVar[int]
        reasons: _containers.RepeatedScalarFieldContainer[_acd_pb2.AgentCallLogCallEnded]
        def __init__(self, reasons: _Optional[_Iterable[_Union[_acd_pb2.AgentCallLogCallEnded, str]]] = ...) -> None: ...
    class CallSkillsInitial(_message.Message):
        __slots__ = ("need", "want")
        NEED_FIELD_NUMBER: _ClassVar[int]
        WANT_FIELD_NUMBER: _ClassVar[int]
        need: _containers.RepeatedScalarFieldContainer[str]
        want: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, need: _Optional[_Iterable[str]] = ..., want: _Optional[_Iterable[str]] = ...) -> None: ...
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
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        NUMBERS_FIELD_NUMBER: _ClassVar[int]
        key: SearchQuery.AgentResponse.Key
        values: SearchQuery.AgentResponse.Values
        numbers: SearchQuery.AgentResponse.Numbers
        def __init__(self, key: _Optional[_Union[SearchQuery.AgentResponse.Key, _Mapping]] = ..., values: _Optional[_Union[SearchQuery.AgentResponse.Values, _Mapping]] = ..., numbers: _Optional[_Union[SearchQuery.AgentResponse.Numbers, _Mapping]] = ...) -> None: ...
    class Results(_message.Message):
        __slots__ = ("channel", "agent_user_name", "segments")
        class Channel(_message.Message):
            __slots__ = ("eq",)
            EQ_FIELD_NUMBER: _ClassVar[int]
            eq: int
            def __init__(self, eq: _Optional[int] = ...) -> None: ...
        class AgentUserName(_message.Message):
            __slots__ = ("any", "all")
            ANY_FIELD_NUMBER: _ClassVar[int]
            ALL_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[str]
            all: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, any: _Optional[_Iterable[str]] = ..., all: _Optional[_Iterable[str]] = ...) -> None: ...
        class Segments(_message.Message):
            __slots__ = ("text",)
            class Text(_message.Message):
                __slots__ = ("phrase",)
                class Phrase(_message.Message):
                    __slots__ = ("words", "slop", "in_order")
                    class Word(_message.Message):
                        __slots__ = ("value", "fuzziness")
                        VALUE_FIELD_NUMBER: _ClassVar[int]
                        FUZZINESS_FIELD_NUMBER: _ClassVar[int]
                        value: str
                        fuzziness: str
                        def __init__(self, value: _Optional[str] = ..., fuzziness: _Optional[str] = ...) -> None: ...
                    WORDS_FIELD_NUMBER: _ClassVar[int]
                    SLOP_FIELD_NUMBER: _ClassVar[int]
                    IN_ORDER_FIELD_NUMBER: _ClassVar[int]
                    words: _containers.RepeatedCompositeFieldContainer[SearchQuery.Results.Segments.Text.Phrase.Word]
                    slop: int
                    in_order: bool
                    def __init__(self, words: _Optional[_Iterable[_Union[SearchQuery.Results.Segments.Text.Phrase.Word, _Mapping]]] = ..., slop: _Optional[int] = ..., in_order: bool = ...) -> None: ...
                PHRASE_FIELD_NUMBER: _ClassVar[int]
                phrase: SearchQuery.Results.Segments.Text.Phrase
                def __init__(self, phrase: _Optional[_Union[SearchQuery.Results.Segments.Text.Phrase, _Mapping]] = ...) -> None: ...
            TEXT_FIELD_NUMBER: _ClassVar[int]
            text: SearchQuery.Results.Segments.Text
            def __init__(self, text: _Optional[_Union[SearchQuery.Results.Segments.Text, _Mapping]] = ...) -> None: ...
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        AGENT_USER_NAME_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        channel: SearchQuery.Results.Channel
        agent_user_name: SearchQuery.Results.AgentUserName
        segments: SearchQuery.Results.Segments
        def __init__(self, channel: _Optional[_Union[SearchQuery.Results.Channel, _Mapping]] = ..., agent_user_name: _Optional[_Union[SearchQuery.Results.AgentUserName, _Mapping]] = ..., segments: _Optional[_Union[SearchQuery.Results.Segments, _Mapping]] = ...) -> None: ...
    class DeleteTime(_message.Message):
        __slots__ = ("exists",)
        EXISTS_FIELD_NUMBER: _ClassVar[int]
        exists: _wrappers_pb2.BoolValue
        def __init__(self, exists: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class TranscriptSid(_message.Message):
        __slots__ = ("any", "gte")
        ANY_FIELD_NUMBER: _ClassVar[int]
        GTE_FIELD_NUMBER: _ClassVar[int]
        any: _containers.RepeatedScalarFieldContainer[int]
        gte: _wrappers_pb2.Int64Value
        def __init__(self, any: _Optional[_Iterable[int]] = ..., gte: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
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
            flag_sids: SearchQuery.FlagSummary.NeedReview.FlagSids
            def __init__(self, flag_sids: _Optional[_Union[SearchQuery.FlagSummary.NeedReview.FlagSids, _Mapping]] = ...) -> None: ...
        class ReviewStatus(_message.Message):
            __slots__ = ("any",)
            ANY_FIELD_NUMBER: _ClassVar[int]
            any: _containers.RepeatedScalarFieldContainer[TranscriptReviewStatus]
            def __init__(self, any: _Optional[_Iterable[_Union[TranscriptReviewStatus, str]]] = ...) -> None: ...
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
            flag_sid: SearchQuery.FlagSummary.Flags.FlagSid
            def __init__(self, flag_sid: _Optional[_Union[SearchQuery.FlagSummary.Flags.FlagSid, _Mapping]] = ...) -> None: ...
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
        need_review: SearchQuery.FlagSummary.NeedReview
        review_status: SearchQuery.FlagSummary.ReviewStatus
        flags: SearchQuery.FlagSummary.Flags
        count: SearchQuery.FlagSummary.Count
        def __init__(self, need_review: _Optional[_Union[SearchQuery.FlagSummary.NeedReview, _Mapping]] = ..., review_status: _Optional[_Union[SearchQuery.FlagSummary.ReviewStatus, _Mapping]] = ..., flags: _Optional[_Union[SearchQuery.FlagSummary.Flags, _Mapping]] = ..., count: _Optional[_Union[SearchQuery.FlagSummary.Count, _Mapping]] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    OR_FIELD_NUMBER: _ClassVar[int]
    AND_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOT_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_LOG_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: SearchQuery.TranscriptSid
    flag_summary: SearchQuery.FlagSummary
    audio_time: SearchQuery.AudioTime
    delete_time: SearchQuery.DeleteTime
    results: SearchQuery.Results
    agent_response: SearchQuery.AgentResponse
    agent_call_log: SearchQuery.AgentCallLog
    phone: SearchQuery.Phone
    def __init__(self, transcript_sid: _Optional[_Union[SearchQuery.TranscriptSid, _Mapping]] = ..., flag_summary: _Optional[_Union[SearchQuery.FlagSummary, _Mapping]] = ..., audio_time: _Optional[_Union[SearchQuery.AudioTime, _Mapping]] = ..., delete_time: _Optional[_Union[SearchQuery.DeleteTime, _Mapping]] = ..., results: _Optional[_Union[SearchQuery.Results, _Mapping]] = ..., agent_response: _Optional[_Union[SearchQuery.AgentResponse, _Mapping]] = ..., agent_call_log: _Optional[_Union[SearchQuery.AgentCallLog, _Mapping]] = ..., phone: _Optional[_Union[SearchQuery.Phone, _Mapping]] = ..., **kwargs) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("total", "hits", "sort")
    class Hit(_message.Message):
        __slots__ = ("transcript",)
        TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
        transcript: Transcript
        def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    total: int
    hits: _containers.RepeatedCompositeFieldContainer[SearchResponse.Hit]
    sort: Sort
    def __init__(self, total: _Optional[int] = ..., hits: _Optional[_Iterable[_Union[SearchResponse.Hit, _Mapping]]] = ..., sort: _Optional[_Union[Sort, _Mapping]] = ...) -> None: ...

class AgentCallLogQuery(_message.Message):
    __slots__ = ("call_skills_initial",)
    CALL_SKILLS_INITIAL_FIELD_NUMBER: _ClassVar[int]
    call_skills_initial: CallSkillsInitialQuery
    def __init__(self, call_skills_initial: _Optional[_Union[CallSkillsInitialQuery, _Mapping]] = ...) -> None: ...

class CallSkillsInitialQuery(_message.Message):
    __slots__ = ("need", "want")
    NEED_FIELD_NUMBER: _ClassVar[int]
    WANT_FIELD_NUMBER: _ClassVar[int]
    need: _containers.RepeatedCompositeFieldContainer[VanaTermsQuery]
    want: _containers.RepeatedCompositeFieldContainer[VanaTermsQuery]
    def __init__(self, need: _Optional[_Iterable[_Union[VanaTermsQuery, _Mapping]]] = ..., want: _Optional[_Iterable[_Union[VanaTermsQuery, _Mapping]]] = ...) -> None: ...

class VanaTermsQuery(_message.Message):
    __slots__ = ("terms", "lacks", "all")
    TERMS_FIELD_NUMBER: _ClassVar[int]
    LACKS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    terms: _containers.RepeatedScalarFieldContainer[str]
    lacks: bool
    all: bool
    def __init__(self, terms: _Optional[_Iterable[str]] = ..., lacks: bool = ..., all: bool = ...) -> None: ...

class Sort(_message.Message):
    __slots__ = ("fields", "after")
    class Field(_message.Message):
        __slots__ = ("name", "desc")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        name: str
        desc: bool
        def __init__(self, name: _Optional[str] = ..., desc: bool = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Sort.Field]
    after: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fields: _Optional[_Iterable[_Union[Sort.Field, _Mapping]]] = ..., after: _Optional[_Iterable[str]] = ...) -> None: ...

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

class Transcript(_message.Message):
    __slots__ = ("transcript_sid", "call_sid", "call_type", "results", "silence", "talk_time", "create_time", "call_start_time", "talk_over", "caller_id", "phone_number", "audio_time", "audio_bytes", "group_name", "agent_call_log", "flag_summary", "delete_time", "number_format", "agent_response", "summary")
    class AgentResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AgentResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AgentResponse, _Mapping]] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_FIELD_NUMBER: _ClassVar[int]
    TALK_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CALL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TALK_OVER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BYTES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALL_LOG_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    results: _containers.RepeatedCompositeFieldContainer[Result]
    silence: Silence
    talk_time: int
    create_time: _timestamp_pb2.Timestamp
    call_start_time: _timestamp_pb2.Timestamp
    talk_over: TalkOver
    caller_id: str
    phone_number: str
    audio_time: int
    audio_bytes: int
    group_name: str
    agent_call_log: _aclpb_pb2.AgentCallLog
    flag_summary: FlagSummary
    delete_time: _timestamp_pb2.Timestamp
    number_format: str
    agent_response: _containers.MessageMap[str, AgentResponse]
    summary: _transcript_summary_pb2.TranscriptSummary
    def __init__(self, transcript_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ..., silence: _Optional[_Union[Silence, _Mapping]] = ..., talk_time: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., call_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., talk_over: _Optional[_Union[TalkOver, _Mapping]] = ..., caller_id: _Optional[str] = ..., phone_number: _Optional[str] = ..., audio_time: _Optional[int] = ..., audio_bytes: _Optional[int] = ..., group_name: _Optional[str] = ..., agent_call_log: _Optional[_Union[_aclpb_pb2.AgentCallLog, _Mapping]] = ..., flag_summary: _Optional[_Union[FlagSummary, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., number_format: _Optional[str] = ..., agent_response: _Optional[_Mapping[str, AgentResponse]] = ..., summary: _Optional[_Union[_transcript_summary_pb2.TranscriptSummary, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("channel", "segments", "agent_first_name", "agent_last_name", "agent_user_name", "begin_time", "duration", "text", "hunt_group_sid", "sentiment")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    channel: int
    segments: _containers.RepeatedCompositeFieldContainer[Segment]
    agent_first_name: str
    agent_last_name: str
    agent_user_name: str
    begin_time: int
    duration: int
    text: str
    hunt_group_sid: int
    sentiment: Sentiment
    def __init__(self, channel: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Segment, _Mapping]]] = ..., agent_first_name: _Optional[str] = ..., agent_last_name: _Optional[str] = ..., agent_user_name: _Optional[str] = ..., begin_time: _Optional[int] = ..., duration: _Optional[int] = ..., text: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., sentiment: _Optional[_Union[Sentiment, _Mapping]] = ...) -> None: ...

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

class Segment(_message.Message):
    __slots__ = ("begin_time", "confidence", "duration", "text", "words")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    confidence: int
    duration: int
    text: str
    words: _containers.RepeatedCompositeFieldContainer[Word]
    def __init__(self, begin_time: _Optional[int] = ..., confidence: _Optional[int] = ..., duration: _Optional[int] = ..., text: _Optional[str] = ..., words: _Optional[_Iterable[_Union[Word, _Mapping]]] = ...) -> None: ...

class Word(_message.Message):
    __slots__ = ("begin_time", "confidence", "duration", "spoken", "redacted")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SPOKEN_FIELD_NUMBER: _ClassVar[int]
    REDACTED_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    confidence: int
    duration: int
    spoken: str
    redacted: bool
    def __init__(self, begin_time: _Optional[int] = ..., confidence: _Optional[int] = ..., duration: _Optional[int] = ..., spoken: _Optional[str] = ..., redacted: bool = ...) -> None: ...

class Silence(_message.Message):
    __slots__ = ("duration", "segments", "occurrence", "threshold")
    class Duration(_message.Message):
        __slots__ = ("total", "max", "percentage")
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        total: int
        max: int
        percentage: int
        def __init__(self, total: _Optional[int] = ..., max: _Optional[int] = ..., percentage: _Optional[int] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("begin_time", "duration")
        BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        begin_time: int
        duration: int
        def __init__(self, begin_time: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...
    class Occurrence(_message.Message):
        __slots__ = ("total",)
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        total: int
        def __init__(self, total: _Optional[int] = ...) -> None: ...
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    duration: Silence.Duration
    segments: _containers.RepeatedCompositeFieldContainer[Silence.Segment]
    occurrence: Silence.Occurrence
    threshold: int
    def __init__(self, duration: _Optional[_Union[Silence.Duration, _Mapping]] = ..., segments: _Optional[_Iterable[_Union[Silence.Segment, _Mapping]]] = ..., occurrence: _Optional[_Union[Silence.Occurrence, _Mapping]] = ..., threshold: _Optional[int] = ...) -> None: ...

class TalkOver(_message.Message):
    __slots__ = ("occurrence", "duration", "results", "threshold")
    class Duration(_message.Message):
        __slots__ = ("total", "max", "percentage")
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        total: int
        max: int
        percentage: int
        def __init__(self, total: _Optional[int] = ..., max: _Optional[int] = ..., percentage: _Optional[int] = ...) -> None: ...
    class Result(_message.Message):
        __slots__ = ("channel", "occurrence", "duration", "segments", "agent_user_name", "agent_session_sid")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        AGENT_USER_NAME_FIELD_NUMBER: _ClassVar[int]
        AGENT_SESSION_SID_FIELD_NUMBER: _ClassVar[int]
        channel: int
        occurrence: TalkOver.Occurrence
        duration: TalkOver.Duration
        segments: _containers.RepeatedCompositeFieldContainer[TalkOver.Segment]
        agent_user_name: str
        agent_session_sid: int
        def __init__(self, channel: _Optional[int] = ..., occurrence: _Optional[_Union[TalkOver.Occurrence, _Mapping]] = ..., duration: _Optional[_Union[TalkOver.Duration, _Mapping]] = ..., segments: _Optional[_Iterable[_Union[TalkOver.Segment, _Mapping]]] = ..., agent_user_name: _Optional[str] = ..., agent_session_sid: _Optional[int] = ...) -> None: ...
    class Segment(_message.Message):
        __slots__ = ("begin_time", "duration")
        BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        begin_time: int
        duration: int
        def __init__(self, begin_time: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...
    class Occurrence(_message.Message):
        __slots__ = ("total",)
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        total: int
        def __init__(self, total: _Optional[int] = ...) -> None: ...
    OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    occurrence: TalkOver.Occurrence
    duration: TalkOver.Duration
    results: _containers.RepeatedCompositeFieldContainer[TalkOver.Result]
    threshold: int
    def __init__(self, occurrence: _Optional[_Union[TalkOver.Occurrence, _Mapping]] = ..., duration: _Optional[_Union[TalkOver.Duration, _Mapping]] = ..., results: _Optional[_Iterable[_Union[TalkOver.Result, _Mapping]]] = ..., threshold: _Optional[int] = ...) -> None: ...

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
    review_status: TranscriptReviewStatus
    def __init__(self, count: _Optional[int] = ..., priority_sum: _Optional[int] = ..., priority_max: _Optional[int] = ..., need_review: _Optional[_Union[FlagSummary.NeedReview, _Mapping]] = ..., flags: _Optional[_Iterable[_Union[FlagSummary.Flag, _Mapping]]] = ..., review_status: _Optional[_Union[TranscriptReviewStatus, str]] = ...) -> None: ...

class AgentResponse(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchByOrgIdRequest(_message.Message):
    __slots__ = ("org_id", "page_size", "sort", "transcript_mask", "flag_summary", "filter")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_MASK_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    page_size: int
    sort: Sort
    transcript_mask: _field_mask_pb2.FieldMask
    flag_summary: SearchQuery.FlagSummary
    filter: str
    def __init__(self, org_id: _Optional[str] = ..., page_size: _Optional[int] = ..., sort: _Optional[_Union[Sort, _Mapping]] = ..., transcript_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., flag_summary: _Optional[_Union[SearchQuery.FlagSummary, _Mapping]] = ..., filter: _Optional[str] = ...) -> None: ...
