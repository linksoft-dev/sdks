import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class Rodoviario(_message.Message):
    __slots__ = ("rntrc", "codigo_agendamento_porto", "tracao_cod_interno_veiculo", "tracao_tipo_carroceria", "tracao_placa", "tracao_tara", "tracao_renavam", "tracao_uf", "tracao_tipo_rodado", "tracao_capacidade_kg", "tracao_capacidade_m3", "tracao_proprietario_cpf_cnpj", "tracao_proprietario_nome", "tracao_proprietario_ie", "tracao_proprietario_uf", "tracao_proprietario_tipo", "ciot", "ciot_cpf_cnpj", "tracao_proprietario_rntrc")
    RNTRC_FIELD_NUMBER: _ClassVar[int]
    CODIGO_AGENDAMENTO_PORTO_FIELD_NUMBER: _ClassVar[int]
    TRACAO_COD_INTERNO_VEICULO_FIELD_NUMBER: _ClassVar[int]
    TRACAO_TIPO_CARROCERIA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PLACA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_TARA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_RENAVAM_FIELD_NUMBER: _ClassVar[int]
    TRACAO_UF_FIELD_NUMBER: _ClassVar[int]
    TRACAO_TIPO_RODADO_FIELD_NUMBER: _ClassVar[int]
    TRACAO_CAPACIDADE_KG_FIELD_NUMBER: _ClassVar[int]
    TRACAO_CAPACIDADE_M3_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_IE_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_UF_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_TIPO_FIELD_NUMBER: _ClassVar[int]
    CIOT_FIELD_NUMBER: _ClassVar[int]
    CIOT_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_RNTRC_FIELD_NUMBER: _ClassVar[int]
    rntrc: str
    codigo_agendamento_porto: str
    tracao_cod_interno_veiculo: str
    tracao_tipo_carroceria: str
    tracao_placa: str
    tracao_tara: float
    tracao_renavam: str
    tracao_uf: str
    tracao_tipo_rodado: str
    tracao_capacidade_kg: float
    tracao_capacidade_m3: float
    tracao_proprietario_cpf_cnpj: str
    tracao_proprietario_nome: str
    tracao_proprietario_ie: str
    tracao_proprietario_uf: str
    tracao_proprietario_tipo: int
    ciot: str
    ciot_cpf_cnpj: str
    tracao_proprietario_rntrc: str
    def __init__(self, rntrc: _Optional[str] = ..., codigo_agendamento_porto: _Optional[str] = ..., tracao_cod_interno_veiculo: _Optional[str] = ..., tracao_tipo_carroceria: _Optional[str] = ..., tracao_placa: _Optional[str] = ..., tracao_tara: _Optional[float] = ..., tracao_renavam: _Optional[str] = ..., tracao_uf: _Optional[str] = ..., tracao_tipo_rodado: _Optional[str] = ..., tracao_capacidade_kg: _Optional[float] = ..., tracao_capacidade_m3: _Optional[float] = ..., tracao_proprietario_cpf_cnpj: _Optional[str] = ..., tracao_proprietario_nome: _Optional[str] = ..., tracao_proprietario_ie: _Optional[str] = ..., tracao_proprietario_uf: _Optional[str] = ..., tracao_proprietario_tipo: _Optional[int] = ..., ciot: _Optional[str] = ..., ciot_cpf_cnpj: _Optional[str] = ..., tracao_proprietario_rntrc: _Optional[str] = ...) -> None: ...

