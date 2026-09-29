import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.exports import exports_pb2 as _exports_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERSON_STATUS_UNSPECIFIED: _ClassVar[PersonStatus]
    PERSON_STATUS_ACTIVE: _ClassVar[PersonStatus]
    PERSON_STATUS_INACTIVE: _ClassVar[PersonStatus]

class LeadStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEAD_STAGE_UNSPECIFIED: _ClassVar[LeadStage]
    LEAD_STAGE_NEW: _ClassVar[LeadStage]
    LEAD_STAGE_CONTACTED: _ClassVar[LeadStage]
    LEAD_STAGE_QUALIFIED: _ClassVar[LeadStage]
    LEAD_STAGE_PROPOSAL: _ClassVar[LeadStage]
    LEAD_STAGE_NEGOTIATION: _ClassVar[LeadStage]
    LEAD_STAGE_WON: _ClassVar[LeadStage]
    LEAD_STAGE_LOST: _ClassVar[LeadStage]

class LeadQualification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LEAD_QUALIFICATION_UNSPECIFIED: _ClassVar[LeadQualification]
    LEAD_QUALIFICATION_COLD: _ClassVar[LeadQualification]
    LEAD_QUALIFICATION_WARM: _ClassVar[LeadQualification]
    LEAD_QUALIFICATION_HOT: _ClassVar[LeadQualification]

class ContactChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTACT_CHANNEL_UNSPECIFIED: _ClassVar[ContactChannel]
    CONTACT_CHANNEL_EMAIL: _ClassVar[ContactChannel]
    CONTACT_CHANNEL_PHONE: _ClassVar[ContactChannel]
PERSON_STATUS_UNSPECIFIED: PersonStatus
PERSON_STATUS_ACTIVE: PersonStatus
PERSON_STATUS_INACTIVE: PersonStatus
LEAD_STAGE_UNSPECIFIED: LeadStage
LEAD_STAGE_NEW: LeadStage
LEAD_STAGE_CONTACTED: LeadStage
LEAD_STAGE_QUALIFIED: LeadStage
LEAD_STAGE_PROPOSAL: LeadStage
LEAD_STAGE_NEGOTIATION: LeadStage
LEAD_STAGE_WON: LeadStage
LEAD_STAGE_LOST: LeadStage
LEAD_QUALIFICATION_UNSPECIFIED: LeadQualification
LEAD_QUALIFICATION_COLD: LeadQualification
LEAD_QUALIFICATION_WARM: LeadQualification
LEAD_QUALIFICATION_HOT: LeadQualification
CONTACT_CHANNEL_UNSPECIFIED: ContactChannel
CONTACT_CHANNEL_EMAIL: ContactChannel
CONTACT_CHANNEL_PHONE: ContactChannel

