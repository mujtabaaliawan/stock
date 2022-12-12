from django.urls import path
from core.views import views


urlpatterns = [
    path('handler', views.DataUpdater.as_view(), name='data_handler'),
]
