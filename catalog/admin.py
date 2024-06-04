from django.contrib import admin

from .models import Products, Suppliers


admin.site.register(Suppliers)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}