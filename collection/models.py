from django.db import models


class Collection(models.Model):
    TYPE_CHOICES = [
        ('katana', 'Katana'),
        ('wakizashi', 'Wakizashi'),
        ('tanto', 'Tanto'),
        ('tachi', 'Tachi'),
        ('naginata', 'Naginata'),
        ('yari', 'Yari'),
        ('other', 'Other'),
    ]

    CURRENCY_CHOICES = [('JPY', '¥ JPY'), ('USD', '$ USD'), ('EUR', '€ EUR')]
    _CURRENCY_SYMBOLS = dict(CURRENCY_CHOICES)

    name_jp = models.CharField(max_length=100, verbose_name="Name (JP)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    provider = models.CharField(max_length=100, blank=True, verbose_name="Provider")
    signature = models.CharField(max_length=100, blank=True, verbose_name="Signature (Mei)")

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='katana', verbose_name="Type")
    blade_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Blade Length (cm)")
    curvature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Curvature (cm)")
    sword_weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Sword Weight (g)")

    motohaba = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Motohaba (cm)")
    sakihaba = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Sakihaba (cm)")
    motogasane = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Motogasane (cm)")
    sakigasane = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Sakigasane (cm)")

    period = models.CharField(max_length=100, blank=True, verbose_name="Period")
    koshirae = models.CharField(max_length=100, blank=True, verbose_name="Koshirae")

    registration = models.CharField(max_length=100, blank=True, verbose_name="Registration")
    certificate = models.CharField(max_length=100, blank=True, verbose_name="Certificate")

    remarks = models.TextField(blank=True, verbose_name="Remarks")

    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Price")
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
