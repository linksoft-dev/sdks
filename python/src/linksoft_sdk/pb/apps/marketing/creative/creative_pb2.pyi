import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Creative(_message.Message):
    __slots__ = ("id", "name", "source", "channels", "created_at", "updated_at", "html_content", "json_content", "text_content", "template_type", "thumbnail_url", "variables", "tags", "description", "created_by", "updated_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    JSON_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    source: str
    channels: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    html_content: str
    json_content: str
    text_content: str
    template_type: str
    thumbnail_url: str
    variables: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    description: str
    created_by: str
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., source: _Optional[str] = ..., channels: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., html_content: _Optional[str] = ..., json_content: _Optional[str] = ..., text_content: _Optional[str] = ..., template_type: _Optional[str] = ..., thumbnail_url: _Optional[str] = ..., variables: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("creative",)
    CREATIVE_FIELD_NUMBER: _ClassVar[int]
    creative: Creative
    def __init__(self, creative: _Optional[_Union[Creative, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("creative",)
    CREATIVE_FIELD_NUMBER: _ClassVar[int]
    creative: Creative
    def __init__(self, creative: _Optional[_Union[Creative, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "creative", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    creative: Creative
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., creative: _Optional[_Union[Creative, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("creative",)
    CREATIVE_FIELD_NUMBER: _ClassVar[int]
    creative: Creative
    def __init__(self, creative: _Optional[_Union[Creative, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("creative",)
    CREATIVE_FIELD_NUMBER: _ClassVar[int]
    creative: Creative
    def __init__(self, creative: _Optional[_Union[Creative, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "source", "channel", "filter", "template_type", "tags")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    source: str
    channel: str
    filter: _filter_pb2.Filter
    template_type: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., source: _Optional[str] = ..., channel: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., template_type: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("creative_list",)
    CREATIVE_LIST_FIELD_NUMBER: _ClassVar[int]
    creative_list: _containers.RepeatedCompositeFieldContainer[Creative]
    def __init__(self, creative_list: _Optional[_Iterable[_Union[Creative, _Mapping]]] = ...) -> None: ...

class ImportCanvaDesignRequest(_message.Message):
    __slots__ = ("design_id",)
    DESIGN_ID_FIELD_NUMBER: _ClassVar[int]
    design_id: str
    def __init__(self, design_id: _Optional[str] = ...) -> None: ...

class ImportCanvaDesignResponse(_message.Message):
    __slots__ = ("url", "file_id", "title")
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    url: str
    file_id: str
    title: str
    def __init__(self, url: _Optional[str] = ..., file_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
