from api.commons import acd_pb2 as _acd_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VanaFlagEvent(_message.Message):
    __slots__ = ("flag_name", "flag_sid", "url", "num_transcripts", "priority")
    FLAG_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NUM_TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    flag_name: str
    flag_sid: int
    url: str
    num_transcripts: int
    priority: int
    def __init__(self, flag_name: _Optional[str] = ..., flag_sid: _Optional[int] = ..., url: _Optional[str] = ..., num_transcripts: _Optional[int] = ..., priority: _Optional[int] = ...) -> None: ...

class VanaFlagReviewEvent(_message.Message):
    __slots__ = ("flag_name", "flag_sid", "url", "num_transcripts", "priority")
    FLAG_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NUM_TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    flag_name: str
    flag_sid: int
    url: str
    num_transcripts: int
    priority: int
    def __init__(self, flag_name: _Optional[str] = ..., flag_sid: _Optional[int] = ..., url: _Optional[str] = ..., num_transcripts: _Optional[int] = ..., priority: _Optional[int] = ...) -> None: ...

class VanaBillingReportEvent(_message.Message):
    __slots__ = ("start_time", "end_time", "url")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., url: _Optional[str] = ...) -> None: ...

class VanaFlagSummaryEvent(_message.Message):
    __slots__ = ("start_time", "end_time", "flag_summaries")
    class FlagSummary(_message.Message):
        __slots__ = ("transcript_sid", "flag_sids")
        TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
        FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
        transcript_sid: int
        flag_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, transcript_sid: _Optional[int] = ..., flag_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    flag_summaries: _containers.RepeatedCompositeFieldContainer[VanaFlagSummaryEvent.FlagSummary]
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., flag_summaries: _Optional[_Iterable[_Union[VanaFlagSummaryEvent.FlagSummary, _Mapping]]] = ...) -> None: ...

class VanaPhraseCorrectionEvent(_message.Message):
    __slots__ = ("start_offset", "end_offset", "original_text", "proposed_text", "url", "channel")
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    original_text: str
    proposed_text: str
    url: str
    channel: int
    def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., original_text: _Optional[str] = ..., proposed_text: _Optional[str] = ..., url: _Optional[str] = ..., channel: _Optional[int] = ...) -> None: ...

class VanaCreateTranscriptEvent(_message.Message):
    __slots__ = ("transcript_sid", "call", "sms")
    class Call(_message.Message):
        __slots__ = ("call_sid", "call_type", "talk_time", "audio_time")
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        TALK_TIME_FIELD_NUMBER: _ClassVar[int]
        AUDIO_TIME_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        call_type: _acd_pb2.CallType.Enum
        talk_time: _duration_pb2.Duration
        audio_time: _duration_pb2.Duration
        def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., talk_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., audio_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Sms(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    call: VanaCreateTranscriptEvent.Call
    sms: VanaCreateTranscriptEvent.Sms
    def __init__(self, transcript_sid: _Optional[int] = ..., call: _Optional[_Union[VanaCreateTranscriptEvent.Call, _Mapping]] = ..., sms: _Optional[_Union[VanaCreateTranscriptEvent.Sms, _Mapping]] = ...) -> None: ...

class VanaCreateSentimentEvent(_message.Message):
    __slots__ = ("transcript_sid", "call", "sms")
    class Call(_message.Message):
        __slots__ = ("call_sid", "call_type")
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        call_type: _acd_pb2.CallType.Enum
        def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...
    class Sms(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    call: VanaCreateSentimentEvent.Call
    sms: VanaCreateSentimentEvent.Sms
    def __init__(self, transcript_sid: _Optional[int] = ..., call: _Optional[_Union[VanaCreateSentimentEvent.Call, _Mapping]] = ..., sms: _Optional[_Union[VanaCreateSentimentEvent.Sms, _Mapping]] = ...) -> None: ...

class VanaCreateSummaryEvent(_message.Message):
    __slots__ = ("transcript_sid", "call", "sms")
    class Call(_message.Message):
        __slots__ = ("call_sid", "call_type")
        CALL_SID_FIELD_NUMBER: _ClassVar[int]
        CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        call_sid: int
        call_type: _acd_pb2.CallType.Enum
        def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ...) -> None: ...
    class Sms(_message.Message):
        __slots__ = ("conversation_sid",)
        CONVERSATION_SID_FIELD_NUMBER: _ClassVar[int]
        conversation_sid: int
        def __init__(self, conversation_sid: _Optional[int] = ...) -> None: ...
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    transcript_sid: int
    call: VanaCreateSummaryEvent.Call
    sms: VanaCreateSummaryEvent.Sms
    def __init__(self, transcript_sid: _Optional[int] = ..., call: _Optional[_Union[VanaCreateSummaryEvent.Call, _Mapping]] = ..., sms: _Optional[_Union[VanaCreateSummaryEvent.Sms, _Mapping]] = ...) -> None: ...
