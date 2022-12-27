from rest_framework import serializers
from api.models import Purchase, Comment, User
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


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = (
        'id',
        'first_name',
        'last_name',
        'email',
    )


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source='user.first_name',
        allow_null=True,
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'message',
            'ticket',
            'user_name',
        )

    def create(self, validated_data):
        comment = Comment.objects.create(
            message=validated_data.get('message'),
            ticket=validated_data.get('ticket'),
            user=self.context['request'].user,
        )
        return comment
