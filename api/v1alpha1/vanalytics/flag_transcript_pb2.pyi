from api.v1alpha1.vanalytics import flag_pb2 as _flag_pb2
from api.v1alpha1.vanalytics import transcript_pb2 as _transcript_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlagReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANY: _ClassVar[FlagReviewStatus]
    TODO: _ClassVar[FlagReviewStatus]
    DONE: _ClassVar[FlagReviewStatus]
    NONE: _ClassVar[FlagReviewStatus]
ANY: FlagReviewStatus
TODO: FlagReviewStatus
DONE: FlagReviewStatus
NONE: FlagReviewStatus

class CreateFlagTranscriptRequest(_message.Message):
    __slots__ = ()
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    flag: _flag_pb2.Flag
    def __init__(self, transcript_sids: _Optional[_Iterable[int]] = ..., flag: _Optional[_Union[_flag_pb2.Flag, _Mapping]] = ...) -> None: ...

class CreateFlagTranscriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFlagTranscriptRequest(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SIDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    transcript_sids: _containers.RepeatedScalarFieldContainer[int]
    filter: str
    def __init__(self, org_id: _Optional[str] = ..., transcript_sids: _Optional[_Iterable[int]] = ..., filter: _Optional[str] = ...) -> None: ...

class DeleteFlagTranscriptResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchFlagTranscriptsRequest(_message.Message):
    __slots__ = ()
    class FlagSid(_message.Message):
        __slots__ = ()
        FILTER_FIELD_NUMBER: _ClassVar[int]
        MATCH_FIELD_NUMBER: _ClassVar[int]
        filter: _containers.RepeatedScalarFieldContainer[int]
        match: int
        def __init__(self, filter: _Optional[_Iterable[int]] = ..., match: _Optional[int] = ...) -> None: ...
    class NotifyGroupId(_message.Message):
        __slots__ = ()
        IS_NULL_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        MATCH_FIELD_NUMBER: _ClassVar[int]
        is_null: bool
        filter: _containers.RepeatedScalarFieldContainer[str]
        match: int
        def __init__(self, is_null: _Optional[bool] = ..., filter: _Optional[_Iterable[str]] = ..., match: _Optional[int] = ...) -> None: ...
    class ReviewGroupId(_message.Message):
        __slots__ = ()
        IS_NULL_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        MATCH_FIELD_NUMBER: _ClassVar[int]
        is_null: bool
        filter: _containers.RepeatedScalarFieldContainer[str]
        match: int
        def __init__(self, is_null: _Optional[bool] = ..., filter: _Optional[_Iterable[str]] = ..., match: _Optional[int] = ...) -> None: ...
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_REVIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    START_TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    END_TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    flag_sid: SearchFlagTranscriptsRequest.FlagSid
    flag_review_status: FlagReviewStatus
    notify_group_id: SearchFlagTranscriptsRequest.NotifyGroupId
    review_group_id: SearchFlagTranscriptsRequest.ReviewGroupId
    start_transcript_sid: int
    end_transcript_sid: int
    order_by: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., flag_sid: _Optional[_Union[SearchFlagTranscriptsRequest.FlagSid, _Mapping]] = ..., flag_review_status: _Optional[_Union[FlagReviewStatus, str]] = ..., notify_group_id: _Optional[_Union[SearchFlagTranscriptsRequest.NotifyGroupId, _Mapping]] = ..., review_group_id: _Optional[_Union[SearchFlagTranscriptsRequest.ReviewGroupId, _Mapping]] = ..., start_transcript_sid: _Optional[int] = ..., end_transcript_sid: _Optional[int] = ..., order_by: _Optional[str] = ...) -> None: ...

class SearchFlagTranscriptsResponse(_message.Message):
    __slots__ = ()
    class Hit(_message.Message):
        __slots__ = ()
        class ReviewedEntry(_message.Message):
            __slots__ = ()
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: bool
            def __init__(self, key: _Optional[int] = ..., value: _Optional[bool] = ...) -> None: ...
        TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
        FLAG_SNAPSHOT_SIDS_FIELD_NUMBER: _ClassVar[int]
        REVIEWED_FIELD_NUMBER: _ClassVar[int]
        FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
        transcript: _transcript_pb2.Transcript
        flag_snapshot_sids: _containers.RepeatedScalarFieldContainer[int]
        reviewed: _containers.ScalarMap[int, bool]
        flag_sids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, transcript: _Optional[_Union[_transcript_pb2.Transcript, _Mapping]] = ..., flag_snapshot_sids: _Optional[_Iterable[int]] = ..., reviewed: _Optional[_Mapping[int, bool]] = ..., flag_sids: _Optional[_Iterable[int]] = ...) -> None: ...
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HITS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    hits: _containers.RepeatedCompositeFieldContainer[SearchFlagTranscriptsResponse.Hit]
    total: int
    def __init__(self, next_page_token: _Optional[str] = ..., hits: _Optional[_Iterable[_Union[SearchFlagTranscriptsResponse.Hit, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
