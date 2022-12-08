from rest_framework.permissions import BasePermission
from trader.models import Trader


class IsTrader(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "trader"


class IsTraderHimself(BasePermission):

    def has_permission(self, request, view):
        trader_id = request.data["trader_id"]
        trader = Trader.objects.get(id=trader_id)
        return request.user.id == trader.user.id

