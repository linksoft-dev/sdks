from linksoft_sdk.pb.apps.dfe.tributacao import tributacao_pb2 as _tributacao_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsTotal(_message.Message):
    __slots__ = ("valor",)
    VALOR_FIELD_NUMBER: _ClassVar[int]
    valor: float
    def __init__(self, valor: _Optional[float] = ...) -> None: ...

class IbsCbsTotal(_message.Message):
    __slots__ = ("valor_base", "ibs", "cbs", "monofasia", "estorno_credito")
    VALOR_BASE_FIELD_NUMBER: _ClassVar[int]
    IBS_FIELD_NUMBER: _ClassVar[int]
    CBS_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_FIELD_NUMBER: _ClassVar[int]
    ESTORNO_CREDITO_FIELD_NUMBER: _ClassVar[int]
    valor_base: float
    ibs: IbsTotal
    cbs: CbsTotal
    monofasia: MonofasiaTotal
    estorno_credito: EstornoCredito
    def __init__(self, valor_base: _Optional[float] = ..., ibs: _Optional[_Union[IbsTotal, _Mapping]] = ..., cbs: _Optional[_Union[CbsTotal, _Mapping]] = ..., monofasia: _Optional[_Union[MonofasiaTotal, _Mapping]] = ..., estorno_credito: _Optional[_Union[EstornoCredito, _Mapping]] = ...) -> None: ...

