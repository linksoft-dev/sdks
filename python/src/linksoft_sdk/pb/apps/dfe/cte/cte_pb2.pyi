import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ambiente(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AMBIENTE_UNSPECIFIED: _ClassVar[Ambiente]
    AMBIENTE_HOMOLOGACAO: _ClassVar[Ambiente]
    AMBIENTE_PRODUCAO: _ClassVar[Ambiente]

class SituacaoCte(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[SituacaoCte]
    SITUACAO_DIGITADO: _ClassVar[SituacaoCte]
    SITUACAO_AUTORIZADO: _ClassVar[SituacaoCte]
    SITUACAO_REJEITADO: _ClassVar[SituacaoCte]
    SITUACAO_CANCELADO: _ClassVar[SituacaoCte]
    SITUACAO_DENEGADO: _ClassVar[SituacaoCte]

class TipoCte(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_CTE_UNSPECIFIED: _ClassVar[TipoCte]
    TIPO_CTE_NORMAL: _ClassVar[TipoCte]
    TIPO_CTE_COMPLEMENTAR: _ClassVar[TipoCte]
    TIPO_CTE_ANULACAO: _ClassVar[TipoCte]
    TIPO_CTE_SUBSTITUICAO: _ClassVar[TipoCte]

class TipoServicoCte(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_SERVICO_UNSPECIFIED: _ClassVar[TipoServicoCte]
    TIPO_SERVICO_NORMAL: _ClassVar[TipoServicoCte]
    TIPO_SERVICO_SUBCONTRATACAO: _ClassVar[TipoServicoCte]
    TIPO_SERVICO_REDESPACHO: _ClassVar[TipoServicoCte]
    TIPO_SERVICO_REDESPACHO_INTERMEDIARIO: _ClassVar[TipoServicoCte]
    TIPO_SERVICO_MULTIMODAL: _ClassVar[TipoServicoCte]

class TomadorServico(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOMADOR_SERVICO_UNSPECIFIED: _ClassVar[TomadorServico]
    TOMADOR_SERVICO_REMETENTE: _ClassVar[TomadorServico]
    TOMADOR_SERVICO_EXPEDIDOR: _ClassVar[TomadorServico]
    TOMADOR_SERVICO_RECEBEDOR: _ClassVar[TomadorServico]
    TOMADOR_SERVICO_DESTINATARIO: _ClassVar[TomadorServico]
    TOMADOR_SERVICO_OUTROS: _ClassVar[TomadorServico]

class ModalCte(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODAL_CTE_UNSPECIFIED: _ClassVar[ModalCte]
    MODAL_CTE_RODOVIARIO: _ClassVar[ModalCte]
    MODAL_CTE_AEREO: _ClassVar[ModalCte]
    MODAL_CTE_AQUAVIARIO: _ClassVar[ModalCte]
    MODAL_CTE_FERROVIARIO: _ClassVar[ModalCte]
    MODAL_CTE_DUTOVIARIO: _ClassVar[ModalCte]
    MODAL_CTE_MULTIMODAL: _ClassVar[ModalCte]

class TipoComponenteVprest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_COMPONENTE_UNSPECIFIED: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_FRETE_PESO: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_FRETE_VALOR: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_PEDAGIO: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_GRIS: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_SEGURO: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_DESPACHO: _ClassVar[TipoComponenteVprest]
    TIPO_COMPONENTE_OUTROS: _ClassVar[TipoComponenteVprest]
AMBIENTE_UNSPECIFIED: Ambiente
AMBIENTE_HOMOLOGACAO: Ambiente
AMBIENTE_PRODUCAO: Ambiente
SITUACAO_UNSPECIFIED: SituacaoCte
SITUACAO_DIGITADO: SituacaoCte
SITUACAO_AUTORIZADO: SituacaoCte
SITUACAO_REJEITADO: SituacaoCte
SITUACAO_CANCELADO: SituacaoCte
SITUACAO_DENEGADO: SituacaoCte
TIPO_CTE_UNSPECIFIED: TipoCte
TIPO_CTE_NORMAL: TipoCte
TIPO_CTE_COMPLEMENTAR: TipoCte
TIPO_CTE_ANULACAO: TipoCte
TIPO_CTE_SUBSTITUICAO: TipoCte
TIPO_SERVICO_UNSPECIFIED: TipoServicoCte
TIPO_SERVICO_NORMAL: TipoServicoCte
TIPO_SERVICO_SUBCONTRATACAO: TipoServicoCte
TIPO_SERVICO_REDESPACHO: TipoServicoCte
TIPO_SERVICO_REDESPACHO_INTERMEDIARIO: TipoServicoCte
TIPO_SERVICO_MULTIMODAL: TipoServicoCte
TOMADOR_SERVICO_UNSPECIFIED: TomadorServico
TOMADOR_SERVICO_REMETENTE: TomadorServico
TOMADOR_SERVICO_EXPEDIDOR: TomadorServico
TOMADOR_SERVICO_RECEBEDOR: TomadorServico
TOMADOR_SERVICO_DESTINATARIO: TomadorServico
TOMADOR_SERVICO_OUTROS: TomadorServico
MODAL_CTE_UNSPECIFIED: ModalCte
MODAL_CTE_RODOVIARIO: ModalCte
MODAL_CTE_AEREO: ModalCte
MODAL_CTE_AQUAVIARIO: ModalCte
MODAL_CTE_FERROVIARIO: ModalCte
MODAL_CTE_DUTOVIARIO: ModalCte
MODAL_CTE_MULTIMODAL: ModalCte
TIPO_COMPONENTE_UNSPECIFIED: TipoComponenteVprest
TIPO_COMPONENTE_FRETE_PESO: TipoComponenteVprest
TIPO_COMPONENTE_FRETE_VALOR: TipoComponenteVprest
TIPO_COMPONENTE_PEDAGIO: TipoComponenteVprest
TIPO_COMPONENTE_GRIS: TipoComponenteVprest
TIPO_COMPONENTE_SEGURO: TipoComponenteVprest
TIPO_COMPONENTE_DESPACHO: TipoComponenteVprest
TIPO_COMPONENTE_OUTROS: TipoComponenteVprest

class Cte(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "account_id", "ambiente", "serie", "numero", "chave", "protocolo", "situacao", "valor_prestacao", "xml", "data_emissao", "operacao", "cfop", "natureza_operacao", "tipo_cte", "tipo_servico", "modal", "cte_globalizado", "municipio_inicio_codigo", "municipio_inicio_nome", "uf_inicio", "municipio_fim_codigo", "municipio_fim_nome", "uf_fim", "valor_receber", "valor_pedagio", "valor_tributos", "produto_predominante", "produto_predominante_id", "valor_carga", "peso_total", "quantidade_carga", "observacao", "data_hora_autorizacao", "xml_autorizacao", "tomador", "remetente", "destinatario", "rejeicoes", "expedidor", "recebedor", "cancelamento", "documentos_referenciados", "rntrc", "icms_cst", "icms_v_bc", "icms_p_icms", "icms_v_icms", "icms_p_red_bc", "componentes_prestacao")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_PRESTACAO_FIELD_NUMBER: _ClassVar[int]
    XML_FIELD_NUMBER: _ClassVar[int]
    DATA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    OPERACAO_FIELD_NUMBER: _ClassVar[int]
    CFOP_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_CTE_FIELD_NUMBER: _ClassVar[int]
    TIPO_SERVICO_FIELD_NUMBER: _ClassVar[int]
    MODAL_FIELD_NUMBER: _ClassVar[int]
    CTE_GLOBALIZADO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_INICIO_CODIGO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_INICIO_NOME_FIELD_NUMBER: _ClassVar[int]
    UF_INICIO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_FIM_CODIGO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_FIM_NOME_FIELD_NUMBER: _ClassVar[int]
    UF_FIM_FIELD_NUMBER: _ClassVar[int]
    VALOR_RECEBER_FIELD_NUMBER: _ClassVar[int]
    VALOR_PEDAGIO_FIELD_NUMBER: _ClassVar[int]
    VALOR_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_PREDOMINANTE_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_PREDOMINANTE_ID_FIELD_NUMBER: _ClassVar[int]
    VALOR_CARGA_FIELD_NUMBER: _ClassVar[int]
    PESO_TOTAL_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_CARGA_FIELD_NUMBER: _ClassVar[int]
    OBSERVACAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    XML_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    TOMADOR_FIELD_NUMBER: _ClassVar[int]
    REMETENTE_FIELD_NUMBER: _ClassVar[int]
    DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    EXPEDIDOR_FIELD_NUMBER: _ClassVar[int]
    RECEBEDOR_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTOS_REFERENCIADOS_FIELD_NUMBER: _ClassVar[int]
    RNTRC_FIELD_NUMBER: _ClassVar[int]
    ICMS_CST_FIELD_NUMBER: _ClassVar[int]
    ICMS_V_BC_FIELD_NUMBER: _ClassVar[int]
    ICMS_P_ICMS_FIELD_NUMBER: _ClassVar[int]
    ICMS_V_ICMS_FIELD_NUMBER: _ClassVar[int]
    ICMS_P_RED_BC_FIELD_NUMBER: _ClassVar[int]
    COMPONENTES_PRESTACAO_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    account_id: str
    ambiente: Ambiente
    serie: int
    numero: int
    chave: str
    protocolo: str
    situacao: SituacaoCte
    valor_prestacao: float
    xml: str
    data_emissao: _timestamp_pb2.Timestamp
    operacao: str
    cfop: str
    natureza_operacao: str
    tipo_cte: TipoCte
    tipo_servico: TipoServicoCte
    modal: ModalCte
    cte_globalizado: bool
    municipio_inicio_codigo: int
    municipio_inicio_nome: str
    uf_inicio: str
    municipio_fim_codigo: int
    municipio_fim_nome: str
    uf_fim: str
    valor_receber: float
    valor_pedagio: float
    valor_tributos: float
    produto_predominante: str
    produto_predominante_id: str
    valor_carga: float
    peso_total: float
    quantidade_carga: float
    observacao: str
    data_hora_autorizacao: _timestamp_pb2.Timestamp
    xml_autorizacao: str
    tomador: Tomador
    remetente: Parte
    destinatario: Parte
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Rejeicao]
    expedidor: Parte
    recebedor: Parte
    cancelamento: Cancelamento
    documentos_referenciados: _containers.RepeatedCompositeFieldContainer[DocReferenciado]
    rntrc: str
    icms_cst: str
    icms_v_bc: float
    icms_p_icms: float
    icms_v_icms: float
    icms_p_red_bc: float
    componentes_prestacao: _containers.RepeatedCompositeFieldContainer[ComponenteVprest]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., account_id: _Optional[str] = ..., ambiente: _Optional[_Union[Ambiente, str]] = ..., serie: _Optional[int] = ..., numero: _Optional[int] = ..., chave: _Optional[str] = ..., protocolo: _Optional[str] = ..., situacao: _Optional[_Union[SituacaoCte, str]] = ..., valor_prestacao: _Optional[float] = ..., xml: _Optional[str] = ..., data_emissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., operacao: _Optional[str] = ..., cfop: _Optional[str] = ..., natureza_operacao: _Optional[str] = ..., tipo_cte: _Optional[_Union[TipoCte, str]] = ..., tipo_servico: _Optional[_Union[TipoServicoCte, str]] = ..., modal: _Optional[_Union[ModalCte, str]] = ..., cte_globalizado: _Optional[bool] = ..., municipio_inicio_codigo: _Optional[int] = ..., municipio_inicio_nome: _Optional[str] = ..., uf_inicio: _Optional[str] = ..., municipio_fim_codigo: _Optional[int] = ..., municipio_fim_nome: _Optional[str] = ..., uf_fim: _Optional[str] = ..., valor_receber: _Optional[float] = ..., valor_pedagio: _Optional[float] = ..., valor_tributos: _Optional[float] = ..., produto_predominante: _Optional[str] = ..., produto_predominante_id: _Optional[str] = ..., valor_carga: _Optional[float] = ..., peso_total: _Optional[float] = ..., quantidade_carga: _Optional[float] = ..., observacao: _Optional[str] = ..., data_hora_autorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., xml_autorizacao: _Optional[str] = ..., tomador: _Optional[_Union[Tomador, _Mapping]] = ..., remetente: _Optional[_Union[Parte, _Mapping]] = ..., destinatario: _Optional[_Union[Parte, _Mapping]] = ..., rejeicoes: _Optional[_Iterable[_Union[Rejeicao, _Mapping]]] = ..., expedidor: _Optional[_Union[Parte, _Mapping]] = ..., recebedor: _Optional[_Union[Parte, _Mapping]] = ..., cancelamento: _Optional[_Union[Cancelamento, _Mapping]] = ..., documentos_referenciados: _Optional[_Iterable[_Union[DocReferenciado, _Mapping]]] = ..., rntrc: _Optional[str] = ..., icms_cst: _Optional[str] = ..., icms_v_bc: _Optional[float] = ..., icms_p_icms: _Optional[float] = ..., icms_v_icms: _Optional[float] = ..., icms_p_red_bc: _Optional[float] = ..., componentes_prestacao: _Optional[_Iterable[_Union[ComponenteVprest, _Mapping]]] = ...) -> None: ...

class ComponenteVprest(_message.Message):
    __slots__ = ("id", "tipo", "nome", "valor")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: TipoComponenteVprest
    nome: str
    valor: float
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[_Union[TipoComponenteVprest, str]] = ..., nome: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class DocReferenciado(_message.Message):
    __slots__ = ("chave", "modelo", "id")
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    chave: str
    modelo: str
    id: str
    def __init__(self, chave: _Optional[str] = ..., modelo: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class Parte(_message.Message):
    __slots__ = ("documento", "nome", "ie", "fone", "email", "endereco", "numero", "complemento", "bairro", "cidade", "cidade_codigo", "uf", "cep", "id")
    DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    FONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ENDERECO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
    BAIRRO_FIELD_NUMBER: _ClassVar[int]
    CIDADE_FIELD_NUMBER: _ClassVar[int]
    CIDADE_CODIGO_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    CEP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    documento: str
    nome: str
    ie: str
    fone: str
    email: str
    endereco: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    cidade_codigo: int
    uf: str
    cep: str
    id: str
    def __init__(self, documento: _Optional[str] = ..., nome: _Optional[str] = ..., ie: _Optional[str] = ..., fone: _Optional[str] = ..., email: _Optional[str] = ..., endereco: _Optional[str] = ..., numero: _Optional[str] = ..., complemento: _Optional[str] = ..., bairro: _Optional[str] = ..., cidade: _Optional[str] = ..., cidade_codigo: _Optional[int] = ..., uf: _Optional[str] = ..., cep: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class Tomador(_message.Message):
    __slots__ = ("servico", "documento", "nome", "ie", "id")
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    servico: TomadorServico
    documento: str
    nome: str
    ie: str
    id: str
    def __init__(self, servico: _Optional[_Union[TomadorServico, str]] = ..., documento: _Optional[str] = ..., nome: _Optional[str] = ..., ie: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class Cancelamento(_message.Message):
    __slots__ = ("protocolo", "motivo", "data_hora", "xml")
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    XML_FIELD_NUMBER: _ClassVar[int]
    protocolo: str
    motivo: str
    data_hora: _timestamp_pb2.Timestamp
    xml: str
    def __init__(self, protocolo: _Optional[str] = ..., motivo: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., xml: _Optional[str] = ...) -> None: ...

class Rejeicao(_message.Message):
    __slots__ = ("id", "data_hora", "data_hora_situacao_doc", "cstat", "mensagem")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_SITUACAO_DOC_FIELD_NUMBER: _ClassVar[int]
    CSTAT_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    data_hora: _timestamp_pb2.Timestamp
    data_hora_situacao_doc: _timestamp_pb2.Timestamp
    cstat: str
    mensagem: str
    def __init__(self, id: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_situacao_doc: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cstat: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class CreateCteRequest(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class CreateCteResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class UpdateCteRequest(_message.Message):
    __slots__ = ("id", "cte", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    cte: Cte
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., cte: _Optional[_Union[Cte, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCteResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class DeleteCteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCteResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class GetCteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCteResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class ListCteRequest(_message.Message):
    __slots__ = ("ids", "main", "situacao", "created_at_gte", "created_at_lte", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    main: str
    situacao: _containers.RepeatedScalarFieldContainer[str]
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., main: _Optional[str] = ..., situacao: _Optional[_Iterable[str]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListCteResponse(_message.Message):
    __slots__ = ("cte_list", "total")
    CTE_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    cte_list: _containers.RepeatedCompositeFieldContainer[Cte]
    total: int
    def __init__(self, cte_list: _Optional[_Iterable[_Union[Cte, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class EmitirCteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmitirCteResponse(_message.Message):
    __slots__ = ("cte", "mensagem")
    CTE_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    mensagem: str
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class CancelarCteRequest(_message.Message):
    __slots__ = ("id", "motivo")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo: str
    def __init__(self, id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class CancelarCteResponse(_message.Message):
    __slots__ = ("cte", "mensagem")
    CTE_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    mensagem: str
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class CorrigirCteRequest(_message.Message):
    __slots__ = ("id", "correcao")
    ID_FIELD_NUMBER: _ClassVar[int]
    CORRECAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    correcao: str
    def __init__(self, id: _Optional[str] = ..., correcao: _Optional[str] = ...) -> None: ...

class CorrigirCteResponse(_message.Message):
    __slots__ = ("cte", "mensagem")
    CTE_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    mensagem: str
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ConsultaProtocoloRequest(_message.Message):
    __slots__ = ("id", "chave")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    chave: str
    def __init__(self, id: _Optional[str] = ..., chave: _Optional[str] = ...) -> None: ...

class ConsultaProtocoloResponse(_message.Message):
    __slots__ = ("protocolo", "situacao", "mensagem")
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    protocolo: str
    situacao: str
    mensagem: str
    def __init__(self, protocolo: _Optional[str] = ..., situacao: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class GetWsStatusRequest(_message.Message):
    __slots__ = ("uf", "ambiente")
    UF_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    uf: str
    ambiente: str
    def __init__(self, uf: _Optional[str] = ..., ambiente: _Optional[str] = ...) -> None: ...

class GetWsStatusResponse(_message.Message):
    __slots__ = ("status", "mensagem")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    status: str
    mensagem: str
    def __init__(self, status: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ImprimirCteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimirCteResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ImportarXmlRequest(_message.Message):
    __slots__ = ("xml",)
    XML_FIELD_NUMBER: _ClassVar[int]
    xml: str
    def __init__(self, xml: _Optional[str] = ...) -> None: ...

class ImportarXmlResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class AddDocumentoReferenciadoRequest(_message.Message):
    __slots__ = ("cte_id", "documento")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    documento: DocReferenciado
    def __init__(self, cte_id: _Optional[str] = ..., documento: _Optional[_Union[DocReferenciado, _Mapping]] = ...) -> None: ...

class AddDocumentoReferenciadoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class UpdateDocumentoReferenciadoRequest(_message.Message):
    __slots__ = ("cte_id", "id", "documento")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    id: str
    documento: DocReferenciado
    def __init__(self, cte_id: _Optional[str] = ..., id: _Optional[str] = ..., documento: _Optional[_Union[DocReferenciado, _Mapping]] = ...) -> None: ...

class UpdateDocumentoReferenciadoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class DeleteDocumentoReferenciadoRequest(_message.Message):
    __slots__ = ("cte_id", "id")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    id: str
    def __init__(self, cte_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteDocumentoReferenciadoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class AddComponentePrestacaoRequest(_message.Message):
    __slots__ = ("cte_id", "componente")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENTE_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    componente: ComponenteVprest
    def __init__(self, cte_id: _Optional[str] = ..., componente: _Optional[_Union[ComponenteVprest, _Mapping]] = ...) -> None: ...

class AddComponentePrestacaoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class UpdateComponentePrestacaoRequest(_message.Message):
    __slots__ = ("cte_id", "id", "componente")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENTE_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    id: str
    componente: ComponenteVprest
    def __init__(self, cte_id: _Optional[str] = ..., id: _Optional[str] = ..., componente: _Optional[_Union[ComponenteVprest, _Mapping]] = ...) -> None: ...

class UpdateComponentePrestacaoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...

class DeleteComponentePrestacaoRequest(_message.Message):
    __slots__ = ("cte_id", "id")
    CTE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    cte_id: str
    id: str
    def __init__(self, cte_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteComponentePrestacaoResponse(_message.Message):
    __slots__ = ("cte",)
    CTE_FIELD_NUMBER: _ClassVar[int]
    cte: Cte
    def __init__(self, cte: _Optional[_Union[Cte, _Mapping]] = ...) -> None: ...
