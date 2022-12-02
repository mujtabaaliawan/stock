from user.models import User
from django.db import models
from transaction.models import Transaction
from favourite.models import Favourite


class Manager(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='trader')
    mobile_number = models.CharField(max_length=20, default='0')
    record = models.ManyToManyField(Transaction, blank=True)
    favourite = models.ManyToManyField(Favourite, blank=True)
