from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from api.models import Comment
from api.serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CommentViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["ticket_id"]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [
                AllowAny,
            ]
        if self.action == 'create':
            self.permission_classes = [
                IsAuthenticated,
            ]
        return super().get_permissions()

    def get_queryset(self):
        return Comment.objects.filter(is_active=True)

    def get_serializer_class(self):
        return CommentSerializer

