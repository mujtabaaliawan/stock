from django.db import models
from company.models import Company


class Price(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_price')
    ldcp = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    current = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    date_time = models.DateTimeField()

