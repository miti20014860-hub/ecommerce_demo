from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
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
        blank=True,
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
    User = get_user_model()

    item_order = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=100)
    delivery_address = models.TextField()
    comment = models.TextField(blank=True)

    item = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.item and not self.item_order:
            self.item_order = self.item.name_en
        super().save(*args, **kwargs)
