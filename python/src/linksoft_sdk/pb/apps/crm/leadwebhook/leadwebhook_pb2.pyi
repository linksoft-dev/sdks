import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TYPE_UNSPECIFIED: _ClassVar[ProviderType]
    PROVIDER_TYPE_JIVO: _ClassVar[ProviderType]
    PROVIDER_TYPE_TAWK: _ClassVar[ProviderType]
    PROVIDER_TYPE_TIDIO: _ClassVar[ProviderType]
    PROVIDER_TYPE_CRISP: _ClassVar[ProviderType]
    PROVIDER_TYPE_INTERCOM: _ClassVar[ProviderType]
    PROVIDER_TYPE_CHATWOOT: _ClassVar[ProviderType]
    PROVIDER_TYPE_LIVECHAT: _ClassVar[ProviderType]
    PROVIDER_TYPE_META_LEAD_ADS: _ClassVar[ProviderType]
    PROVIDER_TYPE_FORM: _ClassVar[ProviderType]
PROVIDER_TYPE_UNSPECIFIED: ProviderType
PROVIDER_TYPE_JIVO: ProviderType
PROVIDER_TYPE_TAWK: ProviderType
PROVIDER_TYPE_TIDIO: ProviderType
PROVIDER_TYPE_CRISP: ProviderType
PROVIDER_TYPE_INTERCOM: ProviderType
PROVIDER_TYPE_CHATWOOT: ProviderType
PROVIDER_TYPE_LIVECHAT: ProviderType
PROVIDER_TYPE_META_LEAD_ADS: ProviderType
PROVIDER_TYPE_FORM: ProviderType

class Webhook(_message.Message):
    __slots__ = ("id", "basic_fields", "name", "provider_type", "pipeline_id", "pipeline_name", "stage_id", "stage_name", "tags", "active", "last_received_at", "total_received")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    id: str
    basic_fields: _metadata_pb2.BasicFields
    name: str
    provider_type: ProviderType
    pipeline_id: str
    pipeline_name: str
    stage_id: str
    stage_name: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    active: bool
    last_received_at: _timestamp_pb2.Timestamp
    total_received: int
    def __init__(self, id: _Optional[str] = ..., basic_fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., provider_type: _Optional[_Union[ProviderType, str]] = ..., pipeline_id: _Optional[str] = ..., pipeline_name: _Optional[str] = ..., stage_id: _Optional[str] = ..., stage_name: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., active: _Optional[bool] = ..., last_received_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_received: _Optional[int] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "webhook", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    webhook: Webhook
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., webhook: _Optional[_Union[Webhook, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "name", "provider_type", "pipeline_id", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    provider_type: ProviderType
    pipeline_id: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., provider_type: _Optional[_Union[ProviderType, str]] = ..., pipeline_id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("webhook_list",)
    WEBHOOK_LIST_FIELD_NUMBER: _ClassVar[int]
    webhook_list: _containers.RepeatedCompositeFieldContainer[Webhook]
    def __init__(self, webhook_list: _Optional[_Iterable[_Union[Webhook, _Mapping]]] = ...) -> None: ...
