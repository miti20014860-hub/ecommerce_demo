from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    image = models.ImageField(
        upload_to='banners/',
        verbose_name=_("banner image")
    )
    caption = models.CharField(
        max_length=60,
        null=True, blank=True,
        verbose_name=_("caption")
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("banner")
        verbose_name_plural = _("banners")

    def __str__(self):
        return f"{self.created_at} - {self.caption}"


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )
    contents_main = models.TextField(
        null=True, blank=True,
        verbose_name=_("contents main")
    )

    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return f"{self.created_at} - {self.title}"


class NewsImage(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("news images")
    )
    image = models.ImageField(
        upload_to='news/%Y/%m/%d/',
        verbose_name=_("image")
    )
    caption = models.CharField(
        max_length=60,
        null=True, blank=True,
        verbose_name=_("caption")
    )
    order = models.PositiveIntegerField(
        db_index=True,
        verbose_name=_("order")
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("news image")
        verbose_name_plural = _("news images")

    def __str__(self):
        return f"{self.order} - {self.news.title} - {self.caption}"


class Notice(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )
    contents_main = models.TextField(
        verbose_name=_("contents main")
    )
    subtitle_1 = models.CharField(
        max_length=40,
        null=True, blank=True,
        verbose_name=_("subtitle 1")
    )
    contents_1 = models.TextField(
        null=True, blank=True,
        verbose_name=_("contents 1")
    )
    subtitle_2 = models.CharField(
        max_length=40,
        null=True, blank=True,
        verbose_name=_("subtitle 2")
    )
    contents_2 = models.TextField(
        null=True, blank=True,
        verbose_name=_("contents 2")
    )
    lat = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name=_("latitude")
    )
    lng = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name=_("longitude")
    )
    address = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("address")
    )
    map_id = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("map id")
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("notice")
        verbose_name_plural = _("notices")

    def __str__(self):
        return f"{self.created_at} - {self.title}"


class NoticeImage(models.Model):
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("notice images")
    )
    image = models.ImageField(
        upload_to='notice/%Y/%m/%d/',
        verbose_name=_("image")
    )
    caption = models.CharField(
        max_length=60,
        null=True, blank=True,
        verbose_name=_("caption")
    )
    order = models.PositiveIntegerField(
        db_index=True,
        verbose_name=_("order")
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("notice image")
        verbose_name_plural = _("notice images")

    def __str__(self):
        return f"{self.order} - {self.notice.title} - {self.caption}"


class Quote(models.Model):
    author = models.CharField(
        max_length=40,
        verbose_name=_("author")
    )
    content = models.TextField(
        verbose_name=_("contents")
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")

    def __str__(self):
        return f"{self.created_at} - {self.author}"
