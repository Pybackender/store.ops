from django.contrib import admin

from about.models import About, Brands, Service

# Register your models here.


@admin.register(About)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Service)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Brands)
class TagAdmin(admin.ModelAdmin):
    list_display = ['image']
