from google.protobuf import timestamp_pb2 as _timestamp_pb2
from services.billing.entities.v1alpha4 import matching_pb2 as _matching_pb2
from services.billing.entities.v1alpha4 import products_pb2 as _products_pb2
from services.billing.entities.v1alpha4 import tags_pb2 as _tags_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateDefinition(_message.Message):
    __slots__ = ("rate_definition_id", "sku_id", "billing_tag", "config", "is_draft", "is_overwrite", "create_time", "update_time", "delete_time", "billing_tag_id")
    RATE_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    SKU_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_TAG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_DRAFT_FIELD_NUMBER: _ClassVar[int]
    IS_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    BILLING_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    rate_definition_id: str
    sku_id: str
    billing_tag: _tags_pb2.BillingTag
    config: _products_pb2.ProductConfig
    is_draft: bool
    is_overwrite: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    billing_tag_id: str
    def __init__(self, rate_definition_id: _Optional[str] = ..., sku_id: _Optional[str] = ..., billing_tag: _Optional[_Union[_tags_pb2.BillingTag, _Mapping]] = ..., config: _Optional[_Union[_products_pb2.ProductConfig, _Mapping]] = ..., is_draft: bool = ..., is_overwrite: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., billing_tag_id: _Optional[str] = ...) -> None: ...

class MatchingRule(_message.Message):
    __slots__ = ("matching_rule_id", "config", "create_time", "delete_time", "update_time", "rule_config", "country_code_prefix")
    MATCHING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RULE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    matching_rule_id: str
    config: _products_pb2.ProductConfig
    create_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    rule_config: _matching_pb2.MatchingConfig
    country_code_prefix: _matching_pb2.CountryCodePrefix
    def __init__(self, matching_rule_id: _Optional[str] = ..., config: _Optional[_Union[_products_pb2.ProductConfig, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rule_config: _Optional[_Union[_matching_pb2.MatchingConfig, _Mapping]] = ..., country_code_prefix: _Optional[_Union[_matching_pb2.CountryCodePrefix, _Mapping]] = ...) -> None: ...
