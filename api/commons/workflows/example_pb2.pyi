from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NodePrint(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class NodeRandom(_message.Message):
    __slots__ = ["min", "max", "single_output"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    single_output: bool
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., single_output: bool = ...) -> None: ...

class NodeConsoleInput(_message.Message):
    __slots__ = ["prompt"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...

class NodeStoreInput(_message.Message):
    __slots__ = ["store_to"]
    STORE_TO_FIELD_NUMBER: _ClassVar[int]
    store_to: str
    def __init__(self, store_to: _Optional[str] = ...) -> None: ...

class NodeComparator(_message.Message):
    __slots__ = ["first_field", "second_field"]
    FIRST_FIELD_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_FIELD_NUMBER: _ClassVar[int]
    first_field: str
    second_field: str
    def __init__(self, first_field: _Optional[str] = ..., second_field: _Optional[str] = ...) -> None: ...

class NodeChatbot(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DiceDocument(_message.Message):
    __slots__ = ["dice_value", "dice_value_max", "dice_value_min", "last_message", "variables", "error"]
    class VariablesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DICE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DICE_VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    DICE_VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    dice_value: int
    dice_value_max: int
    dice_value_min: int
    last_message: str
    variables: _containers.ScalarMap[str, str]
    error: str
    def __init__(self, dice_value: _Optional[int] = ..., dice_value_max: _Optional[int] = ..., dice_value_min: _Optional[int] = ..., last_message: _Optional[str] = ..., variables: _Optional[_Mapping[str, str]] = ..., error: _Optional[str] = ...) -> None: ...

class ChatbotDocument(_message.Message):
    __slots__ = ["in_message", "out_message", "error"]
    IN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    in_message: str
    out_message: str
    error: str
    def __init__(self, in_message: _Optional[str] = ..., out_message: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
