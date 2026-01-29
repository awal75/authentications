from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # List page
    list_display = ('email', 'role','date_joined', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    readonly_fields = ('date_joined',) 

    # Detail/Edit page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('role',)}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add user page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('email',)
    ordering = ('-date_joined',)

    # Because we removed username field
    filter_horizontal = ('groups', 'user_permissions')
