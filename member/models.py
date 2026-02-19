from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    first_name = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("last name")
    )
    phone = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name=_("phone")
    )
    payment = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("payment")
    )
    address = models.TextField(
        null=True, blank=True,
        verbose_name=_("address")
    )

    def __str__(self):
        return self.username
