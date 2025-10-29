# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Collection, CollectionImage


# Inline 讓圖片可以在 Collection 編輯頁面內管理
class CollectionImageInline(admin.TabularInline):
    model = CollectionImage
    extra = 1  # 預設顯示 1 個空白上傳欄
    fields = ('image', 'image_preview', 'caption', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 80px; width: auto; object-fit: contain;" />',
                obj.image.url
            )
        return "(No image)"
    image_preview.short_description = "Preview"


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_jp', 'type', 'formatted_price', 'provider', 'created_at')
    list_filter = ('type', 'currency', 'provider', 'created_at')
    search_fields = ('name_en', 'name_jp', 'provider', 'signature', 'period', 'registration', 'certificate')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CollectionImageInline]

    fieldsets = (
        (None, {
            'fields': ('name_jp', 'name_en', 'provider', 'signature')
        }),
        ('Sword Details', {
            'fields': (
                'type', 'blade_length', 'curvature', 'sword_weight',
                ('motohaba', 'sakihaba'), ('motogasane', 'sakigasane')
            ),
            'classes': ('collapse',)
        }),
        ('History & Description', {
            'fields': ('period_type', 'period', 'koshirae', 'registration', 'certificate', 'remarks'),
            'classes': ('collapse',)
        }),
        ('Price', {
            'fields': ('price', 'currency'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # 讓 formatted_price 能在列表中顯示
    def formatted_price(self, obj):
        return obj.formatted_price()
    formatted_price.short_description = "Price"
    formatted_price.admin_order_field = 'price'