class EstornoCredito(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class IbsTotal(_message.Message):
    __slots__ = ("valor_uf", "valor_municipio", "valor", "credito_presumido", "diferimento", "devolucao_tributos")
    VALOR_UF_FIELD_NUMBER: _ClassVar[int]
    VALOR_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    CREDITO_PRESUMIDO_FIELD_NUMBER: _ClassVar[int]
    DIFERIMENTO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    valor_uf: float
    valor_municipio: float
    valor: float
    credito_presumido: CreditoPresumidoTotal
    diferimento: DiferimentoTotal
    devolucao_tributos: DevolucaoTributosTotal
    def __init__(self, valor_uf: _Optional[float] = ..., valor_municipio: _Optional[float] = ..., valor: _Optional[float] = ..., credito_presumido: _Optional[_Union[CreditoPresumidoTotal, _Mapping]] = ..., diferimento: _Optional[_Union[DiferimentoTotal, _Mapping]] = ..., devolucao_tributos: _Optional[_Union[DevolucaoTributosTotal, _Mapping]] = ...) -> None: ...

class CbsTotal(_message.Message):
    __slots__ = ("valor", "credito_presumido", "diferimento", "devolucao_tributos")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    CREDITO_PRESUMIDO_FIELD_NUMBER: _ClassVar[int]
    DIFERIMENTO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    valor: float
    credito_presumido: CreditoPresumidoTotal
    diferimento: DiferimentoTotal
    devolucao_tributos: DevolucaoTributosTotal
    def __init__(self, valor: _Optional[float] = ..., credito_presumido: _Optional[_Union[CreditoPresumidoTotal, _Mapping]] = ..., diferimento: _Optional[_Union[DiferimentoTotal, _Mapping]] = ..., devolucao_tributos: _Optional[_Union[DevolucaoTributosTotal, _Mapping]] = ...) -> None: ...

class MonofasiaTotal(_message.Message):
    __slots__ = ("ibs", "cbs")
    IBS_FIELD_NUMBER: _ClassVar[int]
    CBS_FIELD_NUMBER: _ClassVar[int]
    ibs: MonofasiaIbsTotal
    cbs: MonofasiaCbsTotal
    def __init__(self, ibs: _Optional[_Union[MonofasiaIbsTotal, _Mapping]] = ..., cbs: _Optional[_Union[MonofasiaCbsTotal, _Mapping]] = ...) -> None: ...

class Totais(_message.Message):
    __slots__ = ("ibs_cbs_total", "valor_nf_tot")
    IS_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_NF_TOT_FIELD_NUMBER: _ClassVar[int]
    ibs_cbs_total: IbsCbsTotal
    valor_nf_tot: float
    def __init__(self, ibs_cbs_total: _Optional[_Union[IbsCbsTotal, _Mapping]] = ..., valor_nf_tot: _Optional[float] = ..., **kwargs) -> None: ...

class MonofasiaIbsTotal(_message.Message):
    __slots__ = ("valor", "valor_reten", "valor_ret")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_RETEN_FIELD_NUMBER: _ClassVar[int]
    VALOR_RET_FIELD_NUMBER: _ClassVar[int]
    valor: float
    valor_reten: float
    valor_ret: float
    def __init__(self, valor: _Optional[float] = ..., valor_reten: _Optional[float] = ..., valor_ret: _Optional[float] = ...) -> None: ...

class MonofasiaCbsTotal(_message.Message):
    __slots__ = ("valor", "valor_reten", "valor_ret")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_RETEN_FIELD_NUMBER: _ClassVar[int]
    VALOR_RET_FIELD_NUMBER: _ClassVar[int]
    valor: float
    valor_reten: float
    valor_ret: float
    def __init__(self, valor: _Optional[float] = ..., valor_reten: _Optional[float] = ..., valor_ret: _Optional[float] = ...) -> None: ...

class CreditoPresumidoTotal(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs", "valor_ibs_cond_sus", "valor_cbs_cond_sus")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_IBS_COND_SUS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_COND_SUS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    valor_ibs_cond_sus: float
    valor_cbs_cond_sus: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ..., valor_ibs_cond_sus: _Optional[float] = ..., valor_cbs_cond_sus: _Optional[float] = ...) -> None: ...

class DiferimentoTotal(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class DevolucaoTributosTotal(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class ImpostoIs(_message.Message):
    __slots__ = ("cst_is", "c_class_trib_is", "base_valor", "aliquota", "aliquota_especifica", "unidade_tributaria", "quantidade_tributada", "valor")
    CST_IS_FIELD_NUMBER: _ClassVar[int]
    C_CLASS_TRIB_IS_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ESPECIFICA_FIELD_NUMBER: _ClassVar[int]
    UNIDADE_TRIBUTARIA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_TRIBUTADA_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    cst_is: str
    c_class_trib_is: str
    base_valor: float
    aliquota: float
    aliquota_especifica: float
    unidade_tributaria: str
    quantidade_tributada: float
    valor: float
    def __init__(self, cst_is: _Optional[str] = ..., c_class_trib_is: _Optional[str] = ..., base_valor: _Optional[float] = ..., aliquota: _Optional[float] = ..., aliquota_especifica: _Optional[float] = ..., unidade_tributaria: _Optional[str] = ..., quantidade_tributada: _Optional[float] = ..., valor: _Optional[float] = ...) -> None: ...

class ImpostoIbsCbs(_message.Message):
    __slots__ = ("cst", "c_class_trib", "base_valor", "exclusao_base", "fator_conversao_proporcional", "ibs_uf", "ibs_municipio", "valor_ibs", "cbs", "trib_regular", "cred_pres_ibs", "cred_pres_cbs", "trib_compra_gov", "monofasia", "calculo_manual_bc", "estorno_credito", "competencia_apuracao")
    CST_FIELD_NUMBER: _ClassVar[int]
    C_CLASS_TRIB_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    EXCLUSAO_BASE_FIELD_NUMBER: _ClassVar[int]
    FATOR_CONVERSAO_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    IBS_UF_FIELD_NUMBER: _ClassVar[int]
    IBS_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    CBS_FIELD_NUMBER: _ClassVar[int]
    TRIB_REGULAR_FIELD_NUMBER: _ClassVar[int]
    CRED_PRES_IBS_FIELD_NUMBER: _ClassVar[int]
    CRED_PRES_CBS_FIELD_NUMBER: _ClassVar[int]
    TRIB_COMPRA_GOV_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_FIELD_NUMBER: _ClassVar[int]
    CALCULO_MANUAL_BC_FIELD_NUMBER: _ClassVar[int]
    ESTORNO_CREDITO_FIELD_NUMBER: _ClassVar[int]
    COMPETENCIA_APURACAO_FIELD_NUMBER: _ClassVar[int]
    cst: str
    c_class_trib: str
    base_valor: float
    exclusao_base: float
    fator_conversao_proporcional: float
    ibs_uf: IbsUf
    ibs_municipio: IbsMunicipio
    valor_ibs: float
    cbs: Cbs
    trib_regular: TribRegular
    cred_pres_ibs: CredPresIbs
    cred_pres_cbs: CredPresCbs
    trib_compra_gov: TribCompraGov
    monofasia: Monofasia
    calculo_manual_bc: bool
    estorno_credito: EstornoCredito
    competencia_apuracao: str
    def __init__(self, cst: _Optional[str] = ..., c_class_trib: _Optional[str] = ..., base_valor: _Optional[float] = ..., exclusao_base: _Optional[float] = ..., fator_conversao_proporcional: _Optional[float] = ..., ibs_uf: _Optional[_Union[IbsUf, _Mapping]] = ..., ibs_municipio: _Optional[_Union[IbsMunicipio, _Mapping]] = ..., valor_ibs: _Optional[float] = ..., cbs: _Optional[_Union[Cbs, _Mapping]] = ..., trib_regular: _Optional[_Union[TribRegular, _Mapping]] = ..., cred_pres_ibs: _Optional[_Union[CredPresIbs, _Mapping]] = ..., cred_pres_cbs: _Optional[_Union[CredPresCbs, _Mapping]] = ..., trib_compra_gov: _Optional[_Union[TribCompraGov, _Mapping]] = ..., monofasia: _Optional[_Union[Monofasia, _Mapping]] = ..., calculo_manual_bc: _Optional[bool] = ..., estorno_credito: _Optional[_Union[EstornoCredito, _Mapping]] = ..., competencia_apuracao: _Optional[str] = ...) -> None: ...

class Monofasia(_message.Message):
    __slots__ = ("perfil_monofasico", "fator_conversao_monofasico", "quantidade_base_calculo", "aliquota_adrem_ibs", "aliquota_adrem_cbs", "monofasia_padrao", "monofasia_reten", "monofasia_ret", "monofasia_dif", "total_ibs", "total_cbs")
    PERFIL_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    FATOR_CONVERSAO_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_BASE_CALCULO_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ADREM_IBS_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ADREM_CBS_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_PADRAO_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_RETEN_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_RET_FIELD_NUMBER: _ClassVar[int]
    MONOFASIA_DIF_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IBS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CBS_FIELD_NUMBER: _ClassVar[int]
    perfil_monofasico: _tributacao_pb2.PerfilMonofasico
    fator_conversao_monofasico: float
    quantidade_base_calculo: float
    aliquota_adrem_ibs: float
    aliquota_adrem_cbs: float
    monofasia_padrao: MonofasiaPadrao
    monofasia_reten: MonofasiaReten
    monofasia_ret: MonofasiaRet
    monofasia_dif: MonofasiaDif
    total_ibs: float
    total_cbs: float
    def __init__(self, perfil_monofasico: _Optional[_Union[_tributacao_pb2.PerfilMonofasico, str]] = ..., fator_conversao_monofasico: _Optional[float] = ..., quantidade_base_calculo: _Optional[float] = ..., aliquota_adrem_ibs: _Optional[float] = ..., aliquota_adrem_cbs: _Optional[float] = ..., monofasia_padrao: _Optional[_Union[MonofasiaPadrao, _Mapping]] = ..., monofasia_reten: _Optional[_Union[MonofasiaReten, _Mapping]] = ..., monofasia_ret: _Optional[_Union[MonofasiaRet, _Mapping]] = ..., monofasia_dif: _Optional[_Union[MonofasiaDif, _Mapping]] = ..., total_ibs: _Optional[float] = ..., total_cbs: _Optional[float] = ...) -> None: ...

class MonofasiaPadrao(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class MonofasiaReten(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class MonofasiaRet(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class MonofasiaDif(_message.Message):
    __slots__ = ("percentual_ibs", "percentual_cbs", "valor_ibs", "valor_cbs")
    PERCENTUAL_IBS_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_CBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    percentual_ibs: float
    percentual_cbs: float
    valor_ibs: float
    valor_cbs: float
    def __init__(self, percentual_ibs: _Optional[float] = ..., percentual_cbs: _Optional[float] = ..., valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class IbsUf(_message.Message):
    __slots__ = ("aliquota", "aliquota_proporcional", "valor", "diferimento", "devolucao_tributos", "reducao")
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    DIFERIMENTO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_FIELD_NUMBER: _ClassVar[int]
    aliquota: float
    aliquota_proporcional: float
    valor: float
    diferimento: Dif
    devolucao_tributos: DevTrib
    reducao: Red
    def __init__(self, aliquota: _Optional[float] = ..., aliquota_proporcional: _Optional[float] = ..., valor: _Optional[float] = ..., diferimento: _Optional[_Union[Dif, _Mapping]] = ..., devolucao_tributos: _Optional[_Union[DevTrib, _Mapping]] = ..., reducao: _Optional[_Union[Red, _Mapping]] = ...) -> None: ...

class IbsMunicipio(_message.Message):
    __slots__ = ("aliquota", "aliquota_proporcional", "valor", "diferimento", "devolucao_tributos", "reducao")
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    DIFERIMENTO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_FIELD_NUMBER: _ClassVar[int]
    aliquota: float
    aliquota_proporcional: float
    valor: float
    diferimento: Dif
    devolucao_tributos: DevTrib
    reducao: Red
    def __init__(self, aliquota: _Optional[float] = ..., aliquota_proporcional: _Optional[float] = ..., valor: _Optional[float] = ..., diferimento: _Optional[_Union[Dif, _Mapping]] = ..., devolucao_tributos: _Optional[_Union[DevTrib, _Mapping]] = ..., reducao: _Optional[_Union[Red, _Mapping]] = ...) -> None: ...

class Cbs(_message.Message):
    __slots__ = ("aliquota", "aliquota_proporcional", "valor", "diferimento", "devolucao_tributos", "reducao")
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    DIFERIMENTO_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    REDUCAO_FIELD_NUMBER: _ClassVar[int]
    aliquota: float
    aliquota_proporcional: float
    valor: float
    diferimento: Dif
    devolucao_tributos: DevTrib
    reducao: Red
    def __init__(self, aliquota: _Optional[float] = ..., aliquota_proporcional: _Optional[float] = ..., valor: _Optional[float] = ..., diferimento: _Optional[_Union[Dif, _Mapping]] = ..., devolucao_tributos: _Optional[_Union[DevTrib, _Mapping]] = ..., reducao: _Optional[_Union[Red, _Mapping]] = ...) -> None: ...

class Dif(_message.Message):
    __slots__ = ("valor", "percentual")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    valor: float
    percentual: float
    def __init__(self, valor: _Optional[float] = ..., percentual: _Optional[float] = ...) -> None: ...

class DevTrib(_message.Message):
    __slots__ = ("valor", "percentual")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    valor: float
    percentual: float
    def __init__(self, valor: _Optional[float] = ..., percentual: _Optional[float] = ...) -> None: ...

class Red(_message.Message):
    __slots__ = ("valor", "percentual", "percentual_efetivo")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_EFETIVO_FIELD_NUMBER: _ClassVar[int]
    valor: float
    percentual: float
    percentual_efetivo: float
    def __init__(self, valor: _Optional[float] = ..., percentual: _Optional[float] = ..., percentual_efetivo: _Optional[float] = ...) -> None: ...

class TribRegular(_message.Message):
    __slots__ = ("cst", "c_class_trib", "aliquota_ibs_uf", "aliquota_ibs_mun", "aliquota_cbs", "valor_ibs_uf", "valor_ibs_mun", "valor_cbs")
    CST_FIELD_NUMBER: _ClassVar[int]
    C_CLASS_TRIB_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_IBS_UF_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_IBS_MUN_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_CBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_IBS_UF_FIELD_NUMBER: _ClassVar[int]
    VALOR_IBS_MUN_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    cst: str
    c_class_trib: str
    aliquota_ibs_uf: float
    aliquota_ibs_mun: float
    aliquota_cbs: float
    valor_ibs_uf: float
    valor_ibs_mun: float
    valor_cbs: float
    def __init__(self, cst: _Optional[str] = ..., c_class_trib: _Optional[str] = ..., aliquota_ibs_uf: _Optional[float] = ..., aliquota_ibs_mun: _Optional[float] = ..., aliquota_cbs: _Optional[float] = ..., valor_ibs_uf: _Optional[float] = ..., valor_ibs_mun: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...

class CredPresIbs(_message.Message):
    __slots__ = ("valor", "percentual")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    valor: float
    percentual: float
    def __init__(self, valor: _Optional[float] = ..., percentual: _Optional[float] = ...) -> None: ...

class CredPresCbs(_message.Message):
    __slots__ = ("valor", "percentual")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    valor: float
    percentual: float
    def __init__(self, valor: _Optional[float] = ..., percentual: _Optional[float] = ...) -> None: ...

class TribCompraGov(_message.Message):
    __slots__ = ("valor_ibs", "valor_cbs")
    VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
    valor_ibs: float
    valor_cbs: float
    def __init__(self, valor_ibs: _Optional[float] = ..., valor_cbs: _Optional[float] = ...) -> None: ...
