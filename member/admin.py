# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)

    # 編輯頁面：分組欄位
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('phone', 'address'),
        }),
    )

    # 新增使用者時的欄位
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('phone', 'address'),
        }),
    )
