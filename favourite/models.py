from django.db import models
from company.models import Company


class Favourite(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='favourite_company')
    field_choices = (
        ("ldcp", "ldcp"),
        ("open", "open"),
        ("high", "high"),
        ("low", "low"),
        ("current", "current"),
        ("change", "change"),
        ("volume", "volume")
    )
    price_field = models.CharField(max_length=10, choices= field_choices,default="current")
    minimum_limit = models.FloatField()
    maximum_limit = models.FloatField()
    trader_user_id = models.IntegerField()
