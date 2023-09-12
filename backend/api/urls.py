from django.urls import path, include

from api.views import (
    GetCityList,
    GetStreetByCityID,
    ShopAPIView,
)

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('city/', GetCityList.as_view()),
    path('<int:city_id>/street/', GetStreetByCityID.as_view()),
    path('shop/', ShopAPIView.as_view()),
]
