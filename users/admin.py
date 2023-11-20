from django.contrib import admin
from users.models import Customer, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'password', 'is_staff', 'is_active', 'user_type', 'last_login', 'date_joined',  ]


@admin.register(Customer)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'profile_image', 'full_name', 'address', 'is_new',  'pin_code', 'user' ]

# @admin.register(OTPManager)
# class myapp(admin.ModelAdmin):
#     list_display = ['id', 'email', 'otp', ]