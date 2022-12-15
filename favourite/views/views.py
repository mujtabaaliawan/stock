from favourite.models import Favourite
from favourite.serializers import FavouriteSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from favourite.permissions.trader_permission import IsTraderUpdate, IsTrader


class FavouriteListCreate(ListCreateAPIView):

    serializer_class = FavouriteSerializer
    permission_classes = (IsTrader,)

    def get_queryset(self):
        current_user_id = self.request.user.id
        return Favourite.objects.filter(trader__user_id=current_user_id)


class FavouriteUpdate(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    permission_classes = (IsTraderUpdate,)
