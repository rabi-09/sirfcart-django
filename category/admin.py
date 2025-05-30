from django.contrib import admin
from .models import Category

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug':('name',)}
    list_display = ('name', 'category_slug')

admin.site.register(Category, categoryAdmin)