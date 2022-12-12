from rest_framework.permissions import BasePermission


class IsTrader(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "trader"
