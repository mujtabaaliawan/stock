from user.models import User
from django.db import models


class Manager(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='manager')
    mobile_number = models.CharField(max_length=20, default='0')
