from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Activity(models.Model):
    Type_CHOICES = [
        ('hands_on', 'Hands-on'),
        ('performance', 'Performance'),
        ('exhibition', 'Exhibition'),
        ('lecture', 'Lecture'),
        ('workshop', 'Workshop')
    ]
    type = models.CharField(max_length=20, choices=Type_CHOICES, verbose_name="Activity Type")

    title = models.TextField(verbose_name=_("Title"))

    Appointment_CHOICES = [('yes', 'Yes'), ('no', 'No'),]

    is_appointment = models.CharField(max_length=20, null=True, blank=True, choices=Appointment_CHOICES, verbose_name="Is Appointment")

    minimum_charge = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Minimum Charge")

    CURRENCY_CHOICES = [('JPY', '¥ JPY'), ('USD', '$ USD'), ('EUR', '€ EUR'),]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='JPY', verbose_name=_("Currency"))

    help_text = models.CharField(max_length=100, blank=True, verbose_name=_("Help Text"),)

    price_included = models.TextField(blank=True, verbose_name=_("Price Included"),)

    provider = models.CharField(max_length=100, verbose_name=_("Provider"),)

    participants = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name=_("Participants"),
    )

    participating_age = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name=_("Participating Age"),
    )

    duration = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("Duration"),
    )

    description = models.TextField(
        verbose_name=_("Description"),
    )

    plan_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 1"),
    )

    price_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 1"),
    )

    summary_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 1"),
    )
    plan_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 2"),
    )

    price_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 2"),
    )

    summary_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 2"),
    )

    plan_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Plan 3"),
    )

    price_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Price 3"),
    )

    summary_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Summary 3"),
    )

    min_p = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("Min. P"),
    )

    reg_deadline = models.CharField(
        null=True, blank=True,
        max_length=100,
        verbose_name=_("Deadline"),
    )

    event_ends = models.DateField(
        verbose_name=_("Event Ends"),
    )

    HOKKAIDO = [
        ('hokkaido', 'Hokkaido'),
    ]

    TOHOKU = [
        ('aomori', 'Aomori'),
        ('iwate', 'Iwate'),
        ('miyagi', 'Miyagi'),
        ('akita', 'Akita'),
        ('yamagata', 'Yamagata'),
        ('fukushima', 'Fukushima'),
    ]

    KANTO = [
        ('ibaraki', 'Ibaraki'),
        ('tochigi', 'Tochigi'),
        ('gunma', 'Gunma'),
        ('saitama', 'Saitama'),
        ('chiba', 'Chiba'),
        ('tokyo', 'Tokyo'),
        ('kanagawa', 'Kanagawa'),
    ]

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

    KANSAI = [
        ('mie', 'Mie'),
        ('shiga', 'Shiga'),
        ('kyoto', 'Kyoto'),
        ('osaka', 'Osaka'),
        ('hyogo', 'Hyogo'),
        ('nara', 'Nara'),
        ('wakayama', 'Wakayama'),
    ]

    CHUGOKU = [
        ('tottori', 'Tottori'),
        ('shimane', 'Shimane'),
        ('okayama', 'Okayama'),
        ('hiroshima', 'Hiroshima'),
        ('yamaguchi', 'Yamaguchi'),
    ]

    SHIKOKU = [
        ('tokushima', 'Tokushima'),
        ('kagawa', 'Kagawa'),
        ('ehime', 'Ehime'),
        ('kochi', 'Kochi'),
    ]

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

    PREFECTURE_CHOICES = (HOKKAIDO + TOHOKU + KANTO + CHUBU + KANSAI + CHUGOKU + SHIKOKU + KYUSHU_OKINAWA)

    prefecture = models.CharField(max_length=20, choices=PREFECTURE_CHOICES, verbose_name="Prefecture")

    lat = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Latitude"))

    lng = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Longitude"))

    address = models.CharField(max_length=100, blank=True, verbose_name=_("Address"))

    map_id = models.CharField(max_length=100, blank=True, verbose_name=_("Map ID"), help_text=_("Google Maps Place ID or custom ID"))

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL Slug"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    @property
    def main_image(self):
        return self.images.first()

    @property
    def main_image_url(self):
        img = self.main_image
        return img.image.url if img and img.image else None


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
