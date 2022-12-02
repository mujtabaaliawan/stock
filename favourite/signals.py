from django.core.signals import request_finished
from django.dispatch import receiver
from favourite.models import Favourite
from django.core.mail import send_mail
from trader.models import Manager


@receiver(request_finished)
def favourite_check(sender, **kwargs):
    favourites = Favourite.objects.all()
    for fav in favourites:
        field_name = fav.price_field
        if field_name == 'ldcp':
            company_field_price = fav.company.price.ldcp
        elif field_name == 'open':
            company_field_price = fav.company.price.open
        elif field_name == 'high':
            company_field_price = fav.company.price.high
        elif field_name == 'low':
            company_field_price = fav.company.price.low
        elif field_name == 'current':
            company_field_price = fav.company.price.current
        elif field_name == 'change':
            company_field_price = fav.company.price.change
        elif field_name == 'volume':
            company_field_price = fav.company.price.volume

        if company_field_price <= fav.minimum_limit:
            favourite_trader = Manager.objects.get(user_id=fav.trader_user_id)
            email = favourite_trader.user.email
            send_mail(
                'Market Favourite Company Price Alert',
                f'Favourite Company {fav.company.name} has reached minimum limit, new value is {company_field_price}',
                'mujtaba.ali@ignicube.com',
                [email],
            )
        if company_field_price >= fav.maximum_limit:
            favourite_trader = Manager.objects.get(user_id=fav.trader_user_id)
            email = favourite_trader.user.email
            send_mail(
                'Market Favourite Company Price Alert',
                f'Favourite Company {fav.company.name} has reached maximum limit, new value is {company_field_price}',
                'mujtaba.ali@ignicube.com',
                [email],
            )
