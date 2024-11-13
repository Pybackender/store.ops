from django.contrib import admin

from showcase.models import Category, Product

# Register your models here.
@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(Product)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}