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

class GoalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOAL_STATUS_UNSPECIFIED: _ClassVar[GoalStatus]
    GOAL_STATUS_ACTIVE: _ClassVar[GoalStatus]
    GOAL_STATUS_INACTIVE: _ClassVar[GoalStatus]
    GOAL_STATUS_FINISHED: _ClassVar[GoalStatus]

class RewardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REWARD_TYPE_UNSPECIFIED: _ClassVar[RewardType]
    REWARD_TYPE_BRONZE: _ClassVar[RewardType]
    REWARD_TYPE_SILVER: _ClassVar[RewardType]
    REWARD_TYPE_GOLD: _ClassVar[RewardType]

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

class GoalBasis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOAL_BASIS_DOCUMENT: _ClassVar[GoalBasis]
    GOAL_BASIS_PAYMENT: _ClassVar[GoalBasis]
GOAL_STATUS_UNSPECIFIED: GoalStatus
GOAL_STATUS_ACTIVE: GoalStatus
GOAL_STATUS_INACTIVE: GoalStatus
GOAL_STATUS_FINISHED: GoalStatus
REWARD_TYPE_UNSPECIFIED: RewardType
REWARD_TYPE_BRONZE: RewardType
REWARD_TYPE_SILVER: RewardType
REWARD_TYPE_GOLD: RewardType
CURRENCY_TYPE_UNSPECIFIED: CurrencyType
CURRENCY_TYPE_BRL: CurrencyType
CURRENCY_TYPE_USD: CurrencyType
CURRENCY_TYPE_EUR: CurrencyType
CURRENCY_TYPE_GBP: CurrencyType
CURRENCY_TYPE_CAD: CurrencyType
CURRENCY_TYPE_AUD: CurrencyType
CURRENCY_TYPE_CHF: CurrencyType
GOAL_BASIS_DOCUMENT: GoalBasis
GOAL_BASIS_PAYMENT: GoalBasis

class Goal(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "name", "description", "status", "start_date", "end_date", "team_id", "team_name", "team_configuration", "salespeople", "rewards", "progress", "currency_type", "fields", "basis")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SALESPEOPLE_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    BASIS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    name: str
    description: str
    status: GoalStatus
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    team_id: str
    team_name: str
    team_configuration: TeamGoalConfiguration
    salespeople: _containers.RepeatedCompositeFieldContainer[SalespersonGoal]
    rewards: _containers.RepeatedCompositeFieldContainer[Reward]
    progress: GoalProgress
    currency_type: CurrencyType
    fields: _metadata_pb2.BasicFields
    basis: GoalBasis
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[GoalStatus, str]] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., team_id: _Optional[str] = ..., team_name: _Optional[str] = ..., team_configuration: _Optional[_Union[TeamGoalConfiguration, _Mapping]] = ..., salespeople: _Optional[_Iterable[_Union[SalespersonGoal, _Mapping]]] = ..., rewards: _Optional[_Iterable[_Union[Reward, _Mapping]]] = ..., progress: _Optional[_Union[GoalProgress, _Mapping]] = ..., currency_type: _Optional[_Union[CurrencyType, str]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., basis: _Optional[_Union[GoalBasis, str]] = ...) -> None: ...

class TeamGoalConfiguration(_message.Message):
    __slots__ = ("daily_value_goal", "weekly_value_goal", "monthly_value_goal", "daily_sales_quantity", "weekly_sales_quantity", "monthly_sales_quantity", "use_value_as_criteria")
    DAILY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    DAILY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    USE_VALUE_AS_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    daily_value_goal: float
    weekly_value_goal: float
    monthly_value_goal: float
    daily_sales_quantity: int
    weekly_sales_quantity: int
    monthly_sales_quantity: int
    use_value_as_criteria: bool
    def __init__(self, daily_value_goal: _Optional[float] = ..., weekly_value_goal: _Optional[float] = ..., monthly_value_goal: _Optional[float] = ..., daily_sales_quantity: _Optional[int] = ..., weekly_sales_quantity: _Optional[int] = ..., monthly_sales_quantity: _Optional[int] = ..., use_value_as_criteria: _Optional[bool] = ...) -> None: ...

