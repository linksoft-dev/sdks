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

class SocialNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOCIAL_NETWORK_UNSPECIFIED: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_INSTAGRAM: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_FACEBOOK: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_X: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_LINKEDIN: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_TIKTOK: _ClassVar[SocialNetwork]
    SOCIAL_NETWORK_THREADS: _ClassVar[SocialNetwork]

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POST_STATUS_UNSPECIFIED: _ClassVar[PostStatus]
    POST_STATUS_DRAFT: _ClassVar[PostStatus]
    POST_STATUS_SCHEDULED: _ClassVar[PostStatus]
    POST_STATUS_PARTIALLY_PUBLISHED: _ClassVar[PostStatus]
    POST_STATUS_PUBLISHED: _ClassVar[PostStatus]
    POST_STATUS_FAILED: _ClassVar[PostStatus]

class PublicationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLICATION_STATUS_UNSPECIFIED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_DRAFT: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_SCHEDULED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_PUBLISHING: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_PUBLISHED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_FAILED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_CANCELLED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_REMOVED: _ClassVar[PublicationStatus]
    PUBLICATION_STATUS_UNPUBLISHED: _ClassVar[PublicationStatus]

class ApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPROVAL_STATUS_UNSPECIFIED: _ClassVar[ApprovalStatus]
    APPROVAL_STATUS_PENDING: _ClassVar[ApprovalStatus]
    APPROVAL_STATUS_APPROVED: _ClassVar[ApprovalStatus]
    APPROVAL_STATUS_CHANGES_REQUESTED: _ClassVar[ApprovalStatus]

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNSPECIFIED: _ClassVar[MediaType]
    MEDIA_TYPE_IMAGE: _ClassVar[MediaType]
    MEDIA_TYPE_VIDEO: _ClassVar[MediaType]
SOCIAL_NETWORK_UNSPECIFIED: SocialNetwork
SOCIAL_NETWORK_INSTAGRAM: SocialNetwork
SOCIAL_NETWORK_FACEBOOK: SocialNetwork
SOCIAL_NETWORK_X: SocialNetwork
SOCIAL_NETWORK_LINKEDIN: SocialNetwork
SOCIAL_NETWORK_TIKTOK: SocialNetwork
SOCIAL_NETWORK_THREADS: SocialNetwork
POST_STATUS_UNSPECIFIED: PostStatus
POST_STATUS_DRAFT: PostStatus
POST_STATUS_SCHEDULED: PostStatus
POST_STATUS_PARTIALLY_PUBLISHED: PostStatus
POST_STATUS_PUBLISHED: PostStatus
POST_STATUS_FAILED: PostStatus
PUBLICATION_STATUS_UNSPECIFIED: PublicationStatus
PUBLICATION_STATUS_DRAFT: PublicationStatus
PUBLICATION_STATUS_SCHEDULED: PublicationStatus
PUBLICATION_STATUS_PUBLISHING: PublicationStatus
PUBLICATION_STATUS_PUBLISHED: PublicationStatus
PUBLICATION_STATUS_FAILED: PublicationStatus
PUBLICATION_STATUS_CANCELLED: PublicationStatus
PUBLICATION_STATUS_REMOVED: PublicationStatus
PUBLICATION_STATUS_UNPUBLISHED: PublicationStatus
APPROVAL_STATUS_UNSPECIFIED: ApprovalStatus
APPROVAL_STATUS_PENDING: ApprovalStatus
APPROVAL_STATUS_APPROVED: ApprovalStatus
APPROVAL_STATUS_CHANGES_REQUESTED: ApprovalStatus
MEDIA_TYPE_UNSPECIFIED: MediaType
MEDIA_TYPE_IMAGE: MediaType
MEDIA_TYPE_VIDEO: MediaType

