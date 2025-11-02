from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models


class Collection(models.Model):
    TYPE_CHOICES = [
        ('katana', 'Katana'),
        ('tachi', 'Tachi'),
        ('wakizashi', 'Wakizashi'),
        ('kodachi', 'Kodachi'),
        ('tanto', 'Tanto'),
    ]

    CURRENCY_CHOICES = [('JPY', '¥ JPY'), ('USD', '$ USD'), ('EUR', '€ EUR')]
    _CURRENCY_SYMBOLS = dict(CURRENCY_CHOICES)

    name_jp = models.CharField(max_length=100, verbose_name="Name (JP)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    provider = models.CharField(max_length=100, verbose_name="Provider")
    signature = models.CharField(max_length=100, verbose_name="Signature (Mei)")

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type")
    blade_length = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name="Blade Length (cm)")
    curvature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Curvature (cm)")
    sword_weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Sword Weight (g)")

    motohaba = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Motohaba (cm)")
    sakihaba = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Sakihaba (cm)")
    motogasane = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Motogasane (cm)")
    sakigasane = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Sakigasane (cm)")

    PERIOD_CHOICES = [('koto', 'Koto'), ('chūkoto', 'Chūkoto'), ('shinto', 'Shinto'), ('gendai_to', 'Gendai-to')]
    period_type = models.CharField(max_length=20, choices=PERIOD_CHOICES, verbose_name="Period Type",
                                   help_text=("pre-1500, 1500~1596, 1596~1867, 1868~"))
    period = models.CharField(max_length=100, verbose_name="Period")
    koshirae = models.CharField(max_length=100, verbose_name="Koshirae")

    registration = models.CharField(max_length=100, null=True, blank=True, verbose_name="Registration")
    certificate = models.CharField(max_length=100, null=True, blank=True, verbose_name="Certificate")

    remarks = models.TextField(verbose_name="Remarks")

    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='JPY', verbose_name="Currency")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
        ordering = ['-created_at', 'name_en']

    def __str__(self):
        return self.name_en or self.name_jp or "Unnamed Collection"

    def formatted_price(self):
        if self.price is not None:
            price_int = int(self.price)
            return f"{price_int:,} {self.currency}"
        return "-"
    formatted_price.short_description = "Price"

    @property
    def main_image_url(self):
        img = self.images.order_by('order').first()
        return img.image.url if img and img.image else None


class CollectionImage(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='collections/%Y/%m/%d/', verbose_name="Image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Caption")
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Collection Image"
        verbose_name_plural = "Collection Images"

    def __str__(self):
        return f"{self.collection} - {self.caption or 'Image'}"


class Order(models.Model):
    User = get_user_model()
    PAYMENT_CHOICES = [
        ('wire_transfer', 'Wire Transfer'),
        ('credit_card', 'Credit Card'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='wire_transfer')
    item_order = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    delivery_address = models.TextField()
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    comment = models.TextField(blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    item = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    item_order = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.short_description = "Customer"

    def payment_display(self):
        return dict(self.PAYMENT_CHOICES).get(self.payment_method, self.payment_method)
    payment_display.short_description = "Payment Method"

    def save(self, *args, **kwargs):
        if self.item and not self.item_order:
            self.item_order = self.item.name_en
        super().save(*args, **kwargs)
