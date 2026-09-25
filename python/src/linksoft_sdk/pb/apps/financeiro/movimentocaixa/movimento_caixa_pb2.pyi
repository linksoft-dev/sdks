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

class MovimentoCaixa(_message.Message):
    __slots__ = ("created_at", "updated_at", "competence", "user_id", "user_name", "id", "code", "descricao", "pessoa_id", "pessoa_nome", "plano_conta_id", "plano_conta_nome", "centro_custo_id", "centro_custo_nome", "forma_pagamento_id", "forma_pagamento_nome", "tipo_pagamento", "caixa_nome", "caixa", "wallet_nome", "wallet_id", "tipo_moeda", "operacao", "valor", "saldo", "obs", "source", "source_id", "doc_number", "reverse_reason", "data_hora_inicial", "data_hora_final")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPETENCE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    WALLET_NOME_FIELD_NUMBER: _ClassVar[int]
    WALLET_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    OPERACAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    SALDO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DOC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVERSE_REASON_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FINAL_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    competence: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    code: int
    descricao: str
    pessoa_id: str
    pessoa_nome: str
    plano_conta_id: str
    plano_conta_nome: str
    centro_custo_id: str
    centro_custo_nome: str
    forma_pagamento_id: str
    forma_pagamento_nome: str
    tipo_pagamento: str
    caixa_nome: str
    caixa: str
    wallet_nome: str
    wallet_id: str
    tipo_moeda: str
    operacao: str
    valor: float
    saldo: float
    obs: str
    source: str
    source_id: str
    doc_number: str
    reverse_reason: str
    data_hora_inicial: _timestamp_pb2.Timestamp
    data_hora_final: _timestamp_pb2.Timestamp
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., competence: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., code: _Optional[int] = ..., descricao: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ..., forma_pagamento_id: _Optional[str] = ..., forma_pagamento_nome: _Optional[str] = ..., tipo_pagamento: _Optional[str] = ..., caixa_nome: _Optional[str] = ..., caixa: _Optional[str] = ..., wallet_nome: _Optional[str] = ..., wallet_id: _Optional[str] = ..., tipo_moeda: _Optional[str] = ..., operacao: _Optional[str] = ..., valor: _Optional[float] = ..., saldo: _Optional[float] = ..., obs: _Optional[str] = ..., source: _Optional[str] = ..., source_id: _Optional[str] = ..., doc_number: _Optional[str] = ..., reverse_reason: _Optional[str] = ..., data_hora_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ResumoMovimentoCaixaRequest(_message.Message):
    __slots__ = ("list",)
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: ListMovimentoCaixaRequest
    def __init__(self, list: _Optional[_Union[ListMovimentoCaixaRequest, _Mapping]] = ...) -> None: ...

class ResumoMovimentoCaixaResponse(_message.Message):
    __slots__ = ("abertura_especie", "entradas_especie", "saidas_especie", "saldo_especie", "total_recebiveis", "recebiveis_por_tipo", "faturamento", "count_vendas", "count_sangria", "count_suprimento", "por_tipo_pagamento", "por_plano_conta")
    ABERTURA_ESPECIE_FIELD_NUMBER: _ClassVar[int]
    ENTRADAS_ESPECIE_FIELD_NUMBER: _ClassVar[int]
    SAIDAS_ESPECIE_FIELD_NUMBER: _ClassVar[int]
    SALDO_ESPECIE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECEBIVEIS_FIELD_NUMBER: _ClassVar[int]
    RECEBIVEIS_POR_TIPO_FIELD_NUMBER: _ClassVar[int]
    FATURAMENTO_FIELD_NUMBER: _ClassVar[int]
    COUNT_VENDAS_FIELD_NUMBER: _ClassVar[int]
    COUNT_SANGRIA_FIELD_NUMBER: _ClassVar[int]
    COUNT_SUPRIMENTO_FIELD_NUMBER: _ClassVar[int]
    POR_TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    POR_PLANO_CONTA_FIELD_NUMBER: _ClassVar[int]
    abertura_especie: float
    entradas_especie: float
    saidas_especie: float
    saldo_especie: float
    total_recebiveis: float
    recebiveis_por_tipo: _containers.RepeatedCompositeFieldContainer[ResumoPorTipo]
    faturamento: float
    count_vendas: int
    count_sangria: int
    count_suprimento: int
    por_tipo_pagamento: _containers.RepeatedCompositeFieldContainer[ResumoGrupo]
    por_plano_conta: _containers.RepeatedCompositeFieldContainer[ResumoGrupo]
    def __init__(self, abertura_especie: _Optional[float] = ..., entradas_especie: _Optional[float] = ..., saidas_especie: _Optional[float] = ..., saldo_especie: _Optional[float] = ..., total_recebiveis: _Optional[float] = ..., recebiveis_por_tipo: _Optional[_Iterable[_Union[ResumoPorTipo, _Mapping]]] = ..., faturamento: _Optional[float] = ..., count_vendas: _Optional[int] = ..., count_sangria: _Optional[int] = ..., count_suprimento: _Optional[int] = ..., por_tipo_pagamento: _Optional[_Iterable[_Union[ResumoGrupo, _Mapping]]] = ..., por_plano_conta: _Optional[_Iterable[_Union[ResumoGrupo, _Mapping]]] = ...) -> None: ...

