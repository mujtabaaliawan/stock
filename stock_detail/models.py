from django.db import models
from company.models import Company


class StockDetail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_price')
    ldcp = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    current = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    date_time = models.DateTimeField()
    is_latest = models.BooleanField(default=False)

    class Meta:
        ordering = ['company_id']
        constraints = [
            models.UniqueConstraint(fields=['company', 'is_latest'],
                                    name='unique_price')
        ]

