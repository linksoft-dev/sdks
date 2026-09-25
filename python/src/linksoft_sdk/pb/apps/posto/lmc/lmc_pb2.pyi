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

class LmcTanque(_message.Message):
    __slots__ = ("numero", "abertura", "conciliacao")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    ABERTURA_FIELD_NUMBER: _ClassVar[int]
    CONCILIACAO_FIELD_NUMBER: _ClassVar[int]
    numero: int
    abertura: float
    conciliacao: float
    def __init__(self, numero: _Optional[int] = ..., abertura: _Optional[float] = ..., conciliacao: _Optional[float] = ...) -> None: ...

class LmcEntrada(_message.Message):
    __slots__ = ("numero_nf", "data_nf", "numero_tanque", "volume_recebido", "nfe_id")
    NUMERO_NF_FIELD_NUMBER: _ClassVar[int]
    DATA_NF_FIELD_NUMBER: _ClassVar[int]
    NUMERO_TANQUE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_RECEBIDO_FIELD_NUMBER: _ClassVar[int]
    NFE_ID_FIELD_NUMBER: _ClassVar[int]
    numero_nf: str
    data_nf: str
    numero_tanque: int
    volume_recebido: float
    nfe_id: str
    def __init__(self, numero_nf: _Optional[str] = ..., data_nf: _Optional[str] = ..., numero_tanque: _Optional[int] = ..., volume_recebido: _Optional[float] = ..., nfe_id: _Optional[str] = ...) -> None: ...

class LmcVenda(_message.Message):
    __slots__ = ("numero_bico", "numero_tanque", "abertura", "fechamento", "afericao", "virada_encerrante", "vendas_no_bico")
    NUMERO_BICO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_TANQUE_FIELD_NUMBER: _ClassVar[int]
    ABERTURA_FIELD_NUMBER: _ClassVar[int]
    FECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    AFERICAO_FIELD_NUMBER: _ClassVar[int]
    VIRADA_ENCERRANTE_FIELD_NUMBER: _ClassVar[int]
    VENDAS_NO_BICO_FIELD_NUMBER: _ClassVar[int]
    numero_bico: int
    numero_tanque: int
    abertura: float
    fechamento: float
    afericao: float
    virada_encerrante: float
    vendas_no_bico: float
    def __init__(self, numero_bico: _Optional[int] = ..., numero_tanque: _Optional[int] = ..., abertura: _Optional[float] = ..., fechamento: _Optional[float] = ..., afericao: _Optional[float] = ..., virada_encerrante: _Optional[float] = ..., vendas_no_bico: _Optional[float] = ...) -> None: ...

class Lmc(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "numero", "data", "produto_id", "produto_nome", "codigo_anp", "preco_avista", "preco_aprazo", "tanques", "entradas", "vendas", "obs", "estoque_abertura", "total_recebido", "volume_disponivel", "vendas_dia_qtde", "valor_vendas_dia", "estoque_escritural", "estoque_fechamento", "perdas_sobras", "valor_acumulado")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_ANP_FIELD_NUMBER: _ClassVar[int]
    PRECO_AVISTA_FIELD_NUMBER: _ClassVar[int]
    PRECO_APRAZO_FIELD_NUMBER: _ClassVar[int]
    TANQUES_FIELD_NUMBER: _ClassVar[int]
    ENTRADAS_FIELD_NUMBER: _ClassVar[int]
    VENDAS_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_ABERTURA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECEBIDO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DISPONIVEL_FIELD_NUMBER: _ClassVar[int]
    VENDAS_DIA_QTDE_FIELD_NUMBER: _ClassVar[int]
    VALOR_VENDAS_DIA_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_ESCRITURAL_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_FECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    PERDAS_SOBRAS_FIELD_NUMBER: _ClassVar[int]
    VALOR_ACUMULADO_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    numero: int
    data: _timestamp_pb2.Timestamp
    produto_id: str
    produto_nome: str
    codigo_anp: str
    preco_avista: float
    preco_aprazo: float
    tanques: _containers.RepeatedCompositeFieldContainer[LmcTanque]
    entradas: _containers.RepeatedCompositeFieldContainer[LmcEntrada]
    vendas: _containers.RepeatedCompositeFieldContainer[LmcVenda]
    obs: str
    estoque_abertura: float
    total_recebido: float
    volume_disponivel: float
    vendas_dia_qtde: float
    valor_vendas_dia: float
    estoque_escritural: float
    estoque_fechamento: float
    perdas_sobras: float
    valor_acumulado: float
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., numero: _Optional[int] = ..., data: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., codigo_anp: _Optional[str] = ..., preco_avista: _Optional[float] = ..., preco_aprazo: _Optional[float] = ..., tanques: _Optional[_Iterable[_Union[LmcTanque, _Mapping]]] = ..., entradas: _Optional[_Iterable[_Union[LmcEntrada, _Mapping]]] = ..., vendas: _Optional[_Iterable[_Union[LmcVenda, _Mapping]]] = ..., obs: _Optional[str] = ..., estoque_abertura: _Optional[float] = ..., total_recebido: _Optional[float] = ..., volume_disponivel: _Optional[float] = ..., vendas_dia_qtde: _Optional[float] = ..., valor_vendas_dia: _Optional[float] = ..., estoque_escritural: _Optional[float] = ..., estoque_fechamento: _Optional[float] = ..., perdas_sobras: _Optional[float] = ..., valor_acumulado: _Optional[float] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("lmc",)
    LMC_FIELD_NUMBER: _ClassVar[int]
    lmc: Lmc
    def __init__(self, lmc: _Optional[_Union[Lmc, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("lmc",)
    LMC_FIELD_NUMBER: _ClassVar[int]
    lmc: Lmc
    def __init__(self, lmc: _Optional[_Union[Lmc, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "lmc", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    LMC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    lmc: Lmc
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., lmc: _Optional[_Union[Lmc, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("lmc",)
    LMC_FIELD_NUMBER: _ClassVar[int]
    lmc: Lmc
    def __init__(self, lmc: _Optional[_Union[Lmc, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("lmc",)
    LMC_FIELD_NUMBER: _ClassVar[int]
    lmc: Lmc
    def __init__(self, lmc: _Optional[_Union[Lmc, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
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

class ListResponse(_message.Message):
    __slots__ = ("lmc_list", "next_page_token")
    LMC_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    lmc_list: _containers.RepeatedCompositeFieldContainer[Lmc]
    next_page_token: str
    def __init__(self, lmc_list: _Optional[_Iterable[_Union[Lmc, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PreencheRequest(_message.Message):
    __slots__ = ("data", "produto_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    data: str
    produto_id: str
    def __init__(self, data: _Optional[str] = ..., produto_id: _Optional[str] = ...) -> None: ...

class PreencheResponse(_message.Message):
    __slots__ = ("lmc", "avisos")
    LMC_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    lmc: Lmc
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lmc: _Optional[_Union[Lmc, _Mapping]] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

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
