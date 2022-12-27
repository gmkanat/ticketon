from rest_framework import serializers

from api.models import Ticket, Image, Category, City, TicketPrice


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url')

    class Meta:
        model = Image
        fields = (
            'id',
            'image',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPrice
        fields = (
            'id',
            'person_type',
            'price',
        )


class TicketListSerializer(serializers.ModelSerializer):
    image = serializers.CharField(
        source='images.first.image.url',
        allow_null=True,
        allow_blank=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    is_purchased = serializers.SerializerMethodField()
    city = CitySerializer(
        read_only=True,
    )
    price = PriceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ticket
        fields = (
            'id',
            'name',
            'description',
            'price',
            'image',
            'category',
            'is_purchased',
            'city',
            'start_time',
        )

    def get_is_purchased(self, obj):
        if self.context['request'].user.is_authenticated:
            return obj.purchases.filter(user=self.context['request'].user).exists()
        return False


class TicketDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(
        many=True,
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    is_purchased = serializers.SerializerMethodField()
    city = CitySerializer(
        read_only=True,
    )
    price = PriceSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Ticket
        fields = (
            'id',
            'name',
            'description',
            'price',
            'images',
            'category',
            'city',
            'is_purchased',
            'start_time',
        )

    def get_is_purchased(self, obj):
        if self.context['request'].user.is_authenticated:
            return obj.purchases.filter(user=self.context['request'].user).exists()
        return False

