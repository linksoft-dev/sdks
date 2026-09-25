import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inutilizacao(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "situacao", "protocolo", "numeroInicial", "numeroFinal", "serie", "ano", "justificativa", "tipo", "ambiente", "xmlAutorizacao", "dataHoraAutorizacao", "rejeicoes")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    NUMEROINICIAL_FIELD_NUMBER: _ClassVar[int]
    NUMEROFINAL_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    ANO_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATIVA_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    XMLAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    situacao: str
    protocolo: str
    numeroInicial: int
    numeroFinal: int
    serie: int
    ano: int
    justificativa: str
    tipo: str
    ambiente: str
    xmlAutorizacao: str
    dataHoraAutorizacao: _timestamp_pb2.Timestamp
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Rejeicao]
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., situacao: _Optional[str] = ..., protocolo: _Optional[str] = ..., numeroInicial: _Optional[int] = ..., numeroFinal: _Optional[int] = ..., serie: _Optional[int] = ..., ano: _Optional[int] = ..., justificativa: _Optional[str] = ..., tipo: _Optional[str] = ..., ambiente: _Optional[str] = ..., xmlAutorizacao: _Optional[str] = ..., dataHoraAutorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rejeicoes: _Optional[_Iterable[_Union[Rejeicao, _Mapping]]] = ...) -> None: ...

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

class CreateInutilizacaoRequest(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...

class CreateInutilizacaoResponse(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...

class UpdateInutilizacaoRequest(_message.Message):
    __slots__ = ("id", "inutilizacao", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    inutilizacao: Inutilizacao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateInutilizacaoResponse(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...

class DeleteInutilizacaoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteInutilizacaoResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetInutilizacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetInutilizacaoResponse(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...

class ListInutilizacaoRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter", "created_at_gte", "created_at_lte", "numero_inicial", "numero_final", "tipo", "situacao")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    NUMERO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FINAL_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    numero_inicial: int
    numero_final: int
    tipo: _containers.RepeatedScalarFieldContainer[str]
    situacao: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., numero_inicial: _Optional[int] = ..., numero_final: _Optional[int] = ..., tipo: _Optional[_Iterable[str]] = ..., situacao: _Optional[_Iterable[str]] = ...) -> None: ...

class ListInutilizacaoResponse(_message.Message):
    __slots__ = ("inutilizacaoList", "next_page_token")
    INUTILIZACAOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    inutilizacaoList: _containers.RepeatedCompositeFieldContainer[Inutilizacao]
    next_page_token: str
    def __init__(self, inutilizacaoList: _Optional[_Iterable[_Union[Inutilizacao, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class EnviaInutilizacaoRequest(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...

class EnviaInutilizacaoResponse(_message.Message):
    __slots__ = ("inutilizacao",)
    INUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    inutilizacao: Inutilizacao
    def __init__(self, inutilizacao: _Optional[_Union[Inutilizacao, _Mapping]] = ...) -> None: ...
