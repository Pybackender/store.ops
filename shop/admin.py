from django.contrib import admin

from shop.models import Categories,Shop

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}




@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'categories']
    prepopulated_fields = {'slug': ('name',)}
