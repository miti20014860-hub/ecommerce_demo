from django.contrib import admin
from django.utils.html import format_html
from .models import Kenshi


@admin.register(Kenshi)
class KenshiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('image_preview', 'video_preview', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),

        ('Image', {
            'fields': ('image', 'image_preview')
        }),

        ('Video', {
            'fields': ('video', 'video_preview')
        }),

        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '''
                <video width="100%" height="240" controls style="max-width: 500px; border-radius: 4px;">
                    <source src="{}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <br>
                <small class="text-muted">File: {}</small>
                ''',
                obj.video.url, obj.video.name.split('/')[-1]
            )
        return "(No video uploaded)"

    def image_preview(self, obj):
        if obj.image.url:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto; border-radius: 4px;" />',
                obj.image.url
            )
        return "(No main image)"
