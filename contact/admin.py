from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id',
    search_fields = 'id', 'first_name', 'last_name'
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    ordering = 'id',
    
    
