from django.urls import path
from price import views


urlpatterns = [
    path('price', views.PriceList.as_view(), name='price_list'),
    path('price/new', views.PriceCreate.as_view(), name='price_new'),
    path('price/<int:pk>', views.PriceUpdate.as_view(), name='price_update'),
]
