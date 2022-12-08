import factory
from factory.django import DjangoModelFactory
from user.models import User
from trader.models import Trader
from django.contrib.auth.hashers import make_password


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'Trader'
    last_name = 'family'
    email = 'trader@gmail.com'
    password = make_password('trader')
    role = 'trader'
    is_staff = True
    is_active = True


class TraderFactory(DjangoModelFactory):
    class Meta:
        model = Trader

    mobile_number = '0312121212'
    user = factory.SubFactory('trader.factories.UserFactory', first_name='Trader', last_name='family',
                              email='trader@gmail.com', password=make_password('trader'),
                              role="trader")