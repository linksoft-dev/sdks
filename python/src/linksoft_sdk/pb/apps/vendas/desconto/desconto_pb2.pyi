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
    TIPO_DESCONTO: _ClassVar[Tipo]
    TIPO_PROMOCOES: _ClassVar[Tipo]

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[Situacao]
    SITUACAO_ATIVO: _ClassVar[Situacao]
    SITUACAO_INATIVO: _ClassVar[Situacao]

class CanalVenda(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANAL_VENDA_UNSPECIFIED: _ClassVar[CanalVenda]
    CANAL_VENDA_LOJA_FISICA: _ClassVar[CanalVenda]
    CANAL_VENDA_LOJA_VIRTUAL: _ClassVar[CanalVenda]

class TipoGrupo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_GRUPO_UNSPECIFIED: _ClassVar[TipoGrupo]
    TIPO_GRUPO_CLIENTE: _ClassVar[TipoGrupo]
    TIPO_GRUPO_VENDEDOR: _ClassVar[TipoGrupo]

class TipoItem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_ITEM_UNSPECIFIED: _ClassVar[TipoItem]
    TIPO_ITEM_POR_CATEGORIA_PRODUTO: _ClassVar[TipoItem]
    TIPO_ITEM_POR_CATEGORIA_SERVICO: _ClassVar[TipoItem]
    TIPO_ITEM_POR_SERVICO: _ClassVar[TipoItem]
    TIPO_ITEM_POR_PRODUTO: _ClassVar[TipoItem]
TIPO_UNSPECIFIED: Tipo
TIPO_DESCONTO: Tipo
TIPO_PROMOCOES: Tipo
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_ATIVO: Situacao
SITUACAO_INATIVO: Situacao
CANAL_VENDA_UNSPECIFIED: CanalVenda
CANAL_VENDA_LOJA_FISICA: CanalVenda
CANAL_VENDA_LOJA_VIRTUAL: CanalVenda
TIPO_GRUPO_UNSPECIFIED: TipoGrupo
TIPO_GRUPO_CLIENTE: TipoGrupo
TIPO_GRUPO_VENDEDOR: TipoGrupo
TIPO_ITEM_UNSPECIFIED: TipoItem
TIPO_ITEM_POR_CATEGORIA_PRODUTO: TipoItem
TIPO_ITEM_POR_CATEGORIA_SERVICO: TipoItem
TIPO_ITEM_POR_SERVICO: TipoItem
TIPO_ITEM_POR_PRODUTO: TipoItem

class Desconto(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "nome", "tipo", "situacao", "situacao_caption", "tipo_grupo", "grupo_id", "grupo_nome", "validade_a_partir", "validade_ate", "dia_semana_segunda", "dia_semana_segunda_horario_inicial", "dia_semana_segunda_horario_final", "dia_semana_terca", "dia_semana_terca_horario_inicial", "dia_semana_terca_horario_final", "dia_semana_quarta", "dia_semana_quarta_horario_inicial", "dia_semana_quarta_horario_final", "dia_semana_quinta", "dia_semana_quinta_horario_inicial", "dia_semana_quinta_horario_final", "dia_semana_sexta", "dia_semana_sexta_horario_inicial", "dia_semana_sexta_horario_final", "dia_semana_sabado", "dia_semana_sabado_horario_inicial", "dia_semana_sabado_horario_final", "dia_semana_domingo", "dia_semana_domingo_horario_inicial", "dia_semana_domingo_horario_final", "itens", "valor_venda_maior_que", "desconto_percentual", "coupon", "desconto_valor", "cumulativo", "autorizado_acima_do_teto", "autorizado_por_user_id", "autorizado_por_user_name", "autorizado_em", "percentual_efetivo_autorizado", "prioridade", "desconto_maximo_valor", "canais", "tabelas_preco", "somente_primeira_compra")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_CAPTION_FIELD_NUMBER: _ClassVar[int]
    TIPO_GRUPO_FIELD_NUMBER: _ClassVar[int]
    GRUPO_ID_FIELD_NUMBER: _ClassVar[int]
    GRUPO_NOME_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_A_PARTIR_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_ATE_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEGUNDA_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEGUNDA_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEGUNDA_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_TERCA_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_TERCA_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_TERCA_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUARTA_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUARTA_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUARTA_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUINTA_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUINTA_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_QUINTA_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEXTA_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEXTA_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SEXTA_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SABADO_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SABADO_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_SABADO_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_DOMINGO_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_DOMINGO_HORARIO_INICIAL_FIELD_NUMBER: _ClassVar[int]
    DIA_SEMANA_DOMINGO_HORARIO_FINAL_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    VALOR_VENDA_MAIOR_QUE_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_VALOR_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVO_FIELD_NUMBER: _ClassVar[int]
    AUTORIZADO_ACIMA_DO_TETO_FIELD_NUMBER: _ClassVar[int]
    AUTORIZADO_POR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTORIZADO_POR_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTORIZADO_EM_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_EFETIVO_AUTORIZADO_FIELD_NUMBER: _ClassVar[int]
    PRIORIDADE_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_MAXIMO_VALOR_FIELD_NUMBER: _ClassVar[int]
    CANAIS_FIELD_NUMBER: _ClassVar[int]
    TABELAS_PRECO_FIELD_NUMBER: _ClassVar[int]
    SOMENTE_PRIMEIRA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    nome: str
    tipo: Tipo
    situacao: Situacao
    situacao_caption: str
    tipo_grupo: TipoGrupo
    grupo_id: str
    grupo_nome: str
    validade_a_partir: _timestamp_pb2.Timestamp
    validade_ate: _timestamp_pb2.Timestamp
    dia_semana_segunda: bool
    dia_semana_segunda_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_segunda_horario_final: _timestamp_pb2.Timestamp
    dia_semana_terca: bool
    dia_semana_terca_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_terca_horario_final: _timestamp_pb2.Timestamp
    dia_semana_quarta: bool
    dia_semana_quarta_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_quarta_horario_final: _timestamp_pb2.Timestamp
    dia_semana_quinta: bool
    dia_semana_quinta_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_quinta_horario_final: _timestamp_pb2.Timestamp
    dia_semana_sexta: bool
    dia_semana_sexta_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_sexta_horario_final: _timestamp_pb2.Timestamp
    dia_semana_sabado: bool
    dia_semana_sabado_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_sabado_horario_final: _timestamp_pb2.Timestamp
    dia_semana_domingo: bool
    dia_semana_domingo_horario_inicial: _timestamp_pb2.Timestamp
    dia_semana_domingo_horario_final: _timestamp_pb2.Timestamp
    itens: _containers.RepeatedCompositeFieldContainer[Item]
    valor_venda_maior_que: float
    desconto_percentual: float
    coupon: Coupon
    desconto_valor: float
    cumulativo: bool
    autorizado_acima_do_teto: bool
    autorizado_por_user_id: str
    autorizado_por_user_name: str
    autorizado_em: _timestamp_pb2.Timestamp
    percentual_efetivo_autorizado: float
    prioridade: int
    desconto_maximo_valor: float
    canais: _containers.RepeatedScalarFieldContainer[CanalVenda]
    tabelas_preco: _containers.RepeatedScalarFieldContainer[str]
    somente_primeira_compra: bool
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., nome: _Optional[str] = ..., tipo: _Optional[_Union[Tipo, str]] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., situacao_caption: _Optional[str] = ..., tipo_grupo: _Optional[_Union[TipoGrupo, str]] = ..., grupo_id: _Optional[str] = ..., grupo_nome: _Optional[str] = ..., validade_a_partir: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., validade_ate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_segunda: _Optional[bool] = ..., dia_semana_segunda_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_segunda_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_terca: _Optional[bool] = ..., dia_semana_terca_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_terca_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_quarta: _Optional[bool] = ..., dia_semana_quarta_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_quarta_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_quinta: _Optional[bool] = ..., dia_semana_quinta_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_quinta_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_sexta: _Optional[bool] = ..., dia_semana_sexta_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_sexta_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_sabado: _Optional[bool] = ..., dia_semana_sabado_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_sabado_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_domingo: _Optional[bool] = ..., dia_semana_domingo_horario_inicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dia_semana_domingo_horario_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., itens: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., valor_venda_maior_que: _Optional[float] = ..., desconto_percentual: _Optional[float] = ..., coupon: _Optional[_Union[Coupon, _Mapping]] = ..., desconto_valor: _Optional[float] = ..., cumulativo: _Optional[bool] = ..., autorizado_acima_do_teto: _Optional[bool] = ..., autorizado_por_user_id: _Optional[str] = ..., autorizado_por_user_name: _Optional[str] = ..., autorizado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., percentual_efetivo_autorizado: _Optional[float] = ..., prioridade: _Optional[int] = ..., desconto_maximo_valor: _Optional[float] = ..., canais: _Optional[_Iterable[_Union[CanalVenda, str]]] = ..., tabelas_preco: _Optional[_Iterable[str]] = ..., somente_primeira_compra: _Optional[bool] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "tipo_item", "item_id", "item_nome", "categoria_id", "categoria_nome", "quantidade_maior_que", "desconto_percentual", "excecao")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_ITEM_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NOME_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_MAIOR_QUE_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    EXCECAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tipo_item: TipoItem
    item_id: str
    item_nome: str
    categoria_id: str
    categoria_nome: str
    quantidade_maior_que: float
    desconto_percentual: float
    excecao: bool
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tipo_item: _Optional[_Union[TipoItem, str]] = ..., item_id: _Optional[str] = ..., item_nome: _Optional[str] = ..., categoria_id: _Optional[str] = ..., categoria_nome: _Optional[str] = ..., quantidade_maior_que: _Optional[float] = ..., desconto_percentual: _Optional[float] = ..., excecao: _Optional[bool] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("desconto",)
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("desconto",)
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "desconto", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    desconto: Desconto
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., desconto: _Optional[_Union[Desconto, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("desconto",)
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("desconto",)
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("desconto_list", "next_page_token")
    DESCONTO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    desconto_list: _containers.RepeatedCompositeFieldContainer[Desconto]
    next_page_token: str
    def __init__(self, desconto_list: _Optional[_Iterable[_Union[Desconto, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Criterio(_message.Message):
    __slots__ = ("tipo", "cliente_id", "vendedor_id", "itens", "valor_venda", "canal", "tabela_preco", "primeira_compra")
    TIPO_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_ID_FIELD_NUMBER: _ClassVar[int]
    VENDEDOR_ID_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    VALOR_VENDA_FIELD_NUMBER: _ClassVar[int]
    CANAL_FIELD_NUMBER: _ClassVar[int]
    TABELA_PRECO_FIELD_NUMBER: _ClassVar[int]
    PRIMEIRA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    tipo: Tipo
    cliente_id: str
    vendedor_id: str
    itens: _containers.RepeatedCompositeFieldContainer[CriterioItem]
    valor_venda: float
    canal: CanalVenda
    tabela_preco: str
    primeira_compra: bool
    def __init__(self, tipo: _Optional[_Union[Tipo, str]] = ..., cliente_id: _Optional[str] = ..., vendedor_id: _Optional[str] = ..., itens: _Optional[_Iterable[_Union[CriterioItem, _Mapping]]] = ..., valor_venda: _Optional[float] = ..., canal: _Optional[_Union[CanalVenda, str]] = ..., tabela_preco: _Optional[str] = ..., primeira_compra: _Optional[bool] = ...) -> None: ...

class CriterioItem(_message.Message):
    __slots__ = ("id", "tipo_item", "quantidade", "categoria_id", "valor")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_ITEM_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_ID_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo_item: TipoItem
    quantidade: float
    categoria_id: str
    valor: float
    def __init__(self, id: _Optional[str] = ..., tipo_item: _Optional[_Union[TipoItem, str]] = ..., quantidade: _Optional[float] = ..., categoria_id: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class DescontoElegivel(_message.Message):
    __slots__ = ("id", "nome", "todos_os_itens", "percentual_desconto", "itens", "valor_desconto")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TODOS_OS_ITENS_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_DESCONTO_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    VALOR_DESCONTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    todos_os_itens: bool
    percentual_desconto: float
    itens: _containers.RepeatedCompositeFieldContainer[DescontoElegivelItem]
    valor_desconto: float
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., todos_os_itens: _Optional[bool] = ..., percentual_desconto: _Optional[float] = ..., itens: _Optional[_Iterable[_Union[DescontoElegivelItem, _Mapping]]] = ..., valor_desconto: _Optional[float] = ...) -> None: ...

class DescontoElegivelItem(_message.Message):
    __slots__ = ("item_id", "tipo_item", "percentual_desconto")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_ITEM_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_DESCONTO_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    tipo_item: TipoItem
    percentual_desconto: float
    def __init__(self, item_id: _Optional[str] = ..., tipo_item: _Optional[_Union[TipoItem, str]] = ..., percentual_desconto: _Optional[float] = ...) -> None: ...

class GetDescontoRequest(_message.Message):
    __slots__ = ("criterio",)
    CRITERIO_FIELD_NUMBER: _ClassVar[int]
    criterio: Criterio
    def __init__(self, criterio: _Optional[_Union[Criterio, _Mapping]] = ...) -> None: ...

class GetDescontoResponse(_message.Message):
    __slots__ = ("desconto_elegivel", "precisa_primeira_compra")
    DESCONTO_ELEGIVEL_FIELD_NUMBER: _ClassVar[int]
    PRECISA_PRIMEIRA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    desconto_elegivel: DescontoElegivel
    precisa_primeira_compra: bool
    def __init__(self, desconto_elegivel: _Optional[_Union[DescontoElegivel, _Mapping]] = ..., precisa_primeira_compra: _Optional[bool] = ...) -> None: ...

class Coupon(_message.Message):
    __slots__ = ("code", "usage_limit", "usage_count", "usage_history", "usage_limit_per_customer", "release_on_cancel")
    CODE_FIELD_NUMBER: _ClassVar[int]
    USAGE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    USAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USAGE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    USAGE_LIMIT_PER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ON_CANCEL_FIELD_NUMBER: _ClassVar[int]
    code: str
    usage_limit: int
    usage_count: int
    usage_history: _containers.RepeatedCompositeFieldContainer[CouponUsage]
    usage_limit_per_customer: int
    release_on_cancel: bool
    def __init__(self, code: _Optional[str] = ..., usage_limit: _Optional[int] = ..., usage_count: _Optional[int] = ..., usage_history: _Optional[_Iterable[_Union[CouponUsage, _Mapping]]] = ..., usage_limit_per_customer: _Optional[int] = ..., release_on_cancel: _Optional[bool] = ...) -> None: ...

class CouponUsage(_message.Message):
    __slots__ = ("used_at", "user_id", "user_name", "order_id", "order_number", "client_id", "client_name", "order_value", "discount_value", "client_cpf_cnpj")
    USED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    used_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    order_id: str
    order_number: str
    client_id: str
    client_name: str
    order_value: float
    discount_value: float
    client_cpf_cnpj: str
    def __init__(self, used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., order_id: _Optional[str] = ..., order_number: _Optional[str] = ..., client_id: _Optional[str] = ..., client_name: _Optional[str] = ..., order_value: _Optional[float] = ..., discount_value: _Optional[float] = ..., client_cpf_cnpj: _Optional[str] = ...) -> None: ...

class UseCouponRequest(_message.Message):
    __slots__ = ("code", "order_id", "client_id", "client_cpf_cnpj", "order_number", "order_value", "discount_value")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_VALUE_FIELD_NUMBER: _ClassVar[int]
    code: str
    order_id: str
    client_id: str
    client_cpf_cnpj: str
    order_number: str
    order_value: float
    discount_value: float
    def __init__(self, code: _Optional[str] = ..., order_id: _Optional[str] = ..., client_id: _Optional[str] = ..., client_cpf_cnpj: _Optional[str] = ..., order_number: _Optional[str] = ..., order_value: _Optional[float] = ..., discount_value: _Optional[float] = ...) -> None: ...

class UseCouponResponse(_message.Message):
    __slots__ = ("desconto", "was_exhausted", "usage")
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    WAS_EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    was_exhausted: bool
    usage: CouponUsage
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ..., was_exhausted: _Optional[bool] = ..., usage: _Optional[_Union[CouponUsage, _Mapping]] = ...) -> None: ...

class ReleaseCouponRequest(_message.Message):
    __slots__ = ("code", "order_id")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    order_id: str
    def __init__(self, code: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...

class ReleaseCouponResponse(_message.Message):
    __slots__ = ("desconto", "released")
    DESCONTO_FIELD_NUMBER: _ClassVar[int]
    RELEASED_FIELD_NUMBER: _ClassVar[int]
    desconto: Desconto
    released: bool
    def __init__(self, desconto: _Optional[_Union[Desconto, _Mapping]] = ..., released: _Optional[bool] = ...) -> None: ...

class ValidateCouponRequest(_message.Message):
    __slots__ = ("code", "criterio", "cpf_cnpj", "tem_desconto_aplicado")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CRITERIO_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    TEM_DESCONTO_APLICADO_FIELD_NUMBER: _ClassVar[int]
    code: str
    criterio: Criterio
    cpf_cnpj: str
    tem_desconto_aplicado: bool
    def __init__(self, code: _Optional[str] = ..., criterio: _Optional[_Union[Criterio, _Mapping]] = ..., cpf_cnpj: _Optional[str] = ..., tem_desconto_aplicado: _Optional[bool] = ...) -> None: ...

class ValidateCouponResponse(_message.Message):
    __slots__ = ("valid", "message", "desconto_elegivel", "cupom_id", "cumulativo", "precisa_primeira_compra")
    VALID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_ELEGIVEL_FIELD_NUMBER: _ClassVar[int]
    CUPOM_ID_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVO_FIELD_NUMBER: _ClassVar[int]
    PRECISA_PRIMEIRA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    message: str
    desconto_elegivel: DescontoElegivel
    cupom_id: str
    cumulativo: bool
    precisa_primeira_compra: bool
    def __init__(self, valid: _Optional[bool] = ..., message: _Optional[str] = ..., desconto_elegivel: _Optional[_Union[DescontoElegivel, _Mapping]] = ..., cupom_id: _Optional[str] = ..., cumulativo: _Optional[bool] = ..., precisa_primeira_compra: _Optional[bool] = ...) -> None: ...

class ProdutoConsultado(_message.Message):
    __slots__ = ("produto_id", "categoria_id")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_ID_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    categoria_id: str
    def __init__(self, produto_id: _Optional[str] = ..., categoria_id: _Optional[str] = ...) -> None: ...

class GetDescontosProdutosRequest(_message.Message):
    __slots__ = ("produtos", "cliente_id", "canal")
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_ID_FIELD_NUMBER: _ClassVar[int]
    CANAL_FIELD_NUMBER: _ClassVar[int]
    produtos: _containers.RepeatedCompositeFieldContainer[ProdutoConsultado]
    cliente_id: str
    canal: CanalVenda
    def __init__(self, produtos: _Optional[_Iterable[_Union[ProdutoConsultado, _Mapping]]] = ..., cliente_id: _Optional[str] = ..., canal: _Optional[_Union[CanalVenda, str]] = ...) -> None: ...

class DescontoProduto(_message.Message):
    __slots__ = ("produto_id", "percentual_desconto", "desconto_id", "desconto_nome")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_DESCONTO_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_ID_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_NOME_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    percentual_desconto: float
    desconto_id: str
    desconto_nome: str
    def __init__(self, produto_id: _Optional[str] = ..., percentual_desconto: _Optional[float] = ..., desconto_id: _Optional[str] = ..., desconto_nome: _Optional[str] = ...) -> None: ...

class GetDescontosProdutosResponse(_message.Message):
    __slots__ = ("descontos",)
    DESCONTOS_FIELD_NUMBER: _ClassVar[int]
    descontos: _containers.RepeatedCompositeFieldContainer[DescontoProduto]
    def __init__(self, descontos: _Optional[_Iterable[_Union[DescontoProduto, _Mapping]]] = ...) -> None: ...
