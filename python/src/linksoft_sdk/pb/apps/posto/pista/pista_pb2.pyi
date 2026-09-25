import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.posto.abastecimento import abastecimento_pb2 as _abastecimento_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EstadoBico(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESTADO_BICO_UNSPECIFIED: _ClassVar[EstadoBico]
    ESTADO_BICO_LIVRE: _ClassVar[EstadoBico]
    ESTADO_BICO_ABASTECENDO: _ClassVar[EstadoBico]
    ESTADO_BICO_INDISPONIVEL: _ClassVar[EstadoBico]
ESTADO_BICO_UNSPECIFIED: EstadoBico
ESTADO_BICO_LIVRE: EstadoBico
ESTADO_BICO_ABASTECENDO: EstadoBico
ESTADO_BICO_INDISPONIVEL: EstadoBico

class BicoEstado(_message.Message):
    __slots__ = ("numero", "bomba", "tanque", "estado", "preco", "encerrante", "volume_parcial", "valor_parcial", "produto")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    TANQUE_FIELD_NUMBER: _ClassVar[int]
    ESTADO_FIELD_NUMBER: _ClassVar[int]
    PRECO_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PARCIAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_PARCIAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    numero: int
    bomba: str
    tanque: str
    estado: EstadoBico
    preco: float
    encerrante: float
    volume_parcial: float
    valor_parcial: float
    produto: str
    def __init__(self, numero: _Optional[int] = ..., bomba: _Optional[str] = ..., tanque: _Optional[str] = ..., estado: _Optional[_Union[EstadoBico, str]] = ..., preco: _Optional[float] = ..., encerrante: _Optional[float] = ..., volume_parcial: _Optional[float] = ..., valor_parcial: _Optional[float] = ..., produto: _Optional[str] = ...) -> None: ...

class Pista(_message.Message):
    __slots__ = ("id", "marca", "versao_agente", "atualizado_em", "concentrador_conectado", "erro", "bicos", "codigo_pareamento", "codigo_expira_em", "codigo_usuario_id", "codigo_usuario_nome", "codigo_org_nome", "aceita_comandos", "tanques")
    ID_FIELD_NUMBER: _ClassVar[int]
    MARCA_FIELD_NUMBER: _ClassVar[int]
    VERSAO_AGENTE_FIELD_NUMBER: _ClassVar[int]
    ATUALIZADO_EM_FIELD_NUMBER: _ClassVar[int]
    CONCENTRADOR_CONECTADO_FIELD_NUMBER: _ClassVar[int]
    ERRO_FIELD_NUMBER: _ClassVar[int]
    BICOS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_PAREAMENTO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_EXPIRA_EM_FIELD_NUMBER: _ClassVar[int]
    CODIGO_USUARIO_ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_USUARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    ACEITA_COMANDOS_FIELD_NUMBER: _ClassVar[int]
    TANQUES_FIELD_NUMBER: _ClassVar[int]
    id: str
    marca: str
    versao_agente: str
    atualizado_em: _timestamp_pb2.Timestamp
    concentrador_conectado: bool
    erro: str
    bicos: _containers.RepeatedCompositeFieldContainer[BicoEstado]
    codigo_pareamento: str
    codigo_expira_em: _timestamp_pb2.Timestamp
    codigo_usuario_id: str
    codigo_usuario_nome: str
    codigo_org_nome: str
    aceita_comandos: bool
    tanques: _containers.RepeatedCompositeFieldContainer[TanquePista]
    def __init__(self, id: _Optional[str] = ..., marca: _Optional[str] = ..., versao_agente: _Optional[str] = ..., atualizado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., concentrador_conectado: _Optional[bool] = ..., erro: _Optional[str] = ..., bicos: _Optional[_Iterable[_Union[BicoEstado, _Mapping]]] = ..., codigo_pareamento: _Optional[str] = ..., codigo_expira_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., codigo_usuario_id: _Optional[str] = ..., codigo_usuario_nome: _Optional[str] = ..., codigo_org_nome: _Optional[str] = ..., aceita_comandos: _Optional[bool] = ..., tanques: _Optional[_Iterable[_Union[TanquePista, _Mapping]]] = ...) -> None: ...

class TanquePista(_message.Message):
    __slots__ = ("numero", "capacidade")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    CAPACIDADE_FIELD_NUMBER: _ClassVar[int]
    numero: int
    capacidade: float
    def __init__(self, numero: _Optional[int] = ..., capacidade: _Optional[float] = ...) -> None: ...

class GetPistaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPistaResponse(_message.Message):
    __slots__ = ("pareado", "pareado_por", "pareado_em", "conectado", "pista", "pendentes")
    PAREADO_FIELD_NUMBER: _ClassVar[int]
    PAREADO_POR_FIELD_NUMBER: _ClassVar[int]
    PAREADO_EM_FIELD_NUMBER: _ClassVar[int]
    CONECTADO_FIELD_NUMBER: _ClassVar[int]
    PISTA_FIELD_NUMBER: _ClassVar[int]
    PENDENTES_FIELD_NUMBER: _ClassVar[int]
    pareado: bool
    pareado_por: str
    pareado_em: _timestamp_pb2.Timestamp
    conectado: bool
    pista: Pista
    pendentes: _containers.RepeatedCompositeFieldContainer[_abastecimento_pb2.Abastecimento]
    def __init__(self, pareado: _Optional[bool] = ..., pareado_por: _Optional[str] = ..., pareado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., conectado: _Optional[bool] = ..., pista: _Optional[_Union[Pista, _Mapping]] = ..., pendentes: _Optional[_Iterable[_Union[_abastecimento_pb2.Abastecimento, _Mapping]]] = ...) -> None: ...

class RecebeEstadoRequest(_message.Message):
    __slots__ = ("pista",)
    PISTA_FIELD_NUMBER: _ClassVar[int]
    pista: Pista
    def __init__(self, pista: _Optional[_Union[Pista, _Mapping]] = ...) -> None: ...

class RecebeEstadoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IniciaPareamentoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IniciaPareamentoResponse(_message.Message):
    __slots__ = ("codigo", "expira_em")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    EXPIRA_EM_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    expira_em: _timestamp_pb2.Timestamp
    def __init__(self, codigo: _Optional[str] = ..., expira_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PareiaRequest(_message.Message):
    __slots__ = ("codigo", "nome_maquina", "versao_agente")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    NOME_MAQUINA_FIELD_NUMBER: _ClassVar[int]
    VERSAO_AGENTE_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    nome_maquina: str
    versao_agente: str
    def __init__(self, codigo: _Optional[str] = ..., nome_maquina: _Optional[str] = ..., versao_agente: _Optional[str] = ...) -> None: ...

class PareiaResponse(_message.Message):
    __slots__ = ("api_url", "org_id", "org_nome", "client_id", "access_token", "refresh_token", "grant_id")
    API_URL_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    api_url: str
    org_id: str
    org_nome: str
    client_id: str
    access_token: str
    refresh_token: str
    grant_id: str
    def __init__(self, api_url: _Optional[str] = ..., org_id: _Optional[str] = ..., org_nome: _Optional[str] = ..., client_id: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., grant_id: _Optional[str] = ...) -> None: ...

class DespareiaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DespareiaResponse(_message.Message):
    __slots__ = ("revogados",)
    REVOGADOS_FIELD_NUMBER: _ClassVar[int]
    revogados: int
    def __init__(self, revogados: _Optional[int] = ...) -> None: ...
