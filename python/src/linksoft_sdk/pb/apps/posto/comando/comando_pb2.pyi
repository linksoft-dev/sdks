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

class Tipo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_UNSPECIFIED: _ClassVar[Tipo]
    TIPO_PRECO: _ClassVar[Tipo]
    TIPO_PRE_DETERMINA: _ClassVar[Tipo]
    TIPO_AUTORIZA: _ClassVar[Tipo]
    TIPO_BLOQUEIA: _ClassVar[Tipo]
    TIPO_LIBERA: _ClassVar[Tipo]
    TIPO_PARA: _ClassVar[Tipo]

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[Situacao]
    SITUACAO_PENDENTE: _ClassVar[Situacao]
    SITUACAO_ENVIADO: _ClassVar[Situacao]
    SITUACAO_EXECUTADO: _ClassVar[Situacao]
    SITUACAO_FALHOU: _ClassVar[Situacao]
    SITUACAO_EXPIRADO: _ClassVar[Situacao]

class Limite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIMITE_UNSPECIFIED: _ClassVar[Limite]
    LIMITE_VALOR: _ClassVar[Limite]
    LIMITE_LITROS: _ClassVar[Limite]
TIPO_UNSPECIFIED: Tipo
TIPO_PRECO: Tipo
TIPO_PRE_DETERMINA: Tipo
TIPO_AUTORIZA: Tipo
TIPO_BLOQUEIA: Tipo
TIPO_LIBERA: Tipo
TIPO_PARA: Tipo
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_PENDENTE: Situacao
SITUACAO_ENVIADO: Situacao
SITUACAO_EXECUTADO: Situacao
SITUACAO_FALHOU: Situacao
SITUACAO_EXPIRADO: Situacao
LIMITE_UNSPECIFIED: Limite
LIMITE_VALOR: Limite
LIMITE_LITROS: Limite

class Comando(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "tipo", "numero_bomba", "numero_bico", "preco_avista", "preco_aprazo", "limite", "limite_valor", "nivel_preco", "aplicar_em", "expira_em", "situacao", "erro", "executado_em", "grupo_id", "produto_id", "produto_nome")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_BOMBA_FIELD_NUMBER: _ClassVar[int]
    NUMERO_BICO_FIELD_NUMBER: _ClassVar[int]
    PRECO_AVISTA_FIELD_NUMBER: _ClassVar[int]
    PRECO_APRAZO_FIELD_NUMBER: _ClassVar[int]
    LIMITE_FIELD_NUMBER: _ClassVar[int]
    LIMITE_VALOR_FIELD_NUMBER: _ClassVar[int]
    NIVEL_PRECO_FIELD_NUMBER: _ClassVar[int]
    APLICAR_EM_FIELD_NUMBER: _ClassVar[int]
    EXPIRA_EM_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    ERRO_FIELD_NUMBER: _ClassVar[int]
    EXECUTADO_EM_FIELD_NUMBER: _ClassVar[int]
    GRUPO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    tipo: Tipo
    numero_bomba: str
    numero_bico: int
    preco_avista: float
    preco_aprazo: float
    limite: Limite
    limite_valor: float
    nivel_preco: int
    aplicar_em: _timestamp_pb2.Timestamp
    expira_em: _timestamp_pb2.Timestamp
    situacao: Situacao
    erro: str
    executado_em: _timestamp_pb2.Timestamp
    grupo_id: str
    produto_id: str
    produto_nome: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., tipo: _Optional[_Union[Tipo, str]] = ..., numero_bomba: _Optional[str] = ..., numero_bico: _Optional[int] = ..., preco_avista: _Optional[float] = ..., preco_aprazo: _Optional[float] = ..., limite: _Optional[_Union[Limite, str]] = ..., limite_valor: _Optional[float] = ..., nivel_preco: _Optional[int] = ..., aplicar_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expira_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., erro: _Optional[str] = ..., executado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., grupo_id: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ...) -> None: ...

class GetComandoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetComandoResponse(_message.Message):
    __slots__ = ("comando",)
    COMANDO_FIELD_NUMBER: _ClassVar[int]
    comando: Comando
    def __init__(self, comando: _Optional[_Union[Comando, _Mapping]] = ...) -> None: ...

class ListComandoRequest(_message.Message):
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

class ListComandoResponse(_message.Message):
    __slots__ = ("comando_list", "next_page_token")
    COMANDO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    comando_list: _containers.RepeatedCompositeFieldContainer[Comando]
    next_page_token: str
    def __init__(self, comando_list: _Optional[_Iterable[_Union[Comando, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class EnviaRequest(_message.Message):
    __slots__ = ("tipo", "numero_bomba", "numero_bico", "limite", "limite_valor", "nivel_preco")
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_BOMBA_FIELD_NUMBER: _ClassVar[int]
    NUMERO_BICO_FIELD_NUMBER: _ClassVar[int]
    LIMITE_FIELD_NUMBER: _ClassVar[int]
    LIMITE_VALOR_FIELD_NUMBER: _ClassVar[int]
    NIVEL_PRECO_FIELD_NUMBER: _ClassVar[int]
    tipo: Tipo
    numero_bomba: str
    numero_bico: int
    limite: Limite
    limite_valor: float
    nivel_preco: int
    def __init__(self, tipo: _Optional[_Union[Tipo, str]] = ..., numero_bomba: _Optional[str] = ..., numero_bico: _Optional[int] = ..., limite: _Optional[_Union[Limite, str]] = ..., limite_valor: _Optional[float] = ..., nivel_preco: _Optional[int] = ...) -> None: ...

class EnviaResponse(_message.Message):
    __slots__ = ("comando",)
    COMANDO_FIELD_NUMBER: _ClassVar[int]
    comando: Comando
    def __init__(self, comando: _Optional[_Union[Comando, _Mapping]] = ...) -> None: ...

class TrocaPrecoRequest(_message.Message):
    __slots__ = ("produto_id", "preco_avista", "preco_aprazo", "aplicar_em")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRECO_AVISTA_FIELD_NUMBER: _ClassVar[int]
    PRECO_APRAZO_FIELD_NUMBER: _ClassVar[int]
    APLICAR_EM_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    preco_avista: float
    preco_aprazo: float
    aplicar_em: _timestamp_pb2.Timestamp
    def __init__(self, produto_id: _Optional[str] = ..., preco_avista: _Optional[float] = ..., preco_aprazo: _Optional[float] = ..., aplicar_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TrocaPrecoResponse(_message.Message):
    __slots__ = ("comandos",)
    COMANDOS_FIELD_NUMBER: _ClassVar[int]
    comandos: _containers.RepeatedCompositeFieldContainer[Comando]
    def __init__(self, comandos: _Optional[_Iterable[_Union[Comando, _Mapping]]] = ...) -> None: ...

class PendentesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PendentesResponse(_message.Message):
    __slots__ = ("comandos",)
    COMANDOS_FIELD_NUMBER: _ClassVar[int]
    comandos: _containers.RepeatedCompositeFieldContainer[Comando]
    def __init__(self, comandos: _Optional[_Iterable[_Union[Comando, _Mapping]]] = ...) -> None: ...

class ResultadoRequest(_message.Message):
    __slots__ = ("id", "executado", "erro")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTADO_FIELD_NUMBER: _ClassVar[int]
    ERRO_FIELD_NUMBER: _ClassVar[int]
    id: str
    executado: bool
    erro: str
    def __init__(self, id: _Optional[str] = ..., executado: _Optional[bool] = ..., erro: _Optional[str] = ...) -> None: ...

class ResultadoResponse(_message.Message):
    __slots__ = ("comando",)
    COMANDO_FIELD_NUMBER: _ClassVar[int]
    comando: Comando
    def __init__(self, comando: _Optional[_Union[Comando, _Mapping]] = ...) -> None: ...
