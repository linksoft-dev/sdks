import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Segment(_message.Message):
    __slots__ = ("id", "name", "description", "filters", "tags", "created_at", "updated_at", "contact_count", "contact_ids", "custom_attributes", "contacts", "field_definitions", "criteria", "kind")
    class CustomAttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_IDS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    FIELD_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    filters: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    contact_count: int
    contact_ids: _containers.RepeatedScalarFieldContainer[str]
    custom_attributes: _containers.ScalarMap[str, str]
    contacts: _containers.RepeatedCompositeFieldContainer[SegmentContact]
    field_definitions: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    criteria: _containers.RepeatedCompositeFieldContainer[SegmentCriteria]
    kind: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., filters: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contact_count: _Optional[int] = ..., contact_ids: _Optional[_Iterable[str]] = ..., custom_attributes: _Optional[_Mapping[str, str]] = ..., contacts: _Optional[_Iterable[_Union[SegmentContact, _Mapping]]] = ..., field_definitions: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ..., criteria: _Optional[_Iterable[_Union[SegmentCriteria, _Mapping]]] = ..., kind: _Optional[str] = ...) -> None: ...

class SegmentCriteria(_message.Message):
    __slots__ = ("field", "operator", "value", "module")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    field: str
    operator: str
    value: str
    module: str
    def __init__(self, field: _Optional[str] = ..., operator: _Optional[str] = ..., value: _Optional[str] = ..., module: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("segment",)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("segment",)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "segment", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    segment: Segment
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., segment: _Optional[_Union[Segment, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("segment",)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("segment",)
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: Segment
    def __init__(self, segment: _Optional[_Union[Segment, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "tag", "filter", "kind")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    tag: str
    filter: _filter_pb2.Filter
    kind: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., tag: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("segment_list",)
    SEGMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    segment_list: _containers.RepeatedCompositeFieldContainer[Segment]
    def __init__(self, segment_list: _Optional[_Iterable[_Union[Segment, _Mapping]]] = ...) -> None: ...

class FieldDefinition(_message.Message):
    __slots__ = ("name", "label", "type", "default_value", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    label: str
    type: str
    default_value: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[str] = ..., default_value: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class SegmentContact(_message.Message):
    __slots__ = ("id", "name", "email", "phone", "attributes", "status", "unsubscribe_token", "subscribed_at", "unsubscribed_at", "unsubscribe_reason")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_AT_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBED_AT_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBE_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    phone: str
    attributes: _containers.ScalarMap[str, str]
    status: str
    unsubscribe_token: str
    subscribed_at: str
    unsubscribed_at: str
    unsubscribe_reason: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., status: _Optional[str] = ..., unsubscribe_token: _Optional[str] = ..., subscribed_at: _Optional[str] = ..., unsubscribed_at: _Optional[str] = ..., unsubscribe_reason: _Optional[str] = ...) -> None: ...

class ResolveContactsRequest(_message.Message):
    __slots__ = ("id", "filter")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    id: str
    filter: _filter_pb2.Filter
    def __init__(self, id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ResolveContactsResponse(_message.Message):
    __slots__ = ("contacts", "total_count")
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[SegmentContact]
    total_count: int
    def __init__(self, contacts: _Optional[_Iterable[_Union[SegmentContact, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class ImportContactsRequest(_message.Message):
    __slots__ = ("id", "contacts", "file_string", "file_name", "validate_only", "update_if_exists")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    FILE_STRING_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    contacts: _containers.RepeatedCompositeFieldContainer[SegmentContact]
    file_string: str
    file_name: str
    validate_only: bool
    update_if_exists: bool
    def __init__(self, id: _Optional[str] = ..., contacts: _Optional[_Iterable[_Union[SegmentContact, _Mapping]]] = ..., file_string: _Optional[str] = ..., file_name: _Optional[str] = ..., validate_only: _Optional[bool] = ..., update_if_exists: _Optional[bool] = ...) -> None: ...

class ImportErrorGroup(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ImportError]
    def __init__(self, errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]] = ...) -> None: ...

class ImportError(_message.Message):
    __slots__ = ("contact", "reason", "details")
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    contact: str
    reason: str
    details: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contact: _Optional[str] = ..., reason: _Optional[str] = ..., details: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportContactsResponse(_message.Message):
    __slots__ = ("contacts", "result", "success", "failed", "total", "erros_by_category")
    class ErrosByCategoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ImportErrorGroup
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ImportErrorGroup, _Mapping]] = ...) -> None: ...
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ERROS_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[SegmentContact]
    result: str
    success: int
    failed: int
    total: int
    erros_by_category: _containers.MessageMap[str, ImportErrorGroup]
    def __init__(self, contacts: _Optional[_Iterable[_Union[SegmentContact, _Mapping]]] = ..., result: _Optional[str] = ..., success: _Optional[int] = ..., failed: _Optional[int] = ..., total: _Optional[int] = ..., erros_by_category: _Optional[_Mapping[str, ImportErrorGroup]] = ...) -> None: ...

class UnsubscribeRequest(_message.Message):
    __slots__ = ("token", "reason", "preview")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    token: str
    reason: str
    preview: bool
    def __init__(self, token: _Optional[str] = ..., reason: _Optional[str] = ..., preview: _Optional[bool] = ...) -> None: ...

class UnsubscribeResponse(_message.Message):
    __slots__ = ("segment_name", "contact_name", "contact_email", "status", "resubscribe_token")
    SEGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESUBSCRIBE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    segment_name: str
    contact_name: str
    contact_email: str
    status: str
    resubscribe_token: str
    def __init__(self, segment_name: _Optional[str] = ..., contact_name: _Optional[str] = ..., contact_email: _Optional[str] = ..., status: _Optional[str] = ..., resubscribe_token: _Optional[str] = ...) -> None: ...

class ResubscribeRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class ResubscribeResponse(_message.Message):
    __slots__ = ("segment_name", "contact_name", "status")
    SEGMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    segment_name: str
    contact_name: str
    status: str
    def __init__(self, segment_name: _Optional[str] = ..., contact_name: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "tipo_relatorio")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    list_request: ListRequest
    tipo_relatorio: str
    def __init__(self, list_request: _Optional[_Union[ListRequest, _Mapping]] = ..., tipo_relatorio: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
