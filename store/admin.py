from django.contrib import admin
from .models import Products
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'product_slug':('product_name',)}

admin.site.register(Products, CategoryAdmin)


