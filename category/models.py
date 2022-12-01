from django.db import models
from company.models import Company


class Category(models.Model):

    name = models.CharField(max_length=255)
    company = models.ManyToManyField(Company, blank=True)