class Pagamento(_message.Message):
    __slots__ = ("responsavel_pagamento_id", "responsavel_pagamento_nome", "responsavel_pagamento_cpf_cnpj", "componentes_pagamento", "valor_contrato", "forma_pagamento", "valor_adiantamento", "parcelamentos", "numero_banco", "numero_agencia", "cnpj_instituicao_pagamento_eletronico", "chave_pix")
    RESPONSAVEL_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_PAGAMENTO_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    COMPONENTES_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_CONTRATO_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_ADIANTAMENTO_FIELD_NUMBER: _ClassVar[int]
    PARCELAMENTOS_FIELD_NUMBER: _ClassVar[int]
    NUMERO_BANCO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_AGENCIA_FIELD_NUMBER: _ClassVar[int]
    CNPJ_INSTITUICAO_PAGAMENTO_ELETRONICO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_PIX_FIELD_NUMBER: _ClassVar[int]
    responsavel_pagamento_id: str
    responsavel_pagamento_nome: str
    responsavel_pagamento_cpf_cnpj: str
    componentes_pagamento: _containers.RepeatedCompositeFieldContainer[ComponentePagamento]
    valor_contrato: float
    forma_pagamento: str
    valor_adiantamento: float
    parcelamentos: _containers.RepeatedCompositeFieldContainer[Parcelamento]
    numero_banco: str
    numero_agencia: str
    cnpj_instituicao_pagamento_eletronico: str
    chave_pix: str
    def __init__(self, responsavel_pagamento_id: _Optional[str] = ..., responsavel_pagamento_nome: _Optional[str] = ..., responsavel_pagamento_cpf_cnpj: _Optional[str] = ..., componentes_pagamento: _Optional[_Iterable[_Union[ComponentePagamento, _Mapping]]] = ..., valor_contrato: _Optional[float] = ..., forma_pagamento: _Optional[str] = ..., valor_adiantamento: _Optional[float] = ..., parcelamentos: _Optional[_Iterable[_Union[Parcelamento, _Mapping]]] = ..., numero_banco: _Optional[str] = ..., numero_agencia: _Optional[str] = ..., cnpj_instituicao_pagamento_eletronico: _Optional[str] = ..., chave_pix: _Optional[str] = ...) -> None: ...

class ComponentePagamento(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "tipo", "valor", "descricao_outros")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_OUTROS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tipo: str
    valor: float
    descricao_outros: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tipo: _Optional[str] = ..., valor: _Optional[float] = ..., descricao_outros: _Optional[str] = ...) -> None: ...

class Parcelamento(_message.Message):
    __slots__ = ("numero_parcela", "data_vencimento", "valor_parcela")
    NUMERO_PARCELA_FIELD_NUMBER: _ClassVar[int]
    DATA_VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_PARCELA_FIELD_NUMBER: _ClassVar[int]
    numero_parcela: str
    data_vencimento: _timestamp_pb2.Timestamp
    valor_parcela: float
    def __init__(self, numero_parcela: _Optional[str] = ..., data_vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valor_parcela: _Optional[float] = ...) -> None: ...

class Proprietario(_message.Message):
    __slots__ = ("cnpj", "rntrc", "nome", "ie", "uf", "tracao_proprietario_tipo")
    CNPJ_FIELD_NUMBER: _ClassVar[int]
    RNTRC_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_TIPO_FIELD_NUMBER: _ClassVar[int]
    cnpj: str
    rntrc: str
    nome: str
    ie: str
    uf: str
    tracao_proprietario_tipo: int
    def __init__(self, cnpj: _Optional[str] = ..., rntrc: _Optional[str] = ..., nome: _Optional[str] = ..., ie: _Optional[str] = ..., uf: _Optional[str] = ..., tracao_proprietario_tipo: _Optional[int] = ...) -> None: ...

