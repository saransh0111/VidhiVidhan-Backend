from django.contrib import admin

from market.models import Products

# Register your models here.

@admin.register(Products)
class myapp(admin.ModelAdmin):
    list_display = ['id', 'product_image', 'product_name', 'price', 'category',  'created', 'modified' ]
