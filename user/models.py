from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role_choices = [
        ("superuser", "superuser"),
        ("trader", "trader")
    ]
    role = models.CharField(max_length=10, choices=role_choices)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'User'
        ordering = ['id']