class SalespersonGoal(_message.Message):
    __slots__ = ("salesperson_id", "salesperson_name", "daily_value_goal", "weekly_value_goal", "monthly_value_goal", "daily_sales_quantity", "weekly_sales_quantity", "monthly_sales_quantity", "progress", "achieved_rewards")
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    DAILY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_VALUE_GOAL_FIELD_NUMBER: _ClassVar[int]
    DAILY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SALES_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_REWARDS_FIELD_NUMBER: _ClassVar[int]
    salesperson_id: str
    salesperson_name: str
    daily_value_goal: float
    weekly_value_goal: float
    monthly_value_goal: float
    daily_sales_quantity: int
    weekly_sales_quantity: int
    monthly_sales_quantity: int
    progress: SalespersonProgress
    achieved_rewards: _containers.RepeatedCompositeFieldContainer[AchievedReward]
    def __init__(self, salesperson_id: _Optional[str] = ..., salesperson_name: _Optional[str] = ..., daily_value_goal: _Optional[float] = ..., weekly_value_goal: _Optional[float] = ..., monthly_value_goal: _Optional[float] = ..., daily_sales_quantity: _Optional[int] = ..., weekly_sales_quantity: _Optional[int] = ..., monthly_sales_quantity: _Optional[int] = ..., progress: _Optional[_Union[SalespersonProgress, _Mapping]] = ..., achieved_rewards: _Optional[_Iterable[_Union[AchievedReward, _Mapping]]] = ...) -> None: ...

class Reward(_message.Message):
    __slots__ = ("id", "name", "description", "type", "required_goal_percentage", "required_minimum_value", "required_minimum_quantity", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_GOAL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_MINIMUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_MINIMUM_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    type: RewardType
    required_goal_percentage: float
    required_minimum_value: float
    required_minimum_quantity: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[RewardType, str]] = ..., required_goal_percentage: _Optional[float] = ..., required_minimum_value: _Optional[float] = ..., required_minimum_quantity: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class AchievedReward(_message.Message):
    __slots__ = ("reward_id", "reward_name", "type", "achieved_date", "achieved_value", "achieved_quantity", "achieved_percentage", "tags")
    REWARD_ID_FIELD_NUMBER: _ClassVar[int]
    REWARD_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_DATE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    reward_id: str
    reward_name: str
    type: RewardType
    achieved_date: _timestamp_pb2.Timestamp
    achieved_value: float
    achieved_quantity: int
    achieved_percentage: float
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, reward_id: _Optional[str] = ..., reward_name: _Optional[str] = ..., type: _Optional[_Union[RewardType, str]] = ..., achieved_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., achieved_value: _Optional[float] = ..., achieved_quantity: _Optional[int] = ..., achieved_percentage: _Optional[float] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class GoalProgress(_message.Message):
    __slots__ = ("total_achieved_value", "total_goal_value", "total_achieved_quantity", "total_goal_quantity", "achieved_percentage", "last_update", "daily_progress", "weekly_progress", "monthly_progress")
    TOTAL_ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GOAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GOAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DAILY_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    total_achieved_value: float
    total_goal_value: float
    total_achieved_quantity: int
    total_goal_quantity: int
    achieved_percentage: float
    last_update: _timestamp_pb2.Timestamp
    daily_progress: PeriodProgress
    weekly_progress: PeriodProgress
    monthly_progress: PeriodProgress
    def __init__(self, total_achieved_value: _Optional[float] = ..., total_goal_value: _Optional[float] = ..., total_achieved_quantity: _Optional[int] = ..., total_goal_quantity: _Optional[int] = ..., achieved_percentage: _Optional[float] = ..., last_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., daily_progress: _Optional[_Union[PeriodProgress, _Mapping]] = ..., weekly_progress: _Optional[_Union[PeriodProgress, _Mapping]] = ..., monthly_progress: _Optional[_Union[PeriodProgress, _Mapping]] = ...) -> None: ...

