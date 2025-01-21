from api.commons import newsroom_pb2 as _newsroom_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewsArticleRequest(_message.Message):
    __slots__ = ("title", "content", "author", "image_reference_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    author: str
    image_reference_id: str
    def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ..., author: _Optional[str] = ..., image_reference_id: _Optional[str] = ...) -> None: ...

class CreateNewsArticleResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class ListNewsArticlesRequest(_message.Message):
    __slots__ = ("statuses", "field_mask")
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedScalarFieldContainer[_newsroom_pb2.ArticleStatus]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, statuses: _Optional[_Iterable[_Union[_newsroom_pb2.ArticleStatus, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListNewsArticlesResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: _containers.RepeatedCompositeFieldContainer[NewsArticleDetails]
    def __init__(self, article_details: _Optional[_Iterable[_Union[NewsArticleDetails, _Mapping]]] = ...) -> None: ...

class GetNewsArticleByIdRequest(_message.Message):
    __slots__ = ("new_article_sid",)
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ...) -> None: ...

class GetNewsArticleByIdResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class UpdateNewsArticleRequest(_message.Message):
    __slots__ = ("article_details", "field_mask")
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNewsArticleResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class NewsArticleDetails(_message.Message):
    __slots__ = ("new_article_sid", "title", "content", "status", "date_created", "last_edited", "author", "image_reference_id")
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITED_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    title: str
    content: str
    status: _newsroom_pb2.ArticleStatus
    date_created: _timestamp_pb2.Timestamp
    last_edited: _timestamp_pb2.Timestamp
    author: str
    image_reference_id: str
    def __init__(self, new_article_sid: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[_newsroom_pb2.ArticleStatus, str]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., author: _Optional[str] = ..., image_reference_id: _Optional[str] = ...) -> None: ...

class PublishedArticleDetails(_message.Message):
    __slots__ = ("published_article_sid", "news_article_details", "date_published", "display_to_user", "always_display", "is_client_article")
    PUBLISHED_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    NEWS_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DATE_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TO_USER_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    IS_CLIENT_ARTICLE_FIELD_NUMBER: _ClassVar[int]
    published_article_sid: int
    news_article_details: NewsArticleDetails
    date_published: _timestamp_pb2.Timestamp
    display_to_user: bool
    always_display: bool
    is_client_article: bool
    def __init__(self, published_article_sid: _Optional[int] = ..., news_article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ..., date_published: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_to_user: bool = ..., always_display: bool = ..., is_client_article: bool = ...) -> None: ...

class UserActivity(_message.Message):
    __slots__ = ("user_activity_log_sid", "date_created", "user_activity_details")
    class UserActivityDetails(_message.Message):
        __slots__ = ("published_article_sid", "published_client_article_sid")
        PUBLISHED_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_CLIENT_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
        published_article_sid: int
        published_client_article_sid: int
        def __init__(self, published_article_sid: _Optional[int] = ..., published_client_article_sid: _Optional[int] = ...) -> None: ...
    USER_ACTIVITY_LOG_SID_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    USER_ACTIVITY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    user_activity_log_sid: int
    date_created: _timestamp_pb2.Timestamp
    user_activity_details: UserActivity.UserActivityDetails
    def __init__(self, user_activity_log_sid: _Optional[int] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user_activity_details: _Optional[_Union[UserActivity.UserActivityDetails, _Mapping]] = ...) -> None: ...

class CreatePublishedArticleRequest(_message.Message):
    __slots__ = ("new_article_sid", "display_to_user", "article_link")
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TO_USER_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_LINK_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    display_to_user: bool
    article_link: str
    def __init__(self, new_article_sid: _Optional[int] = ..., display_to_user: bool = ..., article_link: _Optional[str] = ...) -> None: ...

class CreatePublishedArticleResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: PublishedArticleDetails
    def __init__(self, published_article_details: _Optional[_Union[PublishedArticleDetails, _Mapping]] = ...) -> None: ...

class ListPublishedArticlesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPublishedArticlesResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: _containers.RepeatedCompositeFieldContainer[PublishedArticleDetails]
    def __init__(self, published_article_details: _Optional[_Iterable[_Union[PublishedArticleDetails, _Mapping]]] = ...) -> None: ...

class GetPublishedArticleByIdRequest(_message.Message):
    __slots__ = ("new_article_sid", "published_article_sid")
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    published_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ..., published_article_sid: _Optional[int] = ...) -> None: ...

class GetPublishedArticleByIdResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: PublishedArticleDetails
    def __init__(self, published_article_details: _Optional[_Union[PublishedArticleDetails, _Mapping]] = ...) -> None: ...

class UserActivityRequest(_message.Message):
    __slots__ = ("published_article_sid", "force", "published_client_article_sid")
    PUBLISHED_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CLIENT_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    published_article_sid: int
    force: bool
    published_client_article_sid: int
    def __init__(self, published_article_sid: _Optional[int] = ..., force: bool = ..., published_client_article_sid: _Optional[int] = ...) -> None: ...

class UserActivityResponse(_message.Message):
    __slots__ = ("user_activity",)
    USER_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    user_activity: UserActivity
    def __init__(self, user_activity: _Optional[_Union[UserActivity, _Mapping]] = ...) -> None: ...

class GetNewsForUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNewsForUserResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: _containers.RepeatedCompositeFieldContainer[PublishedArticleDetails]
    def __init__(self, published_article_details: _Optional[_Iterable[_Union[PublishedArticleDetails, _Mapping]]] = ...) -> None: ...

class StoreNewsArticleImageRequest(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class NewsArticleImage(_message.Message):
    __slots__ = ("uuid", "new_article_sid", "content", "download_url", "image_reference_id", "image_type", "temp_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMP_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    new_article_sid: int
    content: str
    download_url: str
    image_reference_id: str
    image_type: str
    temp_id: _wrappers_pb2.StringValue
    def __init__(self, uuid: _Optional[str] = ..., new_article_sid: _Optional[int] = ..., content: _Optional[str] = ..., download_url: _Optional[str] = ..., image_reference_id: _Optional[str] = ..., image_type: _Optional[str] = ..., temp_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class StoreNewsArticleImageResponse(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class ListImagesForNewsArticleRequest(_message.Message):
    __slots__ = ("new_article_sid",)
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ...) -> None: ...

class ListImagesForNewsArticleResponse(_message.Message):
    __slots__ = ("news_article_images",)
    NEWS_ARTICLE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    news_article_images: _containers.RepeatedCompositeFieldContainer[NewsArticleImage]
    def __init__(self, news_article_images: _Optional[_Iterable[_Union[NewsArticleImage, _Mapping]]] = ...) -> None: ...

class UploadNewsArticleImageRequest(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class UploadNewsArticleImageResponse(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class CreateClientArticleRequest(_message.Message):
    __slots__ = ("title", "content", "author", "image_reference_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    author: str
    image_reference_id: str
    def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ..., author: _Optional[str] = ..., image_reference_id: _Optional[str] = ...) -> None: ...

class CreateClientArticleResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class UpdateClientArticleRequest(_message.Message):
    __slots__ = ("article_details", "field_mask")
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateClientArticleResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...

class ListClientArticlesRequest(_message.Message):
    __slots__ = ("statuses", "field_mask")
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedScalarFieldContainer[_newsroom_pb2.ArticleStatus]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, statuses: _Optional[_Iterable[_Union[_newsroom_pb2.ArticleStatus, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListClientArticlesResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: _containers.RepeatedCompositeFieldContainer[NewsArticleDetails]
    def __init__(self, article_details: _Optional[_Iterable[_Union[NewsArticleDetails, _Mapping]]] = ...) -> None: ...

class CreatePublishedClientArticleRequest(_message.Message):
    __slots__ = ("new_article_sid", "display_to_user", "article_link", "always_show")
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TO_USER_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_LINK_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_SHOW_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    display_to_user: bool
    article_link: str
    always_show: bool
    def __init__(self, new_article_sid: _Optional[int] = ..., display_to_user: bool = ..., article_link: _Optional[str] = ..., always_show: bool = ...) -> None: ...

class CreatePublishedClientArticleResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: PublishedArticleDetails
    def __init__(self, published_article_details: _Optional[_Union[PublishedArticleDetails, _Mapping]] = ...) -> None: ...

class GetPublishedClientArticleByIdRequest(_message.Message):
    __slots__ = ("published_article_sid",)
    PUBLISHED_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    published_article_sid: int
    def __init__(self, published_article_sid: _Optional[int] = ...) -> None: ...

class GetPublishedClientArticleByIdResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: PublishedArticleDetails
    def __init__(self, published_article_details: _Optional[_Union[PublishedArticleDetails, _Mapping]] = ...) -> None: ...

class StoreClientArticleImageRequest(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class StoreClientArticleImageResponse(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class ListImagesForClientArticleRequest(_message.Message):
    __slots__ = ("new_article_sid",)
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ...) -> None: ...

class ListImagesForClientArticleResponse(_message.Message):
    __slots__ = ("news_article_images",)
    NEWS_ARTICLE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    news_article_images: _containers.RepeatedCompositeFieldContainer[NewsArticleImage]
    def __init__(self, news_article_images: _Optional[_Iterable[_Union[NewsArticleImage, _Mapping]]] = ...) -> None: ...

class UploadClientArticleImageRequest(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class UploadClientArticleImageResponse(_message.Message):
    __slots__ = ("image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: NewsArticleImage
    def __init__(self, image: _Optional[_Union[NewsArticleImage, _Mapping]] = ...) -> None: ...

class ListPublishedClientArticlesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPublishedClientArticlesResponse(_message.Message):
    __slots__ = ("published_article_details",)
    PUBLISHED_ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    published_article_details: _containers.RepeatedCompositeFieldContainer[PublishedArticleDetails]
    def __init__(self, published_article_details: _Optional[_Iterable[_Union[PublishedArticleDetails, _Mapping]]] = ...) -> None: ...

class GetClientArticleByIdRequest(_message.Message):
    __slots__ = ("new_article_sid",)
    NEW_ARTICLE_SID_FIELD_NUMBER: _ClassVar[int]
    new_article_sid: int
    def __init__(self, new_article_sid: _Optional[int] = ...) -> None: ...

class GetClientArticleByIdResponse(_message.Message):
    __slots__ = ("article_details",)
    ARTICLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    article_details: NewsArticleDetails
    def __init__(self, article_details: _Optional[_Union[NewsArticleDetails, _Mapping]] = ...) -> None: ...
