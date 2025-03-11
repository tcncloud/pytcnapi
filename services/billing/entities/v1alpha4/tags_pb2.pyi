from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATEGORY_UNSPECIFIED: _ClassVar[Category]
    CATEGORY_COMMUNICATIONS_OMNI_CHAT: _ClassVar[Category]
    CATEGORY_COMMUNICATIONS_OMNI_EMAIL: _ClassVar[Category]
    CATEGORY_COMMUNICATIONS_OMNI_SMS: _ClassVar[Category]
    CATEGORY_COMMUNICATIONS_OMNI_AGENT: _ClassVar[Category]
    CATEGORY_COMMUNICATIONS_OMNI_RESOURCES: _ClassVar[Category]
    CATEGORY_DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE: _ClassVar[Category]
    CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_VOICE_ANALYTICS: _ClassVar[Category]
    CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_AI_BUNDLE: _ClassVar[Category]
    CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_MANAGEMENT_SCHEDULER: _ClassVar[Category]
CATEGORY_UNSPECIFIED: Category
CATEGORY_COMMUNICATIONS_OMNI_CHAT: Category
CATEGORY_COMMUNICATIONS_OMNI_EMAIL: Category
CATEGORY_COMMUNICATIONS_OMNI_SMS: Category
CATEGORY_COMMUNICATIONS_OMNI_AGENT: Category
CATEGORY_COMMUNICATIONS_OMNI_RESOURCES: Category
CATEGORY_DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE: Category
CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_VOICE_ANALYTICS: Category
CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_AI_BUNDLE: Category
CATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_MANAGEMENT_SCHEDULER: Category

class BillingTag(_message.Message):
    __slots__ = ("billing_tag_id", "name", "create_time", "update_time", "delete_time", "category", "billing_category")
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    BILLING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    billing_tag_id: str
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    category: str
    billing_category: Category
    def __init__(self, billing_tag_id: _Optional[str] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., category: _Optional[str] = ..., billing_category: _Optional[_Union[Category, str]] = ...) -> None: ...
