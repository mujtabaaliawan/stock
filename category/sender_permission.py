from rest_framework.permissions import BasePermission


class IsSender(BasePermission):

    def has_permission(self, request, view):
        allowed_ips = ('127.0.0.1', '127.0.0.2')
        allowed_tokens = ('igni', 'cube')
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in allowed_ips:
            token = request.headers['Secret-Token']
            if token in allowed_tokens:
                return True
        return False