class SalespersonProgress(_message.Message):
    __slots__ = ("daily_achieved_value", "weekly_achieved_value", "monthly_achieved_value", "daily_achieved_quantity", "weekly_achieved_quantity", "monthly_achieved_quantity", "daily_percentage", "weekly_percentage", "monthly_percentage", "last_update", "last_sale_id", "last_sale_value", "last_sale_date")
    DAILY_ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    DAILY_ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DAILY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LAST_SALE_DATE_FIELD_NUMBER: _ClassVar[int]
    daily_achieved_value: float
    weekly_achieved_value: float
    monthly_achieved_value: float
    daily_achieved_quantity: int
    weekly_achieved_quantity: int
    monthly_achieved_quantity: int
    daily_percentage: float
    weekly_percentage: float
    monthly_percentage: float
    last_update: _timestamp_pb2.Timestamp
    last_sale_id: str
    last_sale_value: float
    last_sale_date: _timestamp_pb2.Timestamp
    def __init__(self, daily_achieved_value: _Optional[float] = ..., weekly_achieved_value: _Optional[float] = ..., monthly_achieved_value: _Optional[float] = ..., daily_achieved_quantity: _Optional[int] = ..., weekly_achieved_quantity: _Optional[int] = ..., monthly_achieved_quantity: _Optional[int] = ..., daily_percentage: _Optional[float] = ..., weekly_percentage: _Optional[float] = ..., monthly_percentage: _Optional[float] = ..., last_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_sale_id: _Optional[str] = ..., last_sale_value: _Optional[float] = ..., last_sale_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PeriodProgress(_message.Message):
    __slots__ = ("achieved_value", "goal_value", "achieved_quantity", "goal_quantity", "percentage", "period_start_date", "period_end_date")
    ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    GOAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    GOAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_DATE_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_DATE_FIELD_NUMBER: _ClassVar[int]
    achieved_value: float
    goal_value: float
    achieved_quantity: int
    goal_quantity: int
    percentage: float
    period_start_date: _timestamp_pb2.Timestamp
    period_end_date: _timestamp_pb2.Timestamp
    def __init__(self, achieved_value: _Optional[float] = ..., goal_value: _Optional[float] = ..., achieved_quantity: _Optional[int] = ..., goal_quantity: _Optional[int] = ..., percentage: _Optional[float] = ..., period_start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., period_end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateGoalRequest(_message.Message):
    __slots__ = ("goal",)
    GOAL_FIELD_NUMBER: _ClassVar[int]
    goal: Goal
    def __init__(self, goal: _Optional[_Union[Goal, _Mapping]] = ...) -> None: ...

class CreateGoalResponse(_message.Message):
    __slots__ = ("goal",)
    GOAL_FIELD_NUMBER: _ClassVar[int]
    goal: Goal
    def __init__(self, goal: _Optional[_Union[Goal, _Mapping]] = ...) -> None: ...

class UpdateGoalRequest(_message.Message):
    __slots__ = ("id", "goal", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    goal: Goal
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., goal: _Optional[_Union[Goal, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateGoalResponse(_message.Message):
    __slots__ = ("goal",)
    GOAL_FIELD_NUMBER: _ClassVar[int]
    goal: Goal
    def __init__(self, goal: _Optional[_Union[Goal, _Mapping]] = ...) -> None: ...

class DeleteGoalRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteGoalResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGoalRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGoalResponse(_message.Message):
    __slots__ = ("goal",)
    GOAL_FIELD_NUMBER: _ClassVar[int]
    goal: Goal
    def __init__(self, goal: _Optional[_Union[Goal, _Mapping]] = ...) -> None: ...

class ListGoalRequest(_message.Message):
    __slots__ = ("ids", "team_id", "salesperson_id", "status", "start_date_gte", "start_date_lte", "end_date_gte", "end_date_lte", "only_active", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    ONLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    team_id: str
    salesperson_id: str
    status: GoalStatus
    start_date_gte: _timestamp_pb2.Timestamp
    start_date_lte: _timestamp_pb2.Timestamp
    end_date_gte: _timestamp_pb2.Timestamp
    end_date_lte: _timestamp_pb2.Timestamp
    only_active: bool
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., team_id: _Optional[str] = ..., salesperson_id: _Optional[str] = ..., status: _Optional[_Union[GoalStatus, str]] = ..., start_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., start_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., only_active: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListGoalResponse(_message.Message):
    __slots__ = ("goalList", "next_page_token")
    GOALLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    goalList: _containers.RepeatedCompositeFieldContainer[Goal]
    next_page_token: str
    def __init__(self, goalList: _Optional[_Iterable[_Union[Goal, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportGoalRequest(_message.Message):
    __slots__ = ("report_type", "list_goal_request", "mail")
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_GOAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    report_type: str
    list_goal_request: ListGoalRequest
    mail: str
    def __init__(self, report_type: _Optional[str] = ..., list_goal_request: _Optional[_Union[ListGoalRequest, _Mapping]] = ..., mail: _Optional[str] = ...) -> None: ...

class ReportGoalResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class UpdateProgressRequest(_message.Message):
    __slots__ = ("goal_id", "salesperson_id", "sale_id", "sale_value", "sale_date")
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SALE_DATE_FIELD_NUMBER: _ClassVar[int]
    goal_id: str
    salesperson_id: str
    sale_id: str
    sale_value: float
    sale_date: _timestamp_pb2.Timestamp
    def __init__(self, goal_id: _Optional[str] = ..., salesperson_id: _Optional[str] = ..., sale_id: _Optional[str] = ..., sale_value: _Optional[float] = ..., sale_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateProgressResponse(_message.Message):
    __slots__ = ("updated_progress", "new_rewards")
    UPDATED_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    NEW_REWARDS_FIELD_NUMBER: _ClassVar[int]
    updated_progress: SalespersonProgress
    new_rewards: _containers.RepeatedCompositeFieldContainer[AchievedReward]
    def __init__(self, updated_progress: _Optional[_Union[SalespersonProgress, _Mapping]] = ..., new_rewards: _Optional[_Iterable[_Union[AchievedReward, _Mapping]]] = ...) -> None: ...

class RecalculateProgressRequest(_message.Message):
    __slots__ = ("goal_id",)
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    goal_id: str
    def __init__(self, goal_id: _Optional[str] = ...) -> None: ...

class RecalculateProgressResponse(_message.Message):
    __slots__ = ("goal", "vendas_consideradas")
    GOAL_FIELD_NUMBER: _ClassVar[int]
    VENDAS_CONSIDERADAS_FIELD_NUMBER: _ClassVar[int]
    goal: Goal
    vendas_consideradas: int
    def __init__(self, goal: _Optional[_Union[Goal, _Mapping]] = ..., vendas_consideradas: _Optional[int] = ...) -> None: ...

class ReplicateGoalRequest(_message.Message):
    __slots__ = ("goal_id", "months")
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    goal_id: str
    months: int
    def __init__(self, goal_id: _Optional[str] = ..., months: _Optional[int] = ...) -> None: ...

class ReplicateGoalResponse(_message.Message):
    __slots__ = ("goals",)
    GOALS_FIELD_NUMBER: _ClassVar[int]
    goals: _containers.RepeatedCompositeFieldContainer[Goal]
    def __init__(self, goals: _Optional[_Iterable[_Union[Goal, _Mapping]]] = ...) -> None: ...

class GetSalespersonProgressRequest(_message.Message):
    __slots__ = ("salesperson_id", "start_date", "end_date", "include_rewards_history")
    SALESPERSON_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REWARDS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    salesperson_id: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    include_rewards_history: bool
    def __init__(self, salesperson_id: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., include_rewards_history: _Optional[bool] = ...) -> None: ...

class GetSalespersonProgressResponse(_message.Message):
    __slots__ = ("salesperson_goals", "total_achieved_value", "total_achieved_quantity", "average_achieved_percentage", "rewards_history")
    SALESPERSON_GOALS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACHIEVED_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACHIEVED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ACHIEVED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    REWARDS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    salesperson_goals: _containers.RepeatedCompositeFieldContainer[SalespersonGoal]
    total_achieved_value: float
    total_achieved_quantity: int
    average_achieved_percentage: float
    rewards_history: _containers.RepeatedCompositeFieldContainer[AchievedReward]
    def __init__(self, salesperson_goals: _Optional[_Iterable[_Union[SalespersonGoal, _Mapping]]] = ..., total_achieved_value: _Optional[float] = ..., total_achieved_quantity: _Optional[int] = ..., average_achieved_percentage: _Optional[float] = ..., rewards_history: _Optional[_Iterable[_Union[AchievedReward, _Mapping]]] = ...) -> None: ...
