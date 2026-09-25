import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEAM_STATUS_UNSPECIFIED: _ClassVar[TeamStatus]
    TEAM_STATUS_ACTIVE: _ClassVar[TeamStatus]
    TEAM_STATUS_INACTIVE: _ClassVar[TeamStatus]
    TEAM_STATUS_SUSPENDED: _ClassVar[TeamStatus]

class MemberRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_ROLE_UNSPECIFIED: _ClassVar[MemberRole]
    MEMBER_ROLE_SALESPERSON: _ClassVar[MemberRole]
    MEMBER_ROLE_COORDINATOR: _ClassVar[MemberRole]
    MEMBER_ROLE_SUPERVISOR: _ClassVar[MemberRole]

class MemberStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBER_STATUS_UNSPECIFIED: _ClassVar[MemberStatus]
    MEMBER_STATUS_ACTIVE: _ClassVar[MemberStatus]
    MEMBER_STATUS_INACTIVE: _ClassVar[MemberStatus]
    MEMBER_STATUS_ON_LEAVE: _ClassVar[MemberStatus]

class CurrencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURRENCY_TYPE_UNSPECIFIED: _ClassVar[CurrencyType]
    CURRENCY_TYPE_BRL: _ClassVar[CurrencyType]
    CURRENCY_TYPE_USD: _ClassVar[CurrencyType]
    CURRENCY_TYPE_EUR: _ClassVar[CurrencyType]
    CURRENCY_TYPE_GBP: _ClassVar[CurrencyType]
    CURRENCY_TYPE_CAD: _ClassVar[CurrencyType]
    CURRENCY_TYPE_AUD: _ClassVar[CurrencyType]
    CURRENCY_TYPE_CHF: _ClassVar[CurrencyType]
TEAM_STATUS_UNSPECIFIED: TeamStatus
TEAM_STATUS_ACTIVE: TeamStatus
TEAM_STATUS_INACTIVE: TeamStatus
TEAM_STATUS_SUSPENDED: TeamStatus
MEMBER_ROLE_UNSPECIFIED: MemberRole
MEMBER_ROLE_SALESPERSON: MemberRole
MEMBER_ROLE_COORDINATOR: MemberRole
MEMBER_ROLE_SUPERVISOR: MemberRole
MEMBER_STATUS_UNSPECIFIED: MemberStatus
MEMBER_STATUS_ACTIVE: MemberStatus
MEMBER_STATUS_INACTIVE: MemberStatus
MEMBER_STATUS_ON_LEAVE: MemberStatus
CURRENCY_TYPE_UNSPECIFIED: CurrencyType
CURRENCY_TYPE_BRL: CurrencyType
CURRENCY_TYPE_USD: CurrencyType
CURRENCY_TYPE_EUR: CurrencyType
CURRENCY_TYPE_GBP: CurrencyType
CURRENCY_TYPE_CAD: CurrencyType
CURRENCY_TYPE_AUD: CurrencyType
CURRENCY_TYPE_CHF: CurrencyType

