from django.urls import path
from stock_detail.views import views


urlpatterns = [
    path('latest', views.StockDetailList.as_view(), name='market_price'),
    path('graph', views.GraphLogger.as_view(), name='company_graph'),
]
