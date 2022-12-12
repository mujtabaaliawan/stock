from django.urls import path
from category.views import views


urlpatterns = [
    path('category', views.CategoryList.as_view(), name='category_list'),
]
