from django.db import models
from company.models import Company
from trader.models import Trader


class Favourite(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='favourite_company')
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='favourite_trader')
    field_choices = (
        ("ldcp", "ldcp"),
        ("open", "open"),
        ("high", "high"),
        ("low", "low"),
        ("current", "current"),
        ("change", "change"),
        ("volume", "volume")
    )
    monitor_field = models.CharField(max_length=10, choices=field_choices, default="current")
    minimum_limit = models.FloatField()
    maximum_limit = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['company', 'trader', 'monitor_field', 'is_active'],
                                    name='unique_favourite')
        ]

