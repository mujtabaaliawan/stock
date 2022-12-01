from django.db import models


class Price(models.Model):

    ldcp = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    current = models.FloatField()
    change = models.FloatField()
    volume = models.FloatField()
