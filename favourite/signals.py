# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from favourite.models import Favourite
# from trader.models import Trader
# from django.core.mail import send_mail
#
#
# @receiver(post_save, sender=(PriceUpdate), weak=False)
# def favourite_check(sender, instance=None, created=False, **kwargs):
#     favourites = Favourite.objects.all()
#     for fav in favourites:
#         company = fav.company
#         field = fav.price_field
#         company_price = fav.company.price.field
#         if company_price <= fav.minimum_limit or company_price >= fav.maximum_limit:
#             favourite_trader = Trader.objects.get(user_id=fav.trader_user_id)
#             email = favourite_trader.user.email
#             send_mail(email)