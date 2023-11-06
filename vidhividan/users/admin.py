from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

 
# class UserAdmin(BaseUserAdmin):
    
#     fieldsets = (
#         (None, {'fields': ('mobile', 'password', 'last_login', 'user_type')}),
#         ('Permissions', {'fields': (
#             'is_active',
#             'is_staff',
#             'is_superuser',
#             'user_permissions',
#         )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('mobile', 'password1', 'password2','user_type','is_staff', 'is_superuser', 'is_active',)
#             }
#         ),
#     )

#     list_display = ('mobile','is_active', 'is_staff','is_superuser', 'last_login', 'date_joined', 'user_type')
#     list_filter = ('is_staff', 'is_superuser', 'is_active',)
#     search_fields = ['mobile',]
#     ordering = ['id',]
#     filter_horizontal = ('user_permissions',)

admin.site.register(User)