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

class IcmsCst(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ICMS_CST_00: _ClassVar[IcmsCst]
    ICMS_CST_02: _ClassVar[IcmsCst]
    ICMS_CST_10: _ClassVar[IcmsCst]
    ICMS_CST_15: _ClassVar[IcmsCst]
    ICMS_CST_20: _ClassVar[IcmsCst]
    ICMS_CST_30: _ClassVar[IcmsCst]
    ICMS_CST_40: _ClassVar[IcmsCst]
    ICMS_CST_41: _ClassVar[IcmsCst]
    ICMS_CST_50: _ClassVar[IcmsCst]
    ICMS_CST_51: _ClassVar[IcmsCst]
    ICMS_CST_53: _ClassVar[IcmsCst]
    ICMS_CST_60: _ClassVar[IcmsCst]
    ICMS_CST_61: _ClassVar[IcmsCst]
    ICMS_CST_70: _ClassVar[IcmsCst]
    ICMS_CST_90: _ClassVar[IcmsCst]

class IsCst(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IS_CST_UNSPECIFIED: _ClassVar[IsCst]
    IS_CST_00: _ClassVar[IsCst]
    IS_CST_10: _ClassVar[IsCst]
    IS_CST_20: _ClassVar[IsCst]
    IS_CST_30: _ClassVar[IsCst]
    IS_CST_40: _ClassVar[IsCst]
    IS_CST_41: _ClassVar[IsCst]
    IS_CST_50: _ClassVar[IsCst]
    IS_CST_51: _ClassVar[IsCst]
    IS_CST_60: _ClassVar[IsCst]
    IS_CST_70: _ClassVar[IsCst]
    IS_CST_90: _ClassVar[IsCst]

class PerfilMonofasico(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERFIL_MONOFASICO_UNSPECIFIED: _ClassVar[PerfilMonofasico]
    PERFIL_MONOFASICO_PADRAO: _ClassVar[PerfilMonofasico]
    PERFIL_MONOFASICO_SUBSTITUIDO: _ClassVar[PerfilMonofasico]
    PERFIL_MONOFASICO_SUBSTITUTO: _ClassVar[PerfilMonofasico]
    PERFIL_MONOFASICO_DIFERIMENTO: _ClassVar[PerfilMonofasico]
ICMS_CST_00: IcmsCst
ICMS_CST_02: IcmsCst
ICMS_CST_10: IcmsCst
ICMS_CST_15: IcmsCst
ICMS_CST_20: IcmsCst
ICMS_CST_30: IcmsCst
ICMS_CST_40: IcmsCst
ICMS_CST_41: IcmsCst
ICMS_CST_50: IcmsCst
ICMS_CST_51: IcmsCst
ICMS_CST_53: IcmsCst
ICMS_CST_60: IcmsCst
ICMS_CST_61: IcmsCst
ICMS_CST_70: IcmsCst
ICMS_CST_90: IcmsCst
IS_CST_UNSPECIFIED: IsCst
IS_CST_00: IsCst
IS_CST_10: IsCst
IS_CST_20: IsCst
IS_CST_30: IsCst
IS_CST_40: IsCst
IS_CST_41: IsCst
IS_CST_50: IsCst
IS_CST_51: IsCst
IS_CST_60: IsCst
IS_CST_70: IsCst
IS_CST_90: IsCst
PERFIL_MONOFASICO_UNSPECIFIED: PerfilMonofasico
PERFIL_MONOFASICO_PADRAO: PerfilMonofasico
PERFIL_MONOFASICO_SUBSTITUIDO: PerfilMonofasico
PERFIL_MONOFASICO_SUBSTITUTO: PerfilMonofasico
PERFIL_MONOFASICO_DIFERIMENTO: PerfilMonofasico

class Tributacao(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "nome", "cfopSaida", "icmsCst", "icmsCstNormal", "icmsOrigem", "icmsModalidadeCalculo", "icmsAliquota", "icmsReducaoBase", "icmsReducaoBaseInterestadual", "icmsCreditoPercentual", "icmsStModalidadeCalculo", "icmsStAliquota", "icmsStMargemValorAdicional", "icmsStReducaoBase", "ipiCst", "ipiAliquota", "ipiReducaoBase", "ipiClasseEnquadramento", "ipiCodigoEnquadramento", "ipiCodigoSeloControle", "pisCst", "pisAliquota", "pisReducaoBase", "pisStAliquota", "pisStReducaoBase", "cofinsCst", "cofinsAliquota", "cofinsReducaoBase", "cofinsStAliquota", "cofinsStReducaoBase", "ibs_cbs_cst", "ibs_cbs_classificacao_tributaria", "ibs_cbs_percentual_reducao_base", "fator_conversao_proporcional", "cbs_cst_normal", "cbs_aliquota", "cbs_aliquota_proporcional", "cbs_reducao_base", "cbs_diferimento_percentual", "cbs_devolucao_tributos_percentual", "cbs_reducao_aliquota_percentual", "ibs_cst_normal", "ibs_aliquota", "ibs_reducao_base", "monofasia_ibs_valor_unitario", "monofasia_cbs_valor_unitario", "perfil_monofasico", "ibs_aliquota_uf", "ibs_aliquota_uf_proporcional", "ibs_aliquota_municipio", "ibs_aliquota_municipio_proporcional", "ibs_diferimento_percentual", "ibs_devolucao_tributos_percentual", "ibs_reducao_aliquota_percentual", "ibs_credito_presumido_percentual", "ibs_credito_presumido_valor", "ibs_cbs_trib_regular_cst", "ibs_cbs_trib_regular_classificacao_tributaria", "ibs_cbs_trib_regular_aliquota_cbs", "ibs_cbs_trib_regular_aliquota_ibs_uf", "ibs_cbs_trib_regular_aliquota_ibs_municipio", "is_cst", "is_cst_normal", "is_aliquota", "is_reducao_base", "is_classificacao_tributaria", "is_aliquota_especifica", "is_unidade_tributaria", "is_quantidade_tributada", "is_calculo_por_quantidade", "is_calculo_por_valor", "regime_tributario", "alterada_pelo_usuario", "classificacao_tributaria", "padrao", "icms_por_uf", "icms_por_regime", "pis_cofins_por_regime", "permite_nfce", "somente_leitura", "fields", "informacoes_complementares")
    class IcmsPorUfEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IcmsPorUf
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IcmsPorUf, _Mapping]] = ...) -> None: ...
    class IcmsPorRegimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IcmsPorRegime
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IcmsPorRegime, _Mapping]] = ...) -> None: ...
    class PisCofinsPorRegimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PisCofinsPorRegime
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PisCofinsPorRegime, _Mapping]] = ...) -> None: ...
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CFOPSAIDA_FIELD_NUMBER: _ClassVar[int]
    ICMSCST_FIELD_NUMBER: _ClassVar[int]
    ICMSCSTNORMAL_FIELD_NUMBER: _ClassVar[int]
    ICMSORIGEM_FIELD_NUMBER: _ClassVar[int]
    ICMSMODALIDADECALCULO_FIELD_NUMBER: _ClassVar[int]
    ICMSALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ICMSREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    ICMSREDUCAOBASEINTERESTADUAL_FIELD_NUMBER: _ClassVar[int]
    ICMSCREDITOPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    ICMSSTMODALIDADECALCULO_FIELD_NUMBER: _ClassVar[int]
    ICMSSTALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ICMSSTMARGEMVALORADICIONAL_FIELD_NUMBER: _ClassVar[int]
    ICMSSTREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    IPICST_FIELD_NUMBER: _ClassVar[int]
    IPIALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    IPIREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    IPICLASSEENQUADRAMENTO_FIELD_NUMBER: _ClassVar[int]
    IPICODIGOENQUADRAMENTO_FIELD_NUMBER: _ClassVar[int]
    IPICODIGOSELOCONTROLE_FIELD_NUMBER: _ClassVar[int]
    PISCST_FIELD_NUMBER: _ClassVar[int]
    PISALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    PISREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    PISSTALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    PISSTREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    COFINSCST_FIELD_NUMBER: _ClassVar[int]
    COFINSALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    COFINSREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    COFINSSTALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    COFINSSTREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_CST_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_CLASSIFICACAO_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_PERCENTUAL_REDUCAO_BASE_FIELD_NUMBER: _ClassVar[int]
    FATOR_CONVERSAO_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    CBS_CST_NORMAL_FIELD_NUMBER: _ClassVar[int]
    CBS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CBS_ALIQUOTA_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    CBS_REDUCAO_BASE_FIELD_NUMBER: _ClassVar[int]
    CBS_DIFERIMENTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    CBS_DEVOLUCAO_TRIBUTOS_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    CBS_REDUCAO_ALIQUOTA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    IBS_CST_NORMAL_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    IBS_REDUCAO_BASE_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_IBS_VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_CBS_VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    PERFIL_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_UF_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_UF_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_MUNICIPIO_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    IBS_DIFERIMENTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    IBS_DEVOLUCAO_TRIBUTOS_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    IBS_REDUCAO_ALIQUOTA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    IBS_CREDITO_PRESUMIDO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    IBS_CREDITO_PRESUMIDO_VALOR_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TRIB_REGULAR_CST_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TRIB_REGULAR_CLASSIFICACAO_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TRIB_REGULAR_ALIQUOTA_CBS_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TRIB_REGULAR_ALIQUOTA_IBS_UF_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TRIB_REGULAR_ALIQUOTA_IBS_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    IS_CST_FIELD_NUMBER: _ClassVar[int]
    IS_CST_NORMAL_FIELD_NUMBER: _ClassVar[int]
    IS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    IS_REDUCAO_BASE_FIELD_NUMBER: _ClassVar[int]
    IS_CLASSIFICACAO_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    IS_ALIQUOTA_ESPECIFICA_FIELD_NUMBER: _ClassVar[int]
    IS_UNIDADE_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    IS_QUANTIDADE_TRIBUTADA_FIELD_NUMBER: _ClassVar[int]
    IS_CALCULO_POR_QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    IS_CALCULO_POR_VALOR_FIELD_NUMBER: _ClassVar[int]
    REGIME_TRIBUTARIO_FIELD_NUMBER: _ClassVar[int]
    ALTERADA_PELO_USUARIO_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICACAO_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    PADRAO_FIELD_NUMBER: _ClassVar[int]
    ICMS_POR_UF_FIELD_NUMBER: _ClassVar[int]
    ICMS_POR_REGIME_FIELD_NUMBER: _ClassVar[int]
    PIS_COFINS_POR_REGIME_FIELD_NUMBER: _ClassVar[int]
    PERMITE_NFCE_FIELD_NUMBER: _ClassVar[int]
    SOMENTE_LEITURA_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    INFORMACOES_COMPLEMENTARES_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    nome: str
    cfopSaida: str
    icmsCst: IcmsCst
    icmsCstNormal: str
    icmsOrigem: str
    icmsModalidadeCalculo: str
    icmsAliquota: float
    icmsReducaoBase: float
    icmsReducaoBaseInterestadual: float
    icmsCreditoPercentual: float
    icmsStModalidadeCalculo: str
    icmsStAliquota: float
    icmsStMargemValorAdicional: float
    icmsStReducaoBase: float
    ipiCst: str
    ipiAliquota: float
    ipiReducaoBase: float
    ipiClasseEnquadramento: str
    ipiCodigoEnquadramento: str
    ipiCodigoSeloControle: str
    pisCst: str
    pisAliquota: float
    pisReducaoBase: float
    pisStAliquota: float
    pisStReducaoBase: float
    cofinsCst: str
    cofinsAliquota: float
    cofinsReducaoBase: float
    cofinsStAliquota: float
    cofinsStReducaoBase: float
    ibs_cbs_cst: str
    ibs_cbs_classificacao_tributaria: str
    ibs_cbs_percentual_reducao_base: float
    fator_conversao_proporcional: float
    cbs_cst_normal: str
    cbs_aliquota: float
    cbs_aliquota_proporcional: float
    cbs_reducao_base: float
    cbs_diferimento_percentual: float
    cbs_devolucao_tributos_percentual: float
    cbs_reducao_aliquota_percentual: float
    ibs_cst_normal: str
    ibs_aliquota: float
    ibs_reducao_base: float
    monofasia_ibs_valor_unitario: float
    monofasia_cbs_valor_unitario: float
    perfil_monofasico: PerfilMonofasico
    ibs_aliquota_uf: float
    ibs_aliquota_uf_proporcional: float
    ibs_aliquota_municipio: float
    ibs_aliquota_municipio_proporcional: float
    ibs_diferimento_percentual: float
    ibs_devolucao_tributos_percentual: float
    ibs_reducao_aliquota_percentual: float
    ibs_credito_presumido_percentual: float
    ibs_credito_presumido_valor: float
    ibs_cbs_trib_regular_cst: str
    ibs_cbs_trib_regular_classificacao_tributaria: str
    ibs_cbs_trib_regular_aliquota_cbs: float
    ibs_cbs_trib_regular_aliquota_ibs_uf: float
    ibs_cbs_trib_regular_aliquota_ibs_municipio: float
    is_cst: IsCst
    is_cst_normal: str
    is_aliquota: float
    is_reducao_base: float
    is_classificacao_tributaria: str
    is_aliquota_especifica: float
    is_unidade_tributaria: str
    is_quantidade_tributada: float
    is_calculo_por_quantidade: bool
    is_calculo_por_valor: bool
    regime_tributario: str
    alterada_pelo_usuario: bool
    classificacao_tributaria: str
    padrao: bool
    icms_por_uf: _containers.MessageMap[str, IcmsPorUf]
    icms_por_regime: _containers.MessageMap[str, IcmsPorRegime]
    pis_cofins_por_regime: _containers.MessageMap[str, PisCofinsPorRegime]
    permite_nfce: bool
    somente_leitura: bool
    fields: _metadata_pb2.BasicFields
    informacoes_complementares: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., nome: _Optional[str] = ..., cfopSaida: _Optional[str] = ..., icmsCst: _Optional[_Union[IcmsCst, str]] = ..., icmsCstNormal: _Optional[str] = ..., icmsOrigem: _Optional[str] = ..., icmsModalidadeCalculo: _Optional[str] = ..., icmsAliquota: _Optional[float] = ..., icmsReducaoBase: _Optional[float] = ..., icmsReducaoBaseInterestadual: _Optional[float] = ..., icmsCreditoPercentual: _Optional[float] = ..., icmsStModalidadeCalculo: _Optional[str] = ..., icmsStAliquota: _Optional[float] = ..., icmsStMargemValorAdicional: _Optional[float] = ..., icmsStReducaoBase: _Optional[float] = ..., ipiCst: _Optional[str] = ..., ipiAliquota: _Optional[float] = ..., ipiReducaoBase: _Optional[float] = ..., ipiClasseEnquadramento: _Optional[str] = ..., ipiCodigoEnquadramento: _Optional[str] = ..., ipiCodigoSeloControle: _Optional[str] = ..., pisCst: _Optional[str] = ..., pisAliquota: _Optional[float] = ..., pisReducaoBase: _Optional[float] = ..., pisStAliquota: _Optional[float] = ..., pisStReducaoBase: _Optional[float] = ..., cofinsCst: _Optional[str] = ..., cofinsAliquota: _Optional[float] = ..., cofinsReducaoBase: _Optional[float] = ..., cofinsStAliquota: _Optional[float] = ..., cofinsStReducaoBase: _Optional[float] = ..., ibs_cbs_cst: _Optional[str] = ..., ibs_cbs_classificacao_tributaria: _Optional[str] = ..., ibs_cbs_percentual_reducao_base: _Optional[float] = ..., fator_conversao_proporcional: _Optional[float] = ..., cbs_cst_normal: _Optional[str] = ..., cbs_aliquota: _Optional[float] = ..., cbs_aliquota_proporcional: _Optional[float] = ..., cbs_reducao_base: _Optional[float] = ..., cbs_diferimento_percentual: _Optional[float] = ..., cbs_devolucao_tributos_percentual: _Optional[float] = ..., cbs_reducao_aliquota_percentual: _Optional[float] = ..., ibs_cst_normal: _Optional[str] = ..., ibs_aliquota: _Optional[float] = ..., ibs_reducao_base: _Optional[float] = ..., monofasia_ibs_valor_unitario: _Optional[float] = ..., monofasia_cbs_valor_unitario: _Optional[float] = ..., perfil_monofasico: _Optional[_Union[PerfilMonofasico, str]] = ..., ibs_aliquota_uf: _Optional[float] = ..., ibs_aliquota_uf_proporcional: _Optional[float] = ..., ibs_aliquota_municipio: _Optional[float] = ..., ibs_aliquota_municipio_proporcional: _Optional[float] = ..., ibs_diferimento_percentual: _Optional[float] = ..., ibs_devolucao_tributos_percentual: _Optional[float] = ..., ibs_reducao_aliquota_percentual: _Optional[float] = ..., ibs_credito_presumido_percentual: _Optional[float] = ..., ibs_credito_presumido_valor: _Optional[float] = ..., ibs_cbs_trib_regular_cst: _Optional[str] = ..., ibs_cbs_trib_regular_classificacao_tributaria: _Optional[str] = ..., ibs_cbs_trib_regular_aliquota_cbs: _Optional[float] = ..., ibs_cbs_trib_regular_aliquota_ibs_uf: _Optional[float] = ..., ibs_cbs_trib_regular_aliquota_ibs_municipio: _Optional[float] = ..., is_cst: _Optional[_Union[IsCst, str]] = ..., is_cst_normal: _Optional[str] = ..., is_aliquota: _Optional[float] = ..., is_reducao_base: _Optional[float] = ..., is_classificacao_tributaria: _Optional[str] = ..., is_aliquota_especifica: _Optional[float] = ..., is_unidade_tributaria: _Optional[str] = ..., is_quantidade_tributada: _Optional[float] = ..., is_calculo_por_quantidade: _Optional[bool] = ..., is_calculo_por_valor: _Optional[bool] = ..., regime_tributario: _Optional[str] = ..., alterada_pelo_usuario: _Optional[bool] = ..., classificacao_tributaria: _Optional[str] = ..., padrao: _Optional[bool] = ..., icms_por_uf: _Optional[_Mapping[str, IcmsPorUf]] = ..., icms_por_regime: _Optional[_Mapping[str, IcmsPorRegime]] = ..., pis_cofins_por_regime: _Optional[_Mapping[str, PisCofinsPorRegime]] = ..., permite_nfce: _Optional[bool] = ..., somente_leitura: _Optional[bool] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., informacoes_complementares: _Optional[str] = ...) -> None: ...

