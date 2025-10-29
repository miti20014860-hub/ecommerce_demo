# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Activity, ActivityImage


# === 圖片 Inline ===
class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1
    fields = ('image', 'image_preview', 'caption', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 80px; width: auto; object-fit: contain; border: 1px solid #ddd;" />',
                obj.image.url
            )
        return "(No image)"
    image_preview.short_description = "Preview"


# === Activity Admin ===
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'title',
        'min_price',
        'prefecture',
        'provider',
        'participants',
        'reg_deadline',
        'created_at'
    )
    list_filter = (
        'reg_deadline',
        'event_ends',
        'created_at',
    )
    search_fields = (
        'title',
        'provider',
        'location',
        'description',
        'plan',
        'price',
        'summary',
        'address',
        'help_text'
    )
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ActivityImageInline]

    # === 嚴格按照 models.py 欄位順序 ===
    fieldsets = (
        # === 基本資訊 ===
        (("Basic Information"), {
            'fields': (
                'type',
                'title',
                'minimum_charge',
                'currency',
                'help_text',
                'price_included',
                'provider',
                'participants',
                'participating_age',
                'duration',
            )
        }),

        # === 內容描述 ===
        (("Content Description"), {
            'fields': (
                'description',
                'plan_1',
                'price_1',
                'summary_1',
                'plan_2',
                'price_2',
                'summary_2',
                'plan_3',
                'price_3',
                'summary_3',
            ),
            'classes': ('collapse',)
        }),

        # === 預約與時間 ===
        (("Booking & Schedule"), {
            'fields': (
                'min_p',
                'reg_deadline',
                'event_ends',

            ),
            'classes': ('collapse',)
        }),

        # === 地圖資訊 ===
        (("Map Information"), {
            'fields': (
                'prefecture',
                'location',
                ('lat', 'lng'),
                'address',
                'map_id',
            ),
            'classes': ('collapse',)
        }),

        # === 時間戳記 ===
        (("Timestamps"), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # === 價格格式化（整數 + 貨幣符號）===
    def min_price(self, obj):
        if obj.minimum_charge is not None:
            price_int = int(float(obj.minimum_charge))
            return f"{price_int:,} {obj.currency}"
        return "-"
    min_price.admin_order_field = 'minimum_charge'
