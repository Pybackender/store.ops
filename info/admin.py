from django.contrib import admin

from info.models import Info

# Register your models here.
@admin.register(Info)
class TagAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone','email']