from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha3 import modules_pb2 as _modules_pb2
from services.billing.entities.v1alpha3 import omni_pb2 as _omni_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateDefinition(_message.Message):
    __slots__ = ("rate_definition_id", "sku_id", "product", "config", "is_draft", "create_time", "update_time", "delete_time")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SKU_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_DRAFT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    sku_id: str
    product: Product
    config: ProductConfig
    is_draft: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    def __init__(self, rate_definition_id: _Optional[str] = ..., sku_id: _Optional[str] = ..., product: _Optional[_Union[Product, _Mapping]] = ..., config: _Optional[_Union[ProductConfig, _Mapping]] = ..., is_draft: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("category_one", "category_two", "category_three", "product_name")
    CATEGORY_ONE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TWO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_THREE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    category_one: str
    category_two: str
    category_three: str
    product_name: str
    def __init__(self, category_one: _Optional[str] = ..., category_two: _Optional[str] = ..., category_three: _Optional[str] = ..., product_name: _Optional[str] = ...) -> None: ...

class ProductConfig(_message.Message):
    __slots__ = ("communications_omni_chat_agent_message_unit", "communications_omni_chat_agent_attachment", "communications_omni_chat_agent_accumulated_attachments", "communications_omni_chat_customer_message_unit", "communications_omni_chat_customer_attachment", "communications_omni_chat_customer_accumulated_attachments", "communications_omni_chat_manager_message_unit", "communications_omni_chat_manager_attachment", "communications_omni_chat_manager_accumulated_attachments", "communications_omni_chat_system_message_unit", "communications_omni_chat_system_attachment", "communications_omni_chat_system_accumulated_attachments", "communications_omni_email_agent_message_unit", "communications_omni_email_agent_size", "communications_omni_email_agent_accumulated_size", "communications_omni_email_customer_message_unit", "communications_omni_email_customer_size", "communications_omni_email_customer_accumulated_size", "communications_omni_email_manager_message_unit", "communications_omni_email_manager_size", "communications_omni_email_manager_accumulated_size", "communications_omni_email_system_message_unit", "communications_omni_email_system_size", "communications_omni_email_system_accumulated_size", "communications_omni_sms_agent_message_unit", "communications_omni_sms_agent_attatchment", "communications_omni_sms_agent_accumulated_attatchments", "communications_omni_sms_customer_message_unit", "communications_omni_sms_customer_attatchment", "communications_omni_sms_customer_accumulated_attatchments", "communications_omni_sms_manager_message_unit", "communications_omni_sms_manager_attatchment", "communications_omni_sms_manager_accumulated_attatchments", "communications_omni_sms_system_message_unit", "communications_omni_sms_system_attatchment", "communications_omni_sms_system_accumulated_attatchments", "communications_omni_agent_seats", "communications_omni_resources_connected_inbox_poll", "communications_omni_resources_connected_inbox_created", "data_management_compliance_compliance_rnd_query", "data_management_compliance_compliance_rnd_query_cached")
    COMMUNICATIONS_OMNI_CHAT_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_AGENT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_AGENT_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_ATTATCHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_ACCUMULATED_ATTATCHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_ATTATCHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_ACCUMULATED_ATTATCHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_ATTATCHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_ACCUMULATED_ATTATCHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_ATTATCHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_ACCUMULATED_ATTATCHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_AGENT_SEATS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_RESOURCES_CONNECTED_INBOX_POLL_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_RESOURCES_CONNECTED_INBOX_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE_RND_QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE_RND_QUERY_CACHED_FIELD_NUMBER: _ClassVar[int]
    communications_omni_chat_agent_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_agent_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_agent_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_customer_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_customer_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_customer_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_manager_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_manager_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_manager_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_system_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_system_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_system_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_email_agent_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_agent_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_agent_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_customer_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_customer_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_customer_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_manager_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_manager_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_manager_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_system_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_system_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_system_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_sms_agent_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_agent_attatchment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_agent_accumulated_attatchments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_customer_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_customer_attatchment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_customer_accumulated_attatchments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_manager_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_manager_attatchment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_manager_accumulated_attatchments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_system_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_system_attatchment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_system_accumulated_attatchments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_agent_seats: _modules_pb2.BasicConfig
    communications_omni_resources_connected_inbox_poll: _modules_pb2.BasicConfig
    communications_omni_resources_connected_inbox_created: _modules_pb2.BasicConfig
    data_management_compliance_compliance_rnd_query: _modules_pb2.BasicConfig
    data_management_compliance_compliance_rnd_query_cached: _modules_pb2.BasicConfig
    def __init__(self, communications_omni_chat_agent_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_agent_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_agent_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_customer_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_customer_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_customer_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_manager_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_manager_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_manager_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_system_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_system_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_system_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_agent_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_agent_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_agent_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_customer_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_customer_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_customer_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_manager_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_manager_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_manager_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_system_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_system_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_system_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_sms_agent_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_agent_attatchment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_agent_accumulated_attatchments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_customer_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_customer_attatchment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_customer_accumulated_attatchments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_manager_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_manager_attatchment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_manager_accumulated_attatchments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_system_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_system_attatchment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_system_accumulated_attatchments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_agent_seats: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_resources_connected_inbox_poll: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_resources_connected_inbox_created: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., data_management_compliance_compliance_rnd_query: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., data_management_compliance_compliance_rnd_query_cached: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...
