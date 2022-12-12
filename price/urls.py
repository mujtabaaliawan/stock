from django.urls import path
from price.views import views


urlpatterns = [
    path('latest', views.LatestPriceList.as_view(), name='market_price'),
    path('graph', views.GraphLogger.as_view(), name='company_graph'),
]
