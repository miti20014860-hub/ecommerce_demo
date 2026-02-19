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
        'name_jp', 'get_full_name', 'email',
        'payment', 'created_at', 'user_link',
    ]
    list_filter = ['name_jp', 'payment', 'created_at']
    search_fields = [
        'name_jp', 'first_name', 'last_name',
        'email', 'phone', 'address'
    ]
    readonly_fields = ['created_at',]
    fieldsets = (
        ("Customer Info", {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone')
        }),
        ("Order Details", {
            'fields': ('name_jp', 'payment', 'address', 'comment')
        }),
        ("Metadata", {
            'fields': ('created_at',)
        }),
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
    get_full_name.short_description = "Name"

    def user_link(self, obj):
        if obj.user:
            url = f"/admin/auth/user/{obj.user.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.user.username)
        return "-"
    user_link.short_description = "User"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
