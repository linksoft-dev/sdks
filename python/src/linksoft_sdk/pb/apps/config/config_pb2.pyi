import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AmbientePadrao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AMBIENTE_PADRAO_UNSPECIFIED: _ClassVar[AmbientePadrao]
    AMBIENTE_PADRAO_PRODUCAO: _ClassVar[AmbientePadrao]
    AMBIENTE_PADRAO_HOMOLOGACAO: _ClassVar[AmbientePadrao]
AMBIENTE_PADRAO_UNSPECIFIED: AmbientePadrao
AMBIENTE_PADRAO_PRODUCAO: AmbientePadrao
AMBIENTE_PADRAO_HOMOLOGACAO: AmbientePadrao

class Contador(_message.Message):
    __slots__ = ("id", "nome", "cpf_cnpj", "cnpj_escritorio", "ie", "isento_ie", "end_cep", "end_endereco", "end_numero", "end_bairro", "end_cidade", "end_cidade_codigo", "end_uf", "telefone", "email", "enviar_nfe_por_email", "crc")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    CNPJ_ESCRITORIO_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    ISENTO_IE_FIELD_NUMBER: _ClassVar[int]
    END_CEP_FIELD_NUMBER: _ClassVar[int]
    END_ENDERECO_FIELD_NUMBER: _ClassVar[int]
    END_NUMERO_FIELD_NUMBER: _ClassVar[int]
    END_BAIRRO_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_CODIGO_FIELD_NUMBER: _ClassVar[int]
    END_UF_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ENVIAR_NFE_POR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    cpf_cnpj: str
    cnpj_escritorio: str
    ie: str
    isento_ie: bool
    end_cep: str
    end_endereco: str
    end_numero: str
    end_bairro: str
    end_cidade: str
    end_cidade_codigo: str
    end_uf: str
    telefone: str
    email: str
    enviar_nfe_por_email: bool
    crc: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., cnpj_escritorio: _Optional[str] = ..., ie: _Optional[str] = ..., isento_ie: _Optional[bool] = ..., end_cep: _Optional[str] = ..., end_endereco: _Optional[str] = ..., end_numero: _Optional[str] = ..., end_bairro: _Optional[str] = ..., end_cidade: _Optional[str] = ..., end_cidade_codigo: _Optional[str] = ..., end_uf: _Optional[str] = ..., telefone: _Optional[str] = ..., email: _Optional[str] = ..., enviar_nfe_por_email: _Optional[bool] = ..., crc: _Optional[str] = ...) -> None: ...

class CertificadoModel(_message.Message):
    __slots__ = ("arquivo_nome", "validade", "senha", "conteudo_upload", "download_link")
    ARQUIVO_NOME_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_FIELD_NUMBER: _ClassVar[int]
    SENHA_FIELD_NUMBER: _ClassVar[int]
    CONTEUDO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    arquivo_nome: str
    validade: _timestamp_pb2.Timestamp
    senha: str
    conteudo_upload: str
    download_link: str
    def __init__(self, arquivo_nome: _Optional[str] = ..., validade: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., senha: _Optional[str] = ..., conteudo_upload: _Optional[str] = ..., download_link: _Optional[str] = ...) -> None: ...

class ConfigNfe(_message.Message):
    __slots__ = ("ambiente_padrao", "serie_padrao", "data_hora_status", "entrada_consulta_bloqueada_ate", "entrada_nsu", "entrada_busca_automatica", "auto_atualiza_preco", "entrada_vincula_itens_ia", "entrada_politica_preco_ia")
    AMBIENTE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    SERIE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_CONSULTA_BLOQUEADA_ATE_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_NSU_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_BUSCA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    AUTO_ATUALIZA_PRECO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_VINCULA_ITENS_IA_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_POLITICA_PRECO_IA_FIELD_NUMBER: _ClassVar[int]
    ambiente_padrao: str
    serie_padrao: int
    data_hora_status: _timestamp_pb2.Timestamp
    entrada_consulta_bloqueada_ate: _timestamp_pb2.Timestamp
    entrada_nsu: int
    entrada_busca_automatica: bool
    auto_atualiza_preco: bool
    entrada_vincula_itens_ia: bool
    entrada_politica_preco_ia: str
    def __init__(self, ambiente_padrao: _Optional[str] = ..., serie_padrao: _Optional[int] = ..., data_hora_status: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entrada_consulta_bloqueada_ate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entrada_nsu: _Optional[int] = ..., entrada_busca_automatica: _Optional[bool] = ..., auto_atualiza_preco: _Optional[bool] = ..., entrada_vincula_itens_ia: _Optional[bool] = ..., entrada_politica_preco_ia: _Optional[str] = ...) -> None: ...

