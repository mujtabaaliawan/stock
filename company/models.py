from django.db import models
from price.models import Price


class Company(models.Model):

    name = models.CharField(max_length=255)
    price = models.ManyToManyField(Price, blank=True)
    latest_prices = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='new_price')

    class Meta:
        ordering = ['id']

