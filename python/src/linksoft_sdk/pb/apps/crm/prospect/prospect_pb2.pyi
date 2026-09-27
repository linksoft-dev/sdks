from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchCriteria(_message.Message):
    __slots__ = ("name", "city", "state", "region", "sector", "cnae_code", "size_range", "cep", "revenue_min", "revenue_max", "domain", "keywords", "cpf_cnpj", "email", "phone", "page", "page_size", "providers", "exclude_customers", "exclude_leads", "integration_ids")
    class IntegrationIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    CNAE_CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_RANGE_FIELD_NUMBER: _ClassVar[int]
    CEP_FIELD_NUMBER: _ClassVar[int]
    REVENUE_MIN_FIELD_NUMBER: _ClassVar[int]
    REVENUE_MAX_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_LEADS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    city: str
    state: str
    region: str
    sector: str
    cnae_code: str
    size_range: str
    cep: str
    revenue_min: float
    revenue_max: float
    domain: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    cpf_cnpj: str
    email: str
    phone: str
    page: int
    page_size: int
    providers: _containers.RepeatedScalarFieldContainer[str]
    exclude_customers: bool
    exclude_leads: bool
    integration_ids: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., region: _Optional[str] = ..., sector: _Optional[str] = ..., cnae_code: _Optional[str] = ..., size_range: _Optional[str] = ..., cep: _Optional[str] = ..., revenue_min: _Optional[float] = ..., revenue_max: _Optional[float] = ..., domain: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., cpf_cnpj: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., providers: _Optional[_Iterable[str]] = ..., exclude_customers: _Optional[bool] = ..., exclude_leads: _Optional[bool] = ..., integration_ids: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ProspectCompany(_message.Message):
    __slots__ = ("id", "provider", "name", "trade_name", "cpf_cnpj", "email", "phone", "website", "address", "city", "state", "cep", "sector", "cnae_code", "size", "capital", "status", "founded_at", "contacts", "extra_data", "confidence_score", "google_place_id", "rating", "reviews_count", "existing_person_id", "existing_relation")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRADE_NAME_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CEP_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    CNAE_CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CAPITAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FOUNDED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    EXISTING_RELATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    provider: str
    name: str
    trade_name: str
    cpf_cnpj: str
    email: str
    phone: str
    website: str
    address: str
    city: str
    state: str
    cep: str
    sector: str
    cnae_code: str
    size: str
    capital: float
    status: str
    founded_at: str
    contacts: _containers.RepeatedCompositeFieldContainer[ProspectPerson]
    extra_data: _containers.ScalarMap[str, str]
    confidence_score: float
    google_place_id: str
    rating: float
    reviews_count: int
    existing_person_id: str
    existing_relation: str
    def __init__(self, id: _Optional[str] = ..., provider: _Optional[str] = ..., name: _Optional[str] = ..., trade_name: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., website: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., cep: _Optional[str] = ..., sector: _Optional[str] = ..., cnae_code: _Optional[str] = ..., size: _Optional[str] = ..., capital: _Optional[float] = ..., status: _Optional[str] = ..., founded_at: _Optional[str] = ..., contacts: _Optional[_Iterable[_Union[ProspectPerson, _Mapping]]] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., confidence_score: _Optional[float] = ..., google_place_id: _Optional[str] = ..., rating: _Optional[float] = ..., reviews_count: _Optional[int] = ..., existing_person_id: _Optional[str] = ..., existing_relation: _Optional[str] = ...) -> None: ...

class ProspectPerson(_message.Message):
    __slots__ = ("id", "provider", "name", "email", "phone", "title", "company_name", "company_cpf_cnpj", "linkedin_url", "role", "extra_data", "confidence_score")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    LINKEDIN_URL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    id: str
    provider: str
    name: str
    email: str
    phone: str
    title: str
    company_name: str
    company_cpf_cnpj: str
    linkedin_url: str
    role: str
    extra_data: _containers.ScalarMap[str, str]
    confidence_score: float
    def __init__(self, id: _Optional[str] = ..., provider: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., title: _Optional[str] = ..., company_name: _Optional[str] = ..., company_cpf_cnpj: _Optional[str] = ..., linkedin_url: _Optional[str] = ..., role: _Optional[str] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., confidence_score: _Optional[float] = ...) -> None: ...

