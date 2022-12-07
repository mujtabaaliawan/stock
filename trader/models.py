from user.models import User
from django.db import models


class Trader(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20, default='0')
