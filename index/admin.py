from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, News, NewsImage, Notice, NoticeImage


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'caption', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_per_page = 20

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; width: auto;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = "Preview"


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ('image', 'image_preview', 'caption', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px; object-fit: contain;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = "Preview"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_featured')
    list_editable = ['is_featured']
    list_filter = ('date', 'created_at')
    search_fields = ('title', 'contents_main')
    inlines = [NewsImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'contents_main', 'is_featured')
        }),
        ('Content 1', {
            'fields': ('subtitle_1', 'contents_1'),
            'classes': ('collapse',)
        }),
        ('Content 2', {
            'fields': ('subtitle_2', 'contents_2'),
            'classes': ('collapse',)
        }),
        ('Map', {
            'fields': (('lat', 'lng'), 'address', 'map_id'),
            'classes': ('collapse',)
        }),
    )


class NoticeImageInline(admin.TabularInline):
    model = NoticeImage
    extra = 1
    fields = ('image', 'image_preview', 'caption', 'order')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 80px; object-fit: contain;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = "Preview"


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('title', 'subtitle_1', 'contents_1', 'address')
    inlines = [NoticeImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'date')
        }),
        ('Content 1', {
            'fields': ('subtitle_1', 'contents_1'),
            'classes': ('collapse',)
        }),
        ('Content 2', {
            'fields': ('subtitle_2', 'contents_2'),
            'classes': ('collapse',)
        }),
        ('Content 3', {
            'fields': ('subtitle_3', 'contents_3'),
            'classes': ('collapse',)
        }),
        ('Map', {
            'fields': (('lat', 'lng'), 'address', 'map_id'),
            'classes': ('collapse',)
        }),
    )
