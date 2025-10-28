from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    # === 基本資訊 ===
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

    # === 內容區塊 1 ===
    subtitle_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 1")
    )
    contents_1 = models.TextField(
        blank=True,
        verbose_name=_("contents 1")
    )

    # === 內容區塊 2 ===
    subtitle_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 2")
    )
    contents_2 = models.TextField(
        blank=True,
        verbose_name=_("contents 2")
    )

    # === 地圖資訊 ===
    lat = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("latitude")
    )
    lng = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("longitude")
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("address")
    )
    map_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("map id"),
        help_text=_("Google Maps Place ID or custom ID")
    )

    # === 時間戳記 ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("newses")
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


# === 圖片模型（多圖管理）===
class NewsImage(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("news")
    )
    image = models.ImageField(
        upload_to='newses/%Y/%m/%d/',
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
        verbose_name = _("news image")
        verbose_name_plural = _("news images")

    def __str__(self):
        return f"{self.news.title} - {self.caption or 'Image'}"


class Notice(models.Model):
    # === 基本資訊 ===
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )
    date = models.DateField(
        verbose_name=_("date")
    )

    # === 內容區塊 1 ===
    subtitle_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 1")
    )
    contents_1 = models.TextField(
        blank=True,
        verbose_name=_("contents 1")
    )

    # === 內容區塊 2 ===
    subtitle_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 2")
    )
    contents_2 = models.TextField(
        blank=True,
        verbose_name=_("contents 2")
    )

    # === 內容區塊 3 ===
    subtitle_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("subtitle 3")
    )
    contents_3 = models.TextField(
        blank=True,
        verbose_name=_("contents 3")
    )

    # === 地圖資訊 ===
    lat = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("latitude")
    )
    lng = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("longitude")
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("address")
    )
    map_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("map id"),
        help_text=_("Google Maps Place ID or custom ID")
    )

    # === 時間戳記 ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("notice")
        verbose_name_plural = _("notices")
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


# === 圖片模型（多圖管理）===
class NoticeImage(models.Model):
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("notice")
    )
    image = models.ImageField(
        upload_to='notices/%Y/%m/%d/',
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
        verbose_name = _("notice image")
        verbose_name_plural = _("notice images")

    def __str__(self):
        return f"{self.notice.title} - {self.caption or 'Image'}"
