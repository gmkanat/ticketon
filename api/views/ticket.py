from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Ticket, Category
from api.serializers import (
    TicketListSerializer,
    TicketDetailSerializer,
    CategorySerializer
)


class TicketViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category_id", "city_id", "start_time"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "price", "category__name", "start_time", ]

    def get_permissions(self):
        self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def get_queryset(self):
        return Ticket.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return TicketListSerializer
        if self.action == 'retrieve':
            return TicketDetailSerializer


class CategoryViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    def get_permissions(self):
        self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def get_queryset(self):
        return Category.objects.filter(is_active=True)

    def get_serializer_class(self):
        return CategorySerializer
