import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cce(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "chave", "correcao", "ambiente", "situacao", "protocolo", "sequencia", "xmlAutorizacao", "dataHoraAutorizacao", "rejeicoes")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    CORRECAO_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    SEQUENCIA_FIELD_NUMBER: _ClassVar[int]
    XMLAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    chave: str
    correcao: str
    ambiente: str
    situacao: str
    protocolo: str
    sequencia: int
    xmlAutorizacao: str
    dataHoraAutorizacao: _timestamp_pb2.Timestamp
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Rejeicao]
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., chave: _Optional[str] = ..., correcao: _Optional[str] = ..., ambiente: _Optional[str] = ..., situacao: _Optional[str] = ..., protocolo: _Optional[str] = ..., sequencia: _Optional[int] = ..., xmlAutorizacao: _Optional[str] = ..., dataHoraAutorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rejeicoes: _Optional[_Iterable[_Union[Rejeicao, _Mapping]]] = ...) -> None: ...

class Rejeicao(_message.Message):
    __slots__ = ("id", "dataHora", "dataHoraSituacaoDoc", "cstat", "mensagem")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATAHORA_FIELD_NUMBER: _ClassVar[int]
    DATAHORASITUACAODOC_FIELD_NUMBER: _ClassVar[int]
    CSTAT_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataHora: _timestamp_pb2.Timestamp
    dataHoraSituacaoDoc: _timestamp_pb2.Timestamp
    cstat: str
    mensagem: str
    def __init__(self, id: _Optional[str] = ..., dataHora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraSituacaoDoc: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cstat: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class CreateCceRequest(_message.Message):
    __slots__ = ("cce",)
    CCE_FIELD_NUMBER: _ClassVar[int]
    cce: Cce
    def __init__(self, cce: _Optional[_Union[Cce, _Mapping]] = ...) -> None: ...

class CreateCceResponse(_message.Message):
    __slots__ = ("cce",)
    CCE_FIELD_NUMBER: _ClassVar[int]
    cce: Cce
    def __init__(self, cce: _Optional[_Union[Cce, _Mapping]] = ...) -> None: ...

class UpdateCceRequest(_message.Message):
    __slots__ = ("id", "cce", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    cce: Cce
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., cce: _Optional[_Union[Cce, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCceResponse(_message.Message):
    __slots__ = ("cce",)
    CCE_FIELD_NUMBER: _ClassVar[int]
    cce: Cce
    def __init__(self, cce: _Optional[_Union[Cce, _Mapping]] = ...) -> None: ...

class DeleteCceRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCceResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCceResponse(_message.Message):
    __slots__ = ("cce",)
    CCE_FIELD_NUMBER: _ClassVar[int]
    cce: Cce
    def __init__(self, cce: _Optional[_Union[Cce, _Mapping]] = ...) -> None: ...

class ListCceRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter", "createdAtGte", "createdAtLte", "situacao")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATEDATGTE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATLTE_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    createdAtGte: _timestamp_pb2.Timestamp
    createdAtLte: _timestamp_pb2.Timestamp
    situacao: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., createdAtGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., createdAtLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[str] = ...) -> None: ...

class ListCceResponse(_message.Message):
    __slots__ = ("cceList", "next_page_token")
    CCELIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cceList: _containers.RepeatedCompositeFieldContainer[Cce]
    next_page_token: str
    def __init__(self, cceList: _Optional[_Iterable[_Union[Cce, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class EnviaPdfEmailRequest(_message.Message):
    __slots__ = ("id", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class EnviaPdfEmailResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class ImprimirCceRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimirCceResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
