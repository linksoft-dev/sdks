from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cfop(_message.Message):
    __slots__ = ("id", "codigo", "descricao", "aplicacao", "categoria", "tipo_operacao", "fora_do_estado", "operacao_com_exterior", "valido_nfe", "valido_nfce", "valido_cte", "valido_cte_os", "valido_servico_comunicacao", "valido_retencao_icms_transporte", "valido_devolucao", "valido_retorno_mercadoria", "valido_transferencia", "valido_venda", "valido_anulacao", "valido_remessa", "valido_operacao_combustivel")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    APLICACAO_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    FORA_DO_ESTADO_FIELD_NUMBER: _ClassVar[int]
    OPERACAO_COM_EXTERIOR_FIELD_NUMBER: _ClassVar[int]
    VALIDO_NFE_FIELD_NUMBER: _ClassVar[int]
    VALIDO_NFCE_FIELD_NUMBER: _ClassVar[int]
    VALIDO_CTE_FIELD_NUMBER: _ClassVar[int]
    VALIDO_CTE_OS_FIELD_NUMBER: _ClassVar[int]
    VALIDO_SERVICO_COMUNICACAO_FIELD_NUMBER: _ClassVar[int]
    VALIDO_RETENCAO_ICMS_TRANSPORTE_FIELD_NUMBER: _ClassVar[int]
    VALIDO_DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    VALIDO_RETORNO_MERCADORIA_FIELD_NUMBER: _ClassVar[int]
    VALIDO_TRANSFERENCIA_FIELD_NUMBER: _ClassVar[int]
    VALIDO_VENDA_FIELD_NUMBER: _ClassVar[int]
    VALIDO_ANULACAO_FIELD_NUMBER: _ClassVar[int]
    VALIDO_REMESSA_FIELD_NUMBER: _ClassVar[int]
    VALIDO_OPERACAO_COMBUSTIVEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo: str
    descricao: str
    aplicacao: str
    categoria: str
    tipo_operacao: str
    fora_do_estado: bool
    operacao_com_exterior: bool
    valido_nfe: bool
    valido_nfce: bool
    valido_cte: bool
    valido_cte_os: bool
    valido_servico_comunicacao: bool
    valido_retencao_icms_transporte: bool
    valido_devolucao: bool
    valido_retorno_mercadoria: bool
    valido_transferencia: bool
    valido_venda: bool
    valido_anulacao: bool
    valido_remessa: bool
    valido_operacao_combustivel: bool
    def __init__(self, id: _Optional[str] = ..., codigo: _Optional[str] = ..., descricao: _Optional[str] = ..., aplicacao: _Optional[str] = ..., categoria: _Optional[str] = ..., tipo_operacao: _Optional[str] = ..., fora_do_estado: _Optional[bool] = ..., operacao_com_exterior: _Optional[bool] = ..., valido_nfe: _Optional[bool] = ..., valido_nfce: _Optional[bool] = ..., valido_cte: _Optional[bool] = ..., valido_cte_os: _Optional[bool] = ..., valido_servico_comunicacao: _Optional[bool] = ..., valido_retencao_icms_transporte: _Optional[bool] = ..., valido_devolucao: _Optional[bool] = ..., valido_retorno_mercadoria: _Optional[bool] = ..., valido_transferencia: _Optional[bool] = ..., valido_venda: _Optional[bool] = ..., valido_anulacao: _Optional[bool] = ..., valido_remessa: _Optional[bool] = ..., valido_operacao_combustivel: _Optional[bool] = ...) -> None: ...

class CreateCfopRequest(_message.Message):
    __slots__ = ("cfop",)
    CFOP_FIELD_NUMBER: _ClassVar[int]
    cfop: Cfop
    def __init__(self, cfop: _Optional[_Union[Cfop, _Mapping]] = ...) -> None: ...

class CreateCfopResponse(_message.Message):
    __slots__ = ("cfop",)
    CFOP_FIELD_NUMBER: _ClassVar[int]
    cfop: Cfop
    def __init__(self, cfop: _Optional[_Union[Cfop, _Mapping]] = ...) -> None: ...

class UpdateCfopRequest(_message.Message):
    __slots__ = ("id", "cfop", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CFOP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    cfop: Cfop
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., cfop: _Optional[_Union[Cfop, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCfopResponse(_message.Message):
    __slots__ = ("cfop",)
    CFOP_FIELD_NUMBER: _ClassVar[int]
    cfop: Cfop
    def __init__(self, cfop: _Optional[_Union[Cfop, _Mapping]] = ...) -> None: ...

class DeleteCfopRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCfopResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCfopRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCfopResponse(_message.Message):
    __slots__ = ("cfop",)
    CFOP_FIELD_NUMBER: _ClassVar[int]
    cfop: Cfop
    def __init__(self, cfop: _Optional[_Union[Cfop, _Mapping]] = ...) -> None: ...

class ListCfopRequest(_message.Message):
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

class ListCfopResponse(_message.Message):
    __slots__ = ("cfopList", "next_page_token")
    CFOPLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cfopList: _containers.RepeatedCompositeFieldContainer[Cfop]
    next_page_token: str
    def __init__(self, cfopList: _Optional[_Iterable[_Union[Cfop, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class FindByOperacaoRequest(_message.Message):
    __slots__ = ("tipo_operacao", "tipo_documento", "natureza_operacao", "fora_estado")
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    FORA_ESTADO_FIELD_NUMBER: _ClassVar[int]
    tipo_operacao: str
    tipo_documento: str
    natureza_operacao: str
    fora_estado: bool
    def __init__(self, tipo_operacao: _Optional[str] = ..., tipo_documento: _Optional[str] = ..., natureza_operacao: _Optional[str] = ..., fora_estado: _Optional[bool] = ...) -> None: ...

class FindByOperacaoResponse(_message.Message):
    __slots__ = ("cfop_list",)
    class CfopValido(_message.Message):
        __slots__ = ("codigo", "descricao")
        CODIGO_FIELD_NUMBER: _ClassVar[int]
        DESCRICAO_FIELD_NUMBER: _ClassVar[int]
        codigo: str
        descricao: str
        def __init__(self, codigo: _Optional[str] = ..., descricao: _Optional[str] = ...) -> None: ...
    CFOP_LIST_FIELD_NUMBER: _ClassVar[int]
    cfop_list: _containers.RepeatedCompositeFieldContainer[FindByOperacaoResponse.CfopValido]
    def __init__(self, cfop_list: _Optional[_Iterable[_Union[FindByOperacaoResponse.CfopValido, _Mapping]]] = ...) -> None: ...

class ImportaTabelaRequest(_message.Message):
    __slots__ = ("file_string",)
    FILE_STRING_FIELD_NUMBER: _ClassVar[int]
    file_string: str
    def __init__(self, file_string: _Optional[str] = ...) -> None: ...

class ImportaTabelaResponse(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...
