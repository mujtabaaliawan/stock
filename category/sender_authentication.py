from rest_framework.authentication import BaseAuthentication
from user.models import User
import jwt
import os
from dotenv import load_dotenv
from category.tokens import allowed_tokens
from category.ips import allowed_ips


class SenderAuthentication(BaseAuthentication):

    def authenticate(self, request):

        user_ip = request.META['REMOTE_ADDR']

        for ip in allowed_ips:
            safe_ip = ip.replace("$", '0').replace('£', '2').replace('r', '1')

            if user_ip == safe_ip:
                encoded_token = request.headers['Secret-Token']
                load_dotenv()
                secret_key = str(os.getenv('TOKEN_KEY'))
                decoded_token = jwt.decode(encoded_token, secret_key, algorithms=["HS256"],
                                           options={"verify_exp": False})

                if decoded_token in allowed_tokens:
                    user = User.objects.get(id=1)
                    return user, None

        return None
