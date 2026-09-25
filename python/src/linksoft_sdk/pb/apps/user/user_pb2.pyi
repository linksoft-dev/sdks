from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserOrgSettings(_message.Message):
    __slots__ = ("org_id", "role")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    role: str
    def __init__(self, org_id: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class UserSettings(_message.Message):
    __slots__ = ("disable_auto_find", "user_org_settings", "metadata")
    class UserOrgSettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UserOrgSettings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UserOrgSettings, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISABLE_AUTO_FIND_FIELD_NUMBER: _ClassVar[int]
    USER_ORG_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    disable_auto_find: bool
    user_org_settings: _containers.MessageMap[str, UserOrgSettings]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, disable_auto_find: _Optional[bool] = ..., user_org_settings: _Optional[_Mapping[str, UserOrgSettings]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
