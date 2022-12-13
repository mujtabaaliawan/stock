from django.urls import path
from favourite.views import views

urlpatterns = [
    path('favourite', views.FavouriteListCreate.as_view(), name='favourite_list_new'),
    path('favourite/<int:pk>', views.FavouriteUpdate.as_view(), name='favourite_update'),
]
