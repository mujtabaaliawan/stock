from favourite.models import Favourite
from favourite.serializers import FavouriteSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class FavouriteList(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteCreate(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteUpdate(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
