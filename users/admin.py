from django.contrib import admin
from users.models import Customer, OTPManager, Pandit, ShopOwner, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'password', 'is_staff', 'is_active', 'user_type', 'last_login', 'date_joined',  ]


@admin.register(Customer)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'profile_image', 'full_name', 'address', 'is_new',  'pin_code', 'user' ]

@admin.register(Pandit)
class myapp(admin.ModelAdmin):
    list_display = ['name', 'profile_image', 'price' ]

@admin.register(ShopOwner)
class myapp(admin.ModelAdmin):
    list_display = ['shop_name', 'profile_image', 'address', 'description']

admin.site.register(OTPManager)
