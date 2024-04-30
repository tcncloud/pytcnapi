from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons import communication_pb2 as _communication_pb2
from api.commons import compliance_pb2 as _compliance_pb2
from api.commons import enums_pb2 as _enums_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessOutboundCallReq(_message.Message):
    __slots__ = ("rule_set_name", "country_code", "phone_number", "call_metadata", "source_id", "source_field", "caller_id", "client_sid", "comm_type", "call_type", "org_id", "region_id", "email", "zip_code")
    class CallMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALL_METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    COMM_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    rule_set_name: str
    country_code: str
    phone_number: str
    call_metadata: _containers.ScalarMap[str, str]
    source_id: int
    source_field: str
    caller_id: str
    client_sid: int
    comm_type: _communication_pb2.CommType
    call_type: str
    org_id: str
    region_id: str
    email: str
    zip_code: str
    def __init__(self, rule_set_name: _Optional[str] = ..., country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., call_metadata: _Optional[_Mapping[str, str]] = ..., source_id: _Optional[int] = ..., source_field: _Optional[str] = ..., caller_id: _Optional[str] = ..., client_sid: _Optional[int] = ..., comm_type: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., call_type: _Optional[str] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., email: _Optional[str] = ..., zip_code: _Optional[str] = ...) -> None: ...

class ProcessRes(_message.Message):
    __slots__ = ("permit", "rule_responses")
    PERMIT_FIELD_NUMBER: _ClassVar[int]
    RULE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    permit: bool
    rule_responses: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.RuleResponse]
    def __init__(self, permit: bool = ..., rule_responses: _Optional[_Iterable[_Union[_compliance_pb2.RuleResponse, _Mapping]]] = ...) -> None: ...

class ScrubList(_message.Message):
    __slots__ = ("list_id", "entries")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    entries: _containers.RepeatedCompositeFieldContainer[ScrubEntry]
    def __init__(self, list_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[ScrubEntry, _Mapping]]] = ...) -> None: ...

class CreateScrubListReq(_message.Message):
    __slots__ = ("list_id", "list", "content_type", "country_code", "scrub_entry_details", "durable")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SCRUB_ENTRY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    list: _containers.RepeatedScalarFieldContainer[str]
    content_type: _compliance_pb2.ContentType
    country_code: str
    scrub_entry_details: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ScrubEntryDetails]
    durable: bool
    def __init__(self, list_id: _Optional[str] = ..., list: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., country_code: _Optional[str] = ..., scrub_entry_details: _Optional[_Iterable[_Union[_compliance_pb2.ScrubEntryDetails, _Mapping]]] = ..., durable: bool = ...) -> None: ...

class AddScrubListEntriesReq(_message.Message):
    __slots__ = ("list_id", "list", "content_type", "country_code", "scrub_entry_details")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SCRUB_ENTRY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    list: _containers.RepeatedScalarFieldContainer[str]
    content_type: _compliance_pb2.ContentType
    country_code: str
    scrub_entry_details: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ScrubEntryDetails]
    def __init__(self, list_id: _Optional[str] = ..., list: _Optional[_Iterable[str]] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., country_code: _Optional[str] = ..., scrub_entry_details: _Optional[_Iterable[_Union[_compliance_pb2.ScrubEntryDetails, _Mapping]]] = ...) -> None: ...

class UpdateScrubEntryReq(_message.Message):
    __slots__ = ("list_id", "notes", "content", "expiration_date", "country_code")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    notes: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    expiration_date: _timestamp_pb2.Timestamp
    country_code: _wrappers_pb2.StringValue
    def __init__(self, list_id: _Optional[str] = ..., notes: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., country_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class UpdateScrubEntryRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteScrubListEntriesReq(_message.Message):
    __slots__ = ("list_id", "list")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, list_id: _Optional[str] = ..., list: _Optional[_Iterable[str]] = ...) -> None: ...

class GetScrubListReq(_message.Message):
    __slots__ = ("list_id",)
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    def __init__(self, list_id: _Optional[str] = ...) -> None: ...

class GetScrubListsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScrubListsRes(_message.Message):
    __slots__ = ("lists",)
    LISTS_FIELD_NUMBER: _ClassVar[int]
    lists: _containers.RepeatedCompositeFieldContainer[ScrubListRes]
    def __init__(self, lists: _Optional[_Iterable[_Union[ScrubListRes, _Mapping]]] = ...) -> None: ...

