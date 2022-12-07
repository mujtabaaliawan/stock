from django.urls import path
from user import views


urlpatterns = [
    path('user', views.UserList.as_view(), name='user_list'),
    path('user/new', views.UserCreate.as_view(), name='user_new'),
    path('user/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    ]