class Media(_message.Message):
    __slots__ = ("id", "file_id", "url", "type", "position", "thumbnail_url", "alt_text", "file_name", "file_size", "media_origin", "canva_design_id", "canva_export_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    CANVA_DESIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CANVA_EXPORT_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_id: str
    url: str
    type: MediaType
    position: int
    thumbnail_url: str
    alt_text: str
    file_name: str
    file_size: int
    media_origin: str
    canva_design_id: str
    canva_export_url: str
    def __init__(self, id: _Optional[str] = ..., file_id: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[MediaType, str]] = ..., position: _Optional[int] = ..., thumbnail_url: _Optional[str] = ..., alt_text: _Optional[str] = ..., file_name: _Optional[str] = ..., file_size: _Optional[int] = ..., media_origin: _Optional[str] = ..., canva_design_id: _Optional[str] = ..., canva_export_url: _Optional[str] = ...) -> None: ...

class Publication(_message.Message):
    __slots__ = ("id", "network", "integration_id", "account_name", "account_avatar", "scheduled_at", "publish_now", "status", "external_post_id", "external_url", "error_message", "published_at", "custom_content", "custom_hashtags", "created_at", "updated_at", "likes", "comments_count", "shares", "impressions", "saves", "clicks", "metrics_updated_at", "reach", "views", "profile_visits", "follows", "video_watch_time_seconds", "ads_campaign_id", "ads_campaign_name", "paid_spend", "paid_impressions", "paid_clicks", "paid_conversions", "paid_revenue", "paid_roi", "boost_source", "publish_origin")
    ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AVATAR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_NOW_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARES_FIELD_NUMBER: _ClassVar[int]
    IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    SAVES_FIELD_NUMBER: _ClassVar[int]
    CLICKS_FIELD_NUMBER: _ClassVar[int]
    METRICS_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REACH_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_VISITS_FIELD_NUMBER: _ClassVar[int]
    FOLLOWS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_WATCH_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ADS_CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ADS_CAMPAIGN_NAME_FIELD_NUMBER: _ClassVar[int]
    PAID_SPEND_FIELD_NUMBER: _ClassVar[int]
    PAID_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    PAID_CLICKS_FIELD_NUMBER: _ClassVar[int]
    PAID_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    PAID_REVENUE_FIELD_NUMBER: _ClassVar[int]
    PAID_ROI_FIELD_NUMBER: _ClassVar[int]
    BOOST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    network: SocialNetwork
    integration_id: str
    account_name: str
    account_avatar: str
    scheduled_at: _timestamp_pb2.Timestamp
    publish_now: bool
    status: PublicationStatus
    external_post_id: str
    external_url: str
    error_message: str
    published_at: _timestamp_pb2.Timestamp
    custom_content: str
    custom_hashtags: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    likes: int
    comments_count: int
    shares: int
    impressions: int
    saves: int
    clicks: int
    metrics_updated_at: _timestamp_pb2.Timestamp
    reach: int
    views: int
    profile_visits: int
    follows: int
    video_watch_time_seconds: int
    ads_campaign_id: str
    ads_campaign_name: str
    paid_spend: float
    paid_impressions: int
    paid_clicks: int
    paid_conversions: int
    paid_revenue: float
    paid_roi: float
    boost_source: str
    publish_origin: str
    def __init__(self, id: _Optional[str] = ..., network: _Optional[_Union[SocialNetwork, str]] = ..., integration_id: _Optional[str] = ..., account_name: _Optional[str] = ..., account_avatar: _Optional[str] = ..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., publish_now: _Optional[bool] = ..., status: _Optional[_Union[PublicationStatus, str]] = ..., external_post_id: _Optional[str] = ..., external_url: _Optional[str] = ..., error_message: _Optional[str] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., custom_content: _Optional[str] = ..., custom_hashtags: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., likes: _Optional[int] = ..., comments_count: _Optional[int] = ..., shares: _Optional[int] = ..., impressions: _Optional[int] = ..., saves: _Optional[int] = ..., clicks: _Optional[int] = ..., metrics_updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reach: _Optional[int] = ..., views: _Optional[int] = ..., profile_visits: _Optional[int] = ..., follows: _Optional[int] = ..., video_watch_time_seconds: _Optional[int] = ..., ads_campaign_id: _Optional[str] = ..., ads_campaign_name: _Optional[str] = ..., paid_spend: _Optional[float] = ..., paid_impressions: _Optional[int] = ..., paid_clicks: _Optional[int] = ..., paid_conversions: _Optional[int] = ..., paid_revenue: _Optional[float] = ..., paid_roi: _Optional[float] = ..., boost_source: _Optional[str] = ..., publish_origin: _Optional[str] = ...) -> None: ...

