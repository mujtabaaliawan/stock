from rest_framework.permissions import BasePermission
from trader.models import Trader
from favourite.models import Favourite


class IsTraderUpdate(BasePermission):

    def has_permission(self, request, view):
        pk = view.kwargs['pk']
        favourite_trader_id = Favourite.objects.get(id=pk).trader_id
        trader_user_id = Trader.objects.get(id=favourite_trader_id).user_id
        return request.user.id == trader_user_id


class IsTraderCreate(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            trader_id = request.data["trader_id"]
            trader = Trader.objects.get(id=trader_id)
            return request.user.id == trader.user.id
        return True
