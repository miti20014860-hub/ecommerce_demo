from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("phone")
    )
    payment = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("payment")
    )
    address = models.TextField(
        blank=True,
        verbose_name=_("address")
    )

    def __str__(self):
        return self.username
