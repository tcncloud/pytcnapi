import datetime

from api.commons.audit import event_types_pb2 as _event_types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha1 import matching_pb2 as _matching_pb2
from services.billing.entities.v1alpha1 import modules_pb2 as _modules_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateDefinitionConfigType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_NOOP: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_SEATS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_POLL: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_CREATED: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY: _ClassVar[RateDefinitionConfigType]
    RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED: _ClassVar[RateDefinitionConfigType]
RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_NOOP: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_SEATS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_POLL: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_CREATED: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY: RateDefinitionConfigType
RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED: RateDefinitionConfigType

class RateDefinition(_message.Message):
    __slots__ = ()
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_DEFINITION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_RULE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    MATCHING_SHA_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    rate_definition_feature_id: str
    rate_definition_group_id: str
    event_type: _event_types_pb2.EventType
    config_type: RateDefinitionConfigType
    matching_rule: _matching_pb2.MatchingRule
    matching_config: _matching_pb2.MatchingConfig
    config: RateDefinitionConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    matching_sha: str
    def __init__(self, rate_definition_id: _Optional[str] = ..., rate_definition_feature_id: _Optional[str] = ..., rate_definition_group_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., config_type: _Optional[_Union[RateDefinitionConfigType, str]] = ..., matching_rule: _Optional[_Union[_matching_pb2.MatchingRule, str]] = ..., matching_config: _Optional[_Union[_matching_pb2.MatchingConfig, _Mapping]] = ..., config: _Optional[_Union[RateDefinitionConfig, _Mapping]] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., matching_sha: _Optional[str] = ...) -> None: ...

class RateDefinitionConfig(_message.Message):
    __slots__ = ()
    AGENT_SEATS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_POLL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_CREATED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CACHED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    agent_seats_config: _modules_pb2.BasicConfig
    agent_text_message_chat_config: _modules_pb2.BasicConfig
    agent_text_message_email_message_config: _modules_pb2.BasicConfig
    agent_text_message_email_size_config: _modules_pb2.BasicUnitConfig
    agent_text_message_sms_config: _modules_pb2.BasicConfig
    task_message_sent_email_message_config: _modules_pb2.BasicConfig
    task_message_sent_email_size_config: _modules_pb2.BasicUnitConfig
    task_message_sent_sms_config: _modules_pb2.BasicConfig
    connected_inbox_poll_config: _modules_pb2.BasicConfig
    manager_text_message_chat_config: _modules_pb2.BasicConfig
    manager_text_message_email_message_config: _modules_pb2.BasicConfig
    manager_text_message_email_size_config: _modules_pb2.BasicUnitConfig
    manager_text_message_sms_config: _modules_pb2.BasicConfig
    customer_text_message_chat_config: _modules_pb2.BasicConfig
    customer_text_message_email_message_config: _modules_pb2.BasicConfig
    customer_text_message_email_size_config: _modules_pb2.BasicUnitConfig
    customer_text_message_sms_config: _modules_pb2.BasicConfig
    agent_text_message_chat_size_config: _modules_pb2.BasicUnitConfig
    manager_text_message_chat_size_config: _modules_pb2.BasicUnitConfig
    customer_text_message_chat_size_config: _modules_pb2.BasicUnitConfig
    connected_inbox_created_config: _modules_pb2.BasicConfig
    agent_text_message_sms_size_config: _modules_pb2.BasicUnitConfig
    manager_text_message_sms_size_config: _modules_pb2.BasicUnitConfig
    customer_text_message_sms_size_config: _modules_pb2.BasicUnitConfig
    task_message_sent_sms_size_config: _modules_pb2.BasicUnitConfig
    agent_chat_message_units_config: _modules_pb2.BasicConfig
    agent_email_message_units_config: _modules_pb2.BasicConfig
    agent_sms_message_units_config: _modules_pb2.BasicConfig
    manager_chat_message_units_config: _modules_pb2.BasicConfig
    manager_email_message_units_config: _modules_pb2.BasicConfig
    manager_sms_message_units_config: _modules_pb2.BasicConfig
    customer_chat_message_units_config: _modules_pb2.BasicConfig
    customer_email_message_units_config: _modules_pb2.BasicConfig
    customer_sms_message_units_config: _modules_pb2.BasicConfig
    system_chat_message_units_config: _modules_pb2.BasicConfig
    system_email_message_units_config: _modules_pb2.BasicConfig
    system_sms_message_units_config: _modules_pb2.BasicConfig
    compliance_rnd_query_config: _modules_pb2.BasicConfig
    compliance_rnd_query_cached_config: _modules_pb2.BasicConfig
    def __init__(self, agent_seats_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., agent_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., task_message_sent_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., task_message_sent_email_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., task_message_sent_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., connected_inbox_poll_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., connected_inbox_created_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., manager_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., customer_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., task_message_sent_sms_size_config: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., agent_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query_cached_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...
