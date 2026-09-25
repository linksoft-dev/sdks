import datetime

from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_APPROVAL_STATUS_UNSPECIFIED: _ClassVar[FileApprovalStatus]
    FILE_APPROVAL_STATUS_PENDING: _ClassVar[FileApprovalStatus]
    FILE_APPROVAL_STATUS_APPROVED: _ClassVar[FileApprovalStatus]
    FILE_APPROVAL_STATUS_REJECTED: _ClassVar[FileApprovalStatus]
FILE_APPROVAL_STATUS_UNSPECIFIED: FileApprovalStatus
FILE_APPROVAL_STATUS_PENDING: FileApprovalStatus
FILE_APPROVAL_STATUS_APPROVED: FileApprovalStatus
FILE_APPROVAL_STATUS_REJECTED: FileApprovalStatus

class File(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "path", "file_id", "file_name", "file_extension", "file_size", "content_type", "temp", "file_hash", "file_type", "path_table", "base64_content", "history", "name", "link", "bucket_name", "provider", "provider_link", "actions", "download_count", "is_public", "approval_status", "approval_note")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMP_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_TABLE_FIELD_NUMBER: _ClassVar[int]
    BASE64_CONTENT_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_LINK_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    path: str
    file_id: str
    file_name: str
    file_extension: str
    file_size: int
    content_type: str
    temp: bool
    file_hash: str
    file_type: str
    path_table: str
    base64_content: str
    history: _containers.RepeatedCompositeFieldContainer[FileHistory]
    name: str
    link: str
    bucket_name: str
    provider: str
    provider_link: str
    actions: _containers.RepeatedCompositeFieldContainer[FileAction]
    download_count: int
    is_public: bool
    approval_status: FileApprovalStatus
    approval_note: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., path: _Optional[str] = ..., file_id: _Optional[str] = ..., file_name: _Optional[str] = ..., file_extension: _Optional[str] = ..., file_size: _Optional[int] = ..., content_type: _Optional[str] = ..., temp: _Optional[bool] = ..., file_hash: _Optional[str] = ..., file_type: _Optional[str] = ..., path_table: _Optional[str] = ..., base64_content: _Optional[str] = ..., history: _Optional[_Iterable[_Union[FileHistory, _Mapping]]] = ..., name: _Optional[str] = ..., link: _Optional[str] = ..., bucket_name: _Optional[str] = ..., provider: _Optional[str] = ..., provider_link: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[FileAction, _Mapping]]] = ..., download_count: _Optional[int] = ..., is_public: _Optional[bool] = ..., approval_status: _Optional[_Union[FileApprovalStatus, str]] = ..., approval_note: _Optional[str] = ...) -> None: ...

class FileAction(_message.Message):
    __slots__ = ("action_type", "timestamp", "origin", "user_id", "user_name", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    timestamp: _timestamp_pb2.Timestamp
    origin: str
    user_id: str
    user_name: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, action_type: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., origin: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class FileHistory(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "created_by", "updated_by", "action")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    updated_by: str
    action: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...
