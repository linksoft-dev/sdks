import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATCH_STATUS_UNSPECIFIED: _ClassVar[BatchStatus]
    BATCH_STATUS_ACTIVE: _ClassVar[BatchStatus]
    BATCH_STATUS_EXPIRED: _ClassVar[BatchStatus]
    BATCH_STATUS_BLOCKED: _ClassVar[BatchStatus]
    BATCH_STATUS_DEPLETED: _ClassVar[BatchStatus]
BATCH_STATUS_UNSPECIFIED: BatchStatus
BATCH_STATUS_ACTIVE: BatchStatus
BATCH_STATUS_EXPIRED: BatchStatus
BATCH_STATUS_BLOCKED: BatchStatus
BATCH_STATUS_DEPLETED: BatchStatus

class Batch(_message.Message):
    __slots__ = ("fields", "created_at", "updated_at", "user_id", "user_name", "id", "account_id", "batch_number", "product_id", "product_name", "stock_id", "stock_name", "quantity", "manufacturing_date", "expiration_date", "supplier_id", "supplier_name", "status")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    account_id: str
    batch_number: str
    product_id: str
    product_name: str
    stock_id: str
    stock_name: str
    quantity: int
    manufacturing_date: _timestamp_pb2.Timestamp
    expiration_date: _timestamp_pb2.Timestamp
    supplier_id: str
    supplier_name: str
    status: BatchStatus
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., account_id: _Optional[str] = ..., batch_number: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., stock_id: _Optional[str] = ..., stock_name: _Optional[str] = ..., quantity: _Optional[int] = ..., manufacturing_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., supplier_id: _Optional[str] = ..., supplier_name: _Optional[str] = ..., status: _Optional[_Union[BatchStatus, str]] = ...) -> None: ...

class CreateBatchRequest(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: Batch
    def __init__(self, batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class CreateBatchResponse(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: Batch
    def __init__(self, batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class UpdateBatchRequest(_message.Message):
    __slots__ = ("id", "batch", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    batch: Batch
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., batch: _Optional[_Union[Batch, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBatchResponse(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: Batch
    def __init__(self, batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class DeleteBatchRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteBatchResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetBatchRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetBatchResponse(_message.Message):
    __slots__ = ("batch",)
    BATCH_FIELD_NUMBER: _ClassVar[int]
    batch: Batch
    def __init__(self, batch: _Optional[_Union[Batch, _Mapping]] = ...) -> None: ...

class ListBatchRequest(_message.Message):
    __slots__ = ("ids", "product_ids", "stock_ids", "statuses", "expiration_date_gte", "expiration_date_lte", "quantity_gte", "quantity_lte", "filter", "page_size", "page_token", "created_at_gte", "created_at_lte", "manufacturing_date_gte", "manufacturing_date_lte", "supplier_ids", "batch_number")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
    STOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_GTE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_IDS_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    product_ids: _containers.RepeatedScalarFieldContainer[str]
    stock_ids: _containers.RepeatedScalarFieldContainer[str]
    statuses: _containers.RepeatedScalarFieldContainer[BatchStatus]
    expiration_date_gte: _timestamp_pb2.Timestamp
    expiration_date_lte: _timestamp_pb2.Timestamp
    quantity_gte: int
    quantity_lte: int
    filter: _filter_pb2.Filter
    page_size: int
    page_token: str
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    manufacturing_date_gte: _timestamp_pb2.Timestamp
    manufacturing_date_lte: _timestamp_pb2.Timestamp
    supplier_ids: _containers.RepeatedScalarFieldContainer[str]
    batch_number: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., product_ids: _Optional[_Iterable[str]] = ..., stock_ids: _Optional[_Iterable[str]] = ..., statuses: _Optional[_Iterable[_Union[BatchStatus, str]]] = ..., expiration_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quantity_gte: _Optional[int] = ..., quantity_lte: _Optional[int] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., manufacturing_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., manufacturing_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., supplier_ids: _Optional[_Iterable[str]] = ..., batch_number: _Optional[str] = ...) -> None: ...

class ListBatchResponse(_message.Message):
    __slots__ = ("batch_list", "next_page_token")
    BATCH_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    batch_list: _containers.RepeatedCompositeFieldContainer[Batch]
    next_page_token: str
    def __init__(self, batch_list: _Optional[_Iterable[_Union[Batch, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "list_batch_request")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_BATCH_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    list_batch_request: ListBatchRequest
    def __init__(self, tipo_relatorio: _Optional[str] = ..., list_batch_request: _Optional[_Union[ListBatchRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
