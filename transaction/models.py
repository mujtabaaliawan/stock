from django.db import models
from price.models import Price


class Transaction(models.Model):

    nature = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=255)
    volume_transacted = models.FloatField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='transaction_prices')



