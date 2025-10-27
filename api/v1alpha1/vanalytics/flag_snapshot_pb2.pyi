import datetime

from api.v1alpha1.vanalytics import dncl_list_pb2 as _dncl_list_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFlagSnapshotsRequest(_message.Message):
    __slots__ = ()
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_SNAPSHOT_SIDS_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_SID_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    order_by: str
    page_token: str
    flag_snapshot_sids: _containers.RepeatedScalarFieldContainer[int]
    mask: _field_mask_pb2.FieldMask
    transcript_sid: int
    def __init__(self, page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., flag_snapshot_sids: _Optional[_Iterable[int]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., transcript_sid: _Optional[int] = ...) -> None: ...

class ListFlagSnapshotsResponse(_message.Message):
    __slots__ = ()
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAG_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    flag_snapshots: _containers.RepeatedCompositeFieldContainer[FlagSnapshot]
    def __init__(self, next_page_token: _Optional[str] = ..., flag_snapshots: _Optional[_Iterable[_Union[FlagSnapshot, _Mapping]]] = ...) -> None: ...

class FlagSnapshot(_message.Message):
    __slots__ = ()
    class BoolExpr(_message.Message):
        __slots__ = ()
        class Filter(_message.Message):
            __slots__ = ()
            FILTER_SID_FIELD_NUMBER: _ClassVar[int]
            filter_sid: int
            def __init__(self, filter_sid: _Optional[int] = ...) -> None: ...
        AND_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        filter: FlagSnapshot.BoolExpr.Filter
        def __init__(self, filter: _Optional[_Union[FlagSnapshot.BoolExpr.Filter, _Mapping]] = ..., **kwargs) -> None: ...
    FLAG_SNAPSHOT_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MUST_REVIEW_FIELD_NUMBER: _ClassVar[int]
    MUST_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    BOOL_EXPR_FIELD_NUMBER: _ClassVar[int]
    DNCL_LIST_FIELD_NUMBER: _ClassVar[int]
    flag_snapshot_sid: int
    flag_sid: int
    name: str
    review_group_id: str
    notify_group_id: str
    priority: int
    version: int
    create_time: _timestamp_pb2.Timestamp
    must_review: bool
    must_notify: bool
    bool_expr: FlagSnapshot.BoolExpr
    dncl_list: _containers.RepeatedCompositeFieldContainer[_dncl_list_pb2.DnclList]
    def __init__(self, flag_snapshot_sid: _Optional[int] = ..., flag_sid: _Optional[int] = ..., name: _Optional[str] = ..., review_group_id: _Optional[str] = ..., notify_group_id: _Optional[str] = ..., priority: _Optional[int] = ..., version: _Optional[int] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., must_review: _Optional[bool] = ..., must_notify: _Optional[bool] = ..., bool_expr: _Optional[_Union[FlagSnapshot.BoolExpr, _Mapping]] = ..., dncl_list: _Optional[_Iterable[_Union[_dncl_list_pb2.DnclList, _Mapping]]] = ...) -> None: ...
