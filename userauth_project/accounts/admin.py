from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type','city', 'state', 'pincode', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'user_type',
                'profile_picture',
                'address_line1',
                'city',
                'state',
                'pincode',
            )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
