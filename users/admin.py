from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    list_display = ('full_name', 'phone', 'email', 'role', 'is_admin', 'is_active')
    list_filter = ('role', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'password')}),
        (_("Personal info"), {'fields': ('full_name',)}),
        (_("Permissions"), {'fields': ('role', 'is_admin', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone', 'email', 'role', 'password1', 'password2', 'is_admin', 'is_active'),
        }),
    )
    search_fields = ('phone', 'email', 'full_name')
    ordering = ('phone',)


admin.site.register(User, UserAdmin)
