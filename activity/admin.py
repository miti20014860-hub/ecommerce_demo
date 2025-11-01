# admin.py
from .models import Activity, ActivityImage, Booking
from django.utils.html import format_html
from django.contrib import admin


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
        'title',
        'type',
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
                'is_appointment',
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


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('activity', 'get_full_name', 'email', 'prefer_date', 'created_at', 'user')
    list_filter = ('activity', 'prefer_date', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'activity', 'user__username', 'user__email')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
    get_full_name.short_description = "Name"
    get_full_name.admin_order_field = 'first_name'

    # 可選：限制非 superuser 只能看自己的預約
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
