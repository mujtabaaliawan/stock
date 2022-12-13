from django.urls import path
from trader.views import views


urlpatterns = [
    path('trader', views.TraderList.as_view(), name='trader_list_new'),
    path('trader/<int:pk>', views.TraderUpdate.as_view(), name='trader_update'),
]
