from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    payment = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username if self.user else f"Profile {self.pk}"
