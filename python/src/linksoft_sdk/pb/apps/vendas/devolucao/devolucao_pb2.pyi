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

class Operacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERACAO_UNSPECIFIED: _ClassVar[Operacao]
    OPERACAO_SAIDA: _ClassVar[Operacao]
    OPERACAO_ENTRADA: _ClassVar[Operacao]
OPERACAO_UNSPECIFIED: Operacao
OPERACAO_SAIDA: Operacao
OPERACAO_ENTRADA: Operacao

class Devolucao(_message.Message):
    __slots__ = ("id", "numero", "tipo_operacao", "situacao", "venda_id", "venda_numero", "data_hora_compra", "chave_nfe_origem", "importar_dados_origem", "pessoa", "motivo_devolucao", "cancelamento_motivo", "cancelamento_data_hora", "obs", "total", "produtos", "carta_credito_id", "carta_credito_numero", "nfe_id", "nfe_numero", "nfe_serie", "nfe_chave", "nfe_situacao", "url_danfe", "url_xml", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    VENDA_ID_FIELD_NUMBER: _ClassVar[int]
    VENDA_NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    CHAVE_NFE_ORIGEM_FIELD_NUMBER: _ClassVar[int]
    IMPORTAR_DADOS_ORIGEM_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_MOTIVO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    CARTA_CREDITO_ID_FIELD_NUMBER: _ClassVar[int]
    CARTA_CREDITO_NUMERO_FIELD_NUMBER: _ClassVar[int]
    NFE_ID_FIELD_NUMBER: _ClassVar[int]
    NFE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    NFE_SERIE_FIELD_NUMBER: _ClassVar[int]
    NFE_CHAVE_FIELD_NUMBER: _ClassVar[int]
    NFE_SITUACAO_FIELD_NUMBER: _ClassVar[int]
    URL_DANFE_FIELD_NUMBER: _ClassVar[int]
    URL_XML_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero: int
    tipo_operacao: Operacao
    situacao: str
    venda_id: str
    venda_numero: str
    data_hora_compra: _timestamp_pb2.Timestamp
    chave_nfe_origem: str
    importar_dados_origem: bool
    pessoa: Pessoa
    motivo_devolucao: str
    cancelamento_motivo: str
    cancelamento_data_hora: _timestamp_pb2.Timestamp
    obs: str
    total: float
    produtos: _containers.RepeatedCompositeFieldContainer[Produto]
    carta_credito_id: str
    carta_credito_numero: int
    nfe_id: str
    nfe_numero: int
    nfe_serie: int
    nfe_chave: str
    nfe_situacao: str
    url_danfe: str
    url_xml: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., numero: _Optional[int] = ..., tipo_operacao: _Optional[_Union[Operacao, str]] = ..., situacao: _Optional[str] = ..., venda_id: _Optional[str] = ..., venda_numero: _Optional[str] = ..., data_hora_compra: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., chave_nfe_origem: _Optional[str] = ..., importar_dados_origem: _Optional[bool] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., motivo_devolucao: _Optional[str] = ..., cancelamento_motivo: _Optional[str] = ..., cancelamento_data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., obs: _Optional[str] = ..., total: _Optional[float] = ..., produtos: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., carta_credito_id: _Optional[str] = ..., carta_credito_numero: _Optional[int] = ..., nfe_id: _Optional[str] = ..., nfe_numero: _Optional[int] = ..., nfe_serie: _Optional[int] = ..., nfe_chave: _Optional[str] = ..., nfe_situacao: _Optional[str] = ..., url_danfe: _Optional[str] = ..., url_xml: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Pessoa(_message.Message):
    __slots__ = ("id", "cpf_cnpj", "ie", "nome", "nome2", "end_cep", "end_endereco", "end_numero", "end_bairro", "end_cidade", "end_cidade_codigo", "end_uf", "telefone", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    NOME2_FIELD_NUMBER: _ClassVar[int]
    END_CEP_FIELD_NUMBER: _ClassVar[int]
    END_ENDERECO_FIELD_NUMBER: _ClassVar[int]
    END_NUMERO_FIELD_NUMBER: _ClassVar[int]
    END_BAIRRO_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_CODIGO_FIELD_NUMBER: _ClassVar[int]
    END_UF_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    cpf_cnpj: str
    ie: str
    nome: str
    nome2: str
    end_cep: str
    end_endereco: str
    end_numero: str
    end_bairro: str
    end_cidade: str
    end_cidade_codigo: str
    end_uf: str
    telefone: str
    email: str
    def __init__(self, id: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., ie: _Optional[str] = ..., nome: _Optional[str] = ..., nome2: _Optional[str] = ..., end_cep: _Optional[str] = ..., end_endereco: _Optional[str] = ..., end_numero: _Optional[str] = ..., end_bairro: _Optional[str] = ..., end_cidade: _Optional[str] = ..., end_cidade_codigo: _Optional[str] = ..., end_uf: _Optional[str] = ..., telefone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class Produto(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "produto_id", "produto_nome", "codigo", "codigo_barra", "un", "obs", "quantidade", "valor_unitario", "total", "variation_product_id", "venda_item_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_BARRA_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    VENDA_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: str
    updated_at: str
    user_id: str
    user_name: str
    produto_id: str
    produto_nome: str
    codigo: str
    codigo_barra: str
    un: str
    obs: str
    quantidade: float
    valor_unitario: float
    total: float
    variation_product_id: str
    venda_item_id: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., codigo: _Optional[str] = ..., codigo_barra: _Optional[str] = ..., un: _Optional[str] = ..., obs: _Optional[str] = ..., quantidade: _Optional[float] = ..., valor_unitario: _Optional[float] = ..., total: _Optional[float] = ..., variation_product_id: _Optional[str] = ..., venda_item_id: _Optional[str] = ...) -> None: ...

class CreateDevolucaoRequest(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class CreateDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class UpdateDevolucaoRequest(_message.Message):
    __slots__ = ("id", "devolucao", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    devolucao: Devolucao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., devolucao: _Optional[_Union[Devolucao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class DeleteDevolucaoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteDevolucaoResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDevolucaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class ListDevolucaoRequest(_message.Message):
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

class ListDevolucaoResponse(_message.Message):
    __slots__ = ("devolucaoList", "next_page_token")
    DEVOLUCAOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    devolucaoList: _containers.RepeatedCompositeFieldContainer[Devolucao]
    next_page_token: str
    def __init__(self, devolucaoList: _Optional[_Iterable[_Union[Devolucao, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class FinalizaDevolucaoRequest(_message.Message):
    __slots__ = ("devolucao_id", "gerar_carta_credito")
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    GERAR_CARTA_CREDITO_FIELD_NUMBER: _ClassVar[int]
    devolucao_id: str
    gerar_carta_credito: bool
    def __init__(self, devolucao_id: _Optional[str] = ..., gerar_carta_credito: _Optional[bool] = ...) -> None: ...

class FinalizaDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class GeraNfeDevolucaoRequest(_message.Message):
    __slots__ = ("devolucao_id",)
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    devolucao_id: str
    def __init__(self, devolucao_id: _Optional[str] = ...) -> None: ...

class GeraNfeDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class GeraCartaCreditoRequest(_message.Message):
    __slots__ = ("devolucao_id",)
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    devolucao_id: str
    def __init__(self, devolucao_id: _Optional[str] = ...) -> None: ...

class GeraCartaCreditoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class CancelaDevolucaoRequest(_message.Message):
    __slots__ = ("devolucao_id", "motivo")
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    devolucao_id: str
    motivo: str
    def __init__(self, devolucao_id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class CancelaDevolucaoResponse(_message.Message):
    __slots__ = ("devolucao",)
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ...) -> None: ...

class GeraFromPedidoRequest(_message.Message):
    __slots__ = ("pedido_id", "itens")
    PEDIDO_ID_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    pedido_id: str
    itens: _containers.RepeatedCompositeFieldContainer[ItemDevolver]
    def __init__(self, pedido_id: _Optional[str] = ..., itens: _Optional[_Iterable[_Union[ItemDevolver, _Mapping]]] = ...) -> None: ...

class GeraFromPedidoResponse(_message.Message):
    __slots__ = ("devolucao", "ja_existia")
    DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    JA_EXISTIA_FIELD_NUMBER: _ClassVar[int]
    devolucao: Devolucao
    ja_existia: bool
    def __init__(self, devolucao: _Optional[_Union[Devolucao, _Mapping]] = ..., ja_existia: _Optional[bool] = ...) -> None: ...

class ItemDevolver(_message.Message):
    __slots__ = ("venda_item_id", "quantidade")
    VENDA_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    venda_item_id: str
    quantidade: float
    def __init__(self, venda_item_id: _Optional[str] = ..., quantidade: _Optional[float] = ...) -> None: ...

class ItensPedidoRequest(_message.Message):
    __slots__ = ("pedido_id",)
    PEDIDO_ID_FIELD_NUMBER: _ClassVar[int]
    pedido_id: str
    def __init__(self, pedido_id: _Optional[str] = ...) -> None: ...

class ItensPedidoResponse(_message.Message):
    __slots__ = ("itens", "pessoa", "chave_nfe_origem", "venda_numero", "devolucao_pendente_id", "devolucao_pendente_numero")
    ITENS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    CHAVE_NFE_ORIGEM_FIELD_NUMBER: _ClassVar[int]
    VENDA_NUMERO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_PENDENTE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_PENDENTE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    itens: _containers.RepeatedCompositeFieldContainer[ItemPedido]
    pessoa: Pessoa
    chave_nfe_origem: str
    venda_numero: str
    devolucao_pendente_id: str
    devolucao_pendente_numero: int
    def __init__(self, itens: _Optional[_Iterable[_Union[ItemPedido, _Mapping]]] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., chave_nfe_origem: _Optional[str] = ..., venda_numero: _Optional[str] = ..., devolucao_pendente_id: _Optional[str] = ..., devolucao_pendente_numero: _Optional[int] = ...) -> None: ...

class ItemPedido(_message.Message):
    __slots__ = ("venda_item_id", "produto_id", "variation_product_id", "produto_nome", "codigo", "un", "valor_unitario", "quantidade_vendida", "quantidade_devolvida", "quantidade_disponivel")
    VENDA_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_VENDIDA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_DEVOLVIDA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_DISPONIVEL_FIELD_NUMBER: _ClassVar[int]
    venda_item_id: str
    produto_id: str
    variation_product_id: str
    produto_nome: str
    codigo: str
    un: str
    valor_unitario: float
    quantidade_vendida: float
    quantidade_devolvida: float
    quantidade_disponivel: float
    def __init__(self, venda_item_id: _Optional[str] = ..., produto_id: _Optional[str] = ..., variation_product_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., quantidade_vendida: _Optional[float] = ..., quantidade_devolvida: _Optional[float] = ..., quantidade_disponivel: _Optional[float] = ...) -> None: ...
