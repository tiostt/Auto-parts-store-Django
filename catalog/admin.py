from django.contrib import admin

from .models import Products, Suppliers


# admin.site.register(Suppliers)

@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'articul', 'price', 'supplier']
    list_filter = ['supplier']
    search_fields = ['name', 'articul', 'price', 'supplier__name']