class PersonTag(_message.Message):
    __slots__ = ("value", "color")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    value: str
    color: str
    def __init__(self, value: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class Person(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "resale", "status", "tags", "name", "name2", "cpf_cnpj", "codigo", "pai", "mae", "nascimento", "ident", "ident_free", "obs", "address", "ies", "contacts", "dependents", "cliente", "vendedor", "grupo_id", "grupo_nome", "usuario_id", "usuario_nome", "driver", "lead", "carrier", "specialty", "registration_number", "require_valid_carteirinha", "fields", "photo_url", "show_in_portal", "authorization_payment_minutes", "authorization_requires_schedule", "custom_fields", "specialties")
    class IesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RESALE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME2_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    PAI_FIELD_NUMBER: _ClassVar[int]
    MAE_FIELD_NUMBER: _ClassVar[int]
    NASCIMENTO_FIELD_NUMBER: _ClassVar[int]
    IDENT_FIELD_NUMBER: _ClassVar[int]
    IDENT_FREE_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IES_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    DEPENDENTS_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    VENDEDOR_FIELD_NUMBER: _ClassVar[int]
    GRUPO_ID_FIELD_NUMBER: _ClassVar[int]
    GRUPO_NOME_FIELD_NUMBER: _ClassVar[int]
    USUARIO_ID_FIELD_NUMBER: _ClassVar[int]
    USUARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    LEAD_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    SPECIALTY_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_VALID_CARTEIRINHA_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: _ClassVar[int]
    SHOW_IN_PORTAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_PAYMENT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_REQUIRES_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SPECIALTIES_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    resale: bool
    status: PersonStatus
    tags: _containers.RepeatedCompositeFieldContainer[PersonTag]
    name: str
    name2: str
    cpf_cnpj: str
    codigo: str
    pai: str
    mae: str
    nascimento: _timestamp_pb2.Timestamp
    ident: str
    ident_free: bool
    obs: str
    address: _containers.RepeatedCompositeFieldContainer[Address]
    ies: _containers.ScalarMap[str, str]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    dependents: _containers.RepeatedCompositeFieldContainer[Dependent]
    cliente: Cliente
    vendedor: Vendedor
    grupo_id: str
    grupo_nome: str
    usuario_id: str
    usuario_nome: str
    driver: Driver
    lead: Lead
    carrier: Carrier
    specialty: str
    registration_number: str
    require_valid_carteirinha: bool
    fields: _metadata_pb2.BasicFields
    photo_url: str
    show_in_portal: bool
    authorization_payment_minutes: int
    authorization_requires_schedule: bool
    custom_fields: _containers.ScalarMap[str, str]
    specialties: _containers.RepeatedCompositeFieldContainer[Specialty]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., resale: _Optional[bool] = ..., status: _Optional[_Union[PersonStatus, str]] = ..., tags: _Optional[_Iterable[_Union[PersonTag, _Mapping]]] = ..., name: _Optional[str] = ..., name2: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., codigo: _Optional[str] = ..., pai: _Optional[str] = ..., mae: _Optional[str] = ..., nascimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ident: _Optional[str] = ..., ident_free: _Optional[bool] = ..., obs: _Optional[str] = ..., address: _Optional[_Iterable[_Union[Address, _Mapping]]] = ..., ies: _Optional[_Mapping[str, str]] = ..., contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]] = ..., dependents: _Optional[_Iterable[_Union[Dependent, _Mapping]]] = ..., cliente: _Optional[_Union[Cliente, _Mapping]] = ..., vendedor: _Optional[_Union[Vendedor, _Mapping]] = ..., grupo_id: _Optional[str] = ..., grupo_nome: _Optional[str] = ..., usuario_id: _Optional[str] = ..., usuario_nome: _Optional[str] = ..., driver: _Optional[_Union[Driver, _Mapping]] = ..., lead: _Optional[_Union[Lead, _Mapping]] = ..., carrier: _Optional[_Union[Carrier, _Mapping]] = ..., specialty: _Optional[str] = ..., registration_number: _Optional[str] = ..., require_valid_carteirinha: _Optional[bool] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., photo_url: _Optional[str] = ..., show_in_portal: _Optional[bool] = ..., authorization_payment_minutes: _Optional[int] = ..., authorization_requires_schedule: _Optional[bool] = ..., custom_fields: _Optional[_Mapping[str, str]] = ..., specialties: _Optional[_Iterable[_Union[Specialty, _Mapping]]] = ...) -> None: ...

class Specialty(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Carrier(_message.Message):
    __slots__ = ("provider_code", "integration_id", "services")
    PROVIDER_CODE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    provider_code: str
    integration_id: str
    services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, provider_code: _Optional[str] = ..., integration_id: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ...) -> None: ...