class SocialPost(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "content", "hashtags", "medias", "publications", "status", "title", "created_by", "updated_by", "total_interactions", "tags", "created_by_name", "ai_generated", "ai_provider", "ai_model", "language", "number", "intelligence_goal", "total_impressions", "total_clicks", "total_saves", "engagement_rate", "click_through_rate", "intelligence_score", "performance_level", "score_summary", "score_reasons", "recommendations", "total_paid_spend", "total_paid_impressions", "total_paid_clicks", "total_paid_conversions", "total_paid_revenue", "paid_roi", "first_published_at", "publish_origin", "next_scheduled_at", "approval_status", "approval_by", "approval_by_name", "approval_at", "approval_note", "total_reach", "total_views", "total_follows")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    MEDIAS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    AI_GENERATED_FIELD_NUMBER: _ClassVar[int]
    AI_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AI_MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_GOAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CLICKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SAVES_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_RATE_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_RATE_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SCORE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SCORE_REASONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAID_SPEND_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAID_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAID_CLICKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAID_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAID_REVENUE_FIELD_NUMBER: _ClassVar[int]
    PAID_ROI_FIELD_NUMBER: _ClassVar[int]
    FIRST_PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_BY_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_AT_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_NOTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REACH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIEWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FOLLOWS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    content: str
    hashtags: _containers.RepeatedScalarFieldContainer[str]
    medias: _containers.RepeatedCompositeFieldContainer[Media]
    publications: _containers.RepeatedCompositeFieldContainer[Publication]
    status: PostStatus
    title: str
    created_by: str
    updated_by: str
    total_interactions: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_by_name: str
    ai_generated: bool
    ai_provider: str
    ai_model: str
    language: str
    number: int
    intelligence_goal: str
    total_impressions: int
    total_clicks: int
    total_saves: int
    engagement_rate: float
    click_through_rate: float
    intelligence_score: float
    performance_level: str
    score_summary: str
    score_reasons: _containers.RepeatedScalarFieldContainer[str]
    recommendations: _containers.RepeatedScalarFieldContainer[str]
    total_paid_spend: float
    total_paid_impressions: int
    total_paid_clicks: int
    total_paid_conversions: int
    total_paid_revenue: float
    paid_roi: float
    first_published_at: _timestamp_pb2.Timestamp
    publish_origin: str
    next_scheduled_at: _timestamp_pb2.Timestamp
    approval_status: ApprovalStatus
    approval_by: str
    approval_by_name: str
    approval_at: _timestamp_pb2.Timestamp
    approval_note: str
    total_reach: int
    total_views: int
    total_follows: int
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., content: _Optional[str] = ..., hashtags: _Optional[_Iterable[str]] = ..., medias: _Optional[_Iterable[_Union[Media, _Mapping]]] = ..., publications: _Optional[_Iterable[_Union[Publication, _Mapping]]] = ..., status: _Optional[_Union[PostStatus, str]] = ..., title: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., total_interactions: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., created_by_name: _Optional[str] = ..., ai_generated: _Optional[bool] = ..., ai_provider: _Optional[str] = ..., ai_model: _Optional[str] = ..., language: _Optional[str] = ..., number: _Optional[int] = ..., intelligence_goal: _Optional[str] = ..., total_impressions: _Optional[int] = ..., total_clicks: _Optional[int] = ..., total_saves: _Optional[int] = ..., engagement_rate: _Optional[float] = ..., click_through_rate: _Optional[float] = ..., intelligence_score: _Optional[float] = ..., performance_level: _Optional[str] = ..., score_summary: _Optional[str] = ..., score_reasons: _Optional[_Iterable[str]] = ..., recommendations: _Optional[_Iterable[str]] = ..., total_paid_spend: _Optional[float] = ..., total_paid_impressions: _Optional[int] = ..., total_paid_clicks: _Optional[int] = ..., total_paid_conversions: _Optional[int] = ..., total_paid_revenue: _Optional[float] = ..., paid_roi: _Optional[float] = ..., first_published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., publish_origin: _Optional[str] = ..., next_scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., approval_status: _Optional[_Union[ApprovalStatus, str]] = ..., approval_by: _Optional[str] = ..., approval_by_name: _Optional[str] = ..., approval_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., approval_note: _Optional[str] = ..., total_reach: _Optional[int] = ..., total_views: _Optional[int] = ..., total_follows: _Optional[int] = ...) -> None: ...

