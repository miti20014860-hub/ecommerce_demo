from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from django.db import models


class Activity(models.Model):
    # === 基本資訊 ===
    Type_CHOICES = [
        ('hands_on', 'Hands-on'),
        ('performance', 'Performance'),
        ('exhibition', 'Exhibition'),
        ('lecture', 'Lecture'),
        ('workshop', 'Workshop')
    ]
    type = models.CharField(
        max_length=20,
        choices=Type_CHOICES,
        verbose_name="Activity Type"
    )

    title = models.TextField(
        verbose_name=_("Title (Very Very Very Very Very Very Very Long)")
    )

    minimum_charge = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Minimum Charge")

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
        verbose_name=_("Provider"),
        help_text=_("Company or person offering the activity")
    )

    participants = models.CharField(
        max_length=50,
        verbose_name=_("Participants"),
        help_text=_("Possible number of bookings")
    )

    participating_age = models.CharField(
        max_length=50,
        verbose_name=_("Participating Age"),
        help_text=_("e.g., 6+, 18+, All ages")
    )

    duration = models.CharField(
        max_length=100,
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
        verbose_name=_("Min. P"),
        help_text=_("Minimum required to run the activity")
    )

    reg_deadline = models.CharField(
        max_length=100,
        verbose_name=_("Deadline"),
        help_text=_("Registration Deadline")
    )

    event_ends = models.DateField(
        verbose_name=_("Event Ends"),
    )

    # === 地圖資訊 ===

    # === 1. Hokkaido ===
    HOKKAIDO = [
        ('hokkaido', 'Hokkaido'),
    ]

    # === 2. Tohoku ===
    TOHOKU = [
        ('aomori', 'Aomori'),
        ('iwate', 'Iwate'),
        ('miyagi', 'Miyagi'),
        ('akita', 'Akita'),
        ('yamagata', 'Yamagata'),
        ('fukushima', 'Fukushima'),
    ]

    # === 3. Kanto ===
    KANTO = [
        ('ibaraki', 'Ibaraki'),
        ('tochigi', 'Tochigi'),
        ('gunma', 'Gunma'),
        ('saitama', 'Saitama'),
        ('chiba', 'Chiba'),
        ('tokyo', 'Tokyo'),
        ('kanagawa', 'Kanagawa'),
    ]

    # === 4. Chubu ===
    CHUBU = [
        ('niigata', 'Niigata'),
        ('toyama', 'Toyama'),
        ('ishikawa', 'Ishikawa'),
        ('fukui', 'Fukui'),
        ('yamanashi', 'Yamanashi'),
        ('nagano', 'Nagano'),
        ('gifu', 'Gifu'),
        ('shizuoka', 'Shizuoka'),
        ('aichi', 'Aichi'),
    ]

    # === 5. Kansai (Kinki) ===
    KANSAI = [
        ('mie', 'Mie'),
        ('shiga', 'Shiga'),
        ('kyoto', 'Kyoto'),
        ('osaka', 'Osaka'),
        ('hyogo', 'Hyogo'),
        ('nara', 'Nara'),
        ('wakayama', 'Wakayama'),
    ]

    # === 6. Chugoku ===
    CHUGOKU = [
        ('tottori', 'Tottori'),
        ('shimane', 'Shimane'),
        ('okayama', 'Okayama'),
        ('hiroshima', 'Hiroshima'),
        ('yamaguchi', 'Yamaguchi'),
    ]

    # === 7. Shikoku ===
    SHIKOKU = [
        ('tokushima', 'Tokushima'),
        ('kagawa', 'Kagawa'),
        ('ehime', 'Ehime'),
        ('kochi', 'Kochi'),
    ]

    # === 8. Kyushu & Okinawa ===
    KYUSHU_OKINAWA = [
        ('fukuoka', 'Fukuoka'),
        ('saga', 'Saga'),
        ('nagasaki', 'Nagasaki'),
        ('kumamoto', 'Kumamoto'),
        ('oita', 'Oita'),
        ('miyazaki', 'Miyazaki'),
        ('kagoshima', 'Kagoshima'),
        ('okinawa', 'Okinawa'),
    ]
    # 組合所有區域
    PREFECTURE_CHOICES = (
        HOKKAIDO +
        TOHOKU +
        KANTO +
        CHUBU +
        KANSAI +
        CHUGOKU +
        SHIKOKU +
        KYUSHU_OKINAWA
    )
    prefecture = models.CharField(
        max_length=20,
        choices=PREFECTURE_CHOICES,
        verbose_name="Prefecture"
    )

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
    # ... 其他欄位

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL Slug"
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

    # === slug ===
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.pk)
        super().save(*args, **kwargs)


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


class Booking(models.Model):
    activity = models.CharField(max_length=200, verbose_name="Activity")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    prefer_date = models.DateField(verbose_name="Preferred Date")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    activity_obj = models.ForeignKey(
        'Activity',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='bookings'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings',
        verbose_name="User",
    )

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.activity}"

    def save(self, *args, **kwargs):
        if self.activity_obj and not self.activity:
            self.activity = self.activity_obj.title
        super().save(*args, **kwargs)
