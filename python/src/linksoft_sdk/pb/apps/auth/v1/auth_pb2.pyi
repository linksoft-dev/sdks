import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.org import org_pb2 as _org_pb2
from linksoft_sdk.pb.apps.user import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginRequest(_message.Message):
    __slots__ = ("username", "password", "device_id", "org_id")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    device_id: str
    org_id: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., device_id: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("user_id", "name", "email", "current_org", "token", "orgs", "avatar_link", "settings")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ORG_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORGS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LINK_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    email: str
    current_org: orgLoginModel
    token: str
    orgs: _containers.RepeatedCompositeFieldContainer[orgLoginModel]
    avatar_link: str
    settings: _user_pb2.UserSettings
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., current_org: _Optional[_Union[orgLoginModel, _Mapping]] = ..., token: _Optional[str] = ..., orgs: _Optional[_Iterable[_Union[orgLoginModel, _Mapping]]] = ..., avatar_link: _Optional[str] = ..., settings: _Optional[_Union[_user_pb2.UserSettings, _Mapping]] = ...) -> None: ...

class orgLoginModel(_message.Message):
    __slots__ = ("id", "name", "cpf_cnpj", "org_codinome", "licenciamento", "chat_javascript_code", "dados_suporte", "revenda_id", "permissoes", "permissoes_by_key", "revenda_at", "white_label", "is_linksoft", "identification", "portal_slug", "group_id", "group_name")
    class PermissoesByKeyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    ORG_CODINOME_FIELD_NUMBER: _ClassVar[int]
    LICENCIAMENTO_FIELD_NUMBER: _ClassVar[int]
    CHAT_JAVASCRIPT_CODE_FIELD_NUMBER: _ClassVar[int]
    DADOS_SUPORTE_FIELD_NUMBER: _ClassVar[int]
    REVENDA_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSOES_FIELD_NUMBER: _ClassVar[int]
    PERMISSOES_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    REVENDA_AT_FIELD_NUMBER: _ClassVar[int]
    WHITE_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_LINKSOFT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
    PORTAL_SLUG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    cpf_cnpj: str
    org_codinome: str
    licenciamento: _org_pb2.Licenciamento
    chat_javascript_code: str
    dados_suporte: str
    revenda_id: str
    permissoes: str
    permissoes_by_key: _containers.ScalarMap[str, bool]
    revenda_at: _timestamp_pb2.Timestamp
    white_label: _org_pb2.WhiteLabelConfig
    is_linksoft: bool
    identification: str
    portal_slug: str
    group_id: str
    group_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., org_codinome: _Optional[str] = ..., licenciamento: _Optional[_Union[_org_pb2.Licenciamento, _Mapping]] = ..., chat_javascript_code: _Optional[str] = ..., dados_suporte: _Optional[str] = ..., revenda_id: _Optional[str] = ..., permissoes: _Optional[str] = ..., permissoes_by_key: _Optional[_Mapping[str, bool]] = ..., revenda_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., white_label: _Optional[_Union[_org_pb2.WhiteLabelConfig, _Mapping]] = ..., is_linksoft: _Optional[bool] = ..., identification: _Optional[str] = ..., portal_slug: _Optional[str] = ..., group_id: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...
