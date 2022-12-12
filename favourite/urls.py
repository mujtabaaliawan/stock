from django.urls import path
from favourite.views import views

urlpatterns = [
    path('favourite', views.FavouriteList.as_view(), name='favourite_list'),
    path('favourite/new', views.FavouriteCreate.as_view(), name='favourite_new'),
    path('favourite/<int:pk>', views.FavouriteUpdate.as_view(), name='favourite_update'),
]
