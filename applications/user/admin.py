from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from applications.user.forms import CustomUserChangeForm
from applications.user.models import User


@admin.register(User)
class UsuarioAdmin(UserAdmin):
    form = CustomUserChangeForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and not obj.username:
            obj.username = obj.email.split('@')[0]
        return form
    list_display = ['first_name', 'last_name', 'email', 'username', 'position', 'phone_number', 'is_active', 'last_login']
    list_filter = ['groups', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
    search_fields = ['first_name', 'last_name', 'username', 'email', 'position']

    fieldsets = (
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'username', 'email', 'position', 'phone_number', 'photo')
        }),
        ('Permisos', {
            'fields': ('is_staff', 'is_superuser', 'groups')
        }),
        ('Información de Usuario', {
            'fields': ('password', 'is_active', 'last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'position', 'phone_number', 'photo')
        }),
        ('Permisos', {
            'fields': ('is_staff', 'is_superuser', 'groups')
        }),
        ('Información de Usuario', {
            'fields': ('password1', 'password2', 'is_active')
        }),
    )
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['email']
