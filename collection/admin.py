from django.contrib import admin
from django.utils.html import format_html
from .models import Collection, CollectionImage, Order


class CollectionImageInline(admin.StackedInline):
    model = CollectionImage
    extra = 0
    min_num = 1
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
    list_display = ('name_en', 'name_jp', 'type', 'provider', 'updated_at')
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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'item_order',
        'payment_method',
        'email_address',
        'created_at',
        'user_link',
    ]
    list_filter = ['payment_method', 'created_at']
    search_fields = [
        'item_order', 'first_name', 'last_name',
        'email_address', 'phone_number', 'delivery_address'
    ]
    readonly_fields = ['created_at', 'user', 'item_order']
    fieldsets = (
        ("Customer Info", {
            'fields': ('user', 'first_name', 'last_name', 'email_address', 'phone_number')
        }),
        ("Order Details", {
            'fields': ('item_order', 'payment_method', 'delivery_address', 'comment')
        }),
        ("Metadata", {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def user_link(self, obj):
        if obj.user:
            url = f"/admin/auth/user/{obj.user.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.user.username)
        return "-"
    user_link.short_description = "User"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True
