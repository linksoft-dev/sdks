import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.imports import imports_pb2 as _imports_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServicoMediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICO_MEDIA_TYPE_UNSPECIFIED: _ClassVar[ServicoMediaType]
    SERVICO_MEDIA_TYPE_IMAGE: _ClassVar[ServicoMediaType]
    SERVICO_MEDIA_TYPE_VIDEO: _ClassVar[ServicoMediaType]
SERVICO_MEDIA_TYPE_UNSPECIFIED: ServicoMediaType
SERVICO_MEDIA_TYPE_IMAGE: ServicoMediaType
SERVICO_MEDIA_TYPE_VIDEO: ServicoMediaType

class Servico(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "nome", "codigo", "dias_validade", "dias_garantia", "un", "valor_unitario", "promocao", "ecommerce", "module", "tributacao", "composicao", "composto", "situacao", "fields", "categoria_id", "categoria_nome", "especialidade_id", "especialidade_nome")
    class Ecommerce(_message.Message):
        __slots__ = ("slug", "available_online", "featured", "short_description", "full_description", "tags", "meta_title", "meta_description", "display_order", "video_url", "estimated_duration_minutes", "requires_scheduling", "primary_media", "media")
        SLUG_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_ONLINE_FIELD_NUMBER: _ClassVar[int]
        FEATURED_FIELD_NUMBER: _ClassVar[int]
        SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FULL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        META_TITLE_FIELD_NUMBER: _ClassVar[int]
        META_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
        VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_DURATION_MINUTES_FIELD_NUMBER: _ClassVar[int]
        REQUIRES_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_MEDIA_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        slug: str
        available_online: bool
        featured: bool
        short_description: str
        full_description: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        meta_title: str
        meta_description: str
        display_order: int
        video_url: str
        estimated_duration_minutes: int
        requires_scheduling: bool
        primary_media: ServicoMedia
        media: _containers.RepeatedCompositeFieldContainer[ServicoMedia]
        def __init__(self, slug: _Optional[str] = ..., available_online: _Optional[bool] = ..., featured: _Optional[bool] = ..., short_description: _Optional[str] = ..., full_description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., meta_title: _Optional[str] = ..., meta_description: _Optional[str] = ..., display_order: _Optional[int] = ..., video_url: _Optional[str] = ..., estimated_duration_minutes: _Optional[int] = ..., requires_scheduling: _Optional[bool] = ..., primary_media: _Optional[_Union[ServicoMedia, _Mapping]] = ..., media: _Optional[_Iterable[_Union[ServicoMedia, _Mapping]]] = ...) -> None: ...
    class Tributacao(_message.Message):
        __slots__ = ("tributacao_id", "tributacao_nome", "codigo_servico_id", "codigo_servico_codigo", "codigo_servico_nome", "cnae_codigo")
        TRIBUTACAO_ID_FIELD_NUMBER: _ClassVar[int]
        TRIBUTACAO_NOME_FIELD_NUMBER: _ClassVar[int]
        CODIGO_SERVICO_ID_FIELD_NUMBER: _ClassVar[int]
        CODIGO_SERVICO_CODIGO_FIELD_NUMBER: _ClassVar[int]
        CODIGO_SERVICO_NOME_FIELD_NUMBER: _ClassVar[int]
        CNAE_CODIGO_FIELD_NUMBER: _ClassVar[int]
        tributacao_id: str
        tributacao_nome: str
        codigo_servico_id: str
        codigo_servico_codigo: str
        codigo_servico_nome: str
        cnae_codigo: str
        def __init__(self, tributacao_id: _Optional[str] = ..., tributacao_nome: _Optional[str] = ..., codigo_servico_id: _Optional[str] = ..., codigo_servico_codigo: _Optional[str] = ..., codigo_servico_nome: _Optional[str] = ..., cnae_codigo: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DIAS_VALIDADE_FIELD_NUMBER: _ClassVar[int]
    DIAS_GARANTIA_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    PROMOCAO_FIELD_NUMBER: _ClassVar[int]
    ECOMMERCE_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    COMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    COMPOSTO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_NOME_FIELD_NUMBER: _ClassVar[int]
    ESPECIALIDADE_ID_FIELD_NUMBER: _ClassVar[int]
    ESPECIALIDADE_NOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    nome: str
    codigo: str
    dias_validade: int
    dias_garantia: int
    un: str
    valor_unitario: float
    promocao: str
    ecommerce: Servico.Ecommerce
    module: Module
    tributacao: Servico.Tributacao
    composicao: _containers.RepeatedCompositeFieldContainer[Composicao]
    composto: bool
    situacao: str
    fields: _metadata_pb2.BasicFields
    categoria_id: str
    categoria_nome: str
    especialidade_id: str
    especialidade_nome: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., nome: _Optional[str] = ..., codigo: _Optional[str] = ..., dias_validade: _Optional[int] = ..., dias_garantia: _Optional[int] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., promocao: _Optional[str] = ..., ecommerce: _Optional[_Union[Servico.Ecommerce, _Mapping]] = ..., module: _Optional[_Union[Module, _Mapping]] = ..., tributacao: _Optional[_Union[Servico.Tributacao, _Mapping]] = ..., composicao: _Optional[_Iterable[_Union[Composicao, _Mapping]]] = ..., composto: _Optional[bool] = ..., situacao: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., categoria_id: _Optional[str] = ..., categoria_nome: _Optional[str] = ..., especialidade_id: _Optional[str] = ..., especialidade_nome: _Optional[str] = ...) -> None: ...

