from django.db import models
from django.utils.translation import gettext_lazy as _


class Activity(models.Model):
    # === 基本資訊 ===
    title = models.TextField(
        verbose_name=_("Title (Very Very Very Very Very Very Very Long)")
    )

    minimum_charge = models.CharField(
        max_length=100,
        verbose_name=_("Minimum Charge"),
    )

    CURRENCY_CHOICES = [
        ('JPY', '¥ JPY'),
        ('USD', '$ USD'),
        ('EUR', '€ EUR'),
    ]
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='JPY',
        verbose_name=_("Currency")
    )

    help_text = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Help Text"),
        help_text=_("Additional guidance or notes for customers")
    )

    price_included = models.TextField(
        blank=True,
        verbose_name=_("Price Included"),
        help_text=_("What is included in the price (e.g., meals, equipment)")
    )

    provider = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Provider"),
        help_text=_("Company or person offering the activity")
    )

    location = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Location"),
        help_text=_("General area or venue name")
    )

    participants = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Participants"),
        help_text=_("Possible number of bookings")
    )

    participating_age = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Participating Age"),
        help_text=_("e.g., 6+, 18+, All ages")
    )

    duration = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Duration"),
        help_text=_("e.g., 2 hours, Half day, 3 days")
    )

    # === 內容描述 ===
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Full description of the activity")
    )

    plan_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 1"),
        help_text=_("Package options")
    )

    price_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 1"),
        help_text=_("Pricing tiers")
    )

    summary_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 1"),
        help_text=_("Short highlight or tagline")
    )
    plan_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 2"),
        help_text=_("Package options")
    )

    price_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 2"),
        help_text=_("Pricing tiers")
    )

    summary_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 2"),
        help_text=_("Short highlight or tagline")
    )

    plan_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 3"),
        help_text=_("Package options")
    )

    price_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 3"),
        help_text=_("Pricing tiers")
    )

    summary_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 3"),
        help_text=_("Short highlight or tagline")
    )

    min_p = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Min. P"),
        help_text=_("Minimum required to run the activity")
    )

    period = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Period"),
        help_text=_("e.g., Year-round, Summer only")
    )

    deadline = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("Deadline"),
        help_text=_("Booking deadline")
    )

    # === 地圖資訊 ===
    lat = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("Latitude")
    )
    lng = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("Longitude")
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Address")
    )
    map_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Map ID"),
        help_text=_("Google Maps Place ID or custom ID")
    )

    # === 圖片管理（多圖）===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def main_image(self):
        return self.images.first()

    @property
    def main_image_url(self):
        img = self.main_image
        return img.image.url if img and img.image else None


# === 圖片模型（關聯式）===
class ActivityImage(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("Activity")
    )
    image = models.ImageField(
        upload_to='activities/%Y/%m/%d/',
        verbose_name=_("Image")
    )
    caption = models.CharField(
        max_length=200, blank=True,
        verbose_name=_("Caption")
    )
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = _("Activity Image")
        verbose_name_plural = _("Activity Images")

    def __str__(self):
        return f"{self.activity.title} - {self.caption or 'Image'}"
