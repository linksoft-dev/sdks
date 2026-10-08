import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_TYPE_UNSPECIFIED: _ClassVar[ConversationType]
    CONVERSATION_TYPE_DIRECT: _ClassVar[ConversationType]
CONVERSATION_TYPE_UNSPECIFIED: ConversationType
CONVERSATION_TYPE_DIRECT: ConversationType

class ConversationMember(_message.Message):
    __slots__ = ("id", "conversation_id", "user_id", "type", "participant_ids", "last_message_at", "last_message_preview", "last_message_author_id", "last_read_at", "created_at", "title", "unread")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNREAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    user_id: str
    type: ConversationType
    participant_ids: _containers.RepeatedScalarFieldContainer[str]
    last_message_at: _timestamp_pb2.Timestamp
    last_message_preview: str
    last_message_author_id: str
    last_read_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    title: str
    unread: bool
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., user_id: _Optional[str] = ..., type: _Optional[_Union[ConversationType, str]] = ..., participant_ids: _Optional[_Iterable[str]] = ..., last_message_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_message_preview: _Optional[str] = ..., last_message_author_id: _Optional[str] = ..., last_read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., unread: _Optional[bool] = ...) -> None: ...

class Attachment(_message.Message):
    __slots__ = ("file_id", "file_hash", "link", "name", "content_type", "size")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    file_hash: str
    link: str
    name: str
    content_type: str
    size: int
    def __init__(self, file_id: _Optional[str] = ..., file_hash: _Optional[str] = ..., link: _Optional[str] = ..., name: _Optional[str] = ..., content_type: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class AttachmentUpload(_message.Message):
    __slots__ = ("name", "base64_content", "content_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BASE64_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    base64_content: str
    content_type: str
    def __init__(self, name: _Optional[str] = ..., base64_content: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...

class ReplyPreview(_message.Message):
    __slots__ = ("message_id", "author_name", "content")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    author_name: str
    content: str
    def __init__(self, message_id: _Optional[str] = ..., author_name: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "conversation_id", "author_id", "author_name", "content", "attachments", "reply_to_message_id", "reply_preview", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    author_id: str
    author_name: str
    content: str
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    reply_to_message_id: str
    reply_preview: ReplyPreview
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., author_id: _Optional[str] = ..., author_name: _Optional[str] = ..., content: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., reply_to_message_id: _Optional[str] = ..., reply_preview: _Optional[_Union[ReplyPreview, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ("user_id", "name", "email")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    email: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class ListContactsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListContactsResponse(_message.Message):
    __slots__ = ("contacts",)
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    def __init__(self, contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations", "unread_count")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[ConversationMember]
    unread_count: int
    def __init__(self, conversations: _Optional[_Iterable[_Union[ConversationMember, _Mapping]]] = ..., unread_count: _Optional[int] = ...) -> None: ...

class StartConversationRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class StartConversationResponse(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: ConversationMember
    def __init__(self, conversation: _Optional[_Union[ConversationMember, _Mapping]] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("conversation_id", "skip", "page_size")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    skip: int
    page_size: int
    def __init__(self, conversation_id: _Optional[str] = ..., skip: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "has_more")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    has_more: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., has_more: _Optional[bool] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ("conversation_id", "content", "attachments", "reply_to_message_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    content: str
    attachments: _containers.RepeatedCompositeFieldContainer[AttachmentUpload]
    reply_to_message_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., content: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[AttachmentUpload, _Mapping]]] = ..., reply_to_message_id: _Optional[str] = ...) -> None: ...

class SendMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class MarkReadRequest(_message.Message):
    __slots__ = ("conversation_id",)
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class MarkReadResponse(_message.Message):
    __slots__ = ("unread_count",)
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    unread_count: int
    def __init__(self, unread_count: _Optional[int] = ...) -> None: ...
