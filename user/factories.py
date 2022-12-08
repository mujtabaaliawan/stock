import factory
from factory.django import DjangoModelFactory
from user.models import User
from trader.models import Trader
from django.contrib.auth.hashers import make_password


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'USER'
    last_name = 'family'
    email = 'user@gmail.com'
    password = make_password('user')
    role = 'trader'
    is_staff = True
    is_active = True
