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

class Recibo(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "tipo", "dataHoraRegistro", "tipoDescricao", "pessoaNome", "pessoaId", "pessoaCpfCnpj", "valor", "recebidoPor", "referente", "fields")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREGISTRO_FIELD_NUMBER: _ClassVar[int]
    TIPODESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PESSOANOME_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    PESSOACPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    RECEBIDOPOR_FIELD_NUMBER: _ClassVar[int]
    REFERENTE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    tipo: str
    dataHoraRegistro: _timestamp_pb2.Timestamp
    tipoDescricao: str
    pessoaNome: str
    pessoaId: str
    pessoaCpfCnpj: str
    valor: float
    recebidoPor: str
    referente: str
    fields: _metadata_pb2.BasicFields
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., tipo: _Optional[str] = ..., dataHoraRegistro: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tipoDescricao: _Optional[str] = ..., pessoaNome: _Optional[str] = ..., pessoaId: _Optional[str] = ..., pessoaCpfCnpj: _Optional[str] = ..., valor: _Optional[float] = ..., recebidoPor: _Optional[str] = ..., referente: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CreateReciboRequest(_message.Message):
    __slots__ = ("recibo",)
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    recibo: Recibo
    def __init__(self, recibo: _Optional[_Union[Recibo, _Mapping]] = ...) -> None: ...

class CreateReciboResponse(_message.Message):
    __slots__ = ("recibo",)
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    recibo: Recibo
    def __init__(self, recibo: _Optional[_Union[Recibo, _Mapping]] = ...) -> None: ...

class UpdateReciboRequest(_message.Message):
    __slots__ = ("id", "recibo", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    recibo: Recibo
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., recibo: _Optional[_Union[Recibo, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateReciboResponse(_message.Message):
    __slots__ = ("recibo",)
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    recibo: Recibo
    def __init__(self, recibo: _Optional[_Union[Recibo, _Mapping]] = ...) -> None: ...

class DeleteReciboRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteReciboResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetReciboRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetReciboResponse(_message.Message):
    __slots__ = ("recibo",)
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    recibo: Recibo
    def __init__(self, recibo: _Optional[_Union[Recibo, _Mapping]] = ...) -> None: ...

class ListReciboRequest(_message.Message):
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

class ListReciboResponse(_message.Message):
    __slots__ = ("reciboList", "next_page_token")
    RECIBOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reciboList: _containers.RepeatedCompositeFieldContainer[Recibo]
    next_page_token: str
    def __init__(self, reciboList: _Optional[_Iterable[_Union[Recibo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ImprimirReciboRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimirReciboResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("fileName", "fileContent", "recibos", "validateOnly")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILECONTENT_FIELD_NUMBER: _ClassVar[int]
    RECIBOS_FIELD_NUMBER: _ClassVar[int]
    VALIDATEONLY_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    fileContent: str
    recibos: _containers.RepeatedCompositeFieldContainer[Recibo]
    validateOnly: bool
    def __init__(self, fileName: _Optional[str] = ..., fileContent: _Optional[str] = ..., recibos: _Optional[_Iterable[_Union[Recibo, _Mapping]]] = ..., validateOnly: _Optional[bool] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ("success", "failed", "total", "htmlReport")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    HTMLREPORT_FIELD_NUMBER: _ClassVar[int]
    success: int
    failed: int
    total: int
    htmlReport: str
    def __init__(self, success: _Optional[int] = ..., failed: _Optional[int] = ..., total: _Optional[int] = ..., htmlReport: _Optional[str] = ...) -> None: ...

class CloneReciboRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneReciboResponse(_message.Message):
    __slots__ = ("recibo",)
    RECIBO_FIELD_NUMBER: _ClassVar[int]
    recibo: Recibo
    def __init__(self, recibo: _Optional[_Union[Recibo, _Mapping]] = ...) -> None: ...
