import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomField_FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_FIELD_FIELD_TYPE_UNSPECIFIED: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_TEXT: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_NUMBER: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_DATE: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_SELECT: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_MULTI_SELECT: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_BOOLEAN: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_COLOR: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_IMAGE: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_FILE: _ClassVar[CustomField_FieldType]
    CUSTOM_FIELD_FIELD_TYPE_CRUD: _ClassVar[CustomField_FieldType]
CUSTOM_FIELD_FIELD_TYPE_UNSPECIFIED: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_TEXT: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_NUMBER: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_DATE: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_SELECT: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_MULTI_SELECT: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_BOOLEAN: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_COLOR: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_IMAGE: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_FILE: CustomField_FieldType
CUSTOM_FIELD_FIELD_TYPE_CRUD: CustomField_FieldType

class CustomField(_message.Message):
    __slots__ = ("id", "name", "label", "fieldType", "defaultValue", "required", "options", "entityType", "active", "createdAt", "updatedAt", "fields", "position", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    FIELDTYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENTITYTYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    label: str
    fieldType: CustomField_FieldType
    defaultValue: str
    required: bool
    options: _containers.RepeatedScalarFieldContainer[str]
    entityType: str
    active: bool
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    fields: _metadata_pb2.BasicFields
    position: int
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., label: _Optional[str] = ..., fieldType: _Optional[_Union[CustomField_FieldType, str]] = ..., defaultValue: _Optional[str] = ..., required: _Optional[bool] = ..., options: _Optional[_Iterable[str]] = ..., entityType: _Optional[str] = ..., active: _Optional[bool] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., position: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class CreateCustomFieldRequest(_message.Message):
    __slots__ = ("customField",)
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    customField: CustomField
    def __init__(self, customField: _Optional[_Union[CustomField, _Mapping]] = ...) -> None: ...

class CreateCustomFieldResponse(_message.Message):
    __slots__ = ("customField",)
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    customField: CustomField
    def __init__(self, customField: _Optional[_Union[CustomField, _Mapping]] = ...) -> None: ...

class UpdateCustomFieldRequest(_message.Message):
    __slots__ = ("id", "customField", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    customField: CustomField
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., customField: _Optional[_Union[CustomField, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCustomFieldResponse(_message.Message):
    __slots__ = ("customField",)
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    customField: CustomField
    def __init__(self, customField: _Optional[_Union[CustomField, _Mapping]] = ...) -> None: ...

class DeleteCustomFieldRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCustomFieldResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCustomFieldRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCustomFieldResponse(_message.Message):
    __slots__ = ("customField",)
    CUSTOMFIELD_FIELD_NUMBER: _ClassVar[int]
    customField: CustomField
    def __init__(self, customField: _Optional[_Union[CustomField, _Mapping]] = ...) -> None: ...

class ListCustomFieldRequest(_message.Message):
    __slots__ = ("ids", "filter", "entityType", "entity_types", "only_active")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ENTITYTYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    ONLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    entityType: str
    entity_types: _containers.RepeatedScalarFieldContainer[str]
    only_active: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., entityType: _Optional[str] = ..., entity_types: _Optional[_Iterable[str]] = ..., only_active: _Optional[bool] = ...) -> None: ...

class ListCustomFieldResponse(_message.Message):
    __slots__ = ("customFieldList",)
    CUSTOMFIELDLIST_FIELD_NUMBER: _ClassVar[int]
    customFieldList: _containers.RepeatedCompositeFieldContainer[CustomField]
    def __init__(self, customFieldList: _Optional[_Iterable[_Union[CustomField, _Mapping]]] = ...) -> None: ...

class CustomFieldEntity(_message.Message):
    __slots__ = ("type", "label")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    type: str
    label: str
    def __init__(self, type: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class ListEntityTypesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEntityTypesResponse(_message.Message):
    __slots__ = ("entities",)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[CustomFieldEntity]
    def __init__(self, entities: _Optional[_Iterable[_Union[CustomFieldEntity, _Mapping]]] = ...) -> None: ...
