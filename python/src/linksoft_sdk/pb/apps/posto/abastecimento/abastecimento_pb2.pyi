import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
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
    SITUACAO_EM_VENDA: _ClassVar[Situacao]
    SITUACAO_VENDIDO: _ClassVar[Situacao]
    SITUACAO_AFERICAO: _ClassVar[Situacao]

class Tipo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_UNSPECIFIED: _ClassVar[Tipo]
    TIPO_NORMAL: _ClassVar[Tipo]
    TIPO_AFERICAO: _ClassVar[Tipo]
    TIPO_OFFLINE: _ClassVar[Tipo]
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_PENDENTE: Situacao
SITUACAO_EM_VENDA: Situacao
SITUACAO_VENDIDO: Situacao
SITUACAO_AFERICAO: Situacao
TIPO_UNSPECIFIED: Tipo
TIPO_NORMAL: Tipo
TIPO_AFERICAO: Tipo
TIPO_OFFLINE: Tipo

class Abastecimento(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "origem_id", "marca", "num_bico", "num_bomba", "num_tanque", "produto_id", "produto_nome", "codigo_anp", "volume", "preco_unitario", "valor_total", "encerrante_inicial", "encerrante_final", "data_hora", "situacao", "tipo", "pedido_id", "pedido_numero", "reserva_user_id", "reserva_user_name", "reserva_em", "bloqueio", "frentista_codigo", "frentista_id", "frentista_nome", "nivel_preco", "veiculo_tag", "posto_veiculo_id", "posto_placa")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    MARCA_FIELD_NUMBER: _ClassVar[int]
    NUM_BICO_FIELD_NUMBER: _ClassVar[int]
    NUM_BOMBA_FIELD_NUMBER: _ClassVar[int]
    NUM_TANQUE_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_ANP_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRECO_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    VALOR_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_INICIAL_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_FINAL_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_ID_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_NUMERO_FIELD_NUMBER: _ClassVar[int]
    RESERVA_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVA_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    RESERVA_EM_FIELD_NUMBER: _ClassVar[int]
    BLOQUEIO_FIELD_NUMBER: _ClassVar[int]
    FRENTISTA_CODIGO_FIELD_NUMBER: _ClassVar[int]
    FRENTISTA_ID_FIELD_NUMBER: _ClassVar[int]
    FRENTISTA_NOME_FIELD_NUMBER: _ClassVar[int]
    NIVEL_PRECO_FIELD_NUMBER: _ClassVar[int]
    VEICULO_TAG_FIELD_NUMBER: _ClassVar[int]
    POSTO_VEICULO_ID_FIELD_NUMBER: _ClassVar[int]
    POSTO_PLACA_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    origem_id: str
    marca: str
    num_bico: int
    num_bomba: str
    num_tanque: str
    produto_id: str
    produto_nome: str
    codigo_anp: str
    volume: float
    preco_unitario: float
    valor_total: float
    encerrante_inicial: float
    encerrante_final: float
    data_hora: _timestamp_pb2.Timestamp
    situacao: Situacao
    tipo: Tipo
    pedido_id: str
    pedido_numero: int
    reserva_user_id: str
    reserva_user_name: str
    reserva_em: _timestamp_pb2.Timestamp
    bloqueio: str
    frentista_codigo: str
    frentista_id: str
    frentista_nome: str
    nivel_preco: int
    veiculo_tag: str
    posto_veiculo_id: str
    posto_placa: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., origem_id: _Optional[str] = ..., marca: _Optional[str] = ..., num_bico: _Optional[int] = ..., num_bomba: _Optional[str] = ..., num_tanque: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., codigo_anp: _Optional[str] = ..., volume: _Optional[float] = ..., preco_unitario: _Optional[float] = ..., valor_total: _Optional[float] = ..., encerrante_inicial: _Optional[float] = ..., encerrante_final: _Optional[float] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., tipo: _Optional[_Union[Tipo, str]] = ..., pedido_id: _Optional[str] = ..., pedido_numero: _Optional[int] = ..., reserva_user_id: _Optional[str] = ..., reserva_user_name: _Optional[str] = ..., reserva_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bloqueio: _Optional[str] = ..., frentista_codigo: _Optional[str] = ..., frentista_id: _Optional[str] = ..., frentista_nome: _Optional[str] = ..., nivel_preco: _Optional[int] = ..., veiculo_tag: _Optional[str] = ..., posto_veiculo_id: _Optional[str] = ..., posto_placa: _Optional[str] = ...) -> None: ...

class GetAbastecimentoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAbastecimentoResponse(_message.Message):
    __slots__ = ("abastecimento",)
    ABASTECIMENTO_FIELD_NUMBER: _ClassVar[int]
    abastecimento: Abastecimento
    def __init__(self, abastecimento: _Optional[_Union[Abastecimento, _Mapping]] = ...) -> None: ...

class ListAbastecimentoRequest(_message.Message):
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

