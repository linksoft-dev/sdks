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

class SerialStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERIAL_STATUS_UNSPECIFIED: _ClassVar[SerialStatus]
    SERIAL_STATUS_AVAILABLE: _ClassVar[SerialStatus]
    SERIAL_STATUS_SOLD: _ClassVar[SerialStatus]
    SERIAL_STATUS_BLOCKED: _ClassVar[SerialStatus]
    SERIAL_STATUS_LOANED: _ClassVar[SerialStatus]
    SERIAL_STATUS_LOST: _ClassVar[SerialStatus]
    SERIAL_STATUS_DAMAGED: _ClassVar[SerialStatus]
SERIAL_STATUS_UNSPECIFIED: SerialStatus
SERIAL_STATUS_AVAILABLE: SerialStatus
SERIAL_STATUS_SOLD: SerialStatus
SERIAL_STATUS_BLOCKED: SerialStatus
SERIAL_STATUS_LOANED: SerialStatus
SERIAL_STATUS_LOST: SerialStatus
SERIAL_STATUS_DAMAGED: SerialStatus

class Serial(_message.Message):
    __slots__ = ("id", "account_id", "serial_number", "product_id", "product_name", "stock_id", "stock_name", "status", "block_reason", "supplier_id", "supplier_name", "entry_date", "exit_date", "notes", "origem", "origem_id", "origem_numero", "pessoa_id", "pessoa_nome", "components", "basic_fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_FIELD_NUMBER: _ClassVar[int]
    EXIT_DATE_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_NUMERO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    account_id: str
    serial_number: str
    product_id: str
    product_name: str
    stock_id: str
    stock_name: str
    status: SerialStatus
    block_reason: str
    supplier_id: str
    supplier_name: str
    entry_date: _timestamp_pb2.Timestamp
    exit_date: _timestamp_pb2.Timestamp
    notes: str
    origem: str
    origem_id: str
    origem_numero: str
    pessoa_id: str
    pessoa_nome: str
    components: _containers.RepeatedCompositeFieldContainer[SerialComponent]
    basic_fields: _metadata_pb2.BasicFields
    def __init__(self, id: _Optional[str] = ..., account_id: _Optional[str] = ..., serial_number: _Optional[str] = ..., product_id: _Optional[str] = ..., product_name: _Optional[str] = ..., stock_id: _Optional[str] = ..., stock_name: _Optional[str] = ..., status: _Optional[_Union[SerialStatus, str]] = ..., block_reason: _Optional[str] = ..., supplier_id: _Optional[str] = ..., supplier_name: _Optional[str] = ..., entry_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., exit_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., notes: _Optional[str] = ..., origem: _Optional[str] = ..., origem_id: _Optional[str] = ..., origem_numero: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., components: _Optional[_Iterable[_Union[SerialComponent, _Mapping]]] = ..., basic_fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class SerialComponent(_message.Message):
    __slots__ = ("description", "serial_number")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    description: str
    serial_number: str
    def __init__(self, description: _Optional[str] = ..., serial_number: _Optional[str] = ...) -> None: ...

class CreateSerialRequest(_message.Message):
    __slots__ = ("serial",)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: Serial
    def __init__(self, serial: _Optional[_Union[Serial, _Mapping]] = ...) -> None: ...

class CreateSerialResponse(_message.Message):
    __slots__ = ("serial",)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: Serial
    def __init__(self, serial: _Optional[_Union[Serial, _Mapping]] = ...) -> None: ...

class UpdateSerialRequest(_message.Message):
    __slots__ = ("id", "serial", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    serial: Serial
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., serial: _Optional[_Union[Serial, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSerialResponse(_message.Message):
    __slots__ = ("serial",)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: Serial
    def __init__(self, serial: _Optional[_Union[Serial, _Mapping]] = ...) -> None: ...

class DeleteSerialRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteSerialResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSerialRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSerialResponse(_message.Message):
    __slots__ = ("serial",)
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial: Serial
    def __init__(self, serial: _Optional[_Union[Serial, _Mapping]] = ...) -> None: ...

class ListSerialRequest(_message.Message):
    __slots__ = ("ids", "product_ids", "stock_ids", "statuses", "serial_number", "supplier_ids", "entry_date_gte", "entry_date_lte", "created_at_gte", "created_at_lte", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
    STOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_IDS_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    product_ids: _containers.RepeatedScalarFieldContainer[str]
    stock_ids: _containers.RepeatedScalarFieldContainer[str]
    statuses: _containers.RepeatedScalarFieldContainer[SerialStatus]
    serial_number: str
    supplier_ids: _containers.RepeatedScalarFieldContainer[str]
    entry_date_gte: _timestamp_pb2.Timestamp
    entry_date_lte: _timestamp_pb2.Timestamp
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., product_ids: _Optional[_Iterable[str]] = ..., stock_ids: _Optional[_Iterable[str]] = ..., statuses: _Optional[_Iterable[_Union[SerialStatus, str]]] = ..., serial_number: _Optional[str] = ..., supplier_ids: _Optional[_Iterable[str]] = ..., entry_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entry_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListSerialResponse(_message.Message):
    __slots__ = ("serial_list", "next_page_token")
    SERIAL_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    serial_list: _containers.RepeatedCompositeFieldContainer[Serial]
    next_page_token: str
    def __init__(self, serial_list: _Optional[_Iterable[_Union[Serial, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "list_serial_request")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_SERIAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    list_serial_request: ListSerialRequest
    def __init__(self, tipo_relatorio: _Optional[str] = ..., list_serial_request: _Optional[_Union[ListSerialRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
