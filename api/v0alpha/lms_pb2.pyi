from annotations import authz_pb2 as _authz_pb2
from api.commons import communication_pb2 as _communication_pb2
from api.commons import compliance_pb2 as _compliance_pb2
from api.commons import lms_pb2 as _lms_pb2
from api.commons import perms_pb2 as _perms_pb2
from api.commons import types_pb2 as _types_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[TimeUnit]
    TIME_WEEKS: _ClassVar[TimeUnit]
    TIME_DAYS: _ClassVar[TimeUnit]
    TIME_HOURS: _ClassVar[TimeUnit]

class EpicEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EPIC_UNKNOWN_TYPE: _ClassVar[EpicEntityType]
    EPIC_ENTITY_TYPE_PATIENT: _ClassVar[EpicEntityType]
    EPIC_ENTITY_TYPE_APPOINTMENT: _ClassVar[EpicEntityType]
    EPIC_ENTITY_TYPE_MEDICATION: _ClassVar[EpicEntityType]
    EPIC_ENTITY_TYPE_MEDICATION_REQUEST: _ClassVar[EpicEntityType]
    EPIC_ENTITY_TYPE_ACCOUNT: _ClassVar[EpicEntityType]
DEFAULT: TimeUnit
TIME_WEEKS: TimeUnit
TIME_DAYS: TimeUnit
TIME_HOURS: TimeUnit
EPIC_UNKNOWN_TYPE: EpicEntityType
EPIC_ENTITY_TYPE_PATIENT: EpicEntityType
EPIC_ENTITY_TYPE_APPOINTMENT: EpicEntityType
EPIC_ENTITY_TYPE_MEDICATION: EpicEntityType
EPIC_ENTITY_TYPE_MEDICATION_REQUEST: EpicEntityType
EPIC_ENTITY_TYPE_ACCOUNT: EpicEntityType

class PipelineCanvasMetadata(_message.Message):
    __slots__ = ("pipeline_canvas_sid", "name", "description", "created_date", "last_edited")
    PIPELINE_CANVAS_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas_sid: int
    name: str
    description: str
    created_date: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, pipeline_canvas_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PipelineCanvas(_message.Message):
    __slots__ = ("metadata", "elements")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    metadata: PipelineCanvasMetadata
    elements: _containers.RepeatedCompositeFieldContainer[Element]
    def __init__(self, metadata: _Optional[_Union[PipelineCanvasMetadata, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[Element, _Mapping]]] = ...) -> None: ...

class PipelineCanvasPreview(_message.Message):
    __slots__ = ("metadata", "entrypoints", "exchanges", "element_count")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINTS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    metadata: PipelineCanvasMetadata
    entrypoints: _containers.RepeatedScalarFieldContainer[str]
    exchanges: _containers.RepeatedScalarFieldContainer[str]
    element_count: int
    def __init__(self, metadata: _Optional[_Union[PipelineCanvasMetadata, _Mapping]] = ..., entrypoints: _Optional[_Iterable[str]] = ..., exchanges: _Optional[_Iterable[str]] = ..., element_count: _Optional[int] = ...) -> None: ...

