from django.db import models
from company.models import Company


class Favourite(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='favourite_company')
    price_field = models.CharField(max_length=10)
    minimum_limit = models.FloatField()
    maximum_limit = models.FloatField()
    trader_user_id = models.IntegerField()