class ProviderInfo(_message.Message):
    __slots__ = ("name", "display_name", "description", "supports_companies", "supports_people", "supports_enrich_company", "supports_enrich_person", "is_active", "integration_id", "requires_integration")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_ENRICH_COMPANY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_ENRICH_PERSON_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    supports_companies: bool
    supports_people: bool
    supports_enrich_company: bool
    supports_enrich_person: bool
    is_active: bool
    integration_id: str
    requires_integration: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., supports_companies: _Optional[bool] = ..., supports_people: _Optional[bool] = ..., supports_enrich_company: _Optional[bool] = ..., supports_enrich_person: _Optional[bool] = ..., is_active: _Optional[bool] = ..., integration_id: _Optional[str] = ..., requires_integration: _Optional[bool] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("criteria",)
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    criteria: SearchCriteria
    def __init__(self, criteria: _Optional[_Union[SearchCriteria, _Mapping]] = ...) -> None: ...

class SearchCompaniesResponse(_message.Message):
    __slots__ = ("companies", "total_count", "provider_errors", "hidden_customers_count", "hidden_leads_count")
    class ProviderErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ERRORS_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_CUSTOMERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_LEADS_COUNT_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[ProspectCompany]
    total_count: int
    provider_errors: _containers.ScalarMap[str, str]
    hidden_customers_count: int
    hidden_leads_count: int
    def __init__(self, companies: _Optional[_Iterable[_Union[ProspectCompany, _Mapping]]] = ..., total_count: _Optional[int] = ..., provider_errors: _Optional[_Mapping[str, str]] = ..., hidden_customers_count: _Optional[int] = ..., hidden_leads_count: _Optional[int] = ...) -> None: ...

