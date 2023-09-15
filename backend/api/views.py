from datetime import datetime

from django.db.models import QuerySet, Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.models import City, Street, Shop
from api.serializers import (
    CitySerializer,
    StreetSerializer,
    GETShopSerializer,
    POSTShopSerializer
)


class GetCityList(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class GetStreetByCityID(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Street.objects.filter(city_id=kwargs['city_id'])
        return Response(StreetSerializer(queryset, many=True).data)


class ShopAPIView(APIView):

    @staticmethod
    def filter_city_street(queryset: QuerySet, params: dict) -> QuerySet:
        city = params.get('city')
        if city is not None:
            if city.isdigit():
                queryset = queryset.filter(city_id=city)
            queryset = queryset.filter(city__name__icontains=city)

        street = params.get('street')
        if street is not None:
            if street.isdigit():
                queryset = queryset.filter(street_id=street)
            queryset = queryset.filter(street__name__icontains=street)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = Shop.objects.all()
        params = request.query_params

        open = params.get('open')
        if open is not None:
            now = datetime.now().time()
            if open in [1, '1', 'true']:
                queryset = queryset.filter(open_time__lte=now, close_time__gte=now)
            else:
                queryset = queryset.filter(
                    Q(open_time__gte=now, close_time__lte=now) | Q(open_time__gte=now, close_time__gte=now)
                )

        queryset = self.filter_city_street(queryset, params)

        return Response(GETShopSerializer(queryset, many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = POSTShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.create(serializer.validated_data)

        return Response({'id': obj.id})
