from django.urls import path
from price import views


urlpatterns = [
    path('prices', views.PriceList.as_view(), name='price_list'),
    path('latest', views.LatestPriceList.as_view(), name='market_price')
]
