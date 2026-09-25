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

class CentroCusto(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "nome", "fields")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    nome: str
    fields: _metadata_pb2.BasicFields
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., nome: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CreateCentroCustoRequest(_message.Message):
    __slots__ = ("centroCusto",)
    CENTROCUSTO_FIELD_NUMBER: _ClassVar[int]
    centroCusto: CentroCusto
    def __init__(self, centroCusto: _Optional[_Union[CentroCusto, _Mapping]] = ...) -> None: ...

class CreateCentroCustoResponse(_message.Message):
    __slots__ = ("centroCusto",)
    CENTROCUSTO_FIELD_NUMBER: _ClassVar[int]
    centroCusto: CentroCusto
    def __init__(self, centroCusto: _Optional[_Union[CentroCusto, _Mapping]] = ...) -> None: ...

class UpdateCentroCustoRequest(_message.Message):
    __slots__ = ("id", "centroCusto", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CENTROCUSTO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    centroCusto: CentroCusto
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., centroCusto: _Optional[_Union[CentroCusto, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCentroCustoResponse(_message.Message):
    __slots__ = ("centroCusto",)
    CENTROCUSTO_FIELD_NUMBER: _ClassVar[int]
    centroCusto: CentroCusto
    def __init__(self, centroCusto: _Optional[_Union[CentroCusto, _Mapping]] = ...) -> None: ...

class DeleteCentroCustoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCentroCustoResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCentroCustoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCentroCustoResponse(_message.Message):
    __slots__ = ("centroCusto",)
    CENTROCUSTO_FIELD_NUMBER: _ClassVar[int]
    centroCusto: CentroCusto
    def __init__(self, centroCusto: _Optional[_Union[CentroCusto, _Mapping]] = ...) -> None: ...

class ListCentroCustoRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListCentroCustoResponse(_message.Message):
    __slots__ = ("centroCustoList", "next_page_token")
    CENTROCUSTOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    centroCustoList: _containers.RepeatedCompositeFieldContainer[CentroCusto]
    next_page_token: str
    def __init__(self, centroCustoList: _Optional[_Iterable[_Union[CentroCusto, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportListaSimplesResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("request", "reportName", "sendByEmail")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPORTNAME_FIELD_NUMBER: _ClassVar[int]
    SENDBYEMAIL_FIELD_NUMBER: _ClassVar[int]
    request: ListCentroCustoRequest
    reportName: str
    sendByEmail: str
    def __init__(self, request: _Optional[_Union[ListCentroCustoRequest, _Mapping]] = ..., reportName: _Optional[str] = ..., sendByEmail: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