class ResumoPorTipo(_message.Message):
    __slots__ = ("tipo_pagamento", "total")
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    tipo_pagamento: str
    total: float
    def __init__(self, tipo_pagamento: _Optional[str] = ..., total: _Optional[float] = ...) -> None: ...

class ResumoGrupo(_message.Message):
    __slots__ = ("categoria", "user_id", "user_name", "entrada", "saida")
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_FIELD_NUMBER: _ClassVar[int]
    SAIDA_FIELD_NUMBER: _ClassVar[int]
    categoria: str
    user_id: str
    user_name: str
    entrada: float
    saida: float
    def __init__(self, categoria: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., entrada: _Optional[float] = ..., saida: _Optional[float] = ...) -> None: ...

class CreateMovimentoCaixaRequest(_message.Message):
    __slots__ = ("movimento_caixa",)
    MOVIMENTO_CAIXA_FIELD_NUMBER: _ClassVar[int]
    movimento_caixa: MovimentoCaixa
    def __init__(self, movimento_caixa: _Optional[_Union[MovimentoCaixa, _Mapping]] = ...) -> None: ...

class CreateMovimentoCaixaResponse(_message.Message):
    __slots__ = ("movimento_caixa",)
    MOVIMENTO_CAIXA_FIELD_NUMBER: _ClassVar[int]
    movimento_caixa: MovimentoCaixa
    def __init__(self, movimento_caixa: _Optional[_Union[MovimentoCaixa, _Mapping]] = ...) -> None: ...