class Composicao(_message.Message):
    __slots__ = ("id", "item_id", "tipo", "nome", "quantidade", "un", "valor_unitario", "total", "codigo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    id: str
    item_id: str
    tipo: str
    nome: str
    quantidade: float
    un: str
    valor_unitario: float
    total: float
    codigo: str
    def __init__(self, id: _Optional[str] = ..., item_id: _Optional[str] = ..., tipo: _Optional[str] = ..., nome: _Optional[str] = ..., quantidade: _Optional[float] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., total: _Optional[float] = ..., codigo: _Optional[str] = ...) -> None: ...

class ServicoMedia(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "media_type", "url", "file_id", "display_name", "file_extension")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    media_type: ServicoMediaType
    url: str
    file_id: str
    display_name: str
    file_extension: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., media_type: _Optional[_Union[ServicoMediaType, str]] = ..., url: _Optional[str] = ..., file_id: _Optional[str] = ..., display_name: _Optional[str] = ..., file_extension: _Optional[str] = ...) -> None: ...

class CreateServicoRequest(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class CreateServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class UpdateServicoRequest(_message.Message):
    __slots__ = ("id", "servico", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    servico: Servico
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., servico: _Optional[_Union[Servico, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class DeleteServicoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteServicoResponse(_message.Message):
    __slots__ = ("id", "avisos")
    ID_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class GetServicoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class ListServicoRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "servico", "filter", "ignore_situacao_padrao")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SITUACAO_PADRAO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    servico: _containers.RepeatedCompositeFieldContainer[Servico]
    filter: _filter_pb2.Filter
    ignore_situacao_padrao: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., servico: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., ignore_situacao_padrao: _Optional[bool] = ...) -> None: ...

class ListServicoResponse(_message.Message):
    __slots__ = ("servico_list", "next_page_token")
    SERVICO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    servico_list: _containers.RepeatedCompositeFieldContainer[Servico]
    next_page_token: str
    def __init__(self, servico_list: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Module(_message.Message):
    __slots__ = ("route", "icon", "category", "category_icon", "title")
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ICON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    route: str
    icon: str
    category: str
    category_icon: str
    title: str
    def __init__(self, route: _Optional[str] = ..., icon: _Optional[str] = ..., category: _Optional[str] = ..., category_icon: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class ImportServicoRequest(_message.Message):
    __slots__ = ("validate_only", "update_if_exists", "servicos")
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    SERVICOS_FIELD_NUMBER: _ClassVar[int]
    validate_only: bool
    update_if_exists: bool
    servicos: _containers.RepeatedCompositeFieldContainer[Servico]
    def __init__(self, validate_only: _Optional[bool] = ..., update_if_exists: _Optional[bool] = ..., servicos: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ...) -> None: ...

class ImportServicoResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: _imports_pb2.ImportResponse
    def __init__(self, report: _Optional[_Union[_imports_pb2.ImportResponse, _Mapping]] = ...) -> None: ...

class SincronizarModulosRequest(_message.Message):
    __slots__ = ("atualizar_precos",)
    ATUALIZAR_PRECOS_FIELD_NUMBER: _ClassVar[int]
    atualizar_precos: bool
    def __init__(self, atualizar_precos: _Optional[bool] = ...) -> None: ...

class SincronizarModulosResponse(_message.Message):
    __slots__ = ("all_modules",)
    ALL_MODULES_FIELD_NUMBER: _ClassVar[int]
    all_modules: _containers.RepeatedCompositeFieldContainer[Module]
    def __init__(self, all_modules: _Optional[_Iterable[_Union[Module, _Mapping]]] = ...) -> None: ...

class AlteracaoCadastroServico(_message.Message):
    __slots__ = ("id", "nome", "codigo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    codigo: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., codigo: _Optional[str] = ...) -> None: ...

class AlteracoesFiltroServico(_message.Message):
    __slots__ = ("ids", "nome", "codigo")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    nome: str
    codigo: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., nome: _Optional[str] = ..., codigo: _Optional[str] = ...) -> None: ...

class AlteracoesConjuntasServicoRequest(_message.Message):
    __slots__ = ("filtro", "tributacao", "codigo_servico", "cnae_codigo")
    FILTRO_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_SERVICO_FIELD_NUMBER: _ClassVar[int]
    CNAE_CODIGO_FIELD_NUMBER: _ClassVar[int]
    filtro: AlteracoesFiltroServico
    tributacao: AlteracaoCadastroServico
    codigo_servico: AlteracaoCadastroServico
    cnae_codigo: str
    def __init__(self, filtro: _Optional[_Union[AlteracoesFiltroServico, _Mapping]] = ..., tributacao: _Optional[_Union[AlteracaoCadastroServico, _Mapping]] = ..., codigo_servico: _Optional[_Union[AlteracaoCadastroServico, _Mapping]] = ..., cnae_codigo: _Optional[str] = ...) -> None: ...

class AlteracoesConjuntasServicoResponse(_message.Message):
    __slots__ = ("quantidade_alterada", "status")
    QUANTIDADE_ALTERADA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    quantidade_alterada: int
    status: str
    def __init__(self, quantidade_alterada: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipoRelatorio", "listServicoRequest")
    TIPORELATORIO_FIELD_NUMBER: _ClassVar[int]
    LISTSERVICOREQUEST_FIELD_NUMBER: _ClassVar[int]
    tipoRelatorio: str
    listServicoRequest: ListServicoRequest
    def __init__(self, tipoRelatorio: _Optional[str] = ..., listServicoRequest: _Optional[_Union[ListServicoRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class CloneServicoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneServicoResponse(_message.Message):
    __slots__ = ("servico",)
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...
