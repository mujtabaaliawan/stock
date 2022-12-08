from django.db import models
from category.models import Category


class Company(models.Model):

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='company_category')

    class Meta:
        ordering = ['id']

