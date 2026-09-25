import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdsPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADS_PLATFORM_UNSPECIFIED: _ClassVar[AdsPlatform]
    ADS_PLATFORM_META: _ClassVar[AdsPlatform]
    ADS_PLATFORM_GOOGLE: _ClassVar[AdsPlatform]

class AdsCampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADS_CAMPAIGN_STATUS_UNSPECIFIED: _ClassVar[AdsCampaignStatus]
    ADS_CAMPAIGN_STATUS_ACTIVE: _ClassVar[AdsCampaignStatus]
    ADS_CAMPAIGN_STATUS_PAUSED: _ClassVar[AdsCampaignStatus]
    ADS_CAMPAIGN_STATUS_COMPLETED: _ClassVar[AdsCampaignStatus]
    ADS_CAMPAIGN_STATUS_REMOVED: _ClassVar[AdsCampaignStatus]
    ADS_CAMPAIGN_STATUS_ARCHIVED: _ClassVar[AdsCampaignStatus]
ADS_PLATFORM_UNSPECIFIED: AdsPlatform
ADS_PLATFORM_META: AdsPlatform
ADS_PLATFORM_GOOGLE: AdsPlatform
ADS_CAMPAIGN_STATUS_UNSPECIFIED: AdsCampaignStatus
ADS_CAMPAIGN_STATUS_ACTIVE: AdsCampaignStatus
ADS_CAMPAIGN_STATUS_PAUSED: AdsCampaignStatus
ADS_CAMPAIGN_STATUS_COMPLETED: AdsCampaignStatus
ADS_CAMPAIGN_STATUS_REMOVED: AdsCampaignStatus
ADS_CAMPAIGN_STATUS_ARCHIVED: AdsCampaignStatus

