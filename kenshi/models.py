from django.db import models
from django.utils.translation import gettext_lazy as _


class Kenshi(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )

    date = models.DateField(
        verbose_name=_("date")
    )

    contents_main = models.TextField(
        blank=True,
        verbose_name=_("contents main")
    )

    subtitle_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 1")
    )
    contents_1 = models.TextField(
        blank=True,
        verbose_name=_("contents 1")
    )

    video = models.FileField(
        upload_to='kenshi/videos/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name=_("video file"),
        help_text=_("Upload MP4 file (max 100MB recommended)")
    )

    @property
    def youtube_id(self):
        if not self.video:
            return None
        import re
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        for pattern in patterns:
            match = re.search(pattern, self.video)
            if match:
                return match.group(1)
        return None

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("kenshi")
        verbose_name_plural = _("kenjutsuka")
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.date}"

    @property
    def main_image(self):
        return self.images.first()

    @property
    def main_image_url(self):
        img = self.main_image
        return img.image.url if img and img.image else None


class KenshiImage(models.Model):
    kenshi = models.ForeignKey(
        Kenshi, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("kenshi")
    )
    image = models.ImageField(
        upload_to='kenjutsuka/%Y/%m/%d/',
        verbose_name=_("image")
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("caption")
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name=_("order")
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("kenshi image")
        verbose_name_plural = _("kenshi images")

    def __str__(self):
        return f"{self.kenshi.title} - {self.caption or 'Image'}"
