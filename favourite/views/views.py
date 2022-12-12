from favourite.models import Favourite
from favourite.serializers import FavouriteSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from trader.models import Trader
from django.http import JsonResponse
from favourite.permissions.trader_permission import IsTrader, IsTraderHimself


class FavouriteCreate(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    permission_classes = [IsTraderHimself]


class FavouriteUpdate(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteList(APIView):

    permission_classes = [IsTrader]

    def get(self, request):

        trader = Trader.objects.get(user_id=request.user.id)
        favourites = Favourite.objects.filter(trader=trader.id)
        favourites_values = list(favourites.values())
        return JsonResponse(favourites_values, safe=False)