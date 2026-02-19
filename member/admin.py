from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Member


@admin.register(Member)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'phone', 'address')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Custom fields'), {'fields': ('phone', 'payment', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Custom fields'), {'fields': ('phone', 'payment', 'address')})
    )
