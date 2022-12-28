from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import Category
from api.serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class CityViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id"]

    def get_permissions(self):
        self.permission_classes = [
            AllowAny,
        ]
        return super().get_permissions()

    def get_queryset(self):
        return Category.objects.filter(is_active=True)

    def get_serializer_class(self):
        return CategorySerializer

