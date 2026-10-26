from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("id", "pdf_base64", "html_content", "template", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    PDF_BASE64_FIELD_NUMBER: _ClassVar[int]
    HTML_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    pdf_base64: str
    html_content: str
    template: str
    data: str
    def __init__(self, id: _Optional[str] = ..., pdf_base64: _Optional[str] = ..., html_content: _Optional[str] = ..., template: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...
