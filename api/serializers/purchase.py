from rest_framework import serializers
from api.models import Purchase, Comment
from api.serializers import TicketListSerializer
from utils import messages


class PurchaseListSerializer(serializers.ModelSerializer):
    ticket = TicketListSerializer(read_only=True)
    ticket_id = serializers.IntegerField(source='ticket', write_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'ticket',
            'ticket_id',
        )

    def validate(self, attrs):
        if Purchase.objects.filter(
                user=self.context['request'].user,
                ticket=attrs['ticket'],
                is_active=True,
        ).exists():
            raise serializers.ValidationError(
                messages.TICKET_ALREADY_IN_PURCHASE,
            )
        return attrs

    def create(self, validated_data):
        if Purchase.objects.filter(
                user=self.context['request'].user,
                ticket=validated_data['ticket'],
                is_active=False,
        ).exists():
            purchase = Purchase.objects.get(
                user=self.context['request'].user,
                ticket=validated_data['ticket'],
                is_active=False,
            )
            purchase.is_active = True
            purchase.save()
            return purchase

        purchase = Purchase.objects.create(
            ticket_id=validated_data['ticket'],
            user=self.context['request'].user,
        )
        return purchase


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'message',
            'ticket',
        )