class Team(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "name", "description", "status", "manager_id", "manager_name", "manager_email", "default_configuration", "members", "region", "product_categories", "cost_center", "performance", "tags", "color", "currency_type", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGER_NAME_FIELD_NUMBER: _ClassVar[int]
    MANAGER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    COST_CENTER_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    name: str
    description: str
    status: TeamStatus
    manager_id: str
    manager_name: str
    manager_email: str
    default_configuration: TeamGoalConfiguration
    members: _containers.RepeatedCompositeFieldContainer[TeamMember]
    region: str
    product_categories: _containers.RepeatedScalarFieldContainer[str]
    cost_center: str
    performance: TeamPerformance
    tags: _containers.RepeatedScalarFieldContainer[str]
    color: str
    currency_type: CurrencyType
    fields: _metadata_pb2.BasicFields
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[TeamStatus, str]] = ..., manager_id: _Optional[str] = ..., manager_name: _Optional[str] = ..., manager_email: _Optional[str] = ..., default_configuration: _Optional[_Union[TeamGoalConfiguration, _Mapping]] = ..., members: _Optional[_Iterable[_Union[TeamMember, _Mapping]]] = ..., region: _Optional[str] = ..., product_categories: _Optional[_Iterable[str]] = ..., cost_center: _Optional[str] = ..., performance: _Optional[_Union[TeamPerformance, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., color: _Optional[str] = ..., currency_type: _Optional[_Union[CurrencyType, str]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class TeamGoalConfiguration(_message.Message):
    __slots__ = ("daily_value_goal", "weekly_value_goal", "monthly_value_goal", "quarterly_value_goal", "yearly_value_goal", "daily_sales_quantity", "weekly_sales_quantity", "monthly_sales_quantity", "quarterly_sales_quantity", "yearly_sales_quantity", "use_value_as_criteria", "commission_percentage", "target_margin_percentage", "target_average_ticket")
    DAILY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    QUARTERLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    YEARLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    DAILY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    QUARTERLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    YEARLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    USE_VALUE_AS_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_MARGIN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_AVERAGE_TICKET_FIELD_NUMBER: _ClassVar[int]
    daily_value_goal: float
    weekly_value_goal: float
    monthly_value_goal: float
    quarterly_value_goal: float
    yearly_value_goal: float
    daily_sales_quantity: int
    weekly_sales_quantity: int
    monthly_sales_quantity: int
    quarterly_sales_quantity: int
    yearly_sales_quantity: int
    use_value_as_criteria: bool
    commission_percentage: float
    target_margin_percentage: float
    target_average_ticket: float
    def __init__(self, daily_value_goal: _Optional[float] = ..., weekly_value_goal: _Optional[float] = ..., monthly_value_goal: _Optional[float] = ..., quarterly_value_goal: _Optional[float] = ..., yearly_value_goal: _Optional[float] = ..., daily_sales_quantity: _Optional[int] = ..., weekly_sales_quantity: _Optional[int] = ..., monthly_sales_quantity: _Optional[int] = ..., quarterly_sales_quantity: _Optional[int] = ..., yearly_sales_quantity: _Optional[int] = ..., use_value_as_criteria: _Optional[bool] = ..., commission_percentage: _Optional[float] = ..., target_margin_percentage: _Optional[float] = ..., target_average_ticket: _Optional[float] = ...) -> None: ...

class TeamMember(_message.Message):
    __slots__ = ("id", "salesperson_id", "salesperson_name", "salesperson_email", "joined_date", "left_date", "status", "role", "commission_percentage", "specialties", "performance")
    ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_EMAIL_FIELD_NUMBER: _ClassVar[int]
    JOINED_DATE_FIELD_NUMBER: _ClassVar[int]
    LEFT_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SPECIALTIES_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    salesperson_id: str
    salesperson_name: str
    salesperson_email: str
    joined_date: _timestamp_pb2.Timestamp
    left_date: _timestamp_pb2.Timestamp
    status: MemberStatus
    role: MemberRole
    commission_percentage: float
    specialties: _containers.RepeatedScalarFieldContainer[str]
    performance: MemberPerformance
    def __init__(self, id: _Optional[str] = ..., salesperson_id: _Optional[str] = ..., salesperson_name: _Optional[str] = ..., salesperson_email: _Optional[str] = ..., joined_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., left_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[MemberStatus, str]] = ..., role: _Optional[_Union[MemberRole, str]] = ..., commission_percentage: _Optional[float] = ..., specialties: _Optional[_Iterable[str]] = ..., performance: _Optional[_Union[MemberPerformance, _Mapping]] = ...) -> None: ...

class TeamPerformance(_message.Message):
    __slots__ = ("total_sales_value", "total_sales_quantity", "average_ticket", "margin_percentage", "active_members_count", "daily_performance", "weekly_performance", "monthly_performance", "quarterly_performance", "yearly_performance", "last_update", "team_ranking", "performance_score")
    TOTAL_SALES_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TICKET_FIELD_NUMBER: _ClassVar[int]
    MARGIN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DAILY_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    QUARTERLY_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TEAM_RANKING_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    total_sales_value: float
    total_sales_quantity: int
    average_ticket: float
    margin_percentage: float
    active_members_count: int
    daily_performance: PeriodPerformance
    weekly_performance: PeriodPerformance
    monthly_performance: PeriodPerformance
    quarterly_performance: PeriodPerformance
    yearly_performance: PeriodPerformance
    last_update: _timestamp_pb2.Timestamp
    team_ranking: int
    performance_score: float
    def __init__(self, total_sales_value: _Optional[float] = ..., total_sales_quantity: _Optional[int] = ..., average_ticket: _Optional[float] = ..., margin_percentage: _Optional[float] = ..., active_members_count: _Optional[int] = ..., daily_performance: _Optional[_Union[PeriodPerformance, _Mapping]] = ..., weekly_performance: _Optional[_Union[PeriodPerformance, _Mapping]] = ..., monthly_performance: _Optional[_Union[PeriodPerformance, _Mapping]] = ..., quarterly_performance: _Optional[_Union[PeriodPerformance, _Mapping]] = ..., yearly_performance: _Optional[_Union[PeriodPerformance, _Mapping]] = ..., last_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., team_ranking: _Optional[int] = ..., performance_score: _Optional[float] = ...) -> None: ...

class MemberPerformance(_message.Message):
    __slots__ = ("sales_value", "sales_quantity", "average_ticket", "margin_percentage", "commission_earned", "last_sale_id", "last_sale_value", "last_sale_date", "last_update")
    SALES_VALUE_FIELD_NUMBER: _ClassVar[int]
    SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TICKET_FIELD_NUMBER: _ClassVar[int]
    MARGIN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_EARNED_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    sales_value: float
    sales_quantity: int
    average_ticket: float
    margin_percentage: float
    commission_earned: float
    last_sale_id: str
    last_sale_value: float
    last_sale_date: _timestamp_pb2.Timestamp
    last_update: _timestamp_pb2.Timestamp
    def __init__(self, sales_value: _Optional[float] = ..., sales_quantity: _Optional[int] = ..., average_ticket: _Optional[float] = ..., margin_percentage: _Optional[float] = ..., commission_earned: _Optional[float] = ..., last_sale_id: _Optional[str] = ..., last_sale_value: _Optional[float] = ..., last_sale_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PeriodPerformance(_message.Message):
    __slots__ = ("sales_value", "goal_value", "sales_quantity", "goal_quantity", "achievement_percentage", "period_start", "period_end")
    SALES_VALUE_FIELD_NUMBER: _ClassVar[int]
    GOAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    GOAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    sales_value: float
    goal_value: float
    sales_quantity: int
    goal_quantity: int
    achievement_percentage: float
    period_start: _timestamp_pb2.Timestamp
    period_end: _timestamp_pb2.Timestamp
    def __init__(self, sales_value: _Optional[float] = ..., goal_value: _Optional[float] = ..., sales_quantity: _Optional[int] = ..., goal_quantity: _Optional[int] = ..., achievement_percentage: _Optional[float] = ..., period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateTeamRequest(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class CreateTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class UpdateTeamRequest(_message.Message):
    __slots__ = ("id", "team", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    team: Team
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., team: _Optional[_Union[Team, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class DeleteTeamRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteTeamResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTeamRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTeamResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class ListTeamRequest(_message.Message):
    __slots__ = ("ids", "manager_id", "salesperson_id", "status", "region", "product_categories", "only_active", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    MANAGER_ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ONLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    manager_id: str
    salesperson_id: str
    status: TeamStatus
    region: str
    product_categories: _containers.RepeatedScalarFieldContainer[str]
    only_active: bool
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., manager_id: _Optional[str] = ..., salesperson_id: _Optional[str] = ..., status: _Optional[_Union[TeamStatus, str]] = ..., region: _Optional[str] = ..., product_categories: _Optional[_Iterable[str]] = ..., only_active: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListTeamResponse(_message.Message):
    __slots__ = ("teamList", "next_page_token")
    TEAMLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    teamList: _containers.RepeatedCompositeFieldContainer[Team]
    next_page_token: str
    def __init__(self, teamList: _Optional[_Iterable[_Union[Team, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportTeamRequest(_message.Message):
    __slots__ = ("report_type", "list_team_request", "mail")
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_TEAM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    report_type: str
    list_team_request: ListTeamRequest
    mail: str
    def __init__(self, report_type: _Optional[str] = ..., list_team_request: _Optional[_Union[ListTeamRequest, _Mapping]] = ..., mail: _Optional[str] = ...) -> None: ...

class ReportTeamResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class AddMemberRequest(_message.Message):
    __slots__ = ("team_id", "member")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member: TeamMember
    def __init__(self, team_id: _Optional[str] = ..., member: _Optional[_Union[TeamMember, _Mapping]] = ...) -> None: ...

class AddMemberResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class RemoveMemberRequest(_message.Message):
    __slots__ = ("team_id", "member_id", "reason")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member_id: str
    reason: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class RemoveMemberResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class UpdateMemberRequest(_message.Message):
    __slots__ = ("team_id", "member_id", "member", "update_mask")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member_id: str
    member: TeamMember
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ..., member: _Optional[_Union[TeamMember, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateMemberResponse(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class GetTeamPerformanceRequest(_message.Message):
    __slots__ = ("team_id", "start_date", "end_date", "include_member_details")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MEMBER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    include_member_details: bool
    def __init__(self, team_id: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., include_member_details: _Optional[bool] = ...) -> None: ...

class GetTeamPerformanceResponse(_message.Message):
    __slots__ = ("team_performance", "member_performances")
    TEAM_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PERFORMANCES_FIELD_NUMBER: _ClassVar[int]
    team_performance: TeamPerformance
    member_performances: _containers.RepeatedCompositeFieldContainer[MemberPerformance]
    def __init__(self, team_performance: _Optional[_Union[TeamPerformance, _Mapping]] = ..., member_performances: _Optional[_Iterable[_Union[MemberPerformance, _Mapping]]] = ...) -> None: ...