class ListAbastecimentoResponse(_message.Message):
    __slots__ = ("abastecimento_list", "next_page_token")
    ABASTECIMENTO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    abastecimento_list: _containers.RepeatedCompositeFieldContainer[Abastecimento]
    next_page_token: str
    def __init__(self, abastecimento_list: _Optional[_Iterable[_Union[Abastecimento, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RecebeRequest(_message.Message):
    __slots__ = ("marca", "abastecimentos")
    MARCA_FIELD_NUMBER: _ClassVar[int]
    ABASTECIMENTOS_FIELD_NUMBER: _ClassVar[int]
    marca: str
    abastecimentos: _containers.RepeatedCompositeFieldContainer[Abastecimento]
    def __init__(self, marca: _Optional[str] = ..., abastecimentos: _Optional[_Iterable[_Union[Abastecimento, _Mapping]]] = ...) -> None: ...

class Recusa(_message.Message):
    __slots__ = ("origem_id", "motivo")
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    origem_id: str
    motivo: str
    def __init__(self, origem_id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class RecebeResponse(_message.Message):
    __slots__ = ("aceitos", "recusas")
    ACEITOS_FIELD_NUMBER: _ClassVar[int]
    RECUSAS_FIELD_NUMBER: _ClassVar[int]
    aceitos: _containers.RepeatedScalarFieldContainer[str]
    recusas: _containers.RepeatedCompositeFieldContainer[Recusa]
    def __init__(self, aceitos: _Optional[_Iterable[str]] = ..., recusas: _Optional[_Iterable[_Union[Recusa, _Mapping]]] = ...) -> None: ...

class ReservaRequest(_message.Message):
    __slots__ = ("id", "frentista_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    FRENTISTA_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    frentista_id: str
    def __init__(self, id: _Optional[str] = ..., frentista_id: _Optional[str] = ...) -> None: ...

class ReservaResponse(_message.Message):
    __slots__ = ("abastecimento",)
    ABASTECIMENTO_FIELD_NUMBER: _ClassVar[int]
    abastecimento: Abastecimento
    def __init__(self, abastecimento: _Optional[_Union[Abastecimento, _Mapping]] = ...) -> None: ...

class AfericaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AfericaoResponse(_message.Message):
    __slots__ = ("abastecimento",)
    ABASTECIMENTO_FIELD_NUMBER: _ClassVar[int]
    abastecimento: Abastecimento
    def __init__(self, abastecimento: _Optional[_Union[Abastecimento, _Mapping]] = ...) -> None: ...

class ResumoPorBicoRequest(_message.Message):
    __slots__ = ("data_hora_inicial", "data_hora_final")
    DATA_HORA_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FINAL_FIELD_NUMBER: _ClassVar[int]
    data_hora_inicial: _timestamp_pb2.Timestamp
    data_hora_final: _timestamp_pb2.Timestamp
    def __init__(self, data_hora_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Salto(_message.Message):
    __slots__ = ("data_hora", "encerrante_final_anterior", "encerrante_inicial", "litros")
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_FINAL_ANTERIOR_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_INICIAL_FIELD_NUMBER: _ClassVar[int]
    LITROS_FIELD_NUMBER: _ClassVar[int]
    data_hora: _timestamp_pb2.Timestamp
    encerrante_final_anterior: float
    encerrante_inicial: float
    litros: float
    def __init__(self, data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., encerrante_final_anterior: _Optional[float] = ..., encerrante_inicial: _Optional[float] = ..., litros: _Optional[float] = ...) -> None: ...

class ResumoBico(_message.Message):
    __slots__ = ("num_bico", "num_bomba", "num_tanque", "produto_id", "produto_nome", "encerrante_inicial", "encerrante_final", "litros_encerrante", "litros_vendidos", "litros_afericao", "litros_pendentes", "litros_em_venda", "diferenca", "valor_vendido", "quantidade", "saltos")
    NUM_BICO_FIELD_NUMBER: _ClassVar[int]
    NUM_BOMBA_FIELD_NUMBER: _ClassVar[int]
    NUM_TANQUE_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_INICIAL_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_FINAL_FIELD_NUMBER: _ClassVar[int]
    LITROS_ENCERRANTE_FIELD_NUMBER: _ClassVar[int]
    LITROS_VENDIDOS_FIELD_NUMBER: _ClassVar[int]
    LITROS_AFERICAO_FIELD_NUMBER: _ClassVar[int]
    LITROS_PENDENTES_FIELD_NUMBER: _ClassVar[int]
    LITROS_EM_VENDA_FIELD_NUMBER: _ClassVar[int]
    DIFERENCA_FIELD_NUMBER: _ClassVar[int]
    VALOR_VENDIDO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    SALTOS_FIELD_NUMBER: _ClassVar[int]
    num_bico: int
    num_bomba: str
    num_tanque: str
    produto_id: str
    produto_nome: str
    encerrante_inicial: float
    encerrante_final: float
    litros_encerrante: float
    litros_vendidos: float
    litros_afericao: float
    litros_pendentes: float
    litros_em_venda: float
    diferenca: float
    valor_vendido: float
    quantidade: int
    saltos: _containers.RepeatedCompositeFieldContainer[Salto]
    def __init__(self, num_bico: _Optional[int] = ..., num_bomba: _Optional[str] = ..., num_tanque: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., encerrante_inicial: _Optional[float] = ..., encerrante_final: _Optional[float] = ..., litros_encerrante: _Optional[float] = ..., litros_vendidos: _Optional[float] = ..., litros_afericao: _Optional[float] = ..., litros_pendentes: _Optional[float] = ..., litros_em_venda: _Optional[float] = ..., diferenca: _Optional[float] = ..., valor_vendido: _Optional[float] = ..., quantidade: _Optional[int] = ..., saltos: _Optional[_Iterable[_Union[Salto, _Mapping]]] = ...) -> None: ...

class ResumoPorBicoResponse(_message.Message):
    __slots__ = ("bicos", "avisos")
    BICOS_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    bicos: _containers.RepeatedCompositeFieldContainer[ResumoBico]
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, bicos: _Optional[_Iterable[_Union[ResumoBico, _Mapping]]] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...