class ConnectedAccount(_message.Message):
    __slots__ = ("integration_id", "network", "account_name", "account_id", "avatar_url", "is_active")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    network: SocialNetwork
    account_name: str
    account_id: str
    avatar_url: str
    is_active: bool
    def __init__(self, integration_id: _Optional[str] = ..., network: _Optional[_Union[SocialNetwork, str]] = ..., account_name: _Optional[str] = ..., account_id: _Optional[str] = ..., avatar_url: _Optional[str] = ..., is_active: _Optional[bool] = ...) -> None: ...

class CreateSocialPostRequest(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class CreateSocialPostResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class UpdateSocialPostRequest(_message.Message):
    __slots__ = ("id", "social_post", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    social_post: SocialPost
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., social_post: _Optional[_Union[SocialPost, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSocialPostResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class DeleteSocialPostRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteSocialPostResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSocialPostRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetSocialPostResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class ListSocialPostRequest(_message.Message):
    __slots__ = ("ids", "status", "network", "scheduled_from", "scheduled_to", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_FROM_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    status: PostStatus
    network: SocialNetwork
    scheduled_from: _timestamp_pb2.Timestamp
    scheduled_to: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[PostStatus, str]] = ..., network: _Optional[_Union[SocialNetwork, str]] = ..., scheduled_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListSocialPostResponse(_message.Message):
    __slots__ = ("social_post_list", "next_page_token")
    SOCIAL_POST_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    social_post_list: _containers.RepeatedCompositeFieldContainer[SocialPost]
    next_page_token: str
    def __init__(self, social_post_list: _Optional[_Iterable[_Union[SocialPost, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddPublicationRequest(_message.Message):
    __slots__ = ("post_id", "publication")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication: Publication
    def __init__(self, post_id: _Optional[str] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class AddPublicationResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class UpdatePublicationRequest(_message.Message):
    __slots__ = ("post_id", "publication_id", "publication")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication_id: str
    publication: Publication
    def __init__(self, post_id: _Optional[str] = ..., publication_id: _Optional[str] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class UpdatePublicationResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class RemovePublicationRequest(_message.Message):
    __slots__ = ("post_id", "publication_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication_id: str
    def __init__(self, post_id: _Optional[str] = ..., publication_id: _Optional[str] = ...) -> None: ...

class RemovePublicationResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class PublishNowRequest(_message.Message):
    __slots__ = ("post_id", "publication_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication_id: str
    def __init__(self, post_id: _Optional[str] = ..., publication_id: _Optional[str] = ...) -> None: ...

class PublishNowResponse(_message.Message):
    __slots__ = ("social_post", "publication")
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    publication: Publication
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class CancelPublicationRequest(_message.Message):
    __slots__ = ("post_id", "publication_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication_id: str
    def __init__(self, post_id: _Optional[str] = ..., publication_id: _Optional[str] = ...) -> None: ...

class CancelPublicationResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class UnpublishRequest(_message.Message):
    __slots__ = ("post_id", "publication_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    publication_id: str
    def __init__(self, post_id: _Optional[str] = ..., publication_id: _Optional[str] = ...) -> None: ...

class UnpublishResponse(_message.Message):
    __slots__ = ("social_post", "publication")
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    publication: Publication
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class ReviewSocialPostRequest(_message.Message):
    __slots__ = ("id", "status", "note")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: ApprovalStatus
    note: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[ApprovalStatus, str]] = ..., note: _Optional[str] = ...) -> None: ...

class ReviewSocialPostResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class ListConnectedAccountsRequest(_message.Message):
    __slots__ = ("network",)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: SocialNetwork
    def __init__(self, network: _Optional[_Union[SocialNetwork, str]] = ...) -> None: ...

class ListConnectedAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[ConnectedAccount]
    def __init__(self, accounts: _Optional[_Iterable[_Union[ConnectedAccount, _Mapping]]] = ...) -> None: ...

class GenerateAIPostRequest(_message.Message):
    __slots__ = ("area_of_operation", "objective", "target_audience", "tone", "platform", "size", "include_emojis", "include_hashtags", "hashtags_count", "keywords", "language", "call_to_action", "additional_instructions", "product_or_service", "generate_image", "image_style", "integration_id", "model", "intelligence_goal", "intelligence_score", "performance_level", "score_reasons", "recommendations", "score_summary", "platforms")
    AREA_OF_OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    HASHTAGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_OR_SERVICE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_STYLE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_GOAL_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SCORE_REASONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    SCORE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    area_of_operation: str
    objective: str
    target_audience: str
    tone: str
    platform: SocialNetwork
    size: str
    include_emojis: bool
    include_hashtags: bool
    hashtags_count: int
    keywords: _containers.RepeatedScalarFieldContainer[str]
    language: str
    call_to_action: str
    additional_instructions: str
    product_or_service: str
    generate_image: bool
    image_style: str
    integration_id: str
    model: str
    intelligence_goal: str
    intelligence_score: float
    performance_level: str
    score_reasons: _containers.RepeatedScalarFieldContainer[str]
    recommendations: _containers.RepeatedScalarFieldContainer[str]
    score_summary: str
    platforms: _containers.RepeatedScalarFieldContainer[SocialNetwork]
    def __init__(self, area_of_operation: _Optional[str] = ..., objective: _Optional[str] = ..., target_audience: _Optional[str] = ..., tone: _Optional[str] = ..., platform: _Optional[_Union[SocialNetwork, str]] = ..., size: _Optional[str] = ..., include_emojis: _Optional[bool] = ..., include_hashtags: _Optional[bool] = ..., hashtags_count: _Optional[int] = ..., keywords: _Optional[_Iterable[str]] = ..., language: _Optional[str] = ..., call_to_action: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., product_or_service: _Optional[str] = ..., generate_image: _Optional[bool] = ..., image_style: _Optional[str] = ..., integration_id: _Optional[str] = ..., model: _Optional[str] = ..., intelligence_goal: _Optional[str] = ..., intelligence_score: _Optional[float] = ..., performance_level: _Optional[str] = ..., score_reasons: _Optional[_Iterable[str]] = ..., recommendations: _Optional[_Iterable[str]] = ..., score_summary: _Optional[str] = ..., platforms: _Optional[_Iterable[_Union[SocialNetwork, str]]] = ...) -> None: ...

class GenerateAIPostResponse(_message.Message):
    __slots__ = ("content", "hashtags", "image_base64", "image_mime_type")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BASE64_FIELD_NUMBER: _ClassVar[int]
    IMAGE_MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    content: str
    hashtags: _containers.RepeatedScalarFieldContainer[str]
    image_base64: str
    image_mime_type: str
    def __init__(self, content: _Optional[str] = ..., hashtags: _Optional[_Iterable[str]] = ..., image_base64: _Optional[str] = ..., image_mime_type: _Optional[str] = ...) -> None: ...

class GenerateBatchAIPostsRequest(_message.Message):
    __slots__ = ("agent_id", "post_count", "area_of_operation", "objective", "target_audience", "tone", "platform", "size", "include_emojis", "include_hashtags", "hashtags_count", "keywords", "language", "call_to_action", "additional_instructions", "product_or_service", "generate_image", "image_style", "integration_id", "model", "intelligence_goal", "intelligence_score", "performance_level", "score_reasons", "recommendations", "score_summary", "platforms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_COUNT_FIELD_NUMBER: _ClassVar[int]
    AREA_OF_OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    HASHTAGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_OR_SERVICE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_STYLE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_GOAL_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SCORE_REASONS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    SCORE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    post_count: int
    area_of_operation: str
    objective: str
    target_audience: str
    tone: str
    platform: SocialNetwork
    size: str
    include_emojis: bool
    include_hashtags: bool
    hashtags_count: int
    keywords: _containers.RepeatedScalarFieldContainer[str]
    language: str
    call_to_action: str
    additional_instructions: str
    product_or_service: str
    generate_image: bool
    image_style: str
    integration_id: str
    model: str
    intelligence_goal: str
    intelligence_score: float
    performance_level: str
    score_reasons: _containers.RepeatedScalarFieldContainer[str]
    recommendations: _containers.RepeatedScalarFieldContainer[str]
    score_summary: str
    platforms: _containers.RepeatedScalarFieldContainer[SocialNetwork]
    def __init__(self, agent_id: _Optional[str] = ..., post_count: _Optional[int] = ..., area_of_operation: _Optional[str] = ..., objective: _Optional[str] = ..., target_audience: _Optional[str] = ..., tone: _Optional[str] = ..., platform: _Optional[_Union[SocialNetwork, str]] = ..., size: _Optional[str] = ..., include_emojis: _Optional[bool] = ..., include_hashtags: _Optional[bool] = ..., hashtags_count: _Optional[int] = ..., keywords: _Optional[_Iterable[str]] = ..., language: _Optional[str] = ..., call_to_action: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., product_or_service: _Optional[str] = ..., generate_image: _Optional[bool] = ..., image_style: _Optional[str] = ..., integration_id: _Optional[str] = ..., model: _Optional[str] = ..., intelligence_goal: _Optional[str] = ..., intelligence_score: _Optional[float] = ..., performance_level: _Optional[str] = ..., score_reasons: _Optional[_Iterable[str]] = ..., recommendations: _Optional[_Iterable[str]] = ..., score_summary: _Optional[str] = ..., platforms: _Optional[_Iterable[_Union[SocialNetwork, str]]] = ...) -> None: ...

class GeneratedPost(_message.Message):
    __slots__ = ("content", "hashtags", "image_base64", "image_mime_type", "recommended_network")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    HASHTAGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BASE64_FIELD_NUMBER: _ClassVar[int]
    IMAGE_MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    content: str
    hashtags: _containers.RepeatedScalarFieldContainer[str]
    image_base64: str
    image_mime_type: str
    recommended_network: str
    def __init__(self, content: _Optional[str] = ..., hashtags: _Optional[_Iterable[str]] = ..., image_base64: _Optional[str] = ..., image_mime_type: _Optional[str] = ..., recommended_network: _Optional[str] = ...) -> None: ...

class GenerateBatchAIPostsResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[GeneratedPost]
    def __init__(self, posts: _Optional[_Iterable[_Union[GeneratedPost, _Mapping]]] = ...) -> None: ...

class SyncMetricsRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class SyncMetricsResponse(_message.Message):
    __slots__ = ("social_post",)
    SOCIAL_POST_FIELD_NUMBER: _ClassVar[int]
    social_post: SocialPost
    def __init__(self, social_post: _Optional[_Union[SocialPost, _Mapping]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "tipo_relatorio")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    list_request: ListSocialPostRequest
    tipo_relatorio: str
    def __init__(self, list_request: _Optional[_Union[ListSocialPostRequest, _Mapping]] = ..., tipo_relatorio: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
