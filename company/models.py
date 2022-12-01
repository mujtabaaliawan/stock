from django.db import models
from price.models import Price


class Company(models.Model):

    name = models.CharField(max_length=255)
    price = models.OneToOneField(Price, on_delete=models.CASCADE)


