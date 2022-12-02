from django.urls import path
from price import views


urlpatterns = [
    path('price', views.PriceList.as_view(), name='price_list'),
]
