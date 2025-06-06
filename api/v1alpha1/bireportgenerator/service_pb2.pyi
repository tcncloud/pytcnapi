from annotations import authz_pb2 as _authz_pb2
from api.commons import bireportgenerator_pb2 as _bireportgenerator_pb2
from api.v1alpha1.bireportgenerator import entities_pb2 as _entities_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateReportJobRequest(_message.Message):
    __slots__ = ("report_job",)
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ...) -> None: ...

class CreateReportJobResponse(_message.Message):
    __slots__ = ("report_job",)
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ...) -> None: ...

class ListReportJobsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListReportJobsResponse(_message.Message):
    __slots__ = ("report_jobs",)
    REPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    report_jobs: _containers.RepeatedCompositeFieldContainer[_entities_pb2.ReportJob]
    def __init__(self, report_jobs: _Optional[_Iterable[_Union[_entities_pb2.ReportJob, _Mapping]]] = ...) -> None: ...

class UpdateReportJobRequest(_message.Message):
    __slots__ = ("report_job", "update_mask")
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateReportJobResponse(_message.Message):
    __slots__ = ("report_job",)
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ...) -> None: ...

class DeleteReportJobRequest(_message.Message):
    __slots__ = ("report_job_id",)
    REPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    report_job_id: str
    def __init__(self, report_job_id: _Optional[str] = ...) -> None: ...

class DeleteReportJobResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetReportJobRequest(_message.Message):
    __slots__ = ("report_job_id",)
    REPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    report_job_id: str
    def __init__(self, report_job_id: _Optional[str] = ...) -> None: ...

class GetReportJobResponse(_message.Message):
    __slots__ = ("report_job",)
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ...) -> None: ...

class GenerateReportRequest(_message.Message):
    __slots__ = ("report_job", "send_as_of_date")
    REPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    SEND_AS_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    report_job: _entities_pb2.ReportJob
    send_as_of_date: _timestamp_pb2.Timestamp
    def __init__(self, report_job: _Optional[_Union[_entities_pb2.ReportJob, _Mapping]] = ..., send_as_of_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateReportResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListReportLogsStreamRequest(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListReportLogsStreamResponse(_message.Message):
    __slots__ = ("report_log",)
    REPORT_LOG_FIELD_NUMBER: _ClassVar[int]
    report_log: _entities_pb2.ReportLog
    def __init__(self, report_log: _Optional[_Union[_entities_pb2.ReportLog, _Mapping]] = ...) -> None: ...
