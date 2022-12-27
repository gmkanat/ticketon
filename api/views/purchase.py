from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Purchase
from api.serializers import PurchaseListSerializer


class PurchaseViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["ticket__name", "ticket__description"]
    filter_fields = ["ticket__category__name"]

    def get_permissions(self):
        self.permission_classes = [
            IsAuthenticated,
        ]
        return super().get_permissions()

    def get_queryset(self):
        return Purchase.objects.filter(is_active=True)

    def get_serializer_class(self):
        return PurchaseListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user)
        instance = get_object_or_404(queryset, pk=kwargs['pk'])
        from datetime import datetime, timedelta
        from django.utils import timezone
        if instance.ticket.start_time > timezone.now() - timedelta(hours=2):
            instance.is_active = False
            instance.save()
            return Response({'message': 'Successfully cancelled'})
        return Response({'message': 'It is too late to sell the ticket'})