class ScrubListRes(_message.Message):
    __slots__ = ("list_id", "read_only", "content_type", "entries_added", "invalid_entries")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    INVALID_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    read_only: bool
    content_type: _compliance_pb2.ContentType
    entries_added: int
    invalid_entries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, list_id: _Optional[str] = ..., read_only: bool = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., entries_added: _Optional[int] = ..., invalid_entries: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteScrubListReq(_message.Message):
    __slots__ = ("list_id",)
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    def __init__(self, list_id: _Optional[str] = ...) -> None: ...

class SearchScrubListReq(_message.Message):
    __slots__ = ("list_id", "term")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    term: str
    def __init__(self, list_id: _Optional[str] = ..., term: _Optional[str] = ...) -> None: ...

class ScrubEntry(_message.Message):
    __slots__ = ("country_sid", "list_id", "source_id", "source_field", "notes", "content", "expiration_date", "result", "type", "country_code", "created_on", "created_by")
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    country_sid: int
    list_id: str
    source_id: int
    source_field: str
    notes: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    expiration_date: _timestamp_pb2.Timestamp
    result: _wrappers_pb2.StringValue
    type: _compliance_pb2.ContentType
    country_code: _wrappers_pb2.StringValue
    created_on: _timestamp_pb2.Timestamp
    created_by: _wrappers_pb2.StringValue
    def __init__(self, country_sid: _Optional[int] = ..., list_id: _Optional[str] = ..., source_id: _Optional[int] = ..., source_field: _Optional[str] = ..., notes: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., result: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., country_code: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RuleAutoCompleteReq(_message.Message):
    __slots__ = ("phrase", "cursor")
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    phrase: str
    cursor: int
    def __init__(self, phrase: _Optional[str] = ..., cursor: _Optional[int] = ...) -> None: ...

class RuleAutoCompleteRes(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, options: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckRuleSetReq(_message.Message):
    __slots__ = ("phrase",)
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    phrase: str
    def __init__(self, phrase: _Optional[str] = ...) -> None: ...

class CheckRuleSetRes(_message.Message):
    __slots__ = ("rules", "warnings")
    RULES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.Rule]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rules: _Optional[_Iterable[_Union[_compliance_pb2.Rule, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class ListRuleSetsReq(_message.Message):
    __slots__ = ("include_disabled",)
    INCLUDE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    include_disabled: bool
    def __init__(self, include_disabled: bool = ...) -> None: ...

class ListRuleSetsRes(_message.Message):
    __slots__ = ("rule_set_id", "name", "rule_count", "disabled")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    name: str
    rule_count: int
    disabled: bool
    def __init__(self, rule_set_id: _Optional[str] = ..., name: _Optional[str] = ..., rule_count: _Optional[int] = ..., disabled: bool = ...) -> None: ...

class GetRuleSetReq(_message.Message):
    __slots__ = ("rule_set_id", "rule_set_sha")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_SHA_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    rule_set_sha: str
    def __init__(self, rule_set_id: _Optional[str] = ..., rule_set_sha: _Optional[str] = ...) -> None: ...

class GetRuleSetByNameReq(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AssignRuleSetReq(_message.Message):
    __slots__ = ("comm_type", "comm_id", "rule_set_id")
    COMM_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMM_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    comm_type: _communication_pb2.CommType
    comm_id: str
    rule_set_id: str
    def __init__(self, comm_type: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., comm_id: _Optional[str] = ..., rule_set_id: _Optional[str] = ...) -> None: ...

class AssignRuleSetRes(_message.Message):
    __slots__ = ("cpl_rule_set_assignment_id",)
    CPL_RULE_SET_ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_assignment_id: str
    def __init__(self, cpl_rule_set_assignment_id: _Optional[str] = ...) -> None: ...

class RenameRuleSetReq(_message.Message):
    __slots__ = ("rule_set_id", "name")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    name: str
    def __init__(self, rule_set_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RenameRuleSetRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateRuleSetReq(_message.Message):
    __slots__ = ("rule_set_id", "name", "rules_text", "rules")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULES_TEXT_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    name: str
    rules_text: str
    rules: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.Rule]
    def __init__(self, rule_set_id: _Optional[str] = ..., name: _Optional[str] = ..., rules_text: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[_compliance_pb2.Rule, _Mapping]]] = ...) -> None: ...

class EnableRuleSetReq(_message.Message):
    __slots__ = ("rule_set_id", "rule_set_sha")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_SHA_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    rule_set_sha: str
    def __init__(self, rule_set_id: _Optional[str] = ..., rule_set_sha: _Optional[str] = ...) -> None: ...

class DisableRuleSetReq(_message.Message):
    __slots__ = ("rule_set_id", "rule_set_sha")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_SHA_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    rule_set_sha: str
    def __init__(self, rule_set_id: _Optional[str] = ..., rule_set_sha: _Optional[str] = ...) -> None: ...

class EnableRuleSetRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableRuleSetRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EvaluationResults(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RuleSet(_message.Message):
    __slots__ = ("rule_set_id", "name", "head", "disabled", "rules_text", "sha", "rules")
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    RULES_TEXT_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    name: str
    head: bool
    disabled: bool
    rules_text: str
    sha: str
    rules: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.Rule]
    def __init__(self, rule_set_id: _Optional[str] = ..., name: _Optional[str] = ..., head: bool = ..., disabled: bool = ..., rules_text: _Optional[str] = ..., sha: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[_compliance_pb2.Rule, _Mapping]]] = ...) -> None: ...

class GetDefaultRulesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultRulesRes(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rules: _Optional[_Iterable[str]] = ...) -> None: ...

class GetScrubListUploadUrlReq(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetScrubListUploadUrlRes(_message.Message):
    __slots__ = ("url", "filename", "bucket")
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    url: str
    filename: str
    bucket: str
    def __init__(self, url: _Optional[str] = ..., filename: _Optional[str] = ..., bucket: _Optional[str] = ...) -> None: ...

class ProcessScrubListUploadReq(_message.Message):
    __slots__ = ("filename", "list_id", "content_type", "notification_message", "country_code")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    list_id: str
    content_type: _compliance_pb2.ContentType
    notification_message: str
    country_code: str
    def __init__(self, filename: _Optional[str] = ..., list_id: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., notification_message: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

class ProcessScrubListUploadRes(_message.Message):
    __slots__ = ("entries_added", "invalid_entries")
    ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    INVALID_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries_added: int
    invalid_entries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entries_added: _Optional[int] = ..., invalid_entries: _Optional[_Iterable[str]] = ...) -> None: ...

class ProcessScrubListDeleteUploadReq(_message.Message):
    __slots__ = ("list_id", "filename", "notification_message")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    filename: str
    notification_message: str
    def __init__(self, list_id: _Optional[str] = ..., filename: _Optional[str] = ..., notification_message: _Optional[str] = ...) -> None: ...

class ProcessScrubListDeleteUploadRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportScrubListReq(_message.Message):
    __slots__ = ("list_id",)
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    def __init__(self, list_id: _Optional[str] = ...) -> None: ...

class ExportScrubListRes(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class Scenario(_message.Message):
    __slots__ = ("cpl_scenario_id", "should_allow", "should_deny", "last_execution_result", "name")
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ALLOW_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DENY_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cpl_scenario_id: int
    should_allow: _compliance_pb2.ScenarioData
    should_deny: _compliance_pb2.ScenarioData
    last_execution_result: _compliance_pb2.ScenarioResult
    name: str
    def __init__(self, cpl_scenario_id: _Optional[int] = ..., should_allow: _Optional[_Union[_compliance_pb2.ScenarioData, _Mapping]] = ..., should_deny: _Optional[_Union[_compliance_pb2.ScenarioData, _Mapping]] = ..., last_execution_result: _Optional[_Union[_compliance_pb2.ScenarioResult, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class CreateScenarioReq(_message.Message):
    __slots__ = ("should_allow", "should_deny", "name")
    SHOULD_ALLOW_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DENY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    should_allow: _compliance_pb2.ScenarioData
    should_deny: _compliance_pb2.ScenarioData
    name: str
    def __init__(self, should_allow: _Optional[_Union[_compliance_pb2.ScenarioData, _Mapping]] = ..., should_deny: _Optional[_Union[_compliance_pb2.ScenarioData, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class CreateScenarioRes(_message.Message):
    __slots__ = ("scenario",)
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    scenario: Scenario
    def __init__(self, scenario: _Optional[_Union[Scenario, _Mapping]] = ...) -> None: ...

class GetScenarioReq(_message.Message):
    __slots__ = ("cpl_scenario_id",)
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_scenario_id: int
    def __init__(self, cpl_scenario_id: _Optional[int] = ...) -> None: ...

class GetScenarioRes(_message.Message):
    __slots__ = ("scenario",)
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    scenario: Scenario
    def __init__(self, scenario: _Optional[_Union[Scenario, _Mapping]] = ...) -> None: ...

class UpdateScenarioReq(_message.Message):
    __slots__ = ("scenario",)
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    scenario: Scenario
    def __init__(self, scenario: _Optional[_Union[Scenario, _Mapping]] = ...) -> None: ...

class UpdateScenarioRes(_message.Message):
    __slots__ = ("scenario",)
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    scenario: Scenario
    def __init__(self, scenario: _Optional[_Union[Scenario, _Mapping]] = ...) -> None: ...

class DeleteScenarioReq(_message.Message):
    __slots__ = ("cpl_scenario_id",)
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_scenario_id: int
    def __init__(self, cpl_scenario_id: _Optional[int] = ...) -> None: ...

class DeleteScenarioRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RunAssignedScenariosReq(_message.Message):
    __slots__ = ("cpl_rule_set_id",)
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    def __init__(self, cpl_rule_set_id: _Optional[str] = ...) -> None: ...

class RunAssignedScenariosRes(_message.Message):
    __slots__ = ("results", "passed_value", "cpl_rule_set_name")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PASSED_VALUE_FIELD_NUMBER: _ClassVar[int]
    CPL_RULE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ScenarioResult]
    passed_value: bool
    cpl_rule_set_name: str
    def __init__(self, results: _Optional[_Iterable[_Union[_compliance_pb2.ScenarioResult, _Mapping]]] = ..., passed_value: bool = ..., cpl_rule_set_name: _Optional[str] = ...) -> None: ...

class ListAllScenariosReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAllScenariosRes(_message.Message):
    __slots__ = ("scenarios",)
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    scenarios: _containers.RepeatedCompositeFieldContainer[Scenario]
    def __init__(self, scenarios: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ...) -> None: ...

class ListAssignedRuleSetsReq(_message.Message):
    __slots__ = ("cpl_scenario_id",)
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_scenario_id: int
    def __init__(self, cpl_scenario_id: _Optional[int] = ...) -> None: ...

class ListAssignedRuleSetsRes(_message.Message):
    __slots__ = ("rule_sets",)
    RULE_SETS_FIELD_NUMBER: _ClassVar[int]
    rule_sets: _containers.RepeatedCompositeFieldContainer[RuleSet]
    def __init__(self, rule_sets: _Optional[_Iterable[_Union[RuleSet, _Mapping]]] = ...) -> None: ...

class ListAssignedScenariosReq(_message.Message):
    __slots__ = ("cpl_rule_set_id",)
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    def __init__(self, cpl_rule_set_id: _Optional[str] = ...) -> None: ...

class AssignedScenario(_message.Message):
    __slots__ = ("scenario", "enabled", "last_execution_result")
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    scenario: Scenario
    enabled: bool
    last_execution_result: _compliance_pb2.ScenarioResult
    def __init__(self, scenario: _Optional[_Union[Scenario, _Mapping]] = ..., enabled: bool = ..., last_execution_result: _Optional[_Union[_compliance_pb2.ScenarioResult, _Mapping]] = ...) -> None: ...

class ListAssignedScenariosRes(_message.Message):
    __slots__ = ("assigned_scenarios",)
    ASSIGNED_SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    assigned_scenarios: _containers.RepeatedCompositeFieldContainer[AssignedScenario]
    def __init__(self, assigned_scenarios: _Optional[_Iterable[_Union[AssignedScenario, _Mapping]]] = ...) -> None: ...

class ListUnassignedScenariosReq(_message.Message):
    __slots__ = ("cpl_rule_set_id",)
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    def __init__(self, cpl_rule_set_id: _Optional[str] = ...) -> None: ...

class ListUnassignedScenariosRes(_message.Message):
    __slots__ = ("scenarios",)
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    scenarios: _containers.RepeatedCompositeFieldContainer[Scenario]
    def __init__(self, scenarios: _Optional[_Iterable[_Union[Scenario, _Mapping]]] = ...) -> None: ...

class AssignScenarioReq(_message.Message):
    __slots__ = ("cpl_rule_set_id", "cpl_scenario_id")
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    cpl_scenario_id: int
    def __init__(self, cpl_rule_set_id: _Optional[str] = ..., cpl_scenario_id: _Optional[int] = ...) -> None: ...

class UnassignScenarioReq(_message.Message):
    __slots__ = ("cpl_rule_set_id", "cpl_scenario_id")
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    cpl_scenario_id: int
    def __init__(self, cpl_rule_set_id: _Optional[str] = ..., cpl_scenario_id: _Optional[int] = ...) -> None: ...

class EnableScenarioReq(_message.Message):
    __slots__ = ("cpl_rule_set_id", "cpl_scenario_id")
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    cpl_scenario_id: int
    def __init__(self, cpl_rule_set_id: _Optional[str] = ..., cpl_scenario_id: _Optional[int] = ...) -> None: ...

class DisableScenarioReq(_message.Message):
    __slots__ = ("cpl_rule_set_id", "cpl_scenario_id")
    CPL_RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    CPL_SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    cpl_rule_set_id: str
    cpl_scenario_id: int
    def __init__(self, cpl_rule_set_id: _Optional[str] = ..., cpl_scenario_id: _Optional[int] = ...) -> None: ...

class CreateConsentProfileReq(_message.Message):
    __slots__ = ("consent_profile_id", "profile_name", "disabled", "channel", "created_by")
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    profile_name: str
    disabled: bool
    channel: _communication_pb2.CommType
    created_by: str
    def __init__(self, consent_profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., disabled: bool = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

class CreateConsentProfileRes(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class GetConsentReq(_message.Message):
    __slots__ = ("consent_id",)
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    def __init__(self, consent_id: _Optional[int] = ...) -> None: ...

class CreateConsentReq(_message.Message):
    __slots__ = ("consent_profile_id", "content", "recorded", "expire", "referring_url", "channel", "topic", "revoked_reason", "granted_reason", "proof", "condition_days_of_the_week", "condition_time_of_day_from", "condition_time_of_day_to", "condition_from", "condition_to", "notes", "conditions", "content_type", "channel_type")
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECORDED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    REFERRING_URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    GRANTED_REASON_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    content: str
    recorded: _timestamp_pb2.Timestamp
    expire: _timestamp_pb2.Timestamp
    referring_url: str
    channel: _communication_pb2.CommType
    topic: str
    revoked_reason: str
    granted_reason: str
    proof: str
    condition_days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    condition_from: _timestamp_pb2.Timestamp
    condition_to: _timestamp_pb2.Timestamp
    notes: str
    conditions: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ConsentCondition]
    content_type: _compliance_pb2.ContentType
    channel_type: _compliance_pb2.Channel
    def __init__(self, consent_profile_id: _Optional[str] = ..., content: _Optional[str] = ..., recorded: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., referring_url: _Optional[str] = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., topic: _Optional[str] = ..., revoked_reason: _Optional[str] = ..., granted_reason: _Optional[str] = ..., proof: _Optional[str] = ..., condition_days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., condition_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., condition_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[_compliance_pb2.ConsentCondition, _Mapping]]] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class CreateConsentRes(_message.Message):
    __slots__ = ("consent_id",)
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    def __init__(self, consent_id: _Optional[int] = ...) -> None: ...

class ConsentProfile(_message.Message):
    __slots__ = ("consent_profile_id", "profile_name", "disabled", "consents", "channel", "created_on", "created_by")
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CONSENTS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    profile_name: str
    disabled: bool
    consents: _containers.RepeatedCompositeFieldContainer[Consent]
    channel: _communication_pb2.CommType
    created_on: _timestamp_pb2.Timestamp
    created_by: str
    def __init__(self, consent_profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., disabled: bool = ..., consents: _Optional[_Iterable[_Union[Consent, _Mapping]]] = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

class Consent(_message.Message):
    __slots__ = ("consent_id", "consent_profile_id", "deleted", "deleted_on", "content", "recorded", "revoked", "expire", "referring_url", "channel", "topic", "revoked_reason", "granted_reason", "proof", "condition_days_of_the_week", "condition_time_of_day_from", "condition_time_of_day_to", "condition_from", "condition_to", "notes", "conditions", "content_type", "channel_type")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETED_ON_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECORDED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    REFERRING_URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    GRANTED_REASON_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    consent_profile_id: str
    deleted: bool
    deleted_on: _timestamp_pb2.Timestamp
    content: str
    recorded: _timestamp_pb2.Timestamp
    revoked: _timestamp_pb2.Timestamp
    expire: _timestamp_pb2.Timestamp
    referring_url: str
    channel: _communication_pb2.CommType
    topic: str
    revoked_reason: str
    granted_reason: str
    proof: str
    condition_days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    condition_from: _timestamp_pb2.Timestamp
    condition_to: _timestamp_pb2.Timestamp
    notes: str
    conditions: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ConsentCondition]
    content_type: _compliance_pb2.ContentType
    channel_type: _compliance_pb2.Channel
    def __init__(self, consent_id: _Optional[int] = ..., consent_profile_id: _Optional[str] = ..., deleted: bool = ..., deleted_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., content: _Optional[str] = ..., recorded: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revoked: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., referring_url: _Optional[str] = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., topic: _Optional[str] = ..., revoked_reason: _Optional[str] = ..., granted_reason: _Optional[str] = ..., proof: _Optional[str] = ..., condition_days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., condition_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., condition_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[_compliance_pb2.ConsentCondition, _Mapping]]] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class GetConsentProfileReq(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class UpdateConsentReq(_message.Message):
    __slots__ = ("consent_id", "consent_profile_id", "content", "recorded", "revoked", "expire", "referring_url", "channel", "topic", "revoked_reason", "granted_reason", "proof", "condition_days_of_the_week", "condition_time_of_day_from", "condition_time_of_day_to", "condition_from", "condition_to", "notes", "conditions", "content_type", "channel_type")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECORDED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    REFERRING_URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    GRANTED_REASON_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    consent_profile_id: str
    content: str
    recorded: _timestamp_pb2.Timestamp
    revoked: _timestamp_pb2.Timestamp
    expire: _timestamp_pb2.Timestamp
    referring_url: str
    channel: _communication_pb2.CommType
    topic: str
    revoked_reason: str
    granted_reason: str
    proof: str
    condition_days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    condition_from: _timestamp_pb2.Timestamp
    condition_to: _timestamp_pb2.Timestamp
    notes: str
    conditions: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ConsentCondition]
    content_type: _compliance_pb2.ContentType
    channel_type: _compliance_pb2.Channel
    def __init__(self, consent_id: _Optional[int] = ..., consent_profile_id: _Optional[str] = ..., content: _Optional[str] = ..., recorded: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revoked: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., referring_url: _Optional[str] = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., topic: _Optional[str] = ..., revoked_reason: _Optional[str] = ..., granted_reason: _Optional[str] = ..., proof: _Optional[str] = ..., condition_days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., condition_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., condition_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[_compliance_pb2.ConsentCondition, _Mapping]]] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class ExpireConsentReq(_message.Message):
    __slots__ = ("consent_id", "expire")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    expire: _timestamp_pb2.Timestamp
    def __init__(self, consent_id: _Optional[int] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RevokeConsentReq(_message.Message):
    __slots__ = ("consent_id", "revoked", "consent_profile_id", "content", "channel_type", "revoked_reason", "content_type")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    revoked: _timestamp_pb2.Timestamp
    consent_profile_id: str
    content: str
    channel_type: _compliance_pb2.Channel
    revoked_reason: str
    content_type: _compliance_pb2.ContentType
    def __init__(self, consent_id: _Optional[int] = ..., revoked: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., consent_profile_id: _Optional[str] = ..., content: _Optional[str] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ..., revoked_reason: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ...) -> None: ...

class EnableConsentProfileReq(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class DisableConsentProfileReq(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class ListConsentProfilesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConsentProfile(_message.Message):
    __slots__ = ("consent_profile_id", "profile_name", "count", "disabled", "channel")
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    profile_name: str
    count: int
    disabled: bool
    channel: _communication_pb2.CommType
    def __init__(self, consent_profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., count: _Optional[int] = ..., disabled: bool = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ...) -> None: ...

class ListConsentProfilesRes(_message.Message):
    __slots__ = ("consent_profiles",)
    CONSENT_PROFILES_FIELD_NUMBER: _ClassVar[int]
    consent_profiles: _containers.RepeatedCompositeFieldContainer[ListConsentProfile]
    def __init__(self, consent_profiles: _Optional[_Iterable[_Union[ListConsentProfile, _Mapping]]] = ...) -> None: ...

class GetConsentUploadUrlReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConsentUploadUrlRes(_message.Message):
    __slots__ = ("url", "filename", "bucket")
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    url: str
    filename: str
    bucket: str
    def __init__(self, url: _Optional[str] = ..., filename: _Optional[str] = ..., bucket: _Optional[str] = ...) -> None: ...

class DeleteConsentReq(_message.Message):
    __slots__ = ("consent_id",)
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    consent_id: int
    def __init__(self, consent_id: _Optional[int] = ...) -> None: ...

class ProcessConsentUploadReq(_message.Message):
    __slots__ = ("filename", "consent_profile_id", "user_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    consent_profile_id: str
    user_id: str
    def __init__(self, filename: _Optional[str] = ..., consent_profile_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ProcessConsentUploadRes(_message.Message):
    __slots__ = ("entries_added",)
    ENTRIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    entries_added: int
    def __init__(self, entries_added: _Optional[int] = ...) -> None: ...

class GetFieldNamesReq(_message.Message):
    __slots__ = ("phone_only",)
    PHONE_ONLY_FIELD_NUMBER: _ClassVar[int]
    phone_only: bool
    def __init__(self, phone_only: bool = ...) -> None: ...

class FieldNames(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResultDescriptionsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PurgeScrubListReq(_message.Message):
    __slots__ = ("list_id",)
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    def __init__(self, list_id: _Optional[str] = ...) -> None: ...

class PurgeScrubListRes(_message.Message):
    __slots__ = ("entries_found",)
    ENTRIES_FOUND_FIELD_NUMBER: _ClassVar[int]
    entries_found: int
    def __init__(self, entries_found: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConsentTopic(_message.Message):
    __slots__ = ("topic", "org_id", "deleted")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    topic: str
    org_id: str
    deleted: bool
    def __init__(self, topic: _Optional[str] = ..., org_id: _Optional[str] = ..., deleted: bool = ...) -> None: ...

class ListConsentTopicsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConsentTopicsRes(_message.Message):
    __slots__ = ("topics",)
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[ConsentTopic]
    def __init__(self, topics: _Optional[_Iterable[_Union[ConsentTopic, _Mapping]]] = ...) -> None: ...

class GetConsentTopicReq(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class UpdateConsentTopicReq(_message.Message):
    __slots__ = ("original_topic", "new_topic")
    ORIGINAL_TOPIC_FIELD_NUMBER: _ClassVar[int]
    NEW_TOPIC_FIELD_NUMBER: _ClassVar[int]
    original_topic: str
    new_topic: str
    def __init__(self, original_topic: _Optional[str] = ..., new_topic: _Optional[str] = ...) -> None: ...

class SearchConsentByContentReq(_message.Message):
    __slots__ = ("content", "consent_profile_id")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    consent_profile_id: str
    def __init__(self, content: _Optional[str] = ..., consent_profile_id: _Optional[str] = ...) -> None: ...

class ConsentByContent(_message.Message):
    __slots__ = ("org_id", "profile_id", "profile_name", "consent_id", "content", "revoked", "expire", "disabled", "channel", "topic", "condition_days_of_the_week", "condition_time_of_day_from", "condition_time_of_day_to", "condition_from", "condition_to", "notes", "content_type", "conditions", "channel_type")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    profile_id: str
    profile_name: str
    consent_id: int
    content: str
    revoked: _timestamp_pb2.Timestamp
    expire: _timestamp_pb2.Timestamp
    disabled: bool
    channel: _communication_pb2.CommType
    topic: str
    condition_days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    condition_from: _timestamp_pb2.Timestamp
    condition_to: _timestamp_pb2.Timestamp
    notes: str
    content_type: _compliance_pb2.ContentType
    conditions: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ConsentCondition]
    channel_type: _compliance_pb2.Channel
    def __init__(self, org_id: _Optional[str] = ..., profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., consent_id: _Optional[int] = ..., content: _Optional[str] = ..., revoked: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disabled: bool = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., topic: _Optional[str] = ..., condition_days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., condition_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., condition_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., conditions: _Optional[_Iterable[_Union[_compliance_pb2.ConsentCondition, _Mapping]]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class SearchConsentByContentRes(_message.Message):
    __slots__ = ("consents",)
    CONSENTS_FIELD_NUMBER: _ClassVar[int]
    consents: _containers.RepeatedCompositeFieldContainer[ConsentByContent]
    def __init__(self, consents: _Optional[_Iterable[_Union[ConsentByContent, _Mapping]]] = ...) -> None: ...

class GetConsentByProfileAndContentReq(_message.Message):
    __slots__ = ("profile_name", "content", "profile_id", "content_type", "channel_type")
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    profile_name: str
    content: str
    profile_id: str
    content_type: _compliance_pb2.ContentType
    channel_type: _compliance_pb2.Channel
    def __init__(self, profile_name: _Optional[str] = ..., content: _Optional[str] = ..., profile_id: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class GetConsentByProfileAndContentRes(_message.Message):
    __slots__ = ("org_id", "profile_id", "profile_name", "consent_id", "revoked", "expire", "disabled", "channel", "topic", "condition_days_of_the_week", "condition_time_of_day_from", "condition_time_of_day_to", "condition_from", "condition_to", "notes", "content_type", "conditions", "channel_type", "revoked_reason", "granted_reason", "proof")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONDITION_DAYS_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    GRANTED_REASON_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    profile_id: str
    profile_name: str
    consent_id: int
    revoked: _timestamp_pb2.Timestamp
    expire: _timestamp_pb2.Timestamp
    disabled: bool
    channel: _communication_pb2.CommType
    topic: str
    condition_days_of_the_week: _containers.RepeatedScalarFieldContainer[_enums_pb2.Weekday.Enum]
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    condition_from: _timestamp_pb2.Timestamp
    condition_to: _timestamp_pb2.Timestamp
    notes: str
    content_type: _compliance_pb2.ContentType
    conditions: _containers.RepeatedCompositeFieldContainer[_compliance_pb2.ConsentCondition]
    channel_type: _compliance_pb2.Channel
    revoked_reason: str
    granted_reason: str
    proof: str
    def __init__(self, org_id: _Optional[str] = ..., profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., consent_id: _Optional[int] = ..., revoked: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disabled: bool = ..., channel: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., topic: _Optional[str] = ..., condition_days_of_the_week: _Optional[_Iterable[_Union[_enums_pb2.Weekday.Enum, str]]] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., condition_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., condition_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., content_type: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., conditions: _Optional[_Iterable[_Union[_compliance_pb2.ConsentCondition, _Mapping]]] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ..., revoked_reason: _Optional[str] = ..., granted_reason: _Optional[str] = ..., proof: _Optional[str] = ...) -> None: ...

class GetConsentByContentReq(_message.Message):
    __slots__ = ("profile_name", "content", "profile_id", "channel_type")
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    profile_name: str
    content: str
    profile_id: str
    channel_type: _compliance_pb2.Channel
    def __init__(self, profile_name: _Optional[str] = ..., content: _Optional[str] = ..., profile_id: _Optional[str] = ..., channel_type: _Optional[_Union[_compliance_pb2.Channel, str]] = ...) -> None: ...

class GetConsentByContentRes(_message.Message):
    __slots__ = ("org_id", "profile_name", "consent", "disabled")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    profile_name: str
    consent: Consent
    disabled: bool
    def __init__(self, org_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., consent: _Optional[_Union[Consent, _Mapping]] = ..., disabled: bool = ...) -> None: ...

class ProcessConsentListDeleteUploadReq(_message.Message):
    __slots__ = ("consent_profile_id", "filename", "notification_message")
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    filename: str
    notification_message: str
    def __init__(self, consent_profile_id: _Optional[str] = ..., filename: _Optional[str] = ..., notification_message: _Optional[str] = ...) -> None: ...

class ProcessConsentListDeleteUploadRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessConsentListDeleteUploadMeta(_message.Message):
    __slots__ = ("time_started",)
    TIME_STARTED_FIELD_NUMBER: _ClassVar[int]
    time_started: _timestamp_pb2.Timestamp
    def __init__(self, time_started: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class QueryHolidaysResponse(_message.Message):
    __slots__ = ("rows",)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[HolidayData]
    def __init__(self, rows: _Optional[_Iterable[_Union[HolidayData, _Mapping]]] = ...) -> None: ...

class HolidayData(_message.Message):
    __slots__ = ("date", "name", "year", "month", "day", "weekday", "types", "is_observed", "country", "states")
    DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    IS_OBSERVED_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    date: str
    name: str
    year: str
    month: str
    day: str
    weekday: str
    types: _containers.RepeatedScalarFieldContainer[str]
    is_observed: str
    country: str
    states: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, date: _Optional[str] = ..., name: _Optional[str] = ..., year: _Optional[str] = ..., month: _Optional[str] = ..., day: _Optional[str] = ..., weekday: _Optional[str] = ..., types: _Optional[_Iterable[str]] = ..., is_observed: _Optional[str] = ..., country: _Optional[str] = ..., states: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryHolidaysRequest(_message.Message):
    __slots__ = ("date", "name", "year", "month", "day", "weekday", "type", "is_observed", "country", "state")
    DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_OBSERVED_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    date: str
    name: str
    year: str
    month: str
    day: str
    weekday: str
    type: str
    is_observed: str
    country: str
    state: str
    def __init__(self, date: _Optional[str] = ..., name: _Optional[str] = ..., year: _Optional[str] = ..., month: _Optional[str] = ..., day: _Optional[str] = ..., weekday: _Optional[str] = ..., type: _Optional[str] = ..., is_observed: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class ExportConsentListRequest(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class ExportConsentListResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...
