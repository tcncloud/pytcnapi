from api.commons.audit import event_types_pb2 as _event_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha2 import matching_pb2 as _matching_pb2
from services.billing.entities.v1alpha2 import modules_pb2 as _modules_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateDefinitionConfigType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_NOOP: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_SEATS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_POLL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_CREATED: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED: _ClassVar[RateDefinitionConfigType]
RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_NOOP: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_SEATS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_POLL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_CREATED: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED: RateDefinitionConfigType

class RateSnapshot(_message.Message):
    __slots__ = ("start_date", "end_date", "rates")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    rates: _containers.RepeatedCompositeFieldContainer[RateDefinition]
    def __init__(self, start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rates: _Optional[_Iterable[_Union[RateDefinition, _Mapping]]] = ...) -> None: ...

class RateDefinition(_message.Message):
    __slots__ = ("rate_definition_id", "event_type", "config_type", "matching_rule", "matching_config", "matching_sha", "create_time", "update_time", "delete_time", "effective_time", "config", "group_id", "config_sha", "thread_id")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MATCHING_SHA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SHA_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    event_type: _event_types_pb2.EventType
    config_type: RateDefinitionConfigType
    matching_rule: _matching_pb2.MatchingRule
    matching_config: _matching_pb2.MatchingConfig
    matching_sha: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    effective_time: _timestamp_pb2.Timestamp
    config: RateDefinitionConfig
    group_id: str
    config_sha: str
    thread_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., config_type: _Optional[_Union[RateDefinitionConfigType, str]] = ..., matching_rule: _Optional[_Union[_matching_pb2.MatchingRule, str]] = ..., matching_config: _Optional[_Union[_matching_pb2.MatchingConfig, _Mapping]] = ..., matching_sha: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., config: _Optional[_Union[RateDefinitionConfig, _Mapping]] = ..., group_id: _Optional[str] = ..., config_sha: _Optional[str] = ..., thread_id: _Optional[str] = ...) -> None: ...

class RateDefinitionConfig(_message.Message):
    __slots__ = ("agent_seats", "connected_inbox_poll", "connected_inbox_created", "agent_message_chat", "agent_message_chat_size", "agent_message_chat_units", "agent_message_email", "agent_message_email_size", "agent_message_email_units", "agent_message_sms", "agent_message_sms_size", "agent_message_sms_units", "manager_message_chat", "manager_message_chat_size", "manager_message_chat_units", "manager_message_email", "manager_message_email_size", "manager_message_email_units", "manager_message_sms", "manager_message_sms_size", "manager_message_sms_units", "system_message_chat", "system_message_chat_size", "system_message_chat_units", "system_message_email", "system_message_email_size", "system_message_email_units", "system_message_sms", "system_message_sms_size", "system_message_sms_units", "customer_message_chat", "customer_message_chat_size", "customer_message_chat_units", "customer_message_email", "customer_message_email_size", "customer_message_email_units", "customer_message_sms", "customer_message_sms_size", "customer_message_sms_units", "compliance_rnd_query", "compliance_rnd_query_cached")
    AGENT_SEATS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_POLL_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_CREATED_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_CHAT_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_CHAT_SIZE_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_CHAT_UNITS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_EMAIL_SIZE_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_EMAIL_UNITS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_SMS_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_SMS_SIZE_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_SMS_UNITS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_CHAT_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_CHAT_SIZE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_CHAT_UNITS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_EMAIL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_EMAIL_UNITS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_SMS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_SMS_SIZE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_MESSAGE_SMS_UNITS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_CHAT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_CHAT_SIZE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_CHAT_UNITS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_EMAIL_SIZE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_EMAIL_UNITS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_SMS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_SMS_SIZE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_SMS_UNITS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_CHAT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_CHAT_SIZE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_CHAT_UNITS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_EMAIL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_EMAIL_UNITS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_SMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_SMS_SIZE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_MESSAGE_SMS_UNITS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CACHED_FIELD_NUMBER: _ClassVar[int]
    agent_seats: _modules_pb2.BasicConfig
    connected_inbox_poll: _modules_pb2.BasicConfig
    connected_inbox_created: _modules_pb2.BasicConfig
    agent_message_chat: _modules_pb2.BasicConfig
    agent_message_chat_size: _modules_pb2.BasicUnitConfig
    agent_message_chat_units: _modules_pb2.BasicConfig
    agent_message_email: _modules_pb2.BasicConfig
    agent_message_email_size: _modules_pb2.BasicUnitConfig
    agent_message_email_units: _modules_pb2.BasicConfig
    agent_message_sms: _modules_pb2.BasicConfig
    agent_message_sms_size: _modules_pb2.BasicUnitConfig
    agent_message_sms_units: _modules_pb2.BasicConfig
    manager_message_chat: _modules_pb2.BasicConfig
    manager_message_chat_size: _modules_pb2.BasicUnitConfig
    manager_message_chat_units: _modules_pb2.BasicConfig
    manager_message_email: _modules_pb2.BasicConfig
    manager_message_email_size: _modules_pb2.BasicUnitConfig
    manager_message_email_units: _modules_pb2.BasicConfig
    manager_message_sms: _modules_pb2.BasicConfig
    manager_message_sms_size: _modules_pb2.BasicUnitConfig
    manager_message_sms_units: _modules_pb2.BasicConfig
    system_message_chat: _modules_pb2.BasicConfig
    system_message_chat_size: _modules_pb2.BasicUnitConfig
    system_message_chat_units: _modules_pb2.BasicConfig
    system_message_email: _modules_pb2.BasicConfig
    system_message_email_size: _modules_pb2.BasicUnitConfig
    system_message_email_units: _modules_pb2.BasicConfig
    system_message_sms: _modules_pb2.BasicConfig
    system_message_sms_size: _modules_pb2.BasicUnitConfig
    system_message_sms_units: _modules_pb2.BasicConfig
    customer_message_chat: _modules_pb2.BasicConfig
    customer_message_chat_size: _modules_pb2.BasicUnitConfig
    customer_message_chat_units: _modules_pb2.BasicConfig
    customer_message_email: _modules_pb2.BasicConfig
    customer_message_email_size: _modules_pb2.BasicUnitConfig
    customer_message_email_units: _modules_pb2.BasicConfig
    customer_message_sms: _modules_pb2.BasicConfig
    customer_message_sms_size: _modules_pb2.BasicUnitConfig
    customer_message_sms_units: _modules_pb2.BasicConfig
    compliance_rnd_query: _modules_pb2.BasicConfig
    compliance_rnd_query_cached: _modules_pb2.BasicConfig
    def __init__(self, agent_seats: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., connected_inbox_poll: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., connected_inbox_created: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_chat: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_chat_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., agent_message_chat_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_email: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_email_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., agent_message_email_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_sms: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_message_sms_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., agent_message_sms_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_chat: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_chat_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_message_chat_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_email: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_email_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_message_email_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_sms: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_message_sms_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_message_sms_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_chat: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_chat_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., system_message_chat_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_email: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_email_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., system_message_email_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_sms: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_message_sms_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., system_message_sms_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_chat: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_chat_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_message_chat_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_email: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_email_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_message_email_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_sms: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_message_sms_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_message_sms_units: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query_cached: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...
