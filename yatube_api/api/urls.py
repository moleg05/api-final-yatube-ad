from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    # JWT
    path("jwt/create/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("posts/", views.PostList.as_view(), name="post-list"),
    path("posts/<int:post_id>/", views.PostDetail.as_view(),
         name="post-detail"),
    path("groups/", views.GroupList.as_view(), name="group-list"),
    path("groups/<int:pk>/", views.GroupDetail.as_view(), name="group-detail"),
    path("follow/", views.FollowList.as_view(), name="follow-list"),
    path(
        "posts/<int:post_id>/comments/",
        views.CommentList.as_view(),
        name="comment-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:comment_id>/",
        views.CommentDetail.as_view(),
        name="comment-detail",
    ),
]