class ConfigNfce(_message.Message):
    __slots__ = ("ambiente_padrao", "serie_padrao", "data_hora_status", "entrada_consulta_bloqueada_ate", "entrada_nsu", "entrada_busca_automatica", "auto_atualiza_preco", "csc", "token")
    AMBIENTE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    SERIE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_CONSULTA_BLOQUEADA_ATE_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_NSU_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_BUSCA_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    AUTO_ATUALIZA_PRECO_FIELD_NUMBER: _ClassVar[int]
    CSC_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ambiente_padrao: str
    serie_padrao: int
    data_hora_status: _timestamp_pb2.Timestamp
    entrada_consulta_bloqueada_ate: _timestamp_pb2.Timestamp
    entrada_nsu: int
    entrada_busca_automatica: bool
    auto_atualiza_preco: bool
    csc: str
    token: int
    def __init__(self, ambiente_padrao: _Optional[str] = ..., serie_padrao: _Optional[int] = ..., data_hora_status: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entrada_consulta_bloqueada_ate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entrada_nsu: _Optional[int] = ..., entrada_busca_automatica: _Optional[bool] = ..., auto_atualiza_preco: _Optional[bool] = ..., csc: _Optional[str] = ..., token: _Optional[int] = ...) -> None: ...

class ConfigMdfe(_message.Message):
    __slots__ = ("ambiente_padrao", "serie_padrao")
    AMBIENTE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    SERIE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    ambiente_padrao: str
    serie_padrao: int
    def __init__(self, ambiente_padrao: _Optional[str] = ..., serie_padrao: _Optional[int] = ...) -> None: ...

class ConfigCte(_message.Message):
    __slots__ = ("ambiente_padrao", "serie_padrao", "serie")
    AMBIENTE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    SERIE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    ambiente_padrao: AmbientePadrao
    serie_padrao: int
    serie: int
    def __init__(self, ambiente_padrao: _Optional[_Union[AmbientePadrao, str]] = ..., serie_padrao: _Optional[int] = ..., serie: _Optional[int] = ...) -> None: ...

class ConfigNfse(_message.Message):
    __slots__ = ("ambiente_padrao", "iss", "reg_ap_trib_sn", "nfse_auto_emite", "serie_padrao", "envia_email_automatico", "webservice_usuario", "webservice_senha")
    AMBIENTE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    ISS_FIELD_NUMBER: _ClassVar[int]
    REG_AP_TRIB_SN_FIELD_NUMBER: _ClassVar[int]
    NFSE_AUTO_EMITE_FIELD_NUMBER: _ClassVar[int]
    SERIE_PADRAO_FIELD_NUMBER: _ClassVar[int]
    ENVIA_EMAIL_AUTOMATICO_FIELD_NUMBER: _ClassVar[int]
    WEBSERVICE_USUARIO_FIELD_NUMBER: _ClassVar[int]
    WEBSERVICE_SENHA_FIELD_NUMBER: _ClassVar[int]
    ambiente_padrao: AmbientePadrao
    iss: float
    reg_ap_trib_sn: int
    nfse_auto_emite: bool
    serie_padrao: str
    envia_email_automatico: bool
    webservice_usuario: str
    webservice_senha: str
    def __init__(self, ambiente_padrao: _Optional[_Union[AmbientePadrao, str]] = ..., iss: _Optional[float] = ..., reg_ap_trib_sn: _Optional[int] = ..., nfse_auto_emite: _Optional[bool] = ..., serie_padrao: _Optional[str] = ..., envia_email_automatico: _Optional[bool] = ..., webservice_usuario: _Optional[str] = ..., webservice_senha: _Optional[str] = ...) -> None: ...

class Cnae(_message.Message):
    __slots__ = ("nome", "codigo")
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    nome: str
    codigo: str
    def __init__(self, nome: _Optional[str] = ..., codigo: _Optional[str] = ...) -> None: ...
