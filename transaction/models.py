from django.db import models
from price.models import Price
from trader.models import Trader


class Transaction(models.Model):
    nature_choices = (
        ("purchase", "purchase"),
        ("sale", "sale")
    )
    nature = models.CharField(max_length=10, choices=nature_choices, default="purchase")
    date = models.DateTimeField(auto_now_add=True)
    volume_transacted = models.FloatField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='transaction_prices')
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='transaction_trader')



