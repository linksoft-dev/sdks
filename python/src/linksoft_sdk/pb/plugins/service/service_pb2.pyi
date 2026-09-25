from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Boolean(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[Boolean]
    YES: _ClassVar[Boolean]
    NO: _ClassVar[Boolean]
UNSPECIFIED: Boolean
YES: Boolean
NO: Boolean
CRUD_FIELD_NUMBER: _ClassVar[int]
crud: _descriptor.FieldDescriptor
TABLENAME_FIELD_NUMBER: _ClassVar[int]
tableName: _descriptor.FieldDescriptor
PROTOJSONMARSHALING_FIELD_NUMBER: _ClassVar[int]
protojsonMarshaling: _descriptor.FieldDescriptor
FIELD_FIELD_NUMBER: _ClassVar[int]
field: _descriptor.FieldDescriptor

class Field(_message.Message):
    __slots__ = ("upperNoSpaceNoAccent", "upperCase", "trimSpace", "removeAccent", "onlyNumber", "ignoreVersion")
    UPPERNOSPACENOACCENT_FIELD_NUMBER: _ClassVar[int]
    UPPERCASE_FIELD_NUMBER: _ClassVar[int]
    TRIMSPACE_FIELD_NUMBER: _ClassVar[int]
    REMOVEACCENT_FIELD_NUMBER: _ClassVar[int]
    ONLYNUMBER_FIELD_NUMBER: _ClassVar[int]
    IGNOREVERSION_FIELD_NUMBER: _ClassVar[int]
    upperNoSpaceNoAccent: Boolean
    upperCase: Boolean
    trimSpace: Boolean
    removeAccent: Boolean
    onlyNumber: Boolean
    ignoreVersion: Boolean
    def __init__(self, upperNoSpaceNoAccent: _Optional[_Union[Boolean, str]] = ..., upperCase: _Optional[_Union[Boolean, str]] = ..., trimSpace: _Optional[_Union[Boolean, str]] = ..., removeAccent: _Optional[_Union[Boolean, str]] = ..., onlyNumber: _Optional[_Union[Boolean, str]] = ..., ignoreVersion: _Optional[_Union[Boolean, str]] = ...) -> None: ...