class UpdateMovimentoCaixaRequest(_message.Message):
    __slots__ = ("id", "movimento_caixa", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOVIMENTO_CAIXA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    movimento_caixa: MovimentoCaixa
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., movimento_caixa: _Optional[_Union[MovimentoCaixa, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMovimentoCaixaResponse(_message.Message):
    __slots__ = ("movimento_caixa",)
    MOVIMENTO_CAIXA_FIELD_NUMBER: _ClassVar[int]
    movimento_caixa: MovimentoCaixa
    def __init__(self, movimento_caixa: _Optional[_Union[MovimentoCaixa, _Mapping]] = ...) -> None: ...

class DeleteMovimentoCaixaRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteMovimentoCaixaResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMovimentoCaixaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMovimentoCaixaResponse(_message.Message):
    __slots__ = ("movimento_caixa",)
    MOVIMENTO_CAIXA_FIELD_NUMBER: _ClassVar[int]
    movimento_caixa: MovimentoCaixa
    def __init__(self, movimento_caixa: _Optional[_Union[MovimentoCaixa, _Mapping]] = ...) -> None: ...

class ListMovimentoCaixaRequest(_message.Message):
    __slots__ = ("ids", "usuario_caixa_id", "usuario_caixa_nome", "dia_movimento", "created_at_gte", "created_at_lte", "competence_gte", "competence_lte", "deposito", "created_at", "caixa", "caixa_nome", "operacao", "tipo_pagamento", "plano_conta_id", "plano_conta_nome", "centro_custo_id", "centro_custo_nome", "wallet_nome", "wallet_id", "saldo_not_zero", "filter", "limit", "page_token")
    IDS_FIELD_NUMBER: _ClassVar[int]
    USUARIO_CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    DIA_MOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    COMPETENCE_GTE_FIELD_NUMBER: _ClassVar[int]
    COMPETENCE_LTE_FIELD_NUMBER: _ClassVar[int]
    DEPOSITO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    OPERACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    WALLET_NOME_FIELD_NUMBER: _ClassVar[int]
    WALLET_ID_FIELD_NUMBER: _ClassVar[int]
    SALDO_NOT_ZERO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    usuario_caixa_id: str
    usuario_caixa_nome: str
    dia_movimento: _timestamp_pb2.Timestamp
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    competence_gte: _timestamp_pb2.Timestamp
    competence_lte: _timestamp_pb2.Timestamp
    deposito: str
    created_at: _timestamp_pb2.Timestamp
    caixa: str
    caixa_nome: str
    operacao: str
    tipo_pagamento: str
    plano_conta_id: str
    plano_conta_nome: str
    centro_custo_id: str
    centro_custo_nome: str
    wallet_nome: str
    wallet_id: str
    saldo_not_zero: bool
    filter: _filter_pb2.Filter
    limit: int
    page_token: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., usuario_caixa_id: _Optional[str] = ..., usuario_caixa_nome: _Optional[str] = ..., dia_movimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., competence_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., competence_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deposito: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., caixa: _Optional[str] = ..., caixa_nome: _Optional[str] = ..., operacao: _Optional[str] = ..., tipo_pagamento: _Optional[str] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ..., wallet_nome: _Optional[str] = ..., wallet_id: _Optional[str] = ..., saldo_not_zero: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMovimentoCaixaResponse(_message.Message):
    __slots__ = ("movimento_caixa_list", "next_page_token")
    MOVIMENTO_CAIXA_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    movimento_caixa_list: _containers.RepeatedCompositeFieldContainer[MovimentoCaixa]
    next_page_token: str
    def __init__(self, movimento_caixa_list: _Optional[_Iterable[_Union[MovimentoCaixa, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportMovimentoCaixaRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "list_movimento_caixa_request")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_MOVIMENTO_CAIXA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    list_movimento_caixa_request: ListMovimentoCaixaRequest
    def __init__(self, tipo_relatorio: _Optional[str] = ..., list_movimento_caixa_request: _Optional[_Union[ListMovimentoCaixaRequest, _Mapping]] = ...) -> None: ...

class ReportMovimentoCaixaResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class GetSaldoMovimentoCaixaRequest(_message.Message):
    __slots__ = ("caixa_id", "usuario_caixa_id", "data")
    CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    caixa_id: str
    usuario_caixa_id: str
    data: _timestamp_pb2.Timestamp
    def __init__(self, caixa_id: _Optional[str] = ..., usuario_caixa_id: _Optional[str] = ..., data: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetSaldoMovimentoCaixaResponse(_message.Message):
    __slots__ = ("saldo",)
    SALDO_FIELD_NUMBER: _ClassVar[int]
    saldo: float
    def __init__(self, saldo: _Optional[float] = ...) -> None: ...

class TransferenciaCaixaRequest(_message.Message):
    __slots__ = ("caixa_origem_id", "caixa_destino_id", "tipo_pagamento", "valor", "itens")
    CAIXA_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    caixa_origem_id: str
    caixa_destino_id: str
    tipo_pagamento: str
    valor: float
    itens: _containers.RepeatedCompositeFieldContainer[TransferenciaItem]
    def __init__(self, caixa_origem_id: _Optional[str] = ..., caixa_destino_id: _Optional[str] = ..., tipo_pagamento: _Optional[str] = ..., valor: _Optional[float] = ..., itens: _Optional[_Iterable[_Union[TransferenciaItem, _Mapping]]] = ...) -> None: ...

class TransferenciaItem(_message.Message):
    __slots__ = ("tipo_pagamento", "valor")
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    tipo_pagamento: str
    valor: float
    def __init__(self, tipo_pagamento: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class TransferenciaCaixaResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class BatchUpdateRequest(_message.Message):
    __slots__ = ("origem_ids", "plano_conta_id", "plano_conta_nome", "centro_custo_id", "centro_custo_nome")
    ORIGEM_IDS_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    origem_ids: _containers.RepeatedScalarFieldContainer[str]
    plano_conta_id: str
    plano_conta_nome: str
    centro_custo_id: str
    centro_custo_nome: str
    def __init__(self, origem_ids: _Optional[_Iterable[str]] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ...) -> None: ...

class BatchUpdateResponse(_message.Message):
    __slots__ = ("updated_count", "message")
    UPDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    updated_count: int
    message: str
    def __init__(self, updated_count: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
