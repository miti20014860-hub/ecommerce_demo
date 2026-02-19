from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Collection(models.Model):
    TYPE_CHOICES = [
        ('tachi', 'Tachi'),
        ('katana', 'Katana'),
        ('kodachi', 'Kodachi'),
        ('wakizashi', 'Wakizashi'),
        ('tanto', 'Tanto'),
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name=_("type")
    )

    name_jp = models.CharField(
        max_length=100,
        verbose_name=_("name (JP)")
    )
    name_en = models.CharField(
        max_length=100,
        verbose_name=_("name (EN)")
    )

    provider = models.CharField(
        max_length=100,
        verbose_name=_("provider")
    )
    signature = models.CharField(
        max_length=100,
        verbose_name=_("signature (Mei)")
    )

    CURRENCY_CHOICES = [
        ('JPY', '¥ JPY'),
        ('USD', '$ USD'),
        ('EUR', '€ EUR')
    ]
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        verbose_name=_("currency")
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name=_("price")
    )

    blade_length = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("blade length (cm)")
    )
    curvature = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("curvature (cm)")
    )
    sword_weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("sword weight (g)")
    )

    motohaba = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("motohaba (cm)")
    )
    sakihaba = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("sakihaba (cm)")
    )
    motogasane = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("motogasane (cm)")
    )
    sakigasane = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("sakigasane (cm)")
    )

    PERIOD_CHOICES = [
        ('koto', 'Koto'),
        ('chūkoto', 'Chūkoto'),
        ('shinto', 'Shinto'),
        ('gendaito', 'Gendaito')
    ]
    period_type = models.CharField(
        max_length=20,
        choices=PERIOD_CHOICES,
        verbose_name=_("period type"),
        help_text=_("pre-1500, 1500~1596, 1596~1867, 1868~")
    )
    period = models.CharField(
        max_length=100,
        verbose_name=_("period")
    )

    koshirae = models.CharField(
        max_length=100,
        default="Shirasaya",
        verbose_name=_("koshirae")
    )
    registration = models.CharField(
        max_length=100,
        default="－",
        verbose_name=_("registration")
    )
    certificate = models.CharField(
        max_length=100,
        default="－",
        verbose_name=_("certificate")
    )
    remarks = models.TextField(
        default="－",
        verbose_name=_("remarks")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("collection")
        verbose_name_plural = _("collections")

    def __str__(self):
        return f"{self.created_at} - {self.name_jp}"


class CollectionImage(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_("activity images")
    )
    image = models.ImageField(
        upload_to='collections/%Y/%m/%d/',
        verbose_name=_("image")
    )
    caption = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_("caption")
    )
    order = models.PositiveIntegerField(
        db_index=True,
        verbose_name=_("order")
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("collection image")
        verbose_name_plural = _("collection images")

    def __str__(self):
        return f"{self.order} - {self.collection.name_jp} - {self.caption}"


class Order(models.Model):
    name_jp = models.CharField(
        max_length=100,
        verbose_name=_("name (JP)")
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
        verbose_name=_("phone number")
    )
    payment = models.CharField(
        max_length=100,
        verbose_name=_("payment method")
    )
    address = models.TextField(
        verbose_name=_("delivery address")
    )
    comment = models.TextField(
        null=True, blank=True,
        verbose_name=_("comment")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("submitted at")
    )
    collection_id = models.CharField(
        max_length=10,
        verbose_name=_("collection id")
    )
    collection_obj = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders',
        verbose_name=_("user")
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.created_at} - {self.first_name} - {self.name_jp}"

    def save(self, *args, **kwargs):
        if self.collection_obj and not self.name_jp:
            self.name_jp = self.collection_obj.name_jp
        elif self.collection_obj and not self.collection_id:
            self.collection_id = self.collection_obj.pk
        super().save(*args, **kwargs)