class SearchPeopleResponse(_message.Message):
    __slots__ = ("people", "total_count", "provider_errors")
    class ProviderErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ERRORS_FIELD_NUMBER: _ClassVar[int]
    people: _containers.RepeatedCompositeFieldContainer[ProspectPerson]
    total_count: int
    provider_errors: _containers.ScalarMap[str, str]
    def __init__(self, people: _Optional[_Iterable[_Union[ProspectPerson, _Mapping]]] = ..., total_count: _Optional[int] = ..., provider_errors: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnrichCompanyRequest(_message.Message):
    __slots__ = ("cpf_cnpj", "google_place_id", "domain", "providers", "integration_ids")
    class IntegrationIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_IDS_FIELD_NUMBER: _ClassVar[int]
    cpf_cnpj: str
    google_place_id: str
    domain: str
    providers: _containers.RepeatedScalarFieldContainer[str]
    integration_ids: _containers.ScalarMap[str, str]
    def __init__(self, cpf_cnpj: _Optional[str] = ..., google_place_id: _Optional[str] = ..., domain: _Optional[str] = ..., providers: _Optional[_Iterable[str]] = ..., integration_ids: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnrichCompanyResponse(_message.Message):
    __slots__ = ("company", "provider_errors")
    class ProviderErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ERRORS_FIELD_NUMBER: _ClassVar[int]
    company: ProspectCompany
    provider_errors: _containers.ScalarMap[str, str]
    def __init__(self, company: _Optional[_Union[ProspectCompany, _Mapping]] = ..., provider_errors: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnrichPersonRequest(_message.Message):
    __slots__ = ("email", "name", "company_domain", "providers", "integration_ids", "company_name")
    class IntegrationIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    company_domain: str
    providers: _containers.RepeatedScalarFieldContainer[str]
    integration_ids: _containers.ScalarMap[str, str]
    company_name: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., company_domain: _Optional[str] = ..., providers: _Optional[_Iterable[str]] = ..., integration_ids: _Optional[_Mapping[str, str]] = ..., company_name: _Optional[str] = ...) -> None: ...

class EnrichPersonResponse(_message.Message):
    __slots__ = ("person", "provider_errors", "credits_charged", "credits_balance")
    class ProviderErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PERSON_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CREDITS_CHARGED_FIELD_NUMBER: _ClassVar[int]
    CREDITS_BALANCE_FIELD_NUMBER: _ClassVar[int]
    person: ProspectPerson
    provider_errors: _containers.ScalarMap[str, str]
    credits_charged: int
    credits_balance: int
    def __init__(self, person: _Optional[_Union[ProspectPerson, _Mapping]] = ..., provider_errors: _Optional[_Mapping[str, str]] = ..., credits_charged: _Optional[int] = ..., credits_balance: _Optional[int] = ...) -> None: ...

class SaveAsLeadsRequest(_message.Message):
    __slots__ = ("companies", "people", "tags", "source_provider", "create_deal", "pipeline_id", "stage_id", "expected_value", "responsible_id", "responsible_name", "custom_fields", "create_deal_for_existing")
    class CustomFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CREATE_DEAL_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CREATE_DEAL_FOR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[ProspectCompany]
    people: _containers.RepeatedCompositeFieldContainer[ProspectPerson]
    tags: _containers.RepeatedScalarFieldContainer[str]
    source_provider: str
    create_deal: bool
    pipeline_id: str
    stage_id: str
    expected_value: float
    responsible_id: str
    responsible_name: str
    custom_fields: _containers.ScalarMap[str, str]
    create_deal_for_existing: bool
    def __init__(self, companies: _Optional[_Iterable[_Union[ProspectCompany, _Mapping]]] = ..., people: _Optional[_Iterable[_Union[ProspectPerson, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ..., source_provider: _Optional[str] = ..., create_deal: _Optional[bool] = ..., pipeline_id: _Optional[str] = ..., stage_id: _Optional[str] = ..., expected_value: _Optional[float] = ..., responsible_id: _Optional[str] = ..., responsible_name: _Optional[str] = ..., custom_fields: _Optional[_Mapping[str, str]] = ..., create_deal_for_existing: _Optional[bool] = ...) -> None: ...

class SaveAsLeadsResponse(_message.Message):
    __slots__ = ("saved_count", "skipped_count", "person_ids", "errors", "deal_ids", "deals_created_count")
    SAVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    PERSON_IDS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    DEAL_IDS_FIELD_NUMBER: _ClassVar[int]
    DEALS_CREATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    saved_count: int
    skipped_count: int
    person_ids: _containers.RepeatedScalarFieldContainer[str]
    errors: _containers.RepeatedScalarFieldContainer[str]
    deal_ids: _containers.RepeatedScalarFieldContainer[str]
    deals_created_count: int
    def __init__(self, saved_count: _Optional[int] = ..., skipped_count: _Optional[int] = ..., person_ids: _Optional[_Iterable[str]] = ..., errors: _Optional[_Iterable[str]] = ..., deal_ids: _Optional[_Iterable[str]] = ..., deals_created_count: _Optional[int] = ...) -> None: ...

class ListProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[ProviderInfo]
    def __init__(self, providers: _Optional[_Iterable[_Union[ProviderInfo, _Mapping]]] = ...) -> None: ...

class ProviderAccount(_message.Message):
    __slots__ = ("id", "name", "provider", "origin", "is_default")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    provider: str
    origin: str
    is_default: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[str] = ..., origin: _Optional[str] = ..., is_default: _Optional[bool] = ...) -> None: ...

class ListAccountsRequest(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: str
    def __init__(self, provider: _Optional[str] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[ProviderAccount]
    def __init__(self, accounts: _Optional[_Iterable[_Union[ProviderAccount, _Mapping]]] = ...) -> None: ...
