# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Kenshi, KenshiImage


# === 圖片 Inline ===
class KenshiImageInline(admin.TabularInline):
    model = KenshiImage
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


# === Kenshi Admin ===
@admin.register(Kenshi)
class KenshiAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'has_video', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('title', 'contents_main', 'subtitle_1', 'contents_1')
    inlines = [KenshiImageInline]
    readonly_fields = ('created_at', 'updated_at', 'video_preview', 'main_image_preview')

    # === 嚴格按照 models.py 欄位順序 ===
    fieldsets = (
        # === 基本資訊 ===
        (None, {
            'fields': ('title', 'date', 'contents_main')
        }),

        # === 內容區塊 1 ===
        ('Content Block 1', {
            'fields': ('subtitle_1', 'contents_1'),
            'classes': ('collapse',)
        }),

        # === 影片上傳 + 預覽 ===
        ('Video', {
            'fields': ('video', 'video_preview'),
            'description': 'Upload MP4 file (recommended: <100MB, 720p)',
            'classes': ('collapse',)
        }),

        # === 圖片預覽 ===
        ('Main Image Preview', {
            'fields': ('main_image_preview',),
            'classes': ('collapse',)
        }),

        # === 時間戳記 ===
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # === 列表頁：是否有影片 ===
    def has_video(self, obj):
        return bool(obj.video)
    has_video.boolean = True
    has_video.short_description = "Video"

    # === 編輯頁：影片預覽 ===
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
    video_preview.short_description = "Video Preview"

    # === 編輯頁：主圖預覽 ===
    def main_image_preview(self, obj):
        if obj.main_image_url:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto; border-radius: 4px;" />',
                obj.main_image_url
            )
        return "(No main image)"
    main_image_preview.short_description = "Main Image"
