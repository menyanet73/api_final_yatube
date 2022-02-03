from rest_framework import viewsets, permissions

from posts.models import Post, Group, Comment, Follow
from .mixins import AuthorPermissionMixin
from .permissions import AuthorOrReadOnly, ReadOnly
from api import serializers


class PostViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (AuthorOrReadOnly,)


class CommentViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (AuthorOrReadOnly,)


class FollowViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = (AuthorOrReadOnly,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (ReadOnly,)