class Lead(_message.Message):
    __slots__ = ("source", "source_provider", "stage", "qualification", "score", "assigned_to_id", "assigned_to_name", "expected_value", "expected_close_date", "loss_reason", "converted_at", "converted_deal_id", "sector", "company_size", "website", "rating", "notes")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    QUALIFICATION_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_TO_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_TO_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CLOSE_DATE_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASON_FIELD_NUMBER: _ClassVar[int]
    CONVERTED_AT_FIELD_NUMBER: _ClassVar[int]
    CONVERTED_DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    COMPANY_SIZE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    source: str
    source_provider: str
    stage: LeadStage
    qualification: LeadQualification
    score: int
    assigned_to_id: str
    assigned_to_name: str
    expected_value: float
    expected_close_date: _timestamp_pb2.Timestamp
    loss_reason: str
    converted_at: _timestamp_pb2.Timestamp
    converted_deal_id: str
    sector: str
    company_size: str
    website: str
    rating: float
    notes: str
    def __init__(self, source: _Optional[str] = ..., source_provider: _Optional[str] = ..., stage: _Optional[_Union[LeadStage, str]] = ..., qualification: _Optional[_Union[LeadQualification, str]] = ..., score: _Optional[int] = ..., assigned_to_id: _Optional[str] = ..., assigned_to_name: _Optional[str] = ..., expected_value: _Optional[float] = ..., expected_close_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., loss_reason: _Optional[str] = ..., converted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., converted_deal_id: _Optional[str] = ..., sector: _Optional[str] = ..., company_size: _Optional[str] = ..., website: _Optional[str] = ..., rating: _Optional[float] = ..., notes: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("id", "types", "address", "zip_code", "number", "city", "city_code", "neighborhood", "state", "state_ident")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    CITY_CODE_FIELD_NUMBER: _ClassVar[int]
    NEIGHBORHOOD_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_IDENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    types: _containers.RepeatedScalarFieldContainer[str]
    address: str
    zip_code: str
    number: str
    city: str
    city_code: str
    neighborhood: str
    state: str
    state_ident: str
    def __init__(self, id: _Optional[str] = ..., types: _Optional[_Iterable[str]] = ..., address: _Optional[str] = ..., zip_code: _Optional[str] = ..., number: _Optional[str] = ..., city: _Optional[str] = ..., city_code: _Optional[str] = ..., neighborhood: _Optional[str] = ..., state: _Optional[str] = ..., state_ident: _Optional[str] = ...) -> None: ...

class SendContactVerificationRequest(_message.Message):
    __slots__ = ("person_id", "contact_id", "channel")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    contact_id: str
    channel: ContactChannel
    def __init__(self, person_id: _Optional[str] = ..., contact_id: _Optional[str] = ..., channel: _Optional[_Union[ContactChannel, str]] = ...) -> None: ...

class SendContactVerificationResponse(_message.Message):
    __slots__ = ("msg", "sent_to")
    MSG_FIELD_NUMBER: _ClassVar[int]
    SENT_TO_FIELD_NUMBER: _ClassVar[int]
    msg: str
    sent_to: str
    def __init__(self, msg: _Optional[str] = ..., sent_to: _Optional[str] = ...) -> None: ...

class ConfirmContactVerificationRequest(_message.Message):
    __slots__ = ("person_id", "contact_id", "code")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    contact_id: str
    code: str
    def __init__(self, person_id: _Optional[str] = ..., contact_id: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ConfirmContactVerificationResponse(_message.Message):
    __slots__ = ("msg", "contact")
    MSG_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    msg: str
    contact: Contact
    def __init__(self, msg: _Optional[str] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ...) -> None: ...

class VouchContactRequest(_message.Message):
    __slots__ = ("person_id", "contact_id", "channel")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    contact_id: str
    channel: ContactChannel
    def __init__(self, person_id: _Optional[str] = ..., contact_id: _Optional[str] = ..., channel: _Optional[_Union[ContactChannel, str]] = ...) -> None: ...

class VouchContactResponse(_message.Message):
    __slots__ = ("msg", "contact")
    MSG_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    msg: str
    contact: Contact
    def __init__(self, msg: _Optional[str] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ("id", "name", "email", "phone", "by_whats_app", "by_sms", "by_email", "email_verified_at", "phone_verified_at", "email_vouch", "phone_vouch", "verification_code", "verification_channel")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    BY_WHATS_APP_FIELD_NUMBER: _ClassVar[int]
    BY_SMS_FIELD_NUMBER: _ClassVar[int]
    BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VOUCH_FIELD_NUMBER: _ClassVar[int]
    PHONE_VOUCH_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    phone: str
    by_whats_app: bool
    by_sms: bool
    by_email: bool
    email_verified_at: _timestamp_pb2.Timestamp
    phone_verified_at: _timestamp_pb2.Timestamp
    email_vouch: ContactVouch
    phone_vouch: ContactVouch
    verification_code: str
    verification_channel: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., by_whats_app: _Optional[bool] = ..., by_sms: _Optional[bool] = ..., by_email: _Optional[bool] = ..., email_verified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., phone_verified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., email_vouch: _Optional[_Union[ContactVouch, _Mapping]] = ..., phone_vouch: _Optional[_Union[ContactVouch, _Mapping]] = ..., verification_code: _Optional[str] = ..., verification_channel: _Optional[str] = ...) -> None: ...

class ContactVouch(_message.Message):
    __slots__ = ("at", "user_id", "user_name")
    AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    def __init__(self, at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class Dependent(_message.Message):
    __slots__ = ("id", "person_id", "person_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    person_id: str
    person_name: str
    def __init__(self, id: _Optional[str] = ..., person_id: _Optional[str] = ..., person_name: _Optional[str] = ...) -> None: ...

class Vendedor(_message.Message):
    __slots__ = ("comissao", "limite_variacao_preco_min", "limite_variacao_preco_max", "desconto_maximo")
    COMISSAO_FIELD_NUMBER: _ClassVar[int]
    LIMITE_VARIACAO_PRECO_MIN_FIELD_NUMBER: _ClassVar[int]
    LIMITE_VARIACAO_PRECO_MAX_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_MAXIMO_FIELD_NUMBER: _ClassVar[int]
    comissao: float
    limite_variacao_preco_min: float
    limite_variacao_preco_max: float
    desconto_maximo: float
    def __init__(self, comissao: _Optional[float] = ..., limite_variacao_preco_min: _Optional[float] = ..., limite_variacao_preco_max: _Optional[float] = ..., desconto_maximo: _Optional[float] = ...) -> None: ...

class Cliente(_message.Message):
    __slots__ = ("vendedor_id", "vendedor_nome", "limite_credito", "saldo_devedor", "credito_disponivel")
    VENDEDOR_ID_FIELD_NUMBER: _ClassVar[int]
    VENDEDOR_NOME_FIELD_NUMBER: _ClassVar[int]
    LIMITE_CREDITO_FIELD_NUMBER: _ClassVar[int]
    SALDO_DEVEDOR_FIELD_NUMBER: _ClassVar[int]
    CREDITO_DISPONIVEL_FIELD_NUMBER: _ClassVar[int]
    vendedor_id: str
    vendedor_nome: str
    limite_credito: float
    saldo_devedor: float
    credito_disponivel: float
    def __init__(self, vendedor_id: _Optional[str] = ..., vendedor_nome: _Optional[str] = ..., limite_credito: _Optional[float] = ..., saldo_devedor: _Optional[float] = ..., credito_disponivel: _Optional[float] = ...) -> None: ...

class Driver(_message.Message):
    __slots__ = ("license_number", "license_expiration", "birth_date")
    LICENSE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LICENSE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    license_number: str
    license_expiration: _timestamp_pb2.Timestamp
    birth_date: _timestamp_pb2.Timestamp
    def __init__(self, license_number: _Optional[str] = ..., license_expiration: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., birth_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("person",)
    PERSON_FIELD_NUMBER: _ClassVar[int]
    person: Person
    def __init__(self, person: _Optional[_Union[Person, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("person",)
    PERSON_FIELD_NUMBER: _ClassVar[int]
    person: Person
    def __init__(self, person: _Optional[_Union[Person, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "person", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    person: Person
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., person: _Optional[_Union[Person, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("person",)
    PERSON_FIELD_NUMBER: _ClassVar[int]
    person: Person
    def __init__(self, person: _Optional[_Union[Person, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id", "avisos")
    ID_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("person",)
    PERSON_FIELD_NUMBER: _ClassVar[int]
    person: Person
    def __init__(self, person: _Optional[_Union[Person, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "cpf_cnpjs", "names", "created_at_gte", "created_at_lte", "limite_credito_gte", "limite_credito_lte", "uf", "cidade", "contact_name", "ident", "codigo", "grupo_id", "grupo_nome", "tipo", "page_size", "page_token", "users_ids", "filter", "lead_stage", "lead_qualification", "lead_source", "ignore_default_status", "ie")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJS_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    LIMITE_CREDITO_GTE_FIELD_NUMBER: _ClassVar[int]
    LIMITE_CREDITO_LTE_FIELD_NUMBER: _ClassVar[int]
    UF_FIELD_NUMBER: _ClassVar[int]
    CIDADE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_NAME_FIELD_NUMBER: _ClassVar[int]
    IDENT_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    GRUPO_ID_FIELD_NUMBER: _ClassVar[int]
    GRUPO_NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERS_IDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LEAD_STAGE_FIELD_NUMBER: _ClassVar[int]
    LEAD_QUALIFICATION_FIELD_NUMBER: _ClassVar[int]
    LEAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEFAULT_STATUS_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    cpf_cnpjs: _containers.RepeatedScalarFieldContainer[str]
    names: _containers.RepeatedScalarFieldContainer[str]
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    limite_credito_gte: float
    limite_credito_lte: float
    uf: str
    cidade: str
    contact_name: str
    ident: str
    codigo: str
    grupo_id: str
    grupo_nome: str
    tipo: str
    page_size: int
    page_token: str
    users_ids: _containers.RepeatedScalarFieldContainer[str]
    filter: _filter_pb2.Filter
    lead_stage: str
    lead_qualification: str
    lead_source: str
    ignore_default_status: bool
    ie: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., cpf_cnpjs: _Optional[_Iterable[str]] = ..., names: _Optional[_Iterable[str]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limite_credito_gte: _Optional[float] = ..., limite_credito_lte: _Optional[float] = ..., uf: _Optional[str] = ..., cidade: _Optional[str] = ..., contact_name: _Optional[str] = ..., ident: _Optional[str] = ..., codigo: _Optional[str] = ..., grupo_id: _Optional[str] = ..., grupo_nome: _Optional[str] = ..., tipo: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., users_ids: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., lead_stage: _Optional[str] = ..., lead_qualification: _Optional[str] = ..., lead_source: _Optional[str] = ..., ignore_default_status: _Optional[bool] = ..., ie: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("person_list", "next_page_token")
    PERSON_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    person_list: _containers.RepeatedCompositeFieldContainer[Person]
    next_page_token: str
    def __init__(self, person_list: _Optional[_Iterable[_Union[Person, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("persons", "file_string", "file_name", "cliente", "fornecedor")
    PERSONS_FIELD_NUMBER: _ClassVar[int]
    FILE_STRING_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    FORNECEDOR_FIELD_NUMBER: _ClassVar[int]
    persons: _containers.RepeatedCompositeFieldContainer[Person]
    file_string: str
    file_name: str
    cliente: bool
    fornecedor: bool
    def __init__(self, persons: _Optional[_Iterable[_Union[Person, _Mapping]]] = ..., file_string: _Optional[str] = ..., file_name: _Optional[str] = ..., cliente: _Optional[bool] = ..., fornecedor: _Optional[bool] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ("result", "error", "success_count", "failed_count", "validation_errors")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    result: str
    error: str
    success_count: int
    failed_count: int
    validation_errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[str] = ..., error: _Optional[str] = ..., success_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., validation_errors: _Optional[_Iterable[str]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "list_request", "mail")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    list_request: ListRequest
    mail: str
    def __init__(self, tipo_relatorio: _Optional[str] = ..., list_request: _Optional[_Union[ListRequest, _Mapping]] = ..., mail: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ExportPersonsRequest(_message.Message):
    __slots__ = ("format", "filter", "include_metadata", "only_customers", "only_vendors")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ONLY_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    ONLY_VENDORS_FIELD_NUMBER: _ClassVar[int]
    format: _exports_pb2.ExportFormat
    filter: _filter_pb2.Filter
    include_metadata: bool
    only_customers: bool
    only_vendors: bool
    def __init__(self, format: _Optional[_Union[_exports_pb2.ExportFormat, str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., include_metadata: _Optional[bool] = ..., only_customers: _Optional[bool] = ..., only_vendors: _Optional[bool] = ...) -> None: ...

class ExportPersonsResponse(_message.Message):
    __slots__ = ("export",)
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    export: _exports_pb2.ExportResponse
    def __init__(self, export: _Optional[_Union[_exports_pb2.ExportResponse, _Mapping]] = ...) -> None: ...

class BatchUpdateFilter(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchUpdateSeller(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class BatchUpdateRequest(_message.Message):
    __slots__ = ("filter", "seller")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SELLER_FIELD_NUMBER: _ClassVar[int]
    filter: BatchUpdateFilter
    seller: BatchUpdateSeller
    def __init__(self, filter: _Optional[_Union[BatchUpdateFilter, _Mapping]] = ..., seller: _Optional[_Union[BatchUpdateSeller, _Mapping]] = ...) -> None: ...

class BatchUpdateResponse(_message.Message):
    __slots__ = ("updated_count", "status")
    UPDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    updated_count: int
    status: str
    def __init__(self, updated_count: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...
