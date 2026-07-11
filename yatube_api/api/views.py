from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from posts.models import Post, Comment, Group, Follow
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer,
)
from django.shortcuts import get_object_or_404


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("pub_date")
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_url_kwarg = "post_id"


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class GroupDetail(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(following__username__icontains=search)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post_id=post_id).order_by("created")

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(author=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_url_kwarg = "comment_id"

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_id")
        get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post_id=post_id, id=comment_id)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
