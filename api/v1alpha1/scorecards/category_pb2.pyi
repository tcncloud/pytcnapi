import datetime

from api.commons import acd_pb2 as _acd_pb2
from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCategoryRequest(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class CreateCategoryResponse(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class ListCategoriesRequest(_message.Message):
    __slots__ = ()
    class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[ListCategoriesRequest.CategoryType]
        SYSTEM: _ClassVar[ListCategoriesRequest.CategoryType]
        USER: _ClassVar[ListCategoriesRequest.CategoryType]
    ANY: ListCategoriesRequest.CategoryType
    SYSTEM: ListCategoriesRequest.CategoryType
    USER: ListCategoriesRequest.CategoryType
    AUTHOR_IDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILES_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    author_ids: _containers.RepeatedScalarFieldContainer[str]
    skill_profiles: _containers.RepeatedScalarFieldContainer[int]
    call_types: _containers.RepeatedScalarFieldContainer[_acd_pb2.CallType.Enum]
    category_type: ListCategoriesRequest.CategoryType
    def __init__(self, author_ids: _Optional[_Iterable[str]] = ..., skill_profiles: _Optional[_Iterable[int]] = ..., call_types: _Optional[_Iterable[_Union[_acd_pb2.CallType.Enum, str]]] = ..., category_type: _Optional[_Union[ListCategoriesRequest.CategoryType, str]] = ...) -> None: ...

class ListCategoriesResponse(_message.Message):
    __slots__ = ()
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Category]
    def __init__(self, categories: _Optional[_Iterable[_Union[_scorecards_pb2.Category, _Mapping]]] = ...) -> None: ...

class UpdateCategoryRequest(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCategoryResponse(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class DeleteCategoryRequest(_message.Message):
    __slots__ = ()
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    def __init__(self, category_id: _Optional[int] = ...) -> None: ...

class DeleteCategoryResponse(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class GetCategoryRequest(_message.Message):
    __slots__ = ()
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    title: str
    def __init__(self, category_id: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class GetCategoryResponse(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _scorecards_pb2.Category
    def __init__(self, category: _Optional[_Union[_scorecards_pb2.Category, _Mapping]] = ...) -> None: ...

class SampleCallsByCategoryRequest(_message.Message):
    __slots__ = ()
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCORER_MAX_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    scorer_max_evaluations: int
    sample_percentage: int
    agent_user_ids: _containers.RepeatedScalarFieldContainer[str]
    scorecard_id: int
    def __init__(self, category_id: _Optional[int] = ..., start_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scorer_max_evaluations: _Optional[int] = ..., sample_percentage: _Optional[int] = ..., agent_user_ids: _Optional[_Iterable[str]] = ..., scorecard_id: _Optional[int] = ...) -> None: ...

class SampleCallsByCategoryResponse(_message.Message):
    __slots__ = ()
    AGENT_CALLS_FIELD_NUMBER: _ClassVar[int]
    agent_calls: _containers.RepeatedCompositeFieldContainer[SampleAgentCall]
    def __init__(self, agent_calls: _Optional[_Iterable[_Union[SampleAgentCall, _Mapping]]] = ...) -> None: ...

class SampleAgentCall(_message.Message):
    __slots__ = ()
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_START_FIELD_NUMBER: _ClassVar[int]
    CALL_DURATION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_FIELD_NUMBER: _ClassVar[int]
    SILENCE_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    call_start: _timestamp_pb2.Timestamp
    call_duration: _duration_pb2.Duration
    speech: _duration_pb2.Duration
    silence: _duration_pb2.Duration
    agent_user_id: str
    def __init__(self, call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., call_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., call_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., speech: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., silence: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., agent_user_id: _Optional[str] = ...) -> None: ...

class ListCategoriesByOrgIdRequest(_message.Message):
    __slots__ = ()
    class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANY: _ClassVar[ListCategoriesByOrgIdRequest.CategoryType]
        SYSTEM: _ClassVar[ListCategoriesByOrgIdRequest.CategoryType]
        USER: _ClassVar[ListCategoriesByOrgIdRequest.CategoryType]
    ANY: ListCategoriesByOrgIdRequest.CategoryType
    SYSTEM: ListCategoriesByOrgIdRequest.CategoryType
    USER: ListCategoriesByOrgIdRequest.CategoryType
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_IDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_PROFILES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    author_ids: _containers.RepeatedScalarFieldContainer[str]
    skill_profiles: _containers.RepeatedScalarFieldContainer[int]
    category_type: ListCategoriesByOrgIdRequest.CategoryType
    def __init__(self, org_id: _Optional[str] = ..., author_ids: _Optional[_Iterable[str]] = ..., skill_profiles: _Optional[_Iterable[int]] = ..., category_type: _Optional[_Union[ListCategoriesByOrgIdRequest.CategoryType, str]] = ...) -> None: ...
