from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, verbose_name="phone")
    address = models.CharField(max_length=200, blank=True, verbose_name="address")

    def __str__(self):
        return self.username
