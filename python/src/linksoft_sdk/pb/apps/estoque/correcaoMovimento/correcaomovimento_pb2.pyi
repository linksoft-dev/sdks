import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[Situacao]
    SITUACAO_PENDENTE: _ClassVar[Situacao]
    SITUACAO_EFETIVADA: _ClassVar[Situacao]
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_PENDENTE: Situacao
SITUACAO_EFETIVADA: Situacao

class CorrecaoMovimento(_message.Message):
    __slots__ = ("fields", "id", "createdAt", "updatedAt", "dataInicial", "usuario_id", "usuario_nome", "usuario_update_id", "usuario_update_nome", "usuario_efetivar_id", "usuario_efetivar_nome", "motivo", "situacao", "estoque_origem_id", "estoque_destino_id", "produto_origem_id", "produto_origem_nome", "produto_origem_quantidade_inicial", "produto_origem_quantidade_final", "produto_destino_id", "produto_destino_nome", "produto_destino_quantidade_inicial", "produto_destino_quantidade_final", "tipo_movimento", "alteracoes", "obs")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    DATAINICIAL_FIELD_NUMBER: _ClassVar[int]
    USUARIO_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    USUARIO_UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_UPDATE_NOME_FIELD_NUMBER: _ClassVar[int]
    USUARIO_EFETIVAR_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_EFETIVAR_NOME_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_QUANTIDADE_INICIAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_QUANTIDADE_FINAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_QUANTIDADE_INICIAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_QUANTIDADE_FINAL_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    ALTERACOES_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    dataInicial: _timestamp_pb2.Timestamp
    usuario_id: str
    usuario_nome: str
    usuario_update_id: str
    usuario_update_nome: str
    usuario_efetivar_id: str
    usuario_efetivar_nome: str
    motivo: str
    situacao: Situacao
    estoque_origem_id: str
    estoque_destino_id: str
    produto_origem_id: str
    produto_origem_nome: str
    produto_origem_quantidade_inicial: float
    produto_origem_quantidade_final: float
    produto_destino_id: str
    produto_destino_nome: str
    produto_destino_quantidade_inicial: float
    produto_destino_quantidade_final: float
    tipo_movimento: _containers.RepeatedCompositeFieldContainer[TipoMovimento]
    alteracoes: _containers.RepeatedCompositeFieldContainer[Alteracoes]
    obs: str
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataInicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., usuario_id: _Optional[str] = ..., usuario_nome: _Optional[str] = ..., usuario_update_id: _Optional[str] = ..., usuario_update_nome: _Optional[str] = ..., usuario_efetivar_id: _Optional[str] = ..., usuario_efetivar_nome: _Optional[str] = ..., motivo: _Optional[str] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., estoque_origem_id: _Optional[str] = ..., estoque_destino_id: _Optional[str] = ..., produto_origem_id: _Optional[str] = ..., produto_origem_nome: _Optional[str] = ..., produto_origem_quantidade_inicial: _Optional[float] = ..., produto_origem_quantidade_final: _Optional[float] = ..., produto_destino_id: _Optional[str] = ..., produto_destino_nome: _Optional[str] = ..., produto_destino_quantidade_inicial: _Optional[float] = ..., produto_destino_quantidade_final: _Optional[float] = ..., tipo_movimento: _Optional[_Iterable[_Union[TipoMovimento, _Mapping]]] = ..., alteracoes: _Optional[_Iterable[_Union[Alteracoes, _Mapping]]] = ..., obs: _Optional[str] = ...) -> None: ...

class TipoMovimento(_message.Message):
    __slots__ = ("nome", "descricao")
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    nome: str
    descricao: str
    def __init__(self, nome: _Optional[str] = ..., descricao: _Optional[str] = ...) -> None: ...

class Alteracoes(_message.Message):
    __slots__ = ("id", "created_at", "quantidade", "referencia", "tipo", "origem", "origem_id", "origem_numero", "obs", "pessoa_id", "pessoa_nome")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_NUMERO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    quantidade: float
    referencia: str
    tipo: str
    origem: str
    origem_id: str
    origem_numero: str
    obs: str
    pessoa_id: str
    pessoa_nome: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quantidade: _Optional[float] = ..., referencia: _Optional[str] = ..., tipo: _Optional[str] = ..., origem: _Optional[str] = ..., origem_id: _Optional[str] = ..., origem_numero: _Optional[str] = ..., obs: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ...) -> None: ...

class CreateCorrecaoMovimentoRequest(_message.Message):
    __slots__ = ("correcaoMovimento",)
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    correcaoMovimento: CorrecaoMovimento
    def __init__(self, correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ...) -> None: ...

class CreateCorrecaoMovimentoResponse(_message.Message):
    __slots__ = ("correcaoMovimento",)
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    correcaoMovimento: CorrecaoMovimento
    def __init__(self, correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ...) -> None: ...

class UpdateCorrecaoMovimentoRequest(_message.Message):
    __slots__ = ("id", "correcaoMovimento", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    correcaoMovimento: CorrecaoMovimento
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCorrecaoMovimentoResponse(_message.Message):
    __slots__ = ("correcaoMovimento",)
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    correcaoMovimento: CorrecaoMovimento
    def __init__(self, correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ...) -> None: ...

class DeleteCorrecaoMovimentoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCorrecaoMovimentoResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCorrecaoMovimentoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCorrecaoMovimentoResponse(_message.Message):
    __slots__ = ("correcaoMovimento",)
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    correcaoMovimento: CorrecaoMovimento
    def __init__(self, correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ...) -> None: ...

class ListCorrecaoMovimentoRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter", "createdAtGte", "createdAtLte", "situacao", "tipoMovimento")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATEDATGTE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATLTE_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    TIPOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    createdAtGte: _timestamp_pb2.Timestamp
    createdAtLte: _timestamp_pb2.Timestamp
    situacao: _containers.RepeatedScalarFieldContainer[Situacao]
    tipoMovimento: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., createdAtGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., createdAtLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[_Iterable[_Union[Situacao, str]]] = ..., tipoMovimento: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCorrecaoMovimentoResponse(_message.Message):
    __slots__ = ("correcaoMovimentoList", "next_page_token")
    CORRECAOMOVIMENTOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    correcaoMovimentoList: _containers.RepeatedCompositeFieldContainer[CorrecaoMovimento]
    next_page_token: str
    def __init__(self, correcaoMovimentoList: _Optional[_Iterable[_Union[CorrecaoMovimento, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipoRelatorio", "listCorrecaoMovimentoRequest")
    TIPORELATORIO_FIELD_NUMBER: _ClassVar[int]
    LISTCORRECAOMOVIMENTOREQUEST_FIELD_NUMBER: _ClassVar[int]
    tipoRelatorio: str
    listCorrecaoMovimentoRequest: ListCorrecaoMovimentoRequest
    def __init__(self, tipoRelatorio: _Optional[str] = ..., listCorrecaoMovimentoRequest: _Optional[_Union[ListCorrecaoMovimentoRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class EfetivarRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EfetivarResponse(_message.Message):
    __slots__ = ("status", "message", "correcaoMovimento")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CORRECAOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    correcaoMovimento: CorrecaoMovimento
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ..., correcaoMovimento: _Optional[_Union[CorrecaoMovimento, _Mapping]] = ...) -> None: ...
