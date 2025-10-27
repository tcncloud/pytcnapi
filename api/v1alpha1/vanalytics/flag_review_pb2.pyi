import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFlagReviewRequest(_message.Message):
    __slots__ = ()
    FLAG_REVIEW_FIELD_NUMBER: _ClassVar[int]
    flag_review: FlagReview
    def __init__(self, flag_review: _Optional[_Union[FlagReview, _Mapping]] = ...) -> None: ...

class BulkCreateFlagReviewRequest(_message.Message):
    __slots__ = ()
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    flag_sid: int
    notes: str
    def __init__(self, flag_sid: _Optional[int] = ..., notes: _Optional[str] = ...) -> None: ...

class BulkCreateFlagReviewResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFlagReviewsRequest(_message.Message):
    __slots__ = ()
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    order_by: str
    page_token: str
    transcript_sid: int
    def __init__(self, page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., transcript_sid: _Optional[int] = ...) -> None: ...

class ListFlagReviewsResponse(_message.Message):
    __slots__ = ()
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    flag_reviews: _containers.RepeatedCompositeFieldContainer[FlagReview]
    def __init__(self, next_page_token: _Optional[str] = ..., flag_reviews: _Optional[_Iterable[_Union[FlagReview, _Mapping]]] = ...) -> None: ...

class FlagReview(_message.Message):
    __slots__ = ()
    FLAG_REVIEW_SID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    FLAG_SNAPSHOT_SID_FIELD_NUMBER: _ClassVar[int]
    flag_review_sid: int
    transcript_sid: int
    flag_sid: int
    create_time: _timestamp_pb2.Timestamp
    notes: str
    flag_snapshot_sid: int
    def __init__(self, flag_review_sid: _Optional[int] = ..., transcript_sid: _Optional[int] = ..., flag_sid: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., flag_snapshot_sid: _Optional[int] = ...) -> None: ...
