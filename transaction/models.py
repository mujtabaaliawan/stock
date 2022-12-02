from django.db import models
from category.models import Category
from company.models import Company


class Transaction(models.Model):

    nature = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='transaction_company')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transaction_category')
    volume = models.FloatField()
    current_price = models.FloatField()