class Reboque(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "tracao_cod_interno_veiculo", "tracao_placa", "tracao_renavam", "tracao_tara", "tracao_capacidade_kg", "tracao_capacidade_m3", "proprietario", "tracao_tipo_carroceria", "tracao_proprietario_uf")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACAO_COD_INTERNO_VEICULO_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PLACA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_RENAVAM_FIELD_NUMBER: _ClassVar[int]
    TRACAO_TARA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_CAPACIDADE_KG_FIELD_NUMBER: _ClassVar[int]
    TRACAO_CAPACIDADE_M3_FIELD_NUMBER: _ClassVar[int]
    PROPRIETARIO_FIELD_NUMBER: _ClassVar[int]
    TRACAO_TIPO_CARROCERIA_FIELD_NUMBER: _ClassVar[int]
    TRACAO_PROPRIETARIO_UF_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tracao_cod_interno_veiculo: str
    tracao_placa: str
    tracao_renavam: str
    tracao_tara: float
    tracao_capacidade_kg: float
    tracao_capacidade_m3: float
    proprietario: Proprietario
    tracao_tipo_carroceria: str
    tracao_proprietario_uf: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tracao_cod_interno_veiculo: _Optional[str] = ..., tracao_placa: _Optional[str] = ..., tracao_renavam: _Optional[str] = ..., tracao_tara: _Optional[float] = ..., tracao_capacidade_kg: _Optional[float] = ..., tracao_capacidade_m3: _Optional[float] = ..., proprietario: _Optional[_Union[Proprietario, _Mapping]] = ..., tracao_tipo_carroceria: _Optional[str] = ..., tracao_proprietario_uf: _Optional[str] = ...) -> None: ...

class Condutor(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "nome", "cpf")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CPF_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    nome: str
    cpf: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., nome: _Optional[str] = ..., cpf: _Optional[str] = ...) -> None: ...

class Carregamento(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "uf", "municipio_codigo", "municipio")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_CODIGO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    uf: str
    municipio_codigo: str
    municipio: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., uf: _Optional[str] = ..., municipio_codigo: _Optional[str] = ..., municipio: _Optional[str] = ...) -> None: ...

class Percurso(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "uf")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    uf: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., uf: _Optional[str] = ...) -> None: ...

class NfeUnidadeCarga(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "tipo", "tipo_text", "identificacao")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    TIPO_TEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICACAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tipo: int
    tipo_text: str
    identificacao: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tipo: _Optional[int] = ..., tipo_text: _Optional[str] = ..., identificacao: _Optional[str] = ...) -> None: ...

class NfeUnidadeTransporte(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "tipo", "tipo_text", "identificacao", "unidades_carga")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    TIPO_TEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICACAO_FIELD_NUMBER: _ClassVar[int]
    UNIDADES_CARGA_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    tipo: str
    tipo_text: str
    identificacao: str
    unidades_carga: _containers.RepeatedCompositeFieldContainer[NfeUnidadeCarga]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., tipo: _Optional[str] = ..., tipo_text: _Optional[str] = ..., identificacao: _Optional[str] = ..., unidades_carga: _Optional[_Iterable[_Union[NfeUnidadeCarga, _Mapping]]] = ...) -> None: ...

class Nfe(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "chave", "unidades_transporte")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    UNIDADES_TRANSPORTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    chave: str
    unidades_transporte: _containers.RepeatedCompositeFieldContainer[NfeUnidadeTransporte]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., chave: _Optional[str] = ..., unidades_transporte: _Optional[_Iterable[_Union[NfeUnidadeTransporte, _Mapping]]] = ...) -> None: ...

class Cte(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "chave", "unidades_transporte")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    UNIDADES_TRANSPORTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    chave: str
    unidades_transporte: _containers.RepeatedCompositeFieldContainer[NfeUnidadeTransporte]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., chave: _Optional[str] = ..., unidades_transporte: _Optional[_Iterable[_Union[NfeUnidadeTransporte, _Mapping]]] = ...) -> None: ...

class Descarregamento(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "uf", "municipio_codigo", "municipio", "nfes", "ctes")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_CODIGO_FIELD_NUMBER: _ClassVar[int]
    MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    NFES_FIELD_NUMBER: _ClassVar[int]
    CTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    uf: str
    municipio_codigo: str
    municipio: str
    nfes: _containers.RepeatedCompositeFieldContainer[Nfe]
    ctes: _containers.RepeatedCompositeFieldContainer[Cte]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., uf: _Optional[str] = ..., municipio_codigo: _Optional[str] = ..., municipio: _Optional[str] = ..., nfes: _Optional[_Iterable[_Union[Nfe, _Mapping]]] = ..., ctes: _Optional[_Iterable[_Union[Cte, _Mapping]]] = ...) -> None: ...

