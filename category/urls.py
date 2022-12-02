from django.urls import path
from category import views


urlpatterns = [
    path('category', views.CategoryList.as_view(), name='category_list'),
    path('handler', views.DataUpdater.as_view(), name='data_handler'),
]
