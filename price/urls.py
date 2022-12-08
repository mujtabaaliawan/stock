from django.urls import path
from price import views


urlpatterns = [
    path('latest', views.LatestPriceList.as_view(), name='market_price')
]
