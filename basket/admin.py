from django.contrib import admin

from basket.models import Basket


# admin.site.register(Basket)

class BasketTabAdmin(admin.TabularInline):
    model = Basket
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1

    
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestamp']
    list_filter = ['created_timestamp']
    search_fields = ['user', 'product', 'quantity', 'created_timestamp']
    
    