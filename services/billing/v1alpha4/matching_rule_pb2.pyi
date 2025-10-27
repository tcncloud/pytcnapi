from google.protobuf import field_mask_pb2 as _field_mask_pb2
from services.billing.entities.v1alpha4 import rates_pb2 as _rates_pb2
from services.billing.v1alpha4 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMatchingRuleRequest(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    matching_rule: _rates_pb2.MatchingRule
    def __init__(self, matching_rule_id: _Optional[str] = ..., matching_rule: _Optional[_Union[_rates_pb2.MatchingRule, _Mapping]] = ...) -> None: ...

class CreateMatchingRuleResponse(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    def __init__(self, matching_rule_id: _Optional[str] = ...) -> None: ...

class DeleteMatchingRuleRequest(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    def __init__(self, matching_rule_id: _Optional[str] = ...) -> None: ...

class DeleteMatchingRuleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMatchingRuleRequest(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    def __init__(self, matching_rule_id: _Optional[str] = ...) -> None: ...

class GetMatchingRuleResponse(_message.Message):
    __slots__ = ()
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    matching_rule: _rates_pb2.MatchingRule
    def __init__(self, matching_rule: _Optional[_Union[_rates_pb2.MatchingRule, _Mapping]] = ...) -> None: ...

class ListMatchingRulesRequest(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    filter: str
    fields: _field_mask_pb2.FieldMask
    sort: _containers.RepeatedCompositeFieldContainer[_core_pb2.Sort]
    page: _core_pb2.Page
    def __init__(self, matching_rule_id: _Optional[str] = ..., filter: _Optional[str] = ..., fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sort: _Optional[_Iterable[_Union[_core_pb2.Sort, _Mapping]]] = ..., page: _Optional[_Union[_core_pb2.Page, _Mapping]] = ...) -> None: ...

class ListMatchingRulesResponse(_message.Message):
    __slots__ = ()
    MATCHING_RULES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    matching_rules: _containers.RepeatedCompositeFieldContainer[_rates_pb2.MatchingRule]
    token: str
    def __init__(self, matching_rules: _Optional[_Iterable[_Union[_rates_pb2.MatchingRule, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class UpdateMatchingRuleRequest(_message.Message):
    __slots__ = ()
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    matching_rule: _rates_pb2.MatchingRule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, matching_rule_id: _Optional[str] = ..., matching_rule: _Optional[_Union[_rates_pb2.MatchingRule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMatchingRuleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
