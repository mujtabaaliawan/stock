from django.urls import path
from manager import views


urlpatterns = [
    path('manager', views.ManagerList.as_view(), name='manager_list'),
    path('manager/new', views.ManagerCreate.as_view(), name='manager_new'),
    path('manager/<int:pk>', views.ManagerUpdate.as_view(), name='manager_update'),
]