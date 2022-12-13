from django.core.signals import request_finished
from django.dispatch import receiver
from favourite.models import Favourite
from django.core.mail import send_mail
from price.models import Price


@receiver(request_finished)
def favourite_check(sender, **kwargs):
    favourites = Favourite.objects.filter(is_active=True)
    for fav in favourites:
        field_name = fav.monitor_field
        email = fav.trader.user.email
        price = Price.objects.filter(company=fav.company_id, is_latest=True)
        company_field_price = getattr(price, field_name)

        if company_field_price <= fav.minimum_limit:
            send_mail(
                'Market Favourite Company Price Alert',
                f'Favourite Company {fav.company.name} has reached minimum limit, new value is {company_field_price}',
                'mujtaba.ali@ignicube.com',
                [email],
            )
        if company_field_price >= fav.maximum_limit:
            send_mail(
                'Market Favourite Company Price Alert',
                f'Favourite Company {fav.company.name} has reached maximum limit, new value is {company_field_price}',
                'mujtaba.ali@ignicube.com',
                [email],
            )
