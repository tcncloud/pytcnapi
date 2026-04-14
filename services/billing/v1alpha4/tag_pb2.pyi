from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.entities.v1alpha4 import tags_pb2 as _tags_pb2
from services.billing.v1alpha4 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBillingTagRequest(_message.Message):
    __slots__ = ("billing_tag_id", "billing_tag")
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_TAG_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    billing_tag: _tags_pb2.BillingTag
    def __init__(self, billing_tag_id: _Optional[str] = ..., billing_tag: _Optional[_Union[_tags_pb2.BillingTag, _Mapping]] = ...) -> None: ...

class CreateBillingTagResponse(_message.Message):
    __slots__ = ("billing_tag_id",)
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    def __init__(self, billing_tag_id: _Optional[str] = ...) -> None: ...

class DeleteBillingTagRequest(_message.Message):
    __slots__ = ("billing_tag_id",)
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    def __init__(self, billing_tag_id: _Optional[str] = ...) -> None: ...

class DeleteBillingTagResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBillingTagRequest(_message.Message):
    __slots__ = ("billing_tag_id",)
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    def __init__(self, billing_tag_id: _Optional[str] = ...) -> None: ...

class GetBillingTagResponse(_message.Message):
    __slots__ = ("billing_tag",)
    BILLING_TAG_FIELD_NUMBER: _ClassVar[int]
    billing_tag: _tags_pb2.BillingTag
    def __init__(self, billing_tag: _Optional[_Union[_tags_pb2.BillingTag, _Mapping]] = ...) -> None: ...

class ListBillingTagsRequest(_message.Message):
    __slots__ = ("billing_tag_id", "filter", "fields", "sort", "page")
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, billing_tag_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListBillingTagsResponse(_message.Message):
    __slots__ = ("billing_tags", "token")
    BILLING_TAGS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    billing_tags: _containers.RepeatedCompositeFieldContainer[_tags_pb2.BillingTag]
    token: str
    def __init__(self, billing_tags: _Optional[_Iterable[_Union[_tags_pb2.BillingTag, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateBillingTagRequest(_message.Message):
    __slots__ = ("billing_tag_id", "billing_tag", "update_mask")
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_TAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    billing_tag: _tags_pb2.BillingTag
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, billing_tag_id: _Optional[str] = ..., billing_tag: _Optional[_Union[_tags_pb2.BillingTag, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBillingTagResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
