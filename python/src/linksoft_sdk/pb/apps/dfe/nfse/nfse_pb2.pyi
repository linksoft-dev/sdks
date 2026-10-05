import datetime

from linksoft_sdk.pb.apps.dfe.emitente import emitente_pb2 as _emitente_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_NAO_ESPECIFICADA: _ClassVar[Situacao]
    SITUACAO_DIGITADA: _ClassVar[Situacao]
    SITUACAO_AUTORIZADA: _ClassVar[Situacao]
    SITUACAO_CANCELADA: _ClassVar[Situacao]
    SITUACAO_REJEITADA: _ClassVar[Situacao]
    SITUACAO_PROCESSANDO: _ClassVar[Situacao]
    SITUACAO_INCONSISTENTE: _ClassVar[Situacao]
    SITUACAO_SUBSTITUIDA: _ClassVar[Situacao]

class Ambiente(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AMBIENTE_HOMOLOGACAO: _ClassVar[Ambiente]
    AMBIENTE_PRODUCAO: _ClassVar[Ambiente]

class NaturezaDaOperacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NATUREZA_UNSPECIFIED: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_MUNICIPIO: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_FORA_MUNICIPIO: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_ISENCAO: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_IMUNE: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_EXIGI_SUSPENSA_DECISAO_JUDICIAL: _ClassVar[NaturezaDaOperacao]
    TRIBUTACAO_EXIGI_SUSPENSA_ADMINISTRATIVO: _ClassVar[NaturezaDaOperacao]

class RegimeEspecial(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGIME_ESPECIAL_NENHUM: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_EMPRESA_MUNICIPAL: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_ESTIMATIVA: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_SOCIEDADE_PROFISSIONAIS: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_COOPERATIVA: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_MEI: _ClassVar[RegimeEspecial]
    REGIME_ESPECIAL_EPP: _ClassVar[RegimeEspecial]

class CodigoCancelamento(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CODIGO_CANCELAMENTO_NAO_ESPECIFICADO: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_ERRO_EMISSAO: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_SERVICO_NAO_PRESTADO: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_ERRO_ASSINATURA: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_DUPLICIDADE: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_ERRO_PROCESSAMENTO: _ClassVar[CodigoCancelamento]
    CODIGO_CANCELAMENTO_OUTROS: _ClassVar[CodigoCancelamento]

class RegimeApuracaoSN(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGIME_APURACAO_SN_NAO_ESPECIFICADO: _ClassVar[RegimeApuracaoSN]
    REGIME_APURACAO_SN_COMPLETO: _ClassVar[RegimeApuracaoSN]
    REGIME_APURACAO_SN_ISSQN_FORA: _ClassVar[RegimeApuracaoSN]
    REGIME_APURACAO_SN_TODOS_FORA: _ClassVar[RegimeApuracaoSN]

class ExigibilidadeISS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXIGIBILIDADE_ISS_NAO_ESPECIFICADA: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_EXIGIVEL: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_NAO_INCIDENCIA: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_ISENCAO: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_EXPORTACAO: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_IMUNIDADE: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_SUSPENSA_JUDICIAL: _ClassVar[ExigibilidadeISS]
    EXIGIBILIDADE_ISS_SUSPENSA_ADMINISTRATIVA: _ClassVar[ExigibilidadeISS]

class TipoOperacaoRejeicao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_OPERACAO_REJEICAO_NAO_ESPECIFICADA: _ClassVar[TipoOperacaoRejeicao]
    TIPO_OPERACAO_REJEICAO_ENVIO: _ClassVar[TipoOperacaoRejeicao]
    TIPO_OPERACAO_REJEICAO_CANCELAMENTO: _ClassVar[TipoOperacaoRejeicao]
    TIPO_OPERACAO_REJEICAO_CONSULTA: _ClassVar[TipoOperacaoRejeicao]
    TIPO_OPERACAO_REJEICAO_SUBSTITUICAO: _ClassVar[TipoOperacaoRejeicao]

class TipoEventoNfse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_EVENTO_NFSE_NAO_ESPECIFICADO: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_AUTORIZACAO: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_CANCELAMENTO: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_EMAIL_ENVIADO: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_EMAIL_FALHA: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_WHATSAPP: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_SUBSTITUICAO: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_DOWNLOAD_XML: _ClassVar[TipoEventoNfse]
    TIPO_EVENTO_NFSE_DOWNLOAD_PDF: _ClassVar[TipoEventoNfse]

class CodigoMotivoSubstituicao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CODIGO_MOTIVO_SUBSTITUICAO_NAO_ESPECIFICADO: _ClassVar[CodigoMotivoSubstituicao]
    CODIGO_MOTIVO_SUBSTITUICAO_ERRO_TOMADOR: _ClassVar[CodigoMotivoSubstituicao]
    CODIGO_MOTIVO_SUBSTITUICAO_ERRO_VALOR: _ClassVar[CodigoMotivoSubstituicao]
    CODIGO_MOTIVO_SUBSTITUICAO_ERRO_DISCRIMINACAO: _ClassVar[CodigoMotivoSubstituicao]
    CODIGO_MOTIVO_SUBSTITUICAO_ERRO_ALIQUOTA: _ClassVar[CodigoMotivoSubstituicao]
    CODIGO_MOTIVO_SUBSTITUICAO_OUTROS: _ClassVar[CodigoMotivoSubstituicao]

class CanalEnvioNfse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANAL_ENVIO_NFSE_UNSPECIFIED: _ClassVar[CanalEnvioNfse]
    CANAL_ENVIO_NFSE_EMAIL: _ClassVar[CanalEnvioNfse]
    CANAL_ENVIO_NFSE_WHATSAPP: _ClassVar[CanalEnvioNfse]

class TipoDownload(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_DOWNLOAD_NAO_ESPECIFICADO: _ClassVar[TipoDownload]
    TIPO_DOWNLOAD_XML: _ClassVar[TipoDownload]
    TIPO_DOWNLOAD_PDF: _ClassVar[TipoDownload]

class FormatoXmlCompetencia(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORMATO_XML_COMPETENCIA_ZIP: _ClassVar[FormatoXmlCompetencia]
    FORMATO_XML_COMPETENCIA_CONSOLIDADO: _ClassVar[FormatoXmlCompetencia]

class ImportaXmlModoAtualizacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORTA_XML_MODO_NAO_SOBRESCREVER: _ClassVar[ImportaXmlModoAtualizacao]
    IMPORTA_XML_MODO_MESCLAR: _ClassVar[ImportaXmlModoAtualizacao]
    IMPORTA_XML_MODO_SOBRESCREVER: _ClassVar[ImportaXmlModoAtualizacao]
SITUACAO_NAO_ESPECIFICADA: Situacao
SITUACAO_DIGITADA: Situacao
SITUACAO_AUTORIZADA: Situacao
SITUACAO_CANCELADA: Situacao
SITUACAO_REJEITADA: Situacao
SITUACAO_PROCESSANDO: Situacao
SITUACAO_INCONSISTENTE: Situacao
SITUACAO_SUBSTITUIDA: Situacao
AMBIENTE_HOMOLOGACAO: Ambiente
AMBIENTE_PRODUCAO: Ambiente
NATUREZA_UNSPECIFIED: NaturezaDaOperacao
TRIBUTACAO_MUNICIPIO: NaturezaDaOperacao
TRIBUTACAO_FORA_MUNICIPIO: NaturezaDaOperacao
TRIBUTACAO_ISENCAO: NaturezaDaOperacao
TRIBUTACAO_IMUNE: NaturezaDaOperacao
TRIBUTACAO_EXIGI_SUSPENSA_DECISAO_JUDICIAL: NaturezaDaOperacao
TRIBUTACAO_EXIGI_SUSPENSA_ADMINISTRATIVO: NaturezaDaOperacao
REGIME_ESPECIAL_NENHUM: RegimeEspecial
REGIME_ESPECIAL_EMPRESA_MUNICIPAL: RegimeEspecial
REGIME_ESPECIAL_ESTIMATIVA: RegimeEspecial
REGIME_ESPECIAL_SOCIEDADE_PROFISSIONAIS: RegimeEspecial
REGIME_ESPECIAL_COOPERATIVA: RegimeEspecial
REGIME_ESPECIAL_MEI: RegimeEspecial
REGIME_ESPECIAL_EPP: RegimeEspecial
CODIGO_CANCELAMENTO_NAO_ESPECIFICADO: CodigoCancelamento
CODIGO_CANCELAMENTO_ERRO_EMISSAO: CodigoCancelamento
CODIGO_CANCELAMENTO_SERVICO_NAO_PRESTADO: CodigoCancelamento
CODIGO_CANCELAMENTO_ERRO_ASSINATURA: CodigoCancelamento
CODIGO_CANCELAMENTO_DUPLICIDADE: CodigoCancelamento
CODIGO_CANCELAMENTO_ERRO_PROCESSAMENTO: CodigoCancelamento
CODIGO_CANCELAMENTO_OUTROS: CodigoCancelamento
REGIME_APURACAO_SN_NAO_ESPECIFICADO: RegimeApuracaoSN
REGIME_APURACAO_SN_COMPLETO: RegimeApuracaoSN
REGIME_APURACAO_SN_ISSQN_FORA: RegimeApuracaoSN
REGIME_APURACAO_SN_TODOS_FORA: RegimeApuracaoSN
EXIGIBILIDADE_ISS_NAO_ESPECIFICADA: ExigibilidadeISS
EXIGIBILIDADE_ISS_EXIGIVEL: ExigibilidadeISS
EXIGIBILIDADE_ISS_NAO_INCIDENCIA: ExigibilidadeISS
EXIGIBILIDADE_ISS_ISENCAO: ExigibilidadeISS
EXIGIBILIDADE_ISS_EXPORTACAO: ExigibilidadeISS
EXIGIBILIDADE_ISS_IMUNIDADE: ExigibilidadeISS
EXIGIBILIDADE_ISS_SUSPENSA_JUDICIAL: ExigibilidadeISS
EXIGIBILIDADE_ISS_SUSPENSA_ADMINISTRATIVA: ExigibilidadeISS
TIPO_OPERACAO_REJEICAO_NAO_ESPECIFICADA: TipoOperacaoRejeicao
TIPO_OPERACAO_REJEICAO_ENVIO: TipoOperacaoRejeicao
TIPO_OPERACAO_REJEICAO_CANCELAMENTO: TipoOperacaoRejeicao
TIPO_OPERACAO_REJEICAO_CONSULTA: TipoOperacaoRejeicao
TIPO_OPERACAO_REJEICAO_SUBSTITUICAO: TipoOperacaoRejeicao
TIPO_EVENTO_NFSE_NAO_ESPECIFICADO: TipoEventoNfse
TIPO_EVENTO_NFSE_AUTORIZACAO: TipoEventoNfse
TIPO_EVENTO_NFSE_CANCELAMENTO: TipoEventoNfse
TIPO_EVENTO_NFSE_EMAIL_ENVIADO: TipoEventoNfse
TIPO_EVENTO_NFSE_EMAIL_FALHA: TipoEventoNfse
TIPO_EVENTO_NFSE_WHATSAPP: TipoEventoNfse
TIPO_EVENTO_NFSE_SUBSTITUICAO: TipoEventoNfse
TIPO_EVENTO_NFSE_DOWNLOAD_XML: TipoEventoNfse
TIPO_EVENTO_NFSE_DOWNLOAD_PDF: TipoEventoNfse
CODIGO_MOTIVO_SUBSTITUICAO_NAO_ESPECIFICADO: CodigoMotivoSubstituicao
CODIGO_MOTIVO_SUBSTITUICAO_ERRO_TOMADOR: CodigoMotivoSubstituicao
CODIGO_MOTIVO_SUBSTITUICAO_ERRO_VALOR: CodigoMotivoSubstituicao
CODIGO_MOTIVO_SUBSTITUICAO_ERRO_DISCRIMINACAO: CodigoMotivoSubstituicao
CODIGO_MOTIVO_SUBSTITUICAO_ERRO_ALIQUOTA: CodigoMotivoSubstituicao
CODIGO_MOTIVO_SUBSTITUICAO_OUTROS: CodigoMotivoSubstituicao
CANAL_ENVIO_NFSE_UNSPECIFIED: CanalEnvioNfse
CANAL_ENVIO_NFSE_EMAIL: CanalEnvioNfse
CANAL_ENVIO_NFSE_WHATSAPP: CanalEnvioNfse
TIPO_DOWNLOAD_NAO_ESPECIFICADO: TipoDownload
TIPO_DOWNLOAD_XML: TipoDownload
TIPO_DOWNLOAD_PDF: TipoDownload
FORMATO_XML_COMPETENCIA_ZIP: FormatoXmlCompetencia
FORMATO_XML_COMPETENCIA_CONSOLIDADO: FormatoXmlCompetencia
IMPORTA_XML_MODO_NAO_SOBRESCREVER: ImportaXmlModoAtualizacao
IMPORTA_XML_MODO_MESCLAR: ImportaXmlModoAtualizacao
IMPORTA_XML_MODO_SOBRESCREVER: ImportaXmlModoAtualizacao

class ExplainRejectionRequest(_message.Message):
    __slots__ = ("id", "ai_integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    ai_integration_id: str
    def __init__(self, id: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class ExplainRejectionResponse(_message.Message):
    __slots__ = ("cstat", "original_message", "explanation", "recommended_actions", "severity")
    CSTAT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    cstat: str
    original_message: str
    explanation: str
    recommended_actions: _containers.RepeatedScalarFieldContainer[str]
    severity: str
    def __init__(self, cstat: _Optional[str] = ..., original_message: _Optional[str] = ..., explanation: _Optional[str] = ..., recommended_actions: _Optional[_Iterable[str]] = ..., severity: _Optional[str] = ...) -> None: ...

class GetCidadesSuportadasRequest(_message.Message):
    __slots__ = ("codigo_municipio",)
    CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    codigo_municipio: str
    def __init__(self, codigo_municipio: _Optional[str] = ...) -> None: ...

class CidadeSuportada(_message.Message):
    __slots__ = ("codigo_municipio", "nome", "uf", "provedor")
    CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    PROVEDOR_FIELD_NUMBER: _ClassVar[int]
    codigo_municipio: str
    nome: str
    uf: str
    provedor: str
    def __init__(self, codigo_municipio: _Optional[str] = ..., nome: _Optional[str] = ..., uf: _Optional[str] = ..., provedor: _Optional[str] = ...) -> None: ...

class GetCidadesSuportadasResponse(_message.Message):
    __slots__ = ("cidades",)
    CIDADES_FIELD_NUMBER: _ClassVar[int]
    cidades: _containers.RepeatedCompositeFieldContainer[CidadeSuportada]
    def __init__(self, cidades: _Optional[_Iterable[_Union[CidadeSuportada, _Mapping]]] = ...) -> None: ...

class Tomador(_message.Message):
    __slots__ = ("id", "cpf_cnpj", "nome", "im", "email", "fone", "endereco", "nif", "codigo_pais", "endereco_exterior")
    class Endereco(_message.Message):
        __slots__ = ("logradouro", "numero", "bairro", "codigo_municipio", "municipio", "uf", "cep", "complemento")
        LOGRADOURO_FIELD_NUMBER: _ClassVar[int]
        NUMERO_FIELD_NUMBER: _ClassVar[int]
        BAIRRO_FIELD_NUMBER: _ClassVar[int]
        CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
        MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
        UF_FIELD_NUMBER: _ClassVar[int]
        CEP_FIELD_NUMBER: _ClassVar[int]
        COMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
        logradouro: str
        numero: str
        bairro: str
        codigo_municipio: str
        municipio: str
        uf: str
        cep: str
        complemento: str
        def __init__(self, logradouro: _Optional[str] = ..., numero: _Optional[str] = ..., bairro: _Optional[str] = ..., codigo_municipio: _Optional[str] = ..., municipio: _Optional[str] = ..., uf: _Optional[str] = ..., cep: _Optional[str] = ..., complemento: _Optional[str] = ...) -> None: ...
    class EnderecoExterior(_message.Message):
        __slots__ = ("codigo_pais", "endereco_completo")
        CODIGO_PAIS_FIELD_NUMBER: _ClassVar[int]
        ENDERECO_COMPLETO_FIELD_NUMBER: _ClassVar[int]
        codigo_pais: str
        endereco_completo: str
        def __init__(self, codigo_pais: _Optional[str] = ..., endereco_completo: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    IM_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FONE_FIELD_NUMBER: _ClassVar[int]
    ENDERECO_FIELD_NUMBER: _ClassVar[int]
    NIF_FIELD_NUMBER: _ClassVar[int]
    CODIGO_PAIS_FIELD_NUMBER: _ClassVar[int]
    ENDERECO_EXTERIOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    cpf_cnpj: str
    nome: str
    im: str
    email: str
    fone: str
    endereco: Tomador.Endereco
    nif: str
    codigo_pais: str
    endereco_exterior: Tomador.EnderecoExterior
    def __init__(self, id: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., nome: _Optional[str] = ..., im: _Optional[str] = ..., email: _Optional[str] = ..., fone: _Optional[str] = ..., endereco: _Optional[_Union[Tomador.Endereco, _Mapping]] = ..., nif: _Optional[str] = ..., codigo_pais: _Optional[str] = ..., endereco_exterior: _Optional[_Union[Tomador.EnderecoExterior, _Mapping]] = ...) -> None: ...

class Intermediario(_message.Message):
    __slots__ = ("cpf_cnpj", "inscricao_municipal", "razao_social", "localizacao_uf", "localizacao_cidade")
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    INSCRICAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    RAZAO_SOCIAL_FIELD_NUMBER: _ClassVar[int]
    LOCALIZACAO_UF_FIELD_NUMBER: _ClassVar[int]
    LOCALIZACAO_CIDADE_FIELD_NUMBER: _ClassVar[int]
    cpf_cnpj: str
    inscricao_municipal: str
    razao_social: str
    localizacao_uf: str
    localizacao_cidade: str
    def __init__(self, cpf_cnpj: _Optional[str] = ..., inscricao_municipal: _Optional[str] = ..., razao_social: _Optional[str] = ..., localizacao_uf: _Optional[str] = ..., localizacao_cidade: _Optional[str] = ...) -> None: ...

class NotaSubstituta(_message.Message):
    __slots__ = ("e_substituidora", "chave_nota_substituida", "motivo_substituicao", "nfse_id_substituida", "numero_nfse_substituida")
    E_SUBSTITUIDORA_FIELD_NUMBER: _ClassVar[int]
    CHAVE_NOTA_SUBSTITUIDA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_SUBSTITUICAO_FIELD_NUMBER: _ClassVar[int]
    NFSE_ID_SUBSTITUIDA_FIELD_NUMBER: _ClassVar[int]
    NUMERO_NFSE_SUBSTITUIDA_FIELD_NUMBER: _ClassVar[int]
    e_substituidora: bool
    chave_nota_substituida: str
    motivo_substituicao: str
    nfse_id_substituida: str
    numero_nfse_substituida: str
    def __init__(self, e_substituidora: _Optional[bool] = ..., chave_nota_substituida: _Optional[str] = ..., motivo_substituicao: _Optional[str] = ..., nfse_id_substituida: _Optional[str] = ..., numero_nfse_substituida: _Optional[str] = ...) -> None: ...

class NotaSubstituida(_message.Message):
    __slots__ = ("nfse_id_substituta", "chave_nfse_substituta", "numero_nfse_substituta", "data_substituicao")
    NFSE_ID_SUBSTITUTA_FIELD_NUMBER: _ClassVar[int]
    CHAVE_NFSE_SUBSTITUTA_FIELD_NUMBER: _ClassVar[int]
    NUMERO_NFSE_SUBSTITUTA_FIELD_NUMBER: _ClassVar[int]
    DATA_SUBSTITUICAO_FIELD_NUMBER: _ClassVar[int]
    nfse_id_substituta: str
    chave_nfse_substituta: str
    numero_nfse_substituta: str
    data_substituicao: _timestamp_pb2.Timestamp
    def __init__(self, nfse_id_substituta: _Optional[str] = ..., chave_nfse_substituta: _Optional[str] = ..., numero_nfse_substituta: _Optional[str] = ..., data_substituicao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MunicipioIncidencia(_message.Message):
    __slots__ = ("uf", "codigo_municipio", "nome_municipio")
    UF_FIELD_NUMBER: _ClassVar[int]
    CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    NOME_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    uf: str
    codigo_municipio: str
    nome_municipio: str
    def __init__(self, uf: _Optional[str] = ..., codigo_municipio: _Optional[str] = ..., nome_municipio: _Optional[str] = ...) -> None: ...

class Servico(_message.Message):
    __slots__ = ("id", "codigo_servico", "codigo_tributacao_nacional", "codigo_nbs", "descricao_servico", "cnae", "servico_nome", "servico_id", "un", "valor_unitario", "quantidade", "total", "impostos", "desconto_condicional", "desconto_incondicional", "valor_liquido_nfse", "codigo_tributacao_municipal")
    class Impostos(_message.Message):
        __slots__ = ("aliquota_iss", "valor_iss", "valor_csll", "valor_inss", "valor_pis", "valor_cofins", "valor_deducoes", "valor_ir", "iss_retido", "valor_iss_retido", "outras_retencoes", "base_calculo", "valor_cbs", "aliquota_cbs", "valor_ibs", "aliquota_ibs", "exigibilidade_iss", "numero_processo_suspensao")
        ALIQUOTA_ISS_FIELD_NUMBER: _ClassVar[int]
        VALOR_ISS_FIELD_NUMBER: _ClassVar[int]
        VALOR_CSLL_FIELD_NUMBER: _ClassVar[int]
        VALOR_INSS_FIELD_NUMBER: _ClassVar[int]
        VALOR_PIS_FIELD_NUMBER: _ClassVar[int]
        VALOR_COFINS_FIELD_NUMBER: _ClassVar[int]
        VALOR_DEDUCOES_FIELD_NUMBER: _ClassVar[int]
        VALOR_IR_FIELD_NUMBER: _ClassVar[int]
        ISS_RETIDO_FIELD_NUMBER: _ClassVar[int]
        VALOR_ISS_RETIDO_FIELD_NUMBER: _ClassVar[int]
        OUTRAS_RETENCOES_FIELD_NUMBER: _ClassVar[int]
        BASE_CALCULO_FIELD_NUMBER: _ClassVar[int]
        VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
        ALIQUOTA_CBS_FIELD_NUMBER: _ClassVar[int]
        VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
        ALIQUOTA_IBS_FIELD_NUMBER: _ClassVar[int]
        EXIGIBILIDADE_ISS_FIELD_NUMBER: _ClassVar[int]
        NUMERO_PROCESSO_SUSPENSAO_FIELD_NUMBER: _ClassVar[int]
        aliquota_iss: float
        valor_iss: float
        valor_csll: float
        valor_inss: float
        valor_pis: float
        valor_cofins: float
        valor_deducoes: float
        valor_ir: float
        iss_retido: bool
        valor_iss_retido: float
        outras_retencoes: float
        base_calculo: float
        valor_cbs: float
        aliquota_cbs: float
        valor_ibs: float
        aliquota_ibs: float
        exigibilidade_iss: ExigibilidadeISS
        numero_processo_suspensao: str
        def __init__(self, aliquota_iss: _Optional[float] = ..., valor_iss: _Optional[float] = ..., valor_csll: _Optional[float] = ..., valor_inss: _Optional[float] = ..., valor_pis: _Optional[float] = ..., valor_cofins: _Optional[float] = ..., valor_deducoes: _Optional[float] = ..., valor_ir: _Optional[float] = ..., iss_retido: _Optional[bool] = ..., valor_iss_retido: _Optional[float] = ..., outras_retencoes: _Optional[float] = ..., base_calculo: _Optional[float] = ..., valor_cbs: _Optional[float] = ..., aliquota_cbs: _Optional[float] = ..., valor_ibs: _Optional[float] = ..., aliquota_ibs: _Optional[float] = ..., exigibilidade_iss: _Optional[_Union[ExigibilidadeISS, str]] = ..., numero_processo_suspensao: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_SERVICO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_TRIBUTACAO_NACIONAL_FIELD_NUMBER: _ClassVar[int]
    CODIGO_NBS_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_SERVICO_FIELD_NUMBER: _ClassVar[int]
    CNAE_FIELD_NUMBER: _ClassVar[int]
    SERVICO_NOME_FIELD_NUMBER: _ClassVar[int]
    SERVICO_ID_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    IMPOSTOS_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_CONDICIONAL_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_INCONDICIONAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_LIQUIDO_NFSE_FIELD_NUMBER: _ClassVar[int]
    CODIGO_TRIBUTACAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo_servico: str
    codigo_tributacao_nacional: str
    codigo_nbs: str
    descricao_servico: str
    cnae: str
    servico_nome: str
    servico_id: str
    un: str
    valor_unitario: float
    quantidade: float
    total: float
    impostos: Servico.Impostos
    desconto_condicional: float
    desconto_incondicional: float
    valor_liquido_nfse: float
    codigo_tributacao_municipal: str
    def __init__(self, id: _Optional[str] = ..., codigo_servico: _Optional[str] = ..., codigo_tributacao_nacional: _Optional[str] = ..., codigo_nbs: _Optional[str] = ..., descricao_servico: _Optional[str] = ..., cnae: _Optional[str] = ..., servico_nome: _Optional[str] = ..., servico_id: _Optional[str] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., quantidade: _Optional[float] = ..., total: _Optional[float] = ..., impostos: _Optional[_Union[Servico.Impostos, _Mapping]] = ..., desconto_condicional: _Optional[float] = ..., desconto_incondicional: _Optional[float] = ..., valor_liquido_nfse: _Optional[float] = ..., codigo_tributacao_municipal: _Optional[str] = ...) -> None: ...

class EventoNfse(_message.Message):
    __slots__ = ("id", "created_at", "user_id", "user_name", "tipo", "codigo", "descricao", "mensagem")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tipo: TipoEventoNfse
    codigo: str
    descricao: str
    mensagem: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tipo: _Optional[_Union[TipoEventoNfse, str]] = ..., codigo: _Optional[str] = ..., descricao: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class Nfse(_message.Message):
    __slots__ = ("id", "numero", "situacao", "fields", "ambiente", "data_hora_emissao", "data_competencia", "natureza_operacao", "emitente", "tomador", "local_prestacao", "incentivo_cultural", "numero_nota_substituta", "optante_simples_nacional", "regime_especial", "reg_ap_trib_sn", "impostos", "desconto_incondicional", "subtotal", "total", "servicos", "construcao_civil", "obs", "xml_lote_envio", "xml_autorizacao", "chave_acesso", "rps", "codigo_verificacao", "url_provedor", "url_pdf", "cancelamento", "rejeicoes", "data_hora_autorizacao", "sem_tomador", "intermediario", "subempreitada", "comprovacao_material", "nota_substituta", "nota_substituida", "municipio_incidencia", "ibs_cbs_habilitado", "serie", "importado_em", "ibscbs", "eventos")
    class LocalDePrestacao(_message.Message):
        __slots__ = ("exterior", "uf", "cidade", "cidade_codigo", "codigo_pais")
        EXTERIOR_FIELD_NUMBER: _ClassVar[int]
        UF_FIELD_NUMBER: _ClassVar[int]
        CIDADE_FIELD_NUMBER: _ClassVar[int]
        CIDADE_CODIGO_FIELD_NUMBER: _ClassVar[int]
        CODIGO_PAIS_FIELD_NUMBER: _ClassVar[int]
        exterior: bool
        uf: str
        cidade: str
        cidade_codigo: str
        codigo_pais: str
        def __init__(self, exterior: _Optional[bool] = ..., uf: _Optional[str] = ..., cidade: _Optional[str] = ..., cidade_codigo: _Optional[str] = ..., codigo_pais: _Optional[str] = ...) -> None: ...
    class Impostos(_message.Message):
        __slots__ = ("base_calculo", "iss_percentual", "iss_valor", "iss_reter", "inss", "cofins", "irrf", "pis_pasep", "csll", "outras_retencoes", "deducoes", "credito", "irpj", "valor_cbs", "aliquota_cbs", "valor_ibs", "aliquota_ibs", "valor_iss_retido")
        BASE_CALCULO_FIELD_NUMBER: _ClassVar[int]
        ISS_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
        ISS_VALOR_FIELD_NUMBER: _ClassVar[int]
        ISS_RETER_FIELD_NUMBER: _ClassVar[int]
        INSS_FIELD_NUMBER: _ClassVar[int]
        COFINS_FIELD_NUMBER: _ClassVar[int]
        IRRF_FIELD_NUMBER: _ClassVar[int]
        PIS_PASEP_FIELD_NUMBER: _ClassVar[int]
        CSLL_FIELD_NUMBER: _ClassVar[int]
        OUTRAS_RETENCOES_FIELD_NUMBER: _ClassVar[int]
        DEDUCOES_FIELD_NUMBER: _ClassVar[int]
        CREDITO_FIELD_NUMBER: _ClassVar[int]
        IRPJ_FIELD_NUMBER: _ClassVar[int]
        VALOR_CBS_FIELD_NUMBER: _ClassVar[int]
        ALIQUOTA_CBS_FIELD_NUMBER: _ClassVar[int]
        VALOR_IBS_FIELD_NUMBER: _ClassVar[int]
        ALIQUOTA_IBS_FIELD_NUMBER: _ClassVar[int]
        VALOR_ISS_RETIDO_FIELD_NUMBER: _ClassVar[int]
        base_calculo: float
        iss_percentual: float
        iss_valor: float
        iss_reter: bool
        inss: float
        cofins: float
        irrf: float
        pis_pasep: float
        csll: float
        outras_retencoes: float
        deducoes: float
        credito: float
        irpj: float
        valor_cbs: float
        aliquota_cbs: float
        valor_ibs: float
        aliquota_ibs: float
        valor_iss_retido: float
        def __init__(self, base_calculo: _Optional[float] = ..., iss_percentual: _Optional[float] = ..., iss_valor: _Optional[float] = ..., iss_reter: _Optional[bool] = ..., inss: _Optional[float] = ..., cofins: _Optional[float] = ..., irrf: _Optional[float] = ..., pis_pasep: _Optional[float] = ..., csll: _Optional[float] = ..., outras_retencoes: _Optional[float] = ..., deducoes: _Optional[float] = ..., credito: _Optional[float] = ..., irpj: _Optional[float] = ..., valor_cbs: _Optional[float] = ..., aliquota_cbs: _Optional[float] = ..., valor_ibs: _Optional[float] = ..., aliquota_ibs: _Optional[float] = ..., valor_iss_retido: _Optional[float] = ...) -> None: ...
    class ConstrucaoCivil(_message.Message):
        __slots__ = ("codigo_obra", "codigo_art")
        CODIGO_OBRA_FIELD_NUMBER: _ClassVar[int]
        CODIGO_ART_FIELD_NUMBER: _ClassVar[int]
        codigo_obra: str
        codigo_art: str
        def __init__(self, codigo_obra: _Optional[str] = ..., codigo_art: _Optional[str] = ...) -> None: ...
    class LoteRps(_message.Message):
        __slots__ = ("protocolo", "data_hora_envio", "data_hora_processamento", "numero_lote", "numero_rps", "serie")
        PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
        DATA_HORA_ENVIO_FIELD_NUMBER: _ClassVar[int]
        DATA_HORA_PROCESSAMENTO_FIELD_NUMBER: _ClassVar[int]
        NUMERO_LOTE_FIELD_NUMBER: _ClassVar[int]
        NUMERO_RPS_FIELD_NUMBER: _ClassVar[int]
        SERIE_FIELD_NUMBER: _ClassVar[int]
        protocolo: str
        data_hora_envio: _timestamp_pb2.Timestamp
        data_hora_processamento: _timestamp_pb2.Timestamp
        numero_lote: str
        numero_rps: str
        serie: str
        def __init__(self, protocolo: _Optional[str] = ..., data_hora_envio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_processamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., numero_lote: _Optional[str] = ..., numero_rps: _Optional[str] = ..., serie: _Optional[str] = ...) -> None: ...
    class Cancelamento(_message.Message):
        __slots__ = ("codigo", "motivo", "data_hora")
        CODIGO_FIELD_NUMBER: _ClassVar[int]
        MOTIVO_FIELD_NUMBER: _ClassVar[int]
        DATA_HORA_FIELD_NUMBER: _ClassVar[int]
        codigo: CodigoCancelamento
        motivo: str
        data_hora: _timestamp_pb2.Timestamp
        def __init__(self, codigo: _Optional[_Union[CodigoCancelamento, str]] = ..., motivo: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Rejeicao(_message.Message):
        __slots__ = ("id", "data_hora", "codigo", "mensagem", "correcao", "operacao")
        ID_FIELD_NUMBER: _ClassVar[int]
        DATA_HORA_FIELD_NUMBER: _ClassVar[int]
        CODIGO_FIELD_NUMBER: _ClassVar[int]
        MENSAGEM_FIELD_NUMBER: _ClassVar[int]
        CORRECAO_FIELD_NUMBER: _ClassVar[int]
        OPERACAO_FIELD_NUMBER: _ClassVar[int]
        id: str
        data_hora: _timestamp_pb2.Timestamp
        codigo: str
        mensagem: str
        correcao: str
        operacao: TipoOperacaoRejeicao
        def __init__(self, id: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., codigo: _Optional[str] = ..., mensagem: _Optional[str] = ..., correcao: _Optional[str] = ..., operacao: _Optional[_Union[TipoOperacaoRejeicao, str]] = ...) -> None: ...
    class IBSCBS(_message.Message):
        __slots__ = ("fin_nfse", "ind_final", "c_ind_op", "tp_oper", "ref_nfse", "tp_ente_gov", "x_tp_ente_gov", "ind_dest", "dest", "adq", "imovel", "valores")
        class Destinatario(_message.Message):
            __slots__ = ("cnpj", "cpf", "inscricao_municipal", "nif", "c_nao_nif", "nome", "endereco", "fone", "email")
            CNPJ_FIELD_NUMBER: _ClassVar[int]
            CPF_FIELD_NUMBER: _ClassVar[int]
            INSCRICAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
            NIF_FIELD_NUMBER: _ClassVar[int]
            C_NAO_NIF_FIELD_NUMBER: _ClassVar[int]
            NOME_FIELD_NUMBER: _ClassVar[int]
            ENDERECO_FIELD_NUMBER: _ClassVar[int]
            FONE_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            cnpj: str
            cpf: str
            inscricao_municipal: str
            nif: str
            c_nao_nif: int
            nome: str
            endereco: Tomador.Endereco
            fone: str
            email: str
            def __init__(self, cnpj: _Optional[str] = ..., cpf: _Optional[str] = ..., inscricao_municipal: _Optional[str] = ..., nif: _Optional[str] = ..., c_nao_nif: _Optional[int] = ..., nome: _Optional[str] = ..., endereco: _Optional[_Union[Tomador.Endereco, _Mapping]] = ..., fone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
        class Adquirente(_message.Message):
            __slots__ = ("cnpj", "cpf", "nif", "c_nao_nif", "nome", "endereco", "fone", "email")
            CNPJ_FIELD_NUMBER: _ClassVar[int]
            CPF_FIELD_NUMBER: _ClassVar[int]
            NIF_FIELD_NUMBER: _ClassVar[int]
            C_NAO_NIF_FIELD_NUMBER: _ClassVar[int]
            NOME_FIELD_NUMBER: _ClassVar[int]
            ENDERECO_FIELD_NUMBER: _ClassVar[int]
            FONE_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            cnpj: str
            cpf: str
            nif: str
            c_nao_nif: int
            nome: str
            endereco: Tomador.Endereco
            fone: str
            email: str
            def __init__(self, cnpj: _Optional[str] = ..., cpf: _Optional[str] = ..., nif: _Optional[str] = ..., c_nao_nif: _Optional[int] = ..., nome: _Optional[str] = ..., endereco: _Optional[_Union[Tomador.Endereco, _Mapping]] = ..., fone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
        class Imovel(_message.Message):
            __slots__ = ("insc_imob_fisc", "c_cib", "endereco")
            INSC_IMOB_FISC_FIELD_NUMBER: _ClassVar[int]
            C_CIB_FIELD_NUMBER: _ClassVar[int]
            ENDERECO_FIELD_NUMBER: _ClassVar[int]
            insc_imob_fisc: str
            c_cib: str
            endereco: Tomador.Endereco
            def __init__(self, insc_imob_fisc: _Optional[str] = ..., c_cib: _Optional[str] = ..., endereco: _Optional[_Union[Tomador.Endereco, _Mapping]] = ...) -> None: ...
        class ValoresIBSCBS(_message.Message):
            __slots__ = ("g_ree_rep_res", "trib")
            class ReeRepRes(_message.Message):
                __slots__ = ("documentos",)
                class Documento(_message.Message):
                    __slots__ = ("tipo_chave_dfe", "x_tipo_chave_dfe", "chave_dfe", "c_mun_doc_fiscal", "n_doc_fiscal", "x_doc_fiscal", "n_doc", "x_doc", "fornecedor_cnpj", "fornecedor_cpf", "fornecedor_nome", "dt_emi_doc", "dt_comp_doc", "tp_ree_rep_res", "x_tp_ree_rep_res", "vlr_ree_rep_res")
                    TIPO_CHAVE_DFE_FIELD_NUMBER: _ClassVar[int]
                    X_TIPO_CHAVE_DFE_FIELD_NUMBER: _ClassVar[int]
                    CHAVE_DFE_FIELD_NUMBER: _ClassVar[int]
                    C_MUN_DOC_FISCAL_FIELD_NUMBER: _ClassVar[int]
                    N_DOC_FISCAL_FIELD_NUMBER: _ClassVar[int]
                    X_DOC_FISCAL_FIELD_NUMBER: _ClassVar[int]
                    N_DOC_FIELD_NUMBER: _ClassVar[int]
                    X_DOC_FIELD_NUMBER: _ClassVar[int]
                    FORNECEDOR_CNPJ_FIELD_NUMBER: _ClassVar[int]
                    FORNECEDOR_CPF_FIELD_NUMBER: _ClassVar[int]
                    FORNECEDOR_NOME_FIELD_NUMBER: _ClassVar[int]
                    DT_EMI_DOC_FIELD_NUMBER: _ClassVar[int]
                    DT_COMP_DOC_FIELD_NUMBER: _ClassVar[int]
                    TP_REE_REP_RES_FIELD_NUMBER: _ClassVar[int]
                    X_TP_REE_REP_RES_FIELD_NUMBER: _ClassVar[int]
                    VLR_REE_REP_RES_FIELD_NUMBER: _ClassVar[int]
                    tipo_chave_dfe: int
                    x_tipo_chave_dfe: str
                    chave_dfe: str
                    c_mun_doc_fiscal: str
                    n_doc_fiscal: str
                    x_doc_fiscal: str
                    n_doc: str
                    x_doc: str
                    fornecedor_cnpj: str
                    fornecedor_cpf: str
                    fornecedor_nome: str
                    dt_emi_doc: str
                    dt_comp_doc: str
                    tp_ree_rep_res: int
                    x_tp_ree_rep_res: str
                    vlr_ree_rep_res: float
                    def __init__(self, tipo_chave_dfe: _Optional[int] = ..., x_tipo_chave_dfe: _Optional[str] = ..., chave_dfe: _Optional[str] = ..., c_mun_doc_fiscal: _Optional[str] = ..., n_doc_fiscal: _Optional[str] = ..., x_doc_fiscal: _Optional[str] = ..., n_doc: _Optional[str] = ..., x_doc: _Optional[str] = ..., fornecedor_cnpj: _Optional[str] = ..., fornecedor_cpf: _Optional[str] = ..., fornecedor_nome: _Optional[str] = ..., dt_emi_doc: _Optional[str] = ..., dt_comp_doc: _Optional[str] = ..., tp_ree_rep_res: _Optional[int] = ..., x_tp_ree_rep_res: _Optional[str] = ..., vlr_ree_rep_res: _Optional[float] = ...) -> None: ...
                DOCUMENTOS_FIELD_NUMBER: _ClassVar[int]
                documentos: _containers.RepeatedCompositeFieldContainer[Nfse.IBSCBS.ValoresIBSCBS.ReeRepRes.Documento]
                def __init__(self, documentos: _Optional[_Iterable[_Union[Nfse.IBSCBS.ValoresIBSCBS.ReeRepRes.Documento, _Mapping]]] = ...) -> None: ...
            class TributosIBSCBS(_message.Message):
                __slots__ = ("cst", "c_class_trib", "c_cred_pres", "g_trib_regular", "g_dif")
                class TribRegular(_message.Message):
                    __slots__ = ("cst_reg", "c_class_trib_reg")
                    CST_REG_FIELD_NUMBER: _ClassVar[int]
                    C_CLASS_TRIB_REG_FIELD_NUMBER: _ClassVar[int]
                    cst_reg: str
                    c_class_trib_reg: str
                    def __init__(self, cst_reg: _Optional[str] = ..., c_class_trib_reg: _Optional[str] = ...) -> None: ...
                class Diferimento(_message.Message):
                    __slots__ = ("p_dif_uf", "p_dif_mun", "p_dif_cbs")
                    P_DIF_UF_FIELD_NUMBER: _ClassVar[int]
                    P_DIF_MUN_FIELD_NUMBER: _ClassVar[int]
                    P_DIF_CBS_FIELD_NUMBER: _ClassVar[int]
                    p_dif_uf: float
                    p_dif_mun: float
                    p_dif_cbs: float
                    def __init__(self, p_dif_uf: _Optional[float] = ..., p_dif_mun: _Optional[float] = ..., p_dif_cbs: _Optional[float] = ...) -> None: ...
                CST_FIELD_NUMBER: _ClassVar[int]
                C_CLASS_TRIB_FIELD_NUMBER: _ClassVar[int]
                C_CRED_PRES_FIELD_NUMBER: _ClassVar[int]
                G_TRIB_REGULAR_FIELD_NUMBER: _ClassVar[int]
                G_DIF_FIELD_NUMBER: _ClassVar[int]
                cst: str
                c_class_trib: str
                c_cred_pres: str
                g_trib_regular: Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS.TribRegular
                g_dif: Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS.Diferimento
                def __init__(self, cst: _Optional[str] = ..., c_class_trib: _Optional[str] = ..., c_cred_pres: _Optional[str] = ..., g_trib_regular: _Optional[_Union[Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS.TribRegular, _Mapping]] = ..., g_dif: _Optional[_Union[Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS.Diferimento, _Mapping]] = ...) -> None: ...
            G_REE_REP_RES_FIELD_NUMBER: _ClassVar[int]
            TRIB_FIELD_NUMBER: _ClassVar[int]
            g_ree_rep_res: Nfse.IBSCBS.ValoresIBSCBS.ReeRepRes
            trib: Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS
            def __init__(self, g_ree_rep_res: _Optional[_Union[Nfse.IBSCBS.ValoresIBSCBS.ReeRepRes, _Mapping]] = ..., trib: _Optional[_Union[Nfse.IBSCBS.ValoresIBSCBS.TributosIBSCBS, _Mapping]] = ...) -> None: ...
        FIN_NFSE_FIELD_NUMBER: _ClassVar[int]
        IND_FINAL_FIELD_NUMBER: _ClassVar[int]
        C_IND_OP_FIELD_NUMBER: _ClassVar[int]
        TP_OPER_FIELD_NUMBER: _ClassVar[int]
        REF_NFSE_FIELD_NUMBER: _ClassVar[int]
        TP_ENTE_GOV_FIELD_NUMBER: _ClassVar[int]
        X_TP_ENTE_GOV_FIELD_NUMBER: _ClassVar[int]
        IND_DEST_FIELD_NUMBER: _ClassVar[int]
        DEST_FIELD_NUMBER: _ClassVar[int]
        ADQ_FIELD_NUMBER: _ClassVar[int]
        IMOVEL_FIELD_NUMBER: _ClassVar[int]
        VALORES_FIELD_NUMBER: _ClassVar[int]
        fin_nfse: int
        ind_final: int
        c_ind_op: str
        tp_oper: int
        ref_nfse: _containers.RepeatedScalarFieldContainer[str]
        tp_ente_gov: int
        x_tp_ente_gov: str
        ind_dest: int
        dest: Nfse.IBSCBS.Destinatario
        adq: Nfse.IBSCBS.Adquirente
        imovel: Nfse.IBSCBS.Imovel
        valores: Nfse.IBSCBS.ValoresIBSCBS
        def __init__(self, fin_nfse: _Optional[int] = ..., ind_final: _Optional[int] = ..., c_ind_op: _Optional[str] = ..., tp_oper: _Optional[int] = ..., ref_nfse: _Optional[_Iterable[str]] = ..., tp_ente_gov: _Optional[int] = ..., x_tp_ente_gov: _Optional[str] = ..., ind_dest: _Optional[int] = ..., dest: _Optional[_Union[Nfse.IBSCBS.Destinatario, _Mapping]] = ..., adq: _Optional[_Union[Nfse.IBSCBS.Adquirente, _Mapping]] = ..., imovel: _Optional[_Union[Nfse.IBSCBS.Imovel, _Mapping]] = ..., valores: _Optional[_Union[Nfse.IBSCBS.ValoresIBSCBS, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATA_COMPETENCIA_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    EMITENTE_FIELD_NUMBER: _ClassVar[int]
    TOMADOR_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PRESTACAO_FIELD_NUMBER: _ClassVar[int]
    INCENTIVO_CULTURAL_FIELD_NUMBER: _ClassVar[int]
    NUMERO_NOTA_SUBSTITUTA_FIELD_NUMBER: _ClassVar[int]
    OPTANTE_SIMPLES_NACIONAL_FIELD_NUMBER: _ClassVar[int]
    REGIME_ESPECIAL_FIELD_NUMBER: _ClassVar[int]
    REG_AP_TRIB_SN_FIELD_NUMBER: _ClassVar[int]
    IMPOSTOS_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_INCONDICIONAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    SERVICOS_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCAO_CIVIL_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    XML_LOTE_ENVIO_FIELD_NUMBER: _ClassVar[int]
    XML_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_ACESSO_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_VERIFICACAO_FIELD_NUMBER: _ClassVar[int]
    URL_PROVEDOR_FIELD_NUMBER: _ClassVar[int]
    URL_PDF_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    SEM_TOMADOR_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARIO_FIELD_NUMBER: _ClassVar[int]
    SUBEMPREITADA_FIELD_NUMBER: _ClassVar[int]
    COMPROVACAO_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    NOTA_SUBSTITUTA_FIELD_NUMBER: _ClassVar[int]
    NOTA_SUBSTITUIDA_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_INCIDENCIA_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    IMPORTADO_EM_FIELD_NUMBER: _ClassVar[int]
    IBSCBS_FIELD_NUMBER: _ClassVar[int]
    EVENTOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero: str
    situacao: Situacao
    fields: _metadata_pb2.BasicFields
    ambiente: Ambiente
    data_hora_emissao: _timestamp_pb2.Timestamp
    data_competencia: _timestamp_pb2.Timestamp
    natureza_operacao: NaturezaDaOperacao
    emitente: _emitente_pb2.Emitente
    tomador: Tomador
    local_prestacao: Nfse.LocalDePrestacao
    incentivo_cultural: bool
    numero_nota_substituta: bool
    optante_simples_nacional: bool
    regime_especial: RegimeEspecial
    reg_ap_trib_sn: RegimeApuracaoSN
    impostos: Nfse.Impostos
    desconto_incondicional: float
    subtotal: float
    total: float
    servicos: _containers.RepeatedCompositeFieldContainer[Servico]
    construcao_civil: Nfse.ConstrucaoCivil
    obs: str
    xml_lote_envio: str
    xml_autorizacao: str
    chave_acesso: str
    rps: Nfse.LoteRps
    codigo_verificacao: str
    url_provedor: str
    url_pdf: str
    cancelamento: Nfse.Cancelamento
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Nfse.Rejeicao]
    data_hora_autorizacao: _timestamp_pb2.Timestamp
    sem_tomador: bool
    intermediario: Intermediario
    subempreitada: bool
    comprovacao_material: bool
    nota_substituta: NotaSubstituta
    nota_substituida: NotaSubstituida
    municipio_incidencia: MunicipioIncidencia
    ibs_cbs_habilitado: bool
    serie: str
    importado_em: _timestamp_pb2.Timestamp
    ibscbs: Nfse.IBSCBS
    eventos: _containers.RepeatedCompositeFieldContainer[EventoNfse]
    def __init__(self, id: _Optional[str] = ..., numero: _Optional[str] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., ambiente: _Optional[_Union[Ambiente, str]] = ..., data_hora_emissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_competencia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., natureza_operacao: _Optional[_Union[NaturezaDaOperacao, str]] = ..., emitente: _Optional[_Union[_emitente_pb2.Emitente, _Mapping]] = ..., tomador: _Optional[_Union[Tomador, _Mapping]] = ..., local_prestacao: _Optional[_Union[Nfse.LocalDePrestacao, _Mapping]] = ..., incentivo_cultural: _Optional[bool] = ..., numero_nota_substituta: _Optional[bool] = ..., optante_simples_nacional: _Optional[bool] = ..., regime_especial: _Optional[_Union[RegimeEspecial, str]] = ..., reg_ap_trib_sn: _Optional[_Union[RegimeApuracaoSN, str]] = ..., impostos: _Optional[_Union[Nfse.Impostos, _Mapping]] = ..., desconto_incondicional: _Optional[float] = ..., subtotal: _Optional[float] = ..., total: _Optional[float] = ..., servicos: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ..., construcao_civil: _Optional[_Union[Nfse.ConstrucaoCivil, _Mapping]] = ..., obs: _Optional[str] = ..., xml_lote_envio: _Optional[str] = ..., xml_autorizacao: _Optional[str] = ..., chave_acesso: _Optional[str] = ..., rps: _Optional[_Union[Nfse.LoteRps, _Mapping]] = ..., codigo_verificacao: _Optional[str] = ..., url_provedor: _Optional[str] = ..., url_pdf: _Optional[str] = ..., cancelamento: _Optional[_Union[Nfse.Cancelamento, _Mapping]] = ..., rejeicoes: _Optional[_Iterable[_Union[Nfse.Rejeicao, _Mapping]]] = ..., data_hora_autorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sem_tomador: _Optional[bool] = ..., intermediario: _Optional[_Union[Intermediario, _Mapping]] = ..., subempreitada: _Optional[bool] = ..., comprovacao_material: _Optional[bool] = ..., nota_substituta: _Optional[_Union[NotaSubstituta, _Mapping]] = ..., nota_substituida: _Optional[_Union[NotaSubstituida, _Mapping]] = ..., municipio_incidencia: _Optional[_Union[MunicipioIncidencia, _Mapping]] = ..., ibs_cbs_habilitado: _Optional[bool] = ..., serie: _Optional[str] = ..., importado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ibscbs: _Optional[_Union[Nfse.IBSCBS, _Mapping]] = ..., eventos: _Optional[_Iterable[_Union[EventoNfse, _Mapping]]] = ...) -> None: ...

class EmitirNfseRequest(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class EmitirNfseResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class CancelarNfseRequest(_message.Message):
    __slots__ = ("id", "codigo_cancelamento", "motivo_cancelamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo_cancelamento: CodigoCancelamento
    motivo_cancelamento: str
    def __init__(self, id: _Optional[str] = ..., codigo_cancelamento: _Optional[_Union[CodigoCancelamento, str]] = ..., motivo_cancelamento: _Optional[str] = ...) -> None: ...

class CancelarNfseResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class SubstituirNfseRequest(_message.Message):
    __slots__ = ("nfse_id_original", "nova_nfse", "codigo_motivo", "descricao_motivo")
    NFSE_ID_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    NOVA_NFSE_FIELD_NUMBER: _ClassVar[int]
    CODIGO_MOTIVO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_MOTIVO_FIELD_NUMBER: _ClassVar[int]
    nfse_id_original: str
    nova_nfse: Nfse
    codigo_motivo: CodigoMotivoSubstituicao
    descricao_motivo: str
    def __init__(self, nfse_id_original: _Optional[str] = ..., nova_nfse: _Optional[_Union[Nfse, _Mapping]] = ..., codigo_motivo: _Optional[_Union[CodigoMotivoSubstituicao, str]] = ..., descricao_motivo: _Optional[str] = ...) -> None: ...

class SubstituirNfseResponse(_message.Message):
    __slots__ = ("nfse_original", "nfse_nova", "mensagem")
    NFSE_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    NFSE_NOVA_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nfse_original: Nfse
    nfse_nova: Nfse
    mensagem: str
    def __init__(self, nfse_original: _Optional[_Union[Nfse, _Mapping]] = ..., nfse_nova: _Optional[_Union[Nfse, _Mapping]] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ConsultarLoteRequest(_message.Message):
    __slots__ = ("emitente", "ambiente", "protocolo", "id")
    EMITENTE_FIELD_NUMBER: _ClassVar[int]
    AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    emitente: _emitente_pb2.Emitente
    ambiente: Ambiente
    protocolo: str
    id: str
    def __init__(self, emitente: _Optional[_Union[_emitente_pb2.Emitente, _Mapping]] = ..., ambiente: _Optional[_Union[Ambiente, str]] = ..., protocolo: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ConsultarLoteResponse(_message.Message):
    __slots__ = ("nfse", "mensagens_erro")
    class Mensagens(_message.Message):
        __slots__ = ("codigo", "codigo_provedor", "mensagem", "correcao")
        class CodigoConsultaLote(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CODIGO_CONSULTA_LOTE_DESCONHECIDO: _ClassVar[ConsultarLoteResponse.Mensagens.CodigoConsultaLote]
            CODIGO_CONSULTA_LOTE_EM_PROCESSAMENTO: _ClassVar[ConsultarLoteResponse.Mensagens.CodigoConsultaLote]
            CODIGO_CONSULTA_LOTE_EM_NFSE_JA_EMITIDA: _ClassVar[ConsultarLoteResponse.Mensagens.CodigoConsultaLote]
            CODIGO_CONSULTA_LOTE_NAO_ENCONTRADO: _ClassVar[ConsultarLoteResponse.Mensagens.CodigoConsultaLote]
        CODIGO_CONSULTA_LOTE_DESCONHECIDO: ConsultarLoteResponse.Mensagens.CodigoConsultaLote
        CODIGO_CONSULTA_LOTE_EM_PROCESSAMENTO: ConsultarLoteResponse.Mensagens.CodigoConsultaLote
        CODIGO_CONSULTA_LOTE_EM_NFSE_JA_EMITIDA: ConsultarLoteResponse.Mensagens.CodigoConsultaLote
        CODIGO_CONSULTA_LOTE_NAO_ENCONTRADO: ConsultarLoteResponse.Mensagens.CodigoConsultaLote
        CODIGO_FIELD_NUMBER: _ClassVar[int]
        CODIGO_PROVEDOR_FIELD_NUMBER: _ClassVar[int]
        MENSAGEM_FIELD_NUMBER: _ClassVar[int]
        CORRECAO_FIELD_NUMBER: _ClassVar[int]
        codigo: ConsultarLoteResponse.Mensagens.CodigoConsultaLote
        codigo_provedor: str
        mensagem: str
        correcao: str
        def __init__(self, codigo: _Optional[_Union[ConsultarLoteResponse.Mensagens.CodigoConsultaLote, str]] = ..., codigo_provedor: _Optional[str] = ..., mensagem: _Optional[str] = ..., correcao: _Optional[str] = ...) -> None: ...
    NFSE_FIELD_NUMBER: _ClassVar[int]
    MENSAGENS_ERRO_FIELD_NUMBER: _ClassVar[int]
    nfse: _containers.RepeatedCompositeFieldContainer[Nfse]
    mensagens_erro: _containers.RepeatedCompositeFieldContainer[ConsultarLoteResponse.Mensagens]
    def __init__(self, nfse: _Optional[_Iterable[_Union[Nfse, _Mapping]]] = ..., mensagens_erro: _Optional[_Iterable[_Union[ConsultarLoteResponse.Mensagens, _Mapping]]] = ...) -> None: ...

class ConsultaNfseRequest(_message.Message):
    __slots__ = ("id", "numero_rps", "serie", "cnpj_prestador", "inscricao_municipal", "codigo_municipio")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_RPS_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    CNPJ_PRESTADOR_FIELD_NUMBER: _ClassVar[int]
    INSCRICAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero_rps: str
    serie: str
    cnpj_prestador: str
    inscricao_municipal: str
    codigo_municipio: str
    def __init__(self, id: _Optional[str] = ..., numero_rps: _Optional[str] = ..., serie: _Optional[str] = ..., cnpj_prestador: _Optional[str] = ..., inscricao_municipal: _Optional[str] = ..., codigo_municipio: _Optional[str] = ...) -> None: ...

class ConsultaNfseResponse(_message.Message):
    __slots__ = ("mensagem", "nfse")
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    nfse: Nfse
    def __init__(self, mensagem: _Optional[str] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class CreateNfseRequest(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class CreateNfseResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class UpdateNfseRequest(_message.Message):
    __slots__ = ("id", "nfse", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    nfse: Nfse
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNfseResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class DeleteNfseRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteNfseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloneNfseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneNfseResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class ListNfseRequest(_message.Message):
    __slots__ = ("ids", "situacao", "data_hora_emissao_gte", "data_hora_emissao_lte", "filter", "data_competencia_gte", "data_competencia_lte", "total_gte", "total_lte")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_GTE_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DATA_COMPETENCIA_GTE_FIELD_NUMBER: _ClassVar[int]
    DATA_COMPETENCIA_LTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LTE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    situacao: _containers.RepeatedScalarFieldContainer[Situacao]
    data_hora_emissao_gte: _timestamp_pb2.Timestamp
    data_hora_emissao_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    data_competencia_gte: _timestamp_pb2.Timestamp
    data_competencia_lte: _timestamp_pb2.Timestamp
    total_gte: float
    total_lte: float
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., situacao: _Optional[_Iterable[_Union[Situacao, str]]] = ..., data_hora_emissao_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_emissao_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., data_competencia_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_competencia_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_gte: _Optional[float] = ..., total_lte: _Optional[float] = ...) -> None: ...

class ListNfseResponse(_message.Message):
    __slots__ = ("nfse_list",)
    NFSE_LIST_FIELD_NUMBER: _ClassVar[int]
    nfse_list: _containers.RepeatedCompositeFieldContainer[Nfse]
    def __init__(self, nfse_list: _Optional[_Iterable[_Union[Nfse, _Mapping]]] = ...) -> None: ...

class GetNfseRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimeDanfseRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ImprimeDanfseResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class EnviaXmlNfseRequest(_message.Message):
    __slots__ = ("ids", "email", "whatsapp_numero", "whatsapp_nome_destinatario", "whatsapp_integration_id", "email_integration_id", "canal", "whatsapp_template_name", "whatsapp_template_language", "message_template_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMERO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    CANAL_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    email: str
    whatsapp_numero: str
    whatsapp_nome_destinatario: str
    whatsapp_integration_id: str
    email_integration_id: str
    canal: CanalEnvioNfse
    whatsapp_template_name: str
    whatsapp_template_language: str
    message_template_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., whatsapp_numero: _Optional[str] = ..., whatsapp_nome_destinatario: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., canal: _Optional[_Union[CanalEnvioNfse, str]] = ..., whatsapp_template_name: _Optional[str] = ..., whatsapp_template_language: _Optional[str] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class EnviaXmlNfseResponse(_message.Message):
    __slots__ = ("whatsapp_web_message", "public_download_link", "whatsapp_web_envios", "falhas")
    WHATSAPP_WEB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_WEB_ENVIOS_FIELD_NUMBER: _ClassVar[int]
    FALHAS_FIELD_NUMBER: _ClassVar[int]
    whatsapp_web_message: str
    public_download_link: str
    whatsapp_web_envios: _containers.RepeatedCompositeFieldContainer[EnvioWhatsappWebNfse]
    falhas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, whatsapp_web_message: _Optional[str] = ..., public_download_link: _Optional[str] = ..., whatsapp_web_envios: _Optional[_Iterable[_Union[EnvioWhatsappWebNfse, _Mapping]]] = ..., falhas: _Optional[_Iterable[str]] = ...) -> None: ...

class EnvioWhatsappWebNfse(_message.Message):
    __slots__ = ("numero", "mensagem")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    numero: str
    mensagem: str
    def __init__(self, numero: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class AddServicoRequest(_message.Message):
    __slots__ = ("nfse_id", "servico")
    NFSE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    nfse_id: str
    servico: Servico
    def __init__(self, nfse_id: _Optional[str] = ..., servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class AddServicoResponse(_message.Message):
    __slots__ = ("nfse",)
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfse: Nfse
    def __init__(self, nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class UpdateServicoRequest(_message.Message):
    __slots__ = ("nfse_id", "id", "servico")
    NFSE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    nfse_id: str
    id: str
    servico: Servico
    def __init__(self, nfse_id: _Optional[str] = ..., id: _Optional[str] = ..., servico: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class UpdateServicoResponse(_message.Message):
    __slots__ = ("servico", "nfse")
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    servico: Servico
    nfse: Nfse
    def __init__(self, servico: _Optional[_Union[Servico, _Mapping]] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class DeleteServicoRequest(_message.Message):
    __slots__ = ("nfse_id", "id")
    NFSE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfse_id: str
    id: str
    def __init__(self, nfse_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteServicoResponse(_message.Message):
    __slots__ = ("result", "nfse")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfse: Nfse
    def __init__(self, result: _Optional[str] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class GetNfseResponse(_message.Message):
    __slots__ = ("id", "nfse", "status", "mensagem")
    ID_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    nfse: Nfse
    status: str
    mensagem: str
    def __init__(self, id: _Optional[str] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ..., status: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class GetDownloadLinkXmlRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDownloadLinkXmlResponse(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class RegistraEventoDownloadRequest(_message.Message):
    __slots__ = ("id", "tipo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: TipoDownload
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[_Union[TipoDownload, str]] = ...) -> None: ...

class RegistraEventoDownloadResponse(_message.Message):
    __slots__ = ("sucesso",)
    SUCESSO_FIELD_NUMBER: _ClassVar[int]
    sucesso: bool
    def __init__(self, sucesso: _Optional[bool] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "list_nfse_request")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_NFSE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    list_nfse_request: ListNfseRequest
    def __init__(self, tipo_relatorio: _Optional[str] = ..., list_nfse_request: _Optional[_Union[ListNfseRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class DownloadXmlCompetenciaRequest(_message.Message):
    __slots__ = ("mes", "ano", "formato", "incluir_pdf")
    MES_FIELD_NUMBER: _ClassVar[int]
    ANO_FIELD_NUMBER: _ClassVar[int]
    FORMATO_FIELD_NUMBER: _ClassVar[int]
    INCLUIR_PDF_FIELD_NUMBER: _ClassVar[int]
    mes: int
    ano: int
    formato: FormatoXmlCompetencia
    incluir_pdf: bool
    def __init__(self, mes: _Optional[int] = ..., ano: _Optional[int] = ..., formato: _Optional[_Union[FormatoXmlCompetencia, str]] = ..., incluir_pdf: _Optional[bool] = ...) -> None: ...

class DownloadXmlCompetenciaResponse(_message.Message):
    __slots__ = ("link", "nome_arquivo", "quantidade_nfse", "valor_total")
    LINK_FIELD_NUMBER: _ClassVar[int]
    NOME_ARQUIVO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_NFSE_FIELD_NUMBER: _ClassVar[int]
    VALOR_TOTAL_FIELD_NUMBER: _ClassVar[int]
    link: str
    nome_arquivo: str
    quantidade_nfse: int
    valor_total: float
    def __init__(self, link: _Optional[str] = ..., nome_arquivo: _Optional[str] = ..., quantidade_nfse: _Optional[int] = ..., valor_total: _Optional[float] = ...) -> None: ...

class EnviaXmlCompetenciaRequest(_message.Message):
    __slots__ = ("mes", "ano", "formato", "incluir_pdf", "email", "whatsapp_numero", "nome_destinatario")
    MES_FIELD_NUMBER: _ClassVar[int]
    ANO_FIELD_NUMBER: _ClassVar[int]
    FORMATO_FIELD_NUMBER: _ClassVar[int]
    INCLUIR_PDF_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMERO_FIELD_NUMBER: _ClassVar[int]
    NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    mes: int
    ano: int
    formato: FormatoXmlCompetencia
    incluir_pdf: bool
    email: str
    whatsapp_numero: str
    nome_destinatario: str
    def __init__(self, mes: _Optional[int] = ..., ano: _Optional[int] = ..., formato: _Optional[_Union[FormatoXmlCompetencia, str]] = ..., incluir_pdf: _Optional[bool] = ..., email: _Optional[str] = ..., whatsapp_numero: _Optional[str] = ..., nome_destinatario: _Optional[str] = ...) -> None: ...

class EnviaXmlCompetenciaResponse(_message.Message):
    __slots__ = ("whatsapp_web_message", "public_download_link", "quantidade_nfse", "valor_total")
    WHATSAPP_WEB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_NFSE_FIELD_NUMBER: _ClassVar[int]
    VALOR_TOTAL_FIELD_NUMBER: _ClassVar[int]
    whatsapp_web_message: str
    public_download_link: str
    quantidade_nfse: int
    valor_total: float
    def __init__(self, whatsapp_web_message: _Optional[str] = ..., public_download_link: _Optional[str] = ..., quantidade_nfse: _Optional[int] = ..., valor_total: _Optional[float] = ...) -> None: ...

class ImportaXmlRequest(_message.Message):
    __slots__ = ("arquivo_base64", "extensao", "nome_arquivo", "importa_tomador", "importa_servicos", "modo_atualizacao")
    ARQUIVO_BASE64_FIELD_NUMBER: _ClassVar[int]
    EXTENSAO_FIELD_NUMBER: _ClassVar[int]
    NOME_ARQUIVO_FIELD_NUMBER: _ClassVar[int]
    IMPORTA_TOMADOR_FIELD_NUMBER: _ClassVar[int]
    IMPORTA_SERVICOS_FIELD_NUMBER: _ClassVar[int]
    MODO_ATUALIZACAO_FIELD_NUMBER: _ClassVar[int]
    arquivo_base64: str
    extensao: str
    nome_arquivo: str
    importa_tomador: bool
    importa_servicos: bool
    modo_atualizacao: ImportaXmlModoAtualizacao
    def __init__(self, arquivo_base64: _Optional[str] = ..., extensao: _Optional[str] = ..., nome_arquivo: _Optional[str] = ..., importa_tomador: _Optional[bool] = ..., importa_servicos: _Optional[bool] = ..., modo_atualizacao: _Optional[_Union[ImportaXmlModoAtualizacao, str]] = ...) -> None: ...

class ImportaXmlResponse(_message.Message):
    __slots__ = ("nfse_list", "total_importadas", "total_erros", "mensagens", "total_ignoradas", "total_atualizadas")
    NFSE_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPORTADAS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROS_FIELD_NUMBER: _ClassVar[int]
    MENSAGENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IGNORADAS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATUALIZADAS_FIELD_NUMBER: _ClassVar[int]
    nfse_list: _containers.RepeatedCompositeFieldContainer[Nfse]
    total_importadas: int
    total_erros: int
    mensagens: _containers.RepeatedScalarFieldContainer[str]
    total_ignoradas: int
    total_atualizadas: int
    def __init__(self, nfse_list: _Optional[_Iterable[_Union[Nfse, _Mapping]]] = ..., total_importadas: _Optional[int] = ..., total_erros: _Optional[int] = ..., mensagens: _Optional[_Iterable[str]] = ..., total_ignoradas: _Optional[int] = ..., total_atualizadas: _Optional[int] = ...) -> None: ...
