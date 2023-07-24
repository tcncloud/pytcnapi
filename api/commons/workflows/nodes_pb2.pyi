from api.commons.workflows import example_pb2 as _example_pb2
from api.commons.workflows import omni_pb2 as _omni_pb2
from api.commons.workflows import omni_bot_pb2 as _omni_bot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeDefinition(_message.Message):
    __slots__ = ["id", "name", "description", "outputs", "error_node_id", "print", "random", "console_input", "comparator", "store_input", "chatbot", "omni_prompt", "omni_set_skill", "omni_to_agent", "omni_error", "omni_bot_test_start", "omni_bot_test_step", "omni_bot_test_end"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PRINT_FIELD_NUMBER: _ClassVar[int]
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_INPUT_FIELD_NUMBER: _ClassVar[int]
    COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    STORE_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHATBOT_FIELD_NUMBER: _ClassVar[int]
    OMNI_PROMPT_FIELD_NUMBER: _ClassVar[int]
    OMNI_SET_SKILL_FIELD_NUMBER: _ClassVar[int]
    OMNI_TO_AGENT_FIELD_NUMBER: _ClassVar[int]
    OMNI_ERROR_FIELD_NUMBER: _ClassVar[int]
    OMNI_BOT_TEST_START_FIELD_NUMBER: _ClassVar[int]
    OMNI_BOT_TEST_STEP_FIELD_NUMBER: _ClassVar[int]
    OMNI_BOT_TEST_END_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    outputs: _containers.RepeatedScalarFieldContainer[str]
    error_node_id: str
    print: _example_pb2.NodePrint
    random: _example_pb2.NodeRandom
    console_input: _example_pb2.NodeConsoleInput
    comparator: _example_pb2.NodeComparator
    store_input: _example_pb2.NodeStoreInput
    chatbot: _example_pb2.NodeChatbot
    omni_prompt: _omni_pb2.OmniNodePrompt
    omni_set_skill: _omni_pb2.OmniNodeSetSkill
    omni_to_agent: _omni_pb2.OmniNodeToAgent
    omni_error: _omni_pb2.OmniNodeError
    omni_bot_test_start: _omni_bot_pb2.OmniBotNodeTestStart
    omni_bot_test_step: _omni_bot_pb2.OmniBotNodeTestStep
    omni_bot_test_end: _omni_bot_pb2.OmniBotNodeTestEnd
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., outputs: _Optional[_Iterable[str]] = ..., error_node_id: _Optional[str] = ..., print: _Optional[_Union[_example_pb2.NodePrint, _Mapping]] = ..., random: _Optional[_Union[_example_pb2.NodeRandom, _Mapping]] = ..., console_input: _Optional[_Union[_example_pb2.NodeConsoleInput, _Mapping]] = ..., comparator: _Optional[_Union[_example_pb2.NodeComparator, _Mapping]] = ..., store_input: _Optional[_Union[_example_pb2.NodeStoreInput, _Mapping]] = ..., chatbot: _Optional[_Union[_example_pb2.NodeChatbot, _Mapping]] = ..., omni_prompt: _Optional[_Union[_omni_pb2.OmniNodePrompt, _Mapping]] = ..., omni_set_skill: _Optional[_Union[_omni_pb2.OmniNodeSetSkill, _Mapping]] = ..., omni_to_agent: _Optional[_Union[_omni_pb2.OmniNodeToAgent, _Mapping]] = ..., omni_error: _Optional[_Union[_omni_pb2.OmniNodeError, _Mapping]] = ..., omni_bot_test_start: _Optional[_Union[_omni_bot_pb2.OmniBotNodeTestStart, _Mapping]] = ..., omni_bot_test_step: _Optional[_Union[_omni_bot_pb2.OmniBotNodeTestStep, _Mapping]] = ..., omni_bot_test_end: _Optional[_Union[_omni_bot_pb2.OmniBotNodeTestEnd, _Mapping]] = ...) -> None: ...