class IcmsPorUf(_message.Message):
    __slots__ = ("aliquota", "cst", "reducao_base")
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CST_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_BASE_FIELD_NUMBER: _ClassVar[int]
    aliquota: float
    cst: str
    reducao_base: float
    def __init__(self, aliquota: _Optional[float] = ..., cst: _Optional[str] = ..., reducao_base: _Optional[float] = ...) -> None: ...

class IcmsPorRegime(_message.Message):
    __slots__ = ("cst",)
    CST_FIELD_NUMBER: _ClassVar[int]
    cst: str
    def __init__(self, cst: _Optional[str] = ...) -> None: ...

class PisCofinsPorRegime(_message.Message):
    __slots__ = ("cst", "pis_aliquota", "cofins_aliquota")
    CST_FIELD_NUMBER: _ClassVar[int]
    PIS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    COFINS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    cst: str
    pis_aliquota: float
    cofins_aliquota: float
    def __init__(self, cst: _Optional[str] = ..., pis_aliquota: _Optional[float] = ..., cofins_aliquota: _Optional[float] = ...) -> None: ...

class CreateTributacaoRequest(_message.Message):
    __slots__ = ("tributacao",)
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    tributacao: Tributacao
    def __init__(self, tributacao: _Optional[_Union[Tributacao, _Mapping]] = ...) -> None: ...

