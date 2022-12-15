from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser


class CoreAdministrator(AnonymousUser):

    def __init__(self):
        super().__init__()

    @property
    def is_authenticated(self):
        return True


class SenderAuthentication(BaseAuthentication):

    def authenticate(self, request):

        user_ip = request.META['REMOTE_ADDR']

        for ip in settings.ALLOWED_IPS:
            safe_ip = ip.replace("$", '0').replace('%', '2').replace('r', '1')

            if user_ip == safe_ip:
                encoded_token = request.headers['Secret-Token']

                secret_key = settings.TOKEN_KEY
                decoded_token = jwt.decode(encoded_token, secret_key, algorithms=["HS256"],
                                           options={"verify_exp": False})
                if decoded_token in settings.ALLOWED_TOKENS:
                    user = CoreAdministrator()
                    return user, None

        return None
