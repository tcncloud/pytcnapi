from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Int32Nullable(_message.Message):
    __slots__ = ["is_null", "value"]
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    value: int
    def __init__(self, is_null: bool = ..., value: _Optional[int] = ...) -> None: ...

class Int64Nullable(_message.Message):
    __slots__ = ["is_null", "value"]
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    value: int
    def __init__(self, is_null: bool = ..., value: _Optional[int] = ...) -> None: ...

class SomeSidAndDateCompare(_message.Message):
    __slots__ = ["some_sid", "date_greater", "date_less"]
    SOME_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_GREATER_FIELD_NUMBER: _ClassVar[int]
    DATE_LESS_FIELD_NUMBER: _ClassVar[int]
    some_sid: int
    date_greater: _timestamp_pb2.Timestamp
    date_less: _timestamp_pb2.Timestamp
    def __init__(self, some_sid: _Optional[int] = ..., date_greater: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_less: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Int64ArraySql(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class Int32ArraySql(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ...) -> None: ...

class StringArraySql(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class BoolArraySql(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, values: _Optional[_Iterable[bool]] = ...) -> None: ...

class Int32ValueArraySql(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    def __init__(self, values: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ...) -> None: ...

class Int64Id(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
