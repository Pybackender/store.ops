from django.contrib import admin

from home.models import Home

# Register your models here.
@admin.register(Home)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject']