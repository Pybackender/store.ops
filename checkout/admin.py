from django.contrib import admin

from checkout.models import Checkout

# Register your models here.
@admin.register(Checkout)
class Checkoutadmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email','country','total_price']
