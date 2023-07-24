from api.commons.auth import user_pb2 as _user_pb2
from api.v0alpha import omniapi_pb2 as _omniapi_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestBotTestStepType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TEST_BOT_TEST_STEP_TYPE_UNSPECIFIED: _ClassVar[TestBotTestStepType]
    TEST_BOT_TEST_STEP_TYPE_OMNICHANNEL_CREATE_PROJECT: _ClassVar[TestBotTestStepType]
    TEST_BOT_TEST_STEP_TYPE_OMNICHANNEL_GET_PROJECT: _ClassVar[TestBotTestStepType]

class TestBotEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TEST_BOT_ENTITY_TYPE_UNSPECIFIED: _ClassVar[TestBotEntityType]
    TEST_BOT_ENTITY_TYPE_USER: _ClassVar[TestBotEntityType]
    TEST_BOT_ENTITY_TYPE_OMNICHANNEL_PROJECT: _ClassVar[TestBotEntityType]
TEST_BOT_TEST_STEP_TYPE_UNSPECIFIED: TestBotTestStepType
TEST_BOT_TEST_STEP_TYPE_OMNICHANNEL_CREATE_PROJECT: TestBotTestStepType
TEST_BOT_TEST_STEP_TYPE_OMNICHANNEL_GET_PROJECT: TestBotTestStepType
TEST_BOT_ENTITY_TYPE_UNSPECIFIED: TestBotEntityType
TEST_BOT_ENTITY_TYPE_USER: TestBotEntityType
TEST_BOT_ENTITY_TYPE_OMNICHANNEL_PROJECT: TestBotEntityType

class TestBotNodeTestStart(_message.Message):
    __slots__ = ["entities"]
    class EntitiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestBotEntity
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestBotEntity, _Mapping]] = ...) -> None: ...
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.MessageMap[str, TestBotEntity]
    def __init__(self, entities: _Optional[_Mapping[str, TestBotEntity]] = ...) -> None: ...

class TestBotNodeTestStep(_message.Message):
    __slots__ = ["should_error", "type", "entity_names"]
    SHOULD_ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    should_error: bool
    type: TestBotTestStepType
    entity_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, should_error: bool = ..., type: _Optional[_Union[TestBotTestStepType, str]] = ..., entity_names: _Optional[_Iterable[str]] = ...) -> None: ...

class TestBotNodeTestEnd(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class TestBotEntity(_message.Message):
    __slots__ = ["type", "atomic", "user", "omnichannel_project"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATOMIC_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_PROJECT_FIELD_NUMBER: _ClassVar[int]
    type: TestBotEntityType
    atomic: bool
    user: _user_pb2.AuthenticatedUser
    omnichannel_project: _omniapi_pb2.Project
    def __init__(self, type: _Optional[_Union[TestBotEntityType, str]] = ..., atomic: bool = ..., user: _Optional[_Union[_user_pb2.AuthenticatedUser, _Mapping]] = ..., omnichannel_project: _Optional[_Union[_omniapi_pb2.Project, _Mapping]] = ...) -> None: ...
