import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.apps.config import config_pb2 as _config_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Emitente(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "razao_social", "nome_fantasia", "cnpj", "inscricao_estadual", "inscricao_municipal", "regime_tributario", "cep", "logradouro", "numero", "complemento", "bairro", "cidade", "codigo_municipio", "uf", "pais", "codigo_pais", "telefone", "email", "nfe_habilitado", "nfce_habilitado", "nfse_habilitado", "mdfe_habilitado", "cte_habilitado", "logo_base64", "ie", "contador", "cfop", "tributacao_nome", "tributacao_id", "aliq_icms_calc_dif", "obs", "certificado", "nfe_config", "nfce_config", "mdfe_config", "nfse_config", "cnae_principal", "cnae_secundarios", "cte_config", "fields")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RAZAO_SOCIAL_FIELD_NUMBER: _ClassVar[int]
    NOME_FANTASIA_FIELD_NUMBER: _ClassVar[int]
    CNPJ_FIELD_NUMBER: _ClassVar[int]
    INSCRICAO_ESTADUAL_FIELD_NUMBER: _ClassVar[int]
    INSCRICAO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    REGIME_TRIBUTARIO_FIELD_NUMBER: _ClassVar[int]
    CEP_FIELD_NUMBER: _ClassVar[int]
    LOGRADOURO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
    BAIRRO_FIELD_NUMBER: _ClassVar[int]
    CIDADE_FIELD_NUMBER: _ClassVar[int]
    CODIGO_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    PAIS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_PAIS_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NFE_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    NFCE_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    NFSE_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    MDFE_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    CTE_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    LOGO_BASE64_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    CONTADOR_FIELD_NUMBER: _ClassVar[int]
    CFOP_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_NOME_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_ID_FIELD_NUMBER: _ClassVar[int]
    ALIQ_ICMS_CALC_DIF_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICADO_FIELD_NUMBER: _ClassVar[int]
    NFE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NFCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MDFE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NFSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CNAE_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    CNAE_SECUNDARIOS_FIELD_NUMBER: _ClassVar[int]
    CTE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    razao_social: str
    nome_fantasia: str
    cnpj: str
    inscricao_estadual: str
    inscricao_municipal: str
    regime_tributario: str
    cep: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    codigo_municipio: str
    uf: str
    pais: str
    codigo_pais: str
    telefone: str
    email: str
    nfe_habilitado: bool
    nfce_habilitado: bool
    nfse_habilitado: bool
    mdfe_habilitado: bool
    cte_habilitado: bool
    logo_base64: str
    ie: str
    contador: _config_pb2.Contador
    cfop: str
    tributacao_nome: str
    tributacao_id: str
    aliq_icms_calc_dif: float
    obs: str
    certificado: _config_pb2.CertificadoModel
    nfe_config: _config_pb2.ConfigNfe
    nfce_config: _config_pb2.ConfigNfce
    mdfe_config: _config_pb2.ConfigMdfe
    nfse_config: _config_pb2.ConfigNfse
    cnae_principal: _config_pb2.Cnae
    cnae_secundarios: _containers.RepeatedCompositeFieldContainer[_config_pb2.Cnae]
    cte_config: _config_pb2.ConfigCte
    fields: _metadata_pb2.BasicFields
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., razao_social: _Optional[str] = ..., nome_fantasia: _Optional[str] = ..., cnpj: _Optional[str] = ..., inscricao_estadual: _Optional[str] = ..., inscricao_municipal: _Optional[str] = ..., regime_tributario: _Optional[str] = ..., cep: _Optional[str] = ..., logradouro: _Optional[str] = ..., numero: _Optional[str] = ..., complemento: _Optional[str] = ..., bairro: _Optional[str] = ..., cidade: _Optional[str] = ..., codigo_municipio: _Optional[str] = ..., uf: _Optional[str] = ..., pais: _Optional[str] = ..., codigo_pais: _Optional[str] = ..., telefone: _Optional[str] = ..., email: _Optional[str] = ..., nfe_habilitado: _Optional[bool] = ..., nfce_habilitado: _Optional[bool] = ..., nfse_habilitado: _Optional[bool] = ..., mdfe_habilitado: _Optional[bool] = ..., cte_habilitado: _Optional[bool] = ..., logo_base64: _Optional[str] = ..., ie: _Optional[str] = ..., contador: _Optional[_Union[_config_pb2.Contador, _Mapping]] = ..., cfop: _Optional[str] = ..., tributacao_nome: _Optional[str] = ..., tributacao_id: _Optional[str] = ..., aliq_icms_calc_dif: _Optional[float] = ..., obs: _Optional[str] = ..., certificado: _Optional[_Union[_config_pb2.CertificadoModel, _Mapping]] = ..., nfe_config: _Optional[_Union[_config_pb2.ConfigNfe, _Mapping]] = ..., nfce_config: _Optional[_Union[_config_pb2.ConfigNfce, _Mapping]] = ..., mdfe_config: _Optional[_Union[_config_pb2.ConfigMdfe, _Mapping]] = ..., nfse_config: _Optional[_Union[_config_pb2.ConfigNfse, _Mapping]] = ..., cnae_principal: _Optional[_Union[_config_pb2.Cnae, _Mapping]] = ..., cnae_secundarios: _Optional[_Iterable[_Union[_config_pb2.Cnae, _Mapping]]] = ..., cte_config: _Optional[_Union[_config_pb2.ConfigCte, _Mapping]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...