class CreatePipelineCanvasReq(_message.Message):
    __slots__ = ("name", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreatePipelineCanvasRes(_message.Message):
    __slots__ = ("pipeline_canvas",)
    PIPELINE_CANVAS_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas: PipelineCanvas
    def __init__(self, pipeline_canvas: _Optional[_Union[PipelineCanvas, _Mapping]] = ...) -> None: ...

class ListPipelineCanvasesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPipelineCanvasesRes(_message.Message):
    __slots__ = ("pipeline_canvas_previews",)
    PIPELINE_CANVAS_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas_previews: _containers.RepeatedCompositeFieldContainer[PipelineCanvasPreview]
    def __init__(self, pipeline_canvas_previews: _Optional[_Iterable[_Union[PipelineCanvasPreview, _Mapping]]] = ...) -> None: ...

class UpdatePipelineCanvasReq(_message.Message):
    __slots__ = ("pipeline_canvas_sid", "name", "description")
    PIPELINE_CANVAS_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas_sid: int
    name: str
    description: str
    def __init__(self, pipeline_canvas_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdatePipelineCanvasRes(_message.Message):
    __slots__ = ("pipeline_canvas",)
    PIPELINE_CANVAS_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas: PipelineCanvas
    def __init__(self, pipeline_canvas: _Optional[_Union[PipelineCanvas, _Mapping]] = ...) -> None: ...

class DeletePipelineCanvasReq(_message.Message):
    __slots__ = ("pipeline_canvas_sid",)
    PIPELINE_CANVAS_SID_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas_sid: int
    def __init__(self, pipeline_canvas_sid: _Optional[int] = ...) -> None: ...

class DeletePipelineCanvasRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPipelineCanvasReq(_message.Message):
    __slots__ = ("pipeline_canvas_sid",)
    PIPELINE_CANVAS_SID_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas_sid: int
    def __init__(self, pipeline_canvas_sid: _Optional[int] = ...) -> None: ...

class GetPipelineCanvasRes(_message.Message):
    __slots__ = ("pipeline_canvas",)
    PIPELINE_CANVAS_FIELD_NUMBER: _ClassVar[int]
    pipeline_canvas: PipelineCanvas
    def __init__(self, pipeline_canvas: _Optional[_Union[PipelineCanvas, _Mapping]] = ...) -> None: ...

class ListPoolsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPoolsResponse(_message.Message):
    __slots__ = ("pools",)
    POOLS_FIELD_NUMBER: _ClassVar[int]
    pools: _containers.RepeatedCompositeFieldContainer[Pool]
    def __init__(self, pools: _Optional[_Iterable[_Union[Pool, _Mapping]]] = ...) -> None: ...

class Pool(_message.Message):
    __slots__ = ("id", "name", "desc")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    desc: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...

class GetPublicKeyReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublicKey(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class FindFieldUsagesReq(_message.Message):
    __slots__ = ("field_name",)
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    def __init__(self, field_name: _Optional[str] = ...) -> None: ...

class NameAndId(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FindFieldUsagesRes(_message.Message):
    __slots__ = ("field_name", "file_templates", "elements")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    file_templates: _containers.RepeatedCompositeFieldContainer[NameAndId]
    elements: _containers.RepeatedCompositeFieldContainer[NameAndId]
    def __init__(self, field_name: _Optional[str] = ..., file_templates: _Optional[_Iterable[_Union[NameAndId, _Mapping]]] = ..., elements: _Optional[_Iterable[_Union[NameAndId, _Mapping]]] = ...) -> None: ...

class ElementError(_message.Message):
    __slots__ = ("invalid_expression", "missing_field", "bad_field_type")
    class InvalidExpression(_message.Message):
        __slots__ = ("expression",)
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        expression: str
        def __init__(self, expression: _Optional[str] = ...) -> None: ...
    class MissingField(_message.Message):
        __slots__ = ("field_name",)
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        def __init__(self, field_name: _Optional[str] = ...) -> None: ...
    class BadFieldType(_message.Message):
        __slots__ = ("field_name",)
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        def __init__(self, field_name: _Optional[str] = ...) -> None: ...
    INVALID_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BAD_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    invalid_expression: ElementError.InvalidExpression
    missing_field: ElementError.MissingField
    bad_field_type: ElementError.BadFieldType
    def __init__(self, invalid_expression: _Optional[_Union[ElementError.InvalidExpression, _Mapping]] = ..., missing_field: _Optional[_Union[ElementError.MissingField, _Mapping]] = ..., bad_field_type: _Optional[_Union[ElementError.BadFieldType, _Mapping]] = ...) -> None: ...

class ElementSummary(_message.Message):
    __slots__ = ("element_id", "element_name", "error")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    element_name: str
    error: ElementError
    def __init__(self, element_id: _Optional[str] = ..., element_name: _Optional[str] = ..., error: _Optional[_Union[ElementError, _Mapping]] = ...) -> None: ...

class FindInvalidElementsReq(_message.Message):
    __slots__ = ("org_id", "region_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region_id: str
    def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class FindInvalidElementsRes(_message.Message):
    __slots__ = ("invalid_elements",)
    INVALID_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    invalid_elements: _containers.RepeatedCompositeFieldContainer[ElementSummary]
    def __init__(self, invalid_elements: _Optional[_Iterable[_Union[ElementSummary, _Mapping]]] = ...) -> None: ...

class GetComplianceScrubListsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetComplianceScrubListsRes(_message.Message):
    __slots__ = ("scrub_lists",)
    SCRUB_LISTS_FIELD_NUMBER: _ClassVar[int]
    scrub_lists: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scrub_lists: _Optional[_Iterable[str]] = ...) -> None: ...

class ProcessElementReq(_message.Message):
    __slots__ = ("element_id", "process_message")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    process_message: str
    def __init__(self, element_id: _Optional[str] = ..., process_message: _Optional[str] = ...) -> None: ...

class ProcessListRequest(_message.Message):
    __slots__ = ("element_id", "list")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    list: bytes
    def __init__(self, element_id: _Optional[str] = ..., list: _Optional[bytes] = ...) -> None: ...

class ProcessListResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StreamListRequest(_message.Message):
    __slots__ = ("org_id", "region_id", "element_id", "chunk")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region_id: str
    element_id: str
    chunk: bytes
    def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., element_id: _Optional[str] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class StreamListResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailableFieldsByElementIdReq(_message.Message):
    __slots__ = ("element_id",)
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    def __init__(self, element_id: _Optional[str] = ...) -> None: ...

class ListFieldsForElementReq(_message.Message):
    __slots__ = ("element_id",)
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    def __init__(self, element_id: _Optional[str] = ...) -> None: ...

class ListFieldsForElementRes(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class ListAutocompleteFieldsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAutocompleteFieldsRes(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class ElementPK(_message.Message):
    __slots__ = ("element_id",)
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    def __init__(self, element_id: _Optional[str] = ...) -> None: ...

class Element(_message.Message):
    __slots__ = ("element_id", "name", "inputs", "input_is_discard", "transform", "last_status", "labels", "created_date", "last_edited", "description", "pipeline_canvas_sid")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_IS_DISCARD_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_CANVAS_SID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    name: str
    inputs: _containers.RepeatedScalarFieldContainer[str]
    input_is_discard: _containers.RepeatedScalarFieldContainer[bool]
    transform: Process
    last_status: _lms_pb2.PipelineElementStatusType
    labels: _containers.RepeatedScalarFieldContainer[str]
    created_date: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    description: str
    pipeline_canvas_sid: int
    def __init__(self, element_id: _Optional[str] = ..., name: _Optional[str] = ..., inputs: _Optional[_Iterable[str]] = ..., input_is_discard: _Optional[_Iterable[bool]] = ..., transform: _Optional[_Union[Process, _Mapping]] = ..., last_status: _Optional[_Union[_lms_pb2.PipelineElementStatusType, str]] = ..., labels: _Optional[_Iterable[str]] = ..., created_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., pipeline_canvas_sid: _Optional[int] = ...) -> None: ...

class PeekListReq(_message.Message):
    __slots__ = ("element_id", "version", "page_size", "page", "process", "peek_at_discards")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    PEEK_AT_DISCARDS_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    version: int
    page_size: int
    page: int
    process: Process
    peek_at_discards: bool
    def __init__(self, element_id: _Optional[str] = ..., version: _Optional[int] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., peek_at_discards: bool = ...) -> None: ...

class PeekListRes(_message.Message):
    __slots__ = ("records", "metrics")
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[RecordProto]
    metrics: ListMetrics
    def __init__(self, records: _Optional[_Iterable[_Union[RecordProto, _Mapping]]] = ..., metrics: _Optional[_Union[ListMetrics, _Mapping]] = ...) -> None: ...

class GetHistoryReq(_message.Message):
    __slots__ = ("element_id", "count", "starting_id")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    STARTING_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    count: int
    starting_id: int
    def __init__(self, element_id: _Optional[str] = ..., count: _Optional[int] = ..., starting_id: _Optional[int] = ...) -> None: ...

class GetHistoryRes(_message.Message):
    __slots__ = ("element_id", "commits")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMITS_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    commits: _containers.RepeatedCompositeFieldContainer[HistoryAndCount]
    def __init__(self, element_id: _Optional[str] = ..., commits: _Optional[_Iterable[_Union[HistoryAndCount, _Mapping]]] = ...) -> None: ...

class History(_message.Message):
    __slots__ = ("element_id", "history_id", "process", "failed", "attempt_number", "reason", "upload_ts", "started_ts", "finished_ts", "event_id", "parent_element_id", "metrics", "discard_metrics")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TS_FIELD_NUMBER: _ClassVar[int]
    STARTED_TS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TS_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DISCARD_METRICS_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    history_id: int
    process: Process
    failed: bool
    attempt_number: int
    reason: _wrappers_pb2.StringValue
    upload_ts: _timestamp_pb2.Timestamp
    started_ts: _timestamp_pb2.Timestamp
    finished_ts: _timestamp_pb2.Timestamp
    event_id: int
    parent_element_id: str
    metrics: ListMetrics
    discard_metrics: ListMetrics
    def __init__(self, element_id: _Optional[str] = ..., history_id: _Optional[int] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., failed: bool = ..., attempt_number: _Optional[int] = ..., reason: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., upload_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finished_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_id: _Optional[int] = ..., parent_element_id: _Optional[str] = ..., metrics: _Optional[_Union[ListMetrics, _Mapping]] = ..., discard_metrics: _Optional[_Union[ListMetrics, _Mapping]] = ...) -> None: ...

class HistoryAndCount(_message.Message):
    __slots__ = ("element_id", "history_id", "ending_history_id", "process", "failed", "attempt_number", "reason", "upload_ts", "started_ts", "finished_ts", "event_id", "parent_element_id", "metrics", "discard_metrics", "count")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    ENDING_HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TS_FIELD_NUMBER: _ClassVar[int]
    STARTED_TS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TS_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DISCARD_METRICS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    history_id: int
    ending_history_id: int
    process: Process
    failed: bool
    attempt_number: int
    reason: _wrappers_pb2.StringValue
    upload_ts: _timestamp_pb2.Timestamp
    started_ts: _timestamp_pb2.Timestamp
    finished_ts: _timestamp_pb2.Timestamp
    event_id: int
    parent_element_id: str
    metrics: ListMetrics
    discard_metrics: ListMetrics
    count: int
    def __init__(self, element_id: _Optional[str] = ..., history_id: _Optional[int] = ..., ending_history_id: _Optional[int] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., failed: bool = ..., attempt_number: _Optional[int] = ..., reason: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., upload_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finished_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_id: _Optional[int] = ..., parent_element_id: _Optional[str] = ..., metrics: _Optional[_Union[ListMetrics, _Mapping]] = ..., discard_metrics: _Optional[_Union[ListMetrics, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class RecordProto(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[RecordFieldProto]
    def __init__(self, fields: _Optional[_Iterable[_Union[RecordFieldProto, _Mapping]]] = ...) -> None: ...

class RecordProtoPair(_message.Message):
    __slots__ = ("old", "new")
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    old: RecordProto
    new: RecordProto
    def __init__(self, old: _Optional[_Union[RecordProto, _Mapping]] = ..., new: _Optional[_Union[RecordProto, _Mapping]] = ...) -> None: ...

class ProcessFields(_message.Message):
    __slots__ = ("fields",)
    class NestedField(_message.Message):
        __slots__ = ("name", "field_type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        field_type: _lms_pb2.RecordType
        def __init__(self, name: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.RecordType, str]] = ...) -> None: ...
    class Field(_message.Message):
        __slots__ = ("name", "field_type", "nested", "format")
        NAME_FIELD_NUMBER: _ClassVar[int]
        FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        NESTED_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        name: str
        field_type: _lms_pb2.RecordType
        nested: _containers.RepeatedCompositeFieldContainer[ProcessFields.NestedField]
        format: str
        def __init__(self, name: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.RecordType, str]] = ..., nested: _Optional[_Iterable[_Union[ProcessFields.NestedField, _Mapping]]] = ..., format: _Optional[str] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[ProcessFields.Field]
    def __init__(self, fields: _Optional[_Iterable[_Union[ProcessFields.Field, _Mapping]]] = ...) -> None: ...

class FieldPK(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("name", "type", "date_modified", "metadata", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _lms_pb2.FieldType
    date_modified: _timestamp_pb2.Timestamp
    metadata: FieldMetadata
    description: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_lms_pb2.FieldType, str]] = ..., date_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[FieldMetadata, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateFieldReq(_message.Message):
    __slots__ = ("name", "type", "date_modified", "new_name", "metadata", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _lms_pb2.FieldType
    date_modified: _timestamp_pb2.Timestamp
    new_name: str
    metadata: FieldMetadata
    description: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_lms_pb2.FieldType, str]] = ..., date_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., new_name: _Optional[str] = ..., metadata: _Optional[_Union[FieldMetadata, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class FieldMetadata(_message.Message):
    __slots__ = ("time_format", "precision", "remove_characters", "replace_empty", "replace_error", "remove_letters", "remove_numbers", "remove_symbols", "leave_characters", "remove_string", "json_dot_path", "json_force_type_match", "starting_position", "field_length")
    TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EMPTY_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ERROR_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LETTERS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    LEAVE_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_STRING_FIELD_NUMBER: _ClassVar[int]
    JSON_DOT_PATH_FIELD_NUMBER: _ClassVar[int]
    JSON_FORCE_TYPE_MATCH_FIELD_NUMBER: _ClassVar[int]
    STARTING_POSITION_FIELD_NUMBER: _ClassVar[int]
    FIELD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    time_format: str
    precision: _lms_pb2.DateTimePrecision
    remove_characters: str
    replace_empty: str
    replace_error: str
    remove_letters: bool
    remove_numbers: bool
    remove_symbols: bool
    leave_characters: str
    remove_string: str
    json_dot_path: str
    json_force_type_match: bool
    starting_position: int
    field_length: int
    def __init__(self, time_format: _Optional[str] = ..., precision: _Optional[_Union[_lms_pb2.DateTimePrecision, str]] = ..., remove_characters: _Optional[str] = ..., replace_empty: _Optional[str] = ..., replace_error: _Optional[str] = ..., remove_letters: bool = ..., remove_numbers: bool = ..., remove_symbols: bool = ..., leave_characters: _Optional[str] = ..., remove_string: _Optional[str] = ..., json_dot_path: _Optional[str] = ..., json_force_type_match: bool = ..., starting_position: _Optional[int] = ..., field_length: _Optional[int] = ...) -> None: ...

class Fields(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class FieldIndex(_message.Message):
    __slots__ = ("index", "datetime")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    index: _containers.RepeatedScalarFieldContainer[str]
    datetime: DateTimeModifier
    def __init__(self, index: _Optional[_Iterable[str]] = ..., datetime: _Optional[_Union[DateTimeModifier, _Mapping]] = ...) -> None: ...

class ListFieldsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordFieldProto(_message.Message):
    __slots__ = ("name", "string_value", "number_value", "bool_value", "phone", "currency", "postal_code", "email", "date_time", "repeated_records", "record_field_map", "err", "enriched_phone", "enriched_zip")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REPEATED_RECORDS_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_MAP_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    ENRICHED_PHONE_FIELD_NUMBER: _ClassVar[int]
    ENRICHED_ZIP_FIELD_NUMBER: _ClassVar[int]
    name: str
    string_value: str
    number_value: float
    bool_value: bool
    phone: Phone
    currency: Currency
    postal_code: PostalCode
    email: Email
    date_time: DateTime
    repeated_records: RepeatedRecords
    record_field_map: RecordFieldMap
    err: Error
    enriched_phone: EnrichedPhone
    enriched_zip: EnrichedZip
    def __init__(self, name: _Optional[str] = ..., string_value: _Optional[str] = ..., number_value: _Optional[float] = ..., bool_value: bool = ..., phone: _Optional[_Union[Phone, _Mapping]] = ..., currency: _Optional[_Union[Currency, _Mapping]] = ..., postal_code: _Optional[_Union[PostalCode, _Mapping]] = ..., email: _Optional[_Union[Email, _Mapping]] = ..., date_time: _Optional[_Union[DateTime, _Mapping]] = ..., repeated_records: _Optional[_Union[RepeatedRecords, _Mapping]] = ..., record_field_map: _Optional[_Union[RecordFieldMap, _Mapping]] = ..., err: _Optional[_Union[Error, _Mapping]] = ..., enriched_phone: _Optional[_Union[EnrichedPhone, _Mapping]] = ..., enriched_zip: _Optional[_Union[EnrichedZip, _Mapping]] = ...) -> None: ...

class RepeatedRecords(_message.Message):
    __slots__ = ("records",)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[RecordProto]
    def __init__(self, records: _Optional[_Iterable[_Union[RecordProto, _Mapping]]] = ...) -> None: ...

class ListElementsReq(_message.Message):
    __slots__ = ("labels",)
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, labels: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFileTemplatesReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FileTemplateField(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _lms_pb2.FieldType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_lms_pb2.FieldType, str]] = ...) -> None: ...

class FileTemplateFields(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[FileTemplateField]
    def __init__(self, fields: _Optional[_Iterable[_Union[FileTemplateField, _Mapping]]] = ...) -> None: ...

class FieldTypes(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[_lms_pb2.FieldType]
    def __init__(self, values: _Optional[_Iterable[_Union[_lms_pb2.FieldType, str]]] = ...) -> None: ...

class FileTemplate(_message.Message):
    __slots__ = ("file_template_id", "name", "description", "field_names", "file_format_params", "file_format", "fields")
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    file_template_id: str
    name: str
    description: str
    field_names: _containers.RepeatedScalarFieldContainer[str]
    file_format_params: FileFormatParams
    file_format: _lms_pb2.FileFormat
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    def __init__(self, file_template_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., field_names: _Optional[_Iterable[str]] = ..., file_format_params: _Optional[_Union[FileFormatParams, _Mapping]] = ..., file_format: _Optional[_Union[_lms_pb2.FileFormat, str]] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...) -> None: ...

class LMSUploadReq(_message.Message):
    __slots__ = ("element_id", "file_id")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    file_id: str
    def __init__(self, element_id: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class LMSUploadRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReRunReq(_message.Message):
    __slots__ = ("list_id", "rerun_url")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    RERUN_URL_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    rerun_url: str
    def __init__(self, list_id: _Optional[str] = ..., rerun_url: _Optional[str] = ...) -> None: ...

class ReRunRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Process(_message.Message):
    __slots__ = ("expression", "append", "sort", "filter", "gs_export", "p3_export", "compl", "dedup", "cfs_export", "sftp_export", "reshape", "lookup", "entrypoint", "compliance_export", "api_entrypoint", "sftp_import", "scrub", "frequency", "cjs_import", "cjs_export", "cjs_enrich", "web_entrypoint", "delete_scrub_entries", "wfm_export", "link_enrich", "rnd", "consent_enrich", "consent_export", "compliance_processor", "consent_entrypoint", "portal_link_enrich", "bulk_web_entrypoint", "omni_exchange_process", "web_exchange_process", "split", "epic_entry_point", "contact_manager_sink", "sum", "finvi_entrypoint", "contact_management_enrichment", "ticket_exchange_sink")
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GS_EXPORT_FIELD_NUMBER: _ClassVar[int]
    P3_EXPORT_FIELD_NUMBER: _ClassVar[int]
    COMPL_FIELD_NUMBER: _ClassVar[int]
    DEDUP_FIELD_NUMBER: _ClassVar[int]
    CFS_EXPORT_FIELD_NUMBER: _ClassVar[int]
    SFTP_EXPORT_FIELD_NUMBER: _ClassVar[int]
    RESHAPE_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_FIELD_NUMBER: _ClassVar[int]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_EXPORT_FIELD_NUMBER: _ClassVar[int]
    API_ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    SFTP_IMPORT_FIELD_NUMBER: _ClassVar[int]
    SCRUB_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CJS_IMPORT_FIELD_NUMBER: _ClassVar[int]
    CJS_EXPORT_FIELD_NUMBER: _ClassVar[int]
    CJS_ENRICH_FIELD_NUMBER: _ClassVar[int]
    WEB_ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCRUB_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    WFM_EXPORT_FIELD_NUMBER: _ClassVar[int]
    LINK_ENRICH_FIELD_NUMBER: _ClassVar[int]
    RND_FIELD_NUMBER: _ClassVar[int]
    CONSENT_ENRICH_FIELD_NUMBER: _ClassVar[int]
    CONSENT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    CONSENT_ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    PORTAL_LINK_ENRICH_FIELD_NUMBER: _ClassVar[int]
    BULK_WEB_ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    OMNI_EXCHANGE_PROCESS_FIELD_NUMBER: _ClassVar[int]
    WEB_EXCHANGE_PROCESS_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    EPIC_ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGER_SINK_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    FINVI_ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_MANAGEMENT_ENRICHMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_EXCHANGE_SINK_FIELD_NUMBER: _ClassVar[int]
    expression: str
    append: AppendProcess
    sort: SortCriteria
    filter: FilterProcess
    gs_export: GSExportProcess
    p3_export: P3ExportProcess
    compl: ComplProcess
    dedup: DeDupCriteria
    cfs_export: CFSExportProcess
    sftp_export: SftpExportProcess
    reshape: ReshapeProcess
    lookup: LookupProcess
    entrypoint: EntrypointProcess
    compliance_export: ComplianceExportProcess
    api_entrypoint: ApiEntrypoint
    sftp_import: SftpImport
    scrub: ScrubProcess
    frequency: FrequencyProcess
    cjs_import: CjsImportProcess
    cjs_export: CjsExportProcess
    cjs_enrich: CjsEnrichmentProcess
    web_entrypoint: WebEntrypointProcess
    delete_scrub_entries: DeleteScrubEntriesProcess
    wfm_export: WfmExportProcess
    link_enrich: PaymentLinkEnrichment
    rnd: RndEnrichmentProcess
    consent_enrich: ConsentEnrichmentProcess
    consent_export: ConsentExportProcess
    compliance_processor: ComplianceProcessor
    consent_entrypoint: ConsentEntrypointProcess
    portal_link_enrich: PortalLinkEnrichment
    bulk_web_entrypoint: BulkWebEntrypointProcess
    omni_exchange_process: OmniExchangeProcess
    web_exchange_process: WebExchangeProcess
    split: SplitCriteria
    epic_entry_point: EpicEntrypoint
    contact_manager_sink: ContactManagerSink
    sum: SumProcess
    finvi_entrypoint: FinviEntrypoint
    contact_management_enrichment: ContactManagementEnrichment
    ticket_exchange_sink: TicketExchangeSink
    def __init__(self, expression: _Optional[str] = ..., append: _Optional[_Union[AppendProcess, _Mapping]] = ..., sort: _Optional[_Union[SortCriteria, _Mapping]] = ..., filter: _Optional[_Union[FilterProcess, _Mapping]] = ..., gs_export: _Optional[_Union[GSExportProcess, _Mapping]] = ..., p3_export: _Optional[_Union[P3ExportProcess, _Mapping]] = ..., compl: _Optional[_Union[ComplProcess, _Mapping]] = ..., dedup: _Optional[_Union[DeDupCriteria, _Mapping]] = ..., cfs_export: _Optional[_Union[CFSExportProcess, _Mapping]] = ..., sftp_export: _Optional[_Union[SftpExportProcess, _Mapping]] = ..., reshape: _Optional[_Union[ReshapeProcess, _Mapping]] = ..., lookup: _Optional[_Union[LookupProcess, _Mapping]] = ..., entrypoint: _Optional[_Union[EntrypointProcess, _Mapping]] = ..., compliance_export: _Optional[_Union[ComplianceExportProcess, _Mapping]] = ..., api_entrypoint: _Optional[_Union[ApiEntrypoint, _Mapping]] = ..., sftp_import: _Optional[_Union[SftpImport, _Mapping]] = ..., scrub: _Optional[_Union[ScrubProcess, _Mapping]] = ..., frequency: _Optional[_Union[FrequencyProcess, _Mapping]] = ..., cjs_import: _Optional[_Union[CjsImportProcess, _Mapping]] = ..., cjs_export: _Optional[_Union[CjsExportProcess, _Mapping]] = ..., cjs_enrich: _Optional[_Union[CjsEnrichmentProcess, _Mapping]] = ..., web_entrypoint: _Optional[_Union[WebEntrypointProcess, _Mapping]] = ..., delete_scrub_entries: _Optional[_Union[DeleteScrubEntriesProcess, _Mapping]] = ..., wfm_export: _Optional[_Union[WfmExportProcess, _Mapping]] = ..., link_enrich: _Optional[_Union[PaymentLinkEnrichment, _Mapping]] = ..., rnd: _Optional[_Union[RndEnrichmentProcess, _Mapping]] = ..., consent_enrich: _Optional[_Union[ConsentEnrichmentProcess, _Mapping]] = ..., consent_export: _Optional[_Union[ConsentExportProcess, _Mapping]] = ..., compliance_processor: _Optional[_Union[ComplianceProcessor, _Mapping]] = ..., consent_entrypoint: _Optional[_Union[ConsentEntrypointProcess, _Mapping]] = ..., portal_link_enrich: _Optional[_Union[PortalLinkEnrichment, _Mapping]] = ..., bulk_web_entrypoint: _Optional[_Union[BulkWebEntrypointProcess, _Mapping]] = ..., omni_exchange_process: _Optional[_Union[OmniExchangeProcess, _Mapping]] = ..., web_exchange_process: _Optional[_Union[WebExchangeProcess, _Mapping]] = ..., split: _Optional[_Union[SplitCriteria, _Mapping]] = ..., epic_entry_point: _Optional[_Union[EpicEntrypoint, _Mapping]] = ..., contact_manager_sink: _Optional[_Union[ContactManagerSink, _Mapping]] = ..., sum: _Optional[_Union[SumProcess, _Mapping]] = ..., finvi_entrypoint: _Optional[_Union[FinviEntrypoint, _Mapping]] = ..., contact_management_enrichment: _Optional[_Union[ContactManagementEnrichment, _Mapping]] = ..., ticket_exchange_sink: _Optional[_Union[TicketExchangeSink, _Mapping]] = ...) -> None: ...

class ComplianceProcessor(_message.Message):
    __slots__ = ("rule_set_id", "comm_type", "call_type", "phone_number_field", "email_field", "zip_code_field", "call_metadata", "country_code")
    class CallMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    COMM_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_FIELD_NUMBER: _ClassVar[int]
    CALL_METADATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    rule_set_id: str
    comm_type: _communication_pb2.CommType
    call_type: str
    phone_number_field: str
    email_field: str
    zip_code_field: str
    call_metadata: _containers.ScalarMap[str, str]
    country_code: str
    def __init__(self, rule_set_id: _Optional[str] = ..., comm_type: _Optional[_Union[_communication_pb2.CommType, _Mapping]] = ..., call_type: _Optional[str] = ..., phone_number_field: _Optional[str] = ..., email_field: _Optional[str] = ..., zip_code_field: _Optional[str] = ..., call_metadata: _Optional[_Mapping[str, str]] = ..., country_code: _Optional[str] = ...) -> None: ...

class ConsentEntrypointProcess(_message.Message):
    __slots__ = ("consent_profile_id",)
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    consent_profile_id: str
    def __init__(self, consent_profile_id: _Optional[str] = ...) -> None: ...

class ConsentEnrichmentProcess(_message.Message):
    __slots__ = ("content_field", "consent_profile", "consent_profile_id")
    CONTENT_FIELD_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    content_field: str
    consent_profile: str
    consent_profile_id: str
    def __init__(self, content_field: _Optional[str] = ..., consent_profile: _Optional[str] = ..., consent_profile_id: _Optional[str] = ...) -> None: ...

class ConsentExportProcess(_message.Message):
    __slots__ = ("content_field", "consent_profile", "consent_profile_id", "run_type", "action", "referring_url", "topic", "revoked_reason", "granted_reason", "proof", "condition_time_of_day_from", "condition_time_of_day_to", "notes", "expire", "condition_from", "condition_to", "content_type_val", "content_type_field_name", "channel_type_val", "channel_type_field_name", "expiration_date", "expiration_field_name", "expiration_after_duration")
    CONTENT_FIELD_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    REFERRING_URL_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    REVOKED_REASON_FIELD_NUMBER: _ClassVar[int]
    GRANTED_REASON_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TIME_OF_DAY_TO_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FROM_FIELD_NUMBER: _ClassVar[int]
    CONDITION_TO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_VAL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_VAL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_AFTER_DURATION_FIELD_NUMBER: _ClassVar[int]
    content_field: str
    consent_profile: str
    consent_profile_id: str
    run_type: _lms_pb2.RunType
    action: _lms_pb2.ConsentActionType
    referring_url: str
    topic: str
    revoked_reason: str
    granted_reason: str
    proof: str
    condition_time_of_day_from: str
    condition_time_of_day_to: str
    notes: str
    expire: str
    condition_from: str
    condition_to: str
    content_type_val: _compliance_pb2.ContentType
    content_type_field_name: str
    channel_type_val: _compliance_pb2.Channel
    channel_type_field_name: str
    expiration_date: _timestamp_pb2.Timestamp
    expiration_field_name: str
    expiration_after_duration: _duration_pb2.Duration
    def __init__(self, content_field: _Optional[str] = ..., consent_profile: _Optional[str] = ..., consent_profile_id: _Optional[str] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., action: _Optional[_Union[_lms_pb2.ConsentActionType, str]] = ..., referring_url: _Optional[str] = ..., topic: _Optional[str] = ..., revoked_reason: _Optional[str] = ..., granted_reason: _Optional[str] = ..., proof: _Optional[str] = ..., condition_time_of_day_from: _Optional[str] = ..., condition_time_of_day_to: _Optional[str] = ..., notes: _Optional[str] = ..., expire: _Optional[str] = ..., condition_from: _Optional[str] = ..., condition_to: _Optional[str] = ..., content_type_val: _Optional[_Union[_compliance_pb2.ContentType, str]] = ..., content_type_field_name: _Optional[str] = ..., channel_type_val: _Optional[_Union[_compliance_pb2.Channel, str]] = ..., channel_type_field_name: _Optional[str] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_field_name: _Optional[str] = ..., expiration_after_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PaymentLinkEnrichment(_message.Message):
    __slots__ = ("fields", "payment_link_config_id", "discard_on_missing_fields", "key_map", "portal_id")
    class KeyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_LINK_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    DISCARD_ON_MISSING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    KEY_MAP_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    payment_link_config_id: str
    discard_on_missing_fields: bool
    key_map: _containers.ScalarMap[str, str]
    portal_id: str
    def __init__(self, fields: _Optional[_Iterable[str]] = ..., payment_link_config_id: _Optional[str] = ..., discard_on_missing_fields: bool = ..., key_map: _Optional[_Mapping[str, str]] = ..., portal_id: _Optional[str] = ...) -> None: ...

class PortalLinkEnrichment(_message.Message):
    __slots__ = ("key_map", "portal_id", "expiration", "demo")
    class KeyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_MAP_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    DEMO_FIELD_NUMBER: _ClassVar[int]
    key_map: _containers.ScalarMap[str, str]
    portal_id: str
    expiration: Expiration
    demo: bool
    def __init__(self, key_map: _Optional[_Mapping[str, str]] = ..., portal_id: _Optional[str] = ..., expiration: _Optional[_Union[Expiration, _Mapping]] = ..., demo: bool = ...) -> None: ...

class Expiration(_message.Message):
    __slots__ = ("units", "quantity")
    UNITS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    units: TimeUnit
    quantity: int
    def __init__(self, units: _Optional[_Union[TimeUnit, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class EntrypointProcess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ApiEntrypoint(_message.Message):
    __slots__ = ("fts_id", "file_template_id", "incremental", "encrypted")
    FTS_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    fts_id: str
    file_template_id: str
    incremental: bool
    encrypted: bool
    def __init__(self, fts_id: _Optional[str] = ..., file_template_id: _Optional[str] = ..., incremental: bool = ..., encrypted: bool = ...) -> None: ...

class HttpReq(_message.Message):
    __slots__ = ("url", "headers", "body", "method", "named_response_values")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class NamedResponseValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    NAMED_RESPONSE_VALUES_FIELD_NUMBER: _ClassVar[int]
    url: str
    headers: _containers.ScalarMap[str, str]
    body: str
    method: _lms_pb2.HttpVerb
    named_response_values: _containers.ScalarMap[str, str]
    def __init__(self, url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., body: _Optional[str] = ..., method: _Optional[_Union[_lms_pb2.HttpVerb, str]] = ..., named_response_values: _Optional[_Mapping[str, str]] = ...) -> None: ...

class WebEntrypointProcess(_message.Message):
    __slots__ = ("http_requests", "file_template_id", "file_template", "name", "cron", "timezone", "enabled")
    HTTP_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRON_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    http_requests: _containers.RepeatedCompositeFieldContainer[HttpReq]
    file_template_id: str
    file_template: FileTemplate
    name: str
    cron: str
    timezone: str
    enabled: bool
    def __init__(self, http_requests: _Optional[_Iterable[_Union[HttpReq, _Mapping]]] = ..., file_template_id: _Optional[str] = ..., file_template: _Optional[_Union[FileTemplate, _Mapping]] = ..., name: _Optional[str] = ..., cron: _Optional[str] = ..., timezone: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class BulkWebEntrypointProcess(_message.Message):
    __slots__ = ("preliminary_requests", "paginated_request", "file_template_id", "name", "cron", "timezone", "enabled", "flush_page_count", "flush_minute_count", "flush_during_check")
    PRELIMINARY_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRON_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLUSH_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLUSH_MINUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DURING_CHECK_FIELD_NUMBER: _ClassVar[int]
    preliminary_requests: _containers.RepeatedCompositeFieldContainer[HttpReq]
    paginated_request: PaginatedHttpRequest
    file_template_id: str
    name: str
    cron: str
    timezone: str
    enabled: bool
    flush_page_count: int
    flush_minute_count: int
    flush_during_check: bool
    def __init__(self, preliminary_requests: _Optional[_Iterable[_Union[HttpReq, _Mapping]]] = ..., paginated_request: _Optional[_Union[PaginatedHttpRequest, _Mapping]] = ..., file_template_id: _Optional[str] = ..., name: _Optional[str] = ..., cron: _Optional[str] = ..., timezone: _Optional[str] = ..., enabled: bool = ..., flush_page_count: _Optional[int] = ..., flush_minute_count: _Optional[int] = ..., flush_during_check: bool = ...) -> None: ...

class OmniExchangeProcess(_message.Message):
    __slots__ = ("project_id", "campaign_id", "time_zone", "days", "hour", "minute")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    campaign_id: int
    time_zone: str
    days: int
    hour: int
    minute: int
    def __init__(self, project_id: _Optional[int] = ..., campaign_id: _Optional[int] = ..., time_zone: _Optional[str] = ..., days: _Optional[int] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...

class WebExchangeProcess(_message.Message):
    __slots__ = ("http_requests", "error_threshold")
    HTTP_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    http_requests: _containers.RepeatedCompositeFieldContainer[HttpReq]
    error_threshold: int
    def __init__(self, http_requests: _Optional[_Iterable[_Union[HttpReq, _Mapping]]] = ..., error_threshold: _Optional[int] = ...) -> None: ...

class PaginatedHttpRequest(_message.Message):
    __slots__ = ("iteration_request", "start_index", "end_for_any", "end_for_all", "request_not_ready", "not_ready_wait_seconds", "not_ready_redo_preliminary", "not_ready_skip_iteration", "process_stop_page")
    ITERATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_FOR_ANY_FIELD_NUMBER: _ClassVar[int]
    END_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NOT_READY_FIELD_NUMBER: _ClassVar[int]
    NOT_READY_WAIT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NOT_READY_REDO_PRELIMINARY_FIELD_NUMBER: _ClassVar[int]
    NOT_READY_SKIP_ITERATION_FIELD_NUMBER: _ClassVar[int]
    PROCESS_STOP_PAGE_FIELD_NUMBER: _ClassVar[int]
    iteration_request: HttpReq
    start_index: int
    end_for_any: _containers.RepeatedCompositeFieldContainer[_lms_pb2.PaginationTerminator]
    end_for_all: _containers.RepeatedCompositeFieldContainer[_lms_pb2.PaginationTerminator]
    request_not_ready: _lms_pb2.PaginationTerminator
    not_ready_wait_seconds: int
    not_ready_redo_preliminary: bool
    not_ready_skip_iteration: bool
    process_stop_page: bool
    def __init__(self, iteration_request: _Optional[_Union[HttpReq, _Mapping]] = ..., start_index: _Optional[int] = ..., end_for_any: _Optional[_Iterable[_Union[_lms_pb2.PaginationTerminator, _Mapping]]] = ..., end_for_all: _Optional[_Iterable[_Union[_lms_pb2.PaginationTerminator, _Mapping]]] = ..., request_not_ready: _Optional[_Union[_lms_pb2.PaginationTerminator, _Mapping]] = ..., not_ready_wait_seconds: _Optional[int] = ..., not_ready_redo_preliminary: bool = ..., not_ready_skip_iteration: bool = ..., process_stop_page: bool = ...) -> None: ...

class SftpImport(_message.Message):
    __slots__ = ("user", "password", "private_key", "address", "port", "file_pattern", "enabled", "file_template_id", "incremental", "encrypted", "cron", "timezone", "transfer_config_name")
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    CRON_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: str
    private_key: str
    address: str
    port: str
    file_pattern: _lms_pb2.FilePattern
    enabled: bool
    file_template_id: str
    incremental: bool
    encrypted: bool
    cron: str
    timezone: str
    transfer_config_name: str
    def __init__(self, user: _Optional[str] = ..., password: _Optional[str] = ..., private_key: _Optional[str] = ..., address: _Optional[str] = ..., port: _Optional[str] = ..., file_pattern: _Optional[_Union[_lms_pb2.FilePattern, _Mapping]] = ..., enabled: bool = ..., file_template_id: _Optional[str] = ..., incremental: bool = ..., encrypted: bool = ..., cron: _Optional[str] = ..., timezone: _Optional[str] = ..., transfer_config_name: _Optional[str] = ...) -> None: ...

class RndEnrichmentProcess(_message.Message):
    __slots__ = ("org_id", "field", "date_last_contact_field")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DATE_LAST_CONTACT_FIELD_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    field: str
    date_last_contact_field: str
    def __init__(self, org_id: _Optional[str] = ..., field: _Optional[str] = ..., date_last_contact_field: _Optional[str] = ...) -> None: ...

class CjsImportProcess(_message.Message):
    __slots__ = ("cjs_collection_id", "enabled", "cron", "timezone", "dedup", "use_zero_values")
    CJS_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRON_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_FIELD_NUMBER: _ClassVar[int]
    USE_ZERO_VALUES_FIELD_NUMBER: _ClassVar[int]
    cjs_collection_id: str
    enabled: bool
    cron: str
    timezone: str
    dedup: bool
    use_zero_values: bool
    def __init__(self, cjs_collection_id: _Optional[str] = ..., enabled: bool = ..., cron: _Optional[str] = ..., timezone: _Optional[str] = ..., dedup: bool = ..., use_zero_values: bool = ...) -> None: ...

class CjsExportProcess(_message.Message):
    __slots__ = ("cjs_collection_id", "header", "run_type", "cjs_collection_name", "overwrite", "update", "update_key_field", "replace_invalid_with_null")
    CJS_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CJS_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPLACE_INVALID_WITH_NULL_FIELD_NUMBER: _ClassVar[int]
    cjs_collection_id: str
    header: ExportHeader
    run_type: _lms_pb2.RunType
    cjs_collection_name: str
    overwrite: bool
    update: bool
    update_key_field: str
    replace_invalid_with_null: bool
    def __init__(self, cjs_collection_id: _Optional[str] = ..., header: _Optional[_Union[ExportHeader, _Mapping]] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., cjs_collection_name: _Optional[str] = ..., overwrite: bool = ..., update: bool = ..., update_key_field: _Optional[str] = ..., replace_invalid_with_null: bool = ...) -> None: ...

class CjsEnrichmentProcess(_message.Message):
    __slots__ = ("cjs_collection_id", "key_field", "enrich_type", "primary_source", "cjs_key_field_name", "column_overwrite", "dedup_key_policy", "use_zero_values")
    CJS_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENRICH_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CJS_KEY_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_KEY_POLICY_FIELD_NUMBER: _ClassVar[int]
    USE_ZERO_VALUES_FIELD_NUMBER: _ClassVar[int]
    cjs_collection_id: str
    key_field: str
    enrich_type: _lms_pb2.EnrichmentType
    primary_source: _lms_pb2.PrimarySource
    cjs_key_field_name: str
    column_overwrite: bool
    dedup_key_policy: _lms_pb2.DedupKeyPolicy
    use_zero_values: bool
    def __init__(self, cjs_collection_id: _Optional[str] = ..., key_field: _Optional[str] = ..., enrich_type: _Optional[_Union[_lms_pb2.EnrichmentType, str]] = ..., primary_source: _Optional[_Union[_lms_pb2.PrimarySource, str]] = ..., cjs_key_field_name: _Optional[str] = ..., column_overwrite: bool = ..., dedup_key_policy: _Optional[_Union[_lms_pb2.DedupKeyPolicy, str]] = ..., use_zero_values: bool = ...) -> None: ...

class AppendProcess(_message.Message):
    __slots__ = ("fts_id",)
    FTS_ID_FIELD_NUMBER: _ClassVar[int]
    fts_id: str
    def __init__(self, fts_id: _Optional[str] = ...) -> None: ...

class LookupProcess(_message.Message):
    __slots__ = ("field_names", "compl", "list", "url")
    class ComplProcess(_message.Message):
        __slots__ = ("country_code",)
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        country_code: str
        def __init__(self, country_code: _Optional[str] = ...) -> None: ...
    class ListLookup(_message.Message):
        __slots__ = ("org_id", "region_id", "element_id", "version")
        ORG_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        org_id: str
        region_id: str
        element_id: str
        version: int
        def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., element_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
    class UrlLookup(_message.Message):
        __slots__ = ("url", "file_template")
        URL_FIELD_NUMBER: _ClassVar[int]
        FILE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        url: str
        file_template: FileTemplate
        def __init__(self, url: _Optional[str] = ..., file_template: _Optional[_Union[FileTemplate, _Mapping]] = ...) -> None: ...
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    COMPL_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    field_names: _containers.RepeatedScalarFieldContainer[str]
    compl: LookupProcess.ComplProcess
    list: LookupProcess.ListLookup
    url: LookupProcess.UrlLookup
    def __init__(self, field_names: _Optional[_Iterable[str]] = ..., compl: _Optional[_Union[LookupProcess.ComplProcess, _Mapping]] = ..., list: _Optional[_Union[LookupProcess.ListLookup, _Mapping]] = ..., url: _Optional[_Union[LookupProcess.UrlLookup, _Mapping]] = ...) -> None: ...

class ComplProcess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFSExportConfig(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _lms_pb2.ExportType
    value: str
    def __init__(self, type: _Optional[_Union[_lms_pb2.ExportType, str]] = ..., value: _Optional[str] = ...) -> None: ...

class CFSExportReqHeader(_message.Message):
    __slots__ = ("export_header", "configs", "org_id", "region_id")
    EXPORT_HEADER_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    export_header: ExportHeader
    configs: _containers.RepeatedCompositeFieldContainer[CFSExportConfig]
    org_id: str
    region_id: str
    def __init__(self, export_header: _Optional[_Union[ExportHeader, _Mapping]] = ..., configs: _Optional[_Iterable[_Union[CFSExportConfig, _Mapping]]] = ..., org_id: _Optional[str] = ..., region_id: _Optional[str] = ...) -> None: ...

class CFSExportProcess(_message.Message):
    __slots__ = ("export_header", "configs")
    EXPORT_HEADER_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    export_header: ExportHeader
    configs: _containers.RepeatedCompositeFieldContainer[CFSExportConfig]
    def __init__(self, export_header: _Optional[_Union[ExportHeader, _Mapping]] = ..., configs: _Optional[_Iterable[_Union[CFSExportConfig, _Mapping]]] = ...) -> None: ...

class FilterProcess(_message.Message):
    __slots__ = ("expression", "operations", "negate")
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    expression: str
    operations: _containers.RepeatedCompositeFieldContainer[FilterOperation]
    negate: bool
    def __init__(self, expression: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[FilterOperation, _Mapping]]] = ..., negate: bool = ...) -> None: ...

class FilterOperation(_message.Message):
    __slots__ = ("checks", "operator")
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[FilterCheck]
    operator: _lms_pb2.ChainOperator
    def __init__(self, checks: _Optional[_Iterable[_Union[FilterCheck, _Mapping]]] = ..., operator: _Optional[_Union[_lms_pb2.ChainOperator, str]] = ...) -> None: ...

class FilterCheck(_message.Message):
    __slots__ = ("val_comp", "type_comp", "list_comp")
    class Value(_message.Message):
        __slots__ = ("string_val", "number_val", "bool_val", "field_name", "date_time")
        STRING_VAL_FIELD_NUMBER: _ClassVar[int]
        NUMBER_VAL_FIELD_NUMBER: _ClassVar[int]
        BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        string_val: str
        number_val: float
        bool_val: bool
        field_name: FieldIndex
        date_time: DateTime
        def __init__(self, string_val: _Optional[str] = ..., number_val: _Optional[float] = ..., bool_val: bool = ..., field_name: _Optional[_Union[FieldIndex, _Mapping]] = ..., date_time: _Optional[_Union[DateTime, _Mapping]] = ...) -> None: ...
    class ValueComparison(_message.Message):
        __slots__ = ("field_name", "op", "value", "negate", "exists")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        OP_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        NEGATE_FIELD_NUMBER: _ClassVar[int]
        EXISTS_FIELD_NUMBER: _ClassVar[int]
        field_name: FieldIndex
        op: _lms_pb2.CompareOperator
        value: FilterCheck.Value
        negate: bool
        exists: bool
        def __init__(self, field_name: _Optional[_Union[FieldIndex, _Mapping]] = ..., op: _Optional[_Union[_lms_pb2.CompareOperator, str]] = ..., value: _Optional[_Union[FilterCheck.Value, _Mapping]] = ..., negate: bool = ..., exists: bool = ...) -> None: ...
    class TypeComparison(_message.Message):
        __slots__ = ("field_name", "matches_field_type", "negate")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        MATCHES_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        NEGATE_FIELD_NUMBER: _ClassVar[int]
        field_name: FieldIndex
        matches_field_type: _lms_pb2.RecordType
        negate: bool
        def __init__(self, field_name: _Optional[_Union[FieldIndex, _Mapping]] = ..., matches_field_type: _Optional[_Union[_lms_pb2.RecordType, str]] = ..., negate: bool = ...) -> None: ...
    class ListComparison(_message.Message):
        __slots__ = ("field_name", "data", "negate")
        class FieldOrVal(_message.Message):
            __slots__ = ("field", "value")
            FIELD_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            field: FieldIndex
            value: FilterCheck.Value
            def __init__(self, field: _Optional[_Union[FieldIndex, _Mapping]] = ..., value: _Optional[_Union[FilterCheck.Value, _Mapping]] = ...) -> None: ...
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        NEGATE_FIELD_NUMBER: _ClassVar[int]
        field_name: FieldIndex
        data: _containers.RepeatedCompositeFieldContainer[FilterCheck.ListComparison.FieldOrVal]
        negate: bool
        def __init__(self, field_name: _Optional[_Union[FieldIndex, _Mapping]] = ..., data: _Optional[_Iterable[_Union[FilterCheck.ListComparison.FieldOrVal, _Mapping]]] = ..., negate: bool = ...) -> None: ...
    VAL_COMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_COMP_FIELD_NUMBER: _ClassVar[int]
    LIST_COMP_FIELD_NUMBER: _ClassVar[int]
    val_comp: FilterCheck.ValueComparison
    type_comp: FilterCheck.TypeComparison
    list_comp: FilterCheck.ListComparison
    def __init__(self, val_comp: _Optional[_Union[FilterCheck.ValueComparison, _Mapping]] = ..., type_comp: _Optional[_Union[FilterCheck.TypeComparison, _Mapping]] = ..., list_comp: _Optional[_Union[FilterCheck.ListComparison, _Mapping]] = ...) -> None: ...

class GSExportProcess(_message.Message):
    __slots__ = ("bucket", "file")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    file: str
    def __init__(self, bucket: _Optional[str] = ..., file: _Optional[str] = ...) -> None: ...

class P3ExportProcess(_message.Message):
    __slots__ = ("header", "contact_list_prefix", "username", "password", "access_token", "country", "dupe_policy", "absent_policy", "template_id", "default_area_code", "schedule_template_number", "description", "run_type", "file_pattern", "filename", "caller_ids", "cell_scrub", "start_time", "end_time", "dial_order", "email_field", "email_from", "follow_the_sun", "messages_per_minute", "randomize_contacts", "schedule_as_paused", "schedule_rule", "sha_digest_override", "sms_field", "sms_source_number", "timezone_override", "zip_scrub", "completion_threshold", "timezone", "compliance_rule", "field_delimiter", "record_delimiter", "quote_fields", "use_custom_date_format", "file_format", "days_into_future", "start_hour", "end_hour", "schedule_by_timezone", "shift_phone_fields", "do_campaign_linking", "campaign_link_id", "stop_trigger")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_PREFIX_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DUPE_POLICY_FIELD_NUMBER: _ClassVar[int]
    ABSENT_POLICY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CALLER_IDS_FIELD_NUMBER: _ClassVar[int]
    CELL_SCRUB_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DIAL_ORDER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FROM_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_THE_SUN_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    RANDOMIZE_CONTACTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_AS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_RULE_FIELD_NUMBER: _ClassVar[int]
    SHA_DIGEST_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_FIELD_NUMBER: _ClassVar[int]
    SMS_SOURCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ZIP_SCRUB_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RULE_FIELD_NUMBER: _ClassVar[int]
    FIELD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    RECORD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DAYS_INTO_FUTURE_FIELD_NUMBER: _ClassVar[int]
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_BY_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_PHONE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DO_CAMPAIGN_LINKING_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    STOP_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    header: ExportHeader
    contact_list_prefix: str
    username: str
    password: str
    access_token: str
    country: str
    dupe_policy: _lms_pb2.DuplicatePolicyType
    absent_policy: _lms_pb2.AbsentPolicyType
    template_id: int
    default_area_code: int
    schedule_template_number: int
    description: str
    run_type: _lms_pb2.RunType
    file_pattern: _lms_pb2.FilePattern
    filename: _lms_pb2.ConstructedFilename
    caller_ids: _containers.RepeatedScalarFieldContainer[int]
    cell_scrub: bool
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    dial_order: _lms_pb2.DialOrderType
    email_field: str
    email_from: str
    follow_the_sun: bool
    messages_per_minute: int
    randomize_contacts: bool
    schedule_as_paused: bool
    schedule_rule: str
    sha_digest_override: bool
    sms_field: str
    sms_source_number: int
    timezone_override: bool
    zip_scrub: bool
    completion_threshold: int
    timezone: str
    compliance_rule: str
    field_delimiter: str
    record_delimiter: str
    quote_fields: bool
    use_custom_date_format: bool
    file_format: _lms_pb2.FileFormat
    days_into_future: int
    start_hour: str
    end_hour: str
    schedule_by_timezone: bool
    shift_phone_fields: bool
    do_campaign_linking: bool
    campaign_link_id: str
    stop_trigger: str
    def __init__(self, header: _Optional[_Union[ExportHeader, _Mapping]] = ..., contact_list_prefix: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., access_token: _Optional[str] = ..., country: _Optional[str] = ..., dupe_policy: _Optional[_Union[_lms_pb2.DuplicatePolicyType, str]] = ..., absent_policy: _Optional[_Union[_lms_pb2.AbsentPolicyType, str]] = ..., template_id: _Optional[int] = ..., default_area_code: _Optional[int] = ..., schedule_template_number: _Optional[int] = ..., description: _Optional[str] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., file_pattern: _Optional[_Union[_lms_pb2.FilePattern, _Mapping]] = ..., filename: _Optional[_Union[_lms_pb2.ConstructedFilename, _Mapping]] = ..., caller_ids: _Optional[_Iterable[int]] = ..., cell_scrub: bool = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dial_order: _Optional[_Union[_lms_pb2.DialOrderType, str]] = ..., email_field: _Optional[str] = ..., email_from: _Optional[str] = ..., follow_the_sun: bool = ..., messages_per_minute: _Optional[int] = ..., randomize_contacts: bool = ..., schedule_as_paused: bool = ..., schedule_rule: _Optional[str] = ..., sha_digest_override: bool = ..., sms_field: _Optional[str] = ..., sms_source_number: _Optional[int] = ..., timezone_override: bool = ..., zip_scrub: bool = ..., completion_threshold: _Optional[int] = ..., timezone: _Optional[str] = ..., compliance_rule: _Optional[str] = ..., field_delimiter: _Optional[str] = ..., record_delimiter: _Optional[str] = ..., quote_fields: bool = ..., use_custom_date_format: bool = ..., file_format: _Optional[_Union[_lms_pb2.FileFormat, str]] = ..., days_into_future: _Optional[int] = ..., start_hour: _Optional[str] = ..., end_hour: _Optional[str] = ..., schedule_by_timezone: bool = ..., shift_phone_fields: bool = ..., do_campaign_linking: bool = ..., campaign_link_id: _Optional[str] = ..., stop_trigger: _Optional[str] = ...) -> None: ...

class ComplianceExportProcess(_message.Message):
    __slots__ = ("list_name", "field", "expiration_field", "country_code", "run_type", "compliance_list_type")
    LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    list_name: str
    field: str
    expiration_field: str
    country_code: str
    run_type: _lms_pb2.RunType
    compliance_list_type: _lms_pb2.ComplianceListType
    def __init__(self, list_name: _Optional[str] = ..., field: _Optional[str] = ..., expiration_field: _Optional[str] = ..., country_code: _Optional[str] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., compliance_list_type: _Optional[_Union[_lms_pb2.ComplianceListType, str]] = ...) -> None: ...

class ScrubProcess(_message.Message):
    __slots__ = ("list_id", "field")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    field: str
    def __init__(self, list_id: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...

class DeleteScrubEntriesProcess(_message.Message):
    __slots__ = ("list_id", "field")
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    list_id: str
    field: str
    def __init__(self, list_id: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...

class FrequencyProcess(_message.Message):
    __slots__ = ("field", "days", "country_code", "meta_field", "dispositions", "results", "disposition_sets")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_FIELD_NUMBER: _ClassVar[int]
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_SETS_FIELD_NUMBER: _ClassVar[int]
    field: str
    days: int
    country_code: str
    meta_field: str
    dispositions: _containers.RepeatedCompositeFieldContainer[DispositionPair]
    results: _containers.RepeatedScalarFieldContainer[str]
    disposition_sets: _containers.RepeatedCompositeFieldContainer[DispositionSet]
    def __init__(self, field: _Optional[str] = ..., days: _Optional[int] = ..., country_code: _Optional[str] = ..., meta_field: _Optional[str] = ..., dispositions: _Optional[_Iterable[_Union[DispositionPair, _Mapping]]] = ..., results: _Optional[_Iterable[str]] = ..., disposition_sets: _Optional[_Iterable[_Union[DispositionSet, _Mapping]]] = ...) -> None: ...

class DispositionSet(_message.Message):
    __slots__ = ("dispositions",)
    DISPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    dispositions: _containers.RepeatedCompositeFieldContainer[DispositionPair]
    def __init__(self, dispositions: _Optional[_Iterable[_Union[DispositionPair, _Mapping]]] = ...) -> None: ...

class DispositionPair(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SftpExportProcess(_message.Message):
    __slots__ = ("dest_filepath", "password", "address", "username", "port", "fileformat", "prepend_headers", "field_delimiter", "record_delimiter", "file_pattern", "run_type", "header", "quote_fields", "use_custom_date_format", "directory", "filename", "shift_phone_fields", "transfer_config_name")
    DEST_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    FILEFORMAT_FIELD_NUMBER: _ClassVar[int]
    PREPEND_HEADERS_FIELD_NUMBER: _ClassVar[int]
    FIELD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    RECORD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SHIFT_PHONE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    dest_filepath: str
    password: str
    address: str
    username: str
    port: int
    fileformat: _lms_pb2.FileFormat
    prepend_headers: bool
    field_delimiter: str
    record_delimiter: str
    file_pattern: _lms_pb2.FilePattern
    run_type: _lms_pb2.RunType
    header: ExportHeader
    quote_fields: bool
    use_custom_date_format: bool
    directory: str
    filename: _lms_pb2.ConstructedFilename
    shift_phone_fields: bool
    transfer_config_name: str
    def __init__(self, dest_filepath: _Optional[str] = ..., password: _Optional[str] = ..., address: _Optional[str] = ..., username: _Optional[str] = ..., port: _Optional[int] = ..., fileformat: _Optional[_Union[_lms_pb2.FileFormat, str]] = ..., prepend_headers: bool = ..., field_delimiter: _Optional[str] = ..., record_delimiter: _Optional[str] = ..., file_pattern: _Optional[_Union[_lms_pb2.FilePattern, _Mapping]] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., header: _Optional[_Union[ExportHeader, _Mapping]] = ..., quote_fields: bool = ..., use_custom_date_format: bool = ..., directory: _Optional[str] = ..., filename: _Optional[_Union[_lms_pb2.ConstructedFilename, _Mapping]] = ..., shift_phone_fields: bool = ..., transfer_config_name: _Optional[str] = ...) -> None: ...

class WfmMultiSkill(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WfmExportProcess(_message.Message):
    __slots__ = ("single", "multi")
    SINGLE_FIELD_NUMBER: _ClassVar[int]
    MULTI_FIELD_NUMBER: _ClassVar[int]
    single: int
    multi: WfmMultiSkill
    def __init__(self, single: _Optional[int] = ..., multi: _Optional[_Union[WfmMultiSkill, _Mapping]] = ...) -> None: ...

class ExportHeader(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class SortReq(_message.Message):
    __slots__ = ("criteria", "record")
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    criteria: SortCriteria
    record: RecordProto
    def __init__(self, criteria: _Optional[_Union[SortCriteria, _Mapping]] = ..., record: _Optional[_Union[RecordProto, _Mapping]] = ...) -> None: ...

class CFSExportReq(_message.Message):
    __slots__ = ("header", "record")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    header: CFSExportReqHeader
    record: RecordProto
    def __init__(self, header: _Optional[_Union[CFSExportReqHeader, _Mapping]] = ..., record: _Optional[_Union[RecordProto, _Mapping]] = ...) -> None: ...

class DeDupCriteria(_message.Message):
    __slots__ = ("action", "fields", "unless", "disjunct_keys")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    UNLESS_FIELD_NUMBER: _ClassVar[int]
    DISJUNCT_KEYS_FIELD_NUMBER: _ClassVar[int]
    action: _lms_pb2.DeDupActions
    fields: _containers.RepeatedCompositeFieldContainer[FieldIndex]
    unless: FilterCheck
    disjunct_keys: bool
    def __init__(self, action: _Optional[_Union[_lms_pb2.DeDupActions, str]] = ..., fields: _Optional[_Iterable[_Union[FieldIndex, _Mapping]]] = ..., unless: _Optional[_Union[FilterCheck, _Mapping]] = ..., disjunct_keys: bool = ...) -> None: ...

class SortCriteria(_message.Message):
    __slots__ = ("ordering", "field_order")
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    FIELD_ORDER_FIELD_NUMBER: _ClassVar[int]
    ordering: _containers.RepeatedScalarFieldContainer[_lms_pb2.SortOrder]
    field_order: _containers.RepeatedCompositeFieldContainer[FieldIndex]
    def __init__(self, ordering: _Optional[_Iterable[_Union[_lms_pb2.SortOrder, str]]] = ..., field_order: _Optional[_Iterable[_Union[FieldIndex, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("error", "raw_value")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    error: str
    raw_value: str
    def __init__(self, error: _Optional[str] = ..., raw_value: _Optional[str] = ...) -> None: ...

class RecordFieldMap(_message.Message):
    __slots__ = ("fields",)
    class FieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RecordFieldProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RecordFieldProto, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, RecordFieldProto]
    def __init__(self, fields: _Optional[_Mapping[str, RecordFieldProto]] = ...) -> None: ...

class Currency(_message.Message):
    __slots__ = ("symbol", "raw_value", "value", "name", "invalid")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    raw_value: str
    value: float
    name: str
    invalid: bool
    def __init__(self, symbol: _Optional[str] = ..., raw_value: _Optional[str] = ..., value: _Optional[float] = ..., name: _Optional[str] = ..., invalid: bool = ...) -> None: ...

class Phone(_message.Message):
    __slots__ = ("raw_value", "full_number", "invalid")
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    FULL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    raw_value: str
    full_number: str
    invalid: bool
    def __init__(self, raw_value: _Optional[str] = ..., full_number: _Optional[str] = ..., invalid: bool = ...) -> None: ...

class PostalCode(_message.Message):
    __slots__ = ("postal_code", "invalid")
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    postal_code: str
    invalid: bool
    def __init__(self, postal_code: _Optional[str] = ..., invalid: bool = ...) -> None: ...

class Email(_message.Message):
    __slots__ = ("local_part", "domain", "full_address", "invalid")
    LOCAL_PART_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FULL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    local_part: str
    domain: str
    full_address: str
    invalid: bool
    def __init__(self, local_part: _Optional[str] = ..., domain: _Optional[str] = ..., full_address: _Optional[str] = ..., invalid: bool = ...) -> None: ...

class DateTimeModifier(_message.Message):
    __slots__ = ("years", "weeks", "days", "hours", "minutes", "seconds")
    YEARS_FIELD_NUMBER: _ClassVar[int]
    WEEKS_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    years: int
    weeks: int
    days: int
    hours: int
    minutes: int
    seconds: int
    def __init__(self, years: _Optional[int] = ..., weeks: _Optional[int] = ..., days: _Optional[int] = ..., hours: _Optional[int] = ..., minutes: _Optional[int] = ..., seconds: _Optional[int] = ...) -> None: ...

class DateTime(_message.Message):
    __slots__ = ("raw_value", "format", "precision", "modifier")
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    raw_value: str
    format: str
    precision: _lms_pb2.DateTimePrecision
    modifier: DateTimeModifier
    def __init__(self, raw_value: _Optional[str] = ..., format: _Optional[str] = ..., precision: _Optional[_Union[_lms_pb2.DateTimePrecision, str]] = ..., modifier: _Optional[_Union[DateTimeModifier, _Mapping]] = ...) -> None: ...

class EnrichedPhone(_message.Message):
    __slots__ = ("area_code", "block_id", "carrier", "cc", "ccnsn", "cell_prefix", "city", "coc_type", "dst", "international_prefix", "iso2", "language", "max", "min", "national_prefix", "ndc", "prefix", "region_code", "region_name", "ssc1", "ssc2", "ssc3", "ssc4", "source", "time_zone", "type", "uses_ndc", "utc")
    AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    CC_FIELD_NUMBER: _ClassVar[int]
    CCNSN_FIELD_NUMBER: _ClassVar[int]
    CELL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COC_TYPE_FIELD_NUMBER: _ClassVar[int]
    DST_FIELD_NUMBER: _ClassVar[int]
    INTERNATIONAL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ISO2_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NDC_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SSC1_FIELD_NUMBER: _ClassVar[int]
    SSC2_FIELD_NUMBER: _ClassVar[int]
    SSC3_FIELD_NUMBER: _ClassVar[int]
    SSC4_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USES_NDC_FIELD_NUMBER: _ClassVar[int]
    UTC_FIELD_NUMBER: _ClassVar[int]
    area_code: str
    block_id: str
    carrier: str
    cc: str
    ccnsn: str
    cell_prefix: str
    city: str
    coc_type: str
    dst: bool
    international_prefix: str
    iso2: str
    language: str
    max: str
    min: str
    national_prefix: str
    ndc: str
    prefix: str
    region_code: str
    region_name: str
    ssc1: str
    ssc2: str
    ssc3: str
    ssc4: str
    source: str
    time_zone: str
    type: str
    uses_ndc: bool
    utc: float
    def __init__(self, area_code: _Optional[str] = ..., block_id: _Optional[str] = ..., carrier: _Optional[str] = ..., cc: _Optional[str] = ..., ccnsn: _Optional[str] = ..., cell_prefix: _Optional[str] = ..., city: _Optional[str] = ..., coc_type: _Optional[str] = ..., dst: bool = ..., international_prefix: _Optional[str] = ..., iso2: _Optional[str] = ..., language: _Optional[str] = ..., max: _Optional[str] = ..., min: _Optional[str] = ..., national_prefix: _Optional[str] = ..., ndc: _Optional[str] = ..., prefix: _Optional[str] = ..., region_code: _Optional[str] = ..., region_name: _Optional[str] = ..., ssc1: _Optional[str] = ..., ssc2: _Optional[str] = ..., ssc3: _Optional[str] = ..., ssc4: _Optional[str] = ..., source: _Optional[str] = ..., time_zone: _Optional[str] = ..., type: _Optional[str] = ..., uses_ndc: bool = ..., utc: _Optional[float] = ...) -> None: ...

class EnrichedZip(_message.Message):
    __slots__ = ("accuracy", "admin_code1", "admin_code2", "admin_code3", "admin_name1", "admin_name2", "admin_name3", "area_code", "city_name", "city_type", "country_code", "county_fips", "county_name", "dst", "iso2", "msa_code", "place_name", "postal_code", "postal_code_key", "postal_type", "province_abbr", "province_name", "source", "state_fips", "time_zone", "utc")
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CODE1_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CODE2_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CODE3_FIELD_NUMBER: _ClassVar[int]
    ADMIN_NAME1_FIELD_NUMBER: _ClassVar[int]
    ADMIN_NAME2_FIELD_NUMBER: _ClassVar[int]
    ADMIN_NAME3_FIELD_NUMBER: _ClassVar[int]
    AREA_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTY_FIPS_FIELD_NUMBER: _ClassVar[int]
    COUNTY_NAME_FIELD_NUMBER: _ClassVar[int]
    DST_FIELD_NUMBER: _ClassVar[int]
    ISO2_FIELD_NUMBER: _ClassVar[int]
    MSA_CODE_FIELD_NUMBER: _ClassVar[int]
    PLACE_NAME_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_KEY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_ABBR_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIPS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    UTC_FIELD_NUMBER: _ClassVar[int]
    accuracy: int
    admin_code1: str
    admin_code2: str
    admin_code3: str
    admin_name1: str
    admin_name2: str
    admin_name3: str
    area_code: str
    city_name: str
    city_type: str
    country_code: str
    county_fips: str
    county_name: str
    dst: bool
    iso2: str
    msa_code: str
    place_name: str
    postal_code: str
    postal_code_key: str
    postal_type: str
    province_abbr: str
    province_name: str
    source: str
    state_fips: str
    time_zone: str
    utc: float
    def __init__(self, accuracy: _Optional[int] = ..., admin_code1: _Optional[str] = ..., admin_code2: _Optional[str] = ..., admin_code3: _Optional[str] = ..., admin_name1: _Optional[str] = ..., admin_name2: _Optional[str] = ..., admin_name3: _Optional[str] = ..., area_code: _Optional[str] = ..., city_name: _Optional[str] = ..., city_type: _Optional[str] = ..., country_code: _Optional[str] = ..., county_fips: _Optional[str] = ..., county_name: _Optional[str] = ..., dst: bool = ..., iso2: _Optional[str] = ..., msa_code: _Optional[str] = ..., place_name: _Optional[str] = ..., postal_code: _Optional[str] = ..., postal_code_key: _Optional[str] = ..., postal_type: _Optional[str] = ..., province_abbr: _Optional[str] = ..., province_name: _Optional[str] = ..., source: _Optional[str] = ..., state_fips: _Optional[str] = ..., time_zone: _Optional[str] = ..., utc: _Optional[float] = ...) -> None: ...

class Now(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ("year", "month", "week", "day_of_month", "day_of_week", "day_of_year", "hour", "minute", "second")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    week: int
    day_of_month: int
    day_of_week: int
    day_of_year: int
    hour: int
    minute: int
    second: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., week: _Optional[int] = ..., day_of_month: _Optional[int] = ..., day_of_week: _Optional[int] = ..., day_of_year: _Optional[int] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., second: _Optional[int] = ...) -> None: ...

class Date(_message.Message):
    __slots__ = ("year", "month", "week", "day_of_month", "day_of_week", "day_of_year")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    week: int
    day_of_month: int
    day_of_week: int
    day_of_year: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., week: _Optional[int] = ..., day_of_month: _Optional[int] = ..., day_of_week: _Optional[int] = ..., day_of_year: _Optional[int] = ...) -> None: ...

class MonthAndDay(_message.Message):
    __slots__ = ("month", "week", "day_of_month", "day_of_week", "day_of_year")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_YEAR_FIELD_NUMBER: _ClassVar[int]
    month: int
    week: int
    day_of_month: int
    day_of_week: int
    day_of_year: int
    def __init__(self, month: _Optional[int] = ..., week: _Optional[int] = ..., day_of_month: _Optional[int] = ..., day_of_week: _Optional[int] = ..., day_of_year: _Optional[int] = ...) -> None: ...

class DayOfWeek(_message.Message):
    __slots__ = ("day_of_week",)
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    day_of_week: int
    def __init__(self, day_of_week: _Optional[int] = ...) -> None: ...

class TimeOfDay(_message.Message):
    __slots__ = ("hour", "minute", "second")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    second: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ..., second: _Optional[int] = ...) -> None: ...

class FileFormatParams(_message.Message):
    __slots__ = ("skip_first_no_lines", "skip_lines_match_regex", "trim_spaces", "custom_delimiter", "skip_first_line", "json_dot_path")
    SKIP_FIRST_NO_LINES_FIELD_NUMBER: _ClassVar[int]
    SKIP_LINES_MATCH_REGEX_FIELD_NUMBER: _ClassVar[int]
    TRIM_SPACES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIRST_LINE_FIELD_NUMBER: _ClassVar[int]
    JSON_DOT_PATH_FIELD_NUMBER: _ClassVar[int]
    skip_first_no_lines: int
    skip_lines_match_regex: str
    trim_spaces: bool
    custom_delimiter: str
    skip_first_line: bool
    json_dot_path: str
    def __init__(self, skip_first_no_lines: _Optional[int] = ..., skip_lines_match_regex: _Optional[str] = ..., trim_spaces: bool = ..., custom_delimiter: _Optional[str] = ..., skip_first_line: bool = ..., json_dot_path: _Optional[str] = ...) -> None: ...

class ReshapeProcess(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[ReshapeAction]
    def __init__(self, actions: _Optional[_Iterable[_Union[ReshapeAction, _Mapping]]] = ...) -> None: ...

class ReshapeAction(_message.Message):
    __slots__ = ("field", "matching_type", "predicate", "operations", "rename", "add_value", "add_field", "add_date", "subtract_value", "subtract_field", "convert", "remove_field", "add_new_field", "change_currency_type", "divide", "multiply", "modulo", "merge", "set_field_value", "add_new_field_from_field", "set_field_from_field", "pad", "trim", "extract")
    class Rename(_message.Message):
        __slots__ = ("new_name",)
        NEW_NAME_FIELD_NUMBER: _ClassVar[int]
        new_name: str
        def __init__(self, new_name: _Optional[str] = ...) -> None: ...
    class AddValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    class AddDate(_message.Message):
        __slots__ = ("datetime",)
        DATETIME_FIELD_NUMBER: _ClassVar[int]
        datetime: DateTimeModifier
        def __init__(self, datetime: _Optional[_Union[DateTimeModifier, _Mapping]] = ...) -> None: ...
    class AddField(_message.Message):
        __slots__ = ("other_field",)
        OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
        other_field: FieldIndex
        def __init__(self, other_field: _Optional[_Union[FieldIndex, _Mapping]] = ...) -> None: ...
    class SubtractValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float
        def __init__(self, value: _Optional[float] = ...) -> None: ...
    class SubtractField(_message.Message):
        __slots__ = ("other_field",)
        OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
        other_field: FieldIndex
        def __init__(self, other_field: _Optional[_Union[FieldIndex, _Mapping]] = ...) -> None: ...
    class Convert(_message.Message):
        __slots__ = ("newType", "new_field", "default_value")
        NEWTYPE_FIELD_NUMBER: _ClassVar[int]
        NEW_FIELD_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        newType: _lms_pb2.RecordType
        new_field: Field
        default_value: RecordFieldProto
        def __init__(self, newType: _Optional[_Union[_lms_pb2.RecordType, str]] = ..., new_field: _Optional[_Union[Field, _Mapping]] = ..., default_value: _Optional[_Union[RecordFieldProto, _Mapping]] = ...) -> None: ...
    class Divide(_message.Message):
        __slots__ = ("default_value", "divisor")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DIVISOR_FIELD_NUMBER: _ClassVar[int]
        default_value: float
        divisor: float
        def __init__(self, default_value: _Optional[float] = ..., divisor: _Optional[float] = ...) -> None: ...
    class Multiply(_message.Message):
        __slots__ = ("default_value", "multiplier")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        default_value: float
        multiplier: float
        def __init__(self, default_value: _Optional[float] = ..., multiplier: _Optional[float] = ...) -> None: ...
    class Modulo(_message.Message):
        __slots__ = ("default_value", "modulus")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        MODULUS_FIELD_NUMBER: _ClassVar[int]
        default_value: int
        modulus: int
        def __init__(self, default_value: _Optional[int] = ..., modulus: _Optional[int] = ...) -> None: ...
    class RemoveField(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AddNewField(_message.Message):
        __slots__ = ("starting_value",)
        STARTING_VALUE_FIELD_NUMBER: _ClassVar[int]
        starting_value: RecordFieldProto
        def __init__(self, starting_value: _Optional[_Union[RecordFieldProto, _Mapping]] = ...) -> None: ...
    class AddNewFieldFromField(_message.Message):
        __slots__ = ("name", "other_field")
        NAME_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
        name: str
        other_field: FieldIndex
        def __init__(self, name: _Optional[str] = ..., other_field: _Optional[_Union[FieldIndex, _Mapping]] = ...) -> None: ...
    class ChangeCurrencyType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetFieldValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: RecordFieldProto
        def __init__(self, value: _Optional[_Union[RecordFieldProto, _Mapping]] = ...) -> None: ...
    class SetFieldFromField(_message.Message):
        __slots__ = ("name", "other_field")
        NAME_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_FIELD_NUMBER: _ClassVar[int]
        name: str
        other_field: FieldIndex
        def __init__(self, name: _Optional[str] = ..., other_field: _Optional[_Union[FieldIndex, _Mapping]] = ...) -> None: ...
    class Merge(_message.Message):
        __slots__ = ("data",)
        class FieldOrVal(_message.Message):
            __slots__ = ("field", "value")
            FIELD_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            field: FieldIndex
            value: str
            def __init__(self, field: _Optional[_Union[FieldIndex, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedCompositeFieldContainer[ReshapeAction.Merge.FieldOrVal]
        def __init__(self, data: _Optional[_Iterable[_Union[ReshapeAction.Merge.FieldOrVal, _Mapping]]] = ...) -> None: ...
    class Pad(_message.Message):
        __slots__ = ("char", "amount", "prefix")
        CHAR_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        char: str
        amount: int
        prefix: bool
        def __init__(self, char: _Optional[str] = ..., amount: _Optional[int] = ..., prefix: bool = ...) -> None: ...
    class Trim(_message.Message):
        __slots__ = ("amount", "data", "marker", "suffix")
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        MARKER_FIELD_NUMBER: _ClassVar[int]
        SUFFIX_FIELD_NUMBER: _ClassVar[int]
        amount: int
        data: str
        marker: str
        suffix: bool
        def __init__(self, amount: _Optional[int] = ..., data: _Optional[str] = ..., marker: _Optional[str] = ..., suffix: bool = ...) -> None: ...
    class Extract(_message.Message):
        __slots__ = ("parts",)
        class Index(_message.Message):
            __slots__ = ("position", "match")
            POSITION_FIELD_NUMBER: _ClassVar[int]
            MATCH_FIELD_NUMBER: _ClassVar[int]
            position: int
            match: str
            def __init__(self, position: _Optional[int] = ..., match: _Optional[str] = ...) -> None: ...
        class Slice(_message.Message):
            __slots__ = ("start_is_exclusive", "end_is_inclusive", "start_index", "end_index")
            START_IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            END_IS_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            START_INDEX_FIELD_NUMBER: _ClassVar[int]
            END_INDEX_FIELD_NUMBER: _ClassVar[int]
            start_is_exclusive: bool
            end_is_inclusive: bool
            start_index: _containers.RepeatedCompositeFieldContainer[ReshapeAction.Extract.Index]
            end_index: _containers.RepeatedCompositeFieldContainer[ReshapeAction.Extract.Index]
            def __init__(self, start_is_exclusive: bool = ..., end_is_inclusive: bool = ..., start_index: _Optional[_Iterable[_Union[ReshapeAction.Extract.Index, _Mapping]]] = ..., end_index: _Optional[_Iterable[_Union[ReshapeAction.Extract.Index, _Mapping]]] = ...) -> None: ...
        PARTS_FIELD_NUMBER: _ClassVar[int]
        parts: _containers.RepeatedCompositeFieldContainer[ReshapeAction.Extract.Slice]
        def __init__(self, parts: _Optional[_Iterable[_Union[ReshapeAction.Extract.Slice, _Mapping]]] = ...) -> None: ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MATCHING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    RENAME_FIELD_NUMBER: _ClassVar[int]
    ADD_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_FIELD_NUMBER: _ClassVar[int]
    ADD_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBTRACT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUBTRACT_FIELD_FIELD_NUMBER: _ClassVar[int]
    CONVERT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_FIELD_NUMBER: _ClassVar[int]
    ADD_NEW_FIELD_FIELD_NUMBER: _ClassVar[int]
    CHANGE_CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIVIDE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLY_FIELD_NUMBER: _ClassVar[int]
    MODULO_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADD_NEW_FIELD_FROM_FIELD_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_FROM_FIELD_FIELD_NUMBER: _ClassVar[int]
    PAD_FIELD_NUMBER: _ClassVar[int]
    TRIM_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FIELD_NUMBER: _ClassVar[int]
    field: str
    matching_type: _lms_pb2.RecordType
    predicate: FilterCheck
    operations: FilterOperation
    rename: ReshapeAction.Rename
    add_value: ReshapeAction.AddValue
    add_field: ReshapeAction.AddField
    add_date: ReshapeAction.AddDate
    subtract_value: ReshapeAction.SubtractValue
    subtract_field: ReshapeAction.SubtractField
    convert: ReshapeAction.Convert
    remove_field: ReshapeAction.RemoveField
    add_new_field: ReshapeAction.AddNewField
    change_currency_type: ReshapeAction.ChangeCurrencyType
    divide: ReshapeAction.Divide
    multiply: ReshapeAction.Multiply
    modulo: ReshapeAction.Modulo
    merge: ReshapeAction.Merge
    set_field_value: ReshapeAction.SetFieldValue
    add_new_field_from_field: ReshapeAction.AddNewFieldFromField
    set_field_from_field: ReshapeAction.SetFieldFromField
    pad: ReshapeAction.Pad
    trim: ReshapeAction.Trim
    extract: ReshapeAction.Extract
    def __init__(self, field: _Optional[str] = ..., matching_type: _Optional[_Union[_lms_pb2.RecordType, str]] = ..., predicate: _Optional[_Union[FilterCheck, _Mapping]] = ..., operations: _Optional[_Union[FilterOperation, _Mapping]] = ..., rename: _Optional[_Union[ReshapeAction.Rename, _Mapping]] = ..., add_value: _Optional[_Union[ReshapeAction.AddValue, _Mapping]] = ..., add_field: _Optional[_Union[ReshapeAction.AddField, _Mapping]] = ..., add_date: _Optional[_Union[ReshapeAction.AddDate, _Mapping]] = ..., subtract_value: _Optional[_Union[ReshapeAction.SubtractValue, _Mapping]] = ..., subtract_field: _Optional[_Union[ReshapeAction.SubtractField, _Mapping]] = ..., convert: _Optional[_Union[ReshapeAction.Convert, _Mapping]] = ..., remove_field: _Optional[_Union[ReshapeAction.RemoveField, _Mapping]] = ..., add_new_field: _Optional[_Union[ReshapeAction.AddNewField, _Mapping]] = ..., change_currency_type: _Optional[_Union[ReshapeAction.ChangeCurrencyType, _Mapping]] = ..., divide: _Optional[_Union[ReshapeAction.Divide, _Mapping]] = ..., multiply: _Optional[_Union[ReshapeAction.Multiply, _Mapping]] = ..., modulo: _Optional[_Union[ReshapeAction.Modulo, _Mapping]] = ..., merge: _Optional[_Union[ReshapeAction.Merge, _Mapping]] = ..., set_field_value: _Optional[_Union[ReshapeAction.SetFieldValue, _Mapping]] = ..., add_new_field_from_field: _Optional[_Union[ReshapeAction.AddNewFieldFromField, _Mapping]] = ..., set_field_from_field: _Optional[_Union[ReshapeAction.SetFieldFromField, _Mapping]] = ..., pad: _Optional[_Union[ReshapeAction.Pad, _Mapping]] = ..., trim: _Optional[_Union[ReshapeAction.Trim, _Mapping]] = ..., extract: _Optional[_Union[ReshapeAction.Extract, _Mapping]] = ...) -> None: ...

class ContactManagerSink(_message.Message):
    __slots__ = ("project_id", "contact_list_name", "contact_list_description", "fields", "ttl", "lifetime", "user_id", "de_duplication_info")
    class DeDuplicationFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHONE_NUMBER: _ClassVar[ContactManagerSink.DeDuplicationFieldType]
        EMAIL_ADDRESS: _ClassVar[ContactManagerSink.DeDuplicationFieldType]
    PHONE_NUMBER: ContactManagerSink.DeDuplicationFieldType
    EMAIL_ADDRESS: ContactManagerSink.DeDuplicationFieldType
    class DeDuplicationMergeStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEEP_EXISTING_LIST: _ClassVar[ContactManagerSink.DeDuplicationMergeStrategy]
        REPLACE_EXISTING_LIST: _ClassVar[ContactManagerSink.DeDuplicationMergeStrategy]
    KEEP_EXISTING_LIST: ContactManagerSink.DeDuplicationMergeStrategy
    REPLACE_EXISTING_LIST: ContactManagerSink.DeDuplicationMergeStrategy
    class DeDuplication(_message.Message):
        __slots__ = ("field_type", "merge_strategy")
        FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        MERGE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        field_type: ContactManagerSink.DeDuplicationFieldType
        merge_strategy: ContactManagerSink.DeDuplicationMergeStrategy
        def __init__(self, field_type: _Optional[_Union[ContactManagerSink.DeDuplicationFieldType, str]] = ..., merge_strategy: _Optional[_Union[ContactManagerSink.DeDuplicationMergeStrategy, str]] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DE_DUPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    contact_list_name: str
    contact_list_description: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    ttl: int
    lifetime: _duration_pb2.Duration
    user_id: str
    de_duplication_info: ContactManagerSink.DeDuplication
    def __init__(self, project_id: _Optional[str] = ..., contact_list_name: _Optional[str] = ..., contact_list_description: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., user_id: _Optional[str] = ..., de_duplication_info: _Optional[_Union[ContactManagerSink.DeDuplication, _Mapping]] = ...) -> None: ...

class SumProcess(_message.Message):
    __slots__ = ("field", "new_name", "group_by", "filter")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    field: str
    new_name: str
    group_by: GroupBy
    filter: FilterOperation
    def __init__(self, field: _Optional[str] = ..., new_name: _Optional[str] = ..., group_by: _Optional[_Union[GroupBy, _Mapping]] = ..., filter: _Optional[_Union[FilterOperation, _Mapping]] = ...) -> None: ...

class GroupBy(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fields: _Optional[_Iterable[str]] = ...) -> None: ...

class ListMetrics(_message.Message):
    __slots__ = ("input_record_count", "output_record_count", "field_names", "field_types", "ftypes", "field_counts", "run_type", "success_message", "max_record_width", "min_record_width", "max_record_index", "min_record_index", "files", "groups", "missing_fields", "seconds_to_start", "seconds_to_process")
    INPUT_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPES_FIELD_NUMBER: _ClassVar[int]
    FTYPES_FIELD_NUMBER: _ClassVar[int]
    FIELD_COUNTS_FIELD_NUMBER: _ClassVar[int]
    RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_RECORD_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MIN_RECORD_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_RECORD_INDEX_FIELD_NUMBER: _ClassVar[int]
    MIN_RECORD_INDEX_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TO_START_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
    input_record_count: int
    output_record_count: int
    field_names: _containers.RepeatedScalarFieldContainer[str]
    field_types: _containers.RepeatedScalarFieldContainer[_lms_pb2.RecordType]
    ftypes: _containers.RepeatedScalarFieldContainer[_lms_pb2.FieldType]
    field_counts: _containers.RepeatedScalarFieldContainer[int]
    run_type: _lms_pb2.RunType
    success_message: str
    max_record_width: int
    min_record_width: int
    max_record_index: int
    min_record_index: int
    files: _containers.RepeatedScalarFieldContainer[str]
    groups: _containers.RepeatedScalarFieldContainer[str]
    missing_fields: _containers.RepeatedScalarFieldContainer[str]
    seconds_to_start: float
    seconds_to_process: float
    def __init__(self, input_record_count: _Optional[int] = ..., output_record_count: _Optional[int] = ..., field_names: _Optional[_Iterable[str]] = ..., field_types: _Optional[_Iterable[_Union[_lms_pb2.RecordType, str]]] = ..., ftypes: _Optional[_Iterable[_Union[_lms_pb2.FieldType, str]]] = ..., field_counts: _Optional[_Iterable[int]] = ..., run_type: _Optional[_Union[_lms_pb2.RunType, str]] = ..., success_message: _Optional[str] = ..., max_record_width: _Optional[int] = ..., min_record_width: _Optional[int] = ..., max_record_index: _Optional[int] = ..., min_record_index: _Optional[int] = ..., files: _Optional[_Iterable[str]] = ..., groups: _Optional[_Iterable[str]] = ..., missing_fields: _Optional[_Iterable[str]] = ..., seconds_to_start: _Optional[float] = ..., seconds_to_process: _Optional[float] = ...) -> None: ...

class ParseReq(_message.Message):
    __slots__ = ("element_id", "session_id", "expression")
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    element_id: str
    session_id: str
    expression: str
    def __init__(self, element_id: _Optional[str] = ..., session_id: _Optional[str] = ..., expression: _Optional[str] = ...) -> None: ...

class ParseRes(_message.Message):
    __slots__ = ("session_id", "expression", "next_tokens", "error", "complete", "process")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    expression: str
    next_tokens: _containers.RepeatedScalarFieldContainer[str]
    error: str
    complete: bool
    process: Process
    def __init__(self, session_id: _Optional[str] = ..., expression: _Optional[str] = ..., next_tokens: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ..., complete: bool = ..., process: _Optional[_Union[Process, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("event_id", "parent_id", "input_ids", "element_id", "process", "upload_ts", "started_ts", "finished_ts", "backoff_till", "attempts", "latest_history")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_IDS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TS_FIELD_NUMBER: _ClassVar[int]
    STARTED_TS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_TILL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    LATEST_HISTORY_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    parent_id: _wrappers_pb2.StringValue
    input_ids: _types_pb2.StringArraySql
    element_id: str
    process: Process
    upload_ts: _timestamp_pb2.Timestamp
    started_ts: _timestamp_pb2.Timestamp
    finished_ts: _timestamp_pb2.Timestamp
    backoff_till: _timestamp_pb2.Timestamp
    attempts: int
    latest_history: _wrappers_pb2.Int64Value
    def __init__(self, event_id: _Optional[int] = ..., parent_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., input_ids: _Optional[_Union[_types_pb2.StringArraySql, _Mapping]] = ..., element_id: _Optional[str] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., upload_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finished_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backoff_till: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attempts: _Optional[int] = ..., latest_history: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class Events(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class ViewQueueReq(_message.Message):
    __slots__ = ("newer_than", "no_newer_than", "after_event_id", "number_of_records")
    NEWER_THAN_FIELD_NUMBER: _ClassVar[int]
    NO_NEWER_THAN_FIELD_NUMBER: _ClassVar[int]
    AFTER_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_RECORDS_FIELD_NUMBER: _ClassVar[int]
    newer_than: _timestamp_pb2.Timestamp
    no_newer_than: _timestamp_pb2.Timestamp
    after_event_id: int
    number_of_records: int
    def __init__(self, newer_than: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., no_newer_than: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., after_event_id: _Optional[int] = ..., number_of_records: _Optional[int] = ...) -> None: ...

class RetypeCollectionReq(_message.Message):
    __slots__ = ("collection_id", "primary_key", "field_types", "as_copy")
    class FieldTypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _lms_pb2.FieldType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_lms_pb2.FieldType, str]] = ...) -> None: ...
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPES_FIELD_NUMBER: _ClassVar[int]
    AS_COPY_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    primary_key: _containers.RepeatedScalarFieldContainer[str]
    field_types: _containers.ScalarMap[str, _lms_pb2.FieldType]
    as_copy: bool
    def __init__(self, collection_id: _Optional[str] = ..., primary_key: _Optional[_Iterable[str]] = ..., field_types: _Optional[_Mapping[str, _lms_pb2.FieldType]] = ..., as_copy: bool = ...) -> None: ...

class RetypeCollectionRes(_message.Message):
    __slots__ = ("collection_id", "inserted_count", "updated_count", "rejected_count", "ignored_count", "rejected_entry_ids")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    INSERTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNORED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_ENTRY_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    inserted_count: int
    updated_count: int
    rejected_count: int
    ignored_count: int
    rejected_entry_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_id: _Optional[str] = ..., inserted_count: _Optional[int] = ..., updated_count: _Optional[int] = ..., rejected_count: _Optional[int] = ..., ignored_count: _Optional[int] = ..., rejected_entry_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CollectionMetadata(_message.Message):
    __slots__ = ("collection_id", "collection_name", "fields", "deleted", "created_by", "created_on", "last_queried", "query_count", "entry_count", "last_updated", "search_count", "last_searched", "primary_key")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    LAST_QUERIED_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEARCHED_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    collection_name: str
    fields: _containers.RepeatedCompositeFieldContainer[CollectionFieldMetadata]
    deleted: bool
    created_by: str
    created_on: _timestamp_pb2.Timestamp
    last_queried: _timestamp_pb2.Timestamp
    query_count: int
    entry_count: int
    last_updated: _timestamp_pb2.Timestamp
    search_count: int
    last_searched: _timestamp_pb2.Timestamp
    primary_key: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_id: _Optional[str] = ..., collection_name: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[CollectionFieldMetadata, _Mapping]]] = ..., deleted: bool = ..., created_by: _Optional[str] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_queried: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., query_count: _Optional[int] = ..., entry_count: _Optional[int] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., search_count: _Optional[int] = ..., last_searched: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., primary_key: _Optional[_Iterable[str]] = ...) -> None: ...

class CollectionEntry(_message.Message):
    __slots__ = ("collection_id", "entry_id", "fields", "last_updated")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    entry_id: str
    fields: _containers.RepeatedCompositeFieldContainer[CollectionField]
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, collection_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[CollectionField, _Mapping]]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MatchReq(_message.Message):
    __slots__ = ("collection_id", "fields", "batch_size")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    fields: _containers.RepeatedCompositeFieldContainer[CollectionField]
    batch_size: int
    def __init__(self, collection_id: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[CollectionField, _Mapping]]] = ..., batch_size: _Optional[int] = ...) -> None: ...

class MatchRes(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CollectionEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CollectionEntry, _Mapping]]] = ...) -> None: ...

class CollectionFieldMetadata(_message.Message):
    __slots__ = ("field_name", "field_type", "field_format")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FORMAT_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    field_type: _lms_pb2.FieldType
    field_format: str
    def __init__(self, field_name: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.FieldType, str]] = ..., field_format: _Optional[str] = ...) -> None: ...

class CollectionField(_message.Message):
    __slots__ = ("field_name", "field_value")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    field_value: str
    def __init__(self, field_name: _Optional[str] = ..., field_value: _Optional[str] = ...) -> None: ...

class GetCollectionReq(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class StreamCollectionReq(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionReq(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class ResetCollectionReq(_message.Message):
    __slots__ = ("collection_id",)
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class ListCollectionsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCollectionsRes(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[CollectionMetadata]
    def __init__(self, collections: _Optional[_Iterable[_Union[CollectionMetadata, _Mapping]]] = ...) -> None: ...

class SearchCollectionsPaginatedReq(_message.Message):
    __slots__ = ("collection_ids", "search", "page_size", "last_id")
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    LAST_ID_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    search: Search
    page_size: int
    last_id: str
    def __init__(self, collection_ids: _Optional[_Iterable[str]] = ..., search: _Optional[_Union[Search, _Mapping]] = ..., page_size: _Optional[int] = ..., last_id: _Optional[str] = ..., **kwargs) -> None: ...

class Search(_message.Message):
    __slots__ = ("term", "fuzziness", "substring", "negate", "case_sensitive", "value")
    TERM_FIELD_NUMBER: _ClassVar[int]
    FUZZINESS_FIELD_NUMBER: _ClassVar[int]
    SUBSTRING_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    term: str
    fuzziness: int
    substring: bool
    negate: bool
    case_sensitive: bool
    value: str
    def __init__(self, term: _Optional[str] = ..., fuzziness: _Optional[int] = ..., substring: bool = ..., negate: bool = ..., case_sensitive: bool = ..., value: _Optional[str] = ...) -> None: ...

class PaginatedSearchRes(_message.Message):
    __slots__ = ("entries", "total", "more_results", "last_id")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    MORE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    LAST_ID_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CollectionEntry]
    total: int
    more_results: bool
    last_id: str
    def __init__(self, entries: _Optional[_Iterable[_Union[CollectionEntry, _Mapping]]] = ..., total: _Optional[int] = ..., more_results: bool = ..., last_id: _Optional[str] = ...) -> None: ...

class GetCollectionEntriesReq(_message.Message):
    __slots__ = ("collection_id", "page_size", "search_after_id")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_AFTER_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    page_size: int
    search_after_id: str
    def __init__(self, collection_id: _Optional[str] = ..., page_size: _Optional[int] = ..., search_after_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetCollectionEntriesRes(_message.Message):
    __slots__ = ("metadata", "entries")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    metadata: CollectionMetadata
    entries: _containers.RepeatedCompositeFieldContainer[CollectionEntry]
    def __init__(self, metadata: _Optional[_Union[CollectionMetadata, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[CollectionEntry, _Mapping]]] = ...) -> None: ...

class DeleteCollectionEntryReq(_message.Message):
    __slots__ = ("collection_id", "entry_id")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    entry_id: str
    def __init__(self, collection_id: _Optional[str] = ..., entry_id: _Optional[str] = ...) -> None: ...

class ListCampaignLinksRes(_message.Message):
    __slots__ = ("Links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    Links: _containers.RepeatedCompositeFieldContainer[Link]
    def __init__(self, Links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("xml_client_prop_sid", "name", "description")
    XML_CLIENT_PROP_SID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    xml_client_prop_sid: int
    name: str
    description: str
    def __init__(self, xml_client_prop_sid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CjsSearchField(_message.Message):
    __slots__ = ("cjs_search_field_id", "cjs_search_definition_id", "field_name", "field_type", "field_value")
    CJS_SEARCH_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    CJS_SEARCH_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    cjs_search_field_id: str
    cjs_search_definition_id: str
    field_name: str
    field_type: _lms_pb2.FieldType
    field_value: str
    def __init__(self, cjs_search_field_id: _Optional[str] = ..., cjs_search_definition_id: _Optional[str] = ..., field_name: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.FieldType, str]] = ..., field_value: _Optional[str] = ...) -> None: ...

class CjsSearchDefinitionMetadata(_message.Message):
    __slots__ = ("cjs_search_definition_id", "name", "description", "deleted", "exec_count", "exec_success", "exec_fail", "created_date", "last_edited")
    CJS_SEARCH_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    EXEC_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXEC_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    EXEC_FAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    cjs_search_definition_id: str
    name: str
    description: str
    deleted: bool
    exec_count: int
    exec_success: int
    exec_fail: int
    created_date: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, cjs_search_definition_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., deleted: bool = ..., exec_count: _Optional[int] = ..., exec_success: _Optional[int] = ..., exec_fail: _Optional[int] = ..., created_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CjsSearchDefinition(_message.Message):
    __slots__ = ("metadata", "search_fields", "whitelisted_return_fields", "blacklisted_return_fields", "unique_identifiers")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_RETURN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_RETURN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    metadata: CjsSearchDefinitionMetadata
    search_fields: _containers.RepeatedCompositeFieldContainer[CjsSearchField]
    whitelisted_return_fields: _containers.RepeatedCompositeFieldContainer[CjsSearchField]
    blacklisted_return_fields: _containers.RepeatedCompositeFieldContainer[CjsSearchField]
    unique_identifiers: _containers.RepeatedCompositeFieldContainer[CjsSearchField]
    def __init__(self, metadata: _Optional[_Union[CjsSearchDefinitionMetadata, _Mapping]] = ..., search_fields: _Optional[_Iterable[_Union[CjsSearchField, _Mapping]]] = ..., whitelisted_return_fields: _Optional[_Iterable[_Union[CjsSearchField, _Mapping]]] = ..., blacklisted_return_fields: _Optional[_Iterable[_Union[CjsSearchField, _Mapping]]] = ..., unique_identifiers: _Optional[_Iterable[_Union[CjsSearchField, _Mapping]]] = ...) -> None: ...

class GetCjsSearchDefinitionReq(_message.Message):
    __slots__ = ("cjs_search_definition_id",)
    CJS_SEARCH_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    cjs_search_definition_id: str
    def __init__(self, cjs_search_definition_id: _Optional[str] = ...) -> None: ...

class DeleteCjsSearchDefinitionReq(_message.Message):
    __slots__ = ("cjs_search_definition_id",)
    CJS_SEARCH_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    cjs_search_definition_id: str
    def __init__(self, cjs_search_definition_id: _Optional[str] = ...) -> None: ...

class ListCjsSearchDefinitionsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCjsSearchDefinitionsRes(_message.Message):
    __slots__ = ("definitions",)
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.RepeatedCompositeFieldContainer[CjsSearchDefinitionMetadata]
    def __init__(self, definitions: _Optional[_Iterable[_Union[CjsSearchDefinitionMetadata, _Mapping]]] = ...) -> None: ...

class ExecuteCjsSearchDefinitionReq(_message.Message):
    __slots__ = ("search_definition_id", "search_fields")
    SEARCH_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    search_definition_id: str
    search_fields: _containers.RepeatedCompositeFieldContainer[CjsExecuteSearchField]
    def __init__(self, search_definition_id: _Optional[str] = ..., search_fields: _Optional[_Iterable[_Union[CjsExecuteSearchField, _Mapping]]] = ...) -> None: ...

class ExecuteCjsSearchDefinitionRes(_message.Message):
    __slots__ = ("collection_entries",)
    COLLECTION_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    collection_entries: _containers.RepeatedCompositeFieldContainer[CollectionEntries]
    def __init__(self, collection_entries: _Optional[_Iterable[_Union[CollectionEntries, _Mapping]]] = ...) -> None: ...

class CollectionEntries(_message.Message):
    __slots__ = ("metadata", "entries")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    metadata: CollectionMetadata
    entries: _containers.RepeatedCompositeFieldContainer[CollectionEntry]
    def __init__(self, metadata: _Optional[_Union[CollectionMetadata, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[CollectionEntry, _Mapping]]] = ...) -> None: ...

class CjsExecuteSearchField(_message.Message):
    __slots__ = ("field_name", "field_type", "field_value")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    field_type: _lms_pb2.FieldType
    field_value: str
    def __init__(self, field_name: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.FieldType, str]] = ..., field_value: _Optional[str] = ...) -> None: ...

class CjsSecureSearchCriteriaMetadata(_message.Message):
    __slots__ = ("cjs_secure_search_criteria_id", "deleted", "created_on", "last_updated")
    CJS_SECURE_SEARCH_CRITERIA_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    cjs_secure_search_criteria_id: str
    deleted: bool
    created_on: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, cjs_secure_search_criteria_id: _Optional[str] = ..., deleted: bool = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CjsSecureSearchCriteria(_message.Message):
    __slots__ = ("metadata", "fields")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    metadata: CjsSecureSearchCriteriaMetadata
    fields: _containers.RepeatedCompositeFieldContainer[CjsSecureSearchCriteriaField]
    def __init__(self, metadata: _Optional[_Union[CjsSecureSearchCriteriaMetadata, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[CjsSecureSearchCriteriaField, _Mapping]]] = ...) -> None: ...

class GetCjsSecureSearchCriteriaReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CjsSecureSearchCriteriaField(_message.Message):
    __slots__ = ("cjs_secure_search_criteria_field_id", "cjs_secure_search_criteria_id", "field_type")
    CJS_SECURE_SEARCH_CRITERIA_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    CJS_SECURE_SEARCH_CRITERIA_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    cjs_secure_search_criteria_field_id: str
    cjs_secure_search_criteria_id: str
    field_type: _lms_pb2.FieldType
    def __init__(self, cjs_secure_search_criteria_field_id: _Optional[str] = ..., cjs_secure_search_criteria_id: _Optional[str] = ..., field_type: _Optional[_Union[_lms_pb2.FieldType, str]] = ...) -> None: ...

class SplitCriteria(_message.Message):
    __slots__ = ("unique", "max_size", "equal_parts")
    UNIQUE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    EQUAL_PARTS_FIELD_NUMBER: _ClassVar[int]
    unique: SplitByUnique
    max_size: SplitByMaxSize
    equal_parts: SplitByEqualParts
    def __init__(self, unique: _Optional[_Union[SplitByUnique, _Mapping]] = ..., max_size: _Optional[_Union[SplitByMaxSize, _Mapping]] = ..., equal_parts: _Optional[_Union[SplitByEqualParts, _Mapping]] = ...) -> None: ...

class UniquePair(_message.Message):
    __slots__ = ("split_on_fields", "split_value")
    SPLIT_ON_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SPLIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    split_on_fields: FieldIndex
    split_value: str
    def __init__(self, split_on_fields: _Optional[_Union[FieldIndex, _Mapping]] = ..., split_value: _Optional[str] = ...) -> None: ...

class SplitByNamedUnique(_message.Message):
    __slots__ = ("named_fields",)
    NAMED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    named_fields: _containers.RepeatedCompositeFieldContainer[UniquePair]
    def __init__(self, named_fields: _Optional[_Iterable[_Union[UniquePair, _Mapping]]] = ...) -> None: ...

class SplitByUnique(_message.Message):
    __slots__ = ("split_on_fields",)
    SPLIT_ON_FIELDS_FIELD_NUMBER: _ClassVar[int]
    split_on_fields: _containers.RepeatedCompositeFieldContainer[FieldIndex]
    def __init__(self, split_on_fields: _Optional[_Iterable[_Union[FieldIndex, _Mapping]]] = ...) -> None: ...

class SplitByMaxSize(_message.Message):
    __slots__ = ("max_size",)
    MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    max_size: int
    def __init__(self, max_size: _Optional[int] = ...) -> None: ...

class SplitByEqualParts(_message.Message):
    __slots__ = ("part_size",)
    PART_SIZE_FIELD_NUMBER: _ClassVar[int]
    part_size: int
    def __init__(self, part_size: _Optional[int] = ...) -> None: ...

class EpicEntrypoint(_message.Message):
    __slots__ = ("cron", "max_wait_time", "entity_types", "group_base_url", "group_fhir_id", "runtime_values", "flush_page_count", "flush_minute_count", "flush_during_check", "timezone", "enabled", "fields", "raw_json", "non_prod", "auth_server")
    CRON_FIELD_NUMBER: _ClassVar[int]
    MAX_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    GROUP_BASE_URL_FIELD_NUMBER: _ClassVar[int]
    GROUP_FHIR_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VALUES_FIELD_NUMBER: _ClassVar[int]
    FLUSH_PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLUSH_MINUTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DURING_CHECK_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    RAW_JSON_FIELD_NUMBER: _ClassVar[int]
    NON_PROD_FIELD_NUMBER: _ClassVar[int]
    AUTH_SERVER_FIELD_NUMBER: _ClassVar[int]
    cron: str
    max_wait_time: float
    entity_types: _containers.RepeatedScalarFieldContainer[EpicEntityType]
    group_base_url: str
    group_fhir_id: str
    runtime_values: RuntimeValues
    flush_page_count: int
    flush_minute_count: int
    flush_during_check: bool
    timezone: str
    enabled: bool
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    raw_json: bool
    non_prod: bool
    auth_server: str
    def __init__(self, cron: _Optional[str] = ..., max_wait_time: _Optional[float] = ..., entity_types: _Optional[_Iterable[_Union[EpicEntityType, str]]] = ..., group_base_url: _Optional[str] = ..., group_fhir_id: _Optional[str] = ..., runtime_values: _Optional[_Union[RuntimeValues, _Mapping]] = ..., flush_page_count: _Optional[int] = ..., flush_minute_count: _Optional[int] = ..., flush_during_check: bool = ..., timezone: _Optional[str] = ..., enabled: bool = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., raw_json: bool = ..., non_prod: bool = ..., auth_server: _Optional[str] = ...) -> None: ...

class RuntimeValues(_message.Message):
    __slots__ = ("state", "access_token", "check_url", "data_urls", "current_iteration", "total_seconds_spent", "errors", "total_not_ready_count", "file_ids", "preliminary_vars", "parent_event_ids", "no_more_pages", "total_fts_ids")
    class FileIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PreliminaryVarsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHECK_URL_FIELD_NUMBER: _ClassVar[int]
    DATA_URLS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ITERATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SECONDS_SPENT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NOT_READY_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    PRELIMINARY_VARS_FIELD_NUMBER: _ClassVar[int]
    PARENT_EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    NO_MORE_PAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FTS_IDS_FIELD_NUMBER: _ClassVar[int]
    state: _lms_pb2.EventState
    access_token: str
    check_url: str
    data_urls: _containers.RepeatedCompositeFieldContainer[EntityURL]
    current_iteration: int
    total_seconds_spent: int
    errors: _containers.RepeatedScalarFieldContainer[str]
    total_not_ready_count: int
    file_ids: _containers.ScalarMap[str, int]
    preliminary_vars: _containers.ScalarMap[str, str]
    parent_event_ids: _containers.RepeatedScalarFieldContainer[int]
    no_more_pages: bool
    total_fts_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, state: _Optional[_Union[_lms_pb2.EventState, str]] = ..., access_token: _Optional[str] = ..., check_url: _Optional[str] = ..., data_urls: _Optional[_Iterable[_Union[EntityURL, _Mapping]]] = ..., current_iteration: _Optional[int] = ..., total_seconds_spent: _Optional[int] = ..., errors: _Optional[_Iterable[str]] = ..., total_not_ready_count: _Optional[int] = ..., file_ids: _Optional[_Mapping[str, int]] = ..., preliminary_vars: _Optional[_Mapping[str, str]] = ..., parent_event_ids: _Optional[_Iterable[int]] = ..., no_more_pages: bool = ..., total_fts_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class EntityURL(_message.Message):
    __slots__ = ("entity_type", "url")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    entity_type: EpicEntityType
    url: str
    def __init__(self, entity_type: _Optional[_Union[EpicEntityType, str]] = ..., url: _Optional[str] = ...) -> None: ...

class SampleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EHREntityType(_message.Message):
    __slots__ = ("epic_entity",)
    EPIC_ENTITY_FIELD_NUMBER: _ClassVar[int]
    epic_entity: EpicEntityType
    def __init__(self, epic_entity: _Optional[_Union[EpicEntityType, str]] = ...) -> None: ...

class FinviEntrypoint(_message.Message):
    __slots__ = ("pool_id", "cron_interval", "disabled", "timezone", "filename_pattern")
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    CRON_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    pool_id: str
    cron_interval: str
    disabled: bool
    timezone: str
    filename_pattern: str
    def __init__(self, pool_id: _Optional[str] = ..., cron_interval: _Optional[str] = ..., disabled: bool = ..., timezone: _Optional[str] = ..., filename_pattern: _Optional[str] = ...) -> None: ...

class ContactManagementEnrichment(_message.Message):
    __slots__ = ("project_id", "contact_list_name", "fields", "de_duplication_info", "insert_if_missing")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DE_DUPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INSERT_IF_MISSING_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    contact_list_name: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    de_duplication_info: ContactManagerSink.DeDuplication
    insert_if_missing: bool
    def __init__(self, project_id: _Optional[str] = ..., contact_list_name: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ..., de_duplication_info: _Optional[_Union[ContactManagerSink.DeDuplication, _Mapping]] = ..., insert_if_missing: bool = ...) -> None: ...

class TicketExchangeSink(_message.Message):
    __slots__ = ("project_id", "template_id", "fields")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    template_id: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., template_id: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...
