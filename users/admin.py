from django.contrib import admin

from basket.admin import BasketTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

    inlines = [BasketTabAdmin, OrderTabulareAdmin]