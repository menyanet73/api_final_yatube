from rest_framework import permissions

from .permissions import AuthorOrReadOnly


class AuthorPermissionMixin:
    permission_classes = (AuthorOrReadOnly, permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        return super().perform_create(serializer)