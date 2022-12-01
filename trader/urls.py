from django.urls import path
from trader import views


urlpatterns = [
    path('trader', views.TraderList.as_view(), name='trader_list'),
    path('trader/new', views.TraderCreate.as_view(), name='trader_new'),
    path('trader/<int:pk>', views.TraderUpdate.as_view(), name='trader_update'),
]