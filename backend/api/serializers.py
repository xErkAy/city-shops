from rest_framework import serializers

from api.exceptions import ExceptionWithMessage
from api.models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class GETShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address')


class POSTShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    city = serializers.IntegerField()
    street = serializers.IntegerField()
    building = serializers.CharField(max_length=10)
    open_time = serializers.TimeField()
    close_time = serializers.TimeField()

    def validate(self, attrs):
        if attrs.get('open_time') > attrs.get('close_time'):
            raise ExceptionWithMessage('Shop opening time cannot be greater than closing time."')
        return attrs

    def create(self, validated_data):
        try:
            city = City.objects.get(id=validated_data.get('city'))
            street = Street.objects.get(id=validated_data.get('street'))
        except City.DoesNotExist:
            raise ExceptionWithMessage('The city with this pk does not exist')
        except Street.DoesNotExist:
            raise ExceptionWithMessage('The street with this pk does not exist')

        return Shop.objects.create(
            name=validated_data.get('name'),
            city=city,
            street=street,
            building=validated_data.get('building'),
            open_time=validated_data.get('open_time'),
            close_time=validated_data.get('close_time')
        )