class Seguro(_message.Message):
    __slots__ = ("responsavel_tipo", "responsavel_cnpj", "seguradora", "seguradora_cnpj", "num_apolice", "averbacoes")
    RESPONSAVEL_TIPO_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEL_CNPJ_FIELD_NUMBER: _ClassVar[int]
    SEGURADORA_FIELD_NUMBER: _ClassVar[int]
    SEGURADORA_CNPJ_FIELD_NUMBER: _ClassVar[int]
    NUM_APOLICE_FIELD_NUMBER: _ClassVar[int]
    AVERBACOES_FIELD_NUMBER: _ClassVar[int]
    responsavel_tipo: str
    responsavel_cnpj: str
    seguradora: str
    seguradora_cnpj: str
    num_apolice: str
    averbacoes: str
    def __init__(self, responsavel_tipo: _Optional[str] = ..., responsavel_cnpj: _Optional[str] = ..., seguradora: _Optional[str] = ..., seguradora_cnpj: _Optional[str] = ..., num_apolice: _Optional[str] = ..., averbacoes: _Optional[str] = ...) -> None: ...

class ProdutoPredominante(_message.Message):
    __slots__ = ("cean", "tipo_carga", "ncm", "nome", "cep_carrega", "cep_descarrega")
    CEAN_FIELD_NUMBER: _ClassVar[int]
    TIPO_CARGA_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CEP_CARREGA_FIELD_NUMBER: _ClassVar[int]
    CEP_DESCARREGA_FIELD_NUMBER: _ClassVar[int]
    cean: str
    tipo_carga: str
    ncm: str
    nome: str
    cep_carrega: str
    cep_descarrega: str
    def __init__(self, cean: _Optional[str] = ..., tipo_carga: _Optional[str] = ..., ncm: _Optional[str] = ..., nome: _Optional[str] = ..., cep_carrega: _Optional[str] = ..., cep_descarrega: _Optional[str] = ...) -> None: ...

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