class CreateTributacaoResponse(_message.Message):
    __slots__ = ("tributacao",)
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    tributacao: Tributacao
    def __init__(self, tributacao: _Optional[_Union[Tributacao, _Mapping]] = ...) -> None: ...

class UpdateTributacaoRequest(_message.Message):
    __slots__ = ("id", "tributacao", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    tributacao: Tributacao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., tributacao: _Optional[_Union[Tributacao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateTributacaoResponse(_message.Message):
    __slots__ = ("tributacao",)
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    tributacao: Tributacao
    def __init__(self, tributacao: _Optional[_Union[Tributacao, _Mapping]] = ...) -> None: ...

class DeleteTributacaoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteTributacaoResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTributacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTributacaoResponse(_message.Message):
    __slots__ = ("tributacao",)
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    tributacao: Tributacao
    def __init__(self, tributacao: _Optional[_Union[Tributacao, _Mapping]] = ...) -> None: ...

class ListTributacaoRequest(_message.Message):
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

class ListTributacaoResponse(_message.Message):
    __slots__ = ("tributacaoList", "next_page_token")
    TRIBUTACAOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tributacaoList: _containers.RepeatedCompositeFieldContainer[Tributacao]
    next_page_token: str
    def __init__(self, tributacaoList: _Optional[_Iterable[_Union[Tributacao, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CloneTributacaoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneTributacaoResponse(_message.Message):
    __slots__ = ("tributacao",)
    TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    tributacao: Tributacao
    def __init__(self, tributacao: _Optional[_Union[Tributacao, _Mapping]] = ...) -> None: ...

class ClassificacaoTributaria(_message.Message):
    __slots__ = ("codigo", "descricao", "cst", "cst_descricao", "nome", "texto_legal", "artigo", "link", "reducao_ibs", "reducao_cbs", "exige_tributacao", "nfe", "nfce")
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    CST_FIELD_NUMBER: _ClassVar[int]
    CST_DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TEXTO_LEGAL_FIELD_NUMBER: _ClassVar[int]
    ARTIGO_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_IBS_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_CBS_FIELD_NUMBER: _ClassVar[int]
    EXIGE_TRIBUTACAO_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    NFCE_FIELD_NUMBER: _ClassVar[int]
    codigo: str
    descricao: str
    cst: str
    cst_descricao: str
    nome: str
    texto_legal: str
    artigo: str
    link: str
    reducao_ibs: float
    reducao_cbs: float
    exige_tributacao: bool
    nfe: bool
    nfce: bool
    def __init__(self, codigo: _Optional[str] = ..., descricao: _Optional[str] = ..., cst: _Optional[str] = ..., cst_descricao: _Optional[str] = ..., nome: _Optional[str] = ..., texto_legal: _Optional[str] = ..., artigo: _Optional[str] = ..., link: _Optional[str] = ..., reducao_ibs: _Optional[float] = ..., reducao_cbs: _Optional[float] = ..., exige_tributacao: _Optional[bool] = ..., nfe: _Optional[bool] = ..., nfce: _Optional[bool] = ...) -> None: ...

class ListClassificacaoTributariaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClassificacaoTributariaResponse(_message.Message):
    __slots__ = ("classificacoes", "ibs_aliquota_uf", "ibs_aliquota_municipio", "cbs_aliquota")
    CLASSIFICACOES_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_UF_FIELD_NUMBER: _ClassVar[int]
    IBS_ALIQUOTA_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    CBS_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    classificacoes: _containers.RepeatedCompositeFieldContainer[ClassificacaoTributaria]
    ibs_aliquota_uf: float
    ibs_aliquota_municipio: float
    cbs_aliquota: float
    def __init__(self, classificacoes: _Optional[_Iterable[_Union[ClassificacaoTributaria, _Mapping]]] = ..., ibs_aliquota_uf: _Optional[float] = ..., ibs_aliquota_municipio: _Optional[float] = ..., cbs_aliquota: _Optional[float] = ...) -> None: ...
