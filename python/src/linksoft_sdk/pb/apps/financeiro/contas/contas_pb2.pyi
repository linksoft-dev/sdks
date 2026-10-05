import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
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
    TIPO_PAGAR: _ClassVar[Tipo]
    TIPO_RECEBER: _ClassVar[Tipo]

class Periodicidade(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERIODICIDADE_UNSPECIFIED: _ClassVar[Periodicidade]
    PERIODICIDADE_SEMANAL: _ClassVar[Periodicidade]
    PERIODICIDADE_QUINZENAL: _ClassVar[Periodicidade]
    PERIODICIDADE_MENSAL: _ClassVar[Periodicidade]
    PERIODICIDADE_BIMESTRAL: _ClassVar[Periodicidade]
    PERIODICIDADE_TRIMESTRAL: _ClassVar[Periodicidade]
    PERIODICIDADE_SEMESTRAL: _ClassVar[Periodicidade]
    PERIODICIDADE_ANUAL: _ClassVar[Periodicidade]
TIPO_UNSPECIFIED: Tipo
TIPO_PAGAR: Tipo
TIPO_RECEBER: Tipo
PERIODICIDADE_UNSPECIFIED: Periodicidade
PERIODICIDADE_SEMANAL: Periodicidade
PERIODICIDADE_QUINZENAL: Periodicidade
PERIODICIDADE_MENSAL: Periodicidade
PERIODICIDADE_BIMESTRAL: Periodicidade
PERIODICIDADE_TRIMESTRAL: Periodicidade
PERIODICIDADE_SEMESTRAL: Periodicidade
PERIODICIDADE_ANUAL: Periodicidade

class SugerePlanoContaIaRequest(_message.Message):
    __slots__ = ("list_contas_request", "ai_integration_id")
    LIST_CONTAS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    list_contas_request: ListContasRequest
    ai_integration_id: str
    def __init__(self, list_contas_request: _Optional[_Union[ListContasRequest, _Mapping]] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class SugestaoPlanoConta(_message.Message):
    __slots__ = ("conta_id", "plano_conta_id", "plano_conta_nome", "plano_conta_codigo", "centro_custo_id", "centro_custo_nome", "confianca", "motivo", "pelo_historico", "pessoa_nome", "descricao", "valor", "vencimento")
    CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_CODIGO_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CONFIANCA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    PELO_HISTORICO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    conta_id: str
    plano_conta_id: str
    plano_conta_nome: str
    plano_conta_codigo: str
    centro_custo_id: str
    centro_custo_nome: str
    confianca: str
    motivo: str
    pelo_historico: bool
    pessoa_nome: str
    descricao: str
    valor: float
    vencimento: _timestamp_pb2.Timestamp
    def __init__(self, conta_id: _Optional[str] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., plano_conta_codigo: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ..., confianca: _Optional[str] = ..., motivo: _Optional[str] = ..., pelo_historico: _Optional[bool] = ..., pessoa_nome: _Optional[str] = ..., descricao: _Optional[str] = ..., valor: _Optional[float] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SugerePlanoContaIaResponse(_message.Message):
    __slots__ = ("sugestoes", "ha_mais")
    SUGESTOES_FIELD_NUMBER: _ClassVar[int]
    HA_MAIS_FIELD_NUMBER: _ClassVar[int]
    sugestoes: _containers.RepeatedCompositeFieldContainer[SugestaoPlanoConta]
    ha_mais: bool
    def __init__(self, sugestoes: _Optional[_Iterable[_Union[SugestaoPlanoConta, _Mapping]]] = ..., ha_mais: _Optional[bool] = ...) -> None: ...

class LeDocumentoIaRequest(_message.Message):
    __slots__ = ("imagem", "mime_type", "texto", "ai_integration_id")
    IMAGEM_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXTO_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    imagem: bytes
    mime_type: str
    texto: str
    ai_integration_id: str
    def __init__(self, imagem: _Optional[bytes] = ..., mime_type: _Optional[str] = ..., texto: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class LeDocumentoIaResponse(_message.Message):
    __slots__ = ("contas", "avisos")
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class FaturaRequest(_message.Message):
    __slots__ = ("ids", "vencimento", "descricao")
    IDS_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    vencimento: _timestamp_pb2.Timestamp
    descricao: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., descricao: _Optional[str] = ...) -> None: ...

class FaturaResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class GeraBoletoRequest(_message.Message):
    __slots__ = ("id", "forma_pagamento_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    forma_pagamento_id: str
    def __init__(self, id: _Optional[str] = ..., forma_pagamento_id: _Optional[str] = ...) -> None: ...

class GeraBoletoResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class SendPaymentLinkRequest(_message.Message):
    __slots__ = ("ids", "email", "channel", "email_integration_id", "whatsapp_integration_id", "whatsapp_template_name", "whatsapp_template_language", "destinatarios", "message_template_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DESTINATARIOS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    email: str
    channel: str
    email_integration_id: str
    whatsapp_integration_id: str
    whatsapp_template_name: str
    whatsapp_template_language: str
    destinatarios: _containers.RepeatedCompositeFieldContainer[DestinatarioCobranca]
    message_template_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., channel: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., whatsapp_template_name: _Optional[str] = ..., whatsapp_template_language: _Optional[str] = ..., destinatarios: _Optional[_Iterable[_Union[DestinatarioCobranca, _Mapping]]] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class DestinatarioCobranca(_message.Message):
    __slots__ = ("conta_id", "nome", "email", "telefone")
    CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    conta_id: str
    nome: str
    email: str
    telefone: str
    def __init__(self, conta_id: _Optional[str] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., telefone: _Optional[str] = ...) -> None: ...

class SendPaymentLinkResponse(_message.Message):
    __slots__ = ("contasList", "whatsapp_web")
    CONTASLIST_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_WEB_FIELD_NUMBER: _ClassVar[int]
    contasList: _containers.RepeatedCompositeFieldContainer[Contas]
    whatsapp_web: _containers.RepeatedCompositeFieldContainer[WhatsappWebEnvio]
    def __init__(self, contasList: _Optional[_Iterable[_Union[Contas, _Mapping]]] = ..., whatsapp_web: _Optional[_Iterable[_Union[WhatsappWebEnvio, _Mapping]]] = ...) -> None: ...

class WhatsappWebEnvio(_message.Message):
    __slots__ = ("numero", "mensagem")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    numero: str
    mensagem: str
    def __init__(self, numero: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class Contas(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "account_id", "situacao", "importado_em", "situacao_dias", "tipo", "pessoa_id", "pessoa_nome", "pessoa_cpf_cnpj", "pessoa_referencia_id", "pessoa_referencia_nome", "pessoa_referencia_cpf_cnpj", "descricao", "plano_conta_id", "plano_conta_nome", "centro_custo_id", "centro_custo_nome", "valor", "baixa_automatica", "baixado_sistema", "forma_pagamento_padrao", "parcela", "parcelas", "tipo_moeda", "cotacao_moeda", "valor_cotacao", "juros_dia_valor", "juros_dia_percentual", "juros_dias_apos_vencimento", "multa_dia_valor", "multa_dia_percentual", "multa_dias_apos_vencimento", "desconto_dia_valor", "desconto_dia_percentual", "desconto_data_ate", "desconto_dias_ate_vencimento", "divida", "motivo_cancelamento", "cancelamento_pessoa_id", "cancelamento_pessoa", "cancelamento_data_hora", "base_calculo", "cheque_nome_titular", "cheque_numero", "cheque_agencia", "cheque_cc", "num_documento", "total_pago", "taxa_adm", "taxa_valor_fixo", "data_hora_quitacao", "vencimento", "date_competence", "previsao_pagamento", "obs", "pagamentos", "origem_id", "origem", "custom_fields", "periodicidade", "periodicidade_quantidade", "periodicidade_indeterminada", "taxas", "periodicidade_dia_base", "periodicidade_proxima_gerada", "checkout_url", "numero", "fields", "org_id", "org_nome", "boleto_url", "boleto_vencimento", "juros_mes_percentual", "multa_percentual", "dias_atraso", "valor_juros", "valor_multa", "fatura_id")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _metadata_pb2.CustomField
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_metadata_pb2.CustomField, _Mapping]] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    IMPORTADO_EM_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_DIAS_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    PESSOA_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    PESSOA_REFERENCIA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_REFERENCIA_NOME_FIELD_NUMBER: _ClassVar[int]
    PESSOA_REFERENCIA_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    BAIXA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    BAIXADO_SISTEMA_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_PADRAO_FIELD_NUMBER: _ClassVar[int]
    PARCELA_FIELD_NUMBER: _ClassVar[int]
    PARCELAS_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    COTACAO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    VALOR_COTACAO_FIELD_NUMBER: _ClassVar[int]
    JUROS_DIA_VALOR_FIELD_NUMBER: _ClassVar[int]
    JUROS_DIA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    JUROS_DIAS_APOS_VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    MULTA_DIA_VALOR_FIELD_NUMBER: _ClassVar[int]
    MULTA_DIA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    MULTA_DIAS_APOS_VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_DIA_VALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_DIA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_DATA_ATE_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_DIAS_ATE_VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    DIVIDA_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    BASE_CALCULO_FIELD_NUMBER: _ClassVar[int]
    CHEQUE_NOME_TITULAR_FIELD_NUMBER: _ClassVar[int]
    CHEQUE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHEQUE_AGENCIA_FIELD_NUMBER: _ClassVar[int]
    CHEQUE_CC_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGO_FIELD_NUMBER: _ClassVar[int]
    TAXA_ADM_FIELD_NUMBER: _ClassVar[int]
    TAXA_VALOR_FIXO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_QUITACAO_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    DATE_COMPETENCE_FIELD_NUMBER: _ClassVar[int]
    PREVISAO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_INDETERMINADA_FIELD_NUMBER: _ClassVar[int]
    TAXAS_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_DIA_BASE_FIELD_NUMBER: _ClassVar[int]
    PERIODICIDADE_PROXIMA_GERADA_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    BOLETO_URL_FIELD_NUMBER: _ClassVar[int]
    BOLETO_VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    JUROS_MES_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    MULTA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    DIAS_ATRASO_FIELD_NUMBER: _ClassVar[int]
    VALOR_JUROS_FIELD_NUMBER: _ClassVar[int]
    VALOR_MULTA_FIELD_NUMBER: _ClassVar[int]
    FATURA_ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    account_id: str
    situacao: str
    importado_em: _timestamp_pb2.Timestamp
    situacao_dias: str
    tipo: str
    pessoa_id: str
    pessoa_nome: str
    pessoa_cpf_cnpj: str
    pessoa_referencia_id: str
    pessoa_referencia_nome: str
    pessoa_referencia_cpf_cnpj: str
    descricao: str
    plano_conta_id: str
    plano_conta_nome: str
    centro_custo_id: str
    centro_custo_nome: str
    valor: float
    baixa_automatica: bool
    baixado_sistema: bool
    forma_pagamento_padrao: FormaPagamentoPadrao
    parcela: str
    parcelas: int
    tipo_moeda: str
    cotacao_moeda: float
    valor_cotacao: float
    juros_dia_valor: float
    juros_dia_percentual: float
    juros_dias_apos_vencimento: int
    multa_dia_valor: float
    multa_dia_percentual: float
    multa_dias_apos_vencimento: int
    desconto_dia_valor: float
    desconto_dia_percentual: float
    desconto_data_ate: _timestamp_pb2.Timestamp
    desconto_dias_ate_vencimento: int
    divida: float
    motivo_cancelamento: str
    cancelamento_pessoa_id: str
    cancelamento_pessoa: str
    cancelamento_data_hora: _timestamp_pb2.Timestamp
    base_calculo: float
    cheque_nome_titular: str
    cheque_numero: str
    cheque_agencia: str
    cheque_cc: str
    num_documento: str
    total_pago: float
    taxa_adm: float
    taxa_valor_fixo: float
    data_hora_quitacao: _timestamp_pb2.Timestamp
    vencimento: _timestamp_pb2.Timestamp
    date_competence: _timestamp_pb2.Timestamp
    previsao_pagamento: _timestamp_pb2.Timestamp
    obs: str
    pagamentos: _containers.RepeatedCompositeFieldContainer[Pagamento]
    origem_id: str
    origem: str
    custom_fields: _containers.MessageMap[str, _metadata_pb2.CustomField]
    periodicidade: Periodicidade
    periodicidade_quantidade: int
    periodicidade_indeterminada: bool
    taxas: _containers.RepeatedCompositeFieldContainer[Taxa]
    periodicidade_dia_base: int
    periodicidade_proxima_gerada: bool
    checkout_url: str
    numero: int
    fields: _metadata_pb2.BasicFields
    org_id: str
    org_nome: str
    boleto_url: str
    boleto_vencimento: _timestamp_pb2.Timestamp
    juros_mes_percentual: float
    multa_percentual: float
    dias_atraso: int
    valor_juros: float
    valor_multa: float
    fatura_id: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., account_id: _Optional[str] = ..., situacao: _Optional[str] = ..., importado_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao_dias: _Optional[str] = ..., tipo: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., pessoa_cpf_cnpj: _Optional[str] = ..., pessoa_referencia_id: _Optional[str] = ..., pessoa_referencia_nome: _Optional[str] = ..., pessoa_referencia_cpf_cnpj: _Optional[str] = ..., descricao: _Optional[str] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ..., valor: _Optional[float] = ..., baixa_automatica: _Optional[bool] = ..., baixado_sistema: _Optional[bool] = ..., forma_pagamento_padrao: _Optional[_Union[FormaPagamentoPadrao, _Mapping]] = ..., parcela: _Optional[str] = ..., parcelas: _Optional[int] = ..., tipo_moeda: _Optional[str] = ..., cotacao_moeda: _Optional[float] = ..., valor_cotacao: _Optional[float] = ..., juros_dia_valor: _Optional[float] = ..., juros_dia_percentual: _Optional[float] = ..., juros_dias_apos_vencimento: _Optional[int] = ..., multa_dia_valor: _Optional[float] = ..., multa_dia_percentual: _Optional[float] = ..., multa_dias_apos_vencimento: _Optional[int] = ..., desconto_dia_valor: _Optional[float] = ..., desconto_dia_percentual: _Optional[float] = ..., desconto_data_ate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., desconto_dias_ate_vencimento: _Optional[int] = ..., divida: _Optional[float] = ..., motivo_cancelamento: _Optional[str] = ..., cancelamento_pessoa_id: _Optional[str] = ..., cancelamento_pessoa: _Optional[str] = ..., cancelamento_data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., base_calculo: _Optional[float] = ..., cheque_nome_titular: _Optional[str] = ..., cheque_numero: _Optional[str] = ..., cheque_agencia: _Optional[str] = ..., cheque_cc: _Optional[str] = ..., num_documento: _Optional[str] = ..., total_pago: _Optional[float] = ..., taxa_adm: _Optional[float] = ..., taxa_valor_fixo: _Optional[float] = ..., data_hora_quitacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_competence: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previsao_pagamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., obs: _Optional[str] = ..., pagamentos: _Optional[_Iterable[_Union[Pagamento, _Mapping]]] = ..., origem_id: _Optional[str] = ..., origem: _Optional[str] = ..., custom_fields: _Optional[_Mapping[str, _metadata_pb2.CustomField]] = ..., periodicidade: _Optional[_Union[Periodicidade, str]] = ..., periodicidade_quantidade: _Optional[int] = ..., periodicidade_indeterminada: _Optional[bool] = ..., taxas: _Optional[_Iterable[_Union[Taxa, _Mapping]]] = ..., periodicidade_dia_base: _Optional[int] = ..., periodicidade_proxima_gerada: _Optional[bool] = ..., checkout_url: _Optional[str] = ..., numero: _Optional[int] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., org_id: _Optional[str] = ..., org_nome: _Optional[str] = ..., boleto_url: _Optional[str] = ..., boleto_vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., juros_mes_percentual: _Optional[float] = ..., multa_percentual: _Optional[float] = ..., dias_atraso: _Optional[int] = ..., valor_juros: _Optional[float] = ..., valor_multa: _Optional[float] = ..., fatura_id: _Optional[str] = ...) -> None: ...

class Taxa(_message.Message):
    __slots__ = ("id", "pessoa_id", "pessoa_nome", "pessoa_cpf_cnpj", "percentual", "valor")
    ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    PESSOA_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    pessoa_id: str
    pessoa_nome: str
    pessoa_cpf_cnpj: str
    percentual: float
    valor: float
    def __init__(self, id: _Optional[str] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., pessoa_cpf_cnpj: _Optional[str] = ..., percentual: _Optional[float] = ..., valor: _Optional[float] = ...) -> None: ...

class Pagamento(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "data_hora", "forma_pagamento_id", "forma_pagamento_nome", "tipo_pagamento", "caixa_id", "caixa_nome", "valor", "identificacao_transacao", "comprovante")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICACAO_TRANSACAO_FIELD_NUMBER: _ClassVar[int]
    COMPROVANTE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    data_hora: _timestamp_pb2.Timestamp
    forma_pagamento_id: str
    forma_pagamento_nome: str
    tipo_pagamento: str
    caixa_id: str
    caixa_nome: str
    valor: float
    identificacao_transacao: str
    comprovante: Comprovante
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., forma_pagamento_id: _Optional[str] = ..., forma_pagamento_nome: _Optional[str] = ..., tipo_pagamento: _Optional[str] = ..., caixa_id: _Optional[str] = ..., caixa_nome: _Optional[str] = ..., valor: _Optional[float] = ..., identificacao_transacao: _Optional[str] = ..., comprovante: _Optional[_Union[Comprovante, _Mapping]] = ...) -> None: ...

class Comprovante(_message.Message):
    __slots__ = ("base64", "url_download", "link_externo", "nome_arquivo", "extensao_arquivo")
    BASE64_FIELD_NUMBER: _ClassVar[int]
    URL_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    LINK_EXTERNO_FIELD_NUMBER: _ClassVar[int]
    NOME_ARQUIVO_FIELD_NUMBER: _ClassVar[int]
    EXTENSAO_ARQUIVO_FIELD_NUMBER: _ClassVar[int]
    base64: str
    url_download: str
    link_externo: str
    nome_arquivo: str
    extensao_arquivo: str
    def __init__(self, base64: _Optional[str] = ..., url_download: _Optional[str] = ..., link_externo: _Optional[str] = ..., nome_arquivo: _Optional[str] = ..., extensao_arquivo: _Optional[str] = ...) -> None: ...

class FormaPagamentoPadrao(_message.Message):
    __slots__ = ("forma_pagamento_id", "forma_pagamento_nome", "caixa_id", "caixa_nome")
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    forma_pagamento_id: str
    forma_pagamento_nome: str
    caixa_id: str
    caixa_nome: str
    def __init__(self, forma_pagamento_id: _Optional[str] = ..., forma_pagamento_nome: _Optional[str] = ..., caixa_id: _Optional[str] = ..., caixa_nome: _Optional[str] = ...) -> None: ...

class CreateContasRequest(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class CreateContasResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class UpdateContasRequest(_message.Message):
    __slots__ = ("id", "contas", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    contas: Contas
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., contas: _Optional[_Union[Contas, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateContasResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class DeleteContasRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteContasResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetContasRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetContasResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class ListContasRequest(_message.Message):
    __slots__ = ("filter", "contas", "situacao", "descricao", "num_documento", "tipo", "emissao_gte", "emissao_lte", "vencimento_gte", "vencimento_lte", "quitacao_gte", "quitacao_lte", "ids", "pessoa_id", "pessoa_referencia_id", "plano_conta_id", "centro_custo_id", "somente_com_plano_conta", "somente_com_centro_custo", "com_baixa_automatica", "sem_baixa_automatica", "tipo_moeda", "total_gte", "total_lte", "order_by", "order_direction", "origem", "origem_id", "sem_plano_conta")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    EMISSAO_GTE_FIELD_NUMBER: _ClassVar[int]
    EMISSAO_LTE_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_GTE_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_LTE_FIELD_NUMBER: _ClassVar[int]
    QUITACAO_GTE_FIELD_NUMBER: _ClassVar[int]
    QUITACAO_LTE_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_REFERENCIA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    SOMENTE_COM_PLANO_CONTA_FIELD_NUMBER: _ClassVar[int]
    SOMENTE_COM_CENTRO_CUSTO_FIELD_NUMBER: _ClassVar[int]
    COM_BAIXA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    SEM_BAIXA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LTE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    SEM_PLANO_CONTA_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.Filter
    contas: _containers.RepeatedCompositeFieldContainer[Contas]
    situacao: _containers.RepeatedScalarFieldContainer[str]
    descricao: str
    num_documento: str
    tipo: str
    emissao_gte: _timestamp_pb2.Timestamp
    emissao_lte: _timestamp_pb2.Timestamp
    vencimento_gte: _timestamp_pb2.Timestamp
    vencimento_lte: _timestamp_pb2.Timestamp
    quitacao_gte: _timestamp_pb2.Timestamp
    quitacao_lte: _timestamp_pb2.Timestamp
    ids: _containers.RepeatedScalarFieldContainer[str]
    pessoa_id: str
    pessoa_referencia_id: str
    plano_conta_id: str
    centro_custo_id: str
    somente_com_plano_conta: bool
    somente_com_centro_custo: bool
    com_baixa_automatica: bool
    sem_baixa_automatica: bool
    tipo_moeda: _containers.RepeatedScalarFieldContainer[str]
    total_gte: float
    total_lte: float
    order_by: _containers.RepeatedCompositeFieldContainer[_filter_pb2.OrderBy]
    order_direction: _containers.RepeatedScalarFieldContainer[str]
    origem: _containers.RepeatedScalarFieldContainer[str]
    origem_id: _containers.RepeatedScalarFieldContainer[str]
    sem_plano_conta: bool
    def __init__(self, filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., contas: _Optional[_Iterable[_Union[Contas, _Mapping]]] = ..., situacao: _Optional[_Iterable[str]] = ..., descricao: _Optional[str] = ..., num_documento: _Optional[str] = ..., tipo: _Optional[str] = ..., emissao_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., emissao_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vencimento_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., vencimento_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quitacao_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quitacao_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ids: _Optional[_Iterable[str]] = ..., pessoa_id: _Optional[str] = ..., pessoa_referencia_id: _Optional[str] = ..., plano_conta_id: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., somente_com_plano_conta: _Optional[bool] = ..., somente_com_centro_custo: _Optional[bool] = ..., com_baixa_automatica: _Optional[bool] = ..., sem_baixa_automatica: _Optional[bool] = ..., tipo_moeda: _Optional[_Iterable[str]] = ..., total_gte: _Optional[float] = ..., total_lte: _Optional[float] = ..., order_by: _Optional[_Iterable[_Union[_filter_pb2.OrderBy, _Mapping]]] = ..., order_direction: _Optional[_Iterable[str]] = ..., origem: _Optional[_Iterable[str]] = ..., origem_id: _Optional[_Iterable[str]] = ..., sem_plano_conta: _Optional[bool] = ...) -> None: ...

class ListContasResponse(_message.Message):
    __slots__ = ("contas_list", "next_page_token")
    CONTAS_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contas_list: _containers.RepeatedCompositeFieldContainer[Contas]
    next_page_token: str
    def __init__(self, contas_list: _Optional[_Iterable[_Union[Contas, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CancelarRequest(_message.Message):
    __slots__ = ("id", "origem", "origem_id", "motivo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    id: str
    origem: str
    origem_id: str
    motivo: str
    def __init__(self, id: _Optional[str] = ..., origem: _Optional[str] = ..., origem_id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class CancelarResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class AddPagamentoRequest(_message.Message):
    __slots__ = ("id", "pagamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    pagamento: Pagamento
    def __init__(self, id: _Optional[str] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ...) -> None: ...

class AddPagamentoResponse(_message.Message):
    __slots__ = ("contas", "pagamento")
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    pagamento: Pagamento
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ...) -> None: ...

class UpdatePagamentoRequest(_message.Message):
    __slots__ = ("id", "pagamento_id", "pagamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    pagamento_id: str
    pagamento: Pagamento
    def __init__(self, id: _Optional[str] = ..., pagamento_id: _Optional[str] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ...) -> None: ...

class UpdatePagamentoResponse(_message.Message):
    __slots__ = ("contas", "pagamento")
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    pagamento: Pagamento
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ...) -> None: ...

class DeletePagamentoRequest(_message.Message):
    __slots__ = ("id", "pagamento_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    pagamento_id: str
    def __init__(self, id: _Optional[str] = ..., pagamento_id: _Optional[str] = ...) -> None: ...

class DeletePagamentoResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class AtualizaComprovanteRequest(_message.Message):
    __slots__ = ("id", "pagamento_id", "base64")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    BASE64_FIELD_NUMBER: _ClassVar[int]
    id: str
    pagamento_id: str
    base64: str
    def __init__(self, id: _Optional[str] = ..., pagamento_id: _Optional[str] = ..., base64: _Optional[str] = ...) -> None: ...

class AtualizaComprovanteResponse(_message.Message):
    __slots__ = ("contas",)
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    contas: Contas
    def __init__(self, contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("file_content", "file_name", "accounts", "validate_only", "update_if_exists", "import_account", "import_person", "import_chart_of_accounts", "import_cost_center")
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PERSON_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CHART_OF_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_COST_CENTER_FIELD_NUMBER: _ClassVar[int]
    file_content: str
    file_name: str
    accounts: _containers.RepeatedCompositeFieldContainer[Contas]
    validate_only: bool
    update_if_exists: bool
    import_account: bool
    import_person: bool
    import_chart_of_accounts: bool
    import_cost_center: bool
    def __init__(self, file_content: _Optional[str] = ..., file_name: _Optional[str] = ..., accounts: _Optional[_Iterable[_Union[Contas, _Mapping]]] = ..., validate_only: _Optional[bool] = ..., update_if_exists: _Optional[bool] = ..., import_account: _Optional[bool] = ..., import_person: _Optional[bool] = ..., import_chart_of_accounts: _Optional[bool] = ..., import_cost_center: _Optional[bool] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ("result", "success", "failed", "total", "erros_by_category", "html_report")
    class ErrosByCategoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ImportErrorGroup
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ImportErrorGroup, _Mapping]] = ...) -> None: ...
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ERROS_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    HTML_REPORT_FIELD_NUMBER: _ClassVar[int]
    result: str
    success: int
    failed: int
    total: int
    erros_by_category: _containers.MessageMap[str, ImportErrorGroup]
    html_report: str
    def __init__(self, result: _Optional[str] = ..., success: _Optional[int] = ..., failed: _Optional[int] = ..., total: _Optional[int] = ..., erros_by_category: _Optional[_Mapping[str, ImportErrorGroup]] = ..., html_report: _Optional[str] = ...) -> None: ...

class ImportErrorGroup(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ImportError]
    def __init__(self, errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]] = ...) -> None: ...

class ImportError(_message.Message):
    __slots__ = ("account", "reason", "details")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    account: str
    reason: str
    details: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, account: _Optional[str] = ..., reason: _Optional[str] = ..., details: _Optional[_Iterable[str]] = ...) -> None: ...

class AlteracaoConjunta(_message.Message):
    __slots__ = ("ids", "plano_conta_id", "plano_conta_nome", "centro_custo_id", "centro_custo_nome", "remover_plano_contas", "remover_centro_custos", "valor", "alterar_tipo_moeda", "tipo_moeda", "baixa_automatica", "nao_baixa_automatica", "vencimento")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_ID_FIELD_NUMBER: _ClassVar[int]
    CENTRO_CUSTO_NOME_FIELD_NUMBER: _ClassVar[int]
    REMOVER_PLANO_CONTAS_FIELD_NUMBER: _ClassVar[int]
    REMOVER_CENTRO_CUSTOS_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ALTERAR_TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    BAIXA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    NAO_BAIXA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    plano_conta_id: str
    plano_conta_nome: str
    centro_custo_id: str
    centro_custo_nome: str
    remover_plano_contas: bool
    remover_centro_custos: bool
    valor: float
    alterar_tipo_moeda: bool
    tipo_moeda: str
    baixa_automatica: bool
    nao_baixa_automatica: bool
    vencimento: _timestamp_pb2.Timestamp
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., plano_conta_id: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., centro_custo_id: _Optional[str] = ..., centro_custo_nome: _Optional[str] = ..., remover_plano_contas: _Optional[bool] = ..., remover_centro_custos: _Optional[bool] = ..., valor: _Optional[float] = ..., alterar_tipo_moeda: _Optional[bool] = ..., tipo_moeda: _Optional[str] = ..., baixa_automatica: _Optional[bool] = ..., nao_baixa_automatica: _Optional[bool] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AlteracaoConjuntaRequest(_message.Message):
    __slots__ = ("list_contas_request", "alteracao")
    LIST_CONTAS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ALTERACAO_FIELD_NUMBER: _ClassVar[int]
    list_contas_request: ListContasRequest
    alteracao: AlteracaoConjunta
    def __init__(self, list_contas_request: _Optional[_Union[ListContasRequest, _Mapping]] = ..., alteracao: _Optional[_Union[AlteracaoConjunta, _Mapping]] = ...) -> None: ...

class AlteracaoConjuntaResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class FaturamentoConjuntoRequest(_message.Message):
    __slots__ = ("ids", "forma_pagamento_id", "forma_pagamento_nome", "caixa_id", "caixa_nome")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    forma_pagamento_id: str
    forma_pagamento_nome: str
    caixa_id: str
    caixa_nome: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., forma_pagamento_id: _Optional[str] = ..., forma_pagamento_nome: _Optional[str] = ..., caixa_id: _Optional[str] = ..., caixa_nome: _Optional[str] = ...) -> None: ...

class FaturamentoConjuntoResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class MesclaContasRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MesclaContasResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class ResumoPessoa(_message.Message):
    __slots__ = ("pessoa_id", "pessoa_nome", "total")
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    pessoa_id: str
    pessoa_nome: str
    total: float
    def __init__(self, pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., total: _Optional[float] = ...) -> None: ...

class ResumoDados(_message.Message):
    __slots__ = ("qtde", "total", "pessoasMap", "pessoas")
    class PessoasMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ResumoPessoa
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ResumoPessoa, _Mapping]] = ...) -> None: ...
    QTDE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PESSOASMAP_FIELD_NUMBER: _ClassVar[int]
    PESSOAS_FIELD_NUMBER: _ClassVar[int]
    qtde: int
    total: float
    pessoasMap: _containers.MessageMap[str, ResumoPessoa]
    pessoas: _containers.RepeatedCompositeFieldContainer[ResumoPessoa]
    def __init__(self, qtde: _Optional[int] = ..., total: _Optional[float] = ..., pessoasMap: _Optional[_Mapping[str, ResumoPessoa]] = ..., pessoas: _Optional[_Iterable[_Union[ResumoPessoa, _Mapping]]] = ...) -> None: ...

class ResumoMesAno(_message.Message):
    __slots__ = ("mes_ano", "receber", "pagar")
    MES_ANO_FIELD_NUMBER: _ClassVar[int]
    RECEBER_FIELD_NUMBER: _ClassVar[int]
    PAGAR_FIELD_NUMBER: _ClassVar[int]
    mes_ano: str
    receber: float
    pagar: float
    def __init__(self, mes_ano: _Optional[str] = ..., receber: _Optional[float] = ..., pagar: _Optional[float] = ...) -> None: ...

class ResumoPagarReceber(_message.Message):
    __slots__ = ("hoje", "atrasada")
    HOJE_FIELD_NUMBER: _ClassVar[int]
    ATRASADA_FIELD_NUMBER: _ClassVar[int]
    hoje: ResumoDados
    atrasada: ResumoDados
    def __init__(self, hoje: _Optional[_Union[ResumoDados, _Mapping]] = ..., atrasada: _Optional[_Union[ResumoDados, _Mapping]] = ...) -> None: ...

class ResumoPagoRecebido(_message.Message):
    __slots__ = ("hoje",)
    HOJE_FIELD_NUMBER: _ClassVar[int]
    hoje: ResumoDados
    def __init__(self, hoje: _Optional[_Union[ResumoDados, _Mapping]] = ...) -> None: ...

class DashboardRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DashboardResponse(_message.Message):
    __slots__ = ("pagar", "pago", "receber", "recebido", "pagar_receber_por_mes", "proximos_dias", "maiores_atrasos")
    PAGAR_FIELD_NUMBER: _ClassVar[int]
    PAGO_FIELD_NUMBER: _ClassVar[int]
    RECEBER_FIELD_NUMBER: _ClassVar[int]
    RECEBIDO_FIELD_NUMBER: _ClassVar[int]
    PAGAR_RECEBER_POR_MES_FIELD_NUMBER: _ClassVar[int]
    PROXIMOS_DIAS_FIELD_NUMBER: _ClassVar[int]
    MAIORES_ATRASOS_FIELD_NUMBER: _ClassVar[int]
    pagar: ResumoPagarReceber
    pago: ResumoPagoRecebido
    receber: ResumoPagarReceber
    recebido: ResumoPagoRecebido
    pagar_receber_por_mes: _containers.RepeatedCompositeFieldContainer[ResumoMesAno]
    proximos_dias: _containers.RepeatedCompositeFieldContainer[ResumoDia]
    maiores_atrasos: _containers.RepeatedCompositeFieldContainer[ContaAtrasada]
    def __init__(self, pagar: _Optional[_Union[ResumoPagarReceber, _Mapping]] = ..., pago: _Optional[_Union[ResumoPagoRecebido, _Mapping]] = ..., receber: _Optional[_Union[ResumoPagarReceber, _Mapping]] = ..., recebido: _Optional[_Union[ResumoPagoRecebido, _Mapping]] = ..., pagar_receber_por_mes: _Optional[_Iterable[_Union[ResumoMesAno, _Mapping]]] = ..., proximos_dias: _Optional[_Iterable[_Union[ResumoDia, _Mapping]]] = ..., maiores_atrasos: _Optional[_Iterable[_Union[ContaAtrasada, _Mapping]]] = ...) -> None: ...

class ResumoDia(_message.Message):
    __slots__ = ("dia", "receber", "pagar")
    DIA_FIELD_NUMBER: _ClassVar[int]
    RECEBER_FIELD_NUMBER: _ClassVar[int]
    PAGAR_FIELD_NUMBER: _ClassVar[int]
    dia: str
    receber: float
    pagar: float
    def __init__(self, dia: _Optional[str] = ..., receber: _Optional[float] = ..., pagar: _Optional[float] = ...) -> None: ...

class ContaAtrasada(_message.Message):
    __slots__ = ("id", "tipo", "pessoa_nome", "descricao", "plano_conta_nome", "vencimento", "dias_atraso", "valor")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PLANO_CONTA_NOME_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    DIAS_ATRASO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: str
    pessoa_nome: str
    descricao: str
    plano_conta_nome: str
    vencimento: str
    dias_atraso: int
    valor: float
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., descricao: _Optional[str] = ..., plano_conta_nome: _Optional[str] = ..., vencimento: _Optional[str] = ..., dias_atraso: _Optional[int] = ..., valor: _Optional[float] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("type", "tipo_relatorio", "list_contas_request")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_CONTAS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    type: Tipo
    tipo_relatorio: str
    list_contas_request: ListContasRequest
    def __init__(self, type: _Optional[_Union[Tipo, str]] = ..., tipo_relatorio: _Optional[str] = ..., list_contas_request: _Optional[_Union[ListContasRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class CloneRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneResponse(_message.Message):
    __slots__ = ("result", "contas")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CONTAS_FIELD_NUMBER: _ClassVar[int]
    result: str
    contas: Contas
    def __init__(self, result: _Optional[str] = ..., contas: _Optional[_Union[Contas, _Mapping]] = ...) -> None: ...

class GetOutstandingBalanceRequest(_message.Message):
    __slots__ = ("pessoa_id",)
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    pessoa_id: str
    def __init__(self, pessoa_id: _Optional[str] = ...) -> None: ...

class GetOutstandingBalanceResponse(_message.Message):
    __slots__ = ("saldo",)
    SALDO_FIELD_NUMBER: _ClassVar[int]
    saldo: float
    def __init__(self, saldo: _Optional[float] = ...) -> None: ...

class DuplicataRequest(_message.Message):
    __slots__ = ("ids", "tipo_relatorio")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    tipo_relatorio: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., tipo_relatorio: _Optional[str] = ...) -> None: ...

class DuplicataResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ExportRequest(_message.Message):
    __slots__ = ("format", "type", "include_metadata", "filter")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    format: str
    type: str
    include_metadata: bool
    filter: _filter_pb2.Filter
    def __init__(self, format: _Optional[str] = ..., type: _Optional[str] = ..., include_metadata: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ExportResponse(_message.Message):
    __slots__ = ("status", "sse_url")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SSE_URL_FIELD_NUMBER: _ClassVar[int]
    status: str
    sse_url: str
    def __init__(self, status: _Optional[str] = ..., sse_url: _Optional[str] = ...) -> None: ...

class ImprimirReciboRequest(_message.Message):
    __slots__ = ("pagamento_id", "ids")
    PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    pagamento_id: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, pagamento_id: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ImprimirReciboResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