class Mdfe(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "situacao", "tipo_ambiente", "forma_emissao", "numero", "serie", "chave", "protocolo", "fields", "data_hora_emissao", "data_hora_autorizacao", "protocolo_encerramento", "data_hora_encerramento", "protocolo_cancelamento", "motivo_cancelamento", "data_hora_cancelamento", "uf_carregamento", "uf_descarregamento", "xml_autorizacao", "xml_cancelamento", "tipo_emitente", "tipo_transportador", "modalidade", "rodoviario", "rodoviario_reboques", "valor_carga", "codigo_unidade", "peso_bruto_total", "inf_adicional_fisco", "inf_adicional_contibuinte", "historico", "calcula_total_baseado_notas", "condutores", "carregamentos", "percursos", "descarregamentos", "seguro", "produto_predominante", "rejeicoes", "pagamento", "informado_externamente")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_ENCERRAMENTO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_ENCERRAMENTO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    UF_CARREGAMENTO_FIELD_NUMBER: _ClassVar[int]
    UF_DESCARREGAMENTO_FIELD_NUMBER: _ClassVar[int]
    XML_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    XML_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    TIPO_EMITENTE_FIELD_NUMBER: _ClassVar[int]
    TIPO_TRANSPORTADOR_FIELD_NUMBER: _ClassVar[int]
    MODALIDADE_FIELD_NUMBER: _ClassVar[int]
    RODOVIARIO_FIELD_NUMBER: _ClassVar[int]
    RODOVIARIO_REBOQUES_FIELD_NUMBER: _ClassVar[int]
    VALOR_CARGA_FIELD_NUMBER: _ClassVar[int]
    CODIGO_UNIDADE_FIELD_NUMBER: _ClassVar[int]
    PESO_BRUTO_TOTAL_FIELD_NUMBER: _ClassVar[int]
    INF_ADICIONAL_FISCO_FIELD_NUMBER: _ClassVar[int]
    INF_ADICIONAL_CONTIBUINTE_FIELD_NUMBER: _ClassVar[int]
    HISTORICO_FIELD_NUMBER: _ClassVar[int]
    CALCULA_TOTAL_BASEADO_NOTAS_FIELD_NUMBER: _ClassVar[int]
    CONDUTORES_FIELD_NUMBER: _ClassVar[int]
    CARREGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    PERCURSOS_FIELD_NUMBER: _ClassVar[int]
    DESCARREGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    SEGURO_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_PREDOMINANTE_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    INFORMADO_EXTERNAMENTE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    situacao: str
    tipo_ambiente: str
    forma_emissao: str
    numero: int
    serie: int
    chave: str
    protocolo: str
    fields: _metadata_pb2.BasicFields
    data_hora_emissao: _timestamp_pb2.Timestamp
    data_hora_autorizacao: _timestamp_pb2.Timestamp
    protocolo_encerramento: str
    data_hora_encerramento: _timestamp_pb2.Timestamp
    protocolo_cancelamento: str
    motivo_cancelamento: str
    data_hora_cancelamento: _timestamp_pb2.Timestamp
    uf_carregamento: str
    uf_descarregamento: str
    xml_autorizacao: str
    xml_cancelamento: str
    tipo_emitente: int
    tipo_transportador: int
    modalidade: int
    rodoviario: Rodoviario
    rodoviario_reboques: _containers.RepeatedCompositeFieldContainer[Reboque]
    valor_carga: float
    codigo_unidade: str
    peso_bruto_total: float
    inf_adicional_fisco: str
    inf_adicional_contibuinte: str
    historico: str
    calcula_total_baseado_notas: bool
    condutores: _containers.RepeatedCompositeFieldContainer[Condutor]
    carregamentos: _containers.RepeatedCompositeFieldContainer[Carregamento]
    percursos: _containers.RepeatedCompositeFieldContainer[Percurso]
    descarregamentos: _containers.RepeatedCompositeFieldContainer[Descarregamento]
    seguro: Seguro
    produto_predominante: ProdutoPredominante
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Rejeicao]
    pagamento: Pagamento
    informado_externamente: bool
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., situacao: _Optional[str] = ..., tipo_ambiente: _Optional[str] = ..., forma_emissao: _Optional[str] = ..., numero: _Optional[int] = ..., serie: _Optional[int] = ..., chave: _Optional[str] = ..., protocolo: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., data_hora_emissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_autorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., protocolo_encerramento: _Optional[str] = ..., data_hora_encerramento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., protocolo_cancelamento: _Optional[str] = ..., motivo_cancelamento: _Optional[str] = ..., data_hora_cancelamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uf_carregamento: _Optional[str] = ..., uf_descarregamento: _Optional[str] = ..., xml_autorizacao: _Optional[str] = ..., xml_cancelamento: _Optional[str] = ..., tipo_emitente: _Optional[int] = ..., tipo_transportador: _Optional[int] = ..., modalidade: _Optional[int] = ..., rodoviario: _Optional[_Union[Rodoviario, _Mapping]] = ..., rodoviario_reboques: _Optional[_Iterable[_Union[Reboque, _Mapping]]] = ..., valor_carga: _Optional[float] = ..., codigo_unidade: _Optional[str] = ..., peso_bruto_total: _Optional[float] = ..., inf_adicional_fisco: _Optional[str] = ..., inf_adicional_contibuinte: _Optional[str] = ..., historico: _Optional[str] = ..., calcula_total_baseado_notas: _Optional[bool] = ..., condutores: _Optional[_Iterable[_Union[Condutor, _Mapping]]] = ..., carregamentos: _Optional[_Iterable[_Union[Carregamento, _Mapping]]] = ..., percursos: _Optional[_Iterable[_Union[Percurso, _Mapping]]] = ..., descarregamentos: _Optional[_Iterable[_Union[Descarregamento, _Mapping]]] = ..., seguro: _Optional[_Union[Seguro, _Mapping]] = ..., produto_predominante: _Optional[_Union[ProdutoPredominante, _Mapping]] = ..., rejeicoes: _Optional[_Iterable[_Union[Rejeicao, _Mapping]]] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ..., informado_externamente: _Optional[bool] = ...) -> None: ...

