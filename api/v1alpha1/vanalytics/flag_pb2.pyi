from api.v1alpha1.vanalytics import filter_pb2 as _filter_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFlagRequest(_message.Message):
    __slots__ = ("flag",)
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: Flag
    def __init__(self, flag: _Optional[_Union[Flag, _Mapping]] = ...) -> None: ...

class ListFlagsRequest(_message.Message):
    __slots__ = ("page_size", "order_by", "page_token", "filter_sid", "flag_sids", "read_mask", "names", "priorities", "must_review", "must_notify")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_SIDS_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    PRIORITIES_FIELD_NUMBER: _ClassVar[int]
    MUST_REVIEW_FIELD_NUMBER: _ClassVar[int]
    MUST_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    order_by: str
    page_token: str
    filter_sid: int
    flag_sids: _containers.RepeatedScalarFieldContainer[int]
    read_mask: _field_mask_pb2.FieldMask
    names: _containers.RepeatedScalarFieldContainer[str]
    priorities: _containers.RepeatedScalarFieldContainer[int]
    must_review: _containers.RepeatedScalarFieldContainer[bool]
    must_notify: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, page_size: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., filter_sid: _Optional[int] = ..., flag_sids: _Optional[_Iterable[int]] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ..., priorities: _Optional[_Iterable[int]] = ..., must_review: _Optional[_Iterable[bool]] = ..., must_notify: _Optional[_Iterable[bool]] = ...) -> None: ...

class ListFlagsResponse(_message.Message):
    __slots__ = ("next_page_token", "flags", "total")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    flags: _containers.RepeatedCompositeFieldContainer[Flag]
    total: int
    def __init__(self, next_page_token: _Optional[str] = ..., flags: _Optional[_Iterable[_Union[Flag, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class UpdateFlagRequest(_message.Message):
    __slots__ = ("flag_sid", "flag", "update_mask")
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    flag_sid: int
    flag: Flag
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, flag_sid: _Optional[int] = ..., flag: _Optional[_Union[Flag, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFlagRequest(_message.Message):
    __slots__ = ("flag_sid",)
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    flag_sid: int
    def __init__(self, flag_sid: _Optional[int] = ..., **kwargs) -> None: ...

class DeleteFlagResponse(_message.Message):
    __slots__ = ("flag",)
    FLAG_FIELD_NUMBER: _ClassVar[int]
    flag: Flag
    def __init__(self, flag: _Optional[_Union[Flag, _Mapping]] = ...) -> None: ...

class GetFlagRequest(_message.Message):
    __slots__ = ("name", "flag_sid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    name: str
    flag_sid: int
    def __init__(self, name: _Optional[str] = ..., flag_sid: _Optional[int] = ...) -> None: ...

class Flag(_message.Message):
    __slots__ = ("flag_sid", "name", "review_group_id", "notify_group_id", "priority", "version", "filters", "must_review", "must_notify", "bool_expr")
    class BoolExpr(_message.Message):
        __slots__ = ("filter",)
        class Filter(_message.Message):
            __slots__ = ("filter_sid",)
            FILTER_SID_FIELD_NUMBER: _ClassVar[int]
            filter_sid: int
            def __init__(self, filter_sid: _Optional[int] = ...) -> None: ...
        AND_FIELD_NUMBER: _ClassVar[int]
        OR_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        NOT_FIELD_NUMBER: _ClassVar[int]
        filter: Flag.BoolExpr.Filter
        def __init__(self, filter: _Optional[_Union[Flag.BoolExpr.Filter, _Mapping]] = ..., **kwargs) -> None: ...
    FLAG_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    MUST_REVIEW_FIELD_NUMBER: _ClassVar[int]
    MUST_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    BOOL_EXPR_FIELD_NUMBER: _ClassVar[int]
    flag_sid: int
    name: str
    review_group_id: str
    notify_group_id: str
    priority: int
    version: int
    filters: _containers.RepeatedCompositeFieldContainer[_filter_pb2.Filter]
    must_review: bool
    must_notify: bool
    bool_expr: Flag.BoolExpr
    def __init__(self, flag_sid: _Optional[int] = ..., name: _Optional[str] = ..., review_group_id: _Optional[str] = ..., notify_group_id: _Optional[str] = ..., priority: _Optional[int] = ..., version: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[_filter_pb2.Filter, _Mapping]]] = ..., must_review: bool = ..., must_notify: bool = ..., bool_expr: _Optional[_Union[Flag.BoolExpr, _Mapping]] = ...) -> None: ...
