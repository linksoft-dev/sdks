from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASOURCE_TYPE_UNSPECIFIED: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_REST: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_POSTGRES: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_MYSQL: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_MONGODB: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_GRAPHQL: _ClassVar[DataSourceType]
    DATASOURCE_TYPE_REDIS: _ClassVar[DataSourceType]

class AuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_TYPE_NONE: _ClassVar[AuthenticationType]
    AUTH_TYPE_BASIC: _ClassVar[AuthenticationType]
    AUTH_TYPE_BEARER: _ClassVar[AuthenticationType]
    AUTH_TYPE_API_KEY: _ClassVar[AuthenticationType]
    AUTH_TYPE_OAUTH2: _ClassVar[AuthenticationType]

class HTTPMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP_METHOD_GET: _ClassVar[HTTPMethod]
    HTTP_METHOD_POST: _ClassVar[HTTPMethod]
    HTTP_METHOD_PUT: _ClassVar[HTTPMethod]
    HTTP_METHOD_DELETE: _ClassVar[HTTPMethod]
    HTTP_METHOD_PATCH: _ClassVar[HTTPMethod]
DATASOURCE_TYPE_UNSPECIFIED: DataSourceType
DATASOURCE_TYPE_REST: DataSourceType
DATASOURCE_TYPE_POSTGRES: DataSourceType
DATASOURCE_TYPE_MYSQL: DataSourceType
DATASOURCE_TYPE_MONGODB: DataSourceType
DATASOURCE_TYPE_GRAPHQL: DataSourceType
DATASOURCE_TYPE_REDIS: DataSourceType
AUTH_TYPE_NONE: AuthenticationType
AUTH_TYPE_BASIC: AuthenticationType
AUTH_TYPE_BEARER: AuthenticationType
AUTH_TYPE_API_KEY: AuthenticationType
AUTH_TYPE_OAUTH2: AuthenticationType
HTTP_METHOD_GET: HTTPMethod
HTTP_METHOD_POST: HTTPMethod
HTTP_METHOD_PUT: HTTPMethod
HTTP_METHOD_DELETE: HTTPMethod
HTTP_METHOD_PATCH: HTTPMethod

class RestConfig(_message.Message):
    __slots__ = ("method", "headers", "body", "response_field")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METHOD_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_FIELD_NUMBER: _ClassVar[int]
    method: HTTPMethod
    headers: _containers.ScalarMap[str, str]
    body: str
    response_field: str
    def __init__(self, method: _Optional[_Union[HTTPMethod, str]] = ..., headers: _Optional[_Mapping[str, str]] = ..., body: _Optional[str] = ..., response_field: _Optional[str] = ...) -> None: ...

class DatabaseConfig(_message.Message):
    __slots__ = ("connection_string", "max_connections", "connection_timeout", "ssl_enabled")
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    MAX_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SSL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    connection_string: str
    max_connections: int
    connection_timeout: int
    ssl_enabled: bool
    def __init__(self, connection_string: _Optional[str] = ..., max_connections: _Optional[int] = ..., connection_timeout: _Optional[int] = ..., ssl_enabled: _Optional[bool] = ...) -> None: ...

class DataSource(_message.Message):
    __slots__ = ("id", "fields", "name", "description", "type", "url", "active", "auth_type", "username", "password", "token", "api_key", "timeout_seconds", "default_query", "cache_enabled", "cache_ttl_seconds", "tags", "rest_config", "db_config", "extra_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QUERY_FIELD_NUMBER: _ClassVar[int]
    CACHE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CACHE_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    description: str
    type: DataSourceType
    url: str
    active: bool
    auth_type: AuthenticationType
    username: str
    password: str
    token: str
    api_key: str
    timeout_seconds: int
    default_query: str
    cache_enabled: bool
    cache_ttl_seconds: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    rest_config: RestConfig
    db_config: DatabaseConfig
    extra_config: str
    def __init__(self, id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[DataSourceType, str]] = ..., url: _Optional[str] = ..., active: _Optional[bool] = ..., auth_type: _Optional[_Union[AuthenticationType, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., token: _Optional[str] = ..., api_key: _Optional[str] = ..., timeout_seconds: _Optional[int] = ..., default_query: _Optional[str] = ..., cache_enabled: _Optional[bool] = ..., cache_ttl_seconds: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., rest_config: _Optional[_Union[RestConfig, _Mapping]] = ..., db_config: _Optional[_Union[DatabaseConfig, _Mapping]] = ..., extra_config: _Optional[str] = ...) -> None: ...