class CreateMdfeRequest(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class CreateMdfeResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class UpdateMdfeRequest(_message.Message):
    __slots__ = ("id", "mdfe", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    MDFE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    mdfe: Mdfe
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., mdfe: _Optional[_Union[Mdfe, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMdfeResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class DeleteMdfeRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteMdfeResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMdfeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMdfeResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class ListMdfeRequest(_message.Message):
    __slots__ = ("ids", "placa", "chave", "situacao", "created_at_gte", "created_at_lte", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PLACA_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    placa: str
    chave: str
    situacao: _containers.RepeatedScalarFieldContainer[str]
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., placa: _Optional[str] = ..., chave: _Optional[str] = ..., situacao: _Optional[_Iterable[str]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListMdfeResponse(_message.Message):
    __slots__ = ("mdfe_list", "next_page_token")
    MDFE_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    mdfe_list: _containers.RepeatedCompositeFieldContainer[Mdfe]
    next_page_token: str
    def __init__(self, mdfe_list: _Optional[_Iterable[_Union[Mdfe, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ImprimirMdfeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimirMdfeResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class EnviaEmailWhatsappRequest(_message.Message):
    __slots__ = ("id", "email", "email_integration_id", "whatsapp_numero", "whatsapp_nome_destinatario", "whatsapp_integration_id", "message_template_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMERO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    email_integration_id: str
    whatsapp_numero: str
    whatsapp_nome_destinatario: str
    whatsapp_integration_id: str
    message_template_id: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., whatsapp_numero: _Optional[str] = ..., whatsapp_nome_destinatario: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class EnviaEmailWhatsappResponse(_message.Message):
    __slots__ = ("whatsapp_web_message", "public_download_link")
    WHATSAPP_WEB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    whatsapp_web_message: str
    public_download_link: str
    def __init__(self, whatsapp_web_message: _Optional[str] = ..., public_download_link: _Optional[str] = ...) -> None: ...

class EmitirRequest(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class EmitirResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class CancelarRequest(_message.Message):
    __slots__ = ("id", "motivo_cancelamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo_cancelamento: str
    def __init__(self, id: _Optional[str] = ..., motivo_cancelamento: _Optional[str] = ...) -> None: ...

class CancelarResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class EncerrarRequest(_message.Message):
    __slots__ = ("id", "chave", "protocolo")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    id: str
    chave: str
    protocolo: str
    def __init__(self, id: _Optional[str] = ..., chave: _Optional[str] = ..., protocolo: _Optional[str] = ...) -> None: ...

class EncerrarResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class ImportaXmlRequest(_message.Message):
    __slots__ = ("arquivo_base64",)
    ARQUIVO_BASE64_FIELD_NUMBER: _ClassVar[int]
    arquivo_base64: str
    def __init__(self, arquivo_base64: _Optional[str] = ...) -> None: ...

class ImportaXmlResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...

class RecuperaProtocoloRequest(_message.Message):
    __slots__ = ("chave",)
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    chave: str
    def __init__(self, chave: _Optional[str] = ...) -> None: ...

class RecuperaProtocoloResponse(_message.Message):
    __slots__ = ("mdfe",)
    MDFE_FIELD_NUMBER: _ClassVar[int]
    mdfe: Mdfe
    def __init__(self, mdfe: _Optional[_Union[Mdfe, _Mapping]] = ...) -> None: ...
