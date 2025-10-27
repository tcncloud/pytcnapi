import datetime

from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons.integrations import integrations_pb2 as _integrations_pb2
from api.commons.org import huntgroup_pb2 as _huntgroup_pb2
from api.commons import perms_pb2 as _perms_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[PrivateFieldType]
    PRIVATE_KEY: _ClassVar[PrivateFieldType]
UNKNOWN: PrivateFieldType
PRIVATE_KEY: PrivateFieldType

class ListJourneyConfigsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListNonJourneyConfigsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntegrationConfigs(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[IntegrationConfig]
    def __init__(self, values: _Optional[_Iterable[_Union[IntegrationConfig, _Mapping]]] = ...) -> None: ...

class GetIntegrationConfigReq(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    name: str
    id: str
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class UpdateIntegrationConfigReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    integration_id: _integrations_pb2.IntegrationType
    name: str
    description: str
    params: Values
    def __init__(self, id: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., params: _Optional[_Union[Values, _Mapping]] = ...) -> None: ...

class DeleteIntegrationConfigReq(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    name: str
    id: str
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ProcessReq(_message.Message):
    __slots__ = ()
    class ParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CONDS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    integration_id: _integrations_pb2.IntegrationType
    method_id: _integrations_pb2.RequestMethod
    config_name: str
    config_id: str
    params: _containers.MessageMap[str, Value]
    conds: _containers.RepeatedCompositeFieldContainer[Condition]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    request_origin: _integrations_pb2.RequestOrigin
    def __init__(self, request_id: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., config_name: _Optional[str] = ..., config_id: _Optional[str] = ..., params: _Optional[_Mapping[str, Value]] = ..., conds: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ...) -> None: ...

class ProcessRes(_message.Message):
    __slots__ = ()
    class DataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    result: bool
    data: _containers.MessageMap[str, Value]
    integration: str
    method: str
    transaction_id: str
    def __init__(self, result: _Optional[bool] = ..., data: _Optional[_Mapping[str, Value]] = ..., integration: _Optional[str] = ..., method: _Optional[str] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class SearchPastTransactionsRequest(_message.Message):
    __slots__ = ()
    class MatchFieldsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INT_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BEFORE_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    int_id: _integrations_pb2.IntegrationType
    method_id: _integrations_pb2.RequestMethod
    match_fields: _containers.ScalarMap[str, str]
    limit: int
    search_before: _timestamp_pb2.Timestamp
    def __init__(self, plugin_instance_id: _Optional[str] = ..., int_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., match_fields: _Optional[_Mapping[str, str]] = ..., limit: _Optional[int] = ..., search_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchPastTransactionsResponse(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PastTxEntity]
    def __init__(self, values: _Optional[_Iterable[_Union[PastTxEntity, _Mapping]]] = ...) -> None: ...

class PastTxEntity(_message.Message):
    __slots__ = ()
    class ReqEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REQ_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    req: _containers.ScalarMap[str, str]
    res: _containers.ScalarMap[str, str]
    created_on: _timestamp_pb2.Timestamp
    def __init__(self, req: _Optional[_Mapping[str, str]] = ..., res: _Optional[_Mapping[str, str]] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListIntegrationsForOrgReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntegrationInfos(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[IntegrationInfo]
    def __init__(self, values: _Optional[_Iterable[_Union[IntegrationInfo, _Mapping]]] = ...) -> None: ...

class IntegrationInfo(_message.Message):
    __slots__ = ()
    class GroupParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Parameter
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Parameter, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    integration_id: _integrations_pb2.IntegrationType
    description: str
    methods: _containers.RepeatedCompositeFieldContainer[MethodInfo]
    group_params: _containers.MessageMap[int, Parameter]
    def __init__(self, name: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., description: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[MethodInfo, _Mapping]]] = ..., group_params: _Optional[_Mapping[int, Parameter]] = ...) -> None: ...

class MethodInfo(_message.Message):
    __slots__ = ()
    class RuntimeParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Parameter
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Parameter, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TX_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    method_id: _integrations_pb2.RequestMethod
    tx_type: _integrations_pb2.TransactionType
    params: _containers.RepeatedCompositeFieldContainer[Parameter]
    url: str
    response: _containers.RepeatedCompositeFieldContainer[Parameter]
    runtime_params: _containers.MessageMap[int, Parameter]
    def __init__(self, name: _Optional[str] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., tx_type: _Optional[_Union[_integrations_pb2.TransactionType, str]] = ..., params: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ..., url: _Optional[str] = ..., response: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ..., runtime_params: _Optional[_Mapping[int, Parameter]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_PARAM_FIELD_NUMBER: _ClassVar[int]
    HELPER_TEXT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_LOCKED_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    param_type: _integrations_pb2.ValueType
    required: bool
    default_value: Value
    display_name: str
    sensitive: bool
    runtime_param: bool
    helper_text: str
    template_locked: bool
    validation: _integrations_pb2.Validation
    def __init__(self, name: _Optional[str] = ..., param_type: _Optional[_Union[_integrations_pb2.ValueType, str]] = ..., required: _Optional[bool] = ..., default_value: _Optional[_Union[Value, _Mapping]] = ..., display_name: _Optional[str] = ..., sensitive: _Optional[bool] = ..., runtime_param: _Optional[bool] = ..., helper_text: _Optional[str] = ..., template_locked: _Optional[bool] = ..., validation: _Optional[_Union[_integrations_pb2.Validation, str]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIntegrationTransactionReq(_message.Message):
    __slots__ = ()
    INTEGRATION_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    integration_transaction_id: str
    def __init__(self, integration_transaction_id: _Optional[str] = ...) -> None: ...

class GetAggregatedMetadataReq(_message.Message):
    __slots__ = ()
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    method_id: _integrations_pb2.RequestMethod
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ...) -> None: ...

class GetAggregatedMetadataRes(_message.Message):
    __slots__ = ()
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    views: int
    verify_attempts: int
    verify_successes: int
    payment_attempts: int
    payment_successes: int
    payment_amount: float
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, views: _Optional[int] = ..., verify_attempts: _Optional[int] = ..., verify_successes: _Optional[int] = ..., payment_attempts: _Optional[int] = ..., payment_successes: _Optional[int] = ..., payment_amount: _Optional[float] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...

class GetIntegrationTransactionReportReq(_message.Message):
    __slots__ = ()
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    group_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., group_by: _Optional[_Iterable[str]] = ...) -> None: ...

class IntegrationTransactionReportRow(_message.Message):
    __slots__ = ()
    class GroupByValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RevenueSubtotalsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    class CountMetricsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FLOW_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REVENUE_FIELD_NUMBER: _ClassVar[int]
    REVENUE_SUBTOTALS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_TRAFFIC_DATE_FIELD_NUMBER: _ClassVar[int]
    LOWEST_TRAFFIC_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_METRICS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    integration_name: str
    method_id: _integrations_pb2.RequestMethod
    method_name: str
    transaction_type: _integrations_pb2.TransactionType
    request_source: _integrations_pb2.RequestSource
    flow_name: str
    campaign_type: str
    group_by_values: _containers.ScalarMap[str, str]
    revenue: float
    revenue_subtotals: _containers.ScalarMap[str, float]
    success_count: int
    failure_count: int
    total_count: int
    highest_traffic_date: str
    lowest_traffic_date: str
    count_metrics: _containers.ScalarMap[str, int]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., integration_name: _Optional[str] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., method_name: _Optional[str] = ..., transaction_type: _Optional[_Union[_integrations_pb2.TransactionType, str]] = ..., request_source: _Optional[_Union[_integrations_pb2.RequestSource, str]] = ..., flow_name: _Optional[str] = ..., campaign_type: _Optional[str] = ..., group_by_values: _Optional[_Mapping[str, str]] = ..., revenue: _Optional[float] = ..., revenue_subtotals: _Optional[_Mapping[str, float]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., total_count: _Optional[int] = ..., highest_traffic_date: _Optional[str] = ..., lowest_traffic_date: _Optional[str] = ..., count_metrics: _Optional[_Mapping[str, int]] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...

class GetIntegrationTransactionReportRes(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[IntegrationTransactionReportRow]
    def __init__(self, values: _Optional[_Iterable[_Union[IntegrationTransactionReportRow, _Mapping]]] = ...) -> None: ...

class GetIntegrationTransactionReportDataReq(_message.Message):
    __slots__ = ()
    class GroupByEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUM_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_AFTER_SID_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    group_by: _containers.ScalarMap[str, str]
    page_size: int
    page_num: int
    integration_id: _integrations_pb2.IntegrationType
    search_after_sid: int
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., group_by: _Optional[_Mapping[str, str]] = ..., page_size: _Optional[int] = ..., page_num: _Optional[int] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., search_after_sid: _Optional[int] = ...) -> None: ...

class GetIntegrationTransactionReportDataRow(_message.Message):
    __slots__ = ()
    class CountMetricsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LinkDataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COUNT_METRICS_FIELD_NUMBER: _ClassVar[int]
    LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    count_metrics: _containers.ScalarMap[str, int]
    link_data: _containers.ScalarMap[str, str]
    date: _timestamp_pb2.Timestamp
    payment_amount: float
    def __init__(self, count_metrics: _Optional[_Mapping[str, int]] = ..., link_data: _Optional[_Mapping[str, str]] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payment_amount: _Optional[float] = ...) -> None: ...

class GetIntegrationTransactionReportDataRes(_message.Message):
    __slots__ = ()
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSACTION_SID_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[GetIntegrationTransactionReportDataRow]
    last_transaction_sid: int
    def __init__(self, entities: _Optional[_Iterable[_Union[GetIntegrationTransactionReportDataRow, _Mapping]]] = ..., last_transaction_sid: _Optional[int] = ...) -> None: ...

class SearchIntegrationTransactionsReq(_message.Message):
    __slots__ = ()
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METHOD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    integration_type: IntegrationType
    request_method: RequestMethod
    transaction_type: TransactionType
    request_source: RequestSource
    result: TransactionResult
    task_id: str
    def __init__(self, start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., integration_type: _Optional[_Union[IntegrationType, _Mapping]] = ..., request_method: _Optional[_Union[RequestMethod, _Mapping]] = ..., transaction_type: _Optional[_Union[TransactionType, _Mapping]] = ..., request_source: _Optional[_Union[RequestSource, _Mapping]] = ..., result: _Optional[_Union[TransactionResult, _Mapping]] = ..., task_id: _Optional[str] = ...) -> None: ...

class SearchIntegrationTransactionsRes(_message.Message):
    __slots__ = ()
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[IntegrationTransaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[IntegrationTransaction, _Mapping]]] = ...) -> None: ...

class IntegrationType(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ...) -> None: ...

class RequestMethod(_message.Message):
    __slots__ = ()
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    method_id: _integrations_pb2.RequestMethod
    def __init__(self, method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ...) -> None: ...

class TransactionType(_message.Message):
    __slots__ = ()
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    transaction_type: _integrations_pb2.TransactionType
    def __init__(self, transaction_type: _Optional[_Union[_integrations_pb2.TransactionType, str]] = ...) -> None: ...

class RequestSource(_message.Message):
    __slots__ = ()
    REQUEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    request_source: _integrations_pb2.RequestSource
    def __init__(self, request_source: _Optional[_Union[_integrations_pb2.RequestSource, str]] = ...) -> None: ...

class TransactionResult(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _integrations_pb2.TransactionResult
    def __init__(self, result: _Optional[_Union[_integrations_pb2.TransactionResult, str]] = ...) -> None: ...

class ListIntegrationConfigNamesReq(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ...) -> None: ...

class ListIntegrationConfigNamesRes(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPaymentLinkConfigReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletePaymentLinkConfigReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Logo(_message.Message):
    __slots__ = ()
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class ListPortalConfigsReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    entity: PortalConfigId
    mask: _field_mask_pb2.FieldMask
    page_size: int
    page: int
    def __init__(self, entity: _Optional[_Union[PortalConfigId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., page_size: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetPortalConfigReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalConfigId
    mask: _field_mask_pb2.FieldMask
    id: str
    def __init__(self, entity: _Optional[_Union[PortalConfigId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeletePortalConfigReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    entity: PortalConfigId
    mask: _field_mask_pb2.FieldMask
    id: str
    def __init__(self, entity: _Optional[_Union[PortalConfigId, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class UpdatePortalLogoReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    id: str
    logo: bytes
    def __init__(self, id: _Optional[str] = ..., logo: _Optional[bytes] = ...) -> None: ...

class GetPortalLogoReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RefreshLinkReq(_message.Message):
    __slots__ = ()
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class RefreshLinkRes(_message.Message):
    __slots__ = ()
    NEW_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    new_expiry: _timestamp_pb2.Timestamp
    def __init__(self, new_expiry: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PaymentLinkConfig(_message.Message):
    __slots__ = ()
    class NameMappingEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BaseDataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DAYS_FIELD_NUMBER: _ClassVar[int]
    LINKS_REFRESHABLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_LINK_VALID_HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_REFRESH_TIMES_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INVOICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    BASE_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    collection_id: str
    integration_id: _integrations_pb2.IntegrationType
    verification_method_id: _integrations_pb2.RequestMethod
    invoice_method_id: _integrations_pb2.RequestMethod
    payment_method_id: _integrations_pb2.RequestMethod
    name_mapping: _containers.ScalarMap[str, str]
    verification_fields: _containers.RepeatedScalarFieldContainer[str]
    payment_portal_id: str
    created_on: _timestamp_pb2.Timestamp
    expiry_days: int
    links_refreshable: bool
    refresh_link_valid_hours: float
    max_refresh_times: int
    verification_request: VerificationRequest
    invoice_request: InvoiceRequest
    payment_requests: _containers.RepeatedCompositeFieldContainer[PaymentRequest]
    base_data: _containers.MessageMap[str, Value]
    templates: PaymentLinkConfigTemplates
    payment_profile_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., collection_id: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., verification_method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., invoice_method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., payment_method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., name_mapping: _Optional[_Mapping[str, str]] = ..., verification_fields: _Optional[_Iterable[str]] = ..., payment_portal_id: _Optional[str] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiry_days: _Optional[int] = ..., links_refreshable: _Optional[bool] = ..., refresh_link_valid_hours: _Optional[float] = ..., max_refresh_times: _Optional[int] = ..., verification_request: _Optional[_Union[VerificationRequest, _Mapping]] = ..., invoice_request: _Optional[_Union[InvoiceRequest, _Mapping]] = ..., payment_requests: _Optional[_Iterable[_Union[PaymentRequest, _Mapping]]] = ..., base_data: _Optional[_Mapping[str, Value]] = ..., templates: _Optional[_Union[PaymentLinkConfigTemplates, _Mapping]] = ..., payment_profile_name: _Optional[str] = ...) -> None: ...

class PaymentLinkConfigTemplates(_message.Message):
    __slots__ = ()
    RECEIPT_SMS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_SMS_SOURCE_PHONE_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_EMAIL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_EMAIL_FROM_ADDR_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    receipt_sms_template: str
    receipt_sms_source_phone: str
    receipt_email_template: str
    receipt_email_from_addr: str
    receipt_template: str
    invoice_template: str
    def __init__(self, receipt_sms_template: _Optional[str] = ..., receipt_sms_source_phone: _Optional[str] = ..., receipt_email_template: _Optional[str] = ..., receipt_email_from_addr: _Optional[str] = ..., receipt_template: _Optional[str] = ..., invoice_template: _Optional[str] = ...) -> None: ...

class VerificationRequest(_message.Message):
    __slots__ = ()
    VERIFICATION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    verification_requests: _containers.RepeatedCompositeFieldContainer[Request]
    verification_fields: _containers.RepeatedCompositeFieldContainer[Parameter]
    def __init__(self, verification_requests: _Optional[_Iterable[_Union[Request, _Mapping]]] = ..., verification_fields: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ...) -> None: ...

class PaymentRequest(_message.Message):
    __slots__ = ()
    PAYMENT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_REQUEST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    payment_fields: _containers.RepeatedCompositeFieldContainer[Parameter]
    payment_request_payload: _containers.RepeatedCompositeFieldContainer[Request]
    payment_request: Request
    name: str
    description: str
    def __init__(self, payment_fields: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ..., payment_request_payload: _Optional[_Iterable[_Union[Request, _Mapping]]] = ..., payment_request: _Optional[_Union[Request, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class InvoiceRequest(_message.Message):
    __slots__ = ()
    INVOICE_REQUEST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    INVOICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FILTER_RESPONSE_KEYS_FIELD_NUMBER: _ClassVar[int]
    invoice_request_payload: _containers.RepeatedCompositeFieldContainer[Request]
    invoice_request: Request
    filter_response_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, invoice_request_payload: _Optional[_Iterable[_Union[Request, _Mapping]]] = ..., invoice_request: _Optional[_Union[Request, _Mapping]] = ..., filter_response_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ()
    class StaticDataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class RenameResponseKeysEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ReassignValidationsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Validation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Validation, _Mapping]] = ...) -> None: ...
    JOURNEY_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_CALL_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    STATIC_DATA_FIELD_NUMBER: _ClassVar[int]
    RENAME_RESPONSE_KEYS_FIELD_NUMBER: _ClassVar[int]
    REASSIGN_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    journey_collection_id: str
    method_call: MethodCall
    config_id: str
    static_data: _containers.MessageMap[str, Value]
    rename_response_keys: _containers.ScalarMap[str, str]
    reassign_validations: _containers.MessageMap[str, Validation]
    def __init__(self, journey_collection_id: _Optional[str] = ..., method_call: _Optional[_Union[MethodCall, _Mapping]] = ..., config_id: _Optional[str] = ..., static_data: _Optional[_Mapping[str, Value]] = ..., rename_response_keys: _Optional[_Mapping[str, str]] = ..., reassign_validations: _Optional[_Mapping[str, Validation]] = ...) -> None: ...

class Validation(_message.Message):
    __slots__ = ()
    ENUM_FIELD_NUMBER: _ClassVar[int]
    enum: _integrations_pb2.Validation
    def __init__(self, enum: _Optional[_Union[_integrations_pb2.Validation, str]] = ...) -> None: ...

class MethodCall(_message.Message):
    __slots__ = ()
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    integration_id: _integrations_pb2.IntegrationType
    method_id: _integrations_pb2.RequestMethod
    def __init__(self, integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ...) -> None: ...

class PortalConfigs(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PortalConfig]
    def __init__(self, values: _Optional[_Iterable[_Union[PortalConfig, _Mapping]]] = ...) -> None: ...

class ListPaymentLinkConfigsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaymentLinkConfigs(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PaymentLinkConfig]
    def __init__(self, values: _Optional[_Iterable[_Union[PaymentLinkConfig, _Mapping]]] = ...) -> None: ...

class ListLinksReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePaymentPortalLinksReq(_message.Message):
    __slots__ = ()
    LINK_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_FIELD_NUMBER: _ClassVar[int]
    link_config_id: str
    expiry: _timestamp_pb2.Timestamp
    user_data: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, link_config_id: _Optional[str] = ..., expiry: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_data: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class CreatePaymentPortalLinksRes(_message.Message):
    __slots__ = ()
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, urls: _Optional[_Iterable[str]] = ...) -> None: ...

class SummaryReq(_message.Message):
    __slots__ = ()
    YEAR_FIELD_NUMBER: _ClassVar[int]
    year: int
    def __init__(self, year: _Optional[int] = ...) -> None: ...

class SummaryRes(_message.Message):
    __slots__ = ()
    YEAR_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    MONTH_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    WEEK_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    year_summary: CalendarSummary
    month_summaries: _containers.RepeatedCompositeFieldContainer[CalendarSummary]
    week_summaries: _containers.RepeatedCompositeFieldContainer[CalendarSummary]
    def __init__(self, year_summary: _Optional[_Union[CalendarSummary, _Mapping]] = ..., month_summaries: _Optional[_Iterable[_Union[CalendarSummary, _Mapping]]] = ..., week_summaries: _Optional[_Iterable[_Union[CalendarSummary, _Mapping]]] = ...) -> None: ...

class CalendarSummary(_message.Message):
    __slots__ = ()
    CALENDAR_NUM_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TYPE_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    calendar_num: int
    summary: TransactionSummary
    type_summaries: _containers.RepeatedCompositeFieldContainer[IntegrationTypeSummary]
    def __init__(self, calendar_num: _Optional[int] = ..., summary: _Optional[_Union[TransactionSummary, _Mapping]] = ..., type_summaries: _Optional[_Iterable[_Union[IntegrationTypeSummary, _Mapping]]] = ...) -> None: ...

class IntegrationTypeSummary(_message.Message):
    __slots__ = ()
    INTEGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    integration_type: _integrations_pb2.IntegrationType
    integration_summary: TransactionSummary
    def __init__(self, integration_type: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., integration_summary: _Optional[_Union[TransactionSummary, _Mapping]] = ...) -> None: ...

class TransactionSummary(_message.Message):
    __slots__ = ()
    TOTAL_TRANSACTIONS_ATTEMPTED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRANSACTIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRANSACTIONS_FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    AVG_AMOUNT_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    total_transactions_attempted: int
    total_transactions_completed: int
    total_transactions_failed: int
    total_amount_collected: float
    avg_amount_collected: float
    def __init__(self, total_transactions_attempted: _Optional[int] = ..., total_transactions_completed: _Optional[int] = ..., total_transactions_failed: _Optional[int] = ..., total_amount_collected: _Optional[float] = ..., avg_amount_collected: _Optional[float] = ...) -> None: ...

class ListIntegrationTemplatesByConfigReq(_message.Message):
    __slots__ = ()
    INTEGRATION_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    integration_config_name: str
    def __init__(self, integration_config_name: _Optional[str] = ...) -> None: ...

class ListIntegrationTemplatesByConfigRes(_message.Message):
    __slots__ = ()
    INTEGRATION_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    integration_templates: _containers.RepeatedCompositeFieldContainer[IntegrationTemplateInfo]
    def __init__(self, integration_templates: _Optional[_Iterable[_Union[IntegrationTemplateInfo, _Mapping]]] = ...) -> None: ...

class IntegrationTemplateInfo(_message.Message):
    __slots__ = ()
    BROADCAST_TEMPLATE_SID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    broadcast_template_sid: int
    template_name: str
    def __init__(self, broadcast_template_sid: _Optional[int] = ..., template_name: _Optional[str] = ...) -> None: ...

class CopyPaymentLinkConfigReq(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CopyPaymentLinkConfigRes(_message.Message):
    __slots__ = ()
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    new_name: str
    def __init__(self, new_name: _Optional[str] = ...) -> None: ...

class ProfileName(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PaymentProfiles(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PaymentProfile]
    def __init__(self, values: _Optional[_Iterable[_Union[PaymentProfile, _Mapping]]] = ...) -> None: ...

class PaymentProfile(_message.Message):
    __slots__ = ()
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    verification: str
    invoice: str
    payments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, verification: _Optional[str] = ..., invoice: _Optional[str] = ..., payments: _Optional[_Iterable[str]] = ...) -> None: ...

class UnknownField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_NEEDED_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_SOURCES_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    reason_needed: str
    potential_sources: _containers.RepeatedScalarFieldContainer[_integrations_pb2.FieldSource]
    suggested_fields: _containers.RepeatedCompositeFieldContainer[ProvidedField]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., reason_needed: _Optional[str] = ..., potential_sources: _Optional[_Iterable[_Union[_integrations_pb2.FieldSource, str]]] = ..., suggested_fields: _Optional[_Iterable[_Union[ProvidedField, _Mapping]]] = ...) -> None: ...

class ProvidedField(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ALT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDED_BY_FIELD_NUMBER: _ClassVar[int]
    PROVIDED_BY_DETAILS_NUM_FIELD_NUMBER: _ClassVar[int]
    PROVIDED_BY_DETAILS_STR_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    alt_name: str
    provided_by: _integrations_pb2.FieldSource
    provided_by_details_num: int
    provided_by_details_str: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., alt_name: _Optional[str] = ..., provided_by: _Optional[_Union[_integrations_pb2.FieldSource, str]] = ..., provided_by_details_num: _Optional[int] = ..., provided_by_details_str: _Optional[str] = ...) -> None: ...

class Values(_message.Message):
    __slots__ = ()
    class ValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, Value]
    def __init__(self, values: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ()
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    NUM_VAL_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    TIME_VAL_FIELD_NUMBER: _ClassVar[int]
    COMP_VAL_FIELD_NUMBER: _ClassVar[int]
    INT_VAL_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    str_val: str
    num_val: float
    bool_val: bool
    time_val: _timestamp_pb2.Timestamp
    comp_val: CompositeVal
    int_val: int
    sensitive: bool
    validation: _integrations_pb2.Validation
    def __init__(self, str_val: _Optional[str] = ..., num_val: _Optional[float] = ..., bool_val: _Optional[bool] = ..., time_val: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comp_val: _Optional[_Union[CompositeVal, _Mapping]] = ..., int_val: _Optional[int] = ..., sensitive: _Optional[bool] = ..., validation: _Optional[_Union[_integrations_pb2.Validation, str]] = ...) -> None: ...

class FieldOrStr(_message.Message):
    __slots__ = ()
    FIELD_FIELD_NUMBER: _ClassVar[int]
    STR_VAL_FIELD_NUMBER: _ClassVar[int]
    field: str
    str_val: str
    def __init__(self, field: _Optional[str] = ..., str_val: _Optional[str] = ...) -> None: ...

class CompositeVal(_message.Message):
    __slots__ = ()
    PARTS_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[FieldOrStr]
    def __init__(self, parts: _Optional[_Iterable[_Union[FieldOrStr, _Mapping]]] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    op: _integrations_pb2.CompareOperation
    value: Value
    def __init__(self, key: _Optional[str] = ..., op: _Optional[_Union[_integrations_pb2.CompareOperation, str]] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...

class IntegrationConfig(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    CONDS_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    integration_id: _integrations_pb2.IntegrationType
    name: str
    description: str
    params: Values
    deleted: bool
    created_on: _timestamp_pb2.Timestamp
    alias: MapString
    conds: Conditions
    method_id: _integrations_pb2.RequestMethod
    def __init__(self, id: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., params: _Optional[_Union[Values, _Mapping]] = ..., deleted: _Optional[bool] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., alias: _Optional[_Union[MapString, _Mapping]] = ..., conds: _Optional[_Union[Conditions, _Mapping]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ...) -> None: ...

class IntegrationTransaction(_message.Message):
    __slots__ = ()
    INTEGRATION_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    integration_transaction_id: str
    task_id: str
    integration_id: _integrations_pb2.IntegrationType
    method_id: _integrations_pb2.RequestMethod
    transaction_type: _integrations_pb2.TransactionType
    request_source: _integrations_pb2.RequestSource
    result: _integrations_pb2.TransactionResult
    amount_collected: float
    request_data: Values
    response_data: Values
    created_on: _timestamp_pb2.Timestamp
    config_name: str
    conds: Conditions
    request_origin: _integrations_pb2.RequestOrigin
    def __init__(self, integration_transaction_id: _Optional[str] = ..., task_id: _Optional[str] = ..., integration_id: _Optional[_Union[_integrations_pb2.IntegrationType, str]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., transaction_type: _Optional[_Union[_integrations_pb2.TransactionType, str]] = ..., request_source: _Optional[_Union[_integrations_pb2.RequestSource, str]] = ..., result: _Optional[_Union[_integrations_pb2.TransactionResult, str]] = ..., amount_collected: _Optional[float] = ..., request_data: _Optional[_Union[Values, _Mapping]] = ..., response_data: _Optional[_Union[Values, _Mapping]] = ..., created_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., config_name: _Optional[str] = ..., conds: _Optional[_Union[Conditions, _Mapping]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ...) -> None: ...

class MapString(_message.Message):
    __slots__ = ()
    class ValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.ScalarMap[str, str]
    def __init__(self, values: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Conditions(_message.Message):
    __slots__ = ()
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Condition]
    def __init__(self, values: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ()
    class ValuesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, Value]
    task_id: str
    src: _integrations_pb2.RequestSource
    def __init__(self, values: _Optional[_Mapping[str, Value]] = ..., task_id: _Optional[str] = ..., src: _Optional[_Union[_integrations_pb2.RequestSource, str]] = ...) -> None: ...

class PortalConfigId(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PortalConfig(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAT_CLIENT_LINK_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONTACT_PHONE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    chat_client_link: str
    contact_email: str
    contact_phone: str
    postal_code: str
    city: str
    state: str
    company_name: str
    logo: bytes
    primary_color: str
    secondary_color: str
    street_address: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., chat_client_link: _Optional[str] = ..., contact_email: _Optional[str] = ..., contact_phone: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., company_name: _Optional[str] = ..., logo: _Optional[bytes] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ..., street_address: _Optional[str] = ...) -> None: ...

class PortalLinkId(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PortalLink(_message.Message):
    __slots__ = ()
    class DataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    id: str
    portal_id: str
    plugin_instance_id: str
    portal_config_id: str
    task_id: str
    data: _containers.MessageMap[str, Value]
    metadata: _containers.MessageMap[str, Value]
    last_edited: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., portal_id: _Optional[str] = ..., plugin_instance_id: _Optional[str] = ..., portal_config_id: _Optional[str] = ..., task_id: _Optional[str] = ..., data: _Optional[_Mapping[str, Value]] = ..., metadata: _Optional[_Mapping[str, Value]] = ..., last_edited: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PortalId(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Portal(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INST_IDS_FIELD_NUMBER: _ClassVar[int]
    PTYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    PORTAL_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    portal_config_id: str
    plugin_inst_ids: _containers.RepeatedScalarFieldContainer[str]
    ptype: PortalType
    last_edited: _timestamp_pb2.Timestamp
    definition_name: str
    portal_segments: PortalSegments
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., portal_config_id: _Optional[str] = ..., plugin_inst_ids: _Optional[_Iterable[str]] = ..., ptype: _Optional[_Union[PortalType, _Mapping]] = ..., last_edited: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., definition_name: _Optional[str] = ..., portal_segments: _Optional[_Union[PortalSegments, _Mapping]] = ...) -> None: ...

class PortalSegments(_message.Message):
    __slots__ = ()
    PORTAL_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    portal_segments: _containers.RepeatedCompositeFieldContainer[PortalSegment]
    def __init__(self, portal_segments: _Optional[_Iterable[_Union[PortalSegment, _Mapping]]] = ...) -> None: ...

class PortalText(_message.Message):
    __slots__ = ()
    VERIFICATION_HEADER_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FOOTER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FOOTER_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_HEADER_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FOOTER_FIELD_NUMBER: _ClassVar[int]
    INVOICE_HEADER_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FOOTER_FIELD_NUMBER: _ClassVar[int]
    verification_header: str
    verification_footer: str
    payment_header: str
    payment_footer: str
    receipt_header: str
    receipt_footer: str
    invoice_header: str
    invoice_footer: str
    def __init__(self, verification_header: _Optional[str] = ..., verification_footer: _Optional[str] = ..., payment_header: _Optional[str] = ..., payment_footer: _Optional[str] = ..., receipt_header: _Optional[str] = ..., receipt_footer: _Optional[str] = ..., invoice_header: _Optional[str] = ..., invoice_footer: _Optional[str] = ...) -> None: ...

class PortalType(_message.Message):
    __slots__ = ()
    PAYMENT_PORTAL_FIELD_NUMBER: _ClassVar[int]
    IVR_PORTAL_FIELD_NUMBER: _ClassVar[int]
    payment_portal: PaymentPortal
    ivr_portal: IVRPortal
    def __init__(self, payment_portal: _Optional[_Union[PaymentPortal, _Mapping]] = ..., ivr_portal: _Optional[_Union[IVRPortal, _Mapping]] = ...) -> None: ...

class PaymentPortal(_message.Message):
    __slots__ = ()
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    PORTAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    verification: _integrations_pb2.VerificationFlow
    invoice: _integrations_pb2.InvoiceFlow
    payments: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.PaymentFlow]
    portal_text: PortalText
    def __init__(self, verification: _Optional[_Union[_integrations_pb2.VerificationFlow, _Mapping]] = ..., invoice: _Optional[_Union[_integrations_pb2.InvoiceFlow, _Mapping]] = ..., payments: _Optional[_Iterable[_Union[_integrations_pb2.PaymentFlow, _Mapping]]] = ..., portal_text: _Optional[_Union[PortalText, _Mapping]] = ...) -> None: ...

class IVRPortal(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PluginInstanceId(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PluginInstance(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_METHODS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    plugin_definition: str
    data: Values
    metadata: Values
    last_edited: _timestamp_pb2.Timestamp
    method_id: _integrations_pb2.RequestMethod
    display_methods: _containers.RepeatedScalarFieldContainer[_integrations_pb2.RequestMethod]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., plugin_definition: _Optional[str] = ..., data: _Optional[_Union[Values, _Mapping]] = ..., metadata: _Optional[_Union[Values, _Mapping]] = ..., last_edited: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ..., display_methods: _Optional[_Iterable[_Union[_integrations_pb2.RequestMethod, str]]] = ...) -> None: ...

class PortalLinkTransactionRow(_message.Message):
    __slots__ = ()
    class LinkDataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    views: int
    verify_attempts: int
    verify_successes: int
    payment_attempts: int
    payment_successes: int
    payment_amount: float
    date: _timestamp_pb2.Timestamp
    link_data: _containers.MessageMap[str, Value]
    def __init__(self, views: _Optional[int] = ..., verify_attempts: _Optional[int] = ..., verify_successes: _Optional[int] = ..., payment_attempts: _Optional[int] = ..., payment_successes: _Optional[int] = ..., payment_amount: _Optional[float] = ..., date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., link_data: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class GetPortalLinksByDateRangeReq(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUM_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    region_id: str
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    page_size: int
    page_num: int
    method_id: _integrations_pb2.RequestMethod
    def __init__(self, org_id: _Optional[str] = ..., region_id: _Optional[str] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_num: _Optional[int] = ..., method_id: _Optional[_Union[_integrations_pb2.RequestMethod, str]] = ...) -> None: ...

class GetPortalLinksByDateRangeRes(_message.Message):
    __slots__ = ()
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[PortalLinkTransactionRow]
    def __init__(self, rows: _Optional[_Iterable[_Union[PortalLinkTransactionRow, _Mapping]]] = ...) -> None: ...

class CallEpicPatientReq(_message.Message):
    __slots__ = ()
    PHONEAGENTID_FIELD_NUMBER: _ClassVar[int]
    ORIGINPHONEEXTENSION_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    EPICCALLID_FIELD_NUMBER: _ClassVar[int]
    PhoneAgentID: str
    OriginPhoneExtension: str
    PhoneNumber: str
    EpicCallID: str
    def __init__(self, PhoneAgentID: _Optional[str] = ..., OriginPhoneExtension: _Optional[str] = ..., PhoneNumber: _Optional[str] = ..., EpicCallID: _Optional[str] = ...) -> None: ...

class CallEpicPatientRes(_message.Message):
    __slots__ = ()
    PHONESYSTEMCALLID_FIELD_NUMBER: _ClassVar[int]
    PhoneSystemCallID: str
    def __init__(self, PhoneSystemCallID: _Optional[str] = ...) -> None: ...

class HangUpEpicPatientCallReq(_message.Message):
    __slots__ = ()
    PHONEAGENTID_FIELD_NUMBER: _ClassVar[int]
    ORIGINPHONEEXTENSION_FIELD_NUMBER: _ClassVar[int]
    EPICCALLID_FIELD_NUMBER: _ClassVar[int]
    PhoneAgentID: str
    OriginPhoneExtension: str
    EpicCallID: str
    def __init__(self, PhoneAgentID: _Optional[str] = ..., OriginPhoneExtension: _Optional[str] = ..., EpicCallID: _Optional[str] = ...) -> None: ...

class GenerateEpicKeyPairReq(_message.Message):
    __slots__ = ()
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, org_id: _Optional[str] = ..., servers: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateEpicKeyPairRes(_message.Message):
    __slots__ = ()
    PRODUCTION_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NON_PRODUCTION_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    production_public_key: str
    non_production_public_key: str
    def __init__(self, production_public_key: _Optional[str] = ..., non_production_public_key: _Optional[str] = ...) -> None: ...

class PortalSegment(_message.Message):
    __slots__ = ()
    WORKFLOW_CHOICES_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    FOOTER_TEXT_FIELD_NUMBER: _ClassVar[int]
    workflow_choices: _containers.RepeatedCompositeFieldContainer[PortalWorkflow]
    header_text: str
    footer_text: str
    def __init__(self, workflow_choices: _Optional[_Iterable[_Union[PortalWorkflow, _Mapping]]] = ..., header_text: _Optional[str] = ..., footer_text: _Optional[str] = ...) -> None: ...

class PortalWorkflow(_message.Message):
    __slots__ = ()
    class DemoResultsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    FOOTER_TEXT_FIELD_NUMBER: _ClassVar[int]
    DEMO_MODE_FIELD_NUMBER: _ClassVar[int]
    DEMO_FAIL_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    DEMO_PASS_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    DEMO_RESULTS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    template: Template
    form_fields: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.FieldDefinition]
    header_text: str
    footer_text: str
    demo_mode: bool
    demo_fail_conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    demo_pass_conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    demo_results: _containers.ScalarMap[str, str]
    workflow_definition_name: str
    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., template: _Optional[_Union[Template, _Mapping]] = ..., form_fields: _Optional[_Iterable[_Union[_integrations_pb2.FieldDefinition, _Mapping]]] = ..., header_text: _Optional[str] = ..., footer_text: _Optional[str] = ..., demo_mode: _Optional[bool] = ..., demo_fail_conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., demo_pass_conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., demo_results: _Optional[_Mapping[str, str]] = ..., workflow_definition_name: _Optional[str] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ()
    class RestructureBeforeEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RestructureAfterEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OptsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESTRUCTURE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    RESTRUCTURE_AFTER_FIELD_NUMBER: _ClassVar[int]
    ACTION_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTS_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    restructure_before: _containers.ScalarMap[str, str]
    restructure_after: _containers.ScalarMap[str, str]
    action_definition_name: str
    opts: _containers.ScalarMap[str, str]
    def __init__(self, plugin_instance_id: _Optional[str] = ..., restructure_before: _Optional[_Mapping[str, str]] = ..., restructure_after: _Optional[_Mapping[str, str]] = ..., action_definition_name: _Optional[str] = ..., opts: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Template(_message.Message):
    __slots__ = ()
    INVOICE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    invoice_template: _integrations_pb2.Invoices
    receipt_template: _integrations_pb2.Receipt
    payment_template: _integrations_pb2.Payment
    def __init__(self, invoice_template: _Optional[_Union[_integrations_pb2.Invoices, _Mapping]] = ..., receipt_template: _Optional[_Union[_integrations_pb2.Receipt, _Mapping]] = ..., payment_template: _Optional[_Union[_integrations_pb2.Payment, _Mapping]] = ...) -> None: ...

class PopulateIntegrationLinkReq(_message.Message):
    __slots__ = ()
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_LINK_FIELD_NUMBER: _ClassVar[int]
    client_sid: int
    agent_sid: int
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    scheduled_callback_id: str
    integration_link: _huntgroup_pb2.IntegrationLink
    def __init__(self, client_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., scheduled_callback_id: _Optional[str] = ..., integration_link: _Optional[_Union[_huntgroup_pb2.IntegrationLink, _Mapping]] = ...) -> None: ...

class PopulateIntegrationLinkRes(_message.Message):
    __slots__ = ()
    INTEGRATION_LINK_FIELD_NUMBER: _ClassVar[int]
    integration_link: _huntgroup_pb2.IntegrationLink
    def __init__(self, integration_link: _Optional[_Union[_huntgroup_pb2.IntegrationLink, _Mapping]] = ...) -> None: ...

class ProcessWorkflowReq(_message.Message):
    __slots__ = ()
    class ParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    PORTAL_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    PORTAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    portal_link_id: str
    portal_id: str
    segment: int
    choice: int
    params: _containers.MessageMap[str, Value]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    request_origin: _integrations_pb2.RequestOrigin
    def __init__(self, portal_link_id: _Optional[str] = ..., portal_id: _Optional[str] = ..., segment: _Optional[int] = ..., choice: _Optional[int] = ..., params: _Optional[_Mapping[str, Value]] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ...) -> None: ...

class ProcessWorkflowRes(_message.Message):
    __slots__ = ()
    class DataEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: _containers.MessageMap[str, Value]
    def __init__(self, success: _Optional[bool] = ..., data: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class InsertPrivateFieldReq(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    private_field_type: PrivateFieldType
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., private_field_type: _Optional[_Union[PrivateFieldType, str]] = ...) -> None: ...

class InsertPrivateFieldRes(_message.Message):
    __slots__ = ()
    PRIVATE_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    private_field_id: int
    def __init__(self, private_field_id: _Optional[int] = ...) -> None: ...

class CalculateFeesReq(_message.Message):
    __slots__ = ()
    class ParamsEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    FEES_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    fees: _containers.RepeatedCompositeFieldContainer[_integrations_pb2.Fee]
    params: _containers.MessageMap[str, Value]
    call_sid: int
    call_type: _acd_pb2.CallType.Enum
    request_origin: _integrations_pb2.RequestOrigin
    def __init__(self, fees: _Optional[_Iterable[_Union[_integrations_pb2.Fee, _Mapping]]] = ..., params: _Optional[_Mapping[str, Value]] = ..., call_sid: _Optional[int] = ..., call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., request_origin: _Optional[_Union[_integrations_pb2.RequestOrigin, str]] = ...) -> None: ...

class CalculateFeesRes(_message.Message):
    __slots__ = ()
    class CalculatedFeesEntry(_message.Message):
        __slots__ = ()
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _money_pb2.Money
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...
    CALCULATED_FEES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_DUE_FIELD_NUMBER: _ClassVar[int]
    calculated_fees: _containers.MessageMap[str, _money_pb2.Money]
    total_amount_due: _money_pb2.Money
    def __init__(self, calculated_fees: _Optional[_Mapping[str, _money_pb2.Money]] = ..., total_amount_due: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...

class IntegrationSettings(_message.Message):
    __slots__ = ()
    ALLOWED_INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
    allowed_integrations: _containers.RepeatedScalarFieldContainer[_integrations_pb2.IntegrationType]
    def __init__(self, allowed_integrations: _Optional[_Iterable[_Union[_integrations_pb2.IntegrationType, str]]] = ...) -> None: ...

class GetIntegrationSettingsReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIntegrationSettingsRes(_message.Message):
    __slots__ = ()
    ALLOWED_INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
    allowed_integrations: _containers.RepeatedScalarFieldContainer[_integrations_pb2.IntegrationType]
    def __init__(self, allowed_integrations: _Optional[_Iterable[_Union[_integrations_pb2.IntegrationType, str]]] = ...) -> None: ...

class UpsertIntegrationSettingsReq(_message.Message):
    __slots__ = ()
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: IntegrationSettings
    def __init__(self, entity: _Optional[_Union[IntegrationSettings, _Mapping]] = ...) -> None: ...

class UpsertIntegrationSettingsRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeliverReceiptReq(_message.Message):
    __slots__ = ()
    EMAIL_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_ID_FIELD_NUMBER: _ClassVar[int]
    email_receipt: EmailReceipt
    receipt_id: str
    def __init__(self, email_receipt: _Optional[_Union[EmailReceipt, _Mapping]] = ..., receipt_id: _Optional[str] = ...) -> None: ...

class EmailReceipt(_message.Message):
    __slots__ = ()
    TO_ADDR_FIELD_NUMBER: _ClassVar[int]
    to_addr: str
    def __init__(self, to_addr: _Optional[str] = ...) -> None: ...

class DeliverReceiptRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
