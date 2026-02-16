from django.db import models
from django.utils.translation import gettext_lazy as _


class Kenshi(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )

    content = models.TextField(
        verbose_name=_("content")
    )

    image = models.ImageField(
        upload_to='kenjyutsuka/images/%Y/%m/%d/',
        verbose_name=_("image")
    )

    video = models.FileField(
        upload_to='kenjyutsuka/videos/%Y/%m/%d/',
        verbose_name=_("video")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("kenshi")
        verbose_name_plural = _("kenjyutsuka")

    def __str__(self):
        return f"{self.created_at} - {self.title}"
