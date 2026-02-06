from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Activity(models.Model):
    Type_CHOICES = [
        ('hands_on', 'Hands-on'),
        ('performance', 'Performance'),
        ('exhibition', 'Exhibition'),
        ('workshop', 'Workshop'),
        ('lecture', 'Lecture')
    ]
    type = models.CharField(
        max_length=20,
        choices=Type_CHOICES,
        verbose_name=_("activity type")
    )

    title = models.TextField(verbose_name=_("title"))

    Appointment_CHOICES = [
        ('yes', 'Yes'), ('no', 'No')
    ]
    is_appointment = models.CharField(
        max_length=10,
        choices=Appointment_CHOICES,
        verbose_name=_("is appointment")
    )

    fee_details = models.CharField(
        max_length=100,
        verbose_name=_("fee details")
    )

    CURRENCY_CHOICES = [('JPY', '¥ JPY'), ('USD', '$ USD'), ('EUR', '€ EUR'),]
    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        verbose_name=_("currency")
    )

    minimum_charge = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name=_("minimum charge")
    )

    price_included = models.TextField(
        default="－",
        verbose_name=_("price included")
    )
    provider = models.CharField(
        max_length=100,
        verbose_name=_("provider")
    )
    participants = models.CharField(
        max_length=50,
        default="－",
        verbose_name=_("participants")
    )
    participating_age = models.CharField(
        max_length=50,
        default="－",
        verbose_name=_("participating Age")
    )
    duration = models.CharField(
        max_length=100,
        default="－",
        verbose_name=_("duration")
    )
    description = models.TextField(
        verbose_name=_("description")
    )
    plan_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("plan 1")
    )
    price_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("price 1")
    )
    summary_1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("summary 1")
    )
    plan_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("plan 2")
    )
    price_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("price 2")
    )
    summary_2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("summary 2")
    )
    plan_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("plan 3")
    )
    price_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("price 3")
    )
    summary_3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("summary 3")
    )
    min_p = models.CharField(
        max_length=100,
        default="－",
        verbose_name=_("min participants")
    )
    reg_deadline = models.CharField(
        max_length=100,
        default="－",
        verbose_name=_("deadline")
    )
    event_ends = models.DateField(
        verbose_name=_("event ends")
    )

    HOKKAIDO = [
        ('hokkaido', 'Hokkaido')
    ]
    TOHOKU = [
        ('aomori', 'Aomori'),
        ('iwate', 'Iwate'),
        ('miyagi', 'Miyagi'),
        ('akita', 'Akita'),
        ('yamagata', 'Yamagata'),
        ('fukushima', 'Fukushima')
    ]
    KANTO = [
        ('ibaraki', 'Ibaraki'),
        ('tochigi', 'Tochigi'),
        ('gunma', 'Gunma'),
        ('saitama', 'Saitama'),
        ('chiba', 'Chiba'),
        ('tokyo', 'Tokyo'),
        ('kanagawa', 'Kanagawa')
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
        ('aichi', 'Aichi')
    ]
    KANSAI = [
        ('mie', 'Mie'),
        ('shiga', 'Shiga'),
        ('kyoto', 'Kyoto'),
        ('osaka', 'Osaka'),
        ('hyogo', 'Hyogo'),
        ('nara', 'Nara'),
        ('wakayama', 'Wakayama')
    ]
    CHUGOKU = [
        ('tottori', 'Tottori'),
        ('shimane', 'Shimane'),
        ('okayama', 'Okayama'),
        ('hiroshima', 'Hiroshima'),
        ('yamaguchi', 'Yamaguchi')
    ]
    SHIKOKU = [
        ('tokushima', 'Tokushima'),
        ('kagawa', 'Kagawa'),
        ('ehime', 'Ehime'),
        ('kochi', 'Kochi')
    ]
    KYUSHU_OKINAWA = [
        ('fukuoka', 'Fukuoka'),
        ('saga', 'Saga'),
        ('nagasaki', 'Nagasaki'),
        ('kumamoto', 'Kumamoto'),
        ('oita', 'Oita'),
        ('miyazaki', 'Miyazaki'),
        ('kagoshima', 'Kagoshima'),
        ('okinawa', 'Okinawa')
    ]
    PREFECTURE_CHOICES = (HOKKAIDO + TOHOKU + KANTO +
                          CHUBU + KANSAI + CHUGOKU + SHIKOKU + KYUSHU_OKINAWA)

    prefecture = models.CharField(
        max_length=20,
        choices=PREFECTURE_CHOICES,
        verbose_name=_("prefecture")
    )

    lat = models.CharField(
        max_length=20,
        verbose_name=_("latitude")
    )
    lng = models.CharField(
        max_length=20,
        verbose_name=_("longitude")
    )
    address = models.CharField(
        max_length=100,
        verbose_name=_("address")
    )
    map_id = models.CharField(
        max_length=100,
        verbose_name=_("map id")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _("activity")
        verbose_name_plural = _("activities")

    def __str__(self):
        return f"{self.created_at} - {self.title}"


class ActivityImage(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("activity images")
    )
    image = models.ImageField(
        upload_to='activities/%Y/%m/%d/',
        verbose_name=_("image")
    )
    caption = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_("caption")
    )
    order = models.PositiveIntegerField(
        db_index=True,
        verbose_name=_("order")
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("activity image")
        verbose_name_plural = _("activity images")

    def __str__(self):
        return f"{self.order} - {self.activity.title} - {self.caption}"


class Booking(models.Model):
    activity = models.CharField(
        max_length=200,
        verbose_name=_("activity")
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("last name")
    )
    email = models.EmailField(
        max_length=100,
        verbose_name=_("email address")
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("phone number")
    )
    prefer_date = models.DateField(
        verbose_name=_("preferred date")
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("comment")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("submitted at")
    )
    activity_obj = models.ForeignKey(
        'Activity',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='bookings'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='bookings',
        verbose_name=_("user")
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.activity}"

    def save(self, *args, **kwargs):
        if self.activity_obj and not self.activity:
            self.activity = self.activity_obj.title
        super().save(*args, **kwargs)