class AdsCampaign(_message.Message):
    __slots__ = ("id", "platform", "external_id", "integration_id", "name", "status", "objective", "campaign_type", "daily_budget", "lifetime_budget", "start_date", "end_date", "currency", "last_sync_at", "total_impressions", "total_reach", "total_clicks", "total_spend", "ctr", "cpc", "cpm", "total_conversions", "daily_metrics", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_TYPE_FIELD_NUMBER: _ClassVar[int]
    DAILY_BUDGET_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_BUDGET_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPEND_FIELD_NUMBER: _ClassVar[int]
    CTR_FIELD_NUMBER: _ClassVar[int]
    CPC_FIELD_NUMBER: _ClassVar[int]
    CPM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    DAILY_METRICS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    platform: AdsPlatform
    external_id: str
    integration_id: str
    name: str
    status: AdsCampaignStatus
    objective: str
    campaign_type: str
    daily_budget: float
    lifetime_budget: float
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp
    currency: str
    last_sync_at: _timestamp_pb2.Timestamp
    total_impressions: int
    total_reach: int
    total_clicks: int
    total_spend: float
    ctr: float
    cpc: float
    cpm: float
    total_conversions: int
    daily_metrics: _containers.RepeatedCompositeFieldContainer[AdsCampaignDailyMetric]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., platform: _Optional[_Union[AdsPlatform, str]] = ..., external_id: _Optional[str] = ..., integration_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[AdsCampaignStatus, str]] = ..., objective: _Optional[str] = ..., campaign_type: _Optional[str] = ..., daily_budget: _Optional[float] = ..., lifetime_budget: _Optional[float] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., last_sync_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_impressions: _Optional[int] = ..., total_reach: _Optional[int] = ..., total_clicks: _Optional[int] = ..., total_spend: _Optional[float] = ..., ctr: _Optional[float] = ..., cpc: _Optional[float] = ..., cpm: _Optional[float] = ..., total_conversions: _Optional[int] = ..., daily_metrics: _Optional[_Iterable[_Union[AdsCampaignDailyMetric, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AdsCampaignDailyMetric(_message.Message):
    __slots__ = ("date", "impressions", "reach", "clicks", "ctr", "cpc", "cpm", "spend", "conversions")
    DATE_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    REACH_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    CTR_FIELD_NUMBER: _ClassVar[int]
    CPC_FIELD_NUMBER: _ClassVar[int]
    CPM_FIELD_NUMBER: _ClassVar[int]
    SPEND_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    date: str
    impressions: int
    reach: int
    clicks: int
    ctr: float
    cpc: float
    cpm: float
    spend: float
    conversions: int
    def __init__(self, date: _Optional[str] = ..., impressions: _Optional[int] = ..., reach: _Optional[int] = ..., clicks: _Optional[int] = ..., ctr: _Optional[float] = ..., cpc: _Optional[float] = ..., cpm: _Optional[float] = ..., spend: _Optional[float] = ..., conversions: _Optional[int] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("ads_campaign",)
    ADS_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ads_campaign: AdsCampaign
    def __init__(self, ads_campaign: _Optional[_Union[AdsCampaign, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("ads_campaign",)
    ADS_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ads_campaign: AdsCampaign
    def __init__(self, ads_campaign: _Optional[_Union[AdsCampaign, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "ads_campaign", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADS_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    ads_campaign: AdsCampaign
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., ads_campaign: _Optional[_Union[AdsCampaign, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("ads_campaign",)
    ADS_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ads_campaign: AdsCampaign
    def __init__(self, ads_campaign: _Optional[_Union[AdsCampaign, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("ads_campaign",)
    ADS_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ads_campaign: AdsCampaign
    def __init__(self, ads_campaign: _Optional[_Union[AdsCampaign, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "platform", "status", "date_from", "date_to", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    platform: AdsPlatform
    status: AdsCampaignStatus
    date_from: str
    date_to: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., platform: _Optional[_Union[AdsPlatform, str]] = ..., status: _Optional[_Union[AdsCampaignStatus, str]] = ..., date_from: _Optional[str] = ..., date_to: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("ads_campaign_list",)
    ADS_CAMPAIGN_LIST_FIELD_NUMBER: _ClassVar[int]
    ads_campaign_list: _containers.RepeatedCompositeFieldContainer[AdsCampaign]
    def __init__(self, ads_campaign_list: _Optional[_Iterable[_Union[AdsCampaign, _Mapping]]] = ...) -> None: ...

class SyncRequest(_message.Message):
    __slots__ = ("platform",)
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    platform: AdsPlatform
    def __init__(self, platform: _Optional[_Union[AdsPlatform, str]] = ...) -> None: ...

class SyncResponse(_message.Message):
    __slots__ = ("campaigns_synced", "campaigns_created", "campaigns_updated", "message")
    CAMPAIGNS_SYNCED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_CREATED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    campaigns_synced: int
    campaigns_created: int
    campaigns_updated: int
    message: str
    def __init__(self, campaigns_synced: _Optional[int] = ..., campaigns_created: _Optional[int] = ..., campaigns_updated: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class GetDashboardRequest(_message.Message):
    __slots__ = ("date_from", "date_to")
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    date_from: str
    date_to: str
    def __init__(self, date_from: _Optional[str] = ..., date_to: _Optional[str] = ...) -> None: ...

class GetDashboardResponse(_message.Message):
    __slots__ = ("total_spend", "total_impressions", "total_clicks", "avg_ctr", "avg_cpc", "active_campaigns", "total_conversions", "spend_by_platform", "daily_spend")
    TOTAL_SPEND_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    AVG_CTR_FIELD_NUMBER: _ClassVar[int]
    AVG_CPC_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    SPEND_BY_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DAILY_SPEND_FIELD_NUMBER: _ClassVar[int]
    total_spend: float
    total_impressions: int
    total_clicks: int
    avg_ctr: float
    avg_cpc: float
    active_campaigns: int
    total_conversions: int
    spend_by_platform: _containers.RepeatedCompositeFieldContainer[PlatformSpend]
    daily_spend: _containers.RepeatedCompositeFieldContainer[DailySpend]
    def __init__(self, total_spend: _Optional[float] = ..., total_impressions: _Optional[int] = ..., total_clicks: _Optional[int] = ..., avg_ctr: _Optional[float] = ..., avg_cpc: _Optional[float] = ..., active_campaigns: _Optional[int] = ..., total_conversions: _Optional[int] = ..., spend_by_platform: _Optional[_Iterable[_Union[PlatformSpend, _Mapping]]] = ..., daily_spend: _Optional[_Iterable[_Union[DailySpend, _Mapping]]] = ...) -> None: ...

class PlatformSpend(_message.Message):
    __slots__ = ("platform", "spend", "impressions", "clicks", "campaigns")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SPEND_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    platform: AdsPlatform
    spend: float
    impressions: int
    clicks: int
    campaigns: int
    def __init__(self, platform: _Optional[_Union[AdsPlatform, str]] = ..., spend: _Optional[float] = ..., impressions: _Optional[int] = ..., clicks: _Optional[int] = ..., campaigns: _Optional[int] = ...) -> None: ...

class DailySpend(_message.Message):
    __slots__ = ("date", "spend", "impressions", "clicks")
    DATE_FIELD_NUMBER: _ClassVar[int]
    SPEND_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    date: str
    spend: float
    impressions: int
    clicks: int
    def __init__(self, date: _Optional[str] = ..., spend: _Optional[float] = ..., impressions: _Optional[int] = ..., clicks: _Optional[int] = ...) -> None: ...

class GetROIRequest(_message.Message):
    __slots__ = ("date_from", "date_to")
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    date_from: str
    date_to: str
    def __init__(self, date_from: _Optional[str] = ..., date_to: _Optional[str] = ...) -> None: ...

class GetROIResponse(_message.Message):
    __slots__ = ("total_ad_spend", "total_revenue", "roi_percentage", "avg_ticket", "total_orders", "previous_period_roi", "daily_roi")
    TOTAL_AD_SPEND_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REVENUE_FIELD_NUMBER: _ClassVar[int]
    ROI_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    AVG_TICKET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ORDERS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PERIOD_ROI_FIELD_NUMBER: _ClassVar[int]
    DAILY_ROI_FIELD_NUMBER: _ClassVar[int]
    total_ad_spend: float
    total_revenue: float
    roi_percentage: float
    avg_ticket: float
    total_orders: int
    previous_period_roi: float
    daily_roi: _containers.RepeatedCompositeFieldContainer[DailyROI]
    def __init__(self, total_ad_spend: _Optional[float] = ..., total_revenue: _Optional[float] = ..., roi_percentage: _Optional[float] = ..., avg_ticket: _Optional[float] = ..., total_orders: _Optional[int] = ..., previous_period_roi: _Optional[float] = ..., daily_roi: _Optional[_Iterable[_Union[DailyROI, _Mapping]]] = ...) -> None: ...

class DailyROI(_message.Message):
    __slots__ = ("date", "ad_spend", "revenue")
    DATE_FIELD_NUMBER: _ClassVar[int]
    AD_SPEND_FIELD_NUMBER: _ClassVar[int]
    REVENUE_FIELD_NUMBER: _ClassVar[int]
    date: str
    ad_spend: float
    revenue: float
    def __init__(self, date: _Optional[str] = ..., ad_spend: _Optional[float] = ..., revenue: _Optional[float] = ...) -> None